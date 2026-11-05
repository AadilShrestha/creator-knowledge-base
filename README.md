# Creator knowledge base

A Markdown knowledge base of e-commerce marketing courses (ad psychology, copywriting, UGC and video scripts, statics, competitor teardowns, testing), built for AI agents that make ad creative. It follows [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources are preserved, knowledge is compiled into linked pages, and every change is logged.

## Use it
- **Agents:** start at [AGENTS.md](AGENTS.md). It routes each task to a skill or playbook.
- **Write a UGC / video ad script:** [write-ugc-script skill](.claude/skills/write-ugc-script/SKILL.md) (works in Claude Code; other agents can read and follow the same file).
- **Everything else:** [AGENT-GUIDE](knowledge-base/AGENT-GUIDE.md) task table, [wiki index](knowledge-base/wiki/index.md), [overview](knowledge-base/wiki/overview.md).

## What's in it
| Course | Creator | Status | Hub |
|---|---|---|---|
| Tether Lab | Sarah Levinger | Ingested | [course hub](knowledge-base/wiki/courses/tether-lab/README.md) |
| Evolve Copywriting | Spencer Pawliw | Ingested and verified (144/144 sources) | [course hub](knowledge-base/wiki/courses/evolve/copywriting/README.md) |
| Evolve Start Here | Spencer Pawliw, Shaun Eng | Ingested and verified (359/359 sources; 175 lessons) | [course hub](knowledge-base/wiki/courses/evolve/start-here/README.md) |
| RMBC II | Stefan Georgi (+7 guests) | Ingested and verified (313/328 sources, 15 excluded duplicates/defects; 58 lessons) | [course hub](knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/README.md) |

## Layout
- `knowledge-base/wiki/`: compiled knowledge (lessons, concepts, frameworks, playbooks, rubrics, libraries).
- `knowledge-base/raw/`: transcripts and extracted text (tracked); original videos and files stay local (ignored by Git).
- `.claude/skills/`: task skills for agents.
- `evals/`: fixed test briefs and before/after runs for checking output quality.
- [INGESTION.md](INGESTION.md): how to add a course.

Open `knowledge-base/` as an Obsidian vault for a visual browser. No database or hosted app is required.
