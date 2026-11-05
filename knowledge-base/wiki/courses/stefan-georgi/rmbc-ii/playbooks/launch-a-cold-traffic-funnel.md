---
title: "Playbook: launch a cold-traffic funnel (matrix → chain → economics → channels → pages → tracking → launch → iterate)"
type: playbook
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi (13-01, 16-03 'SPG', 09-01, 10-01, 12-01, 11-02); guests Dynh Nguyen (12-02 native), David O'Connell (12-03 Google), Max Finn (12-04 TikTok), Ethan Bence (16-01 CRO), Patrick Stiles (16-05 VSL data)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-02-native-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-03-google-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-04-tiktok-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-01-1-1-abandon-cart-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [playbook, funnel, cold-traffic, hidden-factors, funnel-economics, channels, meta, native, google, tiktok, tracking, cro, launch]
updated: 2026-11-02
---

# Playbook: launch a cold-traffic funnel
> Run this when asked "plan the funnel for X" or "get X ready for cold traffic": score the offer on the 15 Hidden Factors to pick the page chain, set the unit economics and a CPA ceiling, choose channels, build only the pages the chain needs, wire tracking and true split tests, then launch and diagnose in a fixed order.

## 🤖 Agent use
- **Use when:** planning a new funnel, re-planning a funnel that does not scale, or picking channels and page types for an offer.
- **Inputs → outputs:** offer facts, price ladder, proof assets, regulatory category, traffic intent, device split, COGS and target CPA → `funnel-spec` (score sheet, band, chain, channel plan, economics sheet with break-even and ceiling, page build list, tracking and test plan, launch read order).
- **Rules:**
  - **DO** score before you build: "Remember, the higher the rating, the less copy you need to add." ([13-01 10:17](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md))
  - **DO** decide whether the offer can lose money on day 0 before any copy ([16-03 11:33–12:37](../lessons/16-03-funnel-economics-with-spg.md)).
  - **DO** define each ad's supporting assets first: "an ad will never exist in a vacuum" ([12-01 00:01:02](../lessons/12-01-meta-ads.md)).
  - **DO** treat the band as a hypothesis: "you just got to test… seven or eight out of 10 [copycats] would not [win]" ([13-01 1:08:00–1:08:55](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
  - **DON'T** copy a competitor's funnel because it is long or short; copy the logic only ([13-01 Agent use](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
  - **DON'T** launch any page that failed the [claim audit](../rubrics/llm-output-claim-audit.md).
  - **IF** a factor scores 1-2 **THEN** try to raise it (BNPL, demo, UGC, guarantee) before adding a page (doc step 4, [13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
- **See also:** [Funnel selection matrix](../concepts/funnel-selection-matrix.md) · [Funnel economics](../concepts/funnel-economics.md) · [Ad-to-page journey](../concepts/ad-to-page-journey.md) · [Sell the click](../concepts/sell-the-click.md) · [Paid traffic by platform](../frameworks/paid-traffic-by-platform.md) · [CRO testing](../frameworks/cro-testing.md) · [Funnel audit](../rubrics/funnel-audit.md) · Evolve: [campaign structure 3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md), [KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md), [scaling rules](../../../evolve/start-here/frameworks/scaling-rules.md)

## Required real inputs (ask for anything missing)
1. Offer: price points, packages, guarantee, one-time vs subscription, payment options (BNPL, Apple Pay).
2. Proof inventory: real reviews (count), UGC, demo footage, studies, press, brand recognition.
3. Regulatory category and any known platform restrictions (health, finance, biz-opp, weight loss).
4. Awareness verdict from research ([02-01](../lessons/02-01-product-market-awareness.md)); if absent, run Stage 1 of [offer-to-funnel-end-to-end](offer-to-funnel-end-to-end.md).
5. Economics: COGS (product, fulfilment, processing), target or current CPA, AOV, cash available, rebill/LTV data and its window.
6. Planned channels, geo, device split, and whether affiliates will run (affects phone numbers on checkout, [11-02 13:34–14:07](../lessons/11-02-checkouts-walkthrough-part-2.md)).
7. Business goal: net profit, revenue, new customers or lifestyle ([16-03 01:53–03:46](../lessons/16-03-funnel-economics-with-spg.md)).
8. Operator benchmarks the user has (CPA, conversion) for the same offer type ([16-03 32:18–33:15](../lessons/16-03-funnel-economics-with-spg.md)).

## Stage 1: score the 15 Hidden Factors and pick the chain
- **Follow:** [funnel-selection-matrix](../concepts/funnel-selection-matrix.md).
- **Prompt (derived from the course doc; the 15 action-item lines are verbatim in [13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)):**
  ```text
  Score this offer on the 15 Hidden Factors using the scale directions below (5 = least copy needed). For each factor give: score, one-line evidence from the product/offer facts I supplied, and "UNKNOWN - need: <fact>" if the facts are missing (do not guess). Then sum, map to Lean (46+), Medium (26-45) or Heavy (<=25), propose the matching chain, list the three lowest-scoring factors, and for each name one lever that could raise it and the test to run. Do not invent proof, stats or compliance clearances.
  [paste the 15 action-item lines]
  [paste offer, price, traffic source, proof assets, category, device split]
  ```
- **Chain by band (doc "Quick Rule of Thumb", [13-01 08:21; 43:51–45:15](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)):**

| Total | Band | Starting chain |
|---|---|---|
| 46+ | Lean | Ad → PDP → Cart |
| 26-45 | Medium #1 | Static or 30-60 s video ad → Quiz/Advertorial → 8-15 min VSL or longer-form landing page → Cart/OTO |
| 26-45 | Medium #2 | 3-10 min in-feed video ad (mini VSL) → optional quiz/advertorial (test) → PDP → Cart/OTO |
| ≤ 25 | Heavy | Ad → possible story presell → 35-45 min VSL/webinar → application/checkout → possible ascension emails |

- **Overrides:** highly aware market that believes the solution works → skip VSL and presell; show price, trust and why you're the better source ([13-01 03:02–07:24](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)); non-urgent pain → lead with an immediate symptom ([13-01 31:13–32:46](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)); $2,000 + low trust → long funnel even for short-attention traffic ([13-01 39:20](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)); native traffic → always presell (guest, [12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md)).
- **Stefan's own default for a new skincare brand (instructor example):** video ads (30 s to a couple of minutes) → PDP → checkout, a more copied-up PDP while social proof is thin, advertorial added if needed ([13-01 1:00:01–1:01:32](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
- **Output:** score sheet, band, chain, three lowest factors with levers.
- **Gate:** user confirms the chain; funnel audit section S.

## Stage 2: unit economics and CPA ceiling
- **Follow:** [funnel-economics](../concepts/funnel-economics.md).
- **Compute (worksheet order derived, [16-03 03:46; 48:30](../lessons/16-03-funnel-economics-with-spg.md)):**
  ```text
  Goal: __
  CPA $__ | AOV (day-0 gross) $__ | COGS $__ (product + fulfilment + processing)
  Gross profit per customer = AOV − CPA − COGS = $__
  Break-even CPA = AOV − COGS = $__
  Day-0 sign: + / −   Cash runway: __   Rebill/LTV (window, source): __
  Lever table (hypothesis → new CPA/AOV/COGS → new GP/customer → × daily volume):
    CPA: better ads | higher conversion | other traffic | abandoned-cart recovery | branded search
    COGS: manufacturer | fulfilment | shipping | processing fees
    AOV: packages | upsell take rate | bump (test vs upsell) | price test
    LTV: continuity | stick rate | email monetisation | phone/text sales
  ```
- **Decisions:** day-0 negative → raise AOV first (upsells are "one of the most obvious things you could do", [14-01 v1 11:14](../lessons/14-01-upsells-overview.md)); go negative only with cash and predictable rebills ([16-03 49:29–51:28](../lessons/16-03-funnel-economics-with-spg.md)); expect CPA to rise with scale and set the ceiling from LTV and goal ([16-03 50:30–51:28](../lessons/16-03-funnel-economics-with-spg.md)).
- **Reference archetypes (instructor examples, [16-03 05:42–11:33](../lessons/16-03-funnel-economics-with-spg.md)):** supplement A CPA $150 / AOV $220 / COGS ~$50 → +$20; supplement B $300 / $150 / $50 → -$200; low-ticket info $40 / $60 / ~$0 → +$20; high-ticket phone sales $1,000 / $3,000 / $1,000 → +$1,000. Illustrations, not targets.
- **Output:** economics sheet with break-even CPA and CPA ceiling.
- **Gate:** funnel audit section E (E2, E3 are ⛔).

## Stage 3: pick channels
- **Follow:** [paid-traffic-by-platform](../frameworks/paid-traffic-by-platform.md).

| Channel | Use when | Chain rule | Key numbers / rules (cited) |
|---|---|---|---|
| Meta | Default cold channel for most DTC offers | Decide sell-the-click vs sell-the-solution; short caption + static → long PDP/advertorial; long video → short page; product shown → product page, never a blind VSL | Five questions: objective, awareness, destination, format, commonalities ([12-01 doc](../lessons/12-01-meta-ads.md)); test hook (first ~3-10 s) and thumbnail with the rest fixed ([12-01 00:12:30](../lessons/12-01-meta-ads.md)); CTA stays on screen after video ends ([00:34:38](../lessons/12-01-meta-ads.md)); VSL conversion from Meta 1.87% (guest claim, [16-05 06:08–07:33](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)). Account structure: Evolve [3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md) |
| Native (Taboola etc.) | Offer fits an older (~55+) audience; health VSLs, gadgets, lead gen | Ad → advertorial or jump page "for 99% of offers" → VSL/PDP/form | Guest claims ([12-02](../lessons/12-02-native-ads.md)): landing-page CTR 40-50% on a short jump page, ~30% on lead-gen pages, ~25-30% on mid/long advertorials; chase "high CPMs with high CTRs and low CPCs"; link tracker for real 50/50 splits; block push/gaming, pause mail placements at start; ask the rep for category benchmarks and a 100-150 publisher starter list |
| Google | Search/Shopping/PMax for product- and most-aware demand; Demand Gen/PMax for cold volume | One message per keyword intent tier; "give them what they're looking for"; VSL pages are not auto-approved for Shopping | Guest claims ([12-03](../lessons/12-03-google-ads.md)): build PMax from proven winners, not first; Demand Gen images with big bright text plus no-text variants; Shopping only for physical products; VSL conversion: Google paid 1.55%, YouTube 0.75% (guest claim, [16-05](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| TikTok | Short-form-native products; brands able to ship 4+ new creatives a week | Soft, informational pitch to the link; no hard "buy now" | Guest claims ([12-04](../lessons/12-04-tiktok-ads.md)): avatar research before spend; ≥ 4 new creatives per weekly batch; aim 1 winner in 4 (expect 1 in 8-10 at start); young accounts 75-80% net-new angles, later ~50/50; scale winners in place and add to the scaling campaign. VSL conversion from TikTok 0.50% (guest claim, [16-05](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |

- **Output:** channel plan (primary, secondary, budget split by test vs scale).
- **Gate:** each channel's chain rule matches the Stage 1 chain.

## Stage 4: build the pages the chain needs
Build in chain order; each page is written from Brief 2.0 ([offer-to-funnel-end-to-end](offer-to-funnel-end-to-end.md) stage 7).

| Page | Build with | Decide first | Gate |
|---|---|---|---|
| Ads | [hook-generation-system](../frameworks/hook-generation-system.md); short/3-7 VSL projects ([write-a-vsl-with-claude](write-a-vsl-with-claude.md) Stage 11); repo skill [write-ugc-script](../../../../../../.claude/skills/write-ugc-script/SKILL.md) | Sell the click or the solution ([12-01 00:03:22](../lessons/12-01-meta-ads.md)) | Claim audit + Tether [ad scorecard](../../../../rubrics/ad-scorecard.md) |
| Presell (advertorial / jump page / quiz) | [advertorial-build](../frameworks/advertorial-build.md) | Length from what the ad revealed ([09-01 36:42–38:00](../lessons/09-01-advertorials-overview-and-examples.md)); one per pain point for native ([09-01 v2 26:07–27:24](../lessons/09-01-advertorials-overview-and-examples.md)) | Claim audit; labelled "Advertorial" |
| VSL | [write-a-vsl-with-claude](write-a-vsl-with-claude.md) | Placement: on-page needs a classic lead ([04-11 11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)) | Claim audit + [VSL review](../rubrics/vsl-review.md) |
| PDP | [pdp-build](../frameworks/pdp-build.md) | Longer after static/short ads or a short advertorial; shorter after 60 s+ video or a long advertorial ([10-01 05:07–07:44](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)) | Claim audit + Tether [landing-page scorecard](../../../../rubrics/landing-page-scorecard.md) |
| Checkout | [checkout-optimization](../frameworks/checkout-optimization.md) | Bump only after an on/off test vs the upsell ([11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)) | Funnel audit C |
| Upsells, abandon-cart, welcome | [post-purchase-and-retention](post-purchase-and-retention.md) | Needed now if day-0 GP is negative | Claim audit + funnel audit P |

- **Congruence check:** the ad's topic and promise reappear in the first screen of the next page; paste the winning ad copy into the advertorial prompt ([09-02 26:24](../lessons/09-02-claude-project-for-advertorials.md)); see [congruence](../concepts/congruence.md).

## Stage 5: tracking and test setup
- Page tests in a split-testing tool: same time, same traffic, random split. Separate ad sets per page "is not a split test" ([16-01 16:33](../lessons/16-01-cro-with-4080-marketing.md)). Native: link tracker (RedTrack, Voluum, ClickMagick per the guest doc) for redirects and splits ([12-02](../lessons/12-02-native-ads.md)).
- Success metric for page tests: earnings per session = conversion × AOV ([16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md)).
- VSL events: fire an event at 2:00 to price "getting somebody to two minutes"; tag deep viewers in the CRM; micro-conversions for retargeting ([16-05 20:35–21:00; 32:55–33:53](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- Player: thumbnail set, captions, smart autoplay/pause ([16-05](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- Abandoned-cart capture live from day one (15 recovered buyers flipped a -$100/customer example to about +$7, [15-01 00:29–03:44](../lessons/15-01-1-1-abandon-cart-sequences.md)).
- **Output:** tracking checklist, ticked.

## Stage 6: pre-launch gates
1. [Claim audit](../rubrics/llm-output-claim-audit.md) on every page, ad, email: all PASS.
2. [VSL review](../rubrics/vsl-review.md) Part 1 ≥ 85% (if a VSL exists).
3. [Funnel audit](../rubrics/funnel-audit.md): no ⛔ fails in E, S, J, C.
4. Human/legal review for health, finance, biz-opp, weight loss.

## Stage 7: launch and read
- **Read order** ([13-01 48:59–53:03](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)): (1) step rates: page → checkout, checkout → purchase; "low page click-through = copy problem"; heatmaps and VSL watch curves; (2) ad metrics: CPM, CPC; (3) AOV: find "an extra $20 or $40".
- **VSL:** compare to 1.78% conversion and 33% / 28% / 3% engagement checkpoints (guest claims, [VSL review Part 2](../rubrics/vsl-review.md)).
- **Test run rules (guest):** ≥ 7 days before calling a loser, ≥ 14 days and one business cycle before a winner; 80-85% probability to win acceptable ([16-01 41:58–42:55](../lessons/16-01-cro-with-4080-marketing.md)). Extreme results → check tracking first ([1:12:55](../lessons/16-01-cro-with-4080-marketing.md)).
- **Output:** daily economics sheet; bottleneck named.

## Stage 8: iterate
- Test inside out: upsells → checkout → cart → landing page → PDP ([16-01 19:53–22:10](../lessons/16-01-cro-with-4080-marketing.md)); big changes, not button colours ([22:41](../lessons/16-01-cro-with-4080-marketing.md)); ideas from ~15 customer calls and support emails ([27:32–29:28](../lessons/16-01-cro-with-4080-marketing.md)).
- Change one matrix factor at a time and re-score ([13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) doc step 4).
- VSL: test leads first ([16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- Price: test ~10-15% above and below (guest, [16-01 46:58–48:29](../lessons/16-01-cro-with-4080-marketing.md)); lower prices can scale ([16-03 26:52–28:52](../lessons/16-03-funnel-economics-with-spg.md)).
- Re-test the page when the winning ad angle changes ([16-01 1:17:31](../lessons/16-01-cro-with-4080-marketing.md)).

## funnel-spec template
```text
FUNNEL SPEC: <offer> | goal __ | date
Matrix: total __ → band __ | lowest factors: __ (lever, test)
Chain: ad (__) → presell (__) → VSL/PDP (__) → checkout (__) → upsells (__) → emails (__)
Economics: CPA $__ | AOV $__ | COGS $__ | GP/customer $__ | break-even CPA $__ | ceiling $__ | LTV (window, source) __
Channels: primary __ (chain rule __) | secondary __ | test/scale split __
Tracking: split tool __ | tracker __ | VSL events __ | CRM tags __ | abandon capture __
Gates: claim audit __ | VSL review __% | funnel audit ⛔ __
First tests (lever → hypothesis → metric → run rule): __
```

## Cross-course notes
- **Meta account structure:** RMBC 12-01 covers ad roles and testing creative; it does not give a campaign build. Use Evolve's [3:2:2 structure](../../../evolve/start-here/frameworks/campaign-structure-322.md) and [scaling rules](../../../evolve/start-here/frameworks/scaling-rules.md) for the account.
- **Landing-page tests:** RMBC's guest (16-01) requires a split tool; Evolve's 3:2:2:2 reads a second page as a separate ad/ad set at ≥ $2k/day. Default: page verdicts from a split tool; Evolve's method is an ad-level read. Logged in the course contradictions notes.
- **Awareness targeting:** RMBC aims cold traffic at problem/solution aware ([02-01 17:01–20:38](../lessons/02-01-product-market-awareness.md)); Evolve Copywriting treats unaware as the most scalable. See [product-market awareness](../concepts/product-market-awareness.md).

## Related
- [Offer to funnel end to end](offer-to-funnel-end-to-end.md) · [Post-purchase and retention](post-purchase-and-retention.md) · [Playbooks hub](README.md) · [Benchmarks library](../libraries/benchmarks.md)
