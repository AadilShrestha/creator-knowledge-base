---
title: "CRO Testing (inside-out prioritisation, earnings per session, run rules, incremental revenue)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Guests Ethan Bence (4080 Marketing) and Eddie Maalouf (BAD Marketing); Stefan Georgi (16-03 economics)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
tags: [cro, split-testing, earnings-per-session, revenue-per-visitor, prioritisation, price-testing, heatmaps, voice-of-customer, listicles, offers]
updated: 2026-11-02
---

# CRO Testing
> Rank funnel steps inside out (upsells → checkout → cart → landing page → PDP …), source test ideas from customers and heatmaps, test one big lever per step with a true random split, judge on earnings per session after 7 days (kill) / 14 days and one business cycle (ship), log monthly incremental revenue, and re-test every winner.

## 🤖 Agent use
- **Use when:** building a test roadmap for pages, checkout, upsells or funnel structure; writing a test hypothesis; reading a result; deciding whether a "best practice" or legal/ops change ships untested.
- **Inputs → outputs:** funnel map, sessions/day per step, CVR and AOV per step, customer calls/support emails/reviews, heatmap and scroll data → ranked test queue → one hypothesis per test → run rule → result read on EPS → incremental-revenue log → next iteration.
- **Rules (guest claims unless marked):**
  - **DO** optimise earnings per session: "Conversion rate without AOV is meaningless." EPS = conversion rate × AOV [16-01 10:25–12:18](../lessons/16-01-cro-with-4080-marketing.md).
  - **DO** test inside out: upsells, checkout, cart, sales/landing page, product pages, collection, home, banner, navigation, menu [16-01 19:53–22:10](../lessons/16-01-cro-with-4080-marketing.md).
  - **DO** test big levers (offer, avatar, funnel structure, above the fold): "Don't do a button color test." [16-01 22:41](../lessons/16-01-cro-with-4080-marketing.md)
  - **DO** talk to ~15 customers before writing tests; guest claims this yields "80% plus of total gains" [16-01 27:32–29:28](../lessons/16-01-cro-with-4080-marketing.md).
  - **DO** run true split tests (same period, same traffic, random split): "page A in October and page B in January… is not a split test." [16-01 16:33](../lessons/16-01-cro-with-4080-marketing.md)
  - **DO** wait ≥7 days to kill, ≥14 days and one business cycle to ship; 80–85% probability to win is acceptable [16-01 41:58–42:55, 1:12:55](../lessons/16-01-cro-with-4080-marketing.md).
  - **DO** re-test winners: "always, always, always iterate on your winners." [16-01 36:49, 58:44](../lessons/16-01-cro-with-4080-marketing.md)
  - **DON'T** ship untested changes from legal or ops on faith; SMS-consent-before-opt-in cut RPV 22% ("$260,000 per month") [16-01 1:10:57–1:11:56](../lessons/16-01-cro-with-4080-marketing.md). Test them, but compliance-required changes still ship; the test sizes the cost (derived).
  - **DON'T** assume a competitor's page works or that pretty converts [16-01 37:44–39:02](../lessons/16-01-cro-with-4080-marketing.md).
  - **IF** a variant shows a drastic drop (e.g. −75%) **THEN** suspect broken tracking first [16-01 1:12:55](../lessons/16-01-cro-with-4080-marketing.md).
  - **IF** low traffic or new brand **THEN** test funnel, avatar, market, product, not headlines [16-01 45:03–45:57](../lessons/16-01-cro-with-4080-marketing.md); run tests sequentially [16-01 40:02](../lessons/16-01-cro-with-4080-marketing.md).
- **See also:** [funnel economics](../concepts/funnel-economics.md) · [funnel audit rubric](../rubrics/funnel-audit.md) · [pdp-build](pdp-build.md) · [checkout optimization](checkout-optimization.md) · [upsell flow build](upsell-flow-build.md) · [congruence](../concepts/congruence.md) · [benchmarks](../libraries/benchmarks.md) · shared [creative testing system](../../../../frameworks/creative-testing-system.md) (ad-level counterpart) · [customer research stack](../../../../frameworks/customer-research-stack.md) · [landing page psychology audit](../../../../frameworks/landing-page-psychology-audit.md)

## Definition
"Conversion revenue optimisation" (Ethan Bence, 4080 Marketing) = direct-response offers and customer-language copy plus UX, judged on EPS / revenue per visitor and incremental revenue, "more concerned with driving increases faster to this metric than we are with knowing exactly why it happened." [16-01 06:24–12:18](../lessons/16-01-cro-with-4080-marketing.md)

## Procedure

### Step 1. Map the funnel and baseline EPS
- **Input:** analytics per step. **Output:** table: step | sessions/day | CVR | AOV | EPS.
- EPS example: 3.5% × $49 = $1.71 [16-01 12:18](../lessons/16-01-cro-with-4080-marketing.md). EPS / CPC ≈ ROAS (rough check only; site-wide EPS < paid EPS) [16-01 12:18–13:14](../lessons/16-01-cro-with-4080-marketing.md).
- **IF** backend LTV far exceeds front-end price (telehealth, membership) **THEN** primary metric = conversion rate: "day one cash is not as important as lifetime value" [16-01 11:22, 1:01:11](../lessons/16-01-cro-with-4080-marketing.md).
- Size what a lift is worth with [funnel economics](../concepts/funnel-economics.md) (16-03 scenarios).

### Step 2. Prioritise inside out
- **Output:** ranked steps.

| Rank | Step | Why | Source |
|---|---|---|---|
| 1 | Upsells | Cannot reduce front-end conversion | [16-01 21:15](../lessons/16-01-cro-with-4080-marketing.md) |
| 2 | Checkout | "Often set live once and never tested"; social proof added can lift 10–20% (guest claim) | [16-01 21:15](../lessons/16-01-cro-with-4080-marketing.md) |
| 3 | Cart | Everyone passes | [16-01 20:45](../lessons/16-01-cro-with-4080-marketing.md) |
| 4 | Sales / landing page (advertorial, VSL page) | Bottleneck for paid traffic | same |
| 5 | PDP | | same |
| 6–10 | Collection, home, banner, nav, menu | Fewer buyers pass through | same |

- Funnels with calls/webinars/quizzes: swap in the quiz, booking page etc. at the matching position [16-01 22:41](../lessons/16-01-cro-with-4080-marketing.md).
- "Whatever gets you testing faster is the framework that you should use" (ICE etc. fine) [16-01 19:53](../lessons/16-01-cro-with-4080-marketing.md).

### Step 3. Source test ideas
1. Call ~15 customers from the CRM; read support emails and sales-call recordings [16-01 27:32–28:30](../lessons/16-01-cro-with-4080-marketing.md).
2. Read our reviews and competitor reviews; listen for feelings, context and repeated phrases; "You can't write better copy than your customer." [16-01 30:27–33:03](../lessons/16-01-cro-with-4080-marketing.md)
3. Heatmaps (Hotjar, Lucky Orange, heatmap.com): clicks on non-clickable elements = test ideas; revenue per click if available [16-01 33:56–35:15](../lessons/16-01-cro-with-4080-marketing.md).
4. Scroll depth: guest example 94% see above the fold, 12% reach mid-page, but over half the purchases come from those 12%; above the fold "gets people reading further, and then the below the fold is what converts." **IF** months spent below the fold **THEN** start above the fold [16-01 35:15–36:49](../lessons/16-01-cro-with-4080-marketing.md).
5. Older avatar → UX care: obvious clickables, legible fonts, simple lists [16-01 33:56–34:26](../lessons/16-01-cro-with-4080-marketing.md).

### Step 4. Choose one big lever
- Test-type matrix: funnel stage × {copy, design, offer, avatar/segment, funnel structure, tech stack, business level} [16-01 39:02](../lessons/16-01-cro-with-4080-marketing.md).

| Lever | Example test (guest results, unverified) | Source |
|---|---|---|
| Copy, risk line | "one-time purchase, no subscription required" +10.5% | [16-01 04:04](../lessons/16-01-cro-with-4080-marketing.md) |
| Copy, headline | Telehealth V1 +6.3% ("no good way around testing headlines other than just testing a bunch") | [16-01 03:33, 53:17](../lessons/16-01-cro-with-4080-marketing.md) |
| Avatar image | Aspirational model +34%; age ladder: youngest best | [16-01 04:36, 1:02:09, 1:15:45](../lessons/16-01-cro-with-4080-marketing.md) |
| Design, menu | Image-led menu + trust bar, no social links +32% RPV | [16-01 54:11](../lessons/16-01-cro-with-4080-marketing.md) |
| Design, collection | List with serves/delivery date beat 2×2 grid, +10% RPV | [16-01 56:10](../lessons/16-01-cro-with-4080-marketing.md) |
| Above the fold | Headline, sub-headline, CTA, social proof, product image; what it solves, who it's for | [16-01 57:44–58:44](../lessons/16-01-cro-with-4080-marketing.md) |
| Offer / price | ±10–15% price steps ("$44 to $47 or $49") | [16-01 46:58–48:29](../lessons/16-01-cro-with-4080-marketing.md) |
| Offer bundle | Free gifts unlocked by quantity tier: CVR <1% → 2.75% (guest claim, Eddie Maalouf) | [16-02 23:18](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md) |
| Funnel structure | Listicle vs PDP: CPA −20–50% (guest claim, Eddie Maalouf); test headlines first, then each reason | [16-02 18:33](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md) |
| Funnel structure | Mix-and-match vs PDP: RPV −7% but subscriptions +467% (CRO loss, business win) | [16-01 1:06:27](../lessons/16-01-cro-with-4080-marketing.md) |
| Tech stack | WebinarJam → StealthSeminar: leads +19%, calls +38%, sales +35% | [16-01 1:09:31](../lessons/16-01-cro-with-4080-marketing.md) |
| Business level | Payment processor ~0%; SMS terms −22% | [16-01 1:10:57–1:11:56](../lessons/16-01-cro-with-4080-marketing.md) |

- Price tests both directions (Stefan, 16-03): "split-test price in both directions; lower prices can raise conversion enough to scale" [16-03 26:52–28:52](../lessons/16-03-funnel-economics-with-spg.md). Guest: info products often convert better at a higher price ($39 → $49, $19 → $29) [16-01 47:59](../lessons/16-01-cro-with-4080-marketing.md).
- Offer flip when stalled: run 3–4 COGS-viable offers at once, scale the winner (guest claim, Eddie Maalouf) [16-02 23:18](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md).

### Step 5. Write the hypothesis
```
Page / step: <bottleneck position>
Evidence: <call count, review phrases, heatmap/scroll data>
Change (big, one lever): <copy | design | offer | avatar | funnel | tech | business>
Primary metric: EPS (or CVR if backend LTV >> front end)
Run rule: >= 7 days to kill, >= 14 days and one business cycle to ship, >= 80-85% probability to win
After result: re-test winner; log monthly incremental revenue
```
(derived template, [16-01 Prompts](../lessons/16-01-cro-with-4080-marketing.md))
- All proof elements in variants must be real (ratings, "certified", review counts); the guest's "Nutritionist Certified" winner would need substantiation for us [16-01 58:44](../lessons/16-01-cro-with-4080-marketing.md).

### Step 6. Launch a true split
- Tools named: Convert.com, VWO, Intelligems, Optimizely; LTV tagging via Hyros or CRM [16-01 13:14–18:58](../lessons/16-01-cro-with-4080-marketing.md).
- 50/50, or 10–20% of traffic per test when running several; no overlapping tests on the same visitors where traffic allows [16-01 40:02–41:05](../lessons/16-01-cro-with-4080-marketing.md).
- Control seasonality and traffic quality: not "one variation during Black Friday and one during July" [16-01 16:33–17:33](../lessons/16-01-cro-with-4080-marketing.md).
- Don't cherry-pick weekdays [16-01 41:58](../lessons/16-01-cro-with-4080-marketing.md).
- Build in a visual editor; redirect tests as fallback. Team: test strategist, designer, developer, copywriter [16-01 50:03–51:54](../lessons/16-01-cro-with-4080-marketing.md).
- **IF** using a Calendly-style booking link **THEN** host the booking page on our domain so it can be tested [16-01 1:16:41–1:17:31](../lessons/16-01-cro-with-4080-marketing.md).

### Step 7. Read the result
| IF | THEN | Source |
|---|---|---|
| < 7 days | Don't call it; early days flip-flop | [16-01 41:58](../lessons/16-01-cro-with-4080-marketing.md) |
| ≥ 7 days, clearly losing | Turn off | [16-01 1:11:56](../lessons/16-01-cro-with-4080-marketing.md) |
| ≥ 14 days + one business cycle, ≥ 80–85% to win on EPS | Ship; queue a re-test of the winner | [16-01 42:55, 36:49](../lessons/16-01-cro-with-4080-marketing.md) |
| Drastic drop (−75%) | Check tracking/integration | [16-01 1:12:55](../lessons/16-01-cro-with-4080-marketing.md) |
| CRO loss but business win (subscriptions, new entry point) | Judge on business metric | [16-01 1:06:27–1:07:55](../lessons/16-01-cro-with-4080-marketing.md) |
| Winner was built for one ad angle and the angle changes | Re-test the page (congruence) | [16-01 1:17:31](../lessons/16-01-cro-with-4080-marketing.md) |
| Flat | Record; pick a bigger lever | [16-01 05:14, 22:41](../lessons/16-01-cro-with-4080-marketing.md) |

- Ship what wins; investigate "why" separately [16-01 11:22, 1:14:52](../lessons/16-01-cro-with-4080-marketing.md).
- Winners decay; "the original… was a previous winner"; don't judge a Black Friday page against everyday copy [16-01 58:44–59:40](../lessons/16-01-cro-with-4080-marketing.md).

### Step 8. Log incremental revenue
- Sheet columns (verbatim) [16-01 15:36](../lessons/16-01-cro-with-4080-marketing.md):
```
Test Name | Date Started | Date Ended | Control EPS | Variant EPS | Control Sessions | Variant Sessions | Sessions During Test | Days Test Ran | Test Incremental Revenue | Monthly Incremental Revenue | Projected 90 Day Incremental Revenue
```
- Monthly incremental = (variant EPS − control EPS) × monthly sessions; guest example: two-week test, 12,000 sessions → ~24,000/month × $0.50 = $12,000/month (derived arithmetic) [16-01 43:27–45:03](../lessons/16-01-cro-with-4080-marketing.md). Avoid annual projections: "a lot can change in a year."
- Record losers too [16-01 15:36](../lessons/16-01-cro-with-4080-marketing.md).

## Failure modes

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| "Winner" CVR up, revenue down | Judged on CVR only | EPS | [16-01 10:25](../lessons/16-01-cro-with-4080-marketing.md) |
| Results flip next month | Called too early; seasonality | Run rules; same period | [16-01 41:58, 16:33](../lessons/16-01-cro-with-4080-marketing.md) |
| Many tests, no lift | Micro-changes (button colour, fonts) | Big levers | [16-01 09:27, 22:41](../lessons/16-01-cro-with-4080-marketing.md) |
| Opinion wars | "Armchair CRO" | Test it; "we are not the market" | [16-01 02:29–05:44, 38:14](../lessons/16-01-cro-with-4080-marketing.md) |
| Copying a competitor page loses | Assumed it works | Test against our control | [16-01 37:44](../lessons/16-01-cro-with-4080-marketing.md) |
| Low-traffic site can't reach significance | Headline-level tests | Funnel/avatar/offer tests, sequential | [16-01 45:03, 40:02](../lessons/16-01-cro-with-4080-marketing.md) |
| Same test helps one brand, hurts another | "Best practices can be general practices" | Test per brand | [16-01 24:09](../lessons/16-01-cro-with-4080-marketing.md) |

## Where it's taught
- [16-01 CRO with 4080 Marketing](../lessons/16-01-cro-with-4080-marketing.md): guessing game [00:00–05:44]; EPS [11:22–14:11]; split-test infrastructure [13:14–19:53]; incremental revenue [14:41–16:33, 43:27–45:03]; inside-out [19:53–22:41]; philosophy [22:41–26:31]; customer ideation [26:31–33:56]; heatmaps [33:56–37:44]; pitfalls [37:44–40:02]; run rules [40:02–42:55]; price tests [46:58–48:29]; results [52:24–1:12:55].
- [16-02 eCom and Amazon with Eddie Maalouf](../lessons/16-02-ecom-and-amazon-with-eddie-maalouf.md): listicles [18:33–19:33]; whitelist page test [19:33–20:22]; run every campaign type [20:22–22:20]; offer fixes [23:18–24:16].
- [16-03 Funnel economics](../lessons/16-03-funnel-economics-with-spg.md): what a lift is worth; price tests both ways [26:52–28:52]; "A-B testing is king" [26:22].

## Cross-course notes
- **Page tests on Meta:** Evolve tests landing pages by duplicating the same 3 ads with a new URL inside one ad set (3:2:2:2 / Page #) ([campaign structure 3:2:2 §5.3](../../../evolve/start-here/frameworks/campaign-structure-322.md)); the 16-01 guest says only a random on-site split with the same traffic is a split test, and two ad sets per page "is not a split test" [16-01 16:33](../lessons/16-01-cro-with-4080-marketing.md). **Agent default:** use an on-site split tool (URL-level random split) for page/CRO decisions; treat Evolve's 3:2:2:2 as an ad-delivery page-fit signal, not a controlled test.
- **Button-colour tests:** the guest says don't [16-01 22:41](../lessons/16-01-cro-with-4080-marketing.md); Stefan lists button colour among A/B options in 16-03 [16-03 19:09–19:36](../lessons/16-03-funnel-economics-with-spg.md). **Default:** big levers first; micro-tests only on high-traffic pages after big levers are exhausted.
- **Explaining winners:** Evolve copywriting asks writers to explain why a winner won ([iteration outcomes](../../../evolve/copywriting/concepts/iteration-outcomes.md)); the guest prioritises the lift and investigates after. Both fine: ship on data, document a hypothesis.
- Shared [creative testing system](../../../../frameworks/creative-testing-system.md) covers ad-level tests; this page is on-site.

## Related
[paid traffic by platform](paid-traffic-by-platform.md) · [webinar funnel](webinar-funnel.md) · [launch a cold-traffic funnel](../playbooks/launch-a-cold-traffic-funnel.md) · [rules library](../libraries/rules.md)
