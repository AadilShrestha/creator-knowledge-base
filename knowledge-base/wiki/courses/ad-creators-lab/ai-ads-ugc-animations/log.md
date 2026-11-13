# Ad Creators Lab: log

## [2026-11-13] ingest | Ad Creators Lab (September 2026), MEGA 5Y1lhJKB
- Inventory: 224 files, 10.66 GB; manifest created (9 exclusions: reseller files and 3 misfiled real-estate videos).
- Full download (`_tools/course_fetch.py`), streaming ASR (`_tools/course_stream.py asr`) and scene-change frames (`course_stream.py frames --by-path`, new flag for courses whose lesson numbers restart per module).
- Docs: `_tools/convert_course_docs.py` now also converts `.htm`; new `_tools/extract_inline_images.py` moves base64 images (Skool pages and Google Docs exports) into `raw/.../linked/inline-images/<page>/`.
- Linked Google Docs, Sheet and Drive files fetched (`raw/.../linked/linked-index.json`).
- 110 lesson pages (L20 reference page by hand; 13 Sonnet writer runs).
- Synthesis (5 Opus runs): concepts, frameworks, playbooks, rubrics, libraries. Course README, index, contradictions (48 rows), MERGE-NOTES, PROGRESS.
- Shared layer wired: AGENTS.md, AGENT-GUIDE, topic-map, contradictions (AC1–AC9), hubs, tool pages, global index.
- Fixes after review: L84 scorecard hook key read in full from frame 38:23; L106 paraphrase replaced by the verbatim transcript line.
