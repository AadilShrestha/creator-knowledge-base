---
title: "VSL length bands"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guest data from Patrick Stiles (Vidalytics)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-01-vsls-section-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-05-vsl-product-buildup-and-reveal.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-08-medium-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-09-short-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [rmbc-ii, vsl, length, benchmarks, in-feed-video, short-vsl, long-form, vidalytics]
updated: 2026-11-02
---

# VSL length bands
> RMBC II works in four VSL bands (long, medium, 3–7 minute, short), but the course's own sources give different edges for each band; Patrick Stiles' Vidalytics data (guest claim) says straight-sale VSLs convert best near 20 minutes and worst near 45, with 15 and 35 minutes as sweet spots. Pick the band by placement, awareness, price and destination, then confirm length by word count, not the model's estimate.

## 🤖 Agent use
- **Use when:** choosing which VSL project to use; setting the target length in an outline prompt; cutting a long VSL down; reviewing a draft's runtime; deciding if a "VSL" is really a video ad.
- **Inputs → outputs:** placement (in-feed / on-page / upsell / pre-call), awareness gap, price/funnel type (straight sale vs book-a-call), destination → band + target minutes + target word count + which beats to keep.
- **Rules:**
  - **DO** pick the band before prompting and use that band's project. [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md); [08-01 recap doc step 1](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DO** size the band to the awareness gap: product-aware markets need little or no VSL; problem-aware markets need mechanism and education. [02-01 34:02–38:52](../lessons/02-01-product-market-awareness.md)
  - **DO** treat 1–7 minute "VSLs" as video ads: they "are almost always going to be honestly the same thing as video ads". [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **DO** measure length yourself; Claude claimed ~8,500 words for a script of 5,707 (script timer ~31 min). [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
  - **DO** prefer the middle of the long band for straight-sale VSLs: best ~20 min, worst ~45 min; book-a-call best ~25, worst ~60; "15 and 35 min VSLs convert highest"; near an hour "engagements and conversions just drop off a cliff" (guest claim, Patrick Stiles). [16-05 35:17–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
  - **DO** split-test the lead before the length: "the highest impact split test is always going to be split testing the lead of the video" (guest claim). [16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
  - **DON'T** run a long VSL on Meta by default; Stefan "would probably shoot for a shorter video ad" there. [07-01 v2 34:11–35:17](../lessons/07-01-long-form-vsl.md)
  - **DON'T** add a long VSL to a solution-aware commodity market: GetThin tested 7-minute VSLs for ~18 months, some "20% worse", never worth it (instructor claim). [13-01 57:20–1:00:01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)
  - **IF** the product's mechanism can be demonstrated or animated **THEN** a 1–10 minute in-feed mini-VSL → short page can replace a long page. [13-01 11:46–12:44](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)
  - **IF** you cut long → medium **THEN** keep every beat, shrink blocks (Airbnb 25 → 16–18 min: qualification/CTA 4–5 → 3–4 min). [07-02 v2](../lessons/07-02-medium-length-vsl.md)
  - **IF** the band is short **THEN** tell the model the brief won't all fit ("some of what is in the brief won't need to make it into these VSLs"). [07-04 v1 10:00](../lessons/07-04-short-vsl.md)
- **See also:** [classic-vsl-structure](classic-vsl-structure.md) · [claude-project-recipe](claude-project-recipe.md) · [product-market-awareness](product-market-awareness.md) · [sell-the-click](sell-the-click.md) · [vsl-review rubric](../rubrics/vsl-review.md) · [benchmarks library](../libraries/benchmarks.md)

## Definition
Four bands, one Claude Project each [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md). "VSL" in RMBC II spans a 60-minute on-page letter down to "two-minute VSLs that are really just like Meta ads. The line blurs." [08-01 14:08–14:45](../lessons/08-01-rmbc-ii-mid-course-recap.md)

### Ranges by source, side by side
| Band | 06-01 project instructions | Spoken elsewhere | Lesson-specific | Live runs (target) |
|---|---|---|---|---|
| **Long** | 25–60 min | Original RMBC: "20 to 50-minute, hour-long" [01-01 10:27](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | 07-01 "Use when": 25–60 min [07-01](../lessons/07-01-long-form-vsl.md) | Unity 27 min; Airbnb book-a-call 25 min ("15 minutes ... or 30, 40 minutes. There's a lot of variance" [07-01 v5 05:02](../lessons/07-01-long-form-vsl.md)) |
| **Medium** | 6–16 min | "a lot of them are going to be 6 to 18 minutes" [01-01 10:27](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | "typically like eight to 15 maybe at most 20 minutes" [04-08 v2 02:03](../lessons/04-08-medium-vsls-structures-and-examples.md); 07-02: "between 6 and 16 minutes" [07-02 v1 00:00](../lessons/07-02-medium-length-vsl.md) | Unity ~18 min (Claude: "18-20"); Airbnb 9 min and 16–18 min cut [07-02](../lessons/07-02-medium-length-vsl.md); [05-02 23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| **3–7 minute** | 3–7 min ("mini video sales letters", usually in-feed Meta, often tease) | ADHD hook ads "really in that three to seven minute VSL range" [08-01 02:55–03:25](../lessons/08-01-rmbc-ii-mid-course-recap.md) | Hook project named "ADHD Hook Ads Generator (1-6 Minutes)" [07-01 v4](../lessons/07-01-long-form-vsl.md); hook scripts 1–3 min [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) | Eye serum "3:30" (~550 words); blood sugar "3 min" scripts ~790–850 words [07-03](../lessons/07-03-3-7-minute-vsl.md) |
| **Short** | 1–4 min | "almost all one to two minutes" [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md); "a minute and a half, two minutes" [01-01 10:27](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | 04-09 structures: 1–5 min [04-09](../lessons/04-09-short-vsls-structures-and-examples.md); 07-04: 1.5–4 min [07-04](../lessons/07-04-short-vsl.md) | Airbnb 5 × 2 min; 1:30 test cut from a 3–7 script [07-03 v1 08:33](../lessons/07-03-3-7-minute-vsl.md) |
| **Upsell video** (not a project band) | 14-02 template: 6–16 min (same as 14-03 instructions) | "anywhere from 10 to 15 minutes, even 18" [14-02 v4 13:22](../lessons/14-02-upsells-case-studies.md) | Emma ~9 min; Synocell 12 min | — |

### Market examples cited for length
| Example | Length | Placement | Source |
|---|---|---|---|
| Nooro edema VSLs | 15, 16, 4 and 2 min under one caption; mini 6:36; medium ~16–17 min (17:25 card) | In-feed Meta | [12-01](../lessons/12-01-meta-ads.md); [04-01](../lessons/04-01-vsls-section-overview.md) |
| Miami MD | ~12–14 min | In-feed Meta | [12-01 17:33–19:58](../lessons/12-01-meta-ads.md) |
| Emma | VSL "like 50 minutes long"; video ads 5–30 min; ads "look four minutes long" | On-page + in-feed | [14-02 v4](../lessons/14-02-upsells-case-studies.md); [04-11 00:40–02:04](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md) |
| Alpilean long VSL | 49:56 | On-page | [04-02](../lessons/04-02-vsl-fundamentals-classic-structure.md) |
| Course handout examples | 6, 15, 35 min | — | [04-01](../lessons/04-01-vsls-section-overview.md) |
| Stefan's own skincare default | Video ads 30 s to "a couple of minutes" → PDP → checkout | In-feed | [13-01 1:00:01–1:01:32](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) |

### 16-05 benchmarks (all guest claims, Patrick Stiles, Vidalytics platform data; correlations, "these aren't split tests")
| Metric | Value | Source |
|---|---|---|
| Average VSL length | 36 min (2025) vs 31 min (2021) | [16-05 34:24](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Average length by niche | Biz Op 24 · Dating 30 · Golf 32 · Health 40 · Finance 59 min | [16-05 34:54](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Best / worst converting length | Straight sale 20 / 45 min · Book-a-call 25 / 60 min · Upsell 20 / 40 min | [16-05 35:17–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Sweet spot slide | "15 and 35 min VSLs convert highest" | [16-05 slide 53](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| CTA drop point | Best 30% of runtime; worst 79% | [16-05 36:12–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Engagement | 33% at 2 min · ~28% at CTA drop · 3% at end | [16-05 19:36](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Conversions at end of video | 47% come from the 3% who reach the end | [16-05 30:44–31:14](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Unmute | Avg 40% (top 10%: 75%); avg unmute at ~7 s | [16-05 24:04–24:30](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Conversion rate | All videos 1.78%; book-a-call ~8% | [16-05 04:14](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |
| Mobile share | 72% (57% in 2021) | [16-05 44:27](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |

### Section shares inside a VSL (course doc "Rough Percentages")
Lead 5–10% · Background 10–15% · UMP 20% · UMS 15% · Build-up and reveal 10% · Close 35% (spoken bands slightly lower for lead/background). [04-05](../lessons/04-05-vsl-product-buildup-and-reveal.md) Multiply by target minutes to budget each section (derived).

## Why it matters
- Wrong band = wrong project = wrong structure: medium keeps the classic structure but shrinks it; short has "not really a lead". [04-08 v2 02:03](../lessons/04-08-medium-vsls-structures-and-examples.md); [04-09 v2 05:02–06:02](../lessons/04-09-short-vsls-structures-and-examples.md)
- Retention compounds: "If someone will stay for three minutes they're probably going to stay for 12 to 15 minutes, and if you get them to 12 to 15, they'll probably stay 20, 30 minutes" (instructor claim). [04-07 46:34](../lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md)
- Model estimates of length are unreliable in both directions (Claude low on medium, high on long; "3-minute" scripts at ~800 words). [05-02 23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md); [07-03](../lessons/07-03-3-7-minute-vsl.md)

## How to use (steps)
1. **Placement and destination first:** in-feed ad that sells the click, on-page VSL, upsell, or pre-call video. [04-11](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md); [07-04 v2 00:01–00:31](../lessons/07-04-short-vsl.md)
2. **Pick the band** (agent default table below) from placement, awareness gap and funnel type.
3. **Set word targets** (derived): ~150 words/min is the rate used in [07-03](../lessons/07-03-3-7-minute-vsl.md); the 07-01 script timer implies ~185 words/min (5,707 words ≈ 31 min). Budget 150–185 wpm and time the read.
4. **Budget sections** with the Rough Percentages.
5. **Prompt with the target minutes** and "estimated length" request; check the outline's timings add up. [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)
6. **After drafting,** count words and time a read; allow 3–4 minutes more for added leads (derived, [07-01](../lessons/07-01-long-form-vsl.md)).
7. **Post-launch,** diagnose with 16-05 benchmarks: below 33% at 2 min → replace the lead; below ~28% at CTA → lead-to-CTA stretch; below 3% at end → close. [16-05 slides 32–34](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) → [vsl-review](../rubrics/vsl-review.md)

### Agent default bands (derived)
| Band | Default target | Use for | Don't use for |
|---|---|---|---|
| Short | 1–2 min (max 4) | In-feed ad selling the click to a VSL/advertorial/PDP; hook tests | Explaining a new category from scratch |
| 3–7 min | 3–5 min | In-feed mechanism-heavy ad, tease + "watch the video" CTA | On-page main sales video |
| Medium | 8–16 min | In-feed long VSL or on-page VSL for problem/solution-aware cold traffic | Product-aware commodity markets |
| Long | 20–35 min (straight sale); 25 min (book-a-call) | On-page VSL for big education gaps, high price, high-ticket calls | Meta in-feed by default; anything near 45–60 min without niche data (Health/Finance averages run longer) |

## Examples
| Case | Band decision | Source |
|---|---|---|
| Unity eye serum: long 27 min, medium ~18 min, 3–7 min "3:30", short | Same brief, four bands | [07-01](../lessons/07-01-long-form-vsl.md)–[07-04](../lessons/07-04-short-vsl.md) |
| Airbnb arbitrage (~$8,000 coaching): 25-min book-a-call long → 16-min cut → 9-min medium → 5 × 2-min shorts | High ticket → book-a-call; cut down by shrinking blocks | [07-01 v5](../lessons/07-01-long-form-vsl.md); [07-02 v2](../lessons/07-02-medium-length-vsl.md); [07-04 v2](../lessons/07-04-short-vsl.md) |
| Nooro: 15, 16, 4 and 2-min videos under one caption: "Some people need a 15 minute video. Some people are like, this is too long." | Run several bands in parallel | [12-01](../lessons/12-01-meta-ads.md) |
| GetThin (solution-aware weight-loss telehealth): 7-min VSLs never beat the short funnel (instructor claim) | No VSL needed | [13-01 57:20–1:00:01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) |

## Common mistakes
- **Trusting the model's runtime label.** [07-03](../lessons/07-03-3-7-minute-vsl.md)
- **Assuming VSLs are getting shorter:** platform average rose 31 → 36 min (guest claim). [16-05 34:24](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
- **Optimizing engagement only:** engagement–conversion correlation is 28% and weakening; "people watch less and buy more" (guest claim). [16-05 14:33–16:27](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
- **Copying "CTA at 30 seconds"** from a nine-figure brand without AOV/LTV context (guest caution). [16-05 42:05–42:35](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
- **Moving an in-feed VSL onto a page unchanged**: same length, wrong lead. [04-11 09:59–11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | Then vs now lengths | 10:27 |
| [04-01](../lessons/04-01-vsls-section-overview.md), [04-02](../lessons/04-02-vsl-fundamentals-classic-structure.md) | Example lengths; 8-part spine | docx; 02:20–02:47 |
| [04-05 Build-up](../lessons/04-05-vsl-product-buildup-and-reveal.md) | Rough Percentages | doc |
| [04-07 Long financial](../lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md) | Retention ladder | 46:34 |
| [04-08 Medium](../lessons/04-08-medium-vsls-structures-and-examples.md) | 8–15, max 20 min | v2 02:03 |
| [04-09 Short](../lessons/04-09-short-vsls-structures-and-examples.md) | 1–5 min structures | v2 05:02–38:51 |
| [06-01 Projects](../lessons/06-01-claude-vsl-projects-setup-overview.md) | Official bands | 00:00–01:29 |
| [07-01](../lessons/07-01-long-form-vsl.md)–[07-04](../lessons/07-04-short-vsl.md) | Live runs and length checks | 07-01 v2 34:11; v3 01:13 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | "The line blurs" | 14:08–14:45 |
| [12-01 Meta](../lessons/12-01-meta-ads.md) | In-feed lengths in market | 17:33–23:32 |
| [13-01 Funnel factors](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) | Demonstrability, attention span | 11:46–12:44; 36:49 |
| [14-02 Upsells](../lessons/14-02-upsells-case-studies.md) | Upsell video length | v4 08:58–13:22 |
| [16-05 Benchmarks](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Length, CTA, engagement data (guest) | 34:24–42:35 |

## Cross-course notes
- **Evolve** is Meta-centred and works in short UGC/video-ad lengths; it has no long-VSL band. Evolve Start Here [KPI thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md) and [KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md) cover ad-level metrics (hook/hold), complementary to 16-05's player metrics. **Agent default:** for RMBC short/3–7 bands evaluate as video ads with Evolve KPIs; for on-page VSLs use 16-05 benchmarks.
- **Tether** [format variation ladder](../../../../frameworks/format-variation-ladder.md): length is one format variable; vary one at a time.

## Related
[classic-vsl-structure](classic-vsl-structure.md) · [claude-project-recipe](claude-project-recipe.md) · [sell-the-click](sell-the-click.md) · [modular-creative-and-hook-swaps](modular-creative-and-hook-swaps.md) · [funnel-selection-matrix](funnel-selection-matrix.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [vsl-review](../rubrics/vsl-review.md) · [benchmarks library](../libraries/benchmarks.md)
