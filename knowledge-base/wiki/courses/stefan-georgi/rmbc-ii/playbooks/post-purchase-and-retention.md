---
title: "Playbook: post-purchase and retention (upsell flow, abandon cart, welcome, promo, reorder, winback)"
type: playbook
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; Patrick Stiles (16-05 upsell VSL data, guest)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-01-1-1-abandon-cart-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-02-1-2-welcome-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-03-1-3-promotional-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-04-1-4-winback-and-reorder-campaigns.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
tags: [playbook, post-purchase, upsell, cross-sell, downsell, email, abandon-cart, welcome, promotion, reorder, winback, ltv, aov]
updated: 2026-11-02
---

# Playbook: post-purchase and retention
> Run this when asked for upsells, a post-purchase flow or email sequences for a product: size the AOV/LTV gap, plan the upsell order and types, draft upsells in the Claude Upsell Generator, then build the five email flows (abandon cart, welcome, promotion, reorder, winback) in the Claude Email Sequence Generator, each outline-first and claim-audited.

## 🤖 Agent use
- **Use when:** planning or writing upsell #1-#N, a cross-sell, a downsell or call-booking upsell; writing any of the five email flows; or raising AOV/LTV because the front end loses money on day 0.
- **Inputs → outputs:** front-end product and offer, economics, supply length, complementary products, real proof, swipe upsells and email examples → `upsell-plan` (order, type, format, pricing), upsell scripts/pages, `email-plan` (flows, triggers, timing, discount ladder) and full sequences, each with a claim-audit block.
- **Rules:**
  - **DO** run the CAC/AOV/COGS arithmetic first; if the first order loses money, upsells are "one of the most obvious things you could do" ([14-01 v1 11:14](../lessons/14-01-upsells-overview.md)).
  - **DO** write upsell #1 as "Reaffirmation first, new or expanded problem second, irresistible offer third." ([14-01 doc; v2 00:34](../lessons/14-01-upsells-overview.md))
  - **DO** ask for an outline first in every project, then write ([15-05 SRT 02:10–02:43](../lessons/15-05-claude-project-for-writing-email-sequences.md)).
  - **DO** act as strategist: "you're more like a strategist than actually writing the copy" ([15-05 SRT 12:30–13:01](../lessons/15-05-claude-project-for-writing-email-sequences.md)); audit logic, timing, pricing and facts ([SRT 14:40; 20:16](../lessons/15-05-claude-project-for-writing-email-sequences.md)).
  - **DON'T** let upsell 2+ assume upsell 1 was bought ([14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)).
  - **DON'T** blame the front-end product when introducing the next offer; the new problem is time, effort, consistency or implementation ([14-02 v6 17:31–18:01; 22:17–22:44](../lessons/14-02-upsells-case-studies.md)).
  - **DON'T** reuse sample proof, pretexts or scarcity (named customers, ratings, "final cases", "I got a notification about you", "I've never offered 40% before"). Gate: [claim audit](../rubrics/llm-output-claim-audit.md).
  - **IF** margins allow **THEN** escalate discounts late, never start at the deepest ([15-01 v2 12:10–13:23](../lessons/15-01-1-1-abandon-cart-sequences.md)).
- **See also:** [Upsell formula](../concepts/upsell-formula.md) · [Upsell flow build](../frameworks/upsell-flow-build.md) · [Email sequences](../frameworks/email-sequences.md) · [Funnel economics](../concepts/funnel-economics.md) · [Templates library](../libraries/templates.md) · [Funnel audit section P](../rubrics/funnel-audit.md) · Tether: [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md)

## Required real inputs (ask for anything missing)
1. Front-end product, price paid, packages, and whether it is one-time or subscription.
2. Economics: CPA, AOV, COGS, margin floor (how deep any discount can go) ([15-01 v2 12:10–12:52](../lessons/15-01-1-1-abandon-cart-sequences.md)).
3. Upsell candidates: more of the same (stock-up pricing), upgraded version, complementary products (URLs), done-for-you/with-you services, community, call offer.
4. Supply length per unit (to compute run-out dates) and realistic shelf life ([15-04 02:21–05:52](../lessons/15-04-1-4-winback-and-reorder-campaigns.md); [15-03 02:43](../lessons/15-03-1-3-promotional-sequences.md)).
5. Shipping origin and times, tracking process, what is in the box, how to use it, what a customer can realistically notice in week 1 ([15-02 02:20–03:19](../lessons/15-02-1-2-welcome-sequences.md)).
6. Support contacts (phone, email, hours) ([15-01 v2 04:51–05:26](../lessons/15-01-1-1-abandon-cart-sequences.md)).
7. Real testimonials and reviews with permission; real customer results for reorder stories ([15-04 04:02–04:30](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)).
8. Real sale reasons and dates (holidays, surplus inventory) and real inventory status if cited ([15-03 01:07–02:11; 09:00–09:34](../lessons/15-03-1-3-promotional-sequences.md)).
9. Swipe upsells and email sequences for project knowledge (structure only).
10. ESP/flow tool and which triggers it supports (cart, checkout, purchase, cancel, days since order).

## Part A: upsells

### Stage A1: size the gap and plan the flow
- **Follow:** [upsell-formula](../concepts/upsell-formula.md) · [funnel-economics](../concepts/funnel-economics.md).
- **Worksheet (course structure, [14-01](../lessons/14-01-upsells-overview.md)):** `First purchase: CAC/CPA __  AOV __  COGS __  Net = AOV − CAC − COGS __`. Then: AOV needed to reach the goal; upsell take rate × price needed (illustration: take rate 20% → 40% is an AOV lever in [16-03 26:22](../lessons/16-03-funnel-economics-with-spg.md); "a good take rate can be 20%", guest claim, [16-05 42:44–43:04](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- **Choose upsell #1 type:**

| Front end | Upsell #1 default | Avoid | Cite |
|---|---|---|---|
| Consumable, one-time buyer (supplement, cleaner, skincare) | More of the same: stock-up pack at a deeper per-unit price | — | [14-01 v2 09:15](../lessons/14-01-upsells-overview.md); "Almost all of these did more of the same… because it works" [14-02 v4 22:27](../lessons/14-02-upsells-case-studies.md) |
| Subscription buyer | New or complementary problem | More of the same ("I want you on subscription") | [14-01 v2 09:47](../lessons/14-01-upsells-overview.md) |
| Big durable purchase | Complementary optimisation (his example: sauna → cold plunge) | A second unit | [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md) |
| Info product, book, coaching | Done-for-you, templates, faster/easier results, call | More of the same | [14-02 v5 06:56; v6 27:25](../lessons/14-02-upsells-case-studies.md) |

- **What to sell** (course list, verbatim headings, [14-01](../lessons/14-01-upsells-overview.md)): Results (better, faster, easier: done for you / automated / done with you; expanded); Savings; Holism ("You just solved part of the problem, now solve the entire problem").
- **Order:** community and done-for-you/with-you in later upsells, not #1 ([14-01 v2 16:19–17:16](../lessons/14-01-upsells-overview.md)); "How many upsells can you do? Test it." ([14-02 v1 16:55](../lessons/14-02-upsells-case-studies.md)).
- **Format:** direct-response (VSL-funnel) audiences → 10-15 min (even 18) video upsell that re-educates on the mechanism, names the cost of stopping, and closes with a one-time stock-up deal ([14-02 v4 05:03–05:32; 14:42](../lessons/14-02-upsells-case-studies.md)); branded e-com → short on-page upsell (Dr. Clean / Happy Mammoth style, [14-03 01:31–02:01](../lessons/14-03-claude-projects-for-upsells.md)). Guest data: upsell VSLs ~24 min average and falling, best ~20 min, seeking bar +60% engagement ([16-05 43:04–43:33](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- **Bump interaction:** an order bump can cut upsell take and lower total AOV; decide by revenue per order across the funnel ([11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)).
- **Output:** `upsell-plan`: upsell #, type, product, price, format, length, what it assumes, downsell.
- **Gate:** user approves the plan; funnel audit P1-P3.

### Stage A2: set up the Claude Upsell Generator
- **Follow:** [upsell-flow-build](../frameworks/upsell-flow-build.md) · [claude-project-recipe](../concepts/claude-project-recipe.md).
- **Project instructions (course, verbatim, [14-03](../lessons/14-03-claude-projects-for-upsells.md)):**
  ```text
  Claude Upsell Generator (Longer Scripts)

  Your job is to generate upsell video scripts. They will typically be between 6 minutes and 16 minutes in length. The documents in your knowledge base includes transcripts from several upsell videos which we can model off while writing new upsells. What you'll want to do is analyze the structure of the various upsell examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new upsells.

  In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current upsell project is.

  One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
  ```
  Knowledge: five swipe upsells as PDFs ([14-03 00:00–00:59](../lessons/14-03-claude-projects-for-upsells.md)). Derived addition: the no-invented-proof line from [write-a-vsl-with-claude](write-a-vsl-with-claude.md) Stage 2.

### Stage A3: draft upsell #1
- **Inputs:** product link (physical) or brief (info); unified research doc/brief if available ([14-03 01:01; 03:09–03:41; 05:12](../lessons/14-03-claude-projects-for-upsells.md)).
- **Prompts (course, verbatim, [14-03](../lessons/14-03-claude-projects-for-upsells.md); placeholders ours):**
  - Run: "Please do a [10] minute upsell script for someone who just bought [product], selling them more of the same. [URL]"
  - Steer to a swipe: "I liked it, but let's model more heavily off of the [swipe A] and [swipe B] structure."
  - Swipe-to-outline route ([14-02](../lessons/14-02-upsells-case-studies.md)): "Here is a video script for an upsell in the [category] space. I want you to analyze it and then create an outline for the structure of the script." → "Now we're going to be writing a new upsell script [for] a different product. I want you to closely model off the [swipe] Upsell as far as structure and length. Also in style and tone. We're going to do this through multiple outputs which means you can go section-by-section… Do not try to condense things, good video scripts are often quite long."
  - More-of-the-same redirect: "since in this case we're selling more [product]. So we don't need to position and then intro a new product…"
  - Expectations timeline: "add… a section where it's like 'here's what you can expect during your journey with [product]: Your First Week, Your First Month… Sixth Month'" (only outcomes the truth sheet supports).
- **Must include:** within the first seconds, the order is being prepared, they are in the right place, don't hit back ([14-02 v6 11:19](../lessons/14-02-upsells-case-studies.md)); per-unit saving and what each unit replaces stated, not left to mental math ([14-02 v1 06:59](../lessons/14-02-upsells-case-studies.md)).
- **Reject:** lines that insult logic or "make them feel like shit" → ask for an empathetic version ([14-03 02:38–04:11](../lessons/14-03-claude-projects-for-upsells.md)); stock-out or price-rise threats unless true (the course big-idea line "what if… the product is either out of stock or costs a lot more money?" is structure only, [14-01 doc](../lessons/14-01-upsells-overview.md)).
- **Output:** upsell #1 script.
- **Gate:** [claim audit](../rubrics/llm-output-claim-audit.md); if a video, [VSL review](../rubrics/vsl-review.md) S14-S17 and B12 (seeking bar, ≤ ~20 min).

### Stage A4: upsell 2+ and call upsells
- Shorter reaffirmation ("you really mean business / you're an action-taker") ([14-02 v6 34:03–36:49](../lessons/14-02-upsells-case-studies.md)); state that it is shown regardless of earlier choices ([14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)).
- Call upsell: "instead of talking about the price, you should really be selling them on booking a call" ([14-03 08:17–09:07](../lessons/14-03-claude-projects-for-upsells.md)).
- **Gate:** claim audit.

## Part B: email flows

### Stage B1: set up the Claude Email Sequence Generator
- **Project instructions (course, verbatim, [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md)):**
  ```text
  Your job is to create various email sequences for different products and services. These will range from eCom products, to coaching or information products.

  You have several documents in your knowledge base that should provide all of the examples you need to write great sequences. You'll see that there are several examples for:

  Abandoned Cart Series
  Welcome Email Series (For New Customers)
  Special Sales and Promotions Series (Holiday Sales, Flash Sales, etc)
  Reorder Series (For Getting A Customer to Order More of a Product Prior to Running Out)
  Winback Series (For Getting a Previous Customer to Once Again Become a Customer).

  You'll also notice that some of the sequences focus more heavily on discounting, while some focus more on emotion.

  What will happen is that I will give you instructions about the kind of email sequence I'm looking to have written, as well as the product or service or brand we are writing the sequence for. You'll then select from relevant examples, synthesizing across several of them when necessary, to create a new sequence.
  ```
  Knowledge: the sample sequences (15 in the course). Give product URLs or a brief per request ([15-05 SRT 08:21; 22:00–23:12](../lessons/15-05-claude-project-for-writing-email-sequences.md)).

### Stage B2: abandon cart (build first; it recovers CPA)
- **Why first:** 100 checkout visitors, 20 buyers, $5,000 spend = $250 CPA; with $150 AOV that is -$100 per customer; 15 recovered buyers → 35 customers, $142.86 CPA, about +$7 per customer (instructor example, [15-01 00:29–03:44](../lessons/15-01-1-1-abandon-cart-sequences.md)).
- **Prompt (course, verbatim, [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md); placeholders ours):** "To start, let's do a 7 day abandon cart sequence for [product]. Let's introduce a [20]% off discount on Day 3, and increase it to a [40]% off Discount on Days 5-7. Can you please outline this sequence for me and then after I approve I'll have you write it. [URL]"
- **Tone feedback (verbatim):** "let's make sure it is empathetic and supportive. We want to call out pain points, but we want to do it more like: 'maybe you've experienced this.' Or 'Some of our customers share that ____' when talking about negatives…"
- **Shape (course samples, [15-01](../lessons/15-01-1-1-abandon-cart-sequences.md)):** email 1 at trigger, email 2 +6 h, then about daily; hardest push in the first 24 h ([v2 05:26–06:37](../lessons/15-01-1-1-abandon-cart-sequences.md)); tag each email with the abandonment reason it attacks: incomplete information, negative past experience, lack of confidence, no trust, price, life got in the way, lack of urgency ([04:44–12:36](../lessons/15-01-1-1-abandon-cart-sequences.md)); FAQ email; phone/hours in the P.S.; discount ladder e.g. 30% → 50% or 25% → 40% depending on margin ([v2 12:10–12:52](../lessons/15-01-1-1-abandon-cart-sequences.md)).
- **Book-a-call offers:** no discount; objection crushing, real timing, peer pressure, future regret ([v2 19:38–26:12](../lessons/15-01-1-1-abandon-cart-sequences.md)).

### Stage B3: welcome (post-purchase onboarding)
- **Five purposes** for every email: reaffirm decision, answer vital questions, build relationship and trust, turn one-time into repeat customers, encourage consumption ([15-02 00:00–01:00](../lessons/15-02-1-2-welcome-sequences.md)).
- **Prompt (course, verbatim pattern, [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md)):** "Now let's do a new customer welcome sequence for [product]. Let's have it be [10] emails. In email #3, let's introduce our [complementary product] as a great compliment to [product], and give the customer a [20]% off code… Please provide an outline of the sequence to me and once I've approved it, I'll have you write it."
- **Timing:** email 1 immediately (thanks, what to expect, ship origin and timing, tracking, what's in the box, support, small code in P.S.); optional founder video at +6 h; check-in timed to real delivery ("Use common sense"); after two weeks move to weekly ([15-02 02:20–08:00](../lessons/15-02-1-2-welcome-sequences.md)). Fix timing logic in feedback (course example: a "one week check-in" on day 5 "doesn't make sense", [15-05 doc 4](../lessons/15-05-claude-project-for-writing-email-sequences.md)).
- **Don't:** "member" language unless true ([15-02 04:00; 05:38](../lessons/15-02-1-2-welcome-sequences.md)); invented pretexts ([15-02](../lessons/15-02-1-2-welcome-sequences.md)). Info/coaching next step: re-sell and answer objections ([13:09–13:46](../lessons/15-02-1-2-welcome-sequences.md)).

### Stage B4: reorder and winback
- **Reorder:** anchor to estimated run-out: −7 days, −3, −1, day of run-out ([15-04 02:21–05:52](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)); progress-and-loss framing: "you're making progress; you'll make even more progress if you keep going; if you don't keep going, you'll lose progress" ([00:34–01:14](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)); don't over-scare on day 1 ([04:30–05:05](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)).
- **Winback (consumable):** sample triggers day 45, 47, 50, 52 after last order; "noticing something since you stopped?" (only effects the truth sheet supports); "month two is when most breakthroughs happen" adapted to the product's real timeline; discounts start ~20% and rise to 40-50% ([15-04 07:28–10:32](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)).
- **Winback (subscription/SaaS/biz-op):** identity and mindset ("don't become another what-if story") plus real active-user wins; sample days 14-21 after cancellation ([15-04 11:05–13:39](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)).

### Stage B5: promotions
- **Prompt (course, verbatim pattern, [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md)):** "Now I want to do a [3] Day sale for [holiday] for [brand]. Let's make it site wide (all products), and they can save [30]%. Please provide an outline." Feedback example: "let's do 3 emails on Day 3. Also don't forget about our other two Skus as well".
- **Rules:** real reason for the sale; deadline in the first email and every email; ≥ 3 sends on the last day; per-SKU math when several SKUs; preview email 6 days before Black Friday; re-explain the product to mixed audiences ([15-03 01:07–13:24](../lessons/15-03-1-3-promotional-sequences.md)). Only real inventory and sales figures ([15-03 09:34](../lessons/15-03-1-3-promotional-sequences.md)).

### Stage B6: gates and measurement
1. [Claim audit](../rubrics/llm-output-claim-audit.md) on every upsell and email (C2, C5, C6, C13, C15, C20 are the usual fails in these lessons).
2. Fact pass: prices, codes, dates, guarantee length, shipping times match the truth sheet ("Pricing is off on this", [15-05 SRT 20:16](../lessons/15-05-claude-project-for-writing-email-sequences.md)).
3. [Funnel audit](../rubrics/funnel-audit.md) section P.
4. Measure: upsell take rate and revenue per order across the whole funnel (not bump take alone); recovered orders and blended CPA ([16-03 47:08–49:29](../lessons/16-03-funnel-economics-with-spg.md)); repeat-purchase and reorder rates.

## Email plan template
```text
EMAIL PLAN: <brand/product>
Flow | Trigger | # emails | Timing | Discount ladder (margin floor __%) | CTA | Claim audit
Abandon cart | checkout started | 7 | 0, +6h, then daily | __% day 3 → __% days 5-7 | return to checkout | __
Welcome | first purchase | __ | 0, +6h, +1d … weekly after 2 wks | cross-sell codes at #__ | consume / repeat | __
Reorder | run-out − 7d | 4 | −7, −3, −1, 0 | __% on run-out day | reorder | __
Winback | __ days since last order / cancel | 4 | __ | __% → __% | return | __
Promo | real event __ | __ | dated; ≥ 3 on last day | __% | buy | __
```

## Related
- [Offer to funnel end to end](offer-to-funnel-end-to-end.md) · [Launch a cold-traffic funnel](launch-a-cold-traffic-funnel.md) · [Playbooks hub](README.md) · [Prompts library](../libraries/prompts.md)
