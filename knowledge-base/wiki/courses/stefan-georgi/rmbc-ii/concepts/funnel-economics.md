---
title: "Funnel economics (CPA, AOV, COGS, gross profit, break-even CPA, LTV)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests Ethan Bence (16-01) and Eddie Maalouf (16-02) where labelled"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md
tags: [funnel-economics, cpa, aov, cogs, ltv, rebills, break-even, order-bump, effective-cpa, eps]
updated: 2026-11-02
---

# Funnel economics
> Four numbers (CPA, AOV, COGS, gross profit per customer) plus LTV decide whether a funnel can scale; every copy, page, checkout and upsell test is a change to one of them, so price every test in CPA and dollars per day before calling it a win.

## 🤖 Agent use
- **Use when:** judging an offer before writing copy; ranking what to test next (ads, page, flow, price, bump, upsell, abandoned-cart recovery, rebills); converting a conversion-rate lift into dollars; deciding whether an order bump helps; setting how much CPA the business is willing to pay.
- **Inputs → outputs:** goal, CPA, AOV, COGS, conversion rate, traffic and spend, abandoned-cart volume, rebill/LTV data with its time window, benchmark source → gross profit per customer, break-even CPA, a ranked lever list with before/after math, and a spend-ceiling decision. Mark every input measured, benchmarked or assumed.
- **Rules:**
  - **DO** write the goal first: net profit (default), revenue (only if selling the company; otherwise "a vanity metric"), new customers/leads, or lifestyle. [16-03 01:53–03:46](../lessons/16-03-funnel-economics-with-spg.md)
  - **DO** compute gross profit per customer = AOV − CPA − COGS, and break-even CPA = AOV − COGS, before touching copy. COGS = product, fulfilment, processing fees; not staff or payroll. [16-03 03:46–05:42; 48:30](../lessons/16-03-funnel-economics-with-spg.md)
  - **DO** treat "does this lose money on day 0?" as the fork that sets the plan. [16-03 11:33–12:37](../lessons/16-03-funnel-economics-with-spg.md)
  - **DO** get benchmarks (CVR, CPA) from operators running the same type of offer before judging a number. [16-03 32:18–33:15](../lessons/16-03-funnel-economics-with-spg.md)
  - **DO** watch CPA; conversion rate "is sort of just a metric to mark that that has happened". [16-03 34:41; 35:37](../lessons/16-03-funnel-economics-with-spg.md)
  - **DO** test price in both directions and judge on CPA and profit, not AOV alone. [16-03 27:49–28:52](../lessons/16-03-funnel-economics-with-spg.md)
  - **DON'T** add an order bump on take rate alone; it can cut total funnel AOV by cannibalising the upsell. A/B it on revenue per order. [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)
  - **DON'T** call a "50% conversion lift" a win until it is converted to CPA and profit per day. [16-03 36:07; 38:03](../lessons/16-03-funnel-economics-with-spg.md)
  - **DON'T** trust borrowed LTV: Stefan's own example uses competitor data, a six-month window and an averaged stick rate, "back of napkin". [16-03 43:03–43:31; 48:30](../lessons/16-03-funnel-economics-with-spg.md)
  - **IF** day-0 gross profit is negative **THEN** require cash or predictable rebills, and keep optimising CPA; Stefan would "rather not go negative unless there's a very compelling reason". [16-03 49:29–51:28](../lessons/16-03-funnel-economics-with-spg.md)
  - **IF** first-order margin is negative and cash is limited **THEN** raise AOV (upsells) before scaling spend. [14-01 v1 11:14](../lessons/14-01-upsells-overview.md)
  - **IF** front-end price and LTV are far apart **THEN** optimise conversion rate rather than earnings per session (guest claim, Ethan Bence). [16-01 11:22](../lessons/16-01-cro-with-4080-marketing.md)
- **See also:** [funnel-selection-matrix](funnel-selection-matrix.md) · [upsell-formula](upsell-formula.md) · [checkout-optimization](../frameworks/checkout-optimization.md) · [upsell-flow-build](../frameworks/upsell-flow-build.md) · [cro-testing](../frameworks/cro-testing.md) · [funnel-audit](../rubrics/funnel-audit.md) · [benchmarks](../libraries/benchmarks.md)

## Definition
Stefan's "dirty math": the unit economics of acquiring one customer. [16-03 00:00–00:59](../lessons/16-03-funnel-economics-with-spg.md)

| Term | Definition in the course | Source |
|---|---|---|
| CPA / CAC | Average cost to acquire a customer (media spend per customer, or the CPA paid to affiliates) | [16-03 06:12](../lessons/16-03-funnel-economics-with-spg.md) |
| AOV (day-0 gross) | Average order value including upsells and package mix | [16-03 03:46–05:42](../lessons/16-03-funnel-economics-with-spg.md) |
| COGS | "The fixed costs related to selling the goods versus other variable costs like staff and payroll": product, fulfilment, processing | [16-03 03:46–05:42](../lessons/16-03-funnel-economics-with-spg.md) |
| Gross profit per customer (GM) | AOV − CPA − COGS ("net profit margin" in 14-01 means the same dollars per customer) | [16-03 05:42](../lessons/16-03-funnel-economics-with-spg.md); [14-01 v1 09:00](../lessons/14-01-upsells-overview.md) |
| Break-even CPA | AOV − COGS (peptide funnel: $299 − $145 ≈ $154) | [16-03 48:30](../lessons/16-03-funnel-economics-with-spg.md) |
| LTV / extra lifetime gross profit | "What is the average additional expected lifetime gross profit of the customer?" | [16-03 42:35–43:03](../lessons/16-03-funnel-economics-with-spg.md) |
| Blended / effective CPA | Total acquisition spend (ads + call-center commissions) ÷ all sales including recovered and organic | [16-03 39:02–40:46; 47:08–48:59](../lessons/16-03-funnel-economics-with-spg.md); [13-01 54:13](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) |
| EPS (earnings per session) | Conversion rate × AOV; "Conversion rate without AOV is meaningless." (guest claim, Ethan Bence) | [16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md) |

## Why it matters
- The same funnel can lose $40 or make $20 per customer on an AOV change alone; Stefan says that gap is "the difference between an eight-figure business and… a business that fails or takes a really long time to scale" (instructor claim). [14-01 v1 06:56–08:25](../lessons/14-01-upsells-overview.md)
- It tells the copywriter what a win is worth. In Stefan's worked example, better ads at the same $3,000 spend move daily profit from about $200 to $3,400. [16-03 13:34–17:41](../lessons/16-03-funnel-economics-with-spg.md)
- It picks the funnel: rows 3, 9 and 13 of the [funnel-selection-matrix](funnel-selection-matrix.md) (price, LTV, payment friction) are economic. [13-01 27:51–38:50](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)

## How to use (steps)
1. Write the goal. [16-03 01:53](../lessons/16-03-funnel-economics-with-spg.md)
2. Fill CPA, AOV, COGS; compute gross profit per customer and break-even CPA.
3. Get a benchmark for CVR and CPA from a named source. [16-03 32:18](../lessons/16-03-funnel-economics-with-spg.md)
4. For each lever, write the hypothesis and recompute CPA and gross profit per customer:

| Lever | Tactics named in the course | Course example (instructor claims) | Source |
|---|---|---|---|
| CPA down: ads | Higher CTR, lower CPM, new creative | 1,000 → 2,000 visitors, CPA $150 → $75 | [16-03 16:33–17:41](../lessons/16-03-funnel-economics-with-spg.md) |
| CPA down: conversion | New sales letter, flow fixes, CRO tests | 1.04% → 2.08% → 2.5%; CPA $300 → $150 → $125 | [16-03 34:41–38:32](../lessons/16-03-funnel-economics-with-spg.md) |
| CPA down: traffic | Other platforms, affiliates, branded search, organic/SEO/Amazon halo | Branded search sales "for like $20 instead of $150" | [16-03 20:03–22:22](../lessons/16-03-funnel-economics-with-spg.md) |
| CPA down: recovery | Call center, SMS, email on abandoned carts | 300 abandons/day; 10% call center + 5% text/email; blended CPA $97.82 | [16-03 39:02–40:46](../lessons/16-03-funnel-economics-with-spg.md) |
| COGS down | Manufacturer, fulfilment, shipping, processing fee | $5 → $3 per bottle; fee 5% → 2.5% | [16-03 22:22–23:52](../lessons/16-03-funnel-economics-with-spg.md) |
| AOV up | Money close, more packages, bump, upsell take rate, price test | $220 → $250 lifts GM $20 → $44; upsell take 20% → 40% | [16-03 24:22–26:52](../lessons/16-03-funnel-economics-with-spg.md) |
| LTV up | Continuity, stick rate, list monetisation, phone/text sales | $1,000 extra gross profit ÷ 6 months ≈ $166/month | [16-03 28:52–29:47; 43:31](../lessons/16-03-funnel-economics-with-spg.md) |

5. Multiply by volume (100 or 1,000 sales/day) to see the monthly value. [16-03 38:03; 40:46](../lessons/16-03-funnel-economics-with-spg.md)
6. Add LTV: extra expected gross profit ÷ months of data, times customers from earlier cohorts. [16-03 43:31–44:55](../lessons/16-03-funnel-economics-with-spg.md)
7. Decide the spend ceiling ("not can you spend, but willing to spend") from goal, cash and rebill foundation. [16-03 49:29–50:30](../lessons/16-03-funnel-economics-with-spg.md)

### Order-bump cannibalisation check (11-02 worked example, hypothetical numbers)
| Scenario | Bump revenue / order | Upsell revenue / order | Total |
|---|---|---|---|
| No bump; $97 upsell at 20% | $0 | $19.40 | **$19.40** |
| $27 bump at 40%; upsell falls to 7% | $10.80 | $6.79 | **$17.59** |
Source: [11-02 17:42–19:04](../lessons/11-02-checkouts-walkthrough-part-2.md). Stefan says "$1.40 more" aloud; the arithmetic gives $1.81. Use the arithmetic. "The good thing about these offer bumps is that your conversion rate's high. The bad thing is it could actually make your AOV lower." [11-02 19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)

### Worksheet (derived from 16-03)
```text
GOAL: [net profit | revenue | new customers | lifestyle]
CPA: $__  AOV: $__  COGS: $__   (each: measured | benchmarked (source) | assumed)
GROSS PROFIT / CUSTOMER = AOV - CPA - COGS = $__
BREAK-EVEN CPA = AOV - COGS = $__
BENCHMARK (source: __): CVR __%  CPA $__
LEVER TEST: [change] -> new CPA $__ -> new gross profit / customer $__
BUMP CHECK: bump take x price + upsell take (with bump) x price vs upsell take (no bump) x price
VOLUME CHECK: __ customers/day x gross profit = $__/day, $__/month
LTV: extra expected gross profit $__ over __ months (own cohort data? Y/N)
WILLING TO SPEND PER CUSTOMER: $__ (cash / rebill foundation: __)
```

## Examples (instructor claims unless stated; numbers are his, not verified)
| Case | Inputs | Result | Source |
|---|---|---|---|
| Supplement A | CPA $150, AOV $220, COGS ~$50 | +$20 per customer | [16-03 05:42](../lessons/16-03-funnel-economics-with-spg.md) |
| Supplement B | CPA $300, AOV $150, COGS $50 | −$200; "not everyone should be an offer owner" | [16-03 07:37](../lessons/16-03-funnel-economics-with-spg.md) |
| Low-ticket info | CPA $40, AOV $60, COGS ~$0 | +$20; "harder to scale" | [16-03 09:38](../lessons/16-03-funnel-economics-with-spg.md) |
| High-ticket phone sales | CPA $1,000, AOV $3,000, COGS $1,000 | +$1,000 | [16-03 10:35](../lessons/16-03-funnel-economics-with-spg.md) |
| Upsell scenarios | $100 CAC; AOV $80 → $160; COGS $20 → $40 | −$40 → +$20; or spend the gain: CAC $120 → $0 and more customers | [14-01 v1 05:04–08:58](../lessons/14-01-upsells-overview.md) |
| GLP-1 peptide funnel (Stefan is CMO/partner) | CPA $300, AOV $299, COGS $145 | −$146 → +$56.18 after flow simplification, page tests and abandon recovery (PDF states $5 and $20 at steps 1-2; inputs give $4 and $29) | [16-03 30:47–40:46](../lessons/16-03-funnel-economics-with-spg.md) |
| "Bad day" blended CPA | 6 FB sales at $328 + 8 call-center + 3 organic/coupon | Blended CPA $174.76; rebills made the day positive | [16-03 47:08–48:59](../lessons/16-03-funnel-economics-with-spg.md) |
| Price up | Skincare single bottle $59 → $79 | AOV up, "conversion stayed exactly the same" | [16-03 27:49](../lessons/16-03-funnel-economics-with-spg.md) |
| Price down | Blood-sugar supplement $69/$59/$49 → ~$39/$34/$29 | "Conversions doubled or tripled", enabled scale | [16-03 28:19–28:52](../lessons/16-03-funnel-economics-with-spg.md) |
| Rebill compounding | 1,000 sales/day, $166/month rebill GP | Month-3 GP $11,645,400 (gross, ignores payroll, refunds, chargebacks) | [16-03 43:31–45:23](../lessons/16-03-funnel-economics-with-spg.md) |
| Amazon/DTC repeat cohorts | Repeat LTV vs average LTV | LTV:CAC 6.3x in his example (guest claim, Eddie Maalouf) | [16-02 07:16](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md) |

## Common mistakes
- Treating revenue as the goal when not selling the company: people who did "$50 million a year and took home $500,000 in profit" (instructor claim). [16-03 01:53–03:46](../lessons/16-03-funnel-economics-with-spg.md)
- Reporting the bump's take rate as a win without the downstream upsell rate. [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)
- Judging a CVR or CPA with no benchmark. [16-03 32:18](../lessons/16-03-funnel-economics-with-spg.md)
- Copying Stefan's arithmetic: it slips several times (16-03 $5/$20 GM, merchant-fee total; 14-01 "I've lost $20"). Recompute every figure. [16-03 23:52; 36:36; 38:03](../lessons/16-03-funnel-economics-with-spg.md); [14-01 v1 06:56](../lessons/14-01-upsells-overview.md)
- Treating rebill gross profit as net. The model ignores payroll, call-center commissions on rebills, refunds, chargebacks, reserves and tax (derived). [16-03 44:26](../lessons/16-03-funnel-economics-with-spg.md)
- Using the attendee "AOV × CVR ≈ 350" rule as a target. Stefan: "I wouldn't make that my Bible metric"; track effective CPA. [13-01 53:39–56:43](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)
- Hidden continuity to lift LTV: "super shady and not sustainable long term". Disclose subscriptions clearly; easy cancellation. [11-02 21:35](../lessons/11-02-checkouts-walkthrough-part-2.md) See [compliance-red-flags](compliance-red-flags.md).
- Call-center and SMS abandon recovery without consent and opt-out (derived compliance note). [16-03 39:02](../lessons/16-03-funnel-economics-with-spg.md)

## Where it's taught
- [16-03 Funnel economics with SPG](../lessons/16-03-funnel-economics-with-spg.md): goals [01:53–03:46]; four questions [03:46–05:42]; archetypes [05:42–11:33]; levers [13:34–29:47]; peptide case [30:17–42:35]; LTV and rebills [43:03–46:14]; bad day [47:08–49:29]; willing to spend [49:29–51:28].
- [14-01 Upsells overview](../lessons/14-01-upsells-overview.md): CAC/AOV/COGS scenarios [v1 04:27–11:14].
- [11-02 Checkouts part 2](../lessons/11-02-checkouts-walkthrough-part-2.md): order-bump math [16:31–19:32]; subscription disclosure [21:35].
- [13-01 Hidden factors](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md): bottleneck diagnosis order and effective CPA [48:59–56:43].
- [16-01 CRO with 4080 Marketing](../lessons/16-01-cro-with-4080-marketing.md) (guest, Ethan Bence): EPS [10:25]; LTV exception [11:22].
- [16-02 Ecom and Amazon with Eddie Maalouf](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md) (guest): LTV, AOV, CAC, TACOS, repeat cohorts [07:16].

## Cross-course notes
- **Evolve Start Here** sets targets as ROAS: breakeven ROAS = 1 ÷ gross margin; scaling ROAS = breakeven + 1 ([kpi-thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md), K061-K062). **Agreement:** same math expressed per dollar of spend rather than per customer; break-even CPA = AOV − COGS ↔ breakeven ROAS = AOV ÷ (AOV − COGS). (derived)
- **Disagreement on LTV:** Evolve says skip LTV/NCPA tooling under about $50k/month spend and use blended ROAS ([kpi-thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md), K048). RMBC 16-03 uses LTV to justify a negative day-0 CPA. **Agent default:** judge on day-0 gross profit and blended CPA/ROAS; use LTV to bid above break-even only with your own observed cohort rebill data and confirmed cash runway.
- **Metric to optimise:** Stefan watches CPA [16-03 35:37](../lessons/16-03-funnel-economics-with-spg.md); guest Ethan Bence uses EPS [16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md). Not a real conflict: EPS × sessions ÷ spend is the inverse view of CPA plus AOV. **Agent default:** report both CPA and revenue per session for every page test.
- **Evolve** [revenue-stage-focus](../../../evolve/start-here/concepts/revenue-stage-focus.md) frames priorities by revenue stage. Tether Lab: [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) for the package ladder behind AOV.

## Related
[funnel-selection-matrix](funnel-selection-matrix.md) · [upsell-formula](upsell-formula.md) · [ad-to-page-journey](ad-to-page-journey.md) · [checkout-optimization](../frameworks/checkout-optimization.md) · [upsell-flow-build](../frameworks/upsell-flow-build.md) · [email-sequences](../frameworks/email-sequences.md) · [launch-a-cold-traffic-funnel](../playbooks/launch-a-cold-traffic-funnel.md) · [funnel-audit](../rubrics/funnel-audit.md) · [benchmarks](../libraries/benchmarks.md)
