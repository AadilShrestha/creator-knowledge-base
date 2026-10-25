---
title: "Tether Lab: ingestion progress"
type: course
creator: sarah-levinger
course: tether-lab
updated: 2026-10-20
---

# Tether Lab: PROGRESS

**Status: complete (summarized + linted).** All 123 source files are accounted for in [manifest.json](manifest.json).

| Count | Value |
|---|---|
| Source files (MEGA `ipoWHTDb`) | 123 (6,075,583,703 bytes) |
| Summarized (mapped to wiki pages) | 119 |
| Excluded | 4 byte-size-identical duplicate videos: 3× "CreativeOS 1 Month Free" promo, 1× Prompt Library tutorial. Each references its canonical file |
| Pending / blocked | 0 / 0 |
| Unique videos transcribed | 38 (~19 h), faster-whisper `large-v3-turbo`, int8_float16 on an RTX 4050 |
| Wiki pages (excl. other courses) | 272 · screenshots and page images: 201 in `wiki/assets/tether-lab/` + PDF page renders |

## How sources were processed
- Docs (HTML/PDF/DOCX/PNG) and lesson videos under 130 MB: full download → `raw/tether-lab/<original path>` (videos kept outside the KB in `D:\resources\_work\tether-lab\video\`).
- Live recordings (16): **audio-only** fetch plus keyframes every 45 s and exact-timestamp frames via `D:\resources\_tools\grab_frames.py`. Full videos were never downloaded.
- Tools (Windows, outside the KB): `D:\resources\_tools\` (`mega_lib.py`, `fetch_audio.py`, `screenshot.py`, `grab_frames.py`, `transcribe.py` + `venv-asr`, `convert_docs.py`, `frames_local.py`, `harvest.py`, `tether_coverage.py`, `lint_links.py`).

## Known limitations
- Machine transcripts. Names were corrected by hand on the wiki pages, but the raw transcripts keep Whisper's errors.
- The May 14 transcript is redacted after 00:56:48 (private post-session conversation).
- Quizzes are Typeform links only. The Prompt Library's "15 more prompts" and several promised resources (TEEP swipe file, qualification cheat sheet) are not in the source.
- The video frames carry a third-party reseller watermark ("VAWZINE VIP").

## Next actions (optional)
- Re-run `python -P D:/resources/_tools/tether_coverage.py` and `lint_links.py` after any edit to verify coverage and links.
- Delete `D:\resources\_work\tether-lab\` (≈2 GB of videos, audio and candidate frames) once no more screenshots are needed. Its audio also contains the redacted private segment.
- Cross-creator synthesis: when the Evolve, Zakaria, RMBC II and Ecomtalent courses are ingested, link their pages into the shared `concepts/`, `frameworks/` and `libraries/` with attribution.
