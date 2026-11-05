---
title: "Checkout Optimization (spec, audit, bump test)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-01-checkouts-walkthrough-part-1.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-01-cro-with-4080-marketing.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
tags: [checkout, order-bump, subscription-disclosure, microcopy, aov, trust, mobile]
updated: 2026-11-02
---

# Checkout Optimization
> The selling is done by checkout, so remove doubt and friction: state "no subscription" when true, put reassurance next to the button on mobile, justify price in numbers, keep add-ons opt-in, and test any order bump on full-funnel revenue per order, not take rate.

## 🤖 Agent use
- **Use when:** specifying, writing microcopy for, or auditing a checkout / order page (Shopify or custom); deciding on an order bump, quantity toggle, phone number or timer.
- **Inputs → outputs:** offer, price ladder, guarantee, shipping and subscription terms, traffic source (affiliate or not), planned upsell(s), competitor checkout screenshots → checkout spec (elements, order, microcopy) + teardown rows + test list.
- **Rules:**
  - **DO** treat checkout as "a formality… it's just time to buy", but "we can't assume the person is going to buy." [11-01 00:00–01:27](../lessons/11-01-checkouts-walkthrough-part-1.md)
  - **DO** state "one-time purchase, no subscription" when true: "it hurts people's conversions every time by not saying no subscription if it's not a subscription." [11-01 10:58–11:26, 19:53](../lessons/11-01-checkouts-walkthrough-part-1.md); Emma's line "probably pays for RMBC 100 times over" (instructor claim) [11-02 05:49](../lessons/11-02-checkouts-walkthrough-part-2.md)
  - **DO** audit on mobile: "mobile is actually the way I would really look at most of this stuff." [11-01 11:53](../lessons/11-01-checkouts-walkthrough-part-1.md)
  - **DON'T** label the button "Buy now"; use "Complete order" or a claim-the-offer label. "What is on this button actually does really matter." [11-02 04:47](../lessons/11-02-checkouts-walkthrough-part-2.md)
  - **DON'T** pre-check paid add-ons (Dr. Clean's pre-added "shipping warranty": "very sneaky… free money for them") [11-01 12:29–13:03](../lessons/11-01-checkouts-walkthrough-part-1.md).
  - **DON'T** use fake scarcity. The "59% left in stock" bar is "probably not true… not condoning it" [11-01 04:04](../lessons/11-01-checkouts-walkthrough-part-1.md). Timers and stock bars only when real.
  - **DON'T** hide a subscription: "super shady and not sustainable long term… but you also don't want to hammer them." [11-02 21:35](../lessons/11-02-checkouts-walkthrough-part-2.md)
  - **DON'T** put terms in an image: "you can't copy and paste it… it's shady AF"; Stefan refused to buy [11-01 17:43–19:53](../lessons/11-01-checkouts-walkthrough-part-1.md).
  - **IF** adding an order bump **THEN** A/B it against the upsell on total revenue per order; it can lower final AOV [11-02 16:30–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md), [16-03 26:22](../lessons/16-03-funnel-economics-with-spg.md).
- **See also:** [pdp-build](pdp-build.md) · [upsell-flow-build](upsell-flow-build.md) · [cro-testing](cro-testing.md) · [funnel economics](../concepts/funnel-economics.md) · [funnel audit rubric](../rubrics/funnel-audit.md) · [compliance red flags](../concepts/compliance-red-flags.md) · shared [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) · [risk reduction hooks](../../../../concepts/risk-reduction-hooks.md) · [Shopify landing pages with Claude](../../../../resources/shopify-landing-pages-with-claude.md)

## Definition
RMBC II's checkout module is a teardown of seven live checkouts (Dr. Clean, David Protein, Clarifion, Happy Mammoth, Emma, SynoCell, Capital Syndicate) [11-01 00:00–01:27](../lessons/11-01-checkouts-walkthrough-part-1.md). No Claude prompts are used; the output is a spec and checklist. Stefan: "honestly not a whole lot has changed" since his earlier checkout module [11-01 00:00](../lessons/11-01-checkouts-walkthrough-part-1.md).

## Procedure

### Step 1. Gather offer facts
- **Input:** product, price ladder, shipping rules, guarantee length, subscription yes/no, digital vs physical, affiliate traffic yes/no, upsell plan.
- **Output:** fact sheet. Every microcopy line below must be true against it.
- **IF** any fact is missing (guarantee days, recurring terms) **THEN** bracket it `[VERIFY: …]`; never guess.

### Step 2. Price benchmark
- **Input:** our per-unit price; 4–6 category prices from retailers.
- **Output:** per-unit / per-use comparison line.
- Stefan priced all-purpose cleaners at Instacart, Publix, Target and Sprouts ($1.99–$8) before judging Dr. Clean's $19.95 [11-01 05:03–08:22](../lessons/11-01-checkouts-walkthrough-part-1.md); he later found one bottle ≈ six tablets, so per-cleaner price was actually lower, "but they don't make that clear" [10-02 09:05–09:33](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md).
- **IF** our price is above category **THEN** show per-unit math beside the package selector and keep proof on the checkout: "Why do I need all this copy… to sell a cleaning spray? Because I'm going to charge you… triple the cost" [11-01 10:25](../lessons/11-01-checkouts-walkthrough-part-1.md).

### Step 3. Choose checkout type
- **Output:** one of: Shopify 2-step / custom 1-page / combined PDP + checkout / 2-step with low-friction first step.

| IF | THEN | Example | Source |
|---|---|---|---|
| Branded Shopify store | Shopify 2-step (info → shipping and payment), express pay on top | Happy Mammoth, David Protein | [11-02 00:29](../lessons/11-02-checkouts-walkthrough-part-2.md), [11-01 14:04](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| DR funnel, want more control | Custom checkout that looks like Shopify | Emma | [11-02 05:18](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| Advertorial already sold hard | Combined PDP + checkout (pick 1/3/6, card on same page) | Clarifion | [11-01 16:10](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| Digital offer after VSL | 2-step: step 1 name + email only, step 2 billing + offer stack | Capital Syndicate | [11-02 15:07–16:31](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| Custom (off-Shopify) checkout | Confirm pixel events and click IDs survive | Emma | [11-02 How to apply](../lessons/11-02-checkouts-walkthrough-part-2.md) |

- Payment friction feeds funnel choice: BNPL / Apple Pay → shorter checkout, more upsells [13-01 36:49](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md). See [funnel selection matrix](../concepts/funnel-selection-matrix.md).

### Step 4. Assemble the element stack
- **Output:** ordered checkout spec. Derived from both parts:

| # | Element | Rule | Source |
|---|---|---|---|
| 1 | Header contact | Phone only if no affiliate traffic; else email | [11-02 13:34–14:37](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 2 | Timer | Only if price or cart is actually reserved | [11-01 03:33](../lessons/11-01-checkouts-walkthrough-part-1.md), [11-02 05:18](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 3 | Express pay | Shop Pay / PayPal / Google Pay on top | [11-02 00:29](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 4 | Form | Address autocomplete ("helps to reduce shipping errors") | [11-01 11:26](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| 5 | Order summary | Product, qty, shipping, total, **total savings**; not hidden on mobile | [11-01 12:29, 13:03](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| 6 | Quantity toggle | Test 1 / 3 / 6 with per-bottle price for AOV | [11-02 07:04](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 7 | Reassurance block | Guarantee, "one-time · no subscription · no hidden fees", security badges, real spokesperson only | [11-02 05:18–06:54](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 8 | Testimonials | 2–4; current-year if dated | [11-02 01:13–01:44, 22:02](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 9 | Objection lines | Shipping, temperature, refill, instant access | [11-01 15:38](../lessons/11-01-checkouts-walkthrough-part-1.md), [11-02 12:52](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 10 | Offer stack (digital) | "Here's what you're about to receive" + bonuses | [11-02 15:36–16:31](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 11 | Checkout FAQ | "Is this a subscription or a one-time payment?" | [11-02 15:36](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 12 | Bump | Unchecked, visible, small vs main offer; see Step 6 | [11-02 16:31](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| 13 | Fees | Plain statement; not "fees will be applied at the end" | [11-01 11:53–12:29](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| 14 | Terms | Text, not an image | [11-01 17:43–19:53](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| 15 | SMS consent | Disclose marketing use | [11-02 06:24](../lessons/11-02-checkouts-walkthrough-part-2.md) |

- **IF** digital product **THEN** add instant-access line so buyers do not expect shipping [11-02 12:52](../lessons/11-02-checkouts-walkthrough-part-2.md).
- **IF** physical product with free-shipping thresholds **THEN** consider a cart progress widget (free shipping at 2, gift at 3) for AOV (David Protein) [11-01 15:09](../lessons/11-01-checkouts-walkthrough-part-1.md).

### Step 5. Write microcopy
- **Output:** final lines. On-screen and spoken examples (use only if true) [11-01](../lessons/11-01-checkouts-walkthrough-part-1.md), [11-02](../lessons/11-02-checkouts-walkthrough-part-2.md):
```
Button: "Complete order"  /  "Claim your supply now"   (never "Buy now")
Trust block: "This is a one-time purchase. No subscription. No hidden fees."
Savings line: "Total savings: $[amount]"
Timer: "Your special price is reserved for [m:ss]"  /  "Order in the next [m:ss] to secure your membership & bonuses."
Digital-product note: "NOTE: This is a digital product available for instant access"
Bump: "ONE TIME OFFER: Want our bonus [item]? Click YES to add this digital [item] to your order. (This offer is not available at any other time.)"
Checkout FAQ: "Is this a subscription or a one-time payment?"
Header phone (only without affiliates): "Order or ask questions by phone: [number]"
Guarantee / support: "[N]-day money-back guarantee · Professional customer support"
```
- Button choice: Stefan endorses both "Complete order" ("feels nice to complete") [11-01 09:57](../lessons/11-01-checkouts-walkthrough-part-1.md) and "Claim your supply now" [11-02 04:47](../lessons/11-02-checkouts-walkthrough-part-2.md). **Agent default (derived):** "Complete order" on the payment step; claim-the-offer wording on the PDP/package CTA; A/B the payment-step button.
- **DON'T** assume "risk-free trial" converts: people are "really burned" on subscriptions; worth testing only [11-02 03:45–04:19](../lessons/11-02-checkouts-walkthrough-part-2.md).

### Step 6. Order-bump decision (math gate)
- **Input:** bump price and expected take; upsell price and take with/without bump.
- **Output:** go / no-go / test.
- Formula (derived from [11-02 17:42–19:04](../lessons/11-02-checkouts-walkthrough-part-2.md)):
```
Revenue per order without bump = upsell_take_no_bump × upsell_price
Revenue per order with bump    = bump_take × bump_price + upsell_take_with_bump × upsell_price
Ship the bump only if (with bump) > (without bump) in a live A/B test.
```
- Stefan's hypothetical: no bump 0.20 × $97 = $19.40; with $27 bump at 40% and upsell falling to 7%: $10.80 + $6.79 = $17.59. (He says "$1.40"; the arithmetic is $1.81.) "The good thing about these offer bumps is that your conversion rate's high. The bad thing is it could actually make your AOV lower." [11-02 19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)
- 16-03 repeats: "A-B testing is king": test bumps because they can interfere with upsells; bump examples "$20 add-on that costs $3" and a $27 info bump [16-03 25:03–26:52](../lessons/16-03-funnel-economics-with-spg.md). Economics: [funnel economics](../concepts/funnel-economics.md).
- **IF** no upsell exists **THEN** the cannibalization risk is absent; test the bump on AOV and front-end CVR (derived).

### Step 7. Mobile pass
- **Output:** phone-width screenshots + fixes.
- Move guarantee and "no subscription" above the place-order button on mobile; Stefan bets "probably like a 10% lift at least" (instructor bet, untested) [11-02 08:56–09:27](../lessons/11-02-checkouts-walkthrough-part-2.md).
- Prefer the form above the fold; if it is pushed down by proof, that signals price shock [11-02 07:35–08:56](../lessons/11-02-checkouts-walkthrough-part-2.md).
- Order summary should not hide pre-added items [11-01 12:29](../lessons/11-01-checkouts-walkthrough-part-1.md).

### Step 8. Test
- CRO places checkout second in test priority, after upsells: "upsells, checkout, cart, sales/landing pages, product pages…" (guest claim, Ethan Bence) [16-01 20:45](../lessons/16-01-cro-with-4080-marketing.md). Checkout is "often set live once and never tested"; adding social proof where it was absent "can lift conversion 10, 15, 20%" (guest claim) [16-01 21:15](../lessons/16-01-cro-with-4080-marketing.md).
- Test queue (derived from both parts): no-subscription line; reassurance above mobile button; button label; quantity toggle; bump on/off; phone number (non-affiliate); package ladder 1-2-3-4 vs 1-3-6 [11-01 09:02](../lessons/11-01-checkouts-walkthrough-part-1.md).
- Run rules: [cro-testing](cro-testing.md).

## Failure modes

| Symptom | Likely cause | Fix | Source |
|---|---|---|---|
| Abandonment at payment | Subscription unclear | Plain "one-time · no subscription" or plain recurring terms | [11-01 10:58](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| Buyer distrust, refunds, chargebacks (derived) | Pre-checked add-ons; terms as image | Opt-in add-ons; text terms | [11-01 12:29, 17:43](../lessons/11-01-checkouts-walkthrough-part-1.md) |
| Price shock | No per-unit math | Step 2 comparison | [10-02 14:23](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) |
| AOV up, total revenue per buyer down | Bump cannibalizes upsell | Step 6 gate | [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| "Is this brand still around?" | Old dated testimonials | Refresh or undate | [11-02 01:13](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| Affiliate conflict | Phone in header | Remove phone on affiliate traffic | [11-02 13:34](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| Lost attribution | Custom checkout drops pixel / click IDs | Verify tracking before launch | [11-02 How to apply](../lessons/11-02-checkouts-walkthrough-part-2.md) |

## Compliance
- Fake timers, stock bars and "stock keeps selling out" are course-observed but not recommended; real only ([11-01 04:04](../lessons/11-01-checkouts-walkthrough-part-1.md)).
- Recurring billing: show terms plainly (US negative-option rules) [11-02 Compliance check](../lessons/11-02-checkouts-walkthrough-part-2.md).
- Spokesperson doctors and "verified customer" labels: real and disclosed, or remove.
- SMS: explicit consent language that discloses marketing use.

## Where it's taught
- [11-01 Checkouts part 1](../lessons/11-01-checkouts-walkthrough-part-1.md): scope [00:00–01:27]; Dr. Clean [02:00–13:32]; David Protein [13:32–16:10]; Clarifion [16:10–20:28]. Note: page built from platform captions; Part 1 video file is a duplicate of Part 2.
- [11-02 Checkouts part 2](../lessons/11-02-checkouts-walkthrough-part-2.md): Happy Mammoth [00:00–03:00]; Emma [03:09–10:00]; SynoCell [10:07–12:01]; Capital Syndicate [12:01–20:12]; bump math [16:31–19:32]; subscription visibility and testimonial dates [20:52–22:20].
- [10-02 Dr. Clean PDP](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md): price-comparison correction [09:05–14:58].
- [16-01 CRO](../lessons/16-01-cro-with-4080-marketing.md): inside-out test order [19:53–22:10].
- [16-03 Funnel economics](../lessons/16-03-funnel-economics-with-spg.md): AOV levers incl. bump [25:03–26:52].

## Cross-course notes
- Shared Tether [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) covers bundle anchoring; RMBC adds the bump-vs-upsell math gate and the no-subscription line.
- Evolve Start Here has no checkout framework; its KPI pages ([kpis-and-columns](../../../evolve/start-here/frameworks/kpis-and-columns.md)) define ad-side metrics only.

## Related
[pdp-build](pdp-build.md) · [upsell-flow-build](upsell-flow-build.md) · [upsell formula](../concepts/upsell-formula.md) · [benchmarks](../libraries/benchmarks.md) · [templates](../libraries/templates.md)
