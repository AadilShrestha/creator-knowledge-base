# RMBC II: log

## [2026-11-02] fetch | Raw sources

- Listed and fetched 328/328 files (30,423,838,082 bytes) from MEGA folder `GwRSGa5C`: documents in full, videos audio-only (`_tools/ecomtalent_fetch.py rmbc2`; SSL errors retried, 0 failures).
- Transcribed 120/120 videos (faster-whisper large-v3-turbo, CUDA). Converted 54 documents, unpacked 51 zip archives safely (`_work/ecomtalent/rmbc2/scripts/safe_unzip.py`) and converted 289 of their documents.
- Built the lesson map: 58 lessons, 16 modules, about 2,941 unique video minutes. 13 `._converted.mp4` re-encodes marked `duplicate_of`.

## [2026-11-02] ingest | Lesson pages 01-01 to 05-03 (paused)

- 25 lesson pages written. Paused by the user mid-wave; the stopped writers' pages were checked on resume, and all had complete closing sections.

## [2026-11-03] ingest | Lesson pages, synthesis, validation

- **Lesson pages:** remaining 33 written in two waves (58/58). 386 images in `wiki/assets/stefan-georgi/rmbc-ii/`.
- **Synthesis pages:** `concepts/` 18 · `frameworks/` 13 · `playbooks/` 5 (4 + hub) · `rubrics/` 4 (3 + hub) · `libraries/` 9 (8 + hub: 130 prompts, 149 hooks, 122 teardowns, 96 rewrites, 55 angles, 356 rules, 1,020 benchmarks, templates).
- **Hub pages:** [README](README.md), [index](index.md), [contradictions](contradictions.md) (91 rows from 97 logged bullets), [MERGE-NOTES](MERGE-NOTES.md), [PROGRESS](PROGRESS.md).
- **Manifest:** 313 verified, 15 excluded (13 re-encodes, TikTok video11 re-upload, the 11-01 Part 1 video that is really Part 2).
- **Validation:** links 0 missing. Quotes: 1,924 checked.
  - 1,011 at the cited time.
  - 307 at the cited time under a different video number.
  - 106 elsewhere in the transcript.
  - 500 not in the transcript: screen, doc or ad text plus light paraphrase.
- **Tool changes:**
  - `_tools/course_manifest.py`: handles `.srt` captions and zip archives.
  - `_tools/verify_quotes.py`: reads every video of a lesson and parses `[vN mm:ss]` and `[h:mm:ss]`.
  - `_tools/course_index.py`: handles module-based lesson maps.
- **Source defects:**
  - 11-01 Part 1 video is a Part 2 re-upload, so the lesson comes from captions only.
  - The 15-05 video is the upsell demo, so the email walkthrough comes from captions and docs.
  - TikTok breakdown 4 exists as captions only.
- **⛔ flagged:** invented doctors, testimonials, studies and review counts; disease-cure, drug-comparison and income claims; fake scarcity; Stefan's "it's an editorial" (09-02 53:09) and "This is all made up" (04-02 21:45). All described as course content, marked structure-only, with compliant alternatives.
