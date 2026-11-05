---
title: "Brief generator (RMBC II Brief 2.0 via Claude Project)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-03-airbnb-arbitrage-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-04-blood-sugar-supplement-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
tags: [brief, brief-2-0, brief-generator, claude-project, vsl-brief, placeholders, revision-loop, rmbc]
updated: 2026-11-02
---

# Brief generator (Brief 2.0 via Claude Project)
> Turn research, a mechanism and offer facts into the 25-field "New Brief" with one Claude Project, revise it by chat as copy chief, replace every placeholder with verified facts, then hand it to a length-specific VSL project.

## 🤖 Agent use
- **Use when:** you have finished research ([deep-research-workflow](deep-research-workflow.md)) and a mechanism ([ump-ideation-and-evaluation](ump-ideation-and-evaluation.md)) and need the single context document that every later copy prompt (VSL, advertorial, hook ad, PDP) consumes; or you must audit an existing brief for missing fields.
- **Inputs → outputs:** unified research doc + UMP/UMS doc + ingredient/studies doc (supplements) + product page URL or offer overview + offer facts (price, guarantee, speakers) → 25-field Brief 2.0 with `[VERIFY: …]` placeholders → revised brief (V1/V2) → outline + length estimate from a VSL project.
- **Rules:**
  - **DO** make a brief for every VSL project: "Do not skip it." [05-01 01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DON'T** fill the brief by hand from scratch; let the generator populate it from your documents. [05-01 10:05](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DO** put the template and classic VSL outline in project knowledge; put per-product files in the chat. [05-02 00:00–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
  - **DO** keep field 3 (teaser promises about the copy) separate from field 9 (product claims). [05-01 11:09](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DO** review as "the director… the boss… the copy chief… the CMO" and revise by chat, not by hand. [05-04 08:53](../lessons/05-04-blood-sugar-supplement-example.md)
  - **DO** save each good version to a document before revising. [05-02 17:46](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md), [05-05 12:02](../lessons/05-05-financial-promo-example.md)
  - **DO** check that the output actually used your attachment; "this is why you gotta stand on top of it." [05-05 07:05–08:56](../lessons/05-05-financial-promo-example.md)
  - **DON'T** pass any generated testimonial, study, statistic, credential, review count, persona, price or scarcity line to copy. Every course example invents them (see [Compliance](#compliance)). Repo rule: never invent proof.
  - **IF** the offer has no live page **THEN** write a 1–2 page offer overview first. [05-03 01:04](../lessons/05-03-airbnb-arbitrage-example.md)
  - **IF** the offer is high-ticket (about $8,000 in the example) **THEN** brief for a book-a-call VSL, not a direct-sale VSL. [05-03 07:38](../lessons/05-03-airbnb-arbitrage-example.md)
  - **IF** the mechanism section is jargon-heavy **THEN** ask Claude to rewrite it without the jargon before generating scripts. [05-02 07:58](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
- **See also:** [Brief 2.0 concept](../concepts/brief-2-0.md) · [Claude project recipe](../concepts/claude-project-recipe.md) · [prompts library](../libraries/prompts.md) · [templates library](../libraries/templates.md) · [VSL build with Claude](vsl-build-with-claude.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md)

## What it is
- **Old brief:** 12 questions a human copywriter filled in before writing long-form copy (audience, pains, one big promise, existing solutions, mechanism, paradoxical question, metaphor, bold claim, product, story, headlines, upsell ideas). [05-01 02:03–07:10](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
- **New brief (Brief 2.0):** 25 fields written for an LLM reader ("enough detail so that when given to an LLM, it could write this whole section without struggling"), populated by a Claude Project from your research and mechanism files. [05-01 01:03–10:05](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
- **Why it matters:** it is the B in RMBC: one document that "will tie together what we did so far" and lets you "print all kinds of copy" across lengths and formats. [05-01 01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md); [05-02 47:10](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)

## Inputs checklist
| Input | Required? | Where it comes from | If missing |
|---|---|---|---|
| Unified research doc (audience, pains, language, objections, failed solutions) | Yes for real work | [deep-research-workflow](deep-research-workflow.md), [02-04](../lessons/02-04-unified-research-process.md) | Generator invents audience; 05-04 got "women 45-65" wrong [05-04 01:38–02:12](../lessons/05-04-blood-sugar-supplement-example.md) |
| UMP/UMS doc | Yes | [ump-ideation-and-evaluation](ump-ideation-and-evaluation.md) | Generator builds a mechanism from repeated study themes (GLUT4 in 05-04); verify before use [05-04 04:07–04:55](../lessons/05-04-blood-sugar-supplement-example.md) |
| Ingredient + studies doc | Supplements only | [02-05](../lessons/02-05-ingredient-deep-research.md) | Field 8 empty or invented |
| Product page URL (web search on) | If a page exists | Live PDP | Use offer overview |
| Offer overview (program title, spokesperson, brand & core promise, curriculum, coaching components, offer/price/guarantee) | If no page | Client facts | Do not let an LLM invent it for a real offer [05-03 03:31](../lessons/05-03-airbnb-arbitrage-example.md) |
| Real offer facts: retail price, VSL price, tiers, guarantee, bonuses, real scarcity | Yes | Client | `[VERIFY: price]` etc. |
| Real speaker(s) and credentials; real testimonials; real credibility builders | Yes | Client | `[VERIFY: …]`; never fabricate |

## Steps

### Step 1 — Build the Brief Generator project (once)
- **Input:** "The New Brief" template (blank) + classic VSL structure outline.
- **Output:** Claude Project "RMBC II Brief Generator".
- **Prompt (project instructions, verbatim, doc "02-21 Brief Generator_Claude Projects.docx"):**
```text
Your Job is to Create New Briefs for Copywriting Projects. These are things that I can give to Claude Projects or other LLMs to have them write copy. We’ll mostly be focused on VSLs here, but I may end up asking you to create a brief for an eCommerce page in the future as well.

I’ve included two documents in your knowledge base for now.

The first is an in-depth brief. It is titled “The New Brief.”

The second is an outline of the classic Video Sales Letter Structure I’ve used for a long time. That one is mostly for reference.

Here’s how this will work:

I will use your chat feature to provide documents that can assist you in writing the brief for a specific product. You’ll then do that. For anything where you don’t have information, you can use placeholders to start.
```
- **Knowledge files:** The New Brief (full text in [Output contract](#output-contract) and [templates library](../libraries/templates.md)); classic VSL outline ([classic VSL structure](../concepts/classic-vsl-structure.md)).
- **Tool/model:** Claude Project; the demo UI shows Claude Sonnet 4. Enable web search if you will link a product page. [05-02 01:02–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
- **Check before moving on:** template uploaded blank ("nothing filled in, just the new brief") [05-02 01:02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md). Repo addition (derived): append to the instructions "Use [VERIFY: …] for every fact, number, name, study, testimonial or credential not present in my attachments."

### Step 2 — Assemble the per-product inputs
- **Input:** files from the [Inputs checklist](#inputs-checklist).
- **Output:** 1–3 attachments + optional URL.
- **Prompt (only if no offer page exists):** the instructor had Gemini draft the offer overview. Spoken, approximate, reconstructed [05-03 03:31](../lessons/05-03-airbnb-arbitrage-example.md):
```text
[Offer type, e.g. high-ticket coaching program] sales funnel. Sketch the program details here. I can use it as an example. Also create a fictional spokesperson and other relevant data.
[Attach: unified research doc, UMP]
```
  Hard stop under repo rules: "create a fictional spokesperson" is a teaching shortcut. For our brands, write the overview from real facts under these verbatim headings: Program Title; Spokesperson / Guru Persona (Name, Archetype, Backstory, Positioning); The Coaching Program Brand & Core Promise; The Core Curriculum (modules with Concept and Deliverables); The High-Ticket Coaching Components; The Offer, Pricing & Guarantee. [05-03 02:10](../lessons/05-03-airbnb-arbitrage-example.md)
- **Tool/model:** any doc editor; Gemini 2.5 Pro in the demo.
- **Check before moving on:** each attachment is plain text or a text PDF (image-heavy PDFs triggered errors in [02-04](../lessons/02-04-unified-research-process.md)).

### Step 3 — Run the per-product prompt
- **Input:** attachments + URL.
- **Output:** 25-field brief as an artifact (eye serum example: about 3,950 words of input became a 3,376-word brief). [05-02 Examples](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
- **Prompt (product with a page, verbatim, "Eye Serum Prompt Example.docx"; brand, product and URL are the per-product edits):**
```text
I want your help generating a new brief for our brand [BRAND]'s [PRODUCT]. Here is a current product page where you can pull some inputs:

[PRODUCT PAGE URL]

Additionally, I am attaching a UMP and also some market research that you can pull from when writing the brief.

I’m also including a document with the ingredients and relevant studies.

Please go ahead and get started now.
```
- **Prompt variants (verbatim course files):**
  - No page, info offer ([05-03](../lessons/05-03-airbnb-arbitrage-example.md)): "I want your help generating a new brief for our [Airbnb Arbitrage Coaching Program]. / I am attaching a UMP and also some market research that you can pull from when writing the brief. / I’m also including a document with some additional relevant information. / Please go ahead and get started now."
  - Ingredients only, narrator specified ([05-04 00:33–01:04](../lessons/05-04-blood-sugar-supplement-example.md)):
```text
I want your help generating a new brief for a new blood sugar supplement VSL.

I am attaching ingredients list and studies for your reference.

Please use placeholders to come up with the strongest brief possible. I will switch out everything later, but I want to see an example of what this brief can look like.

Let's have this VSL come from the perspective of a woman who has a personal struggle with diabetes (either her own blood sugar is high, or someone close to hers is) and who meets an expert who helps show her the real solution.

Please go ahead and get started now.
```
  - Single offer document ([05-05 03:20–04:04](../lessons/05-05-financial-promo-example.md)): "I want your help generating a new brief for a [Financial Newsletter VSL]. / I'm attaching a document with additional relevant information. / Please go ahead and get started now."
- **Tool/model:** the Brief Generator project.
- **Check before moving on:** the first line of the reply references your files (eye serum: "Let me first gather information from the product page and then create the brief using the research documents you've provided") [05-02 01:42](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); names, bonuses and price match your attachment (see failure F1).

### Step 4 — Audit the draft field by field
- **Input:** generated brief + your attachments.
- **Output:** list of placeholders, unsourced claims, wrong assumptions.
- **Prompt:** none in the course; run the [LLM output claim audit](../rubrics/llm-output-claim-audit.md) (derived).
- **Check:** for each of the 25 fields, mark source = attachment / product page / generator. Real examples of generator-only content to flag: "Harvard researchers…", "97% of eye creams fail", "45% wrinkle reduction in 60 days", "39% in just four weeks" (05-02); "$12,000+ monthly passive income", "Featured in BiggerPockets" (05-03); "20 human clinical trials", doses not in the research, A1C testimonials (05-04); "15-25% annual returns" (05-05). [05-02 10:51–14:52](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [05-03](../lessons/05-03-airbnb-arbitrage-example.md); [05-04](../lessons/05-04-blood-sugar-supplement-example.md); [05-05 04:51–06:18](../lessons/05-05-financial-promo-example.md)

### Step 5 — Save V1, then revise by chat
- **Input:** audit notes + decisions (pricing in VSL, speakers, partner brand, bonuses, mechanism simplification, audience).
- **Output:** revised brief.
- **Prompt (revision message, reconstructed from speech, approximate) [05-02 19:03–20:19](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md):**
```text
This was great overall. Really good job. Here are a few tweaks or pieces of information for revisions.
First off, for the pricing, let's go with the one-time purchase pricing in the VSL and show the subscribe and save options below the VSL.
Second, the main speaker would be Laura. She's a mom of two in Florida.
Dr. Schilling helps explain what's really going on, the UMP and UMS. The whole VSL will come from Laura, recounting what Dr. Schilling shared. Ultimately, Laura partnered with her husband to create Opal Beauty.
Lastly, go with no bonuses.
```
  The instructor says these persona details are not true ("I'm using this mostly for an example") [05-02 13:46; 19:03](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md). Pattern only: pricing decision → main speaker → expert role → partner brand → bonuses.
- **Prompt (audience correction, screen text, verbatim) [05-04 04:18](../lessons/05-04-blood-sugar-supplement-example.md):** "I think the audience is women and men. I think having it be primarily women is fine, but I wouldn't ignore men."
- **Tool/model:** same chat.
- **Check:** re-read the story field after revision ("I'm going to make sure the story stayed the same"); replace the saved brief. [05-02 20:19–23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)

### Step 6 — (Optional) Generate a second story version
- **Input:** saved V1 + a one-paragraph alternative narrator and arc.
- **Output:** V2 brief (same mechanism and ingredients, different story and speaker roles).
- **Prompt (screen text, verbatim; cut off on screen) [05-04 12:36](../lessons/05-04-blood-sugar-supplement-example.md):**
```text
This is great, thank you. Now I would like to see a second version of the brief, where it comes from the doctor. Let's have him share the story of a patient who was at her wits end about her high blood sugar. We can tell more about her suffering and then the doctor felt helpless, and decided to go on a quest to figure out why so many like this patient still struggle with high blood sugar despite all the medications, artificial sweeteners and other solutions out there. This ultimately led him to discover the UMP, the UMS, the ingredients, and then he created a
```
- **Check:** V1 kept and labelled ("V1… and now… V2") [05-04 12:32](../lessons/05-04-blood-sugar-supplement-example.md); the doctor must be a real, verifiable person before copy. Treat narrator perspective as a test variable ("you can do both and decide") [05-04 15:17](../lessons/05-04-blood-sugar-supplement-example.md).

### Step 7 — Replace placeholders with verified facts
- **Input:** revised brief + client facts.
- **Output:** final brief with no unresolved `[VERIFY: …]` in fields that will reach copy.
- **Prompt:** none in course (derived step). The instructor's own position: "I will switch out everything later" [05-04 00:33](../lessons/05-04-blood-sugar-supplement-example.md); "hopefully it's true" about credibility builders [05-01 13:12](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md).
- **Check:** fields 8, 9, 12–16, 17–22 each trace to a real source; proof gaps become a collection checklist (05-03 lists "proof categories needed": before/after snapshots, booking-income screenshots, landlord interviews) [05-03 06:34–07:38](../lessons/05-03-airbnb-arbitrage-example.md).

### Step 8 — Hand off to a length project
- **Input:** final brief.
- **Output:** outline + length estimate (approve before drafting) or a concept list.
- **Prompt (medium project, screen text, verbatim) [05-02 24:24](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md):**
```text
I'm going to upload a comprehensive brief for a new VSL. It should give you everything you need to write it. Please review, and then I want you to give me an outline for this new VSL, along with your estimate for how long it'll be. Let's aim for about 18 minutes.
```
- **Prompt (short project, screen text, verbatim) [05-02 33:36](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md):**
```text
Here's a brief for a VSL for our skincare brand. Please review and then give me 5-10 short VSL concepts you think would be worth testing?
```
- **Prompt (long-form, structure-modelled, screen text, verbatim; truncated on screen) [05-05 14:52](../lessons/05-05-financial-promo-example.md):**
```text
Here's a brief for a new financial offer. I want you to model off the structure of the Agora Secret Trust Fund sales letter you have in your knowledge base, to write a new VSL Script for the new offer, based on the brief. Please keep the structure very similar, and if you need to do it over multiple outputs that's fine, just prompt me if you run out of space and I'll tell you to continue.
```
- **Tool/model:** the length-specific VSL projects from [vsl-build-with-claude](vsl-build-with-claude.md).
- **Check:** Claude "estimates a little low", so ask for a bit more than your target [05-02 23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); remove the brand name from the script unless intended [05-02 26:59](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md).

## Decision points
| IF | THEN | Source |
|---|---|---|
| Product has a live page | Link it, enable web search, attach research + UMP + ingredients | [05-02 01:02–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| No page (coaching, course, info product) | Write the offer overview first (six headings), attach it as "additional relevant information" | [05-03 01:04–03:31](../lessons/05-03-airbnb-arbitrage-example.md) |
| Only ingredient research exists | Run anyway for ideation; name the narrator; treat mechanism and everything else as placeholders to verify | [05-04 01:38; 09:53–10:23](../lessons/05-04-blood-sugar-supplement-example.md) |
| No separate UMP file (one combined offer doc) | Attach the single doc and confirm the output used it | [05-05 03:20–04:04](../lessons/05-05-financial-promo-example.md) |
| No brand story / spokesperson yet | Name the narrator perspective in the prompt ("you need to kind of know who this spokesperson is") | [05-04 01:04](../lessons/05-04-blood-sugar-supplement-example.md) |
| Offer around $8,000 | Brief for a book-a-call VSL | [05-03 07:38](../lessons/05-03-airbnb-arbitrage-example.md) |
| Subscribe-and-save exists | One-time price in the VSL; subscription options below it | [05-02 19:03](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Bundle offer (e.g. six-bottle) | Show price per bottle; don't add "limited 3 per customer" scarcity that blocks it | [05-04 07:44–08:16](../lessons/05-04-blood-sugar-supplement-example.md) |
| Product is a supplement | Fill field 8: main ingredients, 2–3 studies each | [05-01 11:09](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) |
| Product is an informational program | Use fascination bullets in field 10 | [05-01 05:12–06:10](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) |
| Want a different story structure | Save V1; ask for "a second version of the brief" with the new narrator | [05-04 10:53–12:32](../lessons/05-04-blood-sugar-supplement-example.md) |
| Generated hook/CTA sells the product instead of the next step | Rewrite the CTA to sell the click ("save 57% off to get more information") | [05-02 42:17–43:17](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Writing the VSL later from a thin product field | Upload the full offer document to the VSL project too | [05-03 06:34](../lessons/05-03-airbnb-arbitrage-example.md) |

## Failure modes and fixes
| # | Symptom | Cause | Fix | Source |
|---|---|---|---|---|
| F1 | Brief is generic, invents bonuses ("The Crisis Playbook", "The Fed Files") and returns not in your doc | Generator ignored the attachment | Re-upload and name the doc: "Well it's the Genetic Royalty Revolution example brief. That's what I'm referring to. This already did some of the legwork for you. Now you just need to put that into the New Brief template, and also fill out the rest of the New Brief Template with placeholder information." | [05-05 07:05–09:52](../lessons/05-05-financial-promo-example.md) |
| F2 | Wrong audience (women only) | Narrator choice in prompt bled into audience; no research attached | Send audience correction (Step 5); attach the unified research doc | [05-04 01:38–02:12](../lessons/05-04-blood-sugar-supplement-example.md) |
| F3 | Mechanism overloaded with jargon (DEJ + weave metaphor) | Generator merged UMP doc with product-page language | "Rewrite the mechanism without it" before drafting scripts | [05-02 07:58; 37:16](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| F4 | Invented studies, stats, credentials, testimonials, review counts | Instructions allow placeholders but the model fills them with plausible numbers | Claim audit (Step 4); bracket as `[VERIFY: …]`; add the repo line to project instructions | [05-02 13:46–14:52](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [05-04](../lessons/05-04-blood-sugar-supplement-example.md) |
| F5 | Mechanism built from rodent/cell study themes | Ingredient-only input | Verify mechanism against human evidence before copy | [05-04 04:07–04:55](../lessons/05-04-blood-sugar-supplement-example.md) |
| F6 | Doses or ingredient counts in brief don't match research | Generator filled field 8/10 from priors | Confirm from the real formula | [05-04 Sources and limitations](../lessons/05-04-blood-sugar-supplement-example.md) |
| F7 | Product field too thin for a VSL | Brief summarises the offer doc | Attach the full offer doc again at the VSL step | [05-03 06:34](../lessons/05-03-airbnb-arbitrage-example.md) |
| F8 | Revision silently changes the story | Whole-artifact rewrite | Re-read story field after each revision; keep saved versions | [05-02 20:19–23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| F9 | VSL script names the brand when it shouldn't | Brand in brief fields 12–14 | Tell the VSL project not to mention the brand | [05-02 26:59](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| F10 | Claude errors or limits on large attachments | Image-heavy PDFs / usage caps | Convert to plain-text PDF; retry later or via Poe with Claude Sonnet 4 | [02-04 16:39–24:24](../lessons/02-04-unified-research-process.md) |

## Output contract
Brief 2.0, 25 fields (verbatim headings from "01-12 The New Brief.docx"; full field text in [05-01](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) and [templates](../libraries/templates.md)). Column 3 is the repo rule for each field.

| # | Field | Agent rule |
|---|---|---|
| 1 | Who's the Audience? | From research, not narrator choice |
| 2 | Pain points / biggest fears (1–3 HUGE; short term, long term) | Customer language from research |
| 3 | Big promises about the sales copy (teasers) | Promise what the copy reveals, not product results |
| 4 | What it looks like when pain points are solved (physical, emotional, social, psychological) | Future-pace; no specific numbers without proof |
| 5 | Existing solutions and why they aren't working | From research |
| 6 | Unique Mechanism of the Problem and of the Solution (LLM-ready detail) | From UMP doc; verified |
| 7 | Unique nickname for the mechanism | e.g. "30 second breakfast hack", "Paper Flipping" [05-01 10:05](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) |
| 8 | (Supplements) main ingredients, 2–3 studies each | Real citations only; note study type (human/animal/cell) |
| 9 | Bold product claims | Structure/function wording for supplements; `[VERIFY: …]` |
| 10 | What is the Product? (features/benefits or fascinations) | From product page/formula |
| 11 | Background story + story of discovery (hero's journey) | Real story or `[VERIFY: founder story]` |
| 12 | Main speaker + credibility snapshot | Real person only |
| 13 | Second speaker / expert | Real, verifiable expert or none |
| 14 | Brand/company partnership | Real |
| 15 | Testimonials / social proof | Real, permissioned only |
| 16 | Credibility builders for the opening | Real sources only; no "Harvard", "Forbes", celebrity endorsements unless true |
| 17 | Normal retail price | Real |
| 18 | Actual VSL price | Real |
| 19 | Options and pricing per option | Real |
| 20 | Guarantee | Real |
| 21 | Bonuses | Real or "none" |
| 22 | Scarcity elements | Real only; repo rule bans fake scarcity |
| 23 | Future-paced results and benefits | No timelines/percentages without proof |
| 24 | Objections and answers | From research |
| 25 | Hooks or big ideas to test in the lead | Ideas only; instructor writes the lead separately [05-02 16:48–17:46](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |

Dropped from the old brief: paradoxical question, metaphor ("AI is quite good at metaphors"), headline ideas, upsell ideas. [05-01 04:11; 07:10](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)

## Compliance
- **Course content, accurately described:** all four worked briefs contain generator-invented proof: named experts and credentials, study percentages, customer counts, star ratings, testimonials with A1C numbers, income figures, investment returns, "Big Pharma" conspiracy lines, disease-cure claims and fabricated scarcity. Structure only; claims not reusable. [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [05-03 Compliance check](../lessons/05-03-airbnb-arbitrage-example.md); [05-04 Sources and limitations](../lessons/05-04-blood-sugar-supplement-example.md); [05-05 Agent use](../lessons/05-05-financial-promo-example.md)
- **Instructor admissions (recorded; hard stops under repo rules):** "I'm not encouraging you to be doing like the dark arts, but there is the power for somebody to… abuse this" [05-04 00:33](../lessons/05-04-blood-sugar-supplement-example.md); "It's probably not very compliant, but like it's so good now" [05-05 10:01](../lessons/05-05-financial-promo-example.md); "I know it's not compliant" [05-05 15:07](../lessons/05-05-financial-promo-example.md); fictional spokesperson requested from Gemini [05-03 03:31](../lessons/05-03-airbnb-arbitrage-example.md); persona details "not actually true" [05-02 13:46](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md).
- **Compliant pattern:**
  - Every unsourced fact → `[VERIFY: source for "…"]`; unresolved placeholders block the hand-off to Step 8 for fields 8, 9 and 12–23.
  - Supplements: structure/function wording ("supports healthy blood sugar levels already in the normal range" style); no treat/cure/reverse/"better than medication" language. The instructor called the 05-04 field-9 claims "pretty compliant", but its hooks, promises, testimonials and credibility lines were not. [05-04 04:55–05:54](../lessons/05-04-blood-sugar-supplement-example.md)
  - Biz-opp/financial: no income or return figures without substantiation and typical-results disclosure; no invented track record.
  - Proof gaps → collection checklist (05-03 "proof categories needed" pattern), never fabricated lines.
  - Copy the mechanism, not the asset: when modelling a winner's structure (05-05 Secret Trust Fund), rewrite all lines; the instructor calls his output "a really direct swipe" [05-05 16:30](../lessons/05-05-financial-promo-example.md). See [composite vs swipe](../concepts/composite-vs-swipe.md), [compliance red flags](../concepts/compliance-red-flags.md).

## Worked examples
| Example | Inputs | Notable output (course content; structure only) | Instructor action | Source |
|---|---|---|---|---|
| Unity Eye Serum (Opal Beauty), skincare, has a page | Unified research + combined ingredient research + UMP/UMS ("collagen architecture breakdown") + product URL | 25 fields; UMS "structural renewal system" signal/repair/lock; nickname "the DEJ renewal protocol"; five hooks + five big ideas | Revised pricing, speaker (Laura narrates Dr. Schilling), no bonuses; then medium (~18 min), short (5–10 concepts, 3-min and 2-min drafts), hook ads, long (~28 min, 5,167 words) | [05-02 00:00–47:10](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [05-03 00:00](../lessons/05-03-airbnb-arbitrage-example.md) |
| Airbnb arbitrage coaching, no page | Unified research + "asset gap" UM doc + Gemini-drafted offer overview ("The Asset Accelerator", $8,000 or 3 × $3,000) | UMP "the Asset Gap", UMS "the Asset Control Method"; nicknames "The Rental Arbitrage Loophole" etc.; 8 objections; proof categories | Fast review; says sell via book-a-call VSL | [05-03 01:04–08:43](../lessons/05-03-airbnb-arbitrage-example.md) |
| Blood sugar chew, ingredients only | 10-ingredient research doc | Mechanism invented from GLUT4 theme ("Glucose Transport Dysfunction", "The Cellular Door Fix"); V1 caregiver narrator, V2 doctor narrator | Audience correction; V2 request; "run the brief thing a couple of times" for new formulas | [05-04 00:00–15:17](../lessons/05-04-blood-sugar-supplement-example.md) |
| Financial newsletter ("Genetic Royalty Revolution") | Single offer doc ideated by Gemini from the Agora Secret Trust Fund transcript | Run 1 ignored attachment; run 2 mapped the doc onto 25 fields | Recovery message; then Long Form VSL Generator modelled on Secret Trust Fund structure | [05-05 00:00–19:27](../lessons/05-05-financial-promo-example.md) |

## Where it's taught
- [05-01 The old brief vs the new brief](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md): why the brief matters [00:00–02:03]; classic brief [02:03–07:10]; new fields [07:10–16:20].
- [05-02 Brief generator + Unity Eye Serum](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md): project setup [00:00–03:07]; output by field [04:12–17:46]; revision [17:46–23:00]; length hand-offs [23:00–47:10].
- [05-03 Airbnb arbitrage](../lessons/05-03-airbnb-arbitrage-example.md): no-page inputs [01:04–03:31]; brief review [03:31–08:43].
- [05-04 Blood sugar supplement](../lessons/05-04-blood-sugar-supplement-example.md): ingredient-only run [00:00–08:53]; when to use [09:53–10:53]; V2 [10:53–15:17].
- [05-05 Financial promo](../lessons/05-05-financial-promo-example.md): offer ideation [00:00–02:48]; failed run and recovery [02:48–11:00]; brief to script [12:02–19:27].

## Cross-course notes
- **Evolve Start Here, [research doc](../../../evolve/start-here/concepts/research-doc.md) and [product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md):** both build the product and mechanism understanding by hand (7-step product overview, then name the mechanism). RMBC lets the generator draft the whole brief, and in 05-04 even invent the mechanism from ingredient studies. **Agent default:** a human-verified product overview and mechanism must exist before the brief; use the generator to fill and format, not to originate mechanism or proof. Logged in contradictions notes.
- **Evolve Copywriting, [ad idea to brief](../../../evolve/copywriting/playbooks/ad-idea-to-brief.md):** a per-ad creative brief. RMBC's Brief 2.0 is the upstream offer-level document; derive per-ad briefs from it.
- **Evolve Copywriting, [unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md) and [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md):** agree that the LLM drafts and the human edits as copy chief.
- **Tether Lab, [creator brief](../../../../playbooks/creator-brief.md):** a production brief for UGC creators; fill its product, claims and proof sections from the final (verified) Brief 2.0 fields 6, 9, 10 and 15.

## Related
- Concepts: [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Brief 2.0](../concepts/brief-2-0.md) · [unified research document](../concepts/unified-research-document.md) · [unique mechanism](../concepts/unique-mechanism.md) · [Claude project recipe](../concepts/claude-project-recipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [compliance red flags](../concepts/compliance-red-flags.md) · [sell the click](../concepts/sell-the-click.md)
- Frameworks: [deep research workflow](deep-research-workflow.md) · [UMP ideation and evaluation](ump-ideation-and-evaluation.md) · [VSL build with Claude](vsl-build-with-claude.md) · [hook generation system](hook-generation-system.md) · [advertorial build](advertorial-build.md) · [PDP build](pdp-build.md)
- Playbooks / rubrics / libraries: [offer to funnel end to end](../playbooks/offer-to-funnel-end-to-end.md) · [write a VSL with Claude](../playbooks/write-a-vsl-with-claude.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [prompts](../libraries/prompts.md) · [templates](../libraries/templates.md)
