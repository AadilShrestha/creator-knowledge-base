---
title: "Rubric: Ad Scorecard (0–100, any ad or script, ours or a competitor's)"
type: rubric
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/frameworks/valence-intensity-diagnostic.md
  - knowledge-base/wiki/frameworks/three-selves-diagnostic.md
  - knowledge-base/wiki/frameworks/visual-weight-hierarchy.md
  - knowledge-base/wiki/frameworks/story-frameworks-for-ads.md
  - knowledge-base/wiki/frameworks/teep-journey.md
  - knowledge-base/wiki/concepts/heuristics.md
  - knowledge-base/wiki/contradictions.md
tags: [rubric, scorecard, qa, hook, clarity, zone, self, heuristics, specificity, proof-integrity, cta, visual-hierarchy, story-structure, teep, auto-fail]
updated: 2026-10-20
---

# Rubric: Ad Scorecard
> A weighted 0–100 score an agent applies to any static, UGC video or script, ours or a competitor's. Ten criteria, each scored **0–3** against concrete anchors from the course; criterion 9 is **visual hierarchy** for statics or **story structure** for video. Any **auto-fail** condition overrides the score.

## 🤖 Agent use
- **Use when:** QA before production (our scripts and statics); after a teardown, to see which criteria carry a competitor's winner; post-mortem on a loser (lowest criterion = first fix).
- **Inputs → outputs:** the ad or script (+ landing page + product truth sheet for our ads) → filled [scoring template](#scoring-template): per-criterion score with one line of evidence, total, band, auto-fail check, top 3 fixes.
- **Rules:**
  - DO score with evidence: quote the line or describe the frame for every score.
  - DO score the image/first frame first, then the largest headline / first line [V&I diagnostic, Step 0–1].
  - DO run the auto-fail list **before** totalling.
  - DO, for competitor ads, score proof integrity on what is visible and cap it at 2 when it can't be verified; never award points for their claims being "true".
  - DON'T use the score alone to pick winners; live results beat rubric scores ([test and iterate](../playbooks/test-and-iterate.md)). The weights are pipeline design.
- **See also:** [UGC script checklist](ugc-script-checklist.md) · [Landing-page scorecard](landing-page-scorecard.md) · [Rules library](../libraries/rules.md) · [Contradictions](../contradictions.md)

**Source key:** May7 = [Live May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · R1 = [Roast #1](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jul9 = [Live Jul 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · Jul16 = [Live Jul 16](../courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) · May21 = [Live May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · Jul2 = [Live Jul 2](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) · Chase = [Chase Mohseni](../courses/tether-lab/05-live-recordings/2025-06-guest-session-02-chase-mohseni.md) · M3 L1 = [The real reason your ad isn't working](../courses/tether-lab/03-valence-intensity-model/01-the-real-reason-your-ad-isnt-working.md) · M3 L3 = [The 4 emotional zones](../courses/tether-lab/03-valence-intensity-model/03-the-4-emotional-zones.md) · M4 L4 = [The 3 selves](../courses/tether-lab/04-self-targeting-system/04-the-3-selves-that-drive-every-buying-decision.md).

## Weights
| # | Criterion | Weight | Applies to |
|---|---|---|---|
| 1 | Hook strength (frame 1 / first 3 s) | 15 | all |
| 2 | Clarity, fluency, cognitive load | 10 | all |
| 3 | Emotional zone fit | 10 | all |
| 4 | Self fit | 8 | all |
| 5 | Heuristic use and stacking | 8 | all |
| 6 | Specificity | 9 | all |
| 7 | Proof integrity | 12 | all |
| 8 | CTA | 6 | all |
| 9 | 9a Visual hierarchy (static) **or** 9b Story structure (video/script) | 14 | one of the two |
| 10 | TEEP fit | 8 | all |
| | **Total** | **100** | |

Points per criterion = weight × score ÷ 3. Total = sum, rounded.

## Anchors (0–3)

### 1. Hook strength (15)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| No hook: logo, "hey guys", slow intro; core message absent in the first 3 s / frame 1 | Generic hook (category claim, "game-changer"); first visual unrelated to the line | Clear, specific hook in frame 1 with at least one heuristic; visual matches the line | Core message in frame 1 **and** a salient or pattern-breaking first visual that matches it, in the customer's words, with the heuristic in the hook |

Course basis: message in frame 1 [R3 0:18:56–0:21:32]; heuristics "mostly in hooks" [Jul9 0:53:44]; [salience](../concepts/heuristics/salience-bias.md); image read first [R3 0:32:37]; the brain reads an ad in ~0.2 s [May7 0:13:29] (Sarah's figure, uncited — don't quote it in copy).

### 2. Clarity, fluency, cognitive load (10)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| You can't say what it's about in one sentence; competing claims ("6 Day Results" + "30 Doses") | Message findable but cluttered; headline >7 words or 4+ line blocks | One message, minor clutter | One message, short lines, nothing competes; would read in a glance |

Basis: [processing fluency](../concepts/heuristics/processing-fluency.md); [cognitive load](../concepts/heuristics/cognitive-load.md); 4–7 words, ≤3 lines [R1 0:14:42; 0:36:37]; claim congruence [Jul16 0:55:36–0:59:47].

### 3. Emotional zone fit (10)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Unmapped / under-emotional ("speaks to logic, not emotion"), or a misfire against the buyer's state, or shames the viewer | Zone identifiable but weakly expressed, or intensity off for the motive (calm ad for an energy product) | Zone matches the purchase motive and buyer state; copy and visuals mostly agree | Zone fits state + motive, and verbs, visuals and promise all push the same way; Z3/Z4 aimed at a situation or industry belief and ends in hope |

Basis: [V&I diagnostic Step 6](../frameworks/valence-intensity-diagnostic.md#step-6-choose-the-target-zone-decision-rules); "it's your vibe" [M3 L1 01:25]; don't trigger a negative sense of self [Jun11 0:20:12–0:21:13]; end with hope [Jun4 0:30:17].

### 4. Self fit (8)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Diluted (scores like 5/6/5) or the wrong self for the stage (raw guilt Ought to cold traffic, no relief) | A dominant self, but promise, verb or proof contradict it | Clear self with a matching proof type | Clear self; promise, verb, identity callout and proof all match the [shift table](../frameworks/rewriting-ads-for-new-selves.md#shift-table-what-changes-when-you-move-to-each-self); right self for the stage |

Basis: [three-selves rubric](../frameworks/three-selves-diagnostic.md#scoring-rubric-apply-per-ad); Ought must resolve to relief [M4 L4 05:36]; Ought after qualification ([contradictions](../contradictions.md) row 17).

### 5. Heuristic use and stacking (8)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| None, or manipulative ("sneakier") | One heuristic, or 4+ fighting each other, or only the expected trio stuck on | 2–3 heuristics with fluency as the base, supporting the message | 2–3 stacked, at least one in the hook, chosen from the customer's belief/season, badges as "supporting characters" |

Basis: [heuristics hub](../concepts/heuristics.md); [heuristic stacking](../concepts/heuristic-stacking.md); "secondary characters" [May7 0:13:03–0:13:29]; belief and season [Jul2 0:13:34–0:15:40].

### 6. Specificity (9)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Umbrella emotion and claims any competitor could make ("real ingredients", "confidence") | Some specifics, still generic overall | A specific situation **or** a specific sub-emotion | A situation "four levels deep", exact names/numbers, customer words, typed proof ("350,000 tea drinkers") |

Basis: [specificity](../concepts/heuristics/specificity.md); [emotion specificity](../concepts/emotion-specificity.md) [Jun4 0:38:43]; "every other bowl was a failure" [R3 0:33:42]; ownable details [R1 0:05:15–0:06:19]; typed proof [Jul16 0:39:20].

### 7. Proof integrity (12)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| (Any fabrication is an auto-fail.) No proof where the claim needs it | Vague or untyped proof ("thousands love it"), or proof that doesn't answer the main objection | Real proof, but weakly matched to the self or the ability crusher | Real, verifiable, typed proof matched to the self and the biggest ability crusher; demonstrated on camera where possible |

Basis: never fabricate ([contradictions](../contradictions.md) row 10); proof by self ([shift table](../frameworks/rewriting-ads-for-new-selves.md)); [Fogg ability crusher](../frameworks/fogg-behavior-model.md) [Jul16 0:27:14]; demonstration > assertion ([skeptic format](../frameworks/skeptic-format.md)). Competitor ads: cap at 2 unless proof is independently verifiable.

### 8. CTA (6)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| None, or only "Shop now" / "Learn more" | Generic CTA | Definitive CTA ("See how it works", "Get yours") | Definitive action verb, tied to a person or habit or a real offer reason, and it matches the landing page |

Basis: [active CTA language](../concepts/active-cta-language.md) [R1 0:26:52–0:29:09]; "start the routine your vet will notice" [May14 0:42:30].

### 9a. Visual hierarchy — statics (14)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Equal-weight scatter, two messages, or the image contradicts the headline | The heaviest element isn't the message | Ranks 1–3 mostly right; limits mostly met | Headline (4–7 words, ≤3 lines) heaviest → image that shows the promise → support; 1-2-3 grid; colour on our product; background supports the text |

Basis: [visual weight hierarchy](../frameworks/visual-weight-hierarchy.md#layout-rules-at-a-glance) [R1 0:19:55–0:40:44]; [hero-image ↔ copy congruence](../concepts/hero-image-copy-congruence.md).

### 9b. Story structure — video/script (14)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Feature list / no structure; message arrives after the scroll decision | Some structure but rushes to the solution (setup < ~1/2), no realism, or cuts too fast to attach | A named framework, setup ≥ ~1/2, a realism beat | Framework followed, ~2/3 setup, realism beat, solution in the last scenes, cuts every 2–4 s, message in frame 1 |

Basis: [story frameworks](../frameworks/story-frameworks-for-ads.md) — 2/3 setup [May14 0:19:45], realism [0:41:04], pace [0:43:30–0:48:12].

### 10. TEEP fit (8)
| 0 | 1 | 2 | 3 |
|---|---|---|---|
| Stage unclear, or the wrong job (a purchase ad doing all the persuading to cold traffic) | Stage identifiable, but depth mismatched (general copy at evaluation) | Stage clear and the ad does that stage's job | Stage clear, depth right (exploration general, evaluation situational), offer only at purchase, named for its campaign |

Basis: [TEEP](../frameworks/teep-journey.md) [May21 0:06:19–0:09:20]; evaluate = situational [R3 0:34:44–0:35:44].

## Auto-fail conditions (score = FAIL regardless of total)
| # | Condition | Why |
|---|---|---|
| AF1 | Any fabricated proof: reviews, testimonials, ratings, counts, press, endorsements, results, before/afters | Non-negotiable ([contradictions](../contradictions.md) row 10) |
| AF2 | Fake scarcity or urgency (stock, deadline, "selling out") not backed by `scarcity_real` | Fake scarcity backfires [Jul9 0:43:49] |
| AF3 | Ad ↔ page mismatch: a claim, offer, price or scarcity line the landing page doesn't repeat or contradicts | Mirror the ad on the page [R3 0:15:00–0:17:00]; vibe [Chase 0:08:26] |
| AF4 | Any claim not in the product truth sheet's `claims_allowed`, or a forbidden/regulated claim | Truth rule |
| AF5 | Uses a competitor's footage, exact script lines, characters, catchphrases, trademarks or claims | Copy the mechanism, not the asset |
| AF6 | Shames the viewer's self or triggers trauma (Z3/Z4 misuse) | [M3 L3 03:48]; [Jun11 0:21:13] |
| AF7 | Sarah's uncited stats presented as fact in copy ("0.48 s", "60,000× faster", "+13.6% likability") | [contradictions](../contradictions.md) |
| AF8 | A synthetic (AI) person delivering a testimonial or personal results | [AI UGC tools](../tools/ai-ugc-tools.md); truth rule |

For **competitor ads**, auto-fails are recorded as `their_risk` (e.g. AF1 on Net Positive's invented badge) and never block the teardown; they are a warning not to copy that element.

## Bands
| Total | Band | Action |
|---|---|---|
| 80–100 | Ship | Produce / launch |
| 65–79 | Revise | Fix every criterion scored ≤1, re-score |
| <65 | Rework | Back to [angle remix](../playbooks/angle-remix.md) or the script framework |
| any + auto-fail | Fail | Remove the failing element; re-score from zero |

## Scoring template
```yaml
scorecard:
  id: SC-<asset id>
  asset: "<ad name / SCR / STA / TD id>"
  owner: ours | competitor
  format: static | video | script
  auto_fail:
    checked: [AF1, AF2, AF3, AF4, AF5, AF6, AF7, AF8]
    triggered: []                  # e.g. [AF2: "Only 9 left" not in scarcity_real]
  criteria:
    - {n: 1, name: hook, weight: 15, score: 0-3, evidence: "<quote/frame>"}
    - {n: 2, name: clarity, weight: 10, score: , evidence: ""}
    - {n: 3, name: zone_fit, weight: 10, score: , evidence: "zone Z?, buyer state …"}
    - {n: 4, name: self_fit, weight: 8, score: , evidence: "A/I/O = ?/?/?"}
    - {n: 5, name: heuristics, weight: 8, score: , evidence: "[slugs]"}
    - {n: 6, name: specificity, weight: 9, score: , evidence: ""}
    - {n: 7, name: proof_integrity, weight: 12, score: , evidence: "truth_refs …"}
    - {n: 8, name: cta, weight: 6, score: , evidence: ""}
    - {n: 9, name: visual_hierarchy | story_structure, weight: 14, score: , evidence: ""}
    - {n: 10, name: teep_fit, weight: 8, score: , evidence: "stage …"}
  total: <0-100>                   # Σ weight × score / 3
  band: ship | revise | rework | fail
  top_fixes:
    - "<lowest criterion → specific change, one variable>"
    - "<…>"
    - "<…>"
```

## Related
[Rubrics hub](README.md) · [UGC script checklist](ugc-script-checklist.md) · [Landing-page scorecard](landing-page-scorecard.md) · [Competitor ad teardown](../playbooks/competitor-ad-teardown.md) · [UGC script writing](../playbooks/ugc-script-writing.md) · [Static ad creation](../playbooks/static-ad-creation.md) · [One core emotion per ad](../concepts/one-core-emotion-per-ad.md) · [Psychology application ladder](../frameworks/psychology-application-ladder.md)
