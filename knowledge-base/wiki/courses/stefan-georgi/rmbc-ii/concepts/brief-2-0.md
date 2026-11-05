---
title: "Brief 2.0 (the New Brief)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-03-airbnb-arbitrage-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-04-blood-sugar-supplement-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
tags: [rmbc-ii, brief, brief-generator, claude-projects, vsl, placeholders, offer]
updated: 2026-11-02
---

# Brief 2.0 (the New Brief)
> A 25-field brief written for an LLM reader, not filled by hand: a "RMBC II Brief Generator" Claude Project populates it from the unified research doc, UM doc, ingredient research and product page (placeholders for anything missing), you revise it by chat as copy chief, and it becomes the single context file every VSL, ad, advertorial, PDP and email project writes from.

## 🤖 Agent use
- **Use when:** after research and mechanism, before any VSL (any length); optionally before PDPs and advertorials; auditing a brief for missing fields; turning an offer with no page into writable context.
- **Inputs → outputs:** product page URL (if any) + unified research doc + UM doc (UMP/UMS) + ingredient/studies doc + offer facts (price tiers, guarantee, bonuses, speaker) → 25-field brief with `[placeholders]` → revised "Expanded Brief 2.0" saved as a doc.
- **Rules:**
  - **DO** make a brief for every VSL: "imperative ... especially imperative for long form ... very useful for short form ... can also be used for PDPs, advertorials". [05-01 00:00–01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) "Do not skip it." [05-01 01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DON'T** fill it by hand: "This is not a document that you fill out from scratch unless you really want to." Let the generator populate it. [05-01 10:05](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DO** put per-product inputs in the chat, not in project knowledge; enable web search so Claude reads the product page; end with "Please go ahead and get started now." [05-02 01:02–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
  - **DO** keep field 3 (promises about what the copy will reveal) separate from field 9 (product claims about life after purchase). [05-01 08:08–11:09](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **DO** check the output actually used your attachment; the financial run ignored it until he re-uploaded and named it: "this is why you gotta stand on top of it." [05-05 07:05–09:52](../lessons/05-05-financial-promo-example.md)
  - **DO** save the first good brief to a doc before revising, then revise by chat (pricing choice, main speaker, expert, bonuses). [05-02 17:46–23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
  - **DO** name the narrator in the prompt when there is no brand story ("you need to kind of know who this spokesperson is"). [05-04 01:04](../lessons/05-04-blood-sugar-supplement-example.md)
  - **DON'T** let generated speakers, credentials, studies, statistics, testimonials, review counts, prices, guarantees or scarcity reach copy. The 5.2 brief added "Harvard researchers…", "97% of eye creams fail", "45% wrinkle reduction in 60 days", none in the inputs. Mark `[VERIFY: …]`; fill fields 12–22 only with real facts. [05-02 Compliance check](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [05-04 06:46–08:53](../lessons/05-04-blood-sugar-supplement-example.md)
  - **HARD STOP:** Stefan's own field-16 guidance on credibility builders ("Harvard scientists ...", "Tony Robbins endorsed ...", "featured in Forbes") comes with "hopefully it's true". Under repo rules a credibility builder is either documented true or removed. [05-01 13:12](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
  - **IF** the offer has no page (coaching, info product) **THEN** write an offer overview doc (spokesperson, curriculum, price, guarantee) from the client's real details and attach it. [05-03 01:04–03:31](../lessons/05-03-airbnb-arbitrage-example.md)
  - **IF** price is high (~$8,000 coaching) **THEN** brief a book-a-call VSL, not a buy-now VSL. [05-03 07:38](../lessons/05-03-airbnb-arbitrage-example.md)
  - **IF** you want a different story **THEN** ask for "a second version of the brief" in the same chat with a one-paragraph narrator premise; keep V1. [05-04 10:53–12:32](../lessons/05-04-blood-sugar-supplement-example.md)
- **See also:** [brief-generator framework](../frameworks/brief-generator.md) · [rmbc-pipeline](rmbc-pipeline.md) · [unified-research-document](unified-research-document.md) · [unique-mechanism](unique-mechanism.md) · [claude-project-recipe](claude-project-recipe.md) · [templates library](../libraries/templates.md) · [prompts library](../libraries/prompts.md)

## Definition
The brief is "the command center": "a 25 point document" built from the mechanism, the research and product details, which the LLM uses to write "VSLs, ads, advertorials, email sequences, everything else". [01-01 12:56–13:54](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) It does what the RMBC I brief did ("getting the information onto a piece of paper that you, a human, would need to write the copy") but "it's more in-depth ... you won't be filling out a lot of it ... And you're doing it to give to an LLM to write copy." [05-01 01:03–02:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)

### Old vs new
| | Classic RMBC brief | Brief 2.0 |
|---|---|---|
| Fields | 12 | 25 |
| Reader | Human copywriter | LLM (field 6: "enough detail so that when given to an LLM, it could write this whole section without struggling") |
| Who fills it | You | Brief Generator Claude Project; you revise |
| Dropped | Paradoxical question, metaphor ("AI is quite good at metaphors"), headline ideas, upsell ideas | — |
| Added | — | Solved-state picture (4), UM nickname (7), ingredients + 2–3 studies (8), speakers and brand partnership (12–14), testimonials (15), credibility builders (16), price/options/guarantee/bonuses/scarcity (17–22), future-paced results (23), objections (24), hooks/big ideas to test (25) |

[05-01 02:03–16:20](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md). Verbatim templates of both: [05-01 Prompts](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md); also in the [templates library](../libraries/templates.md).

### The 25 fields: source and compliance status
| # | Field (short) | Comes from | Compliance status for our brands |
|---|---|---|---|
| 1 | Audience | Unified research doc §1 (with awareness stage) | OK |
| 2 | Pain points, short/long term; 1–3 huge | Unified doc §2 | OK (real customer language preferred) |
| 3 | Big promises about the sales copy (teaser) | Derived from pains | OK if a teaser, not a product claim |
| 4 | Solved state: physical, emotional, social, psychological | Unified doc hopes/dreams | OK as aspiration; no outcome guarantees |
| 5 | Existing solutions and why they fail | Unified doc §4 | No disparaging false claims about competitors |
| 6 | UMP + UMS in detail | UM doc | Every physiology/finance statement `[VERIFY]` |
| 7 | UM nickname ("7 second bowel releasing ritual", "30 second breakfast hack", "Paper Flipping") | UM doc / ideation | OK; name only |
| 8 | Ingredients + 2–3 studies each | Ingredient research [02-05](../lessons/02-05-ingredient-deep-research.md) | Open each study; check dose, population, human data |
| 9 | Bold product claims | Generator | Highest risk: substantiation required; structure/function wording for supplements |
| 10 | Product: features/benefits or fascinations | Product page | OK if factual |
| 11 | Background story + story of discovery (hero's journey) | Generator / you | Real story only, or labelled dramatization |
| 12 | Main speaker + credibility | You | Real, consenting person only |
| 13 | Second speaker / expert | You | Real, credentialed, consenting expert only |
| 14 | Brand partnership | You | Real only |
| 15 | Testimonials / social proof | You | Real reviews only; never generated |
| 16 | Credibility builders for the opening | You | Documented or removed (see hard stop) |
| 17–19 | Retail price, VSL price, options | Product page / offer | Real prices; no fake "normal price" anchors |
| 20 | Guarantee | Offer | Real terms only |
| 21 | Bonuses | Offer | Real only |
| 22 | Scarcity | Offer | Real deadlines/stock only; no fake countdowns |
| 23 | Future-paced results | Generator | Typicality disclosure if results implied |
| 24 | Objections + answers | Unified doc §3 | OK |
| 25 | Hooks / big ideas to test in the lead | Generator / hook research | OK; hooks inherit claim rules |

Field list from [05-01](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md); "comes from" and status columns are (derived).

## Why it matters
- It ties the pipeline together: "It will tie together what we did so far. It will also give you what you need to just print all kinds of copy." [05-01 01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
- "This is essential, essential for RMBC II." [08-01 03:25–03:53](../lessons/08-01-rmbc-ii-mid-course-recap.md)
- Several fields are "really like instructions for the LLM as much as for you" [05-01 08:08](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md): field 25 seeds VSL leads; 12–14 fix the narrator so drafts don't drift.
- Even with only ingredient research, running the generator "a couple of times" yields usable pain points, promises, nicknames and story structures to react to. [05-04 09:53–10:23](../lessons/05-04-blood-sugar-supplement-example.md)

## How to use (steps)
1. **Build the project once:** name "RMBC II Brief Generator"; instructions = the verbatim generator text ("Your Job is to Create New Briefs for Copywriting Projects ... For anything where you don't have information, you can use placeholders to start."); knowledge = blank "The New Brief" + classic VSL outline ("mostly for reference"). [05-02 00:00–01:02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
2. **Per product, in chat:** "I want your help generating a new brief for [brand]'s [product]. Here is a current product page ... [URL]. Additionally, I am attaching a UMP and also some market research ... I'm also including a document with the ingredients and relevant studies. Please go ahead and get started now." Web search on. [05-02 Prompts B](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
3. **No page?** Attach an offer overview doc with the client's real program facts. [05-03 01:04](../lessons/05-03-airbnb-arbitrage-example.md)
4. **Check attachment use**; if generic, re-upload and name it. [05-05 09:52](../lessons/05-05-financial-promo-example.md)
5. **Save V1** to a doc. [05-02 17:46](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
6. **Revise by chat:** "This was great overall ... Here are a few tweaks": pricing shown in the VSL vs below it, main speaker, expert role, brand partnership, bonuses yes/no. [05-02 19:03–20:19](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
7. **Fix weak sections:** e.g. "rewrite the mechanism without [the jargon]"; add a big idea if missing. [05-02 07:58](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); [08-01 07:58–08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)
8. **Claim pass:** run [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md); every unverifiable item in fields 6, 8, 9, 11–23 → `[VERIFY: …]` or delete.
9. **Hand off** to the length project: ask for an outline and estimated length first. [05-02 23:00–25:57](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) → [claude-project-recipe](claude-project-recipe.md)

## Examples
| Run | Inputs | What the lesson shows | Compliance note | Source |
|---|---|---|---|---|
| Opal Beauty Unity Eye Serum | Product URL + UMP + market research + ingredient doc | Full 25 fields; revision (one-time price in VSL, speaker "Laura", expert "Dr. Schilling", no bonuses); then medium/short/hook/long drafts | Laura persona details are "not actually true ... I'm using this mostly for an example"; Harvard/97%/45% figures unsourced | [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Airbnb arbitrage coaching | UMP + unified research + Gemini-made offer overview | Brief for a no-page offer; proof listed as *categories* of assets needed | "$12,000+ monthly passive income", "150+ property owners", "Featured in BiggerPockets" are generated; income claims | [05-03](../lessons/05-03-airbnb-arbitrage-example.md) |
| Blood-sugar supplement | Ingredient/studies doc only + "use placeholders" | Generator invented audience, mechanism (GLUT4 theme), story; V2 doctor-told version | "reversing type 2 diabetes", "better than most prescription medications", "Big Pharma is trying to hide it": disease and conspiracy claims; structure only | [05-04](../lessons/05-04-blood-sugar-supplement-example.md) |
| Financial newsletter | Winning VSL transcript → LLM-invented offer → brief → long VSL | Attachment-ignored recovery; "swipe the structure" | Stefan: "I know it's not compliant"; cancer/Alzheimer's cures, 5x–10x returns, fictional "Dr. Elias Vance": hard stop | [05-05](../lessons/05-05-financial-promo-example.md) |

All four: structure only; claims not reusable.

## Common mistakes
- **Skipping the brief for short form.** "People who didn't do long form copy kind of skipped over it." [05-01 01:03](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
- **Merging teaser promises (3) with product claims (9)**, which makes the lead sell the product too early. [05-01 11:09](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)
- **Brand name inside the script** ("founder at Opal Beauty"): "you probably wouldn't mention Opal Beauty in the VSL". [05-02 26:59](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
- **Thin product section** for info offers: upload the longer offer doc again when writing the VSL. [05-03 06:34](../lessons/05-03-airbnb-arbitrage-example.md)
- **Treating placeholders as facts.** "I will switch out everything later" [05-04 00:33](../lessons/05-04-blood-sugar-supplement-example.md): agents must actually switch them out or stop.
- **Overwriting V1** when exploring a new story; generate V2 alongside. [05-04 12:32](../lessons/05-04-blood-sugar-supplement-example.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | "Command center"; live generator demos | 11:29–16:51 |
| [05-01 Old vs new brief](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) | Both templates; every new field explained | 00:00–16:20 |
| [05-02 Brief generator + Unity](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Project instructions, per-product prompt, revision, hand-off | 00:00–47:10 |
| [05-03 Airbnb arbitrage](../lessons/05-03-airbnb-arbitrage-example.md) | No-page offer | 01:04–08:43 |
| [05-04 Blood sugar](../lessons/05-04-blood-sugar-supplement-example.md) | Ingredients-only input; V1/V2 narrators | 00:33–12:32 |
| [05-05 Financial promo](../lessons/05-05-financial-promo-example.md) | Offer ideation from a winner; attachment recovery | 00:00–16:30 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | B-stage steps and output | 03:25–03:53; 05:28–06:47 |

## Cross-course notes
- **Evolve Copywriting** has a short-form creative brief path ([video-ad-script-workflow](../../../evolve/copywriting/frameworks/video-ad-script-workflow.md)); RMBC's brief is a long-form offer brief that also feeds short VSLs. **Agent default:** for a single UGC/short ad, use the Evolve or Tether brief; for any VSL, advertorial, PDP or multi-asset funnel, build Brief 2.0 first and derive short-ad briefs from fields 2, 6, 7 and 25.
- **Evolve Start Here** [product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md) warns "AI in general makes educated guesses"; it matches the placeholder risk here.
- **Tether Lab** [creator brief playbook](../../../../playbooks/creator-brief.md) is the production brief for a creator; RMBC's brief is the copy brief upstream of it.

## Related
[rmbc-pipeline](rmbc-pipeline.md) · [unified-research-document](unified-research-document.md) · [unique-mechanism](unique-mechanism.md) · [claude-project-recipe](claude-project-recipe.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [compliance-red-flags](compliance-red-flags.md) · [classic-vsl-structure](classic-vsl-structure.md) · [brief-generator](../frameworks/brief-generator.md)
