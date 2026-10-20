# Paste everything below into Claude Code, from the repository root

You are helping me contribute to a shared, persistent Markdown knowledge base. I am new to Claude Code and use a MacBook. Do the file work, explain browser-login steps simply, and save progress so another session can resume. Our subject is e-commerce, marketing, customer research, copywriting, and ad creative. Preserve all substantial course teaching, including material outside ad scripting.

## Read first

Read `CLAUDE.md`, `AGENTS.md`, `knowledge-base/CLAUDE.md`, `handoff/MAC-SETUP.md`, and the two assigned courses' `PROGRESS.md`, `manifest.json`, and `index.md`. Read Karpathy's architecture using Agent Reach's web-reading route: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f . Use its raw sources → compiled wiki → operating schema pattern. Work on the actual files, not only a proposed plan.

## Assignment

Process **everything available** in these two MEGA folders:

1. **Evolve Copywriting**: https://mega.nz/folder/LlQnyCIZ#l_Dfcb8HnnxfFk_siwzDjA
   - Inventory baseline: 144 files, about 2.63 GB.
   - Wiki: `knowledge-base/wiki/courses/evolve/copywriting/`
   - Local originals: `knowledge-base/raw/evolve/copywriting/originals/`
   - Derived evidence: adjacent `_transcripts/` and `_extracted/` folders.
2. **Evolve Start Here**: https://mega.nz/folder/jhQDiSSY#eDwZp_oMz5QVaEtPL-_s1g
   - Inventory baseline: 359 files, about 6.53 GB.
   - Wiki: `knowledge-base/wiki/courses/evolve/start-here/`
   - Local originals: `knowledge-base/raw/evolve/start-here/originals/`
   - Derived evidence: adjacent `_transcripts/` and `_extracted/` folders.

Counts describe the remote listing on 2026-10-20, not completed ingestion. Re-list/reconcile if it changes. `evolve` identifies the source brand; verify actual instructor names from the course before attributing claims. Separate courses even if instructors overlap. Preserve their original lesson ordering. Pair HTML/video/attachments belonging to the same lesson; account for every file independently.

## First actions

Check repo root, branch, worktree changes, disk space, macOS version, architecture, and installed tools. Use `contrib/friend-creators`, preserving other contributors' changes. Follow `handoff/MAC-SETUP.md` to install missing project dependencies and Agent Reach. Human login, MEGA app downloads, and actual access/permission blockers are the only things to hand back to me; continue independent work while waiting. Explain any necessary approval by naming the tool or guide requiring it. No paid remote transcription service is requested.

Use the official MEGA desktop app or documented MEGAcmd commands for downloads. Agent Reach routes web/docs access, not MEGA decryption. Check downloaded names and sizes against each manifest. Quota errors are checkpoints, not reasons to mark content complete. If direct download automation fails, give me the exact app step and destination, then prepare the ingestion workspace.

On Apple Silicon, use `mlx-whisper` with `tools/kb/transcribe.py --backend mlx`. On Intel, use `faster-whisper` CPU with `--backend cpu --model small`. Use complete existing subtitles when available. Test a short clip, review quality, then transcribe full recordings sequentially. Store timestamped text, SRT, and JSON under the assigned course's `_transcripts/`, keeping source-relative subfolders. Read the helper's `--help`. Run a full sample lesson, including its document attachments and useful screenshots, before the remaining batches.

Extract documents with appropriate local tools: PyMuPDF for PDF, python-docx for Word, BeautifulSoup for HTML, openpyxl for XLSX, python-pptx for slides. Include worksheet names/formulas and meaningful slide notes where applicable. OCR scanned pages; mark anything unreadable or inaccessible. Inspect visuals at cited moments; select images of diagrams, ad examples, worked steps, and tables, with useful captions. Save selected screenshots under `knowledge-base/wiki/assets/evolve/<course>/` and link relatively.

## Write useful knowledge

Follow the page contract in AGENTS.md. Every lesson must explain what it teaches, its concrete steps and examples, and how an agent can use it. Preserve exact supplied prompts/templates, important before/after rewrites, caveats, and source timestamps/page/slide/sheet citations. Distinguish instructor statements from your derived applications. Check uncertain claims against the original, and label remaining uncertainty. Never invent evidence or fill an inaccessible source with general knowledge.

Build course-local concepts, frameworks, people, resources, contradictions, and source-backed libraries/playbooks/rubrics when the teaching supports them. De-duplicate examples while retaining every citation. Link to related existing shared knowledge. Keep existing Tether Lab and global files unchanged in this contribution; put proposed shared synthesis/index changes into course-local `MERGE-NOTES.md` for later integration.

Maintain the course `README.md`, navigable `index.md`, append-only `log.md`, `manifest.json`, and `PROGRESS.md` after every batch. Each manifest file needs processed stages, current status, evidence path(s), wiki page(s), and blockers or exclusions. A title, download, or transcript alone is not an ingested lesson. Record byte-identical duplicates explicitly with their canonical file; preserve distinct HTML/video/attachment contributions.

## Verify and hand off

Run `python tools/kb/check_links.py <your-course-path>` for each course, and verify image files, source references, manifest coverage, and sampled timestamps. The old Tether Lab baseline has unfinished links; report those separately from defects introduced here. Map every teaching source to detailed knowledge or an explicit blocker/exclusion. Report total, verified, pending, blocked, and excluded counts; disclose unreadable material.

Save progress before a session limit or stopping: current batch, exact counts, filenames, blocker, next action/command, and latest commit. Commit separate course batches using explicit paths. Review staged filenames so only notes, derived text evidence, and small selected images go into Git. Original media/documents, models, tokens, and temporary files stay local.

Once checked, push `contrib/friend-creators` and create a PR against `main` with course coverage, methods, limitations, validation, and proposed global integration. Leave merging to the owner. If the course is still blocked, clearly label a partial PR. If GitHub access is unavailable, commit locally and explain the exact missing access step. Continue until the task is complete or all available independent work is exhausted by a real blocker.
