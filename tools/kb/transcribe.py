"""Local timestamped transcription; Apple Silicon MLX or faster-whisper CPU.

Example: python tools/kb/transcribe.py audio.m4a path/to/lesson --backend mlx
The output prefix creates lesson.txt, lesson.srt, and lesson.json.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path


def timestamp(seconds, srt=False):
    milliseconds = max(0, round(float(seconds) * 1000))
    hours, remainder = divmod(milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, millis = divmod(remainder, 1000)
    base = f"{hours:02}:{minutes:02}:{secs:02}"
    return f"{base},{millis:03}" if srt else base


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def write_outputs(prefix, segments, metadata):
    txt, srt = [], []
    for number, segment in enumerate(segments, 1):
        start, end, text = segment["start"], segment["end"], segment["text"].strip()
        txt.append(f"[{timestamp(start)}] {text}\n")
        srt.append(f"{number}\n{timestamp(start, True)} --> {timestamp(end, True)}\n{text}\n")
    payloads = {
        ".txt": "\n".join(txt),
        ".srt": "\n".join(srt),
        ".json": json.dumps({**metadata, "segments": segments}, ensure_ascii=False, indent=2) + "\n",
    }
    prefix.parent.mkdir(parents=True, exist_ok=True)
    for suffix, content in payloads.items():
        target = Path(str(prefix) + suffix)
        temp = Path(str(target) + ".tmp")
        temp.write_text(content, encoding="utf-8")
        temp.replace(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output_prefix", type=Path)
    parser.add_argument("--backend", choices=["auto", "mlx", "cpu"], default="auto")
    parser.add_argument("--model", help="MLX Hugging Face model ID, or faster-whisper model name")
    parser.add_argument("--language", default=None, help="Language code, e.g. en; omitted means detect")
    parser.add_argument("--source-id", help="Stable manifest source ID for provenance")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"Input file not found: {args.input}")
    apple_silicon = platform.system() == "Darwin" and platform.machine() == "arm64"
    backend = ("mlx" if apple_silicon else "cpu") if args.backend == "auto" else args.backend
    if backend == "mlx" and not apple_silicon:
        parser.error("MLX needs native Apple Silicon macOS. Use --backend cpu on Intel/Windows.")
    model = args.model or ("mlx-community/whisper-large-v3-turbo" if backend == "mlx" else "small")
    metadata = {
        "source_file": args.input.name,
        "source_id": args.source_id,
        "source_sha256": digest(args.input),
        "backend": backend,
        "model": model,
        "requested_language": args.language,
        "machine_generated": True,
    }
    outputs = [Path(str(args.output_prefix) + suffix) for suffix in (".txt", ".srt", ".json")]
    if any(p.exists() for p in outputs) and not args.overwrite:
        try:
            old = json.loads(outputs[-1].read_text(encoding="utf-8"))
        except (OSError, ValueError):
            old = {}
        if all(p.is_file() for p in outputs) and all(old.get(k) == v for k, v in metadata.items()):
            print(f"Skip matching existing transcript: {args.output_prefix}")
            return
        parser.error("Existing outputs differ or are incomplete. Inspect them, then use --overwrite to regenerate.")
    print(f"Transcribing {args.input.name} with {backend}/{model}", flush=True)
    if backend == "mlx":
        import mlx_whisper
        result = mlx_whisper.transcribe(
            str(args.input), path_or_hf_repo=model, language=args.language, verbose=False
        )
        segments = [
            {"start": float(s["start"]), "end": float(s["end"]), "text": s["text"].strip()}
            for s in result["segments"]
        ]
        metadata["detected_language"] = result.get("language")
    else:
        from faster_whisper import WhisperModel
        engine = WhisperModel(model, device="cpu", compute_type="int8")
        iterator, info = engine.transcribe(str(args.input), language=args.language, vad_filter=True, beam_size=5)
        segments = [{"start": float(s.start), "end": float(s.end), "text": s.text.strip()} for s in iterator]
        metadata["detected_language"] = info.language
        metadata["duration_seconds"] = info.duration
    if not segments or not any(s["text"].strip() for s in segments):
        raise RuntimeError("No speech text was produced. Inspect audio and record the blocker.")
    write_outputs(args.output_prefix, segments, metadata)
    print(f"Saved {len(segments)} segments to {args.output_prefix}.[txt|srt|json]")
    print("Review the transcript, recording ending, names, and numbers before marking it verified.")


if __name__ == "__main__":
    main()
