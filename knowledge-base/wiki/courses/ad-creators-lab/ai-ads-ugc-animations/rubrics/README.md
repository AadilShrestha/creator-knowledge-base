---
title: "Ad Creators Lab rubrics hub"
type: rubric
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (roast scorecard, 083–084); Ad Creators Lab (AI video failure modes across lessons)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
tags: [rubric, hub, qa, scorecard, ai-video, compliance]
updated: 2026-11-13
---

# Ad Creators Lab rubrics hub
> Two quality gates for AI-produced ads: a yes/no QA checklist for generated footage and the course's own 4-part /20 roast scorecard with a compliance line. Run them in the order below; any compliance failure blocks the ad.

## 🤖 Agent use
- **Use when:** after generation (per clip), after the edit (master), and before any upload; when ranking variants.
- **Inputs → outputs:** clip, master or static + script + product photos + context (avatar, awareness, offer, page) → QA log, scorecard, verdict (SHIP / FIX / BLOCK), top fixes.
- **Rules:**
  - **DO** run the claim audit on the script and prompt pack before generating, then the QA checklist per clip, then the full checklist and scorecard on the master.
  - **DO** use a separate reviewer (another agent or a person) and keep a human final yes/no [L93 50:59–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
  - **DON'T** let a high score override a compliance fail or live results.
- **See also:** [Playbooks hub](../playbooks/README.md) · [Shared rubrics hub](../../../../rubrics/README.md) · [RMBC claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

| Rubric | Applies to | Output | Pass mark | Used in |
|---|---|---|---|---|
| [AI video QA checklist](ai-video-qa-checklist.md) | every generated clip (sections A–F) and every finished AI video (A–H) | `ai_video_qa` (YES/NO per item, blockers, verdict) | No ⛔ item NO; <3 other NO on the master (derived) | [AI UGC](../playbooks/produce-an-ai-ugc-ad.md), [animated](../playbooks/produce-an-animated-ai-ad.md) |
| [Ad roast scorecard](ad-roast-scorecard.md) | any video, static or script with shot list | `roast_scorecard` (hook, clarity, sells, execution 0–5; /20; compliance line) | ≥15/20, no criterion <3, compliance PASS (derived; the course sets no threshold) | all four playbooks |

## Gate order
| # | Gate | When | Blocks on |
|---|---|---|---|
| 1 | [RMBC claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | Script, prompt pack, headline bank, lyrics, before generation | Any unsourced claim or fabricated proof |
| 2 | [AI video QA](ai-video-qa-checklist.md) A–F | Each clip | ⛔ items (product, label, words, text, sync) |
| 3 | [AI video QA](ai-video-qa-checklist.md) A–H | Master | ⛔ items incl. safe zone and compliance |
| 4 | [Ad roast scorecard](ad-roast-scorecard.md) | Master or static | Compliance line FAIL; score below pass |
| 5 | Human final yes/no, paused upload | Before spend | Any doubt |

## Related rubrics in other courses
| Rubric | Course | Use alongside for |
|---|---|---|
| [Ad scorecard (100 pt)](../../../../rubrics/ad-scorecard.md) | Tether Lab (shared) | Full written teardown or justification |
| [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) | Tether Lab (shared) | Script before the director's brief |
| [Copy checklist scorecard](../../../evolve/copywriting/rubrics/copy-checklist-scorecard.md) | Evolve Copywriting | Copy craft |
| [Execution checklist](../../../evolve/start-here/rubrics/execution-checklist.md) | Evolve Start Here | Concept before production |
| [Landing-page scorecard](../../../../rubrics/landing-page-scorecard.md) | Tether Lab (shared) | Page fit when CTR is high and conversion low [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md) |
