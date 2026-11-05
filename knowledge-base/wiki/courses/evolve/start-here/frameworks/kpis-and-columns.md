---
title: "KPIs and columns (Evolve targets from margin, the Ads Manager column preset, custom metric formulas, read order and benchmarks)"
type: framework
creator: evolve
course: start-here
instructor: "Evolve (Spencer in L088, L100, L104; Spencer Pawliw in L110-L113; speaker unverified in L101, L107, L115-L117, L120); Shaun Eng in L108"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/046-ad-account-research.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/088-the-execution-problem.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/092-evolve-facebook-ads-philosophy.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/094-how-to-set-up-a-3-2-2-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/096-how-to-set-up-zombie-graveyard-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/097-how-to-set-up-abo-scaling-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/100-how-to-see-ads-performance-our-columns.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/101-how-to-set-targets-kpis.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/102-action-item-set-your-targets-kpis.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/107-how-to-protect-against-bad-ads-over-spending.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/110-winning-ads-definition-part-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/112-winning-ad-definitions-0-mo-1m-mo.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/113-how-to-generate-submit-winning-ad-report.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/115-how-to-scale-facebook-ads-up-down.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/116-how-to-understand-facebook-ads-attribution.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/117-how-to-view-attribution-in-tw-triple-whale.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/118-advanced-surf-scaling-method.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/121-how-to-deal-with-roller-coaster-performance.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/122-how-to-do-learnings-part-1-losers.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/124-how-to-do-learnings-part-3-losers.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/160-feedback-loops-with-your-brand-ambassadors.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/171-how-to-make-any-product-work-brand-building-pt-1.md
tags: [framework, kpi, targets, breakeven-roas, scaling-roas, blended-roas, mer, cpa, ncpa, ltv, columns, custom-metrics, hook-rate, hold-rate, ctr, cpm, cvr, aov, frequency, attribution, benchmarks]
updated: 2026-11-02
---

# KPIs and columns
> Set the brand's Breakeven and Scaling targets from gross margin (not a flat "3x"), pick the KPI level the account can measure, build one Ads Manager column preset with four custom metrics (AOV, CVR, Video Hook, Video Hold), and read every table in the same order: spend, then ROAS/CPA on click-based data, then AOV/CVR, then the soft metrics as diagnostics only.

## 🤖 Agent use
- **Use when:** setting or checking targets before any test or scaling decision; building or auditing an Ads Manager view; reading an export; diagnosing why an ad got spend but not sales (or the reverse); choosing which number (Meta, blended, Triple Whale) decides what.
- **Inputs → outputs:** price + shipping, unit cost + shipping, AOV, daily/monthly ad spend, Shopify revenue, Ads Manager export (with 7-day-click comparison), optional Triple Whale NCPA/LTV → a written target card (Breakeven and Scaling ROAS, CPA equivalents, KPI level), the column preset, a ranked read of ads, and a diagnosis per ad from the benchmark and symptom tables.
- **Rules:**
  - **DON'T** adopt a flat "3x ROAS": "It varies very much so based on what your actual profit margins are." At 65% margin, 2-2.5x is profitable and ~1.5x is break even. [L101 00:00; 02:17](../lessons/101-how-to-set-targets-kpis.md)
  - **DO** compute Breakeven ROAS = 1 ÷ gross margin and Scaling ROAS = Breakeven + 1 ("typically adding one point"), and write both down before reading any ad. [L101 01:40; 02:50](../lessons/101-how-to-set-targets-kpis.md) [L102 page](../lessons/102-action-item-set-your-targets-kpis.md)
  - **DO** sort by Amount spent and look only at ads with spend and results: "We only care about ads that are getting spend and ads that are getting results." [L100 00:00; 07:27](../lessons/100-how-to-see-ads-performance-our-columns.md)
  - **DO** judge on money ("You pay bills with money"): ROAS and CPA on 7-day-click data. Hook, hold, CTR and CPC are "soft metrics". [L100 00:56](../lessons/100-how-to-see-ads-performance-our-columns.md) [L088 32:17–33:16](../lessons/088-the-execution-problem.md) [L115 09:41](../lessons/115-how-to-scale-facebook-ads-up-down.md)
  - **DON'T** trust hook or hold without purchases ("We've seen ads with insane hook and hold rates just not perform at all"); images have no hook or hold. [L100 13:08](../lessons/100-how-to-see-ads-performance-our-columns.md)
  - **DON'T** scale on Facebook-reported ROAS alone; check blended ROAS (Shopify revenue ÷ total ad spend). [L101 05:59](../lessons/101-how-to-set-targets-kpis.md)
  - **IF** spend < ~$50k/month **THEN** use blended + in-platform ROAS; skip NCPA/LTV. [L101 07:38; 09:26](../lessons/101-how-to-set-targets-kpis.md)
  - **IF** a cheap-click ad takes spend at a poor ROAS **THEN** check landing-page views ÷ link clicks (78% on a click-bait ad vs ~100% on a healthy one). [L107 03:34–04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md)
  - **DON'T** use Triple Whale for ad-set or ad decisions; set its window to 14 days and read it per channel. [L117 04:21–06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md)
  - **DON'T** invent targets, benchmarks or results for a brand; compute them from its numbers or bracket the gap. [L102 page](../lessons/102-action-item-set-your-targets-kpis.md) (repo rule)
- **See also:** [Campaign structure 3:2:2](campaign-structure-322.md) · [Scaling rules](scaling-rules.md) · [Winning-ad labels](../concepts/winning-ad-labels.md) · [Click-based attribution](../concepts/click-based-attribution.md) · [KPI thresholds](../libraries/kpi-thresholds.md) (K060-K069, K120-K134, K180-K185) · [Rules](../libraries/rules.md) (KP01-KP13, SC11-SC19) · [Learnings review](learnings-review.md) · [Ad account audit](../rubrics/ad-account-audit.md) · Copywriting: [iteration outcomes](../../copywriting/concepts/iteration-outcomes.md)

**Labels:** "(instructor claim)" = result stated without independent check. "(derived)" = this page's arithmetic or combination. "page" / "doc" / "frame" = lesson page text, linked doc or on-screen value without a timestamp.

## 1. Definition
Three things, used together:
1. **Targets:** per-brand Breakeven and Scaling values at one of three KPI levels (BROAS, in-platform ROAS, CPA/NCPA + LTV). [L101 04:36–09:26; page](../lessons/101-how-to-set-targets-kpis.md)
2. **Column preset:** a saved Ads Manager column set with four custom metrics. [L100 00:56–05:39; page](../lessons/100-how-to-see-ads-performance-our-columns.md)
3. **Read order and benchmarks:** spend first, money second, soft metrics last, each with a stated threshold. [L100 05:39–15:34](../lessons/100-how-to-see-ads-performance-our-columns.md)

## 2. Why it matters
- Targets decide every later move: "above scaling ROAS → push budget; below → drop budget." [L101 09:26](../lessons/101-how-to-set-targets-kpis.md) The scaling flowchart asks "are we hitting target KPI?" and "are you below breakeven KPI?" ([scaling rules](scaling-rules.md)). [L115 00:00; 08:23](../lessons/115-how-to-scale-facebook-ads-up-down.md)
- A flat 3x leaves money on the table: at 65% margin, $3,000/month at 2.5x still makes $1,875 true profit (frame). [L101 02:17–03:00](../lessons/101-how-to-set-targets-kpis.md)
- Soft metrics mislead without spend: "there are ads with 50% hook rates that suck and ads with 20% hook rates that crush". [L088 32:17](../lessons/088-the-execution-problem.md)

## 3. Procedure A: set the targets
1. Collect **P** = price + shipping charged (e.g. $89.99 + $5 = $94.99; "if your product is $100 and you include shipping in that price, then you would just put $100") and **C** = unit cost + shipping cost (e.g. $25 + $10 = $35). [L101 00:00–00:53](../lessons/101-how-to-set-targets-kpis.md)
2. Gross margin **m = (P − C) ÷ P** (derived; the lesson uses a calculator, easyamedia.com/profit-calculator, with fees zeroed). [L101 00:53–01:27](../lessons/101-how-to-set-targets-kpis.md)
3. **Breakeven ROAS = 1 ÷ m** (frame: m 0.65 → 1.54; formula derived from the calculator output). [L101 01:40](../lessons/101-how-to-set-targets-kpis.md)
4. **Scaling ROAS = Breakeven ROAS + 1.** [L101 02:50](../lessons/101-how-to-set-targets-kpis.md)
5. CPA equivalents (derived, for CPA-run accounts): **Breakeven CPA ≈ AOV × m** (gross profit per order); **Scaling CPA ≈ AOV ÷ Scaling ROAS**. The lesson defines them only in words: "The maximum amount you can spend to acquire a customer" / "The ideal amount you are spending to acquire a customer". [L101 page](../lessons/101-how-to-set-targets-kpis.md)
6. Pick the KPI level (table below), store the card where the team sees it, reset it when margin, price or shipping changes. [L101 01:27; 04:36](../lessons/101-how-to-set-targets-kpis.md)
7. Daily budget input: "$50-$100/day... if you're spending less, that is fine"; monthly = daily × 30. [L101 01:27](../lessons/101-how-to-set-targets-kpis.md)

### KPI levels
| Level | KPI | Use when | Formula / tool | Source |
|---|---|---|---|---|
| Beginner | **BROAS** (blended ROAS, MER) | Few sales, little organic, mostly ad-driven | Shopify revenue ÷ total ad spend ($10,000 ÷ $4,000 = 2.5) | [L101 05:59; page](../lessons/101-how-to-set-targets-kpis.md) |
| Intermediate | **In-platform ROAS** + MER | More organic sales ($10-15k/month mostly organic) | Meta Purchase ROAS on 7-day click, checked against MER | [L101 06:52](../lessons/101-how-to-set-targets-kpis.md) |
| Advanced | **CPA / NCPA + LTV** (3, 6, 12 months) | ≥ ~$50k/month with Triple Whale | Breakeven CPA, Scaling CPA, LTV by cohort | [L101 07:38–08:30](../lessons/101-how-to-set-targets-kpis.md) |

### Target card (fill-in template, derived)
```text
Brand: ______   Date: ______   KPI level: BROAS | ROAS | CPA+LTV
P (price + shipping charged): $____   C (unit cost + shipping): $____
Gross margin m = (P − C) ÷ P = ____
Breakeven ROAS = 1 ÷ m = ____        Scaling ROAS = Breakeven + 1 = ____
AOV: $____   Breakeven CPA ≈ AOV × m = $____   Scaling CPA ≈ AOV ÷ Scaling ROAS = $____
Minimum daily spend (cash-flow floor, see scaling rules): $____
Attribution for decisions: 7-day click     Blended check: Shopify revenue ÷ total ad spend
```

### Worked numbers from the lessons
| Case | Inputs | Result | Source |
|---|---|---|---|
| Calculator frame | m = 0.65 | Breakeven 1.54 → Scaling 2.54 | [L101 01:40; 02:50](../lessons/101-how-to-set-targets-kpis.md) |
| Spoken inputs | P $94.99, C $35 | m ≈ 0.63 → Breakeven ≈ 1.58 → Scaling ≈ 2.58 (derived) | [L101 00:00](../lessons/101-how-to-set-targets-kpis.md) |
| 3x vs 2.5x, $3,000/month, 65% margin | 3.00x / 2.50x | $2,850 / $1,875 true profit; both profitable | [L101 02:20; 03:00 frames](../lessons/101-how-to-set-targets-kpis.md) |
| Spend beats ROAS | $10k at 4x vs $20k at 3.5x | ~$16k vs "25,000" profit (≈ $25.5k at 65%, derived) | [L101 03:41](../lessons/101-how-to-set-targets-kpis.md) |
| Blended (Triple Whale, 30 days) | $232,198 revenue, $72,449 ads | BROAS 3.20; client "happy" above 3x | [L101 05:27–05:30](../lessons/101-how-to-set-targets-kpis.md) |
| LTV | First cohort ~$241 → ~$282 by month 12 | Scale harder than first-order CPA allows | [L101 07:38–08:30](../lessons/101-how-to-set-targets-kpis.md) |

**IF** ROAS is very high (example 5x) **THEN** scale until it falls: lower ROAS at higher spend can make more total profit, especially once LTV exists. [L101 03:41](../lessons/101-how-to-set-targets-kpis.md) Price floors that make targets reachable: AOV $60+ after bundles; price ≥ 3x COGS + shipping. [L171 08:13; 09:12](../lessons/171-how-to-make-any-product-work-brand-building-pt-1.md)

## 4. Procedure B: build the column preset
Path: Ads Manager → Columns → Customize columns; delete bid strategy; for Purchases untick the sub-variants (mobile app, website, offline, Meta); reorder with the drag handle; save as a preset (he names it "$"); reselect the preset if the table shows "Custom". [L100 00:56–05:39](../lessons/100-how-to-see-ads-performance-our-columns.md)

### Column list (page text, canonical order)
```text
Campaign
Date created
Attribution setting
Delivery
Budget
Amount spent
Results
Cost per result
Purchases
Cost per purchase
Purchases conversion value
Purchase ROAS (return on ad spend)
AOV
CVR
Impressions
Reach
Frequency
CPM (cost per 1,000 impressions)
Link clicks
Cost per link click
Link CTR (click-through rate)
Video Hook
Video Hold
Video average play time
Adds to cart
Cost per add to cart
Checkouts Initiated
Cost per checkout initiated
URL parameters
```
Results and Purchases are both kept because "sometimes we will get shop orders" next to website purchases. [L100 07:27–08:21](../lessons/100-how-to-see-ads-performance-our-columns.md) The spoken build also uses unique outbound clicks/CTR, engagement rate and quality ranking; use the page list (derived choice on the [L100 page](../lessons/100-how-to-see-ads-performance-our-columns.md)). Engagement rate and quality ranking are "vanity metric[s]". [L100 14:55](../lessons/100-how-to-see-ads-performance-our-columns.md)

### Custom metrics ("Create custom metric")
| Metric | Formula | Format | Note | Source |
|---|---|---|---|---|
| AOV | Purchases conversion value ÷ Purchases | Currency | Shows which variant lifts basket size | [L100 03:43; frame 04:00](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| CVR | Purchases ÷ Landing page views | % | "You can do purchases divided by link clicks, but we typically do landing page views" | [L100 04:40; frame 04:50](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| Video Hook | 3-second video plays ÷ Impressions | % | Video only | [L100 04:40; 11:32](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| Video Hold | ThruPlays ÷ Impressions | % | ThruPlay = 15 s or full ad if shorter; "not three second plays by impressions" | [L100 04:40; 11:32](../lessons/100-how-to-see-ads-performance-our-columns.md) [L088 32:17](../lessons/088-the-execution-problem.md) |

### Add these for the decisions in the other two frameworks (derived from the cited lessons)
| Add | Formula / where | Why | Source |
|---|---|---|---|
| Landing page views + **LPV rate** | Landing page views ÷ Link clicks (custom metric) | Click-bait check (~78% bad vs ~100% healthy) | [L107 03:34–04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) |
| **7-day-click purchases / ROAS** | Columns → Compare attribution settings → 7-day click | Click share ≥ 60% gate; decisions on click data | [L115 03:23–04:36](../lessons/115-how-to-scale-facebook-ads-up-down.md) [L116 02:32](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| **Click share** | 7-day-click purchases ÷ all purchases (sheet formula, derived) | Scale only if > 60% | [L115 04:36–05:51](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| **Spend share** | Ad-set spend ÷ campaign spend, same 7 days (sheet formula) | Winning-ad label tier | [L112 05:13](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md) → [winning-ad labels](../concepts/winning-ad-labels.md) |

## 5. Procedure C: read the table
**Windows:** last 7 days (click-based) for kill/keep and label calls [L120 04:25](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) [L112 06:39](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md); day-by-day breakdown for a test's first 3-7 days [L094 27:02–28:31](../lessons/094-how-to-set-up-a-3-2-2-campaign.md); last 30 days for performance; last 30-90 days for past winners, caution past 3 months, 6 max. [L100 05:39–07:27](../lessons/100-how-to-see-ads-performance-our-columns.md)

**Level:** ad set for kill decisions (never kill at ad level) [L094 page](../lessons/094-how-to-set-up-a-3-2-2-campaign.md); ad level and Breakdown → Dynamic creative element for text and headline reads. [L094 10:59–11:55](../lessons/094-how-to-set-up-a-3-2-2-campaign.md)

| Step | Read | Question | Source |
|---|---|---|---|
| 1 | Amount spent (sorted) and spend share | Did Meta choose it? "In this campaign method, the most important thing is spend." | [L094 26:29–27:02](../lessons/094-how-to-set-up-a-3-2-2-campaign.md) [L100 07:27](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| 2 | Purchase ROAS / CPA on 7-day click vs target and breakeven; campaign and whole account | Is it profitable? Purchase ROAS "is the big one" | [L100 08:21](../lessons/100-how-to-see-ads-performance-our-columns.md) [L115 00:00; 09:41](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| 3 | Click share | Is the ROAS real or view-through? | [L115 04:36](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| 4 | AOV, CVR | What does the ad do to basket and page? | [L100 14:01–14:55](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| 5 | Video Hook, Video Hold (video, with spend) | Is it stopping and holding people? | [L100 11:32–13:08](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| 6 | Link CTR, CPC, CPM, LPV rate | Is Meta happy, is the click honest? | [L100 09:02–10:51](../lessons/100-how-to-see-ads-performance-our-columns.md) [L107 03:34](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) |
| 7 | Frequency, date created | Prospecting or retargeting? new or proven? | [L120 07:47](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) |
| 8 | Adds to cart, checkouts | New accounts only: "you probably don't even need these" | [L100 13:08–14:01](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| 9 | URL parameters | Every ad tagged? | [L100 14:55](../lessons/100-how-to-see-ads-performance-our-columns.md) |

Example of step 1: "an ad with about $250 spent at roughly 3.9 ROAS is not really an ad that excites me" next to three ads taking the bulk of a $2,600 week. [L100 00:00–00:56](../lessons/100-how-to-see-ads-performance-our-columns.md)

## 6. Benchmarks (conflicting values side by side)
| Metric | Formula | L100 columns video | L088 doc / other | Agent default | Source |
|---|---|---|---|---|---|
| Video Hook | 3-s plays ÷ impressions | 21% okay · 30% good · 40% really good · 50%+ exceptional | Doc: ≥ 25%. Copywriting: < 30% "suspect" | Floor 25%, good 30%+; diagnostic only | [L100 11:32](../lessons/100-how-to-see-ads-performance-our-columns.md) [L088 31:47](../lessons/088-the-execution-problem.md) |
| Video Hold | ThruPlays ÷ impressions | > 5% always · > 10% good · > 15% sensational; compare by length (13% on a 7-s ad vs 9.8% on ~60 s) | Doc: ≥ 30% of hook rate (25% hook → 7.5%, "at least 8%") | ≥ 5% absolute and ≥ 30% of hook; compare like-length ads | [L100 11:32–12:22](../lessons/100-how-to-see-ads-performance-our-columns.md) [L088 31:47](../lessons/088-the-execution-problem.md) |
| Link CTR | Link clicks ÷ impressions | > 1% target; > 1.5% good | Doc: ≥ 1% | ≥ 1% | [L100 10:00](../lessons/100-how-to-see-ads-performance-our-columns.md) [L088 32:17](../lessons/088-the-execution-problem.md) |
| CPC | Spend ÷ link clicks | "If the ad is profitable, it doesn't matter what the cost per click is" | Very low CPC + poor ROAS = click-bait | Ignore unless paired with poor ROAS | [L100 10:00–10:51](../lessons/100-how-to-see-ads-performance-our-columns.md) [L107 04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) |
| CPM | Spend ÷ impressions × 1,000 | ~$10 "very, very good"; $30-$70 "really hard to manage" | Sudden unexplained drop ($35 → $8) = Meta anomaly | Context only; fix with better ads | [L100 09:02–10:00](../lessons/100-how-to-see-ads-performance-our-columns.md) [L121 05:12–06:22](../lessons/121-how-to-deal-with-roller-coaster-performance.md) |
| Frequency | Impressions ÷ reach | 5.95 over 30 days on 185,000 reached = "pretty intense" | ≤ 1.5 = prospecting; 5-6 normal in zombie; highest-frequency ads (e.g. 2.77) = probable retargeting | ≤ 1.5 read as prospecting; 7-day > ~3 read as retargeting-leaning (derived) | [L100 09:02](../lessons/100-how-to-see-ads-performance-our-columns.md) [L120 07:47](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) [L096 03:54](../lessons/096-how-to-set-up-zombie-graveyard-campaign.md) [L046 04:03–05:02](../lessons/046-ad-account-research.md) |
| LPV rate | LPV ÷ link clicks | — | ~78% on a 0.26x click-bait ad vs ~100% on a healthy ad set | Investigate < 90% (derived) | [L107 03:34–04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) |
| Adds to cart | ATC vs link clicks | 1,500 link clicks with 1 ATC = concerning (new accounts) | — | Funnel check if near zero | [L100 13:08](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| CVR, AOV | §4 formulas | Examples: CVR 2.11-7.95%, AOV $210-$284; $284 at 2.68% vs $263 at 2.1% | No threshold given | Compare within the account only | [L100 14:01–14:55; frame 14:10](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| Click share | 7DC purchases ÷ all purchases | > 60% to scale (example 104 of 111) | 32% (77 of 234) = view-through problem | > 60% | [L115 04:36](../lessons/115-how-to-scale-facebook-ads-up-down.md) [L116 09:32](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| ROAS / CPA | — | Target set from margin (§3) | Reported 7.79x vs 2.83 on 7-day click | Always 7-day click vs the card | [L101](../lessons/101-how-to-set-targets-kpis.md) [L116 07:02–08:10](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Spend before reading soft metrics | — | Not stated in Start Here | Copywriting: $1k spend after 7 days | $1k after 7 days | [iteration outcomes](../../copywriting/concepts/iteration-outcomes.md) |

Observed no-spend losers: hook ~16% with hold "insanely low" got no CBO spend [L122 02:32](../lessons/122-how-to-do-learnings-part-1-losers.md); but in a creator report the 18-21% thumbstop ads carried the spend over 42-48% ones [L160 02:20](../lessons/160-feedback-loops-with-your-brand-ambassadors.md). Soft metrics explain, they don't decide.

## 7. Symptom → read → action
| Symptom | Likely cause | Action | Source |
|---|---|---|---|
| No spend after 3-7 days | Meta didn't choose it; check hook/hold first | Off at day 7; learnings on why "customers didn't care"; zombie at the right tier | [L122 02:32](../lessons/122-how-to-do-learnings-part-1-losers.md) [L124 29:59](../lessons/124-how-to-do-learnings-part-3-losers.md) [L096 02:19](../lessons/096-how-to-set-up-zombie-graveyard-campaign.md) |
| High hook, low hold | Opening stops people, body doesn't hold | Rework body/format (storytelling or explained text-on-screen) | [L100 12:22](../lessons/100-how-to-see-ads-performance-our-columns.md) [L122 05:06–06:31](../lessons/122-how-to-do-learnings-part-1-losers.md) |
| Great hook/hold, no purchases | Soft metrics only | Ignore them; judge on ROAS/CPA | [L100 13:08](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| Very cheap CPC, big spend, poor ROAS, low LPV rate | Click-bait / accidental clicks | Turn off; never launch a hook that the page doesn't pay off | [L107 02:48–04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) |
| Spend hog with "sensational" CPC but terrible CVR and AOV | Meta chased cheap clicks | Kill after 24-48 h if still bad ([scaling rules](scaling-rules.md)) | [L120 01:26](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) |
| High reported ROAS, low 7DC ROAS | View-through credit | Decide on 7DC; test a 7DC-only campaign if click share is low | [L116 07:02–10:50](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Meta ROAS fine, blended weak | Paid credit not incremental | Hold scaling; check blended before scaling | [L118 04:52–05:48](../lessons/118-advanced-surf-scaling-method.md) [L101 05:59](../lessons/101-how-to-set-targets-kpis.md) |
| Spike on email-send days | Email sales attributed to ads | Don't credit the ad account | [L116 03:45](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| High frequency on a top spender | Retargeting-leaning | Don't read its ROAS as scalable; keep it fed by prospecting ads | [L120 07:47–08:25](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) |
| CPM $30-$70 | Ads Meta doesn't favour | Make ads that "make Facebook happy" | [L100 10:00](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| 1,500 clicks, 1 add to cart | Page or tracking problem | Funnel bug check | [L100 13:08](../lessons/100-how-to-see-ads-performance-our-columns.md) [L115 11:04–12:13](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| High ABO ROAS | Possibly retargeting purchases | Check new-visitor % | [L110 12:47](../lessons/110-winning-ads-definition-part-1.md) |
| Low-spend ad with great ROAS | Can "hog view through attribution" or last click | Don't promote it on its own numbers | [L092 05:53](../lessons/092-evolve-facebook-ads-philosophy.md) |

## 8. Which number decides what
| Decision | Number | Setting | Source |
|---|---|---|---|
| Kill / keep / label a test | Spend share + ad ROAS vs campaign ROAS | Meta, 7-day click (or 1-day click), 7 days | [L110 09:38–11:18](../lessons/110-winning-ads-definition-part-1.md) [L112 06:39](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md) |
| Daily budget move | Campaign + account ROAS/CPA vs target and breakeven; click share | Meta 7-day click | [L115 00:00–09:41](../lessons/115-how-to-scale-facebook-ads-up-down.md) |
| Intra-day promo moves | Period blended return (Shopify revenue ÷ total ad spend) | Surf sheet | [L118 04:52–05:48](../lessons/118-advanced-surf-scaling-method.md) |
| Is the account profitable | BROAS / MER | Shopify + all ad spend | [L101 05:27–05:59](../lessons/101-how-to-set-targets-kpis.md) |
| Is Meta (channel) incremental | Triple Whale TA (click) + Total Impact, NC ROAS | 14-day window; never lifetime | [L117 00:00–06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |
| Exclusion / incremental tests | Blended sales, new-visitor %, Northbeam | — | [L097 11:33–12:17](../lessons/097-how-to-set-up-abo-scaling-campaign.md) |
| Subscription / established brand | NC ROAS (2x in-platform can be 0.8x NC) | Triple Whale | [L117 05:49](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |

Full attribution logic: [click-based attribution](../concepts/click-based-attribution.md).

## 9. Report and audit column sets
- **Winning-ad report** (Ads Reporting): exactly Campaign name, Ad name, Day breakdown, Amount spent, Purchases, Cost per purchase, Purchase conversion value, ROAS, or "it will not work"; currency USD; 7-day click; CSV with "Include summary row"; at least ~8 weeks of spend. [L113 01:21–03:42](../lessons/113-how-to-generate-submit-winning-ad-report.md)
- **Ad-account audit** (new or inherited account): top prospecting and top retargeting creatives for the last 30 days and the last 6 months, ranked by "highest spend and lowest CPA... or best ROAS"; best hook-rate videos; best hold/CTR videos; share link per ad; if no retargeting exists write "no clear retargeting ads over the last 30 days" and list the highest-frequency ads. [L046 00:00–07:29](../lessons/046-ad-account-research.md) Rubric: [ad account audit](../rubrics/ad-account-audit.md).

## 10. Examples (from the lessons)
- **Champions vs DCT (30 days):** Champions 160 purchases at 3.95 ROAS vs a DCT ad set 22 at 3.44; account CPM $10.55, hook 8.57%, hold 4.30%. "Money sits in Champions." [L100 frames 08:30; 10:15](../lessons/100-how-to-see-ads-performance-our-columns.md)
- **CTR spread:** 2.6% champions, 1.19% and 0.61% on two DCTs; one ad at nearly double the CPC had a similar ROAS, so it stayed. [L100 10:00–10:51](../lessons/100-how-to-see-ads-performance-our-columns.md)
- **Top reel:** hook 21.47%, hold 13.22%; image ads show "—". [L100 frame 11:40](../lessons/100-how-to-see-ads-performance-our-columns.md)
- **Click-bait:** "click for sensitive info" ad: 1,649 link clicks vs ~1,300 LPVs, 0.26x, "we blew basically $1,500". [L107 02:48–04:25](../lessons/107-how-to-protect-against-bad-ads-over-spending.md)
- **Click share pass:** 111 purchases, 104 click-based, click ROAS 2.4. [L115 04:36](../lessons/115-how-to-scale-facebook-ads-up-down.md)

## 11. Common mistakes
| Mistake | Fix | Source |
|---|---|---|
| Copying a "3x" target | Margin-based breakeven + 1 | [L101 00:00–02:50](../lessons/101-how-to-set-targets-kpis.md) |
| Ranking ads by ROAS instead of spend | Sort by Amount spent first | [L100 07:27](../lessons/100-how-to-see-ads-performance-our-columns.md) |
| Promoting a tiny-spend, high-ROAS ad | 3x-budget test ([scaling rules](scaling-rules.md)) | [L120 05:15–05:46](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) |
| Reading hook/hold on images or on $2 of spend | Video only; $1k after 7 days (Copywriting) | [L100 13:08](../lessons/100-how-to-see-ads-performance-our-columns.md) [iteration outcomes](../../copywriting/concepts/iteration-outcomes.md) |
| Trusting Meta-reported ROAS with heavy view-through | 7-day click + blended | [L116 07:02](../lessons/116-how-to-understand-facebook-ads-attribution.md) |
| Using Triple Whale for ad decisions, lifetime window | Channel level, 14 days | [L117 04:21–06:50](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) |
| NCPA/LTV dashboards under $50k/month | Blended + in-platform | [L101 07:38](../lessons/101-how-to-set-targets-kpis.md) |
| Using old winners (> 6 months) as references | 30-90 day window | [L100 06:33](../lessons/100-how-to-see-ads-performance-our-columns.md) |

## 12. Conflicting values (agent defaults)
| # | Topic | Position A | Position B | Agent default |
|---|---|---|---|---|
| K1 | Hook / hold / CTR floors | Doc: hook ≥ 25%, hold ≥ 30% of hook, CTR ≥ 1% [L088 31:47](../lessons/088-the-execution-problem.md) | Columns: hook 21/30/40/50%+, hold > 5/10/15%, CTR > 1% / > 1.5% [L100 10:00–11:32](../lessons/100-how-to-see-ads-performance-our-columns.md) | Hook 25%, hold 5% and 30% of hook, CTR 1%; diagnostics after spend + ROAS (same as kpi-thresholds C1) |
| K2 | CVR denominator | LPV (agency default) [L100 04:40](../lessons/100-how-to-see-ads-performance-our-columns.md) | Link clicks also acceptable [L100 04:40](../lessons/100-how-to-see-ads-performance-our-columns.md) | LPV; add LPV rate to catch click-bait |
| K3 | Column list | Page list (Link clicks/CTR, avg play time) [L100 page](../lessons/100-how-to-see-ads-performance-our-columns.md) | Spoken build (unique outbound, engagement, quality ranking) [L100 02:48; 14:55](../lessons/100-how-to-see-ads-performance-our-columns.md) | Page list + §4 additions |
| K4 | KPI basis for budget moves | In-platform 7-day click [L115 09:41](../lessons/115-how-to-scale-facebook-ads-up-down.md) | Blended per period in promos [L118 05:48](../lessons/118-advanced-surf-scaling-method.md); beginners on BROAS [L101 06:52](../lessons/101-how-to-set-targets-kpis.md) | Daily evergreen: 7DC in-platform; weekly: confirm BROAS ≥ breakeven BROAS; promo surf: blended |
| K5 | Where spend share is measured | Initial campaign (tiers < $500k/month) [L112 05:13](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md) | Account, 7 days (2% loser, ≥ 10% early) [L124 07:04](../lessons/124-how-to-do-learnings-part-3-losers.md) | Label on campaign share; use account share in learnings |
| K6 | Champions lookback | Last 30 days or maximum [L094 13:50](../lessons/094-how-to-set-up-a-3-2-2-campaign.md) | 30-90 days, ≤ 6 months [L100 06:33](../lessons/100-how-to-see-ads-performance-our-columns.md) | 30-90 days |

## 13. Where it's taught
| Lesson | What it adds | Timestamps |
|---|---|---|
| [L100 Columns](../lessons/100-how-to-see-ads-performance-our-columns.md) | Preset, custom metrics, read order, benchmarks | 00:00–17:10 |
| [L101 Targets & KPIs](../lessons/101-how-to-set-targets-kpis.md) | Breakeven/scaling ROAS, KPI levels, blended ROAS, LTV | 00:00–09:26 |
| [L102 Action item](../lessons/102-action-item-set-your-targets-kpis.md) | Write the numbers before moving on | page |
| [L088 Execution problem](../lessons/088-the-execution-problem.md) | Creative-quality benchmark doc; "soft metrics" | 31:47–33:16 |
| [L107 Overspend](../lessons/107-how-to-protect-against-bad-ads-over-spending.md) | LPV ÷ link clicks click-bait check | 02:48–05:10 |
| [L110](../lessons/110-winning-ads-definition-part-1.md) / [L112](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md) | Click-based labelling; spend share | 09:38–12:47; 05:13–06:39 |
| [L113 Winning-ad report](../lessons/113-how-to-generate-submit-winning-ad-report.md) | Report columns, USD, 7DC | 01:21–03:42 |
| [L115 Scaling](../lessons/115-how-to-scale-facebook-ads-up-down.md) | Compare attribution settings; 60% click share | 03:23–05:51 |
| [L116](../lessons/116-how-to-understand-facebook-ads-attribution.md) / [L117](../lessons/117-how-to-view-attribution-in-tw-triple-whale.md) | 7DC vs view-through; Triple Whale windows and NC ROAS | 02:32–12:11; 00:00–11:48 |
| [L118 Surf scaling](../lessons/118-advanced-surf-scaling-method.md) | Blended per period | 04:52–05:48 |
| [L120 Turn-offs](../lessons/120-how-to-see-if-you-should-turn-off-high-spend-ads.md) | Frequency ≤ 1.5 = prospecting | 07:47 |
| [L046 Ad account research](../lessons/046-ad-account-research.md) | Audit columns and windows | 00:00–07:29 |
| [L122](../lessons/122-how-to-do-learnings-part-1-losers.md) / [L124](../lessons/124-how-to-do-learnings-part-3-losers.md) / [L160](../lessons/160-feedback-loops-with-your-brand-ambassadors.md) | Hook/hold on losers; account spend share; thumbstop caveat | 02:32; 05:13–07:54; 02:20 |

## 14. Cross-course notes
- **Evolve Copywriting:** [iteration outcomes](../../copywriting/concepts/iteration-outcomes.md) gives the label vocabulary and a soft-metric floor (hook < 30% suspect; low = CTR < 1%, hook < 25%, hold < 5%) plus the **$1k spend after 7 days** minimum before reading hook/hold. Start Here adds the margin-based targets, the exact column preset and the 7-day-click and blended checks. Agreement on the 25% hook / 1% CTR floors; Start Here's L100 video is looser (21% "okay").
- **Tether Lab (shared):** [creative testing system](../../../../frameworks/creative-testing-system.md) narrows new statics by **CTR** early and reads CPA/CVR later; the [test-and-iterate playbook](../../../../playbooks/test-and-iterate.md) warns not to scale a high-CTR variant without checking AOV and CVR. **Difference:** Evolve never ranks by CTR; spend share and 7-day-click ROAS decide, CTR is a diagnostic. Default for our accounts: Evolve's order; use Tether's CTR read only for pre-spend static screening.

## 15. Related
[Campaign structure 3:2:2](campaign-structure-322.md) · [Scaling rules](scaling-rules.md) · [Learnings review](learnings-review.md) · [Rewrite losers and iterate](rewrite-losers-and-iterate.md) · [Winning-ad labels](../concepts/winning-ad-labels.md) · [Click-based attribution](../concepts/click-based-attribution.md) · [Revenue-stage focus](../concepts/revenue-stage-focus.md) · [KPI thresholds](../libraries/kpi-thresholds.md) · [Ad account audit](../rubrics/ad-account-audit.md) · [Weekly media-buying routine](../playbooks/weekly-media-buying-routine.md)

## In other courses
- RMBC II: [Funnel economics (CPA, AOV, COGS, gross profit, break-even CPA, LTV)](../../../stefan-georgi/rmbc-ii/concepts/funnel-economics.md): CPA / AOV / COGS math (R9)
- RMBC II: [Benchmarks library: RMBC II (every number: VSL lengths, engagement, CTR, CPA, AOV, conversion, funnel scores, upsell, email and test thresholds)](../../../stefan-georgi/rmbc-ii/libraries/benchmarks.md): funnel benchmarks

Which page owns the topic: [topic map](../../../../topic-map.md).
