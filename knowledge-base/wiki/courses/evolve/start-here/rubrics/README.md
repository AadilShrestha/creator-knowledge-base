---
title: "Evolve Start Here rubrics hub"
type: rubric
creator: evolve
course: start-here
instructor: "Evolve (Spencer Pawliw on L88, L110, L113, L122; other cited lessons unverified)"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/088-the-execution-problem.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/128-how-to-do-learnings-questions.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/046-ad-account-research.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/093-full-media-buying-strategy-outline-2026.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/094-how-to-set-up-a-3-2-2-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/100-how-to-see-ads-performance-our-columns.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/116-how-to-understand-facebook-ads-attribution.md
tags: [rubric, hub, qa, execution, ad-account-audit, media-buying, quality-gates]
updated: 2026-11-02
---

# Evolve Start Here rubrics hub
> Two scoring tools: the **execution checklist** judges an ad or script (13 execution checks, strategy-vs-execution test, retest limit); the **ad account audit** judges a Meta account (creative audit, ⛔ measurement gates, structure, performance and hygiene checks). Copy truth and psychology are scored by the Copywriting and Tether Lab rubrics.

## 🤖 Agent use
- **Use when:** a draft needs QA before launch, a researched ad lost, or an account needs a health check before you plan tests or scaling.
- **Inputs → outputs:** an ad (script, visuals, metrics) or an ad account (exports, targets, settings) → the matching scorecard with evidence per Fail, a verdict and routed fixes.
- **Rules:**
  - **DO** run gates first: Copywriting truth gates for ads; the audit's ⛔ G1-G4 (targets, 7-day click, click-based share, tracking) for accounts.
  - **DO** quote evidence (line, shot, setting, number) for every Fail.
  - **DON'T** let soft metrics decide: "focus on what actually matters, which is ROAS and CPA". [L88 32:17](../lessons/088-the-execution-problem.md)
  - **DON'T** fail an account for missing structures below their spend gate (ABO scaling, 3:2:2:2, separate whitelisting). [L93 00:00](../lessons/093-full-media-buying-strategy-outline-2026.md)
  - **IF** an angle failed three honest executions **THEN** change the angle. [L88 33:16-34:04](../lessons/088-the-execution-problem.md)
- **See also:** [Playbooks hub](../playbooks/README.md) · [Libraries hub](../libraries/README.md) · Copywriting: [rubrics hub](../../copywriting/rubrics/README.md) · Tether Lab: [rubrics hub](../../../../rubrics/README.md)

| Rubric | Applies to | Output | Pass | Used in |
|---|---|---|---|---|
| [Execution checklist](execution-checklist.md) | any script, static or brief before launch; any researched ad that lost | 13-row Pass/Fail with fixes; strategy-vs-execution verdict; next test | no truth-gate fail; 13/13 ship, 11-12 fix then ship, ≤ 10 rewrite (derived bands) | [learnings review](../frameworks/learnings-review.md), [launch end to end](../playbooks/launch-a-new-product-end-to-end.md), [weekly routine](../playbooks/weekly-media-buying-routine.md) W7, [rewrite losers and iterate](../frameworks/rewrite-losers-and-iterate.md) |
| [Ad account audit](ad-account-audit.md) | a Meta account with spend history: onboarding, stalled scale, quarterly check | creative-audit block + scored S/M/P/H checks + fix routing (`ad_account_audit` YAML) | no ⛔ gate fail; ≥ 85% healthy, 65-84% fix this week, < 65% rebuild beside old campaigns (derived bands) | [launch end to end](../playbooks/launch-a-new-product-end-to-end.md), [weekly routine](../playbooks/weekly-media-buying-routine.md) prerequisites, [research stack workflow](../frameworks/research-stack-workflow.md) (ad-account research step) |

## Order of use
| Order | Tool | Course | Judges |
|---|---|---|---|
| 1 | [Copy checklist scorecard](../../copywriting/rubrics/copy-checklist-scorecard.md) ⛔ gates | Evolve Copywriting | product truth, no fabricated proof, no fake urgency, copy the mechanism not the asset |
| 2 | [Execution checklist](execution-checklist.md) | Evolve Start Here | emotion, curiosity, suspense, grade ≤ 6, empty/bossy/repetitive claims, spoken voice, customer language, angle specificity and crowding, editing style, format fit |
| 3 | [14 questions](../frameworks/learnings-review.md#procedure-d-the-14-questions-pre-launch-qa-and-post-test-diagnosis) | Evolve Start Here | brief-level QA: right user hooked, native, label, camouflage, core desire taught, differentiation ([L128](../lessons/128-how-to-do-learnings-questions.md)) |
| 4 | [Ad scorecard](../../../../rubrics/ad-scorecard.md), [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) | Tether Lab | zone, self, heuristics, proof integrity, story structure |
| 5 | [Ad account audit](ad-account-audit.md) | Evolve Start Here | account structure, measurement, test hygiene, scaling discipline (L46, L92-121) |
| 6 | [Landing page scorecard](../../../../rubrics/landing-page-scorecard.md) | Tether Lab | the page the ads send to (Start Here has no page rubric) |

## Related
[Learnings review](../frameworks/learnings-review.md) · [KPI thresholds](../libraries/kpi-thresholds.md) · [Winning-ad labels](../concepts/winning-ad-labels.md) · [Campaign structure 3:2:2](../frameworks/campaign-structure-322.md) · [Scaling rules](../frameworks/scaling-rules.md)
