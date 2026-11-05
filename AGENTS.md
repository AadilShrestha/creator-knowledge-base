# Agent instructions

This repository is a knowledge base built from paid e-commerce marketing courses: ad psychology, copywriting, UGC and video scripts, static ads, competitor teardowns, creative testing, Meta media buying, and long-form direct response (VSLs, advertorials, PDPs, checkouts, upsells, email, funnels). Agents use it to produce marketing work for our own DTC brands.

## Making something with the knowledge (most tasks)

Open the matching entry point and follow it. **Don't read the whole wiki.** The entry points tell you exactly which files to open.

| Task | Open and follow |
|---|---|
| UGC script, video ad script, ad hooks, fix an ad script | [.claude/skills/write-ugc-script/SKILL.md](.claude/skills/write-ugc-script/SKILL.md) |
| Everything else: research, angles, mechanism, competitor teardown, statics, briefs, VSLs, advertorials, PDPs and landing pages, checkout / upsells / email, funnels and unit economics, Claude Projects, media buying and scaling, tests and iteration, creator programs | [knowledge-base/AGENT-GUIDE.md](knowledge-base/AGENT-GUIDE.md), "Task → start here" table |
| A topic two courses both teach, or two pages that disagree | [knowledge-base/wiki/topic-map.md](knowledge-base/wiki/topic-map.md) (owner page + conflict row) |
| Look up a concept, lesson or quote | [knowledge-base/wiki/index.md](knowledge-base/wiki/index.md), then grep `knowledge-base/wiki/` |

Rules for every output:
1. **Real inputs first.** Ask for, or find, product facts, the offer, the audience and real customer language (reviews, comments, Reddit) before writing. List what's missing instead of guessing.
2. **Never invent proof.** No made-up reviews, quotes, counts, ratings, studies, experts, endorsements, results or scarcity. Bracket unverified facts. Run every LLM-written draft through the [claim audit](knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md); course example scripts and briefs often contain invented proof, so reuse their structure only.
3. **Copy the mechanism, not the asset.** Reuse structures and patterns, never lines, characters or claims from competitor or example ads.
4. **Large library files** (hooks, teardowns, rewrites run to 10k+ words): search them with grep for your niche or pattern. Don't read them top to bottom.
5. Cite the knowledge you rely on (course, lesson, timestamp) when the user asks why.

## Adding a course to the knowledge base

Read [INGESTION.md](INGESTION.md) first and follow it fully. It covers source inventory, download, transcription, page contracts, manifests and validation. The wiki's page schema is in [knowledge-base/CLAUDE.md](knowledge-base/CLAUDE.md).

## Repository rules
- Git operations (commit, push, branches) only when the user explicitly asks.
- Don't regenerate the global index with the old `_tools/build_index.py`.
- Original course videos and files stay local in `knowledge-base/raw/**/originals/` (ignored by Git). Transcripts and extracted text are tracked.
- Test briefs for checking output quality live in [evals/](evals/README.md).
