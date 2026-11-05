---
title: "Click-based attribution (7-day click over view-through)"
type: concept
creator: evolve
course: start-here
instructor: "Spencer Pawliw (lessons 110, 112, 113, 120); unverified (lessons 92, 97, 101, 106, 115, 116, 117)"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/092-evolve-facebook-ads-philosophy.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/093-full-media-buying-strategy-outline-2026.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/097-how-to-set-up-abo-scaling-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/101-how-to-set-targets-kpis.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/106-turning-on-seasonal-ads-for-quick-performance.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/109-how-to-set-up-naming-templates.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/110-winning-ads-definition-part-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/112-winning-ad-definitions-0-mo-1m-mo.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/113-how-to-generate-submit-winning-ad-report.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/115-how-to-scale-facebook-ads-up-down.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/116-how-to-understand-facebook-ads-attribution.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/117-how-to-view-attribution-in-tw-triple-whale.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/154-how-to-contact-winning-creators-affiliate.md
tags: [attribution, 7-day-click, 1-day-view, view-through, incrementality, triple-whale, nc-roas, scaling-gate, meta-ads]
updated: 2026-11-02
---

# Click-based attribution (7-day click over view-through)
> "Click Based = Good, View Through = No Good": Evolve judges, labels and scales ads on **7-day-click** purchases, checks how much reported ROAS is only 1-day view, requires 60%+ click-based purchases before scaling, and reads Triple Whale only at channel level for incrementality.

## 🤖 Agent use
- **Use when:** reading a Meta ROAS before scaling or killing; labelling a test ad; explaining why Meta, Shopify and Triple Whale disagree; diagnosing roller-coaster days or a high reported ROAS that will not scale; choosing a campaign attribution setting; judging a creator's ad results.
- **Inputs → outputs:** Ads Manager data with **Compare attribution settings** (7-day click, 1-day click, 1-day view), daily spend, email-send dates, returning-customer rate, Triple Whale TA / Total Impact / NC ROAS → click share of purchases, click ROAS vs target, a scale/wait decision, and whether to test a 7-day-click-only campaign.
- **Rules:**
  - **DO** use 7-day click as the performance basis. [L116 page text; 00:00; 08:10](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **DO** label winners only on click-based data (7-day or 1-day click): "View data is not incremental from what we have seen." [L110 09:38–11:18](../lessons/110-winning-ads-definition-part-1.md); [L112 doc](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md)
  - **DO** require **60%+ of purchases click-based, or click data alone meeting KPI**, before raising budget; otherwise wait 24 hours. [L115 03:23–05:51; 07:13–08:23](../lessons/115-how-to-scale-facebook-ads-up-down.md)
  - **IF** most purchases are view-through (example: 77 of 234 click-based = 32%) **THEN** duplicate winners into a 7-day-click-only campaign and compare. [L116 09:32–10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **IF** spending >$1,000/day (or a bad view-through problem at any spend) **THEN** set campaigns to 7-day click; **IF** under $1,000/day and short of data **THEN** 7-day click + 1-day view. [L116 10:50–12:11](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **DON'T** read a high reported ROAS (7.79x) as performance when click ROAS is 2.83x. [L116 07:02–08:10](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **DON'T** credit the ad account for email-day spikes. [L116 03:45](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **DON'T** use Triple Whale for ad-set or ad decisions; use it per channel, window 14 days, Meta on TA (click). [L117 00:00; 04:21–06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)
  - **DON'T** expect the switch to fix scale: "Is this going to scale your ad account from $1,000 to $10,000 per day? Absolutely not." [L116 10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md)
  - **DON'T** judge a low-spend ad by its own attributed purchases; low-spend ads can "hog view through attribution". [L92 05:53](../lessons/092-evolve-facebook-ads-philosophy.md)
- **See also:** [winning-ad-labels](winning-ad-labels.md) · [revenue-stage-focus](revenue-stage-focus.md) · [KPIs and columns](../frameworks/kpis-and-columns.md) · [Scaling rules](../frameworks/scaling-rules.md) · [Campaign structure 3:2:2](../frameworks/campaign-structure-322.md) · [Ad account audit](../rubrics/ad-account-audit.md) · [KPI thresholds](../libraries/kpi-thresholds.md)

## Definition
- **Attribution does two jobs:** it tells Meta whom to optimise toward, and it is how Meta reports purchases back. [L116 00:00](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- **7-day click:** purchase within 7 days of a click (a later re-click restarts the window). **1-day click:** purchase within 24 hours of a click. **1-day view:** purchase within a day of seeing (not clicking) the ad. [L116 01:11; 05:58](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- **Click share** = 7-day-click purchases ÷ total purchases (derived from [L116 09:32](../lessons/116-how-to-understand-facebook-ads-attribution.md)).
- **Net new customers** is the second non-negotiable: check new-visitor % (Northbeam/Triple Whale); "for 98% of businesses" growth means new customers (instructor claim). [L110 11:18–12:01](../lessons/110-winning-ads-definition-part-1.md)
- **Triple Whale glossary** (page text): TI = which channel is incremental; TA = click-through ROAS; TA+V = click + view; FC = first click; LC = last click; "TA combines FC and LC". [L117 page](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)

## Why it matters
- View-through inflates Meta numbers for three reasons: email sends, returning customers (cheapest buyers), organic and influencer activity. Result: "you might start overspending dramatically". [L116 03:45–05:58](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- "You spent seven K at a five, why didn't you spend more? It's because our actual seven day click KPI was not meeting the target KPI." [L116 05:58](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- Switching one brand to a 7-day-click campaign: ~3x the spend at 3.13x click ROAS vs the 7DC1DV campaign's 2.83x click ROAS (reported 7.79x) (instructor's account; "a very specific view-through problem"). [L116 07:02–10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- Platform revenue always exceeds reality: TA showed 500K+ vs about 390K on Total Impact ("ad platforms want to take credit"). [L117 01:24](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)
- A 2x platform ROAS can be 0.8x NC ROAS: "You're just targeting the same customers that have bought before." [L117 05:49](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)

## How to use (steps)
1. In Ads Manager: Columns → **Compare attribution settings**; add 7-day click and 1-day click. Optionally "see only the first conversion". [L116 02:32](../lessons/116-how-to-understand-facebook-ads-attribution.md)
2. For the campaign/period record: total purchases, 7-day-click purchases, 1-day-view purchases, reported ROAS, 7-day-click ROAS. [L116 02:32–03:45](../lessons/116-how-to-understand-facebook-ads-attribution.md)
3. Compute click share; compare with the 60% scaling gate. [L115 04:36–05:51](../lessons/115-how-to-scale-facebook-ads-up-down.md)
4. At ad level, flag any ad with spend and zero click purchases ("collecting attribution"; one had nine purchases, zero click). [L116 09:32–10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md)
5. Mark email-send days, returning-customer rate, influencer activity. [L116 03:45–05:58](../lessons/116-how-to-understand-facebook-ads-attribution.md)
6. Decide the setting (table below). If view-through dominates, run a 7-day-click-only duplicate campaign with the same ads. [L116 07:02; 12:11](../lessons/116-how-to-understand-facebook-ads-attribution.md)
7. Check incrementality at channel level in Triple Whale (14-day window, TA + Total Impact + NC ROAS) and blended Shopify sales. [L117 06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md); [L97 12:17](../lessons/097-how-to-set-up-abo-scaling-campaign.md)
8. Store click share and click ROAS beside reported ROAS in every report; standardise reports to USD and 7-day click. [L113 01:21](../lessons/113-how-to-generate-submit-winning-ad-report.md)

### Attribution setting by situation
| Situation | Setting / action | Source |
|---|---|---|
| Spend under $1,000/day, need data | 7-day click + 1-day view (still judge on 7-day click) | [L116 11:50–12:11](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Spend over $1,000/day | 7-day click | [L116 12:11](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Majority of purchases view-through, any spend | Test 7-day-click-only campaign | [L116 09:32–12:11](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Healthy click share (~70%) | Still test a 7-day-click campaign "to see if Facebook optimizes differently" | [L116 10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Spend over $100,000/day | Start watching 1-day click | [L116 10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Main CBO on 7-day click, proven ads | Optional ABO test ad sets: hard exclusions (7DC), 1-day click (exclude purchasers), Meta incremental attribution (strong exclusions) | [L97 08:52–11:33](../lessons/097-how-to-set-up-abo-scaling-campaign.md) |
| Roller-coaster days | Check view-through attribution first | [L116 10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md) |

### Triple Whale read-out by channel
| Channel | Read | Conclude | Source |
|---|---|---|---|
| Meta, TikTok, AppLovin, Snapchat, Pinterest | TA + Total Impact; ignore TA+V | Incremental or not; scale on TA vs target | [L117 00:00; 11:48](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |
| Google search/shopping | TA, First Click, Last Click, NC ROAS; discount branded search (20x+ "isn't incremental") | Prospecting if first-click on target and last-click lower | [L117 08:16–11:48](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |
| Google YouTube/Display | Total Impact | Upper-funnel incrementality | [L117 11:48–13:17](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |

## Examples (from the lessons)
| Case | Reported | Click-based | Lesson read | Source |
|---|---|---|---|---|
| September ad set, ~$5,000 spend | 120 purchases, ROAS 5.32 | 43 on 7-day click (77 1-day view), ROAS 2.24 | Inflated | [L116 02:32–03:45](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| October 7DC1DV vs 7DC campaigns | 7.79x on ~$8K | 2.83x vs 3.13x on ~$24K | Switch scaled spend | [L116 07:02–08:10](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Scaling-protocol demo | 111 purchases, campaign ROAS 2.59 | 104 click-based, click ROAS 2.4 | Passes 60% gate | [L115 04:36](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| Creator ad | $66 spend, 1 purchase | "99.9% sure it was view through" | Don't hire on it | [L154 00:38](../lessons/154-how-to-contact-winning-creators-affiliate.md) |
| Meta in Triple Whale (30 days) | Platform 2.42 | TA 2.38; Total Impact 3.09 | Meta incremental | [L117 00:00; 03:20 frame](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |

## Common mistakes
- Scaling off reported ROAS without the click check. [L115 03:23–05:51](../lessons/115-how-to-scale-facebook-ads-up-down.md)
- Leaving the Triple Whale window on lifetime ("very inaccurate"). [L117 05:49–06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)
- Comparing a Triple Whale campaign ROAS with Meta's: survey purchases sit in one "Triple Survey" bucket. [L117 04:21](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)
- Judging a new creative on day-1 ROAS when 1-day and 7-day click diverge. [L116 05:58](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- Treating the 7-day-click switch as a fix-all. [L116 10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md)
- Relying on Facebook alone: "Facebook only has a seven-day attribution window"; use blended ROAS (MER) too, especially for new brands. [L101 05:59](../lessons/101-how-to-set-targets-kpis.md)

## Where it's taught
| Lesson | What it adds | Timestamps |
|---|---|---|
| [L92 FB ads philosophy](../lessons/092-evolve-facebook-ads-philosophy.md) | Low-spend ads hog view-through / last click | [05:53] |
| [L93 Media buying outline](../lessons/093-full-media-buying-strategy-outline-2026.md) | 1-day-click and incremental-attribution test ad sets | [01:45–02:47] |
| [L97 ABO scaling](../lessons/097-how-to-set-up-abo-scaling-campaign.md) | Hard exclusions / 1-day click / incremental ad sets; incrementality check | [08:52–12:17] |
| [L101 Targets & KPIs](../lessons/101-how-to-set-targets-kpis.md) | Blended ROAS vs in-platform; 7-day window limit; NCPA only above ~$50K/month | [05:59–09:26] |
| [L106 Seasonal ads](../lessons/106-turning-on-seasonal-ads-for-quick-performance.md) | Relaunch some ad sets at 7-day click only | [07:44–08:34] |
| [L109 Naming templates](../lessons/109-how-to-set-up-naming-templates.md) | `7DC-1DV` / `7DC` in names | doc |
| [L110 Definition part 1](../lessons/110-winning-ads-definition-part-1.md) | Click-based + net-new customers are non-negotiable for labels | [09:38–12:01] |
| [L112 Definitions](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md) | Same, doc "Mission" | doc |
| [L113 Generate report](../lessons/113-how-to-generate-submit-winning-ad-report.md) | Reports in USD + 7-day click | [00:00–01:21] |
| [L115 Scale up & down](../lessons/115-how-to-scale-facebook-ads-up-down.md) | 60% click-based gate; KPI on 7-day click | [03:23–08:23; 09:41] |
| [L116 FB attribution](../lessons/116-how-to-understand-facebook-ads-attribution.md) | Core lesson | [00:00–13:05] |
| [L117 Triple Whale](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) | Channel-level incrementality | [00:00–13:17] |
| [L120 Turn off high-spend ads](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) | Judge on click-based data | [04:25] |
| [L154 Contact winning creators](../lessons/154-how-to-contact-winning-creators-affiliate.md) | View-through purchase ≠ creator win | [00:38] |

## Cross-course notes
- **Evolve Copywriting:** no attribution lesson; its [Iteration outcomes](../../copywriting/concepts/iteration-outcomes.md) labels assume trustworthy spend/KPI data. Apply this page before using those labels.
- **Tether Lab:** no attribution guidance in the shared pages; [Creative testing system](../../../../frameworks/creative-testing-system.md) judges on CPA/CVR. Read those on 7-day click when the account is Meta.
- **Internal conflicts** (logged): 1-day click is fine for labels (L110/L112) and used as a test ad set (L97), but "don't worry about" it under $100K/day (L116); labels require click-only data (L110) while sub-$1K/day accounts run 7DC+1DV (L116). Default: optimise on the L116 setting for the spend level, but always *read and label* on 7-day click.

## Related
[winning-ad-labels](winning-ad-labels.md) · [revenue-stage-focus](revenue-stage-focus.md) · [whitelisting-and-partnership-ads](whitelisting-and-partnership-ads.md) · [KPIs and columns](../frameworks/kpis-and-columns.md) · [Scaling rules](../frameworks/scaling-rules.md) · [Weekly media-buying routine](../playbooks/weekly-media-buying-routine.md)
