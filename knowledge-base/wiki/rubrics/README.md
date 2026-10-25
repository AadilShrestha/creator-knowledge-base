---
title: "Rubrics hub"
type: rubric
creator: synthesis
course: tether-lab
sources:
  - knowledge-base/wiki/rubrics/
  - knowledge-base/wiki/frameworks/
tags: [rubric, hub, qa, quality-gates, scorecard, checklist]
updated: 2026-10-20
---

# Rubrics hub
> Scoring checklists an agent applies to an ad, script or page. They are the **quality gates** of the [playbook pipeline](../playbooks/README.md): nothing goes to production or gets budget without passing the relevant rubric. Anchors come from Tether Lab sources; weights and thresholds are pipeline design.

## 🤖 Agent use
- **Use when:** before production (scripts, statics), before launch (landing pages), and after a teardown (to see which criteria carry a competitor's winner).
- **Inputs → outputs:** an asset + its context (landing page, product truth sheet) → a filled scoring block with evidence, a band, auto-fail flags and the top fixes.
- **Rules:** run auto-fails first; score with quoted evidence; fix the lowest criterion first, one variable at a time; live results beat rubric scores.
- **See also:** [Playbooks](../playbooks/README.md) · [Rules library](../libraries/rules.md) · [Contradictions](../contradictions.md) · [AGENT-GUIDE](../../AGENT-GUIDE.md)

| Rubric | Applies to | Output | Pass mark | Used in |
|---|---|---|---|---|
| [Ad scorecard](ad-scorecard.md) | any static, video or script, ours or a competitor's | `scorecard` (0–100, 10 weighted criteria, auto-fails AF1–AF8) | ≥80, no auto-fail | [teardown](../playbooks/competitor-ad-teardown.md), [static creation](../playbooks/static-ad-creation.md), [UGC script writing](../playbooks/ugc-script-writing.md) |
| [UGC script checklist](ugc-script-checklist.md) | every UGC script before the creator brief | `ugc_checklist` (pass / fix / block) | no ⛔ item failed, <3 other fails | [UGC script writing](../playbooks/ugc-script-writing.md), [creator brief](../playbooks/creator-brief.md) |
| [Landing-page scorecard](landing-page-scorecard.md) | landers, PDPs, advertorials (ours and competitors') | `lp_scorecard` (0–100, 6 sections, auto-fails LP1–LP5) | ≥80, no auto-fail | [teardown](../playbooks/competitor-ad-teardown.md), [test and iterate](../playbooks/test-and-iterate.md) |

Related diagnostics that work like rubrics: [valence-intensity diagnostic](../frameworks/valence-intensity-diagnostic.md) (zone scoring), [three-selves diagnostic](../frameworks/three-selves-diagnostic.md) (self scoring 0–10), [3 Vs check](../frameworks/three-vs-of-creative.md) (vibe / variety / velocity).
