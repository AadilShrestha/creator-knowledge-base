---
title: "Upsell Flow Build (economics → offer type → format → script with Claude → review → test)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-01-upsells-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
tags: [upsells, post-purchase, aov, stock-up, cross-sell, downsell, video-upsell, claude-project, prompts]
updated: 2026-11-02
---

# Upsell Flow Build
> Prove the upsell is needed with CAC/AOV/COGS math, pick upsell #1's offer type from the buyer's situation (consumable, subscription, durable, info), choose short page vs 6–16 minute video, draft the script in a Claude Project modeled on swipes, edit for funnel logic, tone and invented proof, then test the flow on revenue per buyer.

## 🤖 Agent use
- **Use when:** planning a post-purchase sequence (pop-up, upsell 1, upsells 2+, downsell, confirmation page); writing an upsell script or page; auditing a competitor's flow.
- **Inputs → outputs:** front-end product and price, COGS, CAC/CPA, one-time vs subscription, consumable vs durable vs info, real inventory constraints, guarantee, real customer language, 3–5 upsell swipes, our [unified research document](../concepts/unified-research-document.md) or [Brief 2.0](../concepts/brief-2-0.md) → margin check → flow map (step, offer type, format, price tiers) → per-step script/page copy → claim-audited draft → test plan.
- **Rules:**
  - **DO** write upsell #1 as: "Reaffirmation first, new or expanded problem second, irresistible offer third." [14-01 v2 00:34](../lessons/14-01-upsells-overview.md)
  - **DO** sell results (better, faster, easier, expanded), savings or holism, not "more stuff". [14-01 v2 11:22](../lessons/14-01-upsells-overview.md)
  - **DO** open by telling buyers where they are: order being prepared, right place, don't hit Back [14-02 v6 02:17, 11:19](../lessons/14-02-upsells-case-studies.md).
  - **DON'T** let upsell 2+ assume the buyer took upsell 1: "People will see this second upsell regardless of if they took #1 or not." [14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)
  - **DON'T** blame the front-end product; the new problem is time, effort, consistency or implementation: "this thing is God's gift… that's not the problem." [14-02 v6 20:54–22:44](../lessons/14-02-upsells-case-studies.md)
  - **DON'T** sell more of the same to a subscriber or a second durable item: "I want you on subscription." [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md)
  - **DON'T** publish Claude's invented testimonials, studies, percentages, founder stories or scarcity counts; every course output has them [14-03 Claims check](../lessons/14-03-claude-projects-for-upsells.md).
  - **DO** read and edit every draft: "It's doing 99% of the work for you, so just use your brain." [14-03 10:44](../lessons/14-03-claude-projects-for-upsells.md)
  - **IF** adding an order bump **THEN** test it against the upsell on total revenue per order [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md).
- **See also:** [upsell formula](../concepts/upsell-formula.md) · [funnel economics](../concepts/funnel-economics.md) · [checkout optimization](checkout-optimization.md) · [email sequences](email-sequences.md) · [claude project recipe](../concepts/claude-project-recipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [prompts library](../libraries/prompts.md) · [templates library](../libraries/templates.md) · shared [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md)

## Procedure

### Step 1. Margin check
- **Input:** CAC/CPA, AOV, COGS, rebill/LTV evidence. **Output:** net per customer and whether upsells are required to scale.
```text
First purchase:  CAC/CPA = ___   AOV (revenue) = ___   COGS = ___   Net = AOV - CAC - COGS = ___
With upsells:    CAC/CPA = ___   AOV = ___            COGS = ___   Net = ___
Spend the gain:  CAC/CPA = ___ (raised)               AOV = ___   COGS = ___   Net = ___ (target ~0 if later purchases/rebills pay back)
```
(worksheet derived from the 14-01 doc [14-01 v1 04:27–11:14](../lessons/14-01-upsells-overview.md))
- Stefan's example: CAC $100, AOV $80, COGS $20 → −$40; AOV $160, COGS $40 → +$20; then raise CAC to $120 → $0 but more customers [14-01 v1 05:04–08:58](../lessons/14-01-upsells-overview.md).
- **IF** net is negative and cash is limited **THEN** raise AOV before scaling spend: upsells are "one of the most obvious things you could do" [14-01 v1 11:14](../lessons/14-01-upsells-overview.md).
- **IF** strong rebills/LTV exist **THEN** paying up to break-even CPA is "a totally fine model if you know what you're doing" [14-01 v1 10:43](../lessons/14-01-upsells-overview.md).
- Upside named in 16-03: raising upsell take rate from 20% to 40% could add "$15 to $25, maybe much more" per customer (instructor claim) [16-03 25:03–26:52](../lessons/16-03-funnel-economics-with-spg.md). Full model: [funnel economics](../concepts/funnel-economics.md).

### Step 2. Pick upsell #1's offer type
- **Input:** buyer situation. **Output:** one offer type + the bridge line.

| IF the buyer just bought | THEN upsell #1 | Bridge (pattern) | Source |
|---|---|---|---|
| Consumable, one-time (supplement, cleaner, skincare) | More of the same: stock-up pack at a deeper discount | "what if you're getting results, you run out, and the product is either out of stock or costs a lot more money?" | [14-01 v2 01:20, 09:15](../lessons/14-01-upsells-overview.md); "Almost all of these did more of the same… it works" [14-02 v4 22:27](../lessons/14-02-upsells-case-studies.md) |
| Subscription | New problem (not more of the same) | "Now you've [result]. What about [new problem]?" | [14-01 v2 09:47](../lessons/14-01-upsells-overview.md) |
| Big durable item ($2,000 sauna) | Complementary optimisation (cold plunge, biohacking) | Expanded problem | [14-01 v2 09:47–10:52](../lessons/14-01-upsells-overview.md) |
| Device | Improved version ("Upgrade your order": $99 → 10x better $149) | Better results | [14-01 v2 13:36](../lessons/14-01-upsells-overview.md) |
| Info product / book / course | Done-for-you, templates, implementation, call; never more of the same | "the problem is you" (time, consistency) | [14-02 v5 06:56, v6 27:25](../lessons/14-02-upsells-case-studies.md) |
| Low-ticket info → coaching | Book-a-call upsell; sell the call, not the price | Personalised plan | [14-03 08:17–09:07](../lessons/14-03-claude-projects-for-upsells.md) |

- Expanded-problem bridge examples (structure only; claims not reusable): knee pain → back pain; eyes → rest of face; dishwasher, toilet, washer after an all-purpose cleaner [14-01 v2 06:43–07:47](../lessons/14-01-upsells-overview.md), [14-02 v1 11:52–18:44](../lessons/14-02-upsells-case-studies.md).
- Stock-up sizing: buyer took 3 bottles → offer 6 more "usually works better than selling them 3 more" [14-02 Steps D](../lessons/14-02-upsells-case-studies.md).

### Step 3. Map the rest of the flow
- **Output:** ordered list: pop-up → U1 → U2… → downsell → confirmation.
- Later steps: complementary product for the expanded problem; improved / done-for-you / done-with-you; community ("You won't be alone") [14-01 v2 16:19–17:16](../lessons/14-01-upsells-overview.md).
- Downsell on decline: same core, smaller package, lower price (Capital Syndicate $297 → $147, coaching call removed) [14-02 v5](../lessons/14-02-upsells-case-studies.md).
- Confirmation page: let buyers add quantity (Happy Mammoth) [14-02 v3 08:13](../lessons/14-02-upsells-case-studies.md); Dr. Clean used notification opt-in + an affiliate "life hacks" page [14-02 v1 20:09–22:20](../lessons/14-02-upsells-case-studies.md) (brand-fit check required).
- **How many upsells?** "Test it. Find out." [14-02 v1 16:55](../lessons/14-02-upsells-case-studies.md). Shopify post-purchase apps cap at about two or three [14-02 v3 00:33–01:10](../lessons/14-02-upsells-case-studies.md). Order is a test variable (Dr. Clean toilet vs dishwasher) [14-02 v1 15:17](../lessons/14-02-upsells-case-studies.md).
- **IF** a later upsell can be reached after a "no" **THEN** its opener must not reference an accepted earlier offer (Step 6 check).

### Step 4. Choose format and price
| IF | THEN format | Source |
|---|---|---|
| Direct-response funnel (VSL/advertorial, supplement) | 10–15 min video (even 18), pack options visible under it, "WAIT! Your order is not complete" header | [14-02 v4 05:03, 13:22](../lessons/14-02-upsells-case-studies.md) |
| Branded Shopify store | Short on-brand page or post-purchase app offer; balance "branded congruent experience versus get that AOV up" | [14-02 v1 10:15–12:51, v3](../lessons/14-02-upsells-case-studies.md) |
| Big price jump (low-ticket book → $297) | Long script (Sell Like Crazy ~5,300 words) | [14-02 v6 08:33–09:39, 31:10–33:03](../lessons/14-02-upsells-case-studies.md) |
| Upsell 2+ | Shorter and more direct; reaffirm briefly ("you really mean business") | [14-02 v6 34:03–36:49](../lessons/14-02-upsells-case-studies.md) |

- Copy Accelerator PDF (attributed in 14-02): work order product → price (most people price upsells too low; test on U1) → format ("formatting is probably more important than copy"; video "11-15 minutes"); U1 "accounts for 80% of your upsell AOV"; aim for "20% - 45% conversion rate"; "AOV matters more than conversion rate on upsells" (instructor-side claims) [14-02 Steps D](../lessons/14-02-upsells-case-studies.md). Benchmarks: [benchmarks library](../libraries/benchmarks.md).
- Put per-unit price and what each unit replaces on the page; Dr. Clean relied on "people doing the math for themselves in their head" [14-02 v1 06:59](../lessons/14-02-upsells-case-studies.md).

### Step 5. Draft with Claude
**Path A: standing Claude Project (6–16 min video scripts)** [14-03](../lessons/14-03-claude-projects-for-upsells.md)
1. Create the Project "Claude Upsell Generator (Longer Scripts)"; paste instructions (verbatim) [14-03 00:17](../lessons/14-03-claude-projects-for-upsells.md):
```text
Claude Upsell Generator (Longer Scripts)

Your job is to generate upsell video scripts. They will typically be between 6 minutes and 16 minutes in length. The documents in your knowledge base includes transcripts from several upsell videos which we can model off while writing new upsells. What you'll want to do is analyze the structure of the various upsell examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new upsells.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current upsell project is.

One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```
2. Load 3–5 swipes as PDFs (course used Emma, Synocell, a more-of-the-same sample, Sabri Suby, Stem Cell Restore) [14-03 00:29–00:59](../lessons/14-03-claude-projects-for-upsells.md). Add our own winners; add the unified research doc or brief so proof comes from research [14-03 03:09–04:11](../lessons/14-03-claude-projects-for-upsells.md).
3. Run per upsell. More of the same [14-03 01:01](../lessons/14-03-claude-projects-for-upsells.md):
```text
Please do a 10 minute upsell script for someone who just bought unity eye serum, selling them more of the same.
https://tryopal.com/products/unity-eye-serum
```
   Steer toward a named swipe:
```text
Thanks. And going back to the Unity Eye Serum - 10 Minute Upsell Script. I liked it, but let's model more heavily off of the Emma and Synocell structure.
```
   Cross-sell as upsell #2 [14-03 02:01](../lessons/14-03-claude-projects-for-upsells.md):
```text
Awesome, good job! Now let's do an 8 minute cross-sell (it will be upsell #2) selling this product:
https://tryopal.com/products/lumessa
```
   Call-booking upsell for info product (brief attached) [14-03 08:36](../lessons/14-03-claude-projects-for-upsells.md):
```text
Here's information for a product we sell as a front end. Right now we're going to sell it as the first upsell, to people who just took a $27 info product called: "Permissionless Income" that teaches people 27 ways to generate extra income. It was from Mack as well. Now we're going to sell them on this concept and to book a call. Let's make the VSL Script 10-15 minutes long.
```
   Replace product names, links and offer details with ours.
- **IF** physical product **THEN** give the landing-page link; **IF** info product **THEN** attach the brief [14-03 01:01, 05:12](../lessons/14-03-claude-projects-for-upsells.md).
- **IF** we want an outline first **THEN** ask for the outline, then the script across "continue" turns [14-03 06:31](../lessons/14-03-claude-projects-for-upsells.md).
- **IF** short on-page upsells are needed **THEN** build a second Project from short-page copies (Dr. Clean / Happy Mammoth style) [14-03 01:31–02:01](../lessons/14-03-claude-projects-for-upsells.md).

**Path B: one-off chat from a single swipe** [14-02 Prompts](../lessons/14-02-upsells-case-studies.md)
1. Format a raw swipe transcript:
```text
Here's a video script, please format it with a break in between each line. You can do it over multiple outputs as needed:

[paste raw transcript]
```
2. Outline the swipe (attach it):
```text
Here is a video script for an upsell in the health space.I want you to analyze it and then create an outline for the structure of the script.
```
3. Write section by section (attach our product inputs):
```text
Perfect thank you. Now we're going to be writing a new upsell script a different product. I want you to closely model off the Rejuvaknee Upsell as far as structure and length. Also in style and tone. We're going to do this through multiple outputs which means you can go section-by-section and when you write each section, just ask me to tell you to continue. Do not try to condense things, good video scripts are often quite long. Here's the information you should need to do this:

[attach: Fitspresso Inputs for Upsell (pdf)]

Please get started with the very first section. Whenever you run out of space just ask me to continue and I'll tell you to keep going.
```
4. Between sections: `yes please continue`
5. **IF** Claude invents a "new discovery" story for a more-of-the-same offer **THEN**:
```text
So here's where you need to be a little bit more creative, since in this case we're selling more Fitspresso. So we don't need to position and then intro a new product, since what we're doing here is selling them "more of the same."
```
6. Optional expectations timeline (only with substantiated outcomes; else describe routine, not results):
```text
This is great. One thing I'd like to add is maybe a section where it's like "here's what you can expect during your journey with Fitspresso: Your First Week, Your First Month, Your Second Month, Your Third Month, Your Fourth Month, Your Fifth Month, and then Your Sixth Month. - and for each of those we paint a picture of their transformation improving and life getting better and better.
```

**Stock-up video blueprint** (derived in [14-02 Steps B](../lessons/14-02-upsells-case-studies.md); give it to Claude as the outline if no swipe): header (WAIT, don't hit Back) → greeting + congratulation + "right place" → reaffirm and future-pace → real customer proof → the turn ("most important decision is made on this page") → re-educate on the mechanism (why it takes time; UMP) → consequence of running out (only if true) → named pack + month-by-month expectations → price anchor and per-unit price → guarantee → true urgency only → CTA + decline line.

### Step 6. Review the draft (quote the line, say why, ask for a revision)
- **Input:** Claude draft. **Output:** edited script + feedback turns.

| Check | Failure seen in the course | Feedback prompt (verbatim) | Source |
|---|---|---|---|
| Funnel logic | U2 opener assumed U1 was bought | "We shouldn't assume they bought the first upsell. People will see this second upsell regardless of if they took #1 or not." | [14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md) |
| Insulting logic | "What most people don't realize is that your eyes are just one part of your face…" | "This doesn't make sense. I'm pretty sure most people do realize that their eyes are just one part of their face." | [14-03 03:09](../lessons/14-03-claude-projects-for-upsells.md) |
| Tone | Shaming contrast ("your eyes will look good but the rest of you will look old!") | Feedback 3 below | [14-03 03:41–04:11](../lessons/14-03-claude-projects-for-upsells.md) |
| Offer focus | Call upsell drifted into program pricing | "instead of talking about the price, you should really be selling them on booking a call" (spoken) | [14-03 08:17–09:07](../lessons/14-03-claude-projects-for-upsells.md) |
| Product blame | Upsell implies the front end was incomplete ("we left out two ingredients") | Rewrite so the new problem is human nature/implementation | [14-02 v6 20:54–22:44](../lessons/14-02-upsells-case-studies.md) |
| Invented proof | Named testimonials, "2019 study", "300%", founder income | Strip; replace with `[VERIFY: …]` or real data | [14-03 Claims check](../lessons/14-03-claude-projects-for-upsells.md) |

Feedback 3 (verbatim) [14-03 doc 3.1](../lessons/14-03-claude-projects-for-upsells.md):
```text
Thanks. Now one more thing, I'd like to see a version of this where the tone is a little more empathetic. Instead of making them feel like shit "your eyes will look good but the rest of you will look old!" let's show more empathy. "A lot of women end up realizing that the one downside is that it highlights other areas of their face that don't look so young. For some of them it might be fine lines around their mouth, or rough uneven texture on their cheeks." Things like that so we're still being persuasive but not calling out any specific woman who watches and assuming things about her.
```
- Then run [LLM output claim audit](../rubrics/llm-output-claim-audit.md) and [compliance red flags](../concepts/compliance-red-flags.md): scarcity ("inventory plummeted", "3-6 months to restock", "only 174 bottles"), drug comparisons (FitSpresso vs injectables), outcome guarantees ("virtually GUARANTEE SUCCESS"), decline-link confirmshaming are course-observed and not reusable [14-02 Claims check, v5 12:27](../lessons/14-02-upsells-case-studies.md).
- Check app placeholder text before launch (Happy Mammoth shipped "Include a short, benefit-driven description…") [14-02 v3 01:40](../lessons/14-02-upsells-case-studies.md).

### Step 7. Test
- Metric: revenue per buyer across the whole post-purchase flow, not take rate alone [14-01 Steps 5](../lessons/14-01-upsells-overview.md); bump-vs-upsell gate in [checkout optimization](checkout-optimization.md#step-6-order-bump-decision-math-gate).
- Test queue (derived from 14-01/14-02): U1 price; U1 offer type (stock-up vs improved vs complement); format (short page vs video); number and order of upsells; per-unit comparison block; "gross them out" problem section on expanded-problem pages [14-02 v1 12:51, 18:44](../lessons/14-02-upsells-case-studies.md).
- CRO places upsells first in test priority: post-purchase upsells "cannot reduce front-end conversion" (guest claim, Ethan Bence) [16-01 21:15](../lessons/16-01-cro-with-4080-marketing.md). Run rules: [cro-testing](cro-testing.md).
- Audit competitors: buy through the flow, save link + screenshot + copy for every page (post-purchase pages cannot be reopened) [14-02 v1 10:15–11:02](../lessons/14-02-upsells-case-studies.md).

## Failure modes

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Subscription churn after upsell | Sold more of the same to a subscriber | New problem instead | [14-01 v2 09:47](../lessons/14-01-upsells-overview.md) |
| Low take on info upsell | Sold "more" info | Done-for-you / faster / easier | [14-02 v5 06:56](../lessons/14-02-upsells-case-studies.md) |
| Buyer confusion, back-button exits | No reorientation | "Your order is being prepared… you're in the right place" opener | [14-02 v6 02:17](../lessons/14-02-upsells-case-studies.md) |
| Refund requests / distrust (derived) | Upsell implies front end was incomplete | Keep product "God's gift"; problem is implementation | [14-02 v6 20:54](../lessons/14-02-upsells-case-studies.md) |
| Stock-up converts "decently, even though it's sort of weak" | No per-unit comparison | Show saving vs alternative | [14-02 v1 08:25–09:34](../lessons/14-02-upsells-case-studies.md) |
| AOV up, total revenue down | Order bump cannibalizes U1 | Bump on/off test | [11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md) |
| Draft full of fake proof | Claude fills swipe slots | Step 6 audit | [14-03 Claims check](../lessons/14-03-claude-projects-for-upsells.md) |

## Where it's taught
- [14-01 Upsells overview](../lessons/14-01-upsells-overview.md): journey two [v1 00:00–02:22]; CAC/AOV/COGS [v1 04:27–11:14]; upsell #1 big idea [v2 00:34–02:53]; new vs expanded [v2 02:53–08:45]; when more of the same [v2 09:15–11:22]; what we sell [v2 11:22–17:16].
- [14-02 Upsells case studies](../lessons/14-02-upsells-case-studies.md): Dr. Clean [v1 05:47–22:56]; David [v2]; Happy Mammoth [v3]; Emma/Synocell [v4]; Capital Syndicate [v5]; Sell Like Crazy + Claude process [v6].
- [14-03 Claude Projects for upsells](../lessons/14-03-claude-projects-for-upsells.md): setup [00:00–00:59]; Unity Eye Serum [01:01–02:01]; Lumessa feedback [02:01–04:11]; call upsell [04:11–10:44].
- [11-02 Checkouts part 2](../lessons/11-02-checkouts-walkthrough-part-2.md): bump vs upsell math [16:31–19:32].
- [16-03 Funnel economics](../lessons/16-03-funnel-economics-with-spg.md): AOV levers [25:03–26:52].

## Cross-course notes
- Evolve has no upsell framework ([14-03 Related](../lessons/14-03-claude-projects-for-upsells.md)); Evolve's [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md) agrees with the "AI drafts, human edits" stance.
- Shared Tether [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) covers bundle anchoring; RMBC adds the reaffirm → problem → offer order and the buyer-situation table.

## Related
[upsell formula](../concepts/upsell-formula.md) · [congruence](../concepts/congruence.md) · [funnel audit rubric](../rubrics/funnel-audit.md) · [email sequences](email-sequences.md) (post-purchase continuation) · [rules library](../libraries/rules.md)
