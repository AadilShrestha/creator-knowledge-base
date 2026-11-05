# Evolve Start Here: progress

Updated: 2026-11-02.

## Current checkpoint
- **Sources:** 359 files (6,528,942,830 bytes): 134 videos, 175 Skool lesson pages (.html), 32 .docx, 8 .pptx, 7 .xlsx, 3 .pdf.
- **Fetched:** 359/359, 0 failures (`_tools/ecomtalent_fetch.py evolve-start`). Documents were downloaded in full; videos were fetched **audio-only**, with frames grabbed on demand from MEGA (`_tools/ecomtalent_frames.py evolve-start`).
- **Transcribed:** 134/134 (faster-whisper large-v3-turbo, CUDA).
- **Extracted:** 225/225 documents, plus 74 embedded Skool images and 56 linked Google Docs/Sheets/Slides (`raw/evolve/start-here/linked/`, `_extracted/_linked/google/`).
- **Blocked:** lesson 5's "100+ Hook Templates" Google Sheet (HTTP 401, needs a login).
- **Lesson map:** `_work/evolve-start/lesson_map.json` lists 175 lessons in 12 sections, about 1,996 video minutes. Brief: `_work/evolve-start/LESSON-BRIEF.md`. Batches: `_work/evolve-start/batches.json` (21).
- **Lesson pages:** 175/175 written (Sonnet writers, 21 batches), 568 screenshots grabbed from MEGA.
- **Synthesis:** 20 concepts, 12 frameworks, 5 playbooks, 3 rubrics, 9 libraries (Opus); `README.md`, `contradictions.md` (93 rows), `MERGE-NOTES.md`, `index.md`, `log.md`.
- **Validation:** 0 missing link targets (230 files); quote check of 2,287 quoted strings found 1,699 near the cited time, 90 elsewhere and 498 not in the transcript (mostly page/doc/screen text); manifest 359/359 verified.
- **Known issue:** screenshots in lessons 156, 158, 160, 162 and 163 show real creators' names or handles inside the image.
- **Global index:** section added to `knowledge-base/wiki/index.md`.
- **Instructors:** Spencer Pawliw (named on screen L1, L2, L110, L113, L122) and Shaun Eng (L14, L108, L133, L166, L169, L172, L175); others unverified.

## Next action
Done. Creator names and faces blurred in the flagged screenshots (2026-11-05); shared-layer wiring done (see MERGE-NOTES.md).

## Earlier checkpoint (2026-10-20)


- State: **inventory prepared; ingestion not started**.
- Source files: **359**, total bytes: **6,528,942,830**.
- Verified: **0**; pending: **359**; blocked: **0 recorded**; excluded: **0**.
- Downloaded/transcribed/extracted/summarized: **0 each** in this assignment.
- File types: .docx: 32, .html: 175, .mp4: 134, .pdf: 3, .pptx: 8, .xlsx: 7.
- Original file listing is fully captured in [manifest.json](manifest.json). This is not a claim that all external embeds/linked downloads are accessible.
- Instructor attribution: **unverified**.

## Next action

1. Detect the local environment, set up required tools, and verify access to the source MEGA folder.
2. Download into `knowledge-base/raw/evolve/start-here/originals/`, preserving the source-relative tree.
3. Reconcile downloaded names/sizes against the manifest. Record actual failures if any.
4. Pair the first teaching unit's HTML, video, and attachments. Test a short transcription clip, then create one complete sample lesson with evidence and useful visuals.
5. Save this checkpoint, manifest stages, course index, and log after each batch.

## Blockers

Local setup, source downloads, and transcription have not been attempted for this course. Record a blocker only after an actual access, permission, or tool failure.

## Resume

Read root `INGESTION.md`, this checkpoint, and the manifest. Inspect saved work, then process the next pending item. Save exact filenames, next action/command, and counts before stopping.
