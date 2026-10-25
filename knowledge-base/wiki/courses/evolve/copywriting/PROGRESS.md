---
title: "Evolve Copywriting: progress"
type: overview
creator: evolve
course: copywriting
updated: 2026-10-22
---

# Evolve Copywriting: progress

Updated: 2026-10-22. **Ingestion complete and verified.**

## Final checkpoint
- Source files: **144** (2,633,624,794 bytes). Manifest: **144 verified**, 0 pending, 0 blocked, 0 excluded. Every file maps to a lesson page that cites its evidence.
- Linked material outside MEGA: 104 Skool lesson images and 9 Google Docs/Sheets fetched (`raw/evolve/copywriting/linked/`). **One blocker:** the lesson 57 "100 Hook Templates" Google Sheet returns 401 (login required); only the 25 rows legible on screen are recorded.
- Duplicates noted, not excluded: the three "How To Write Video Ads" DOCX files (lessons 70, 71, 72) have identical text; the verbatim prompt lives once on lesson 72.
- Instructor: **Spencer Pawliw** (on-screen tweet "@spencepawliw", lesson 40 [02:40]; self-references in lessons 8, 25, 30, 55).

## What was built
| Area | Pages | Words |
|---|---|---|
| Lessons (`lessons/`) | 72 | ≈241k |
| Concepts | 28 | ≈67k |
| Frameworks | 8 | ≈22k |
| Playbooks (+ hub) | 5 | ≈9k |
| Rubric (+ hub) | 2 | ≈4k |
| Libraries (+ hub) | 9 | ≈69k: hooks 229, templates 209, rewrites 179, ad teardowns 186 + 23 positioning moves, angles 75, rules 305, prompts 26 indexed |
| Hub, index, contradictions (16 within-course + 29 cross-course), merge notes | 4 | |
- Screenshots and images: 385 in `wiki/assets/evolve/copywriting/`.

## Validation evidence
- Links: `python tools/kb/check_links.py knowledge-base/wiki/courses/evolve/copywriting` → 130 files, **0 missing targets** (links, images and frontmatter sources). Whole wiki: 0 missing link/image targets; the remaining flags are older Tether Lab frontmatter paths written relative to `knowledge-base/` (baseline, unchanged).
- Transcripts: 59/59 videos, faster-whisper large-v3-turbo on CUDA (the first 7 non-batched, the rest batched); no transcript ends more than 20 s before its recording.
- Timestamp sample: `_tools/verify_quotes.py` checked 1,531 quoted lines. 1,145 were found in the transcripts, 1,120 of them inside the cited range ±60 s. 11 mis-timed narration quotes were corrected. The rest are mostly ad lines shown on a slide and spoken later. Unmatched quotes are mostly on-screen or document text; spot checks confirmed them.
- Visuals: candidate frames (scene changes plus a frame at least every 10 s, facecam-aware dedupe) reviewed for every video lesson.

## Known limitations
- Not in the course files: Canva "winning ads" decks, Loom/Frame.io videos, the FigJam board, several prompt docs linked from L37, and the `/ad-iteration` skill's own instructions. The pages say so where they are referenced.
- Many performance claims ("$1M ad", spend shares, "breakthrough") are the instructor's labels without published data, and are labelled as such.
- The video-script process assumes AI voiceover + B-roll. Adaptations to on-camera UGC are marked "(derived)".

## Resume / maintenance
- Rebuild the course index: `python -P _tools/course_index.py knowledge-base/wiki/courses/evolve/copywriting _work/new4/lesson_map.json "Evolve Copywriting"`.
- Refresh the manifest stages: `python -P _tools/course_manifest.py knowledge-base evolve copywriting _work/new4/lesson_map.json` (keeps `verified`).
- Library sources and the builder are in `_work/new4/lib_src/` and `_work/new4/lib_build.py`.
- Next shared-synthesis proposals: [MERGE-NOTES](MERGE-NOTES.md).
