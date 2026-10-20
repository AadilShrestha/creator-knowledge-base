---
title: "Three Selves Diagnostic (score an ad for Actual / Ideal / Ought)"
type: framework
course: tether-lab
module: 04-self-targeting-system
sources:
  - raw/tether-lab/_transcripts/4. The Self Targeting System/2. Diagnose Which Self Your Ads Target.txt
  - raw/tether-lab/_transcripts/4. The Self Targeting System/5. Run The 3 Selves Diagnostic on Your Ads.txt
  - raw/tether-lab/_transcripts/4. The Self Targeting System/6. How to Use The Prompts For Instant Insights.txt
  - raw/tether-lab/_extracted/4. The Self Targeting System/11. 3-Selves Course - Prompts.md
  - raw/tether-lab/_extracted/4. The Self Targeting System/10. eBook Which ‘You’ Are You Selling To (2).md
tags: [framework, diagnostic, three-selves, ad-teardown, scoring, competitor-research]
updated: 2026-10-20
---

# Three Selves Diagnostic
> A runnable procedure to score any ad, script or batch of ads (ours or a competitor's) on **Actual / Ideal / Ought** (0–10), find the dominant self, and spot the **missing selves** that become the next angle variants.

## 🤖 Agent use
- **Use when:** step 1 of a competitor teardown or our own account audit. Before writing variants, find out which identity a winning ad activates and which ones nobody in the niche is using.
- **Inputs → outputs:** 1–20 ads (image, copy, or video transcript; optional CTR/CVR/ROAS/AOV/LTV) → per-ad scores + justification, a summary table, dominant self, under-used selves and next test directions (output format below).
- **Rules:**
  - DO score copy **and** visuals: headline, subhead, primary text, badges, buttons, callouts, image, on-screen text [L5 03:30].
  - DO score all three selves independently, 0 = not present, 10 = dominant focus (e-book). Selves can co-exist.
  - DO justify every score in 1–2 sentences quoting the cue words (prompt doc).
  - DO classify by **motivation frame**, not tense: "your future self will thank you" = Ought.
  - DO sample 9 (3 top / 3 mid / 3 flop) for an account audit [L2 01:20].
  - DON'T analyse a whole library at once [L2 00:45].
  - DON'T read the result as customer preference without performance data. Without metrics it shows the *creator's default* [L2 02:40].
- **See also:** [3 selves](../concepts/three-selves.md) · [Three selves prompts](../resources/three-selves-prompts.md) · next step: [Rewriting ads for new selves](rewriting-ads-for-new-selves.md) · then [Testing ads by self type](testing-ads-by-self-type.md)

## Inputs
| Input | Required? | Notes |
|---|---|---|
| Ads | Yes | Screenshots for statics. Transcript (+ key frame notes) for video. Sarah starts with statics because "core messaging first" is easier [L5 04:00] |
| Ad IDs / names | Strongly recommended | Naming conventions let the output map back to ads [L5 04:41] |
| Performance per ad | Optional | CTR, CVR, ROAS (Prompt 2). Add AOV, add-to-cart and LTV if you have them, to read the [L8 signatures](testing-ads-by-self-type.md#decision-table-read-the-result) |
| Sample design | For audits | 3 top / 3 mid / 3 flop. For competitors (no metrics), use proxies: longest-running, most variants or duplicates, recently paused *(agent adaptation)* |

## Scoring rubric (apply per ad)
Score each self **0–10** by how strongly the ad speaks to it (0 = not present, 10 = dominant focus).

| Signal | Actual Self | Ideal Self | Ought Self |
|---|---|---|---|
| Core frame | "Who I am right now": validate, keep consistent | "Who I want to be": become, grow, potential | "Who I should be": duty, standard, protect |
| Time / social orientation | Present | Future | Social expectation [L4 05:44] |
| Copy cues | "you already…", "made for people like you", "for [identity] who know", "this is so me", "exactly what I needed", "you earned this", "stick to what feels right", "finally, X that gets *you*" | "step into…", "unlock your next level", "the version of you who…", "finally becoming…", "one day I'll…", "for [legends] only", "what if this is the thing that finally works?", "your future self deserves" | "should", "you know you should…", "it's about time I…", "don't risk…", "don't let this fall through the cracks", "people are counting on you", "real adults…", "details matter", "your future self will thank you" |
| Emotion (e-book) | Comfort, pride | Hope, inspiration | Guilt, pressure (resolved into relief) |
| Trigger (e-book) | Seeking validation or alignment | Comparing self to who they want to be | Social norms or inner expectations |
| Typical proof / visual | Peer reviews ("from real wine lovers"), identity callouts, lifestyle-in-progress | Transformation, status, "legend"/elevated product hero shots, before→after upgrade comparisons [L6 07:18] | Authority/press ("As seen in…"), expert approval, safety/protection feature callouts, responsibility imagery (parent and child) |
| Sells | Reassurance: "you're already this person" | Hope, aspiration, thrill, progress | Relief and reassurance: "this is how you meet the standard" |

**Calibration examples (from the course):**
| Ad | Actual | Ideal | Ought | Why | Source |
|---|---|---|---|---|---|
| "No more skipping workouts. Your future self will thank you." | 1 | 7 | 9 | Doesn't affirm who they are · motivational future pacing · guilt-driven pressure | e-book p. 5 |
| "Your comfort shouldn't be negotiable." | 7 | 3 | 2 | Comfort as deserved (current identity) · slight self-care nod · weak responsibility angle | Prompt 2 example |
| "Rosé All Day" (High Camp) | 8 | 3 | 2 | Strong identity validation for wine lovers | [L6 05:37] |
| "He put up the tent, but you brought the flask." | high | low | low | Reinforces existing role. Calm, proven language (Sarah's label: Actual) | [L5 01:30] |
| "For campfire legends only." | – | high | – | Become the legend (Sarah's label: Ideal) | [L5 02:04] |
| "Because details matter, even outdoors." | – | – | high | You should care about details (Sarah's label: Ought) | [L5 02:34] |

## Procedure
1. **Collect** the sample (9 ads: 3/3/3, or a competitor set by proxy). Transcribe videos.
2. **Score each ad** with the rubric. In ChatGPT, paste [Prompt 1](../resources/three-selves-prompts.md#prompt-1-self-discrepancy-ad-analysis-no-performance-data) and upload the screenshots (delete the `[INSERT…]` placeholder), then reply "proceed" when asked [L6 03:14], [04:43]. As an LLM agent, apply the rubric directly.
3. **Justify** each score in 1–2 sentences, citing cue words and visual elements.
4. **Tabulate**: `Ad | Actual | Ideal | Ought | Dominant | Notes`.
5. **Summarise**: which self is most common; patterns *by ad type* (identity callouts vs product-hero vs comparison) [L6 06:37].
6. **If metrics exist**, run [Prompt 2](../resources/three-selves-prompts.md#bonus-prompt-2-self-discrepancy--performance-analysis): correlate dominant self with CTR/CVR/ROAS, find under-used selves, recommend a test ratio (e.g. 50% Actual / 30% Ideal / 20% Ought) and next test directions.
7. **Hand off** the winners plus their missing selves to [Rewriting ads for new selves](rewriting-ads-for-new-selves.md).

## Decision table: what to do with the result
| Finding | Interpretation | Action |
|---|---|---|
| One self is highest in most ads (≥ ~70%) *(threshold = agent heuristic)* | Default self / [angle rut](../concepts/angle-rut.md) | Rewrite top ads into the other two selves |
| Ideal dominates (most common case) | Aspirational rut. Segment will dry up [L3 00:58] | Prioritise Actual (AOV) and Ought (LTV) variants |
| Ideal dominates only on product-hero/comparison ads | Product-elevation habit [L6 06:57] | Write Actual/Ought versions of the product-hero ads specifically |
| Ought is near zero across the set | Untapped duty/protection lane | Brief Ought variants with authority proof. Plan for a slow start |
| Mixed scores on one ad (e.g. 5/6/5) | Unclear self, diluted message | Sharpen into single-self variants |
| Competitor's winners all share one self | That self works in the niche. The other selves are uncontested | Keep their mechanism, re-target it to an uncontested self for our product |
| With metrics: top ROAS ads are Actual, top CTR ads are Ideal | Matches [L8 signatures](testing-ads-by-self-type.md) | Use Ideal for prospecting volume, Actual for profitable conversion (e-book funnel guide) |

## Output format (for downstream agents)
```markdown
### Self diagnostic: <brand / set name> (<date>)
| Ad | Hook / headline | Actual | Ideal | Ought | Dominant | Key cues (copy + visual) |
|----|-----------------|--------|-------|-------|----------|--------------------------|
| A1 | "…" | 8 | 3 | 2 | Actual | "for wine lovers", peer reviews |

**Dominant self across set:** <self> (<n>/<N> ads)
**By ad type:** identity-callout → …; product-hero → …; comparison → …
**Under-used selves:** <self(s)>
**Performance link (if metrics):** <self> ↔ <metric pattern>
**Recommended ratio for next batch:** <e.g. 50% Actual / 30% Ideal / 20% Ought>
**Next test directions:** <e.g. "Test Ought framing using duty, responsibility, and protection angles" on A1, A4>
```

## Worked example (from the course)
![Slide: three High Camp ads with Ideal / Actual / Ought scores](../assets/tether-lab/04-self-targeting-system/05-score-output-0330.jpg)
*The lesson 5 output slide. ⚠️ Rows 2 and 3 look swapped versus the narration (campfire legends = Ideal, details matter = Ought). Don't use those numbers as calibration.*

![ChatGPT summary table: nine ads with Actual / Ideal / Ought scores and notes](../assets/tether-lab/04-self-targeting-system/05-summary-table-0430.jpg)
*A Prompt 1 summary table (9 High Camp ads). Notes like "Status-based Ideal Self play" and "Most responsibility-anchored" show the expected justification style. Full transcription in [lesson 5](../courses/tether-lab/04-self-targeting-system/05-run-the-3-selves-diagnostic-on-your-ads.md).*

High Camp takeaways (lesson 6): Actual is the most consistent (identity callouts), Ideal dominates product-hero ads, and Ought is minor (quality justifications) [L6 06:37–07:54].

## Self-spotting in customer language (for research and reviews)
Use the same cues on **reviews, survey responses, DMs** (e-book "pro tip") to learn which self *customers* speak from, then write in their words:
- Actual: "This is so me." "Exactly what I needed."
- Ideal: "One day I'll…" "Finally becoming…"
- Ought: "I should really…" "It's about time I…"

## Common mistakes
- Scoring copy only and ignoring the image or badges [L5 03:44].
- Treating any future reference as Ideal (see calibration example 1).
- Using an open prompt ("what do you see?") instead of numeric scoring. "Give chat some fences" [L6 04:18].
- Changing the offer in the follow-up test, which ruins attribution ([rewriting](rewriting-ads-for-new-selves.md)).

## Where it's taught
- [L2 Diagnose Which Self Your Ads Target](../courses/tether-lab/04-self-targeting-system/02-diagnose-which-self-your-ads-target.md) [01:13–02:50]
- [L5 Run the 3 Selves Diagnostic](../courses/tether-lab/04-self-targeting-system/05-run-the-3-selves-diagnostic-on-your-ads.md) [00:00–06:36]
- [L6 How to Use the Prompts](../courses/tether-lab/04-self-targeting-system/06-how-to-use-the-prompts-for-instant-insights.md) [02:50–08:33]
- E-book chapters 2, 3, 7: [Which 'You' Are You Selling To?](../resources/which-you-are-you-selling-to-ebook.md)

## Related
[3 selves](../concepts/three-selves.md) · [Actual](../concepts/actual-self.md) / [Ideal](../concepts/ideal-self.md) / [Ought](../concepts/ought-self.md) · [Angle rut](../concepts/angle-rut.md) · [Valence–intensity diagnostic](valence-intensity-diagnostic.md) (run next to pick the emotion) · [Prompt library](../courses/tether-lab/07-prompt-library/README.md)
