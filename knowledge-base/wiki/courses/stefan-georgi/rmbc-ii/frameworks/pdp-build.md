---
title: "PDP Build (outline-extract → swipe → copy-chief → test)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md
tags: [pdp, product-page, ecom-lander, claude-prompts, outline-extraction, swipe-structure, mobile, price-comparison]
updated: 2026-11-02
---

# PDP Build
> Size the product page to the selling still left after the ad and pre-sell page, extract a working competitor PDP's structure with Claude, rebuild that structure from our brief, strip all invented proof, audit on mobile, and test two structures against each other.

## 🤖 Agent use
- **Use when:** writing or rewriting a PDP / "eCom lander" for our brand; auditing a PDP for missed copy; turning a competitor PDP into a reusable outline.
- **Inputs → outputs:** traffic source in front of the page (ad format and length, advertorial length) + 1–2 reference PDPs in a similar vertical + our [Brief 2.0](../concepts/brief-2-0.md) (or live product URL) → saved outline doc(s) → PDP copy with design/structure notes → claim-audited draft → 2-structure test plan.
- **Rules:**
  - **DO** fix the PDP's job before writing: "It depends on what the goal is… what the rest of the journey before the product page looks like." [10-01 00:36–03:52](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **DO** write a longer PDP behind static or <60s video ads and short advertorials; shorter behind 60s+ video or long advertorials. "You have to do the selling somewhere." [10-01 05:07–07:44](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **DO** extract structure, not copy: "you're just taking the structure… the outline of the structure." [10-01 53:12](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **DO** review on mobile first; most sales come from mobile, "70% to 90%… In some cases, 100%" (instructor claim; check our own analytics). [10-02 18:30](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)
  - **DO** make the CTA label echo the offer headline ("Get -65% discount", not "buy now") and keep a sticky CTA bar. [10-02 03:28, 06:12](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)
  - **DON'T** write "money-saving solution" without numbers: "That's like not good copy… show, don't tell." [10-02 08:29–10:05](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)
  - **DON'T** hunt for the one perfect page: "you just have to test stuff." [10-01 50:31](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **DON'T** ship any Claude-generated testimonial, review count, rating, doctor, study, press logo or medical outcome. Every course output contains them; they are layout placeholders. See [compliance red flags](../concepts/compliance-red-flags.md).
  - **IF** affiliates send traffic **THEN** no phone number in the header; **IF** no affiliates **THEN** test one. [10-02 01:25–02:28](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)
- **See also:** [ad-to-page journey](../concepts/ad-to-page-journey.md) · [advertorial build](advertorial-build.md) · [checkout optimization](checkout-optimization.md) · [CRO testing](cro-testing.md) · [prompts library](../libraries/prompts.md) · [templates library](../libraries/templates.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · shared [landing page scorecard](../../../../rubrics/landing-page-scorecard.md) · [landing page psychology audit](../../../../frameworks/landing-page-psychology-audit.md) · [Shopify landing pages with Claude](../../../../resources/shopify-landing-pages-with-claude.md)

## Definition
A PDP in RMBC II is the modern replacement for the text sales letter: "very long, but… more branded… easier to run on Facebook" [10-01 01:22](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). It has one of three jobs: heavy selling, a branded experience that pushes a pre-sold visitor "over the hump", or both [10-01 00:36–03:52](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). Stefan rejected a dedicated Claude Project for PDPs: "I don't think you need it. I would just do it the way I did in this video" (pick a page you like, say "go model") [10-01 52:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).

## Procedure

### Step 1. Set the PDP's job and length
- **Input:** what sits in front of the page (ad format and length; advertorial yes/no and length); traffic temperature.
- **Output:** one sentence: "Traffic arrives from [X]; the PDP must still sell [Y]; target length [long / short]."
- **Decision table** (derived from [10-01 05:07–09:47](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)):

| IF traffic arrives from | THEN PDP job | Length |
|---|---|---|
| Static ad or short video (<60s), and/or short advertorial | Do the remaining selling: why other solutions failed, real cause (UMP), why ours works (UMS) | Long, "mini sales letter" |
| Medium/long video (60s+) and/or long advertorial | Convert a pre-sold visitor; brand experience | Short |
| Retargeting / brand-build | Brand store page | Short (Happy Mammoth store page: "I don't think it works for cold traffic") [10-01 11:49](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Hijacked, universally wanted trend (e.g. GLP-1 meds) | Trust, speed, reviews | Short; "very, very rare" [10-01 05:41–06:46](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Long video + long advertorial (Nooro pattern) | Test only | Long; "pretty rare" [10-01 08:15–09:33](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Free webinar / live-event signup | Registration only (one action) | Short; see [webinar funnel](webinar-funnel.md) and Calvin Tran page [10-02 16:35–21:38](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) |

- Selling "by awareness level" means: why other solutions failed, the real cause of the problem, and, for product-aware buyers, why other products fail and ours is superior; "twisting the knife" so they act today [10-01 05:41–07:14](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). See [product-market awareness](../concepts/product-market-awareness.md).
- **Failure mode:** cold traffic sent to a short brand page. Fix: send cold to the long page; keep the short page for retargeting [10-01 11:49–12:52](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).

### Step 2. Pick 1–2 reference PDPs
- **Input:** competitor and adjacent-vertical PDPs.
- **Output:** 1–2 URLs (or 2 similar product pages from one brand).
- **Selection rule:** "find something that is working that looks good… ideally you know it works because it means it's got a lot of elements, it's in a similar vertical" [10-01 54:08–54:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). Proxy for "working": ads running to it for a long time (derived).
- **Course reference set:** Happy Mammoth (long supplement PDP), Emma Relief (branded + video), Dr. Clean (physical-product DR/e-com hybrid, 20 sections), Heat Healer sauna (hard product, 13 sections). Skeletons: [templates library](../libraries/templates.md).
- **IF** physical product or supplement and want a "classic" clean template **THEN** use the Dr. Clean pattern [10-02 00:26, 02:59](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md). **IF** device/hard product **THEN** the sauna pattern ("[Action verb] + [Outcome]: [technical explanation], leading to [specific user experience]") [10-01 doc 8](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).

### Step 3. Extract the outline (new Claude chat, web search ON)
- **Input:** reference URL(s).
- **Output:** templatized section outline with bracketed variables.
- **Prompt A, two links from one brand** [10-01 20:56–21:30](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md):
```
I'm going to share two product page links from a brand with you. They are for two different products, but similar. Please review them, and then I would like for you to create a templatized outline that captures both the structure, and all of the common elements. This should be something someone could use for other products and brands to produce similar Product Pages.

[link 1]
[link 2]
```
- **Prompt B, one link** (doc typo "I'm going to a product page link" fixed) [10-01 31:19](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md), [10-02 doc 3](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md):
```
I'm going to share a product page link from a brand with you. Please review it, and then I would like for you to create a templatized outline that captures both the structure, and all of the common elements. This should be something someone could use for other products and brands to produce similar Product Pages.

[link]
```
- **IF** Claude says it cannot fetch the page (robots.txt) **THEN** paste the page copy as plain text (Ctrl/Cmd+Shift+V), attach one or more above-the-fold screenshots, and send [10-02 15:35–16:35](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md):
```
okay here's the copy attached. And here's a screenshot of the above the fold.
```
- **Failure mode:** with two links Claude may merge the pages unevenly ("it did for one about the other") [10-01 24:29](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). Check every section of both pages appears; re-run per page if not.

### Step 4. Save the outline as its own doc
- **Output:** a named file, e.g. "[Brand] PDP outline sample".
- **Why:** if the competitor page changes, "here's the structure. I have it." [10-01 25:08, 41:18](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)

### Step 5. Swipe the structure for our product
- **Input:** saved outline (same chat or attached) + our brief or live PDP URL.
- **Output:** full PDP copy with design and structural notes.
- **IF** product has a live page **THEN** Prompt C [10-01 25:45](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md):
```
Awesome, so now if we were going to test a new PDP for [product], following this structure, what would it look like? Can you go ahead and write the copy for it and indicate all the other design and structural elements? Here's the current PDP:

[product URL]
```
- **IF** we have a brief (preferred) **THEN** Prompt D, brief attached [10-01 33:49](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md):
```
Now, if we were going to test a new PDP for [product], following this structure, what would it look like? Can you go ahead and write the copy for it and indicate all the other design and structural elements? I've attached a brief that should give you all of the information on the [product] you need.
```
- **IF** no website exists yet **THEN** in the same conversation attach the brief and send [10-01 42:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md):
```
Nice! Now let's do a PDP for this blood sugar offer. It doesn't have a website yet. Do the exact same thing you did before please!
```
(Replace "blood sugar offer" with our product.)
- **IF** a brief AND a site both exist **THEN** attach the brief and also tell Claude to visit the site; Stefan says the brief-only run "probably would have been better" with the site fetched [10-01 41:18](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).
- **IF** no brief exists **THEN** stop and build one first: [brief generator](brief-generator.md). Without it the output is "such a swipe that you're like, oh God, this is dumb" [10-01 53:12](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).
- **IF** Claude starts coding / building an HTML artifact **THEN** stop it and send Prompt E [10-01 38:37](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md):
```
I don't need you to code or do HTML. I also don't want it in plain text. Instead, can you please just write the copy with formatting. Maybe it's best if you don't do it as an artifact?
```
  Known failure: in the video this did not fully stop the artifact; he used the copy from it anyway [10-01 39:23](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). Put the no-code line in the first swipe prompt to pre-empt it (derived).

### Step 6. Copy-chief edit and claim strip
- **Input:** Step 5 draft.
- **Output:** edited draft where every proof slot is real or bracketed.
- Edit "as copy chief" exactly as for VSLs [10-01 44:06–44:37](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); method in [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md).
- Check mechanism: problem → unique mechanism of the problem → solution (UMP → UMS) [10-01 15:42, 20:17](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). See [unique mechanism](../concepts/unique-mechanism.md).
- Run [LLM output claim audit](../rubrics/llm-output-claim-audit.md). Replace with `[VERIFY: …]`:

| Slot in the course outputs | What Claude invented in the course runs | Compliant replacement |
|---|---|---|
| Hero rating / review count | "4.8/5 stars from 5,832+ women" [10-01 41:18](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | Real store rating and count, or delete |
| Testimonials | Named reviewers (Sarah K., Elizabeth K.…) | Real, consented reviews only; else `[VERIFY: customer review]` |
| Statistical hook | "87% of eye aging", "3x faster" | `[VERIFY: stat + source]` or a non-numeric problem statement |
| Clinical study / "6 breakthroughs" | Uncited studies, percentages | Cite real ingredient research from the [unified research document](../concepts/unified-research-document.md); structure/function wording for supplements |
| Medical outcome | "Reduces A1C by up to 2 points", "stop taking insulin" (doc 7) | Hard stop: disease-treatment and drug-replacement claims are not allowed |
| Press logos / "#1 rated" / "rated most effective of [Year]" | Dr. Clean template slots 2, 15, 18 | Only if true and documented; else delete slot [10-02 template note](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) |
| Scarcity ("stock keeps selling out") | Template slot 18 | Only real stock/time limits |

### Step 7. Fill structural gaps the outline misses
- **Price justification.** Compute per-unit or per-use price and show it next to the category price. Dr. Clean's biggest miss: "$19.95" looked expensive versus ~$5 cleaners, but "it's actually like six bottles for $19.99… they don't make that clear" [10-02 07:21–14:58](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md). Block (fill with real numbers):
```
One [bottle/kit] = [N] [units]. That's $[price per unit] each vs $[category price] at [store].
[3-pack] = [N] units, $[total], $[per unit] each.
```
- **Package pricing.** Show price per bottle first, total after (Happy Mammoth) [10-01 17:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).
- **Future pacing timeline** (24 hours / Day 7 / Day 14 / Day 30) [10-01 14:25, 20:17](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md): only with outcomes we can substantiate; otherwise describe the routine, not results.
- **Repeat core value props** in hero, icon row and footer: "a little bit repetitive… But that's okay" [10-02 05:06](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md).
- **Mechanism visibility.** Dr. Clean's refill-tablet mechanism was missed even by Stefan on repeat views [10-02 07:21–07:55, 11:10](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md). Check that a skimmer gets the mechanism in the hero.

### Step 8. Mobile audit
- **Input:** built page (unpublished theme per [Shopify landing pages with Claude](../../../../resources/shopify-landing-pages-with-claude.md)).
- **Output:** phone-width screenshot + fix list.
- Checklist ([10-02](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)): CTA visible above the fold or sticky [19:01]; CTA label = offer headline [03:28]; announcement/urgency bar only if true; trust strip; in-page nav to sections [00:54–02:59]; phone number per affiliate rule.
- **Failure mode:** judging by desktop. Calvin Tran's desktop page: "Nobody's ever seen this page besides me." [10-02 19:01](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md)
- Score with the shared [landing page scorecard](../../../../rubrics/landing-page-scorecard.md).

### Step 9. Test two structures
- **Output:** test plan: current page vs Structure A vs Structure B.
- Stefan ran Happy Mammoth-style and Emma-style for the same product and kept both: "between the two, I like the Happy Mammoth one more, but I'll save this one as well" [10-01 41:18](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md). "Try and hit doubles and occasionally you'll just end up hitting a home run." [10-01 52:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
- Run rules (sample size, primary metric, earnings per session): [CRO testing](cro-testing.md).

## Failure modes (summary)

| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Claude returns HTML / artifact | No format instruction | Prompt E; add no-code line up front | [10-01 34:37–39:23](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| "robots.txt" fetch failure | Site blocks bots | Paste copy + screenshot | [10-02 15:35](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) |
| Output is a dumb clone of the competitor | No brief / thin product info | Attach Brief 2.0; tell Claude to visit our site | [10-01 41:18, 53:12](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Output full of stats, reviews, doctors | Claude fills template slots | Step 6 claim strip | [10-01 Compliance check](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Sticker shock / high discount needed | Value not shown in numbers | Step 7 price-comparison block | [10-02 14:23](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) |
| Long PDP not converting cold | No pre-sell, or wrong length for traffic | Recheck Step 1; add advertorial or video in front | [10-01 45:06–46:46](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |

## Where it's taught
- [10-01 PDP overviews and Claude processes](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md): purposes [00:00–03:52]; length rule [05:07–09:47]; Happy Mammoth teardown [09:47–20:56]; extraction [20:56–29:07]; brief-fed swipe and no-code fix [29:07–41:18]; no-website run [41:50–45:06]; sauna → Clarifion [45:06–48:55]; mindset [49:57–55:10].
- [10-02 Dr. Clean and Calvin Tran](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md): Dr. Clean section read [00:54–14:58]; price-comparison miss [07:21–14:58]; robots.txt fallback [15:35–16:35]; registration page and mobile [16:35–21:38].

## Cross-course notes
- **Shared Tether pages:** use [landing page psychology audit](../../../../frameworks/landing-page-psychology-audit.md) and [offer and bundle psychology](../../../../frameworks/offer-and-bundle-psychology.md) for the psychology layer; RMBC adds the length-by-traffic rule and the Claude extract-and-swipe procedure.
- **Evolve Copywriting:** the Dr. Clean "spend less money" critique is the same principle as Evolve's [show, don't tell](../../../evolve/copywriting/concepts/show-dont-tell.md) and [comparisons](../../../evolve/copywriting/concepts/comparisons.md).

## Related
[ad-to-page journey](../concepts/ad-to-page-journey.md) · [congruence](../concepts/congruence.md) · [composite vs swipe](../concepts/composite-vs-swipe.md) · [advertorial build](advertorial-build.md) · [checkout optimization](checkout-optimization.md) · [funnel audit rubric](../rubrics/funnel-audit.md)
