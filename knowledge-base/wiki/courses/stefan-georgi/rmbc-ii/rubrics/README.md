---
title: "RMBC II rubrics hub (claim audit, VSL review, funnel audit)"
type: rubric
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests Patrick Stiles (16-05) and Ethan Bence (16-01) where cited"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [rubric, hub, quality-gate, claim-audit, vsl, funnel]
updated: 2026-11-02
---

# RMBC II rubrics hub
> Three scored gates for RMBC II work: the mandatory claim audit on every LLM draft, the VSL review (script structure plus live 16-05 benchmarks), and the funnel audit (structure fit, economics, journey, checkout, post-purchase, testing).

## 🤖 Agent use
- **Use when:** any RMBC playbook stage reaches its quality gate, or you are asked to review, audit or diagnose a VSL, page, funnel or LLM draft.
- **Inputs → outputs:** the asset + the truth sheet (real facts and proof) + live metrics if any → a scoring block, a verdict and an ordered fix list.
- **Rules:**
  - **DO** run [llm-output-claim-audit](llm-output-claim-audit.md) first on anything a model wrote. Its ⛔ fails block every other score.
  - **DO** quote the line or metric behind each score; a score with no evidence is a fail.
  - **DO** fix in the order: claims → structure → polish. For live VSLs: the lead first ([16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md); [04-05 30:58–35:38](../lessons/04-05-vsl-product-buildup-and-reveal.md)).
  - **DON'T** let a rubric score replace a test. Stefan: "you just got to test" ([13-01 1:08:00–1:08:55](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
  - **DON'T** treat bands and weights here as course content; they are pipeline design. The checks and their citations are the course content.
- **See also:** [Playbooks hub](../playbooks/README.md) · [Compliance red flags](../concepts/compliance-red-flags.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · Evolve: [copy checklist scorecard](../../../evolve/copywriting/rubrics/copy-checklist-scorecard.md), [Start Here rubrics](../../../evolve/start-here/rubrics/README.md) · Tether: [rubrics hub](../../../../rubrics/README.md)

## Which rubric
| You have | Run | Output | Blocks on |
|---|---|---|---|
| Any LLM output (research doc, brief, VSL, hooks, advertorial, PDP, checkout copy, upsell, emails) | [LLM output claim audit](llm-output-claim-audit.md) | Claim register + PASS / FIX / BLOCK | Invented experts, testimonials, stats, review counts, scarcity, disease/drug, cosmetic-as-drug, income claims, endorsements, invented stories, fake reference prices, hidden subscriptions, deceptive formats, AI personas |
| A VSL outline or script (any length, in-feed or on-page) | [VSL review](vsl-review.md) Part 1 | 23 structure checks, %, record / fix / re-outline | Claim audit BLOCK; spine order, lead-teases, real build-up, close at 0 |
| A live VSL with player data | [VSL review](vsl-review.md) Part 2 | First failing benchmark (conversion, 2-min / CTA / end engagement, unmute, end-of-video conversions, length, CTA drop, upsell, device, returning visitors) and its fix | n.a. (diagnostic) |
| A funnel plan or a live funnel | [Funnel audit](funnel-audit.md) | Section scores E/S/J/C/P/T, ⛔ blockers, bottleneck, ranked tests with $ value | Unknown unit economics, chain/band mismatch, blind VSL behind product ads, billing unclear, fake scarcity, wrong test metric, fake split tests |

## Gate placement in the RMBC pipeline
| Pipeline stage ([RMBC pipeline](../concepts/rmbc-pipeline.md)) | Gate |
|---|---|
| Unified research document | Claim audit (C2, C3, C4, C7, C9): research quotes and stats are leads, not proof |
| UM doc | Claim audit (C3, C8, C9, C18) |
| Brief 2.0 | Claim audit (all); resolve every placeholder to `[VERIFY: …]` |
| VSL outline | VSL review S1-S13, S21 |
| VSL draft | Claim audit → VSL review full Part 1 |
| Ads, advertorial, PDP, checkout | Claim audit → funnel audit J and C sections; Tether [landing-page scorecard](../../../../rubrics/landing-page-scorecard.md) and [ad scorecard](../../../../rubrics/ad-scorecard.md) |
| Upsells, emails | Claim audit → funnel audit P section |
| Live funnel | VSL review Part 2 → funnel audit E, T and bottleneck finder |

## Related
- [Write a VSL with Claude](../playbooks/write-a-vsl-with-claude.md) · [Launch a cold-traffic funnel](../playbooks/launch-a-cold-traffic-funnel.md) · [Offer to funnel end to end](../playbooks/offer-to-funnel-end-to-end.md) · [Post-purchase and retention](../playbooks/post-purchase-and-retention.md) · [Benchmarks library](../libraries/benchmarks.md)
