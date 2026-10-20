# Knowledge Base — Schema & Operating Manual

This is an LLM-maintained knowledge base following Karpathy's "LLM Wiki" pattern
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
**Humans read it; the LLM writes and maintains it.**

## PURPOSE — read this first

This knowledge base is **reference material for AI agents that create UGC / performance ad creative** (scripts, hooks, creator briefs, static and video concepts) for our own e-commerce brands. The typical agent job:

1. Research competitor ads that are performing (ad libraries, TikTok and Meta) and **tear them down**: which angle, hook, heuristic, emotion, self, format, and why it works.
2. Pull out the transferable pattern (angle, hook structure, emotional move, proof type) and **remix it for our product**. Copy the mechanism, not the asset: new script, new visuals, our claims.
3. Write the UGC script and the creator/production brief, then plan tests and iterations.

So every page must be **operational**: an agent should be able to read a page and *do* something with it. Prefer imperative rules, checklists, decision tables, templates, verbatim prompts, and tagged real examples over prose. Human readability still matters, but agent usability comes first.

### Required on every lesson / session / concept / framework page
A section right after the summary line:

```
## 🤖 Agent use
- **Use when:** <which task in the ad-creation pipeline this helps with>
- **Inputs → outputs:** <what the agent needs, what it produces>
- **Rules:** <imperative DO / DON'T bullets distilled from the source>
- **See also:** <prompts, frameworks, libraries to combine with>
```

### Structured knowledge units (so later passes can harvest them into libraries)
Whenever a source contains one of these, record it in this exact table form on the page where it appears (with a `[mm:ss]` citation):

- **Hooks**: `| Hook (verbatim or near) | Heuristic(s) | Emotion / zone | Self targeted | Why it works | Source |`
- **Angles**: `| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |`
- **Ad teardowns** (every real ad shown or critiqued, especially in "Roast My Ads"): `| Brand / product (niche) | Format | Hook / opening | What works | What fails | Fix suggested | Principle | Source |`
- **Rewrites (before → after)**: `| Before | After | What changed (verb / visual / promise / self / intensity) | Source |`
- **Rules of thumb**: bullets starting with **DO** / **DON'T** / **IF … THEN …**

These get compiled into `wiki/libraries/` (hooks, angles, ad-teardowns, rewrites, rules) and `wiki/playbooks/` (end-to-end agent workflows) after ingest.

## Three layers

| Layer | Path | Who edits | What it is |
|---|---|---|---|
| Raw sources | `raw/` | nobody (immutable) | Original course files + machine extractions (transcripts, text from HTML/PDF/DOCX, PDF page images). Source of truth. |
| Wiki | `wiki/` | the LLM | Summaries, lesson notes, concept/framework/person/tool pages, overview, index, log. |
| Schema | `CLAUDE.md` (this file) | human + LLM | Conventions and workflows. |

## Directory map

```
knowledge-base/
├── CLAUDE.md                      ← this file
├── raw/
│   ├── tether-lab/                ← mirror of the MEGA folder (html/pdf/docx/png…)
│   │   ├── _transcripts/          ← Whisper transcripts per video (.txt paragraphs w/ [hh:mm:ss], .srt, .json)
│   │   └── _extracted/            ← markdown text pulled from HTML lesson pages, PDFs, DOCX
│   └── assets/tether-lab/pdf-pages/  ← every PDF page rendered as PNG
└── wiki/
    ├── index.md                   ← catalog of EVERY wiki page (read this first)
    ├── log.md                     ← append-only chronological log
    ├── overview.md                ← big-picture synthesis across all courses
    ├── courses/<course>/          ← README.md (course hub) + one folder per module, one page per lesson/session
    ├── concepts/                  ← one idea per page (e.g. valence, loss aversion). concepts/heuristics/ = one page per heuristic/bias
    ├── frameworks/                ← step-by-step procedures / diagnostics / checklists you can run
    ├── people/                    ← instructors, guests
    ├── tools/                     ← software/products mentioned (CreativeOS, ChatGPT…)
    ├── brands/                    ← brand case files: every ad/page of that brand discussed anywhere, by niche
    ├── resources/                 ← books, reading lists, templates, newsletters
    ├── playbooks/                 ← end-to-end agent workflows (competitor teardown → angle → UGC script → brief → test)
    ├── libraries/                 ← harvested, tagged collections: hooks, angles, ad teardowns, rewrites, rules
    ├── rubrics/                   ← scoring checklists an agent applies to an ad or script
    └── assets/<course>/<module>/  ← screenshots chosen for wiki pages
```

## Page conventions

- **File names**: lowercase-kebab-case, ASCII only. Lessons are prefixed with their order: `03-the-4-emotional-zones.md`.
- **Links**: standard relative markdown links (`[Valence](../../concepts/valence.md)`) so it works in Obsidian, VS Code and GitHub. Link generously: every concept mentioned that has a page gets linked on first mention.
- **Images**: `![caption](../../../assets/tether-lab/03-valence-intensity-model/03-zones-0142.jpg)` with a one-line italic caption under it explaining what the screenshot shows and why it matters. Name screenshots `<lesson-number>-<short-topic>-<mmss>.jpg`. Only embed screenshots that carry information (slides, diagrams, ad examples, UI steps) — not talking heads.
- **Timestamps**: cite video moments as `[mm:ss]` (or `[h:mm:ss]`) taken from the transcript, so the reader can jump to the video.
- **Frontmatter** (YAML) on every page:

```yaml
---
title: "The 4 Emotional Zones"
type: lesson            # lesson | session | module | course | concept | framework | person | tool | resource | prompt | overview | playbook | library | rubric | brand
course: tether-lab
module: 03-valence-intensity-model
order: 3
video_length: "16:42"   # lessons/sessions only
sources:                # raw files this page is built from (paths relative to knowledge-base/)
  - raw/tether-lab/_transcripts/3. The Valence & Intensity Model/3.The 4 Emotional Zones (a.k.a Your Target Map).txt
tags: [emotion, targeting]
updated: 2026-10-20
---
```

### Lesson / session page template

```
# <Title>
> One-sentence summary of what this lesson teaches.

## TL;DR            ← 3–6 bullets, the stuff you'd remember a month later
## Key ideas        ← detailed notes, organized by sub-topic, with [mm:ss] citations
## Framework / steps← numbered procedure if the lesson teaches one (link to frameworks/ page)
## Examples         ← concrete ads, brands, before/after rewrites given in the lesson
## Screenshots      ← (or inline within Key ideas) captioned images
## Notable quotes   ← short verbatim lines worth keeping
## How to apply     ← action checklist
## Related          ← links to concepts / frameworks / other lessons
## Sources          ← links to raw transcript, page text, PDF
```

### Concept / framework pages
Definition → why it matters → how to use it (steps) → examples → common mistakes → "Where it's taught" (backlinks to every lesson/session that covers it, with timestamps) → related concepts.

## Workflows

### Ingest (adding a new source)
1. Put the original file under `raw/<course>/…` (never edit raw files afterwards). Transcribe/extract into `_transcripts/` / `_extracted/`.
2. Write/refresh the lesson or session page.
3. Update every concept/framework/person/tool page the source touches (add to "Where it's taught", add new examples, flag contradictions).
4. Update `wiki/index.md` and the course `README.md`.
5. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` + bullet list of pages created/changed.

### Query
Read `wiki/index.md` first, then the relevant pages; answer with links to wiki pages and `[mm:ss]` video citations. If the answer is a reusable synthesis, file it as a new page and log it (`## [date] query | …`).

### Lint
Periodically check for: orphan pages (not in index / no inbound links), concepts mentioned without pages, contradictions between instructors, stale claims, broken links/images. Log as `## [date] lint | …`.

## Tooling used to build this
Scripts live outside the KB in `D:\resources\_tools\` (MEGA partial fetcher that pulls only audio + keyframes, faster-whisper GPU transcription, doc converters).
