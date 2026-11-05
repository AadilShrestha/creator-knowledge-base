---
title: "Email Sequences (abandon cart, welcome, promo, reorder, winback) with a Claude Project"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-01-1-1-abandon-cart-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-02-1-2-welcome-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-03-1-3-promotional-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-04-1-4-winback-and-reorder-campaigns.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
tags: [email, abandon-cart, welcome-series, promotions, reorder, winback, discount-ladder, timing, claude-project, retention]
updated: 2026-11-02
---

# Email Sequences
> Pick the sequence type, set its trigger and timing table, assign one reason or purpose per email, set the discount ladder from margin, have a Claude Project (loaded with the 15 course sample sequences or our own) outline first, approve, write, then audit timing, pricing, facts and tone before any send.

## 🤖 Agent use
- **Use when:** writing or auditing an abandoned-cart, welcome, promotional (holiday / Black Friday / flash), reorder or winback sequence for an e-com, info or coaching offer.
- **Inputs → outputs:** sequence type; product URL or brief; price, margin floor (max discount), guarantee, shipping and delivery timing, days of supply, support phone/hours, real testimonials and customer language, true sale reason and deadline, real inventory status → timing table (email #, send time, reason/purpose, subject options, offer) → outline → full copy with 2–3 subject options per email → audited sequence.
- **Rules:**
  - **DO** ask for an outline first, approve it, then write: "Can you please outline this sequence for me and then after I approve I'll have you write it." [15-05 SRT 02:10–02:43](../lessons/15-05-claude-project-for-writing-email-sequences.md)
  - **DO** act as strategist: "you're more like a strategist than actually writing the copy." [15-05 SRT 12:30–13:01](../lessons/15-05-claude-project-for-writing-email-sequences.md)
  - **DO** tag each abandon-cart email with one abandonment reason; don't repeat the same message [15-01 04:44–12:36](../lessons/15-01-1-1-abandon-cart-sequences.md).
  - **DO** hit hardest in the first 24 hours; email 2 at +6 hours [15-01 v2 05:26–06:37](../lessons/15-01-1-1-abandon-cart-sequences.md).
  - **DON'T** start at the deepest discount: "start with like 30% off and move to 50% off or start with 25% off and move to 40% off… Depends on margins." [15-01 v2 12:10–12:52](../lessons/15-01-1-1-abandon-cart-sequences.md)
  - **DON'T** assume what the reader thinks; "maybe you've experienced this" / "Some of our customers share that ___" [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md); "Let me guess…" [15-01 v2 22:07](../lessons/15-01-1-1-abandon-cart-sequences.md).
  - **DON'T** invent scarcity, traction or customers. The samples contain "347% increase in order volume", "we're down to our final cases", "I never will again", invented "Maria", A1C outcomes; all are structure only [15-03 compliance table](../lessons/15-03-1-3-promotional-sequences.md), [15-01 Version 2](../lessons/15-01-1-1-abandon-cart-sequences.md).
  - **DON'T** ship AI copy unread: "It's doing 99% of the work for you." [15-05 10:44](../lessons/15-05-claude-project-for-writing-email-sequences.md)
  - **IF** CTA is a booked call on a high-ticket offer **THEN** no discount; objections, real scarcity, peer pressure, future regret [15-01 v2 19:38–26:12](../lessons/15-01-1-1-abandon-cart-sequences.md).
- **See also:** [upsell flow build](upsell-flow-build.md) · [checkout optimization](checkout-optimization.md) · [funnel economics](../concepts/funnel-economics.md) · [claude project recipe](../concepts/claude-project-recipe.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [compliance red flags](../concepts/compliance-red-flags.md) · [prompts library](../libraries/prompts.md) · [templates library](../libraries/templates.md) · Evolve [objection handling](../../../evolve/copywriting/concepts/objection-handling.md) · shared [risk reduction hooks](../../../../concepts/risk-reduction-hooks.md)

## Procedure

### Step 1. Justify and choose the sequence
- **Input:** checkout conversion, CPA, AOV. **Output:** sequence list with expected impact.
- Abandon-cart math (Stefan): 100 checkout visitors, 20 buy, $5,000 spend → $250 CPA; AOV $150 → −$100 per customer. Recover 15 more by email/SMS/call center → 35 customers, $142.86 CPA, ~+$7 gross per customer [15-01 00:29–03:44](../lessons/15-01-1-1-abandon-cart-sequences.md). Plug in our numbers (derived).

| Sequence | Trigger | Goal | Source |
|---|---|---|---|
| Abandon cart | Checkout started, no order | Recover the sale | [15-01](../lessons/15-01-1-1-abandon-cart-sequences.md) |
| Welcome | First purchase | Reaffirm, answer questions, trust, repeat purchase, consumption | [15-02 00:00–01:00](../lessons/15-02-1-2-welcome-sequences.md) |
| Promo | Calendar or real reason | Revenue spike from list | [15-03](../lessons/15-03-1-3-promotional-sequences.md) |
| Reorder | Estimated run-out date | Repeat order with no gap | [15-04 01:14–05:52](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |
| Winback | No order after reorder window / cancellation | Reactivate | [15-04 05:52–14:38](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |

### Step 2. Set up the Claude Project (once)
- Name "Claude Email Sequence Generator"; paste instructions (verbatim) [15-05 doc 1](../lessons/15-05-claude-project-for-writing-email-sequences.md):
```
New Project Name:
Claude Email Sequence Generator

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
- Knowledge: the 15 course sample sequences (+1 SMS sample) or, better, our own proven sequences [15-05 SRT 00:30–01:36](../lessons/15-05-claude-project-for-writing-email-sequences.md). The course samples carry invented claims; add a note in the project that examples are structure-only (derived).
- **Failure mode:** the recorded 15-05 video file is actually the upsell project; the email walkthrough lives in the platform SRT and docs [15-05 §0](../lessons/15-05-claude-project-for-writing-email-sequences.md).

### Step 3. Build the timing table for the chosen type

**3a. Abandon cart (7 days)** [15-01 v2 05:26–14:33](../lessons/15-01-1-1-abandon-cart-sequences.md)

| # | Timing | Reason it attacks (pick per email) | Angle |
|---|---|---|---|
| 1 | At trigger | Life got in the way / trust | Reconnect, future pacing, social proof, support line |
| 2 | +6 h | Trust / incomplete info | Social proof + "why trust us" (guarantee, no subscription, shipping) |
| 3 | +1 day | Lack of confidence | Real customer story + future pacing + price anchor |
| 4 | +1 day | Incomplete information | FAQ email |
| 5 | +1 day | Negative past experience / belief | Science/mechanism or risk reversal |
| 6 | +1 day | Price | Discount upgrade |
| 7 | Final day (1–3 sends) | Urgency | Deadline close |

- Reason map (Stefan's buckets): incomplete information; negative past experience; lack of confidence (self or outside approval); no trust in you; price too high; life got in the way; lack of urgency (pain or offer) [15-01 04:44–12:36](../lessons/15-01-1-1-abandon-cart-sequences.md).
- **IF** price/urgency is the assumed reason **THEN** discount-led (course V1: 50% → 60% on day 6). **IF** confidence/past failure **THEN** emotion-led with first discount on day 3 (V2: 40% day 3 → 55% day 5). Stefan's pick for supplements: V2, plus phone number from email 3 [15-01 v2 19:38](../lessons/15-01-1-1-abandon-cart-sequences.md).
- **IF** book-a-call coaching **THEN** V3: recap + "what stopped you?" → objection crushing ("Let me guess…") → fear-of-failure story → timing logic → real scarcity with reason → peer pressure → future regret [15-01 v2 19:38–26:12](../lessons/15-01-1-1-abandon-cart-sequences.md).
- **IF** low-ticket course ($97) **THEN** "use the supplement thing, but do a discount for a course" [15-01 v2 26:46](../lessons/15-01-1-1-abandon-cart-sequences.md).
- P.S. on most emails: real support phone and hours; it "converts people with unspoken questions" [15-01 v2 04:51–05:26](../lessons/15-01-1-1-abandon-cart-sequences.md).

**3b. Welcome** [15-02](../lessons/15-02-1-2-welcome-sequences.md)

| Email type | Timing | Purpose | Source |
|---|---|---|---|
| Thank-you / what to expect (ship timing, tracking, box contents, support, optional code) | Immediately | Reaffirm, answer questions | [02:20–03:19] |
| Founder video | +6 h | Trust | [03:19–03:57] |
| Unboxing / how to use / portal tour | +1–2 days | Consumption | [04:28–05:05] |
| Arrival check / first assignment | +3 days (time to real delivery) | Consumption | [05:05–06:36] |
| Repeat-purchase or cross-sell offer | +5–7 days | Repeat customer | [05:38–07:08] |
| Survey with reward | +2 weeks | Feedback | [07:08–08:36] |
| Restock | +4 weeks (before run-out) | Reorder | [08:00–08:36] |
| Photo/testimonial request | +5 weeks | Real social proof | [08:36] |
| Subscribe-and-save push | +8 weeks | Subscription | [08:36–09:10] |
| Success stories + strategy-call pitch (courses) | +2 days to +2 weeks | Ascension | [13:09–15:45] |

- The five purposes: reaffirm decision; answer vital questions; establish relationship and trust; turn one-time into repeat customer; encourage consumption. Delete any email that serves none (derived from [15-02 00:00–01:00]).
- "You don't have to do all these, but I like it"; after two weeks go weekly [15-02 04:28, 08:00](../lessons/15-02-1-2-welcome-sequences.md).
- **IF** low-ticket course with a next-step offer **THEN** re-sell and answer objections as in abandon cart [15-02 13:09–13:46](../lessons/15-02-1-2-welcome-sequences.md).
- **DON'T** use "member" language unless true [15-02 04:00, 05:38](../lessons/15-02-1-2-welcome-sequences.md).

**3c. Promo** [15-03](../lessons/15-03-1-3-promotional-sequences.md)

| Campaign | Emails | Send moments | Source |
|---|---|---|---|
| Holiday 72-hour | 5 | Launch → T-24h → final-day AM → final-day PM → T-3h | doc 1 |
| Black Friday week | 6 | T-6d preview → T-4d → T-3d (gratitude) → Thanksgiving → BF AM → BF PM | docs 2, 5 |
| 24-hour flash | 3 | Hour 0 → Hour 12 → Hour 22–23 | docs 3, 6 |

- State a real reason (holiday, event, surplus inventory) [15-03 01:07–02:11](../lessons/15-03-1-3-promotional-sequences.md); deadline in every email; final day 3+ sends: "I like three emails at least" [15-03 03:14–05:34](../lessons/15-03-1-3-promotional-sequences.md).
- **IF** multiple SKUs **THEN** show usual → sale price per SKU and combination prices; "if you had one SKU, you wouldn't do this" [15-03 02:43–03:46](../lessons/15-03-1-3-promotional-sequences.md).
- **IF** promoting a tool/course to a mixed audience **THEN** re-explain what it does in every email [15-03 11:38–13:24](../lessons/15-03-1-3-promotional-sequences.md).

**3d. Reorder (anchor = run-out date)** [15-04 02:21–05:52](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)
```
REORDER (anchor = run-out date)
-7d: praise consistency + what's happening now + "you're about a week from running out" + 3 reorder steps
-3d: "stopping too soon" + analogy + stories of delayed breakthroughs + reorder steps
-1d: consequence of a gap (be honest, not scary) + phone ordering
 0d: "last dose" + [x]% for 12 hours + midnight deadline
```
(derived template from [15-04 Prompts](../lessons/15-04-1-4-winback-and-reorder-campaigns.md))
- Run-out = order date + days of supply, adjusted for shipping (derived).
- Core message: "you're making progress; you'll make even more progress if you keep going; if you don't keep going, you'll lose progress." [15-04 00:34–01:14](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)
- **DON'T** over-scare: the day-1 sample "is a little bit aggressive scaring them" [15-04 04:30–05:05](../lessons/15-04-1-4-winback-and-reorder-campaigns.md).

**3e. Winback (anchor = last order or cancellation)** [15-04 05:52–14:38](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)
```
WINBACK (anchor = last order or cancellation)
 +45d / +14d: concern + what they may be noticing/doing + restart discount
 +47d / +16d: breakthrough month or system-pulling-you-back angle + discount still active
 +50d / +19d: higher discount ("I just authorized") + cost of missing it
 +52d / +21d: final discount + bonus + hard expiry
```
- First figure = consumable (30-day supply), second = subscription cancellation.
- Angles: "noticing something?" since stopping; "your body remembers"; "month two is when most breakthroughs happen" (adapt month to product; claims must be substantiated); subscription: old-habits / "what if" regret + active-user proof [15-04 06:27–13:39](../lessons/15-04-1-4-winback-and-reorder-campaigns.md).

### Step 4. Set the discount ladder
- **Input:** margin floor. **Output:** % per email + codes.

| Sequence | Course samples | Stefan's stated rule | Agent default (derived) |
|---|---|---|---|
| Abandon cart | V1 50% → 60%; V2 40% (d3) → 55% (d5); 15-05 demo 20% (d3) → 40% (d5–7) | Start 25–30%, escalate to 40–50% by margin; "$40 instead of $100 is still better usually than collecting $0" [15-01 v2 12:10–13:23](../lessons/15-01-1-1-abandon-cart-sequences.md) | Start 20–30%, one step up near the end, never below margin floor |
| Book-a-call | None | No discount [15-01 v2 23:06](../lessons/15-01-1-1-abandon-cart-sequences.md) | None |
| Promo | 50% holiday, 60% + free ship BF, 40% flash | Big savings with a reason [15-03 01:07](../lessons/15-03-1-3-promotional-sequences.md) | Margin-driven; one discount for the window |
| Reorder | 20% on run-out day only | Discount on last email [15-04 Steps](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) | Same |
| Winback | 20% → 40% (consumable); 25% × 3 mo → 50% + bonus (subscription) | "I'm lean[ing] for a discount for winbacks… I might even be more aggressive" [15-04 08:58–10:32](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) | 20% → 40% unless margin is thin; then smaller steps |

- Clarify the base: "50% off the normal retail price, not 50% off the price you already saw" [15-01 v2 01:09–01:44](../lessons/15-01-1-1-abandon-cart-sequences.md).
- "I've never offered X% before / never will again" only if literally true.

### Step 5. Request the outline
- Template components (derived from [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md)): type + length; discount placement; cross-sell slots by email number; source (URL or brief); approval gate; tone guardrails.
- Verbatim course prompts (replace product names, URLs, codes):
```
To start, let's do a 7 day abandon cart sequence for Unity Eye Serum. Let's introduce a 20% off discount on Day 3, and increase it to a 40% off Discount on Days 5-7. Can you please outline this sequence for me and then after I approve I'll have you write it.

https://tryopal.com/products/unity-eye-serum
```
```
Now let's do a new customer welcome sequence for Unity Eye Serum. Let's have it be 10 emails.

In email #3, let's introduce our Opaline Riche Creme as a great compliment to Unity Eye Serum, and give the customer a 20% off code they can use when ordering it.

https://tryopal.com/products/opaline

In email #7 let's introduce our Sacred Whipped Tallow and also offer a 20% off code.

https://tryopal.com/products/sacred

In email #10 let's give them a 20% off store wide coupon.

https://tryopal.com/

Please provide an outline of the sequence to me and once I've approved it, I'll have you write it.
```
```
Okay awesome job. Now I want to do a 3 Day sale for 4th of July for Opal Beauty. Let's make it site wide (all products), and they can save 30%. Please provide an outline.
```
```
This is the brief for a financial newsletter product. Please review and then come up with a 7 email abandon cart sequence outline. Once approved I'll have you write the sequence.
```
- **IF** no website **THEN** paste the brief or sales letter instead of a URL [15-05 SRT 22:00–23:12](../lessons/15-05-claude-project-for-writing-email-sequences.md).
- **IF** another holiday **THEN** "we'll do a Labor Day sequence, five emails, six emails, whatever" [15-03 06:17](../lessons/15-03-1-3-promotional-sequences.md).
- No dedicated prompts for reorder or winback are shown; use the same pattern with the 3d/3e timing table (derived).

### Step 6. Review the outline, then approve with fixes
- Check timing logic against real delivery; products complete; discount placement. Verbatim feedback examples [15-05 docs 4, 6](../lessons/15-05-claude-project-for-writing-email-sequences.md):
```
Okay nice. For Email 2 let's say "will be shipping soon if it hasn't already."

For email 3: let's make the code Rich20.

For Email 4 it seems like if it's going Day 5 a "one week checkin" doesn't make sense, it's too early. Let's move that to Email 5 (day 10) and move the rest of the emails back correspondingly.

Let's also do a new Email 4 that comes out on Day 5 - please provide suggestions.
```
```
Thanks but let's do 3 emails on Day 3. Also don't forget about our other two Skus as well:
```
```
Let's offer them an extra 25% off starting on Day 5.
```
- Approve with the tone guardrail (verbatim) [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md):
```
Okay great, let's go ahead and write it. One note for the tone with Email 1, and in general, let's make sure it is empathetic and supportive. We want to call out pain points, but we want to do it more like: "maybe you've experienced this." Or "Some of our customers share that ____" when talking about negatives. What we don't want to do is make it sound like we're assuming things about the prospect, ie: "Hey you hate how you look in the mirror huh"?"
```

### Step 7. Audit the written sequence

| Check | Course example | Source |
|---|---|---|
| Timing logic | One-week check-in cannot be day 5 | [15-05 SRT 10:53](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Content logic vs delivery | "Perfect partner" email on day 3 may land before the product | [15-05 SRT 14:09](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Pricing | "Pricing is off on this." | [15-05 SRT 20:16](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| All SKUs present | Missing two SKUs in the sale | [15-05 SRT 18:25](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Formatting / emojis | "so bizarre with the formatting and also the emojis" | [15-05 SRT 19:46](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Invented proof | Named customers, "15,000+ others", stats, "FDA-approved facilities", "clinically-proven" | [15-01 v2 02:16–03:16](../lessons/15-01-1-1-abandon-cart-sequences.md) |
| Fake pretexts | "I got a notification about you", "apology coupon", false 24-h expiry | [15-02 Agent use](../lessons/15-02-1-2-welcome-sequences.md) |
| Disease / drug claims | A1C, "come off insulin", glucose numbers | [15-04 Agent use](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |
| Invented jargon | "glucose doors slam shut": "the name is really bothering me" | [15-04 02:21–03:21](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |
| Spammy social lines | "they might think it's spam" | [15-03 12:42](../lessons/15-03-1-3-promotional-sequences.md) |
| Biz-op income claims | "$12,000 per month", named students | [15-01 Version 3](../lessons/15-01-1-1-abandon-cart-sequences.md) |

Then run [LLM output claim audit](../rubrics/llm-output-claim-audit.md). Replace unverified items with `[VERIFY: …]`.

## Reusable subject/hook patterns (structure only)
From the samples ([15-01 Prompts](../lessons/15-01-1-1-abandon-cart-sequences.md), [15-04 patterns](../lessons/15-04-1-4-winback-and-reorder-campaigns.md)):
```
[Name], you were so close            -> reconnect / curiosity
Quick story                           -> customer story email (real customer only)
48 Hours Left: [Offer] + [Credibility cue]
I just UPGRADED your discount         -> discount upgrade (only if true)
Let me guess. After [watching/reading], you thought "[objection]"
While you waited, they took action    -> peer pressure (book-a-call; real cases only)
Time for your reorder, [Name]         -> reorder
Month [N] is when most breakthroughs happen  -> winback (substantiate)
I'm worried you're falling back into old patterns  -> subscription winback
```

## Failure modes

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Sequence feels repetitive, low clicks | Same reason every email | One reason per email | [15-01 v2 03:51–13:56](../lessons/15-01-1-1-abandon-cart-sequences.md) |
| Margin erosion | Opened at deepest discount | Start low, escalate | [15-01 v2 12:10](../lessons/15-01-1-1-abandon-cart-sequences.md) |
| Unsubscribes / complaints (derived) | Presumptuous or shaming tone | Tone guardrail prompt | [15-05 doc 2](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Welcome emails arrive before product | Timing not tied to delivery | Time check-ins to delivery | [15-02 06:11–06:36](../lessons/15-02-1-2-welcome-sequences.md) |
| Reorder lands after run-out | Anchored to order date only | Anchor to run-out, −7 days | [15-04 02:21](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |
| Lost lapsed buyers | No winback discount | 20% → 40% ladder | [15-04 08:58–10:32](../lessons/15-04-1-4-winback-and-reorder-campaigns.md) |

## Where it's taught
- [15-01 Abandon cart](../lessons/15-01-1-1-abandon-cart-sequences.md): math [00:29–04:44]; reason map [04:44–16:56]; design [v2 00:01–13:56]; V1 [v2 00:33–14:33]; V2 [v2 14:33–19:38]; book-a-call [v2 19:38–26:46].
- [15-02 Welcome](../lessons/15-02-1-2-welcome-sequences.md): purposes [00:00–01:00]; supplement 15 emails [01:00–09:10]; $97 course [09:10–15:45]; coaching [15:45–16:56].
- [15-03 Promotional](../lessons/15-03-1-3-promotional-sequences.md): holiday [01:07–06:17]; Black Friday [06:17–09:00]; flash [09:00–10:38]; tool [10:38–14:25].
- [15-04 Winback and reorder](../lessons/15-04-1-4-winback-and-reorder-campaigns.md): reorder [01:14–05:52]; winback supplement [05:52–10:32]; subscription [10:32–14:38].
- [15-05 Claude project](../lessons/15-05-claude-project-for-writing-email-sequences.md): setup [SRT 00:00–01:36]; abandon cart demo [SRT 01:36–07:20]; welcome [SRT 07:20–16:15]; 4th of July [SRT 16:15–21:25]; financial newsletter [SRT 22:00–25:57].

## Cross-course notes
- Evolve and the shared Tether pages have no email-sequence framework (checked); RMBC is the KB's only source. Evolve [objection handling](../../../evolve/copywriting/concepts/objection-handling.md) supports the reason-per-email approach.
- The tone rule (no assumptions about the reader) matches 14-03's upsell feedback; see [upsell flow build](upsell-flow-build.md).

## Related
[post-purchase and retention playbook](../playbooks/post-purchase-and-retention.md) · [upsell formula](../concepts/upsell-formula.md) · [benchmarks](../libraries/benchmarks.md) · [rules](../libraries/rules.md)
