# Evolve Start Here: log

## [2026-10-20] setup | Inventory and course workspace

- Listed all 359 remote files (6,528,942,830 bytes) without downloading course content.
- Created manifest, progress checkpoint, course overview, navigation, and integration notes.
- All ingestion statuses remain pending; instructor attribution remains unverified.

## [2026-11-02] ingest | Evolve Start Here (full course)

- **Sources fetched:** 359/359, 0 failures (134 videos, 175 Skool lesson pages, 32 DOCX, 8 PPTX, 7 XLSX, 3 PDF; 6,528,942,830 bytes inventoried). Documents downloaded in full; videos fetched **audio-only**, with frames grabbed from MEGA on demand (`_tools/ecomtalent_fetch.py evolve-start`, `_tools/ecomtalent_frames.py evolve-start`).
- **Transcription:** 134/134 videos (faster-whisper large-v3-turbo, CUDA), about 1,996 video minutes.
- **Extraction:** 225/225 documents, plus 74 embedded Skool images and 56 linked Google Docs/Sheets/Slides (`raw/evolve/start-here/linked/`, `_extracted/_linked/google/`).
- **Lesson pages:** 175 in `lessons/` (12 sections per `_work/evolve-start/lesson_map.json`), with 568 screenshots in `wiki/assets/evolve/start-here/`.
- **Synthesis pages:** `concepts/` 20 · `frameworks/` 12 · `playbooks/` 5 (4 + hub) · `rubrics/` 3 (2 + hub) · `libraries/` 9 (8 + hub: 165 hooks, 111 angles, 80 teardowns + 7 positioning moves, 71 rewrites, 74 templates, 28 prompts, 649 rules, 215 KPI thresholds).
- **Course hub pages:** [README](README.md) (course hub), [index](index.md), [contradictions](contradictions.md) (93 rows in 12 groups, merged from ~106 logged bullets), [MERGE-NOTES](MERGE-NOTES.md).
- **Validation:** manifest 359/359 verified, all sources mapped to lesson pages. Links: `tools/kb/check_links.py` on 230 files: 0 missing in the hub pages written today; 5 broken targets remain in `index.md` (summaries copied from lesson pages keep lesson-relative paths: `071-…`, `072-…`, `074-…`, `../../copywriting/concepts/market-awareness.md`; they need a `lessons/` or `../copywriting/` prefix). Quotes: `_tools/verify_quotes.py`, 2,287 quoted strings; 1,699 near the cited time, 90 elsewhere in the transcript, 498 not in the transcript (mostly page, doc or screen text).
- **Instructors:** Spencer Pawliw (on screen in L1, 2, 110, 113, 122) and Shaun Eng (on screen in L14, 108, 133, 166, 169, 172, 175; "Sean" in L171); guest Chef Karlo in L130; others unverified.
- **Blockers:** lesson 5's "100+ Hook Templates" Google Sheet (HTTP 401, login required); only rows visible in the recording are transcribed. Screen content outside the grabbed frames isn't captured.
- **⛔ flagged:** L172 ripping and metadata stripping, L90 and L98 ripped raw content, L130 health-claim prompt (P20); described as course content with compliant alternatives, not to be executed.
