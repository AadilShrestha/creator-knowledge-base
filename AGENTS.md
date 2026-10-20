# Knowledge-base operating instructions

## Purpose and startup

Build a source-grounded reference for agents and humans doing e-commerce research, copywriting, competitor-ad analysis, UGC scripts, creative briefs, and testing. Preserve teaching beyond that focus when a course contains it; classify it rather than dropping it.

At session start: read this file, `knowledge-base/CLAUDE.md`, the course's `PROGRESS.md` and `manifest.json`, then its `index.md`, when those files exist. Resolve paths from the workspace root, never from a Windows drive hardcoded in old tools. Create missing course checkpoints before processing sources.

For new courses, the creator-local paths below take precedence over the older single-course paths in `knowledge-base/CLAUDE.md`.

## Three layers and exact destinations

1. Original inputs: `knowledge-base/raw/<creator>/<course>/originals/`. Preserve downloaded filenames and original directory hierarchy. These binaries are ignored by Git.
2. Derived source evidence: `knowledge-base/raw/<creator>/<course>/_transcripts/` (`.txt`, `.srt`, `.json`) and `_extracted/` (`.md`, `.txt`, `.json`, `.csv`). Mirror the original relative path to avoid duplicate basenames. Git tracks these text formats. Treat extraction and transcription as imperfect evidence, not final knowledge.
3. Compiled knowledge: `knowledge-base/wiki/courses/<creator>/<course>/`. Store `README.md`, `index.md`, append-only `log.md`, `PROGRESS.md`, `manifest.json`, ordered `lessons/`, `concepts/`, `frameworks/`, `libraries/`, `playbooks/`, `rubrics/`, `people/`, `resources/`, and `contradictions.md` as needed. Small selected screenshots go to `knowledge-base/wiki/assets/<creator>/<course>/`.

Existing Tether Lab pages keep their current paths. New creators use lowercase ASCII slugs. Use `evolve` as the source organization until instructors are verified. Multiple courses from a creator remain separate course subfolders. Course-local pages retain attribution; after review, reusable cross-creator synthesis can be added to shared `wiki/concepts/`, `wiki/frameworks/`, etc., with backlinks to each creator.

## Local workflow

Build and save the knowledge base directly in the selected local workspace. No repository, branch, commit, push, or pull request is required for ingestion. Perform Git operations only when explicitly requested. Preserve unrelated existing work and keep each creator/course in its own folder. Link to related shared knowledge and integrate reusable ideas with source attribution. Do not regenerate the global index with the old Windows-only `_tools/build_index.py`; it assumes the old course depth.

Detect the operating system, architecture, disk space, and available tools. Set up required local dependencies and scripts, using a Python virtual environment. On a Mac, select an Apple Silicon or Intel-compatible transcription backend. Ask the user only for an actual missing permission, login, or access requirement; give a single concrete step and continue independent work.

## Ingestion workflow

1. Inventory every remote source, including nested folders, documents, templates, and duplicates. Reconcile file count and bytes with the source listing. Each file gets a stable source ID, original path, size, type, and explicit status in `manifest.json`.
2. Download with the official MEGA desktop app or documented MEGAcmd commands. Agent Reach helps read web/docs; it does not itself decrypt MEGA folders or transcribe local videos. Record quota/access failures as blocked, with next action. Preserve manifests so work resumes.
3. Extract existing captions first. Otherwise transcribe the whole recording with timestamps using `tools/kb/transcribe.py`; on Apple Silicon prefer MLX, on Intel use faster-whisper CPU. Run one sample before batching. Keep model names and machine-transcription provenance. Inspect silence, missing endings, uncertain names, and suspicious numbers against the recording.
4. Extract full document content, including slide notes, tables, spreadsheet tabs, and linked attachments actually available. OCR scanned material. Mark inaccessible embeds and unreadable sections. Never summarize a file from its title alone.
5. Read the complete transcript/extraction and inspect meaningful visuals. Write one lesson/session page per teaching unit; pair its HTML, recording, and attachments without losing their individual manifest records. Choose screenshots showing slides, worked examples, ads, or UI steps; caption and timestamp them.
6. Integrate course-local concepts, frameworks, prompts, examples, and contradictions. Maintain `index.md` and append to `log.md`. Update manifest entries and `PROGRESS.md` after each batch, not just at the end.
7. Validate relative links, image files, evidence references, inventory coverage, and sampled timestamp accuracy. Existing unrelated Tether Lab defects are baseline issues; verify the contribution separately.

## Knowledge page contract

Use YAML frontmatter with `title`, `type`, `creator`, `course`, `sources` (repo-relative evidence paths), `tags`, and `updated`. Cite video claims with `[hh:mm:ss]` or `[mm:ss]`; cite documents with page/slide/sheet/section. Use ordinary relative Markdown links, forward slashes, and filenames that work on Mac and Windows.

A lesson contains: one-sentence summary; **Agent use** (use when, inputs → outputs, imperative rules, related pages); key ideas with evidence; steps or framework; concrete examples and before/after rewrites; exact prompts/templates when supplied; meaningful screenshots; application checklist; related links; sources and limitations. Keep the useful detail, not a transcript dump or generic short summary.

Label verbatim quotations, instructor claims, machine-transcription uncertainty, and your derived applications. Preserve dissent between creators with attribution and context. Never invent missing examples, proof, statistics, resource content, or timestamps. Capture source-backed hooks, angles, ad teardowns, rewrites, and rules in structured tables using the existing KB schema when applicable. De-duplicate libraries without losing source citations.

## Status and completion

Manifest statuses: `pending`, `downloaded`, `transcribed`, `extracted`, `summarized`, `verified`, `blocked`, `excluded`. Track stage booleans separately because an intermediate status cannot represent every artifact. `excluded` needs an explicit reason such as a byte-identical duplicate and a reference to its canonical file. Unprocessed content is pending or blocked, never silently excluded.

Only mark `verified` when the complete source was processed, its linked evidence and wiki page exist, meaningful visuals were considered, and checks passed. The manifest must map every teaching source to a page or a documented exclusion/blocker. Report exclusions and blockers separately; zero pending items alone does not mean complete.

Before stopping: save exact counts, blockers, current lesson, completed files, and next action/command in `PROGRESS.md`; leave a concise status for the human. At a session limit, the next session resumes from these files. Do not promise unattended work after the process stops.

## Query and maintenance

For answers, start with the relevant course/global index, read the supporting pages, and cite course, lesson, and timestamp/page. File reusable syntheses back into the appropriate wiki scope and log them. Periodic lint checks links, missing evidence, unindexed pages, contradictions, and source coverage.
