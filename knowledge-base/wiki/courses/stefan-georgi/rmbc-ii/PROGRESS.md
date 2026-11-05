# PROGRESS: stefan-georgi / rmbc-ii

Updated: 2026-11-03.

## Current checkpoint
- **State:** ingestion complete. Manifest: 313 verified, 15 excluded, `ingestion_complete: true`.
- **Source:** MEGA folder `GwRSGa5C` ("Stefan Georgi - RMBC II (1)"), 328 files, 30,423,838,082 bytes, in 16 modules. Files: 120 mp4, 103 srt, 51 zip, 38 docx, 15 pdf, 1 pptx.
- **Fetched:** 328/328, 0 failures (`_tools/ecomtalent_fetch.py rmbc2`). Documents were downloaded in full. Videos were fetched **audio-only**, with frames grabbed on demand (`_tools/ecomtalent_frames.py rmbc2`).
- **Transcribed:** 120/120 (faster-whisper large-v3-turbo). The 103 platform captions were used for spellings, and they are the only source for 11-01 Part 1 and the 15-05 email walkthrough.
- **Extracted:** 54/54 top-level documents and 51 zip archives (409 files unpacked; 289 documents converted to `_extracted/_unzipped/`). Some saved landing-page HTML extracted nearly empty, so writers parsed the originals instead (12-02, 13-01, 14-02).
- **Excluded (15):**
  - 13 `._converted.mp4` re-encodes.
  - TikTok `video11` (a re-upload of `video10`).
  - The 11-01 "Part 1" video, which is actually a re-upload of Part 2 (same size and transcript).
- **Lesson map:** `_work/rmbc2/lesson_map.json` has 58 lessons in 16 modules, about 2,941 unique video minutes. Brief: `_work/rmbc2/LESSON-BRIEF.md`.
- **Lesson pages:** 58/58 (Sonnet writers), about 313k words, 386 images in `wiki/assets/stefan-georgi/rmbc-ii/`.
- **Synthesis (Opus):** 18 concepts, 13 frameworks, 5 playbooks, 4 rubrics and 9 libraries, about 245k words. Brief: `_work/rmbc2/SYNTHESIS-BRIEF.md`; harvest: `_work/rmbc2/harvest/`.
  - Libraries: 130 prompts, 149 hooks, 122 teardowns, 96 rewrites, 55 angles, 356 rules, 1,020 benchmark rows, templates.
- **Hub pages:** `README.md`, `index.md`, `contradictions.md` (91 rows), `MERGE-NOTES.md`, `log.md`.
- **Validation:**
  - **Links:** 0 missing targets.
  - **Quotes:** 1,924 timestamped quotes checked.
    - 1,318 are at the cited time; 307 of those are under a different video number than the lesson map.
    - 106 appear elsewhere in the transcript.
    - 500 are not in the transcript. These are mostly screen, doc or ad text plus light paraphrase; spot-checked samples were present at the cited time.
  - Details: `_work/rmbc2/verify_quotes.txt`.
- **Instructors:** Stefan Georgi (modules 1–15 and 16-03 "SPG"). Guests:
  - Dynh Nguyen (12-02)
  - David O'Connell (12-03)
  - Max Finn (12-04)
  - Ethan Bence (16-01)
  - Eddie Maalouf (16-02)
  - Dylan Vanas (16-04)
  - Patrick Stiles (16-05)
- **Compliance:** most course examples contain invented proof and disease, income or scarcity claims. They're flagged on every page as structure-only. See `concepts/compliance-red-flags.md` and `rubrics/llm-output-claim-audit.md`.
- **Global index:** section added to `knowledge-base/wiki/index.md`.

## Next action
Done. Shared-layer wiring done 2026-11-05 (AGENT-GUIDE rows, topic map, contradictions R1–R16, hub pointers). Optional: re-transcribe 11-01 if a correct Part 1 video turns up.
