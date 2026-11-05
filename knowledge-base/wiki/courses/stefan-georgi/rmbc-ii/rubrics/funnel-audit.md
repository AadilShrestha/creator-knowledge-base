---
title: "Funnel audit rubric (13-01 structure fit, 16-03 economics, 11-01/11-02 checkout, 16-01 CRO)"
type: rubric
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi (13-01, 11-01, 11-02, 16-03 'SPG', 09-01, 10-01, 12-01, 14-01); Ethan Bence of 4080 Marketing (16-01, guest); Dynh Nguyen (12-02, guest)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-01-checkouts-walkthrough-part-1.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-05-vsl-product-buildup-and-reveal.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-02-native-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-01-1-1-abandon-cart-sequences.md
tags: [rubric, funnel-audit, funnel-structure, hidden-factors, unit-economics, cpa, aov, cogs, ltv, checkout, order-bump, cro, earnings-per-session, split-testing]
updated: 2026-11-02
---

# Funnel audit rubric
> A scored audit of a whole cold-traffic funnel, ours or a competitor's: does the page chain fit the offer (13-01 Hidden Factors), do the unit economics work (16-03), are the ad-to-page handoffs congruent (09-01, 10-01, 12-01), is the checkout doing its job (11-01, 11-02), and is the testing programme measuring the right thing (16-01).

## 🤖 Agent use
- **Use when:** before launch (is this funnel worth building?), when a live funnel is unprofitable or won't scale, when picking the next test, or when tearing down a competitor funnel to learn why it is long or short.
- **Inputs → outputs:** funnel map (ad → each page → checkout → upsells → emails) with screenshots/URLs; offer, price ladder, guarantee; CPA, AOV, COGS, conversion per step, traffic source and device mix, LTV/rebill data if any; testing tool and current tests → section scores, ⛔ blockers, the single biggest bottleneck, and a ranked test list with the dollar value of each lever.
- **Rules:**
  - **DO** run sections in order E (economics) → S (structure) → J (journey) → C (checkout) → P (post-purchase) → T (testing). Economics decides "a very different direction" for an offer making +$20 vs -$200 per customer ([16-03 11:33–12:37](../lessons/16-03-funnel-economics-with-spg.md)).
  - **DO** diagnose a poorly converting funnel in Stefan's order: step conversion rates vs benchmarks, then ad metrics (CPM/CPC), then AOV ([13-01 48:59–53:03](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
  - **DO** convert every lever to CPA and profit per day before calling it a win: "a higher conversion rate can mean a lower CPA, which can be more scale, more profit" ([16-03 34:41](../lessons/16-03-funnel-economics-with-spg.md)).
  - **DON'T** treat the matrix total as a verdict: "It doesn't mean you're not going to test things." ([13-01 48:27](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md))
  - **DON'T** assume a competitor's funnel works because it exists ([16-01 37:44–38:14](../lessons/16-01-cro-with-4080-marketing.md)); copy its structure, never its claims ([13-01 compliance flags](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
  - **IF** any page copy is LLM-written **THEN** run the [LLM output claim audit](llm-output-claim-audit.md) on it; a ⛔ fail there blocks the funnel.
- **See also:** [Funnel selection matrix](../concepts/funnel-selection-matrix.md) · [Funnel economics](../concepts/funnel-economics.md) · [Ad-to-page journey](../concepts/ad-to-page-journey.md) · [Congruence](../concepts/congruence.md) · [Checkout optimization](../frameworks/checkout-optimization.md) · [CRO testing](../frameworks/cro-testing.md) · [Launch a cold-traffic funnel (playbook)](../playbooks/launch-a-cold-traffic-funnel.md) · [VSL review](vsl-review.md) · Tether: [landing-page scorecard](../../../../rubrics/landing-page-scorecard.md), [creative testing system](../../../../frameworks/creative-testing-system.md) · Evolve: [KPI thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md), [ad account audit](../../../evolve/start-here/rubrics/ad-account-audit.md)

## Scoring
Each check: **PASS** (1) / **FAIL** (0) / n.a. (with reason). ⛔ checks block launch or scaling when failed. Section % = passes ÷ applicable. Bands (pipeline design, not the course's): ≥ 80% healthy, 60-79% fix before scaling, < 60% rebuild that section.

---

## E. Unit economics (16-03, 11-02)
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| E1 | Goal stated | One goal written: net profit, revenue, new customers or lifestyle | The goal comes before the math; Stefan assumes net profit "generally" ([16-03 01:53–03:46](../lessons/16-03-funnel-economics-with-spg.md)) | Ask the owner; default to net profit |
| E2 ⛔ | Four numbers known | CPA/CAC, AOV (day-0 gross), COGS (product, fulfilment, processing; not payroll), gross profit per customer = AOV − CPA − COGS | "compute four numbers before touching copy" ([16-03 03:46–05:42](../lessons/16-03-funnel-economics-with-spg.md)) | Fill from ad account, store and supplier invoices; mark estimates `[VERIFY]` |
| E3 ⛔ | Break-even CPA known and compared | Break-even CPA = AOV − COGS is computed and current CPA is below it, or a funded plan exists to sit above it | [16-03 48:30](../lessons/16-03-funnel-economics-with-spg.md) (break-even formula is the lesson's derived worksheet) | Raise AOV (upsells, packages) or cut COGS before scaling |
| E4 | Day-0 sign handled | If gross profit per customer < 0: cash runway and predictable rebills documented | "rather not go negative unless there's a very compelling reason" ([16-03 49:29–51:28](../lessons/16-03-funnel-economics-with-spg.md)); at -$200 per customer, $5,000 buys few sales ([08:06–09:08](../lessons/16-03-funnel-economics-with-spg.md)) | Fix AOV first; "going negative to acquire customers is actually a totally fine model if you know what you're doing" only with rebills ([14-01 v1 10:43–11:14](../lessons/14-01-upsells-overview.md)) |
| E5 | LTV assumptions explicit | LTV window, margin and stick rate stated; source is own data, not competitor napkin math | His LTV example is "back of napkin" on competitor data ([16-03 43:03–43:31; 48:30](../lessons/16-03-funnel-economics-with-spg.md)) | Label LTV as estimate; use own cohort data when available |
| E6 | Benchmarks sourced | CPA and conversion judged against operators running the same offer type | "is that conversion rate good? Is the CPA high, low, average?" — ask media buyers, peers, masterminds ([16-03 32:18–33:15](../lessons/16-03-funnel-economics-with-spg.md)) | Get 2-3 operator benchmarks; note them with source |
| E7 | Blended / effective CPA tracked | CPA includes call-center, SMS/email recovery and organic/coupon sales | Bad day: Facebook-only CPA $328 → $174.76 blended after call-center and coupon sales ([16-03 47:08–49:29](../lessons/16-03-funnel-economics-with-spg.md)); Stefan prefers effective CPA over the "AOV × CVR ≈ 350" heuristic ("I wouldn't make that my Bible metric", [13-01 53:39–56:43](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Add recovery channels to the CPA sheet |
| E8 | Lever table built | Each lever (CPA, COGS, AOV, LTV) has a hypothesis and recomputed profit per customer × daily volume | Five levers in order of thought ([16-03 13:07–29:47](../lessons/16-03-funnel-economics-with-spg.md)); multiply by 100 or 1,000 sales/day ([38:03; 40:46](../lessons/16-03-funnel-economics-with-spg.md)) | Use the worksheet in [funnel economics](../concepts/funnel-economics.md) |
| E9 ⛔ | Order bump measured on total funnel AOV | Bump tested on/off with the planned upsell; decision on revenue per order across the funnel | $27 bump at 40% + $97 upsell at 7% = $17.59/order vs $19.40 with no bump (upsell at 20%) ([11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md); his spoken "$1.40" is wrong, the figures give $1.81) | A/B the bump; keep it only if total revenue per order rises |

## S. Structure fit (13-01 Hidden Factors matrix)
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| S1 | 15 factors scored | All 15 rows scored 1-5 (5 = least copy needed), each with one line of evidence or "UNKNOWN - need: <fact>" | "Remember, the higher the rating, the less copy you need to add." ([13-01 10:17](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Use the scoring prompt in [funnel selection matrix](../concepts/funnel-selection-matrix.md) |
| S2 ⛔ | Chain matches band | Total maps to the live chain: **46+ lean** (ad → PDP → cart); **26-45 medium** (static/30-60 s ad → quiz/advertorial → 8-15 min VSL or long lander → cart/OTO, or 3-10 min in-feed mini-VSL → optional quiz/advertorial → PDP → cart/OTO); **≤ 25 heavy** (ad → story presell → 35-45 min VSL/webinar → application/checkout → ascension emails) | Bands and chains from the doc ([13-01 08:21; 43:51–45:15](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Add or remove a presell step; test the band's chain against the current one |
| S3 | Low rows have a lever | Every factor scoring 1-2 has one named lever (BNPL, demo/animation, UGC, guarantee) and a test | "change one factor at a time" (doc step 4); raise demonstrability before adding copy ([13-01 11:46–12:44](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Raise the factor before adding pages |
| S4 | Factors read in combination | Short-attention traffic is not used to justify a short funnel when price is high and trust low | "you're selling something that's $2,000 and you have no trust… you're still going to probably need longer funnels" ([13-01 39:20](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Re-score; weight price, trust, risk |
| S5 | Urgency proxy used when pain is slow | Non-urgent problems lead with an immediate symptom | "an immediate pain point that is symptomatic of the long-term one" ([13-01 31:13–32:46](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Rewrite the ad/lead around the near-term symptom |
| S6 | Pre-sell carries checkout friction | Where checkout has friction (BNPL approval, configurator), the pre-sell is strong enough | "pre-selling enough that when they get to the checkout… they'll suffer through it" ([13-01 38:50](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Strengthen presell or remove friction |

## J. Journey and congruence
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| J1 ⛔ | Ad job matches the page | Each ad is labelled "sell the click" or "sell the solution", and the next page does the remaining selling | "it's a lot easier to sell the click than it is to sell the prospect" ([12-01 00:03:22](../lessons/12-01-meta-ads.md)) | Re-label ads; re-route |
| J2 ⛔ | No blind VSL behind a product-revealing ad | Ads that show the product go to a product page, not a blind VSL | "A blind VSL is basically never going to talk to product aware or most aware." ([12-01 00:39:15–00:39:43](../lessons/12-01-meta-ads.md)) | Route product-revealing ads to PDP |
| J3 | Page length inverse to ad length | Static/short (< 60 s) ad or short advertorial → longer PDP; 60 s+ video or long advertorial → shorter PDP | "You have to do the selling somewhere." ([10-01 05:07–07:44](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)); [12-01 00:32:42](../lessons/12-01-meta-ads.md) | Lengthen or shorten the page |
| J4 ⛔ | No cold curiosity ad straight to a short PDP when belief is needed | A presell (advertorial) sits between a cold/curiosity ad and a short PDP for belief-heavy products | Predicted result: "Your CPA is going to be way too high. Your AOV is going to be way too low… never be able to scale." (instructor claim, [09-01 07:45](../lessons/09-01-advertorials-overview-and-examples.md)) | Insert a long advertorial; one per pain point if needed ([09-01 v2 26:07–27:24](../lessons/09-01-advertorials-overview-and-examples.md)) |
| J5 | Advertorial length follows what the ad revealed | If the video ad already revealed problem, product and mechanism, the advertorial is short and names the product early | [09-01 36:42–38:00; 44:14–45:09](../lessons/09-01-advertorials-overview-and-examples.md) | Cut to a graphics-heavy short advertorial |
| J6 | Native traffic presold and labelled | Native ads go to an advertorial or jump page (not a PDP) "for 99% of offers"; page labelled "Advertorial"/"Advertisement" | Guest claim ([12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md)); native compliance is "lower", not "none" ([09-01 compliance table](../lessons/09-01-advertorials-overview-and-examples.md)) | Add jump page/advertorial and label |
| J7 | VSL placement fit | An on-page VSL has a classic lead; an in-feed winner was not dropped onto the page unchanged | [04-11 09:59–11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md) | Rewrite the on-page lead; see [VSL review](vsl-review.md) |
| J8 | Message congruence after ad changes | Page re-tested when the winning ad angle changes; best ad copy pasted into the advertorial | "IF the winning page was built for one ad angle THEN re-test the page" ([16-01 1:17:31](../lessons/16-01-cro-with-4080-marketing.md)); [09-02 26:24](../lessons/09-02-claude-project-for-advertorials.md) | Re-test page with the new angle |
| J9 | VSL vs e-com compared on revenue per visitor | Page-type comparisons use revenue per visitor, not conversion rate | Stefan's rule of thumb: e-com page converts about double at about half the AOV (instructor claim, [04-05 58:47–59:14](../lessons/04-05-vsl-product-buildup-and-reveal.md)) | Re-read the test on RPV/EPS |

## C. Checkout (11-01, 11-02)
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| C1 ⛔ | Billing clarity | One-time vs subscription stated in text near the button; "One-time purchase · No subscription · No hidden fees" when true; terms readable as text | "it hurts people's conversions every time by not saying no subscription" ([11-01 10:58–11:26](../lessons/11-01-checkouts-walkthrough-part-1.md)); Emma line ([11-02 05:49](../lessons/11-02-checkouts-walkthrough-part-2.md)); guest test: the line added +10.5% (guest claim, [16-01 04:04](../lessons/16-01-cro-with-4080-marketing.md)); terms as image "shady" ([11-01 18:45–19:25](../lessons/11-01-checkouts-walkthrough-part-1.md)) | Add the line; convert terms to text |
| C2 ⛔ | No fake scarcity, no sneaky add-ons | Timers and stock bars reflect real rules; add-ons opt-in and visible | "59% left in stock… probably not true" ([11-01 04:04](../lessons/11-01-checkouts-walkthrough-part-1.md)); pre-added shipping warranty "very sneaky" ([11-01 12:29–13:03](../lessons/11-01-checkouts-walkthrough-part-1.md)) | Remove or make real; untick add-ons |
| C3 | Reassurance stack near the form | Guarantee, support, SSL, 2-4 real testimonials; on mobile the strongest reassurance sits above the button | [11-01 10:25](../lessons/11-01-checkouts-walkthrough-part-1.md); "probably like a 10% lift at least" (instructor bet, untested, [11-02 08:56–09:27](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Move guarantee/no-subscription above the button on mobile; test |
| C4 | Testimonials current | Dated testimonials refreshed; or undated | Happy Mammoth's 2024-only reviews look old ([11-02 01:13–01:44; 22:02](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Refresh with recent real reviews |
| C5 | Button copy | Button states the action/offer ("Complete order", "Claim your supply now"), not "Buy now" | [11-01 09:57](../lessons/11-01-checkouts-walkthrough-part-1.md); "these things actually do make a difference" ([11-02 04:47](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Rewrite and test |
| C6 | Order summary shows savings and quantity options | Savings visible; quantity toggle (1/3/6) tested | [11-01 13:03](../lessons/11-01-checkouts-walkthrough-part-1.md); [11-02 07:04](../lessons/11-02-checkouts-walkthrough-part-2.md) | Add savings line; test toggle |
| C7 | Phone number decision matches traffic | Phone number tested in header when no affiliates run; absent when affiliates do | Affiliates lose credit when the call center sells ([11-02 13:34–14:07](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Add or remove per traffic mix |
| C8 | Digital offers say instant access | Digital product checkouts state instant access and show the offer stack | [11-02 12:52; 19:32–20:52](../lessons/11-02-checkouts-walkthrough-part-2.md) | Add "instant access" line and stack |
| C9 | Price benchmarked | Price compared with real category prices before judging it | Stefan's grocery-shelf check for Dr. Clean's $19.95 ([11-01 05:03–08:22](../lessons/11-01-checkouts-walkthrough-part-1.md)) | Build a sourced price-comparison block |
| C10 | Mobile pass | Checkout reviewed on mobile first | "mobile is actually the way I would really look at most of this stuff" ([11-01 11:53](../lessons/11-01-checkouts-walkthrough-part-1.md)) | Audit on a phone viewport |

## P. Post-purchase and recovery
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| P1 | Upsell #1 exists and follows the formula | Reaffirm → new or expanded problem → offer; type chosen (more of the same / improved / complementary) | [14-01 v2 00:34](../lessons/14-01-upsells-overview.md); [14-02 v6 02:17–03:16](../lessons/14-02-upsells-case-studies.md) | Build via [post-purchase playbook](../playbooks/post-purchase-and-retention.md) |
| P2 | Upsell type fits the buyer | Subscription buyers not offered more of the same; durable-goods buyers offered complements | [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md) | Switch type |
| P3 | Later upsells don't assume earlier ones | Upsell 2+ works whether or not upsell 1 was taken | "We shouldn't assume they bought the first upsell." ([14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)) | Rewrite opener |
| P4 | Abandoned-cart recovery live | Email/SMS (and call center if viable) recovery running; first 24 h hit hardest | Worked math: 15 recovered buyers turn -$100/customer into about +$7 ([15-01 00:29–03:44](../lessons/15-01-1-1-abandon-cart-sequences.md)); [16-03 39:02](../lessons/16-03-funnel-economics-with-spg.md) | Build via [email sequences](../frameworks/email-sequences.md) |

## T. Testing programme (16-01, guest Ethan Bence)
| ID | Check | PASS if | Why (cited) | Fix |
|---|---|---|---|---|
| T1 ⛔ | Right success metric | Page/funnel tests judged on earnings per session (conversion × AOV) or revenue per visitor; conversion rate alone only where backend LTV dominates | "Conversion rate without AOV is meaningless." (guest claim, [16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md)); exceptions [11:22; 1:01:11](../lessons/16-01-cro-with-4080-marketing.md) | Add EPS/RPV to the test report |
| T2 ⛔ | True split tests | Same period, same traffic, random split in a testing tool | Two ad sets to page A and two to page B "is not a split test" ([16-01 16:33](../lessons/16-01-cro-with-4080-marketing.md)) | Move page tests into a split tool (redirect test if needed, [50:03–51:54](../lessons/16-01-cro-with-4080-marketing.md)) |
| T3 | Inside-out priority | Test queue starts at upsells, checkout, cart, landing page before PDP, collection, home, nav | Every visitor passes the bottleneck points ([16-01 19:53–22:10](../lessons/16-01-cro-with-4080-marketing.md)) | Re-rank the queue |
| T4 | Big changes | Tests change offer, avatar, structure or above-the-fold; no button-colour tests; low-traffic brands test structure/avatar/market | "Don't do a button color test." ([16-01 22:41](../lessons/16-01-cro-with-4080-marketing.md)); [45:03–45:57](../lessons/16-01-cro-with-4080-marketing.md) | Replace micro tests |
| T5 | Run rules | ≥ 7 days before calling a loser; ≥ 14 days and one business cycle before a winner; 80-85% probability to win accepted | Guest rules ([16-01 41:58–42:55; 1:12:55](../lessons/16-01-cro-with-4080-marketing.md)) | Extend or stop tests accordingly |
| T6 | Ideas from customers | Test hypotheses come from ~15 customer calls, support emails, sales calls, reviews; heatmaps and scroll depth checked | Guest claim: "80% plus of total gains" from talking to customers ([16-01 27:32–29:28](../lessons/16-01-cro-with-4080-marketing.md)); only 12% reached mid-page yet produced over half the purchases on one advertorial ([35:15–36:49](../lessons/16-01-cro-with-4080-marketing.md)) | Run VOC before the next test |
| T7 | Anomalies checked | Extreme results (e.g. -75%) investigated as tracking faults first | [16-01 1:12:55](../lessons/16-01-cro-with-4080-marketing.md) | Audit tracking |
| T8 | Winners iterated; ops changes tested | Above-the-fold winners re-tested; legal/ops changes tested before rollout | "always, always, always iterate on your winners" ([16-01 36:49; 58:44](../lessons/16-01-cro-with-4080-marketing.md)); SMS-consent step cost RPV -22% (guest claim, [1:10:57–1:11:56](../lessons/16-01-cro-with-4080-marketing.md)) | Queue a follow-up test; test ops changes |
| T9 | Price tested both ways | Price tests ~10-15% above and below | Guest ([16-01 46:58–48:29](../lessons/16-01-cro-with-4080-marketing.md)); lower prices can lift conversion enough to scale ([16-03 26:52–28:52](../lessons/16-03-funnel-economics-with-spg.md)) | Schedule a price test |

## Bottleneck finder (run after scoring)
1. Back into the AOV, CPA and CPM the goal needs ([13-01 48:59](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
2. Step rates: landing page → checkout; checkout → purchase. "Low page click-through = copy problem"; use heatmaps and VSL watch-time curves ([13-01 48:59–53:03](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md); [VSL review Part 2](vsl-review.md)).
3. Ad metrics: CPM, CPC. Thought test: "if I cut the cost per click in half and all the metrics stay the same, do I have a winner?" ([13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
4. If everything is decent: find "an extra $20 or $40" of AOV ([13-01 53:03](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).

## Output block
```text
FUNNEL AUDIT: <brand/offer> | date | auditor
Goal: __ | CPA $__ | AOV $__ | COGS $__ | GP/customer $__ | Break-even CPA $__ | LTV (window, source) __
Matrix total: __ → band __ | live chain: __ | match: Y/N
Sections: E __% | S __% | J __% | C __% | P __% | T __%
⛔ blockers: __
Bottleneck (step 1-4 above): __
Ranked tests (lever → hypothesis → expected ΔCPA or ΔAOV → $/day at current volume):
1. …
Claim audit on page copy: PASS/FIX/BLOCK
```

## Conflicts
| Topic | Position A | Position B | Agent default |
|---|---|---|---|
| Order bump | Listed as an AOV lever ([16-03 24:22–26:22](../lessons/16-03-funnel-economics-with-spg.md)) | Can lower total funnel AOV by cannibalising the upsell ([11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Bump only after an on/off test measured on revenue per order across the whole funnel |
| Headline metric | EPS / revenue per visitor (guest, [16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md)) | CPA is "the number to watch" ([16-03 35:37](../lessons/16-03-funnel-economics-with-spg.md)); effective CPA ([13-01 54:13](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Page tests: EPS/RPV. Funnel go/no-go and scaling: effective CPA vs break-even CPA |
| How to test landing pages (cross-course) | True split in a testing tool; separate ad sets per page "is not a split test" ([16-01 16:33](../lessons/16-01-cro-with-4080-marketing.md)) | Evolve 3:2:2:2: a second landing page as a separate ad/ad set inside the testing campaign at ≥ $2k/day ([Evolve campaign-structure-322](../../../evolve/start-here/frameworks/campaign-structure-322.md)) | Page-vs-page decisions: split tool. Evolve's method is an ad-level read (which ad + page pair Meta spends on), not a page verdict |
| Native funnels vs lean band | Lean band (46+) allows ad → PDP ([13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)) | Native: advertorial/jump page "for 99% of offers" (guest, [12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md)) | Channel overrides band: always presell on native |

## Related
- [Funnel selection matrix](../concepts/funnel-selection-matrix.md) · [Funnel economics](../concepts/funnel-economics.md) · [Upsell formula](../concepts/upsell-formula.md) · [Checkout optimization](../frameworks/checkout-optimization.md) · [CRO testing](../frameworks/cro-testing.md) · [Paid traffic by platform](../frameworks/paid-traffic-by-platform.md) · [Benchmarks library](../libraries/benchmarks.md)
