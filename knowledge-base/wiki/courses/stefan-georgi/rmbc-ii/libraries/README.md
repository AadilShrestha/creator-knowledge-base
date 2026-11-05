---
title: "Libraries hub: RMBC II (prompts, hooks, ad teardowns, rewrites, templates, angles, rules, benchmarks)"
type: library
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests Dynh Nguyen (12-02), David O'Connell (12-03), Max Finn (12-04), Ethan Bence (16-01), Eddie Maalouf (16-02), Dylan Vanas (16-04), Patrick Stiles (16-05)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [library, hub, index, prompts, hooks, ad-teardowns, rewrites, templates, angles, rules, benchmarks]
updated: 2026-11-02
---

# Libraries hub (RMBC II)
> The lookup layer for Stefan Georgi's RMBC II: every prompt, hook, teardown, rewrite, template, angle, rule and number from the 58 lesson pages, de-duplicated, tagged and linked back to the lesson and timestamp. Use it for lookups inside a task; the [playbooks](../playbooks/README.md) and [frameworks](../frameworks/vsl-build-with-claude.md) run the full workflows.

## 🤖 Agent use
- **Use when:** you need a precedent, a prompt to paste, a structure to fill, a rule to settle a decision or a number to plan or judge against, while doing research, mechanism, brief, VSL, ad, advertorial, PDP, checkout, upsell, email or test work for our brands.
- **Inputs → outputs:** your current step (table below) → the right library → filtered rows (grep by section, niche, lesson, claim risk) → a prompt, structure, mechanism or number with its citation → our own asset, checked against [rules §16](rules.md#16-compliance-hard-stops) and the [LLM output claim audit](../rubrics/llm-output-claim-audit.md).
- **Rules:**
  - **DO** grep the large libraries; don't read them top to bottom (prompts, rules, benchmarks and teardowns each run to thousands of words).
  - **DO** copy the mechanism, not the asset: reuse structure, beat order and prompt shape, never lines, characters, numbers or claims from course examples or competitor pages. [06-01 09:15–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md) · [AGENTS.md rule 3](../../../../../../AGENTS.md)
  - **DO** treat every row marked "do not reuse", ⛔ or "example claim" as structure only; claims not reusable. Course examples routinely contain invented doctors, testimonials, studies, counts, disease and income claims, and fake scarcity.
  - **DON'T** treat "(instructor claim)", "(guest claim)", "Claude output" or "LLM-generated" rows as evidence that something works.
  - **IF** two libraries or rows disagree **THEN** use the conflict tables in [rules](rules.md#conflicts-at-a-glance) and [benchmarks](benchmarks.md#conflicting-values-side-by-side) and say which default you followed.
- **See also:** [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Compliance red flags](../concepts/compliance-red-flags.md) · [Rubrics](../rubrics/README.md) · Evolve: [Copywriting libraries](../../../evolve/copywriting/libraries/README.md), [Start Here KPI thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md) · Tether Lab: [shared libraries](../../../../libraries/README.md)

## The 9 libraries
| Library | What it holds | Size | Organised by | How to grep it |
|---|---|---|---|---|
| [Prompts](prompts.md) | Every verbatim prompt, follow-up and Claude Project instruction (research, mechanism, brief, VSL, hooks, advertorial, PDP, ads, upsells, email), with inputs, failure modes and compliant fixes | 241 harvested blocks → ~130 numbered entries (R1…, M1…) | Pipeline stage: Research → Mechanism → Brief → Claude Project instructions → VSL drafting → Hooks → Advertorials → PDPs → Ads → Upsells → Email | `grep -n "^### " prompts.md` (entry list) · `grep -n "^### M" prompts.md` (mechanism prompts) · `grep -n -i "continue" prompts.md` |
| [Hooks](hooks.md) | Every hook shown, written or generated, tagged by niche, awareness, format, length band and claim risk | 167 harvested → 149 entries | 10 hook families (contrarian / "Nope" ladder, command, hidden cause, call-outs, self-tests, story, authority, social proof, specific promise, TikTok hook stacks) | `grep -i "skincare" hooks.md` · `grep "| do not reuse |" hooks.md` · `grep "LLM-generated" hooks.md` |
| [Ad teardowns](ad-teardowns.md) | Every real ad, VSL, advertorial, PDP, checkout, upsell page and webinar ad critiqued: what works, what fails, fix, principle | 131 harvested → 122 entries | Asset type: VSLs, short video, advertorials/native, PDPs, checkouts, Meta, Google, TikTok, upsells, webinar ads, competitor snapshots | `grep "| checkout |" ad-teardowns.md` · `grep -i "nooro" ad-teardowns.md` · `grep "| do not reuse |" ad-teardowns.md` |
| [Rewrites](rewrites.md) | Before → after edits: Stefan's copy-chief fixes to Claude drafts, structure swaps, hook/lead fixes, offer and claim edits, guest ad edits | 96 entries | Asset: mechanism naming, closes, big ideas/leads, briefs, VSL drafts, advertorials, paid ads, upsells | `grep "| mechanism |" rewrites.md` · `grep "| upsell script |" rewrites.md` |
| [Templates](templates.md) | Fill-in structures and outlines: classic VSL spine, in-feed vs on-page VSL, short-VSL structures, advertorial, PDP, upsell, email sequences, brief fields | 109 harvested rows | Asset type | `grep -n "^## " templates.md` · `grep -i "upsell" templates.md` |
| [Angles](angles.md) | Angles as reasons to buy, with core desire or pain, awareness stage, best format, example line and claim risk; plus upsell bridges and abandon-cart email angles | 37 entries + 11 upsell bridges + 7 abandon-cart angles | Source: awareness-stage, psychographic, big-idea, brief, advertorial, short-form video, upsell and email angles | `grep -i "<niche>" angles.md` |
| [Rules](rules.md) | Canonical DO / DON'T / IF…THEN rules with every citation; 14 flagged conflicts; compliance hard stops | 807 harvested → 356 rules | 16 job sections: research, mechanism, brief, Claude, VSL, hooks, ads by platform, advertorials, PDP, checkout, funnel, upsells, email, CRO, webinars, compliance | `grep -n "^- \*\*VS" rules.md` (VSL rules) · `grep -n "⚖️" rules.md` (conflicts) · `grep -n "^- \*\*X" rules.md` (hard stops) |
| [Benchmarks](benchmarks.md) | Every number: VSL lengths, section sizes, engagement and conversion baselines, landing-page CTR, funnel scores, CPA/AOV/COGS math, upsell length and take rate, email timing and discount ladders, test durations, webinar KPIs | 1,020 rows (72 ⛔ example claims); 15 conflict tables; Evolve comparison | Topic tables, quick reference, conflicts side by side | `grep -n "take rate" benchmarks.md` · `grep -n "\[16-05" benchmarks.md` · `grep -n "guest claim" benchmarks.md` |
| README (this page) | The index: what each library holds, how to grep it, which to open for which job | 9 libraries | Pipeline step | — |

The templates size is the harvested-row count; that page states its final count after merging.

## Which library for which job
| Pipeline step | IF you need… | THEN open | Filter by |
|---|---|---|---|
| 1. Research | The deep-research, merge or ingredient prompt | [Prompts → Research](prompts.md#research) | R-numbered entries |
| 1. Research | How to read and verify the output | [Rules §1](rules.md#1-research), [rules X13](rules.md#16-compliance-hard-stops) | — |
| 2. Mechanism | Ideation, evaluation or expansion prompt | [Prompts → Mechanism](prompts.md#mechanism) | M-numbered entries |
| 2. Mechanism | How to judge and name a mechanism | [Rules §2](rules.md#2-unique-mechanism), [rewrites §1](rewrites.md) | — |
| 3. Brief | Generator setup and revision prompts | [Prompts → Brief](prompts.md#brief), [rules §3](rules.md#3-brief) | — |
| 4. VSL | Structure and beat order | [Templates](templates.md), [rules §5](rules.md#5-vsls) | Length band |
| 4. VSL | Length, close share, engagement targets | [Benchmarks](benchmarks.md#decision-quick-reference-derived) | VSL rows |
| 4. VSL | Project instructions and drafting prompts | [Prompts → Claude Project instructions / VSL drafting](prompts.md#claude-project-instructions) | — |
| 5. Hooks and ads | Opening lines and hook families | [Hooks](hooks.md), [prompts → Hooks](prompts.md#hooks) | Niche, awareness, claim risk |
| 5. Hooks and ads | Platform rules and numbers | [Rules §7](rules.md#7-ads-by-platform), [benchmarks](benchmarks.md) (Meta, native, Google, TikTok tables) | Platform |
| 5. Hooks and ads | A competitor precedent | [Ad teardowns](ad-teardowns.md), [angles](angles.md) | Asset type, niche |
| 6. Pages | Advertorial, PDP, checkout structure and rules | [Templates](templates.md), [rules §8–§10](rules.md#8-advertorials) | — |
| 7. Funnel | Choose the funnel; unit economics | [Rules §11](rules.md#11-funnel-structure-and-economics), [benchmarks → funnel tables](benchmarks.md) | — |
| 8. Post-purchase | Upsell and email structure, timing, discounts | [Templates](templates.md), [rules §12–§13](rules.md#12-upsells), [benchmarks](benchmarks.md) | — |
| 9. Test | What to test first, how long, what counts as a win | [Rules §14](rules.md#14-cro-and-testing), [benchmarks → CRO](benchmarks.md) | — |
| 10. QA | Edits that fix weak drafts | [Rewrites](rewrites.md) | Change type |
| 10. QA | Claims that must not ship | [Rules §16](rules.md#16-compliance-hard-stops), [LLM output claim audit](../rubrics/llm-output-claim-audit.md) | — |

## Conventions
- **Citations:** `[07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)` = lesson 07-01, third video, 01:13. Non-video sources: "docx", "doc", "slide", "frame", "screen", "PDF p.n", "SRT", "page" (lesson-page text).
- **Attribution:** Stefan Georgi teaches modules 1–15 and 16-03 ("SPG"). Guests: 12-02 Dynh Nguyen (native), 12-03 David O'Connell (Google), 12-04 Max Finn (TikTok), 16-01 Ethan Bence of 4080 Marketing (CRO), 16-02 Eddie Maalouf (e-com and Amazon), 16-04 Dylan Vanas (webinars), 16-05 Patrick Stiles of Vidalytics (VSL benchmarks). Guest figures carry "(guest claim)".
- **Provenance tags:** "(derived)" = inference or arithmetic made on the lesson page or in the library; "LLM-generated" / "Claude output" = model text from a course demo, not a live asset; "(instructor claim)" / "(guest claim)" = unverified result.
- **IDs:** rules use section prefixes (RS, MC, BR, CL, VS, HK, AD, AV, PD, CK, FN, UP, EM, CR, WB, X); benchmarks use B001…; prompts use stage letters (R, M, …). Cite IDs in briefs and reviews.
- **Relationship to other courses:** these pages hold RMBC II's teaching only. Evolve's libraries cover ad-level copywriting and Meta media buying; where RMBC and Evolve disagree, the rules and benchmarks pages state both and give an agent default.

## Coverage and gaps
- **Sources:** all 58 lesson pages were harvested (807 rules, 241 prompt blocks, 167 hooks, 131 teardowns, 109 templates, 96 rewrites, 37 angles before merging); numbers were extracted from every lesson page's notes, examples and tables.
- **Evidence limits:** the course shows almost no controlled data. Stefan's results are anecdotes; the 16-05 Vidalytics figures are platform aggregates ("these aren't split tests"); 16-01 to 16-04 guest numbers come from their own decks and clients.
- **Compliance:** module 5 to 15 example outputs were generated with placeholders on purpose; every invented proof element is flagged in the lesson pages and must be replaced with real, verified facts or cut.
