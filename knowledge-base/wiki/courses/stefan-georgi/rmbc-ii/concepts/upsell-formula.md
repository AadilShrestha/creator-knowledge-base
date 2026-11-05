---
title: "Upsell formula (reaffirm → new or expanded problem → irresistible offer)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
tags: [upsells, post-purchase, stock-up, cross-sell, more-of-the-same, new-problem, expanded-problem, aov]
updated: 2026-11-02
---

# Upsell formula
> Upsell #1 is three beats in a fixed order: reaffirm the purchase, name a new or expanded problem (or the run-out risk), then the irresistible offer; first decide what you are really selling (better/faster/easier results, savings, holism) and whether the buyer gets more of the same or a complementary product.

## 🤖 Agent use
- **Use when:** planning or writing a post-purchase flow (pop-up, upsell 1, upsells 2+, downsell, confirmation page); choosing what upsell 1 sells; auditing a competitor's upsell flow.
- **Inputs → outputs:** front-end product and what the buyer just bought, purchase model (one-time vs subscription), consumable vs durable vs info, price ladder, AOV/COGS/CPA, verified mechanism and proof → an upsell plan (type, order, format, price) and a beat outline for each upsell. Scripts: [upsell-flow-build](../frameworks/upsell-flow-build.md).
- **Rules:**
  - **DO** write upsell #1 in this order: "Reaffirmation first, new or expanded problem second, irresistible offer third." [14-01 v2 00:34](../lessons/14-01-upsells-overview.md); [14-02 v4 04:59](../lessons/14-02-upsells-case-studies.md)
  - **DO** open by telling the buyer where they are and that the order is being prepared ("where am I in the process?", credited to Jay DeBolt). [14-02 v6 02:17–02:48](../lessons/14-02-upsells-case-studies.md)
  - **DO** decide what you are selling before writing: better, faster, easier (done for you / automated / done with you), expanded results, savings, or holism. [14-01 v2 11:22](../lessons/14-01-upsells-overview.md)
  - **IF** the product is a one-time consumable **THEN** default upsell 1 to more of the same (stock-up at a deeper per-unit saving). "Almost all of these did more of the same, which is interesting because it works." [14-02 v4 22:27](../lessons/14-02-upsells-case-studies.md)
  - **IF** the buyer is on a subscription **THEN** don't sell more of the same; go to a new problem. "I want you on subscription." [14-01 v2 09:47](../lessons/14-01-upsells-overview.md)
  - **IF** the product is a big durable purchase (a $2,000 sauna) **THEN** sell complementary optimisation, not a second unit. [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md)
  - **IF** the front end is info, a book or coaching **THEN** sell done-for-you, templates, implementation or faster/easier results, not more of the same. [14-02 v5 06:56; v6 27:25](../lessons/14-02-upsells-case-studies.md)
  - **DON'T** blame the front-end product to justify the next offer ("we left out two really important ingredients" makes buyers ask why it wasn't included). The product "is God's gift"; the new problem is time, consistency or implementation. [14-02 v6 20:54–22:44](../lessons/14-02-upsells-case-studies.md)
  - **DON'T** repeat 1,000 words of reaffirmation on upsells 2-4; get more direct. [14-02 v6 34:03–36:49](../lessons/14-02-upsells-case-studies.md)
  - **DON'T** assume the buyer took the previous upsell when writing upsell 2. [14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)
  - **DON'T** use invented scarcity ("out of stock 9 times", "3-6 months to restock", "friends and family discount") or fabricated proof from the swipes. Use real constraints or none. [14-02 Claims check](../lessons/14-02-upsells-case-studies.md)
  - **DO** show per-unit saving and what each unit replaces; Dr. Clean relies on "people doing the math for themselves in their head". [14-02 v1 06:59](../lessons/14-02-upsells-case-studies.md)
  - **DO** test the number, order and price of upsells, and measure revenue per order across bump + upsells. [14-02 v1 16:55](../lessons/14-02-upsells-case-studies.md); [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)
- **See also:** [upsell-flow-build](../frameworks/upsell-flow-build.md) · [funnel-economics](funnel-economics.md) · [congruence](congruence.md) · [post-purchase-and-retention](../playbooks/post-purchase-and-retention.md) · [templates](../libraries/templates.md) · [prompts](../libraries/prompts.md) · [compliance-red-flags](compliance-red-flags.md)

## Definition
"Journey two" starts the moment the buyer pays: "It's never going to be easier than it is right then and there." [14-01 v1 01:46](../lessons/14-01-upsells-overview.md) The upsell formula is the doc's "Upsell #1 Big Idea": reaffirm → new or expanded problem → irresistible offer. Verbatim baseline script:

```text
"Hey you just got this product, great job. But what if you're getting results, you run out, and the product is either out of stock or costs a lot more money?"
```
Source: [14-01 doc; v2 00:34–02:01](../lessons/14-01-upsells-overview.md). Stefan on that baseline: "It works, but it's not always the best." [14-01 v2 02:01](../lessons/14-01-upsells-overview.md)

### The three problem types
| Type | Meaning | Bridge pattern | Source |
|---|---|---|---|
| More of the same | No new problem; protect the result against running out or a price rise | "What if you're getting results, you run out…" | [14-01 v2 06:09–06:43](../lessons/14-01-upsells-overview.md) |
| New problem | Solving the first problem creates a fresh one | "Now you know how to [result]. But how do you [keep/protect it]?" | [14-01 v2 02:53–06:09](../lessons/14-01-upsells-overview.md) |
| Expanded problem | Adjacent pain, "expanding outward" | "Now you've fixed your knee pain. What about your back pain?" | [14-01 v2 06:43–07:47](../lessons/14-01-upsells-overview.md) |

### What are we selling (verbatim from the doc)
```text
Results.
Better Results
Faster Results
Easier Results (Done For You, Automated, Done With You)
Expanded Results (Solving The New Problem or a Complementary Problem)

Savings:
Save even more money today (and get even better results).

Holism:
You just solved part of the problem, now solve the entire problem (or at least another big, urgent pain point).
```
Source: [14-01 v2 11:22](../lessons/14-01-upsells-overview.md).

### Stock-up vs complementary: decision table
| Front-end situation | Upsell 1 | Later upsells / cross-sells | Source |
|---|---|---|---|
| One-time consumable (supplement, cleaner, skincare) | More of the same (stock-up pack, deeper per-unit price) | Complementary/expanded-problem products | [14-01 v2 09:15](../lessons/14-01-upsells-overview.md); [14-02 v4 22:27](../lessons/14-02-upsells-case-studies.md) |
| Subscription | New problem (not more supply) | Expanded problem | [14-01 v2 09:47](../lessons/14-01-upsells-overview.md) |
| Durable, high price (sauna) | Complementary optimisation | Expanded problem | [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md) |
| Device | Improved version ($99 hearing aid → "10x better" $149, "Upgrade your order") | Complementary | [14-01 v2 13:36](../lessons/14-01-upsells-overview.md) |
| Info / book / coaching | Done-for-you, templates, implementation (easier/faster) | Downsell without the call; accountability/community | [14-01 v2 14:10–17:16](../lessons/14-01-upsells-overview.md); [14-02 v5 06:29–13:49](../lessons/14-02-upsells-case-studies.md) |

Later-upsell menu from the doc: complementary product or service, improved version or done-for-you/with-you, community ("join this membership community… You won't be alone"). [14-01 v2 16:19–17:16](../lessons/14-01-upsells-overview.md)

## Why it matters
- AOV is the cheapest lever when day-0 margin is negative: $100 CAC with $80 AOV loses $40 per customer; $160 AOV makes +$20 (instructor's worked example). [14-01 v1 04:27–08:25](../lessons/14-01-upsells-overview.md) See [funnel-economics](funnel-economics.md).
- Upsell 1 "accounts for 80% of your upsell AOV"; aim for a "20% - 45% conversion rate (a lot of this depends on the price)"; "AOV matters more than conversion rate on upsells" (Copy Accelerator PDF quoted in 14-02; instructor claim). [14-02, section D](../lessons/14-02-upsells-case-studies.md)

## How to use (steps)
1. Compute first-order margin (AOV − CAC − COGS). [14-01 v1 11:14](../lessons/14-01-upsells-overview.md)
2. Classify the front end (consumable, subscription, durable, device, info) and pick upsell 1 type from the table.
3. Pick the "what are we selling" promise (results, savings, holism).
4. Pick the format: short branded page (Dr. Clean, Happy Mammoth) or 10-15 minute video (DR supplement funnels; "even 18 minutes"). [14-02 v4 05:03](../lessons/14-02-upsells-case-studies.md) Balance "branded congruent experience versus get that AOV up". [14-02 v1 10:15–12:51](../lessons/14-02-upsells-case-studies.md)
5. Outline upsell 1 with the beats below; mark every fact `[VERIFY: …]`.
6. Plan upsells 2+ shorter and more direct; write a downsell if declining (drop a component, lower price). [14-02 v5 11:32–12:12](../lessons/14-02-upsells-case-studies.md)
7. Test count, order, price; measure revenue per order with bump and upsells together.

### Stock-up video upsell beats (derived from Emma, Synocell and Stefan's FitSpresso edit in 14-02)
| # | Beat | Compliant note |
|---|---|---|
| 1 | Header: order not complete, don't hit Back | Keep factual; no false double-billing threat unless true |
| 2 | Congratulate; you're in the right place; watch to the end | — |
| 3 | Reaffirm and future-pace | Typical, not guaranteed, results |
| 4 | Real customer stories | Real reviews only, with permission |
| 5 | Turn: the result depends on consistent use | — |
| 6 | Re-educate on the mechanism: why it takes time | Structure/function wording; `[VERIFY: mechanism]` |
| 7 | Consequence of stopping/running out | No disease or fear claims; true stock constraints only |
| 8 | Named pack + what to expect month by month | Expectations from real data or bracketed |
| 9 | Per-unit and total price anchor, per-day comparison | Real reference prices only |
| 10 | Guarantee | Actual terms |
| 11 | Urgency: one-time, this page only | Only if actually enforced |
| 12 | CTA + decline line | Avoid confirmshaming |
Source of beat order: [14-02 section B; v4 05:03–20:47](../lessons/14-02-upsells-case-studies.md). Length 6-16 minutes per the Claude Project instructions. [14-03 00:00–00:29](../lessons/14-03-claude-projects-for-upsells.md)

## Examples (structure only; claims not reusable)
| Case | Type and format | What to take | Source |
|---|---|---|---|
| Dr. Clean tablets | Pop-up + upsell 1 stock-up ("Never Run Out…"), upsells 2-4 dishwasher/toilet/washer | Templated expanded-problem pages; add per-bottle savings | [14-02 v1 05:47–18:44](../lessons/14-02-upsells-case-studies.md) |
| Happy Mammoth | Shopify post-purchase: 2 extra bottles $20 off, then cross-sell | Fixed quantity; mobile-first; stock-out testimonial (claims flagged) | [14-02 v3 01:10–08:13](../lessons/14-02-upsells-case-studies.md) |
| Emma / Synocell | 9-12 min video stock-up; packs visible under video | Re-educate on mechanism, consequence, stock-up deal. "It's nothing novel here. It's what everyone does." | [14-02 v4 05:03–20:47](../lessons/14-02-upsells-case-studies.md) |
| Capital Syndicate | Video OTO1 done-for-you $297 → downsell $147 → OTO3 accountability | Downsell drops the call; continuity revealed late ("sneaky") | [14-02 v5 06:29–13:49](../lessons/14-02-upsells-case-studies.md) |
| Sabri Suby "Sell Like Crazy" | 5,000+ word video after a book | Reaffirm long, doubt, "the problem is you", founder struggle, hype each component | [14-02 v6 08:33–33:03](../lessons/14-02-upsells-case-studies.md) |
| Unity Eye Serum / Lumessa / Airbnb call | Claude Project runs: more of the same, cross-sell, call booking | Steer with specific feedback; sell the call, not the price | [14-03 01:01–10:44](../lessons/14-03-claude-projects-for-upsells.md) |

## Common mistakes
- Selling "more stuff" instead of results, savings or holism. [14-01 v2 11:22](../lessons/14-01-upsells-overview.md)
- More of the same on a subscription (kills the subscription) or a durable product. [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md)
- New "discovery" story on a more-of-the-same upsell; Stefan cut it from Claude's FitSpresso draft. [14-02 Rewrites](../lessons/14-02-upsells-case-studies.md)
- Insulting logic or shaming the viewer ("most people don't realize your eyes are just one part of your face"). [14-03 02:38–04:11](../lessons/14-03-claude-projects-for-upsells.md)
- Shipping a template with placeholder text live (Happy Mammoth product blurb). [14-02 v3 01:40](../lessons/14-02-upsells-case-studies.md)
- Hidden continuity revealed late (Capital Syndicate $97). Disclose at the offer. [14-02 v5 09:48–10:49](../lessons/14-02-upsells-case-studies.md); [11-02 21:35](../lessons/11-02-checkouts-walkthrough-part-2.md)
- Confirmshaming decline links ("I'm in no rush to get results"). [14-02 v5 12:27](../lessons/14-02-upsells-case-studies.md) (derived compliance note: dark pattern; avoid)
- Adding an order bump that cannibalises upsell 1. [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)

## Where it's taught
- [14-01 Upsells overview](../lessons/14-01-upsells-overview.md): economics [v1 04:27–11:14]; big idea [v2 00:34–02:53]; problem types [v2 02:53–08:45]; when more of the same [v2 09:15–11:22]; what are we selling [v2 11:22–17:16].
- [14-02 Upsells case studies](../lessons/14-02-upsells-case-studies.md): Dr. Clean [v1]; David [v2]; Happy Mammoth [v3]; Emma/Synocell [v4]; Capital Syndicate [v5]; Sell Like Crazy and Q&A [v6]; Claims check.
- [14-03 Claude Projects for upsells](../lessons/14-03-claude-projects-for-upsells.md): project setup [00:00–00:59]; three runs [01:01–10:44].
- [11-02 Checkouts part 2](../lessons/11-02-checkouts-walkthrough-part-2.md): bump vs upsell math [16:31–19:32].
- [13-01 Hidden factors](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md): factors 9 and 13 shape the upsell plan [27:51; 36:49].

## Cross-course notes
- **Evolve** (Copywriting, Start Here) has no upsell-script framework in the KB (checked concept and framework lists). RMBC is the source for post-purchase copy.
- **Tether Lab:** [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) covers pack ladders and anchoring used in stock-up offers; the RMBC per-unit-saving rule is consistent with it.
- **Within RMBC:** 14-02 (video) and the 14-03 project (6-16 min) favour long video upsells for DR funnels, while Dr. Clean, David and Happy Mammoth show short branded pages. **Agent default:** short page for branded e-com with PDP funnels; long video for VSL-sourced DR traffic; test both. [14-02 v4 14:42; v1 10:15](../lessons/14-02-upsells-case-studies.md)

## Related
[funnel-economics](funnel-economics.md) · [congruence](congruence.md) · [funnel-selection-matrix](funnel-selection-matrix.md) · [upsell-flow-build](../frameworks/upsell-flow-build.md) · [email-sequences](../frameworks/email-sequences.md) · [post-purchase-and-retention](../playbooks/post-purchase-and-retention.md) · [compliance-red-flags](compliance-red-flags.md)
