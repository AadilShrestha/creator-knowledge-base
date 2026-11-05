---
title: "Unified Research Document"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-02-competitor-research-walkthrough-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-03-psychographic-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
tags: [rmbc-ii, research, unified-research-document, competitor-research, psychographics, ingredient-research, claude]
updated: 2026-11-02
---

# Unified Research Document
> The R-stage hand-off: three deep-research reports (product-market awareness, competitors, psychographics) merged by one Claude prompt into a short four-section brief (demographics, psychographics with language and promises, objections, failed existing solutions) that is attached to every later copy prompt; ingredient research stays a separate companion doc.

## 🤖 Agent use
- **Use when:** the awareness, competitor and psychographic reports exist and you need one compact context file for the UM, brief, VSL, advertorial, ad, PDP or email prompts.
- **Inputs → outputs:** 3–4 PDFs (awareness report, best competitor summary, Claude-merged psychographic summary, optional descriptive-language doc) + niche/product/region line + target awareness segments → one "Unified Research Brief" with four numbered sections; separately, the ingredient claim doc for formulated products.
- **Rules:**
  - **DO** use the merge prompt as written; "you can honestly just copy and paste it in as is most of the time". [02-04 01:25; 07:55–08:20](../lessons/02-04-unified-research-process.md)
  - **DO** change the highlighted segment line per market (default "Problem Aware and Solution Aware"; GLP-1: solution aware; biz-opp: problem aware and even unaware). [02-04 02:10–03:10](../lessons/02-04-unified-research-process.md)
  - **DON'T** ask for TAM, market size, growth, revenue or strategy: "good knowledge ... as a marketer, but not for direct response copy". [02-04 06:48](../lessons/02-04-unified-research-process.md)
  - **DON'T** add an "anything else relevant" item; it was removed after testing. [02-04 07:17](../lessons/02-04-unified-research-process.md)
  - **DO** label in-prompt examples "from a DIFFERENT PRODUCT in a DIFFERENT NICHE" so the model copies format, not content. [02-04 03:10–04:10](../lessons/02-04-unified-research-process.md)
  - **DO** strip sources to plain text (Ctrl/Cmd+Shift+V into a new doc, delete works-cited, export PDF) if Claude errors. [02-04 16:39–21:42](../lessons/02-04-unified-research-process.md)
  - **IF** Claude still fails or is rate-limited **THEN** retry in an hour or run the same prompt on Poe with Claude Sonnet 4; Gemini's merge "was just not that good". [02-04 21:42–24:24](../lessons/02-04-unified-research-process.md)
  - **DO** override the generated avoid-list and timelines with your product's real facts ("if you got faster results, I would talk about faster results"). [02-04 14:03–15:36](../lessons/02-04-unified-research-process.md)
  - **DON'T** treat "Primary Promises" as claims for your product. They are LLM-synthesised leads; each needs `[VERIFY: …]` and real substantiation. (derived; [02-04 Compliance flags](../lessons/02-04-unified-research-process.md))
  - **DON'T** keep the weight-loss example lines in the prompt ("Lose up to 71 lbs of fat fast", "fat cell hypothermia"); replace with compliant, niche-neutral format examples. Structure only; claims not reusable. [02-04 Compliance flags](../lessons/02-04-unified-research-process.md)
- **See also:** [deep-research-workflow](../frameworks/deep-research-workflow.md) · [product-market-awareness](product-market-awareness.md) · [brief-2-0](brief-2-0.md) · [rmbc-pipeline](rmbc-pipeline.md) · [prompts library](../libraries/prompts.md) · [Evolve: research doc](../../../evolve/start-here/concepts/research-doc.md)

## Definition
"One very simplified document that we can use as we go to generate various forms of copy with LLMs", built from "the different research pieces we've pulled thus far around product and market awareness, competitor research, and psychographic research". [02-04 00:00–00:29](../lessons/02-04-unified-research-process.md) In 01-01 Stefan calls the goal one "perfect document that is all the kind of research information we would need to write great copy". [01-01 06:33–07:24](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)

### Inputs (what each source contributes)
| Input | Produced by | What it adds that the others don't | Read-only-this | Source |
|---|---|---|---|---|
| Product-market awareness report | Deep-research "Prompt #1" in Gemini + ChatGPT | Target stage(s) and size of the education gap | TAM, % per stage, majority verdict | [02-01](../lessons/02-01-product-market-awareness.md) |
| Competitor summary | Competitor deep-research prompt (+ phrase-mining add-on); best single LLM | Claims/core messaging, prices, what customers love and dislike, repeated phrases | "core messaging, pricing, and what customers love and dislike. I don't even care about the philosophy" [13:14–14:21] | [02-02](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| Psychographic summary (Claude-merged) | 22-question questionnaire in 2–3 LLMs (blocks: Demographic Insights, Other Existing Solutions, Curiosity, Corruption) → Claude merge | Beliefs, enemies, "in their own words" quotes, forgotten-cure and corruption story leads | Full read once when new to a market | [02-03](../lessons/02-03-psychographic-research.md) |
| Descriptive-language doc (optional) | Follow-up quotes prompt in the psychographic chat | Extra pain/desired-outcome customer language | — | [02-03 v2 42:40–47:07](../lessons/02-03-psychographic-research.md) |
| **Not merged:** ingredient research | Perplexity (default) and/or ChatGPT with market overview + mechanism attached | Per-ingredient, study-tied claims split into mechanism-supporting and pain-point claims | — | [02-05](../lessons/02-05-ingredient-deep-research.md) |

The ingredient doc goes to the brief generator alongside the unified doc ("Upload Unified Research Doc, UM Doc, Ingredient Research (Optional)"). [08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md)

### Output schema
| # | Section (prompt wording) | Sub-fields seen in outputs | Feeds |
|---|---|---|---|
| 1 | Target Market Demographic Overview: "Focus on people who fall into the Problem Aware and Solution Aware Market segments primarily" | Age band and peak, generation, income, life stage/role, digital behaviour (problem-aware vs solution-aware searches, platforms, reliance on reviews) | Brief field 1 "Audience" [05-02 04:12](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); narrator's journey |
| 2 | Target Market Psychographic Overview | Pain points (physical/visual, emotional, practical) · hopes and dreams / ideal future state · how they view themselves · language to use / avoid · Primary Promises (efficacy, emotional, lifestyle) | Hooks, leads, future pacing, word choice |
| 3 | Biggest objections and how to address them | e.g. "I've tried everything, nothing works", too expensive, will irritate, "peptides are marketing and hype" | Objection handling, FAQ, close |
| 4 | Existing solutions tried and why they are inadequate | Mass-market, prestige, budget actives, professional treatments, DIY | UMP / "dismissing alternatives"; mechanism contrast |

Derived from [02-04 08:20–16:39](../lessons/02-04-unified-research-process.md). Verbatim merge prompt: [02-04 Prompts](../lessons/02-04-unified-research-process.md) and the [prompts library](../libraries/prompts.md).

## Why it matters
- One context file instead of three long reports keeps every downstream Claude Project consistent and within limits. [02-04 00:29](../lessons/02-04-unified-research-process.md)
- Section 4 powers the core VSL move: "In the vast majority of copy, you're kind of talking about alternative solutions and dismissing them as not being adequate"; the obvious objection ("I tried other products" / "I'm pretty happy, why switch?") is answered with a unique mechanism. [02-04 15:36–16:39](../lessons/02-04-unified-research-process.md)
- It is the first upload to the brief generator; the brief's audience field is copied from it ("how did we get that? From our unified research document"). [05-02 04:12](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)

## How to use (steps)
1. Collect the reports; pick the best competitor run (he skipped a weak Perplexity competitor report). [02-04 07:17–07:55; 18:20–20:15](../lessons/02-04-unified-research-process.md)
2. Convert each to plain text, remove citations/images, export as PDF. [02-04 17:13–18:20](../lessons/02-04-unified-research-process.md)
3. Fill niche/product/region (optional; leaving them blank "didn't really matter") and set the segment line from the awareness verdict. [02-04 01:25–03:10](../lessons/02-04-unified-research-process.md)
4. Replace the in-prompt weight-loss examples with compliant format examples (derived).
5. New Claude chat → paste prompt → attach PDFs → run. Fallback: Poe/Claude Sonnet 4. [02-04 08:20; 23:12–24:24](../lessons/02-04-unified-research-process.md)
6. Critique: "You do need to be a critical thinker still even for LLMs." Edit avoid-list, timelines, promises. [02-04 14:03–15:36](../lessons/02-04-unified-research-process.md)
7. Mark every promise, stat, quote and story as `[VERIFY: source]` until checked against real proof (derived; LLM "quotes" drift between passes [02-03](../lessons/02-03-psychographic-research.md)).
8. Save as "Unified Research Document – [product]" and attach it (not the raw reports) to the UM, brief and copy projects. [02-04 27:20](../lessons/02-04-unified-research-process.md)
9. Formulated product? Run ingredient research twice (without and with the mechanism), merge into one PDF, and keep it as the companion doc. [02-05 06:13–07:19](../lessons/02-05-ingredient-deep-research.md)

## Examples
| Run | What happened | Source |
|---|---|---|
| Peptide eye serum, US women 40+ | Four PDFs → "Unified Research Brief: Peptide Eye Serum Campaign for U.S. Women 40+": sandwich-generation "chief medical officer", dimensionalised pain groups, use/avoid lists, objections, six failed solution types | [02-04 08:20–16:39](../lessons/02-04-unified-research-process.md) |
| Airbnb arbitrage coaching | "maximum image count" error → plain-text rebuild → still failing → Poe/Claude Sonnet 4 succeeded; output includes biz-opp use/avoid lexicon ("proven system, step-by-step blueprint, no BS" vs "get rich quick, guru, guaranteed success") | [02-04 16:39–27:58](../lessons/02-04-unified-research-process.md) |
| First untuned run | Returned TAM, growth and revenue; fixed by numbering the four items and adding the exclusion sentence | [02-04 06:48–07:17](../lessons/02-04-unified-research-process.md) |
| Instructor's avoid-list override | Avoid-list said "instant transformation" is desperate; "If you're selling like an instant eye lift ... I might still speak to that" | [02-04 14:33](../lessons/02-04-unified-research-process.md) |

Compliance: generated promises such as "Visibly reduced crow's feet ... in 4 to 8 weeks", "Clinically proven peptide technology that rebuilds collagen from within" and biz-opp lines like "Escape the paycheck-to-paycheck cycle within 6-12 months" are course outputs. Structure only; claims not reusable.

## Common mistakes
- **Feeding raw reports to every copy prompt** instead of the merged doc. [02-04 00:29](../lessons/02-04-unified-research-process.md)
- **Keeping market sizing in the doc**: it dilutes direct-response context. [02-04 06:48](../lessons/02-04-unified-research-process.md)
- **Leaving prompt examples that steer content**: in psychographics, Gemini returned "Ancel Keys" for skincare because the example named him. [02-03 v2 23:50–26:33](../lessons/02-03-psychographic-research.md)
- **Accepting competitor numbers**: price, revenue and guarantee data differed across three models for the same brand. [02-02](../lessons/02-02-competitor-research-walkthrough-and-examples.md)
- **Shipping ingredient claims unchecked**: the Perplexity output still cited brand blogs and supplier pages despite the "NCBI only" rule. [02-05 02:32; 04:43](../lessons/02-05-ingredient-deep-research.md)
- **Skipping research because you're modelling a winner.** Stefan admits you "can conceivably shortcut a lot of this research and still get a good copy" when modelling a proven VSL [02-04 04:10–05:11](../lessons/02-04-unified-research-process.md). Agent default: still build the doc; customer language and objections must come from research, not the swipe.

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Course overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | "Combine them into one" | 06:33–07:24 |
| [02-01 Product-market awareness](../lessons/02-01-product-market-awareness.md) | Input 1 | whole lesson; v2 28:20 (save for merge) |
| [02-02 Competitor research](../lessons/02-02-competitor-research-walkthrough-and-examples.md) | Input 2 | 00:28–01:51; 13:14–14:21 |
| [02-03 Psychographic research](../lessons/02-03-psychographic-research.md) | Input 3 (+ language doc) | v1 00:00; v2 35:49–48:14 |
| [02-04 Unified research process](../lessons/02-04-unified-research-process.md) | The merge prompt, outputs, troubleshooting | 00:00–27:58 |
| [02-05 Ingredient deep research](../lessons/02-05-ingredient-deep-research.md) | Companion doc | 00:00–07:51 |
| [05-02 Brief generator](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Doc as brief input | 04:12 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | Named R-stage output | 05:28–06:47 |

## Cross-course notes
- **Evolve Start Here** [research doc](../../../evolve/start-here/concepts/research-doc.md): a hand-filled per-brand "brand Bible" (V4.0) with ad-copy bank, phrase bank, product, problems/solutions, avatars, FAQ, competitors, ad-account audit. **RMBC** generates a shorter LLM-synthesised brief from deep-research reports. They agree that research precedes writing and that failed alternatives and objections are core. **Difference:** Evolve sources language from real reviews, Reddit and calls; RMBC's language comes from LLM reports. **Agent default:** if an Evolve research doc exists, upload it as an extra PDF to the RMBC merge; take customer quotes only from the Evolve doc or real sources, never from the LLM reports unverified.
- **Tether Lab** [customer research stack](../../../../frameworks/customer-research-stack.md) covers primary customer research (reviews, surveys); use it to verify the unified doc's "in their own words" lines.
- **Evolve Copywriting** [labels and customer language](../../../evolve/copywriting/concepts/labels-and-customer-language.md) and [beliefs](../../../evolve/copywriting/concepts/beliefs.md) map onto sections 2 and 3.

## Related
[rmbc-pipeline](rmbc-pipeline.md) · [product-market-awareness](product-market-awareness.md) · [unique-mechanism](unique-mechanism.md) · [brief-2-0](brief-2-0.md) · [compliance-red-flags](compliance-red-flags.md) · [deep-research-workflow](../frameworks/deep-research-workflow.md) · [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md)
