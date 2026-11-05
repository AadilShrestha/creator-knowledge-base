---
title: "RMBC II prompt library: every prompt and Claude Project instruction, by pipeline stage"
type: library
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guest Max Finn (12-04: R9, AD4, AD5)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-02-competitor-research-walkthrough-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-03-psychographic-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-01-unique-mechanisms-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-02-ump-ideation-with-llms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-01-vsls-section-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-04-vsl-background-stories-and-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-09-short-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-03-airbnb-arbitrage-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-04-blood-sugar-supplement-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-04-tiktok-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
tags: [rmbc-ii, library, prompts, claude-projects, llm, research, unique-mechanism, brief, vsl, hooks, advertorial, pdp, upsell, email, funnel]
updated: 2026-11-02
---

# RMBC II prompt library
> Every LLM prompt, follow-up and Claude Project instruction in RMBC II, grouped by pipeline stage (Research → Mechanism → Brief → Copy → funnel assets). Each entry gives the verbatim text, its inputs, the lesson and timestamp, its verbatim status and the known failure modes, with a compliant fix wherever the course prompt asks for invented proof.

## 🤖 Agent use
- **Use when:** you are at any LLM step of the RMBC pipeline: market research, mechanism ideation or ranking, brief generation, setting up a Claude Project, outlining or drafting a VSL, generating hooks, swiping an advertorial or PDP structure, writing ad captions, upsell scripts or email sequences, or giving an LLM feedback on a draft.
- **Inputs → outputs:** the stage you are at → the [quick-find table](#quick-find) → the entry → paste the fenced prompt, fill its placeholders with **real** inputs (product facts, offer, unified research doc, mechanism doc, brief) → LLM output → run the [claim audit](../rubrics/llm-output-claim-audit.md) before anything ships.
- **Rules:**
  - **DO** paste course prompts verbatim and change only the placeholders. Stefan's prompts are deliberately plain; the leverage is in the attachments (research doc, UM doc, brief, example files). [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DO** run the outline-first gate on every long asset: ask for an outline (and an estimated length), edit it, then say "write it". [07-01 v1 28:33–40:12](../lessons/07-01-long-form-vsl.md)
  - **DO** keep the "don't rush or condense… whenever you run out of space just prompt me and I'll tell you to continue" line in project instructions and draft prompts; the continuation message is just "continue" / "yes please continue". [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) · [14-02](../lessons/14-02-upsells-case-studies.md)
  - **DO** attach the brief or research doc *with* the prompt. Two course runs failed because the attachment was missing or ignored ([B6](#b6-recovery-when-the-model-ignores-the-attachment), [V24](#v24-attach-the-forgotten-brief-and-lock-earlier-sections)).
  - **DO** swap the seed examples inside a prompt for your own niche. Examples bias output: Gemini picked Ancel Keys because the prompt named him [02-03 v2 24:06](../lessons/02-03-psychographic-research.md); skincare seed hooks leaked into the Airbnb run [07-01 v5 54:02](../lessons/07-01-long-form-vsl.md).
  - **DON'T** ship any testimonial, doctor, study, statistic, review count, timeline result, scarcity or price "value" that an LLM produced. Course prompts often ask for these; every entry with that risk carries a **⚠ compliance** note with the compliant edit. Repo rule: real proof only, otherwise `[VERIFY: …]`.
  - **DON'T** treat a *reconstructed* or *partial* prompt as Stefan's exact wording. Use it as a pattern; the status line says which it is.
  - **IF** a prompt is marked *derived* **THEN** it was built by this KB from the lessons, not by Stefan; use it, but don't cite it as course text.
  - **IF** Claude starts coding or making an artifact when you want copy **THEN** use [D5](#d5-stop-claude-from-coding-the-page). **IF** it cannot fetch a URL **THEN** paste the copy plus an above-the-fold screenshot ([D7](#d7-fallback-when-claude-cannot-fetch-the-page)).
- **See also:** [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Templates](templates.md) · [Hooks](hooks.md) · [Rules](rules.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [Evolve Start Here prompts](../../../evolve/start-here/libraries/prompts.md) · [Tether Lab prompt index](../../../../libraries/prompts.md)

## How to read an entry
- **Status** uses the lesson page's own label: **verbatim** (course document, or text fully legible on screen), **partial** (verbatim but cut off on screen or truncated in the file), **reconstructed** (spoken; wording approximate, use as a pattern), **derived** (built by this KB, not a course asset).
- Placeholders keep the course's own style (`_PRODUCT_`, `PRODUCT`, `__Document Type__`, `[link]`). Square brackets added by the lesson pages mark a fill-in or a note about missing text.
- Timestamps are `[mm:ss]` in the lesson video; `v2`, `v3`… mark later videos of the same lesson. "doc" means the prompt comes from a course file, named in the source line.
- Typos in course files are kept on purpose (the lesson pages flag them).
- Structures and outlines that are not themselves prompts (classic VSL outline, short-VSL structures, advertorial, PDP, upsell and email skeletons, webinar scripts, checkout microcopy) live in [templates.md](templates.md). This page includes a template only when it is pasted into a prompt or uploaded as project knowledge and is not a VSL, advertorial, email or upsell structure.

## Quick-find
| Stage | ID | Prompt | Lesson | Status |
|---|---|---|---|---|
| Research | R1 | [Market awareness deep research](#r1-market-awareness-deep-research) | 02-01 | verbatim |
| Research | R2 | [Competitor deep research](#r2-competitor-deep-research) | 02-02 | verbatim |
| Research | R3 | [Psychographic deep research](#r3-psychographic-deep-research) | 02-03 | verbatim |
| Research | R4 | [Merge several deep-research reports into one](#r4-merge-several-deep-research-reports-into-one) | 02-03 | verbatim |
| Research | R5 | [Follow-up for the market's own words](#r5-follow-up-for-the-markets-own-words) | 02-03 | verbatim |
| Research | R6 | [Unified research document](#r6-unified-research-document) | 02-04 | verbatim |
| Research | R7 | [Ingredient deep research (claims tied to studies)](#r7-ingredient-deep-research-claims-tied-to-studies) | 02-05 | verbatim |
| Research | R8 | [Header for a combined ingredient research file](#r8-header-for-a-combined-ingredient-research-file) | 02-05 | verbatim |
| Research | R9 | [Ultimate universal target avatar deep research (guest)](#r9-ultimate-universal-target-avatar-deep-research-guest) | 12-04 | verbatim |
| Mechanism | M1 | [One-off UMP ideation](#m1-one-off-ump-ideation) | 03-02 · 03-01 | verbatim |
| Mechanism | M2 | [More like number three](#m2-more-like-number-three) | 03-02 | reconstructed |
| Mechanism | M3 | [Mechanism evaluation and ranking](#m3-mechanism-evaluation-and-ranking) | 03-03 | verbatim |
| Mechanism | M4 | [Mechanism expansion into VSL copy](#m4-mechanism-expansion-into-vsl-copy) | 03-04 | verbatim |
| Mechanism | M5 | [Reframe the mechanism after the first version](#m5-reframe-the-mechanism-after-the-first-version) | 03-03 | reconstructed |
| Mechanism | M6 | [Combine several mechanisms into one](#m6-combine-several-mechanisms-into-one) | 03-04 | verbatim |
| Mechanism | M7 | [Correct an awareness mismatch in the output](#m7-correct-an-awareness-mismatch-in-the-output) | 03-04 | verbatim |
| Mechanism | M8 | [Pick the mechanism names](#m8-pick-the-mechanism-names) | 03-04 | verbatim/partial |
| Mechanism | M9 | [Ask for more believable names and analogies](#m9-ask-for-more-believable-names-and-analogies) | 03-04 | reconstructed |
| Mechanism | M10 | [Weird UMP brainstorm (AgentGPT)](#m10-weird-ump-brainstorm-agentgpt) | 03-05 | verbatim |
| Mechanism | M11 | [Mechanism definition block (input)](#m11-mechanism-definition-block-input) | 03-05 | derived |
| Brief | B1 | [Generate a new brief](#b1-generate-a-new-brief) | 05-02 · 05-03 · 05-05 | verbatim |
| Brief | B2 | [Placeholder brief from ingredients only](#b2-placeholder-brief-from-ingredients-only) | 05-04 | verbatim |
| Brief | B3 | [Revise the brief (pricing, speaker, bonuses)](#b3-revise-the-brief-pricing-speaker-bonuses) | 05-02 | reconstructed |
| Brief | B4 | [Correct the audience](#b4-correct-the-audience) | 05-04 | verbatim |
| Brief | B5 | [Second brief version told from the doctor](#b5-second-brief-version-told-from-the-doctor) | 01-01 | verbatim |
| Brief | B6 | [Recovery when the model ignores the attachment](#b6-recovery-when-the-model-ignores-the-attachment) | 05-05 | partial |
| Brief | B7 | [Draft an offer overview with an LLM (training examples only)](#b7-draft-an-offer-overview-with-an-llm-training-examples-only) | 05-03 | reconstructed |
| Brief | B8 | [Ideate a hypothetical offer from a winning VSL (training examples only)](#b8-ideate-a-hypothetical-offer-from-a-winning-vsl-training-examples-only) | 05-05 | reconstructed |
| Brief | B9 | [Update the brief with chosen big ideas](#b9-update-the-brief-with-chosen-big-ideas) | 07-01 | verbatim |
| Brief | B10 | [The New Brief (project knowledge file)](#b10-the-new-brief-project-knowledge-file) | 05-01 | verbatim |
| Claude Project instructions | P1 | [Unique Mechanisms project](#p1-unique-mechanisms-project) | 03-05 | verbatim |
| Claude Project instructions | P2 | [Brief Generator project](#p2-brief-generator-project) | 05-02 | verbatim |
| Claude Project instructions | P3 | [Long Form VSL Generator project](#p3-long-form-vsl-generator-project) | 07-01 | verbatim |
| Claude Project instructions | P4 | [Medium Length VSL Generator project](#p4-medium-length-vsl-generator-project) | 06-01 | verbatim |
| Claude Project instructions | P5 | [3-7 Minute VSL Generator project](#p5-3-7-minute-vsl-generator-project) | 06-01 | verbatim |
| Claude Project instructions | P6 | [Short Length VSL Generator project](#p6-short-length-vsl-generator-project) | 06-01 | verbatim |
| Claude Project instructions | P7 | [Hook-heavy Meta ads project (ADHD Super-Hook)](#p7-hook-heavy-meta-ads-project-adhd-super-hook) | 04-10 | verbatim |
| Claude Project instructions | P8 | [Advertorials project](#p8-advertorials-project) | 09-02 | verbatim |
| Claude Project instructions | P9 | [PDPs (no project)](#p9-pdps-no-project) | 10-01 | none |
| Claude Project instructions | P10 | [Meta captions generator project](#p10-meta-captions-generator-project) | 12-01 | verbatim |
| Claude Project instructions | P11 | [Upsell Generator project (longer scripts)](#p11-upsell-generator-project-longer-scripts) | 14-03 | verbatim |
| Claude Project instructions | P12 | [Email Sequence Generator project](#p12-email-sequence-generator-project) | 15-05 | verbatim |
| VSL drafting and editing | V1 | [Long VSL outline request](#v1-long-vsl-outline-request) | 07-01 | verbatim |
| VSL drafting and editing | V2 | [Lazy swipe test (model one VSL closely)](#v2-lazy-swipe-test-model-one-vsl-closely) | 07-01 | verbatim |
| VSL drafting and editing | V3 | [Model a named VSL from project knowledge (financial)](#v3-model-a-named-vsl-from-project-knowledge-financial) | 05-05 | partial |
| VSL drafting and editing | V4 | [Outline feedback: promise, future pace, hold back the brand](#v4-outline-feedback-promise-future-pace-hold-back-the-brand) | 07-01 | reconstructed |
| VSL drafting and editing | V5 | [Attach the classic structure and revise the outline](#v5-attach-the-classic-structure-and-revise-the-outline) | 07-01 | verbatim |
| VSL drafting and editing | V6 | [Make the narrator recount the expert's reveal](#v6-make-the-narrator-recount-the-experts-reveal) | 07-01 · 07-02 | verbatim |
| VSL drafting and editing | V7 | [Draft the same outline in a second model](#v7-draft-the-same-outline-in-a-second-model) | 07-01 | verbatim |
| VSL drafting and editing | V8 | [Write the VSL from the approved outline](#v8-write-the-vsl-from-the-approved-outline) | 07-01 | verbatim |
| VSL drafting and editing | V9 | [Fix the mechanism focus in a draft](#v9-fix-the-mechanism-focus-in-a-draft) | 07-01 | reconstructed |
| VSL drafting and editing | V10 | [Patch ingredients into a multi-step solution](#v10-patch-ingredients-into-a-multi-step-solution) | 07-01 | reconstructed |
| VSL drafting and editing | V11 | [Book-a-call VSL outline (problem aware)](#v11-book-a-call-vsl-outline-problem-aware) | 07-01 | partial |
| VSL drafting and editing | V12 | [Fix bridges and logic gaps in a draft](#v12-fix-bridges-and-logic-gaps-in-a-draft) | 07-01 | reconstructed |
| VSL drafting and editing | V13 | [Doctor-led outline from brief plus classic outline, then ingredient patches](#v13-doctor-led-outline-from-brief-plus-classic-outline-then-ingredient-patches) | 07-01 | reconstructed |
| VSL drafting and editing | V14 | [Outline with a length estimate](#v14-outline-with-a-length-estimate) | 07-02 | verbatim |
| VSL drafting and editing | V15 | [Remix the outline with the classic structure](#v15-remix-the-outline-with-the-classic-structure) | 07-02 | verbatim |
| VSL drafting and editing | V16 | [Swap the spokesperson and background story](#v16-swap-the-spokesperson-and-background-story) | 07-02 | reconstructed |
| VSL drafting and editing | V17 | [Cut an existing VSL to a target length](#v17-cut-an-existing-vsl-to-a-target-length) | 07-02 · 07-04 | verbatim/reconstructed |
| VSL drafting and editing | V18 | [Nine-minute book-a-call outline (problem aware)](#v18-nine-minute-book-a-call-outline-problem-aware) | 07-02 | partial |
| VSL drafting and editing | V19 | [Medium VSL agent template (derived)](#v19-medium-vsl-agent-template-derived) | 07-02 | derived |
| VSL drafting and editing | V20 | [Five 3-7 minute concepts from a brief](#v20-five-3-7-minute-concepts-from-a-brief) | 07-03 | verbatim |
| VSL drafting and editing | V21 | [Pick a hook and ask for a timed outline](#v21-pick-a-hook-and-ask-for-a-timed-outline) | 07-03 | verbatim |
| VSL drafting and editing | V22 | [Shorter sibling of a finished ad](#v22-shorter-sibling-of-a-finished-ad) | 07-03 | reconstructed |
| VSL drafting and editing | V23 | [Video-ad outline from a brief and an opening hook](#v23-video-ad-outline-from-a-brief-and-an-opening-hook) | 07-03 | verbatim |
| VSL drafting and editing | V24 | [Attach the forgotten brief and lock earlier sections](#v24-attach-the-forgotten-brief-and-lock-earlier-sections) | 07-03 | verbatim |
| VSL drafting and editing | V25 | [Pre-empt an objection, then write](#v25-pre-empt-an-objection-then-write) | 07-03 | verbatim |
| VSL drafting and editing | V26 | [Fix a "Nope" sequence that makes false denials](#v26-fix-a-nope-sequence-that-makes-false-denials) | 07-03 | verbatim |
| VSL drafting and editing | V27 | [3-7 minute agent template (derived)](#v27-3-7-minute-agent-template-derived) | 07-03 | derived |
| VSL drafting and editing | V28 | [Ten short VSL concepts from a product page](#v28-ten-short-vsl-concepts-from-a-product-page) | 07-04 | verbatim |
| VSL drafting and editing | V29 | [Pick a concept](#v29-pick-a-concept) | 07-04 | verbatim |
| VSL drafting and editing | V30 | [Short VSL concepts from a brief](#v30-short-vsl-concepts-from-a-brief) | 05-02 · 07-04 | verbatim |
| VSL drafting and editing | V31 | [Use an earlier hook and write](#v31-use-an-earlier-hook-and-write) | 07-04 | verbatim |
| VSL drafting and editing | V32 | [CTA variants of the same ad](#v32-cta-variants-of-the-same-ad) | 07-04 | verbatim |
| VSL drafting and editing | V33 | [Five short VSLs from a brief plus chosen hooks](#v33-five-short-vsls-from-a-brief-plus-chosen-hooks) | 07-04 | verbatim |
| VSL drafting and editing | V34 | [Line-edit an outline, then write](#v34-line-edit-an-outline-then-write) | 07-04 | verbatim |
| VSL drafting and editing | V35 | [Ten short concepts from an existing script](#v35-ten-short-concepts-from-an-existing-script) | 07-04 | verbatim |
| VSL drafting and editing | V36 | [Tease more, give away less; change the voice](#v36-tease-more-give-away-less-change-the-voice) | 07-04 | verbatim/reconstructed |
| VSL drafting and editing | V37 | [Clean up a swiped transcript](#v37-clean-up-a-swiped-transcript) | 04-04 · 14-02 | verbatim/reconstructed |
| Hooks | H1 | [Deep research hook generation](#h1-deep-research-hook-generation) | 04-10 | verbatim |
| Hooks | H2 | [Hook generation for tools that can't read long PDFs (Perplexity)](#h2-hook-generation-for-tools-that-cant-read-long-pdfs-perplexity) | 04-10 | verbatim |
| Hooks | H3 | [Snippets, not bullets (feedback)](#h3-snippets-not-bullets-feedback) | 04-10 | verbatim |
| Hooks | H4 | [Generate still more hooks from a hook database](#h4-generate-still-more-hooks-from-a-hook-database) | 04-10 | verbatim |
| Hooks | H5 | [Start a hook-heavy ad session](#h5-start-a-hook-heavy-ad-session) | 04-10 | verbatim |
| Hooks | H6 | [Hook generation for a new niche (problem aware)](#h6-hook-generation-for-a-new-niche-problem-aware) | 07-01 | partial |
| Hooks | H7 | [Hook generation from an existing script (financial)](#h7-hook-generation-from-an-existing-script-financial) | 07-04 | partial |
| Hooks | H8 | [Hook-heavy micro-lead concepts from a finished VSL](#h8-hook-heavy-micro-lead-concepts-from-a-finished-vsl) | 07-01 | reconstructed |
| Hooks | H9 | [ADHD hook ad concepts from a brief](#h9-adhd-hook-ad-concepts-from-a-brief) | 05-02 | reconstructed |
| Hooks | H10 | [Edit a hook (and test a new mechanism on the same ad)](#h10-edit-a-hook-and-test-a-new-mechanism-on-the-same-ad) | 07-04 | verbatim/partial |
| Hooks | H11 | [Swap the hook, keep the body](#h11-swap-the-hook-keep-the-body) | 07-03 · 07-04 | verbatim/reconstructed |
| Advertorials | A1 | [Outline the structure of an advertorial](#a1-outline-the-structure-of-an-advertorial) | 09-01 | verbatim |
| Advertorials | A2 | [Swipe the structure for our product](#a2-swipe-the-structure-for-our-product) | 09-01 | verbatim |
| Advertorials | A3 | [Ten advertorial hooks from a source document](#a3-ten-advertorial-hooks-from-a-source-document) | 09-02 | verbatim |
| Advertorials | A4 | [Outline one advertorial angle](#a4-outline-one-advertorial-angle) | 09-02 | verbatim |
| Advertorials | A5 | [Write the advertorial](#a5-write-the-advertorial) | 09-02 | verbatim |
| Advertorials | A6 | [Shorter version for testing](#a6-shorter-version-for-testing) | 09-02 | verbatim |
| Advertorials | A7 | [Second angle in the short format](#a7-second-angle-in-the-short-format) | 09-02 | reconstructed |
| Advertorials | A8 | [Multi-point review feedback](#a8-multi-point-review-feedback) | 09-02 | reconstructed |
| Advertorials | A9 | [Add a missing motive to the story](#a9-add-a-missing-motive-to-the-story) | 09-02 | verbatim |
| Advertorials | A10 | [Build the advertorial page in Magic Patterns](#a10-build-the-advertorial-page-in-magic-patterns) | 09-02 | verbatim/reconstructed |
| PDPs | D1 | [Extract a PDP outline from two product pages](#d1-extract-a-pdp-outline-from-two-product-pages) | 10-01 | verbatim |
| PDPs | D2 | [Extract a PDP outline from one product page](#d2-extract-a-pdp-outline-from-one-product-page) | 10-01 | verbatim |
| PDPs | D3 | [Swipe the structure for a product with a live page](#d3-swipe-the-structure-for-a-product-with-a-live-page) | 10-01 | verbatim |
| PDPs | D4 | [Swipe the structure from a brief](#d4-swipe-the-structure-from-a-brief) | 10-01 | verbatim |
| PDPs | D5 | [Stop Claude from coding the page](#d5-stop-claude-from-coding-the-page) | 10-01 | verbatim |
| PDPs | D6 | [PDP for an offer with no website yet](#d6-pdp-for-an-offer-with-no-website-yet) | 10-01 | verbatim |
| PDPs | D7 | [Fallback when Claude cannot fetch the page](#d7-fallback-when-claude-cannot-fetch-the-page) | 10-02 | verbatim |
| Ads | AD1 | [Meta ad captions](#ad1-meta-ad-captions) | 12-01 | reconstructed |
| Ads | AD2 | [Five-question ad analysis](#ad2-five-question-ad-analysis) | 12-01 | verbatim/derived |
| Ads | AD3 | [Outline a short ad against a structure doc](#ad3-outline-a-short-ad-against-a-structure-doc) | 04-09 | verbatim/partial/derived |
| Ads | AD4 | [Veo 3 vlog prompt generator (guest, fragments)](#ad4-veo-3-vlog-prompt-generator-guest-fragments) | 12-04 | partial |
| Ads | AD5 | [Build a prompt generator for a new video format](#ad5-build-a-prompt-generator-for-a-new-video-format) | 12-04 | reconstructed |
| Upsells | U1 | [Outline an upsell swipe's structure](#u1-outline-an-upsell-swipes-structure) | 14-02 | verbatim |
| Upsells | U2 | [Write a new upsell section by section from the swipe](#u2-write-a-new-upsell-section-by-section-from-the-swipe) | 14-02 | verbatim |
| Upsells | U3 | [Redirect when the upsell is "more of the same"](#u3-redirect-when-the-upsell-is-more-of-the-same) | 14-02 | verbatim |
| Upsells | U4 | [Add an expectations timeline](#u4-add-an-expectations-timeline) | 14-02 | verbatim |
| Upsells | U5 | [More-of-the-same upsell from a product URL](#u5-more-of-the-same-upsell-from-a-product-url) | 14-03 | verbatim |
| Upsells | U6 | [Cross-sell script and its three feedback rounds](#u6-cross-sell-script-and-its-three-feedback-rounds) | 14-03 | verbatim |
| Upsells | U7 | [Book-a-call upsell for info-product buyers](#u7-book-a-call-upsell-for-info-product-buyers) | 14-03 · 05-03 | verbatim |
| Email | E1 | [Abandon cart sequence with a discount ladder](#e1-abandon-cart-sequence-with-a-discount-ladder) | 15-05 | verbatim |
| Email | E2 | [Welcome series with cross-sells](#e2-welcome-series-with-cross-sells) | 15-05 | verbatim |
| Email | E3 | [Site-wide holiday sale](#e3-site-wide-holiday-sale) | 15-05 | verbatim |
| Email | E4 | [Abandon cart sequence from a brief](#e4-abandon-cart-sequence-from-a-brief) | 15-05 | verbatim |
| Funnel and economics | F1 | [Hidden factors seed prompt](#f1-hidden-factors-seed-prompt) | 13-01 | partial |
| Funnel and economics | F2 | [Score an offer on the 15 hidden factors](#f2-score-an-offer-on-the-15-hidden-factors) | 13-01 | verbatim/derived |
| Review and feedback prompts | X1 | [Second-model review of a lead](#x1-second-model-review-of-a-lead) | 07-02 | reconstructed |
| Review and feedback prompts | X2 | [Audit a VSL against the RMBC outline (derived)](#x2-audit-a-vsl-against-the-rmbc-outline-derived) | 04-01 | derived |
| Review and feedback prompts | X3 | [VSL straight-line check (derived)](#x3-vsl-straight-line-check-derived) | 04-02 | derived |
| Review and feedback prompts | X4 | [Advertorial review checklist (derived)](#x4-advertorial-review-checklist-derived) | 09-02 | derived |
| Review and feedback prompts | X5 | [Feedback patterns used across the course](#x5-feedback-patterns-used-across-the-course) | compiled | derived |

## Research
Pipeline output: three or four deep-research reports merged into one **unified research document** ([concept](../concepts/unified-research-document.md), [framework](../frameworks/deep-research-workflow.md)). Order in the course: awareness → competitors → psychographics → (optional) ingredients → merge. [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md)

### R1. Market awareness deep research
- **Use when:** first step for any new product or offer; you need the majority awareness stage, a TAM estimate and a % of TAM per stage before choosing leads, ad angles or funnel length.
- **Inputs:** `YOUR NICHE`, `_PRODUCT_`, `_GEOGRAPHY_`, optional `_DETAILS_` (e.g. "Focus on women 35+.").

```text
I want your help evaluating the level of Market Awareness for a product in the YOUR NICHE space. The specific product is _PRODUCT_

I would like for you to dive deep to help me understand the current level of market awareness for this product in _GEOGRAPHY_.

Optional:
Here are more details about the market _DETAILS_

To do this, we can look at the classic levels of Product and Market awareness that is often attributed to Eugene Schwarz, which can be categorized as follows:

1. Unaware: Prospects are not even aware of a problem or need that your product or service can solve.

2. Problem Aware: Prospects recognize they have a problem or need but are unaware of potential solutions.

3. Solution Aware: Prospects know that solutions exist for their problem, but they are not yet aware of your specific solution.

4. Product Aware: Prospects know about your solution, your product or service, and are evaluating its features and benefits.

5. Most Aware: Prospects are highly aware of your solution, its benefits, and are likely to make a purchase decision soon.

For the intents of this exercise, let's not consider Product Aware or Most Aware to be for our specific product and brand. Instead let's consider it to be an awareness about similar/nearly identical products and brands that offer those products.

In order to make this assessment please utilize a variety of signals including social media chatter, articles and blog posts, influencer content, search trends, any available sales data on the product category (and its growth), and so on.

Additionally:

1. Please provide an overview of the estimated TAM (total addressable market) for this product.

2. Please provide a rough estimate of what percentage of the TAM falls into each category of product/market awareness.

3. At the end of your review, please give me a FINAL selection for which stage of Product/Market Awareness the majority of individuals within the market fall.

Thanks!
```

- **Source:** [02-01 v2 01:30](../lessons/02-01-product-market-awareness.md) (screenshot of the template); doc `01-2 Product-Market Awareness Deep Research Prompt Examples.docx`, "Prompt #1".
- **Status:** verbatim. The file spells "Schwarz".
- **Notes:**
  - Run it in Gemini Deep Research (his preference, for the tables) and at least one other LLM; numbers differ by model but give "a general gauge". [02-01 v2 04:21–05:57; v2 21:18–22:59](../lessons/02-01-product-market-awareness.md)
  - Read only the TAM section, the % per stage and the final verdict. [v2 09:40, 10:45]
  - The "Product Aware / Most Aware = aware of the category, not our brand" paragraph is Stefan's deliberate modification for small DTC brands. Keep it. [02:49–03:48]
  - Course quirk: Examples 3 and 4 in the docx drop the "To do this, we can look at…" sentence. Keep the full template every run. [02-01 Prompts]
  - The percentages are LLM estimates, not measurements. Label them "(LLM estimate)" in the unified research doc.

### R2. Competitor deep research
- **Use when:** after R1; you need competitor demos, funnels, core messaging, recurring hooks and angles, pricing, and what customers love and hate about them.
- **Inputs:** `YOUR NICHE`, `_PRODUCT_`, `_GEOGRAPHY_`, competitor type, optional `_DETAILS_`.

```text
I want your help doing competitor research for a product in the YOUR NICHE space. The specific product is _PRODUCT_and we are focused on competitors in _GEOGRAPHY_.

Specifically, we're looking for D2C brands who primarily sell online through eCommerce or Direct Response sales funnels.

For each competitor you find, I want to understand:

Who is the target demo they speak to?

What are their main new customer acquisition funnels?
What is their core messaging in their ads, advertorials, and other advertising assets?
What are examples of their advertisements or landing page assets if available?
Are there any recurring or repetitive hooks/angles/big ideas you see consistently appearing in their advertising assets?
What is their pricing structure?
What do customers love and what do customers dislike about them (use reviews, social signals, social media platforms, etc to answer this)?

If available, what is their estimated overall business revenue and revenue for their hero product(s) that are most similar to the one I've mentioned?

Optional:
Here are more details about the market _DETAILS_

Please go ahead and get started now, and thank you!
```

Variant lines from the same doc. Biz-opp competitor line (replaces the "D2C brands" line):

```text
Specifically, we're looking for coaching programs, training platforms, and gurus who primarily sell online through Direct Response sales funnels.
```

Final question appended before "Please go ahead" in Example 2 (Airbnb arbitrage):

```text
What are the core promises they make to prospective customers? Value props, language they use when selling their programs, etc? I'm really looking for specific phrases, claims, verbiage used. Basically, if I were selling an Air BNB Arbitrage program I'd be looking for phrases, sentences, fragments that we see these competitors repeatedly use that I can use as well.
```

Example 3 (golf) details line and appended question:

```text
Here are more details about the market: let's focus on amateur golfers, the market is not for professionals here.
```

```text
What are the core promises they make to prospective customers? Value props, language they use when selling their clubs, etc? I'm really looking for specific phrases, claims, verbiage used. Basically, if I were selling new golf club that adds distance and fixes a golfer's slice, I'd be looking for phrases, sentences, fragments that we see these competitors repeatedly use that I can use as well.
```

- **Source:** [02-02](../lessons/02-02-competitor-research-walkthrough-and-examples.md); doc `02-1 Competitor Research Prompt Examples.docx` (Prompt #1 and Examples 1–3). The spoken golf version [47:30–48:12] differs slightly.
- **Status:** verbatim.
- **Notes:**
  - Spoken follow-up after the first Airbnb report (reconstructed): "Okay, thanks. However, I'm really looking for specific phrases, claims, verbiage used. Basically, if I were selling an Airbnb arbitrage [program], I'd be looking for phrases, sentences, fragments that we see these competitors repeatedly use." [02-02 30:47–31:31](../lessons/02-02-competitor-research-walkthrough-and-examples.md) This became the appended "core promises" question; include it from the start.
  - ChatGPT asks clarifying questions; his answers: "both" influencers and platforms (Airbnb); "focus on drivers for now… similar value props" (golf). [34:38–35:10; 52:39–53:36]
  - ⚠ compliance: "phrases… I can use as well" means harvesting competitor *language patterns*, not copying their claims. Copy the mechanism, not the asset ([AGENTS.md](../../../../../../AGENTS.md) rule 3); revenue estimates in the output are LLM guesses, label them.

### R3. Psychographic deep research
- **Use when:** after R1–R2; you need pains, beliefs, hopes, attitudes, experiences with existing solutions and the market's own words.
- **Inputs:** `DEMO/Market Information` (one line, e.g. the three demo lines below).

```text
I am writing some sales copy targeted towards DEMO/Market Information. I'd like your help doing psychographic research. What are their struggles and pain points? What are their beliefs?

Below is a series of questions I used in the past, as part of my RMBC Method for copywriting, where the R stands for research. This should be a good framework to use while doing research on the demo. I'd love it if you can even provide 'quotes' from folks in this demo by looking at comments on social media, or in forums, etc. Basically we want to hear what they're saying and what they believe. We want to hear answers in their own words!

Here’s the list of questions:

Insights Into Demographic :

Who Is Your Customer?

What Attitudes Do They Have? (Religious, Political, Social, Economic)?

What Are Their Hopes and Dreams?

What Are Their Victories and Failures?

What Outside Forces Do THEY Believe Have Prevented Their Best Life?

What Are Their Prejudices?

Sum Up Their Core Beliefs About Life, Love, and Family In 1-3 Sentences.

Other Existing Solutions:

What is the Market Already Using? (List Out)

What Has Their Experience Been Like?

What Does the Market Like About Existing Solutions?

What Does the Market Dislike About Existing Solutions?

Are Their Horror Stories About Existing Solutions?

Does the Market Believe Existing Solution Works?

If Not, Why?

Curiosity:

Has Someone Tried to Solve the Market’s Pain Points Before In A Very Unique Way?

What Was The Result?

Is There A Conspiratorial Story Behind Why Old Solutions Didn’t Work?

Are There Any Older Attempts to Solve the Problem (Pre-1960) That Are Unique?

What Happened? Were they successful but forgotten? Or were they a failure? Why?

Examples:

1) Nikola Tesla in the energy space. Big energy didn’t want his solutions, he was discredited and shamed. His inventions and discoveries were thrown into the ash heap of history until now.

2) U.S. Army tried to cure foot fungus during WWII, surgeon general was on a desperate race because troops were missing service time. Finally succeeded by using Undecylenic Acid. But today we forget how effective it is.

Corruption:

Is There A Belief That the Market’s Pain Point Used To Not Exist, Or Used To Not Be So Bad?

Is There A Belief That It’s Been Recently Exacerbated By Outside Forces?

If So, What Are Those Forces And What’s The Reason Behind Their Presence?

Examples:

Obesity and diabetes being the result of Dr. Ancil Keyes.

This isolated group of people doesn’t struggle from whatever condition/pain point that most of us do. In America we DO suffer from this pain point. The reason why is that we are exposed to these outside forces while this isolated group isn’t.
```

Demo lines used in the three worked examples (the only text that changes):

```text
Example 1 (eye serum): U.S. women 40 + who have wrinkles, dark spots, or puffy eye bags.

Example 2 (biz-op): people in the U.S. looking for additional income and financial freedom. This is sometimes referred to as the “biz opp” space.

Example 3 (golf): amateur golfers who want to fix their slice, hit their drives further, and in general post lower scores while enjoying playing golf more due to playing consistently better.
```

- **Source:** [02-03](../lessons/02-03-psychographic-research.md); doc `03-1 Psychographic Deep Research Prompts.docx`, "Prompt #1". Run in Gemini, ChatGPT and Perplexity.
- **Status:** verbatim.
- **Notes:**
  - The examples steer the output: Gemini picked Ancel Keys because the prompt named him. Swap or delete the Tesla, undecylenic-acid and Keys examples to fit your niche; Example #2 (biz-op) drops the Curiosity examples and the Keys line. [02-03 v2 24:06](../lessons/02-03-psychographic-research.md)
  - Merge the reports with [R4](#r4-merge-several-deep-research-reports-into-one); get extra customer language with [R5](#r5-follow-up-for-the-markets-own-words).
  - ⚠ compliance: the "Curiosity" and "Corruption" questions invite conspiracy narratives ("Big energy", "Dr. Ancil Keyes" caused obesity). Treat answers as *beliefs the market holds*, not facts. Any "quote" the LLM returns must link to a real, findable post; otherwise mark `[VERIFY: source of quote]` and never present it as a testimonial.

### R4. Merge several deep-research reports into one
- **Use when:** you have 2+ deep-research PDFs on the same demographic (from R3 or similar) and want one unified psychographic report.
- **Inputs:** each report attached as a PDF; "demographic" is the only variable and can stay generic.

Opening of the prompt (verbatim):

```text
I am writing some sales copy targeted towards a specific demographic.

I’ve had multiple LLMs generate Deep Research reports for me on this demographic, and I am attaching each of those as a PDF here.

What I would like your help with is to go through these reports and then create one unified report that I can use as a reference.

For greater context, here is the prompt I give to LLMs for deep research.
```

Then paste the body of [R3](#r3-psychographic-deep-research) from "I'd like your help doing psychographic research." to the end ("…while this isolated group isn't."). The doc's copy differs from R3 in one word: example 1 starts "1) Tesla in the energy space" (not "Nikola Tesla"). Then close with:

```text
========

Please go ahead and create the document now.
```

- **Source:** [02-03](../lessons/02-03-psychographic-research.md); doc `03-2 Claude Deep Research Summary Prompt.docx`. Run in Claude.
- **Status:** verbatim (split here only to avoid repeating the R3 body).
- **Notes:** check the output has one section per question and an "In Her Own Words" quote block per section; the biz-op version adds Executive Summary, Strategic Synthesis, Actionable Copywriting Angles, a Voice of Customer Lexicon and a Conclusion. [02-03 Prompts](../lessons/02-03-psychographic-research.md)

### R5. Follow-up for the market's own words
- **Use when:** in the same chat as an R3 report, to collect pain and desire language (adjectives, descriptors) for hooks and copy.
- **Inputs:** the highlighted variables: audience ("women"), pain ("aging skin, looking older, wrinkles, and so on."), desired state ("skin that looks youthful and amazing").

```text
Thanks. Now please continue deep research and leverage social signals like social media, forums, etc to provide the following:

1. As many quotes as possible from women describing their specific pain points around aging skin, looking older, wrinkles, and so on. I want to hear how they think about the specific pain points here in their own words!

2. As many quotes as possible from women describing the opposite: skin that looks youthful and amazing. What adjectives and other descriptors do they use?
```

- **Source:** [02-03 v2 42:30–43:40](../lessons/02-03-psychographic-research.md); doc `03-3 Optional Follow-Up Prompt…docx`.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: LLM "quotes" are frequently paraphrased or invented. Keep only quotes you can trace to a real post or review; use the rest as vocabulary, never as attributed quotes or testimonials.

### R6. Unified research document
- **Use when:** you have the awareness, competitor and psychographic reports and need the single reference doc every later prompt (UM, brief, hooks) attaches.
- **Inputs:** `_NICHE_`, `_PRODUCT_`, `_REGION_`; the research PDFs; the yellow-highlighted awareness line (change per market).

```text
I’m working on a marketing campaign in _NICHE_. The product is _PRODUCT_ and we focus on customers in _REGION_.

So far I have performed research around Product/Market Awareness Levels, Competitors, and Psychographic Research.

I am going to upload several PDFs that contain this research.

What I want you to do is go through these PDFs in-depth and then create one unified research brief that contains all of the key elements that would be needed in order to successfully implement this campaign. Specifically, this will be a unified document that I will share with you and other LLMs for background information and context as we generate additional copy and marketing assets, most of which will be direct response oriented.

I don’t need information on TAM size, or even specific strategies that were included in these deep research reports. Instead what I really need are the following:

1. Target Market Demographic Overview

Focus on people who fall into the Problem Aware and Solution Aware Market segments primarily.

2. Target Market Psychographic Overview

What are their problems and pain points?

[Examples, from a DIFFERENT PRODUCT in a DIFFERENT NICHE]

Feel embarrassed, ashamed and humiliated about their weight, especially when comparing themselves to thinner women.

- Struggle to lose weight with diet and exercise. Get frustrated when the weight comes back after losing a few pounds.

- Feel like a prisoner in their body and that their weight is destined to keep increasing.

- Experience low self-esteem, lack of confidence, feeling unattractive.

- Health and mobility issues like low energy, trouble moving, joint pain.

- Judged and stared at by others for their weight. Feel they are a burden.

- Clothes don't fit right anymore. Can't fit into "skinny" jeans.

- Fear their partner no longer finds them attractive.

- Can't keep up with kids/grandkids or do activities they enjoy.

What are their hopes and dreams?

(Specifically, what does their ideal future state look like where their problem has been solved. What would that look like? How would they look and feel? When they dream and imagine this future, what else is true about their life at this point?)

How do they view themselves more broadly, what language should we use when speaking to them, and what language should we avoid?

What are the Primary Promises we can make to them, and that they would want to hear, when it comes to solving their pain points?

[Examples, from a DIFFERENT PRODUCT in a DIFFERENT NICHE]

- Experience Rapid fat loss from belly, hips, thighs without extreme diet or exercise.

- Lose up to 71 lbs of fat fast.

- Boost metabolism and burn fat 24/7 by activating "fat cell hypothermia".

- Increase confidence, self-esteem, feeling sexy and vibrant again.

- Fit back into favorite clothes like jeans, dresses, and swimwear.

- Regain independence and stop feeling held back by weight.

- Be admired, desired, and turn heads again.

- Reclaim energy, youthfulness and love life again.

- Free yourself from guilt, shame and worry about your weight.

3. What will their biggest objections be to our marketing campaigns for our product, and how can we address those?

4. What existing solutions has the market tried already? Why are those existing solutions not adequate enough?
```

- **Source:** [02-04](../lessons/02-04-unified-research-process.md); doc `04-1 Unified Research Document Prompt Process.docx`. Demonstrated in Claude.ai and Poe.
- **Status:** verbatim.
- **Also appears:** [01-01 06:33](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) as a spoken paraphrase (derived): "Here are three research documents… Combine them into one unified research document…".
- **Notes:**
  - The two example blocks are from a weight-loss offer in a different niche: format guides only. He says the parenthetical under "hopes and dreams" is partly redundant [02-04 03:36]; an earlier fifth item ("anything else you think is relevant") was removed [07:17].
  - Output schema to check against: demographic overview; psychographics (pains, hopes, language to use and avoid, primary promises); objections and answers; existing solutions and why they fail. [02-04](../lessons/02-04-unified-research-process.md)
  - ⚠ compliance: the example promises ("Lose up to 71 lbs of fat fast", "activating 'fat cell hypothermia'") are unsubstantiated weight-loss claims; structure only, claims not reusable. The model will imitate their boldness. Add to the prompt: "Primary promises must be benefits we can substantiate; mark any number or mechanism claim [VERIFY]."

### R7. Ingredient deep research (claims tied to studies)
- **Use when:** supplement or skincare offers; you need per-ingredient claims backed by published studies, tied to the unique mechanism (V1) or to market pain points only (V2).
- **Inputs:** ingredient list; attachments: unified research doc ("overview of the market and their paint points") and the UM doc.

```text
Prompt V1 (For When You Know the UM and Have Done Deep Research On The Market)

These are the ingredients for an eye serum I'll be doing sales copy for:

Dipalmitoyl Hydroxyproline

Pistacia Lentiscus Extract

Saccharide Isomerate

Sodium Hyaluronate

Cupuacu Seed Butter and Jojoba Esters

Vitamin C and Vitamin E

Amino acids (Proline, Glycine, and Alanine)

I'm attaching two documents for reference. One is an overview of the market and their paint points. The second is the unique mechanism I'll be using.

What I want for you to do is come up with a list of claims for each ingredient that can be tied back to specific studies or research. This research needs to come from stuff published on NCBI or other scientific journals, and cannot include things from random blogs or websites. Give preference to RCTs with humans, but if those aren't available you can include other studies too.

Claims should be focused on the following things:

1. How the ingredient supports the unique mechanism of the solution (when applicable).

2. Additional studies of how the ingredient helps alleviate pain points of the market (regardless of the connection to the mechanism).

Please keep the claims digestible with references. I don't need a big biology lesson. I just need accurate claims showing the best efficacy and results possible for each ingredient, so I can take those and use them in various marketing assets.
```

Example fill (blood sugar chew; only the product line and ingredient list change, the doc repeats the full body):

```text
These are the ingredients for an blood sugar support chew I'll be doing sales copy for:

Xylitol, Ceylon Cinnamon (Cinnamomum verum ) bark,

Corosolic Acid [from Banaba (Lagerstroemia speciosa )

leaf extract], Saffron (Crocus sativus L. ) bulb extract,

Fucoxanthin (from Laminaria japonica ), Fucoidan (from

Laminaria japonica ), Citrus sinensis , Kudzu (Pueraria

montana ) flower extract, Oleuropein [from Olive (Olea

europaea ) leaf extract], Berberine HCL

What I want is for you to do is come up with a list of claims for each ingredient that can be tied back to specific studies or research. [... identical body to Prompt V1 from "This research needs to come from stuff published on NCBI" through "... use them in various marketing assets."]
```

- **Source:** [02-05](../lessons/02-05-ingredient-deep-research.md); doc `05-2 Ingredient Deep Research Prompt.docx`.
- **Status:** verbatim. Source typos kept ("paint points", "I just need to accurate claims").
- **Notes:**
  - Prompt V2 (no mechanism yet) is not a separate file: "basically the same prompt" without the mechanism attachment, with claim type 1 "not applicable". [02-05 01:59](../lessons/02-05-ingredient-deep-research.md)
  - Run in two LLMs (Perplexity and ChatGPT in the course), then combine with the header in [R8](#r8-header-for-a-combined-ingredient-research-file).
  - ⚠ compliance: "showing the best efficacy and results possible" pushes cherry-picking. Add: "For each claim give the study design, population, dose and effect size; flag in-vitro and animal studies; phrase supplement claims as structure/function ('supports healthy…'), never treat, cure or prevent." Open every cited study before using it; LLM citations can be wrong or invented.

### R8. Header for a combined ingredient research file
- **Use when:** you paste two LLMs' ingredient research into one file to attach to the brief generator.
- **Inputs:** none.

```text
Note for Claude or other LLMs:

This is research on ingredients from two LLMs. As a result, you may see the same study data point twice.
```

- **Source:** [02-05](../lessons/02-05-ingredient-deep-research.md); top of `Combined Ingredient Research_Unity Eye Serum.docx`, followed by a "Perplexity" section and a "ChatGPT" section.
- **Status:** verbatim.

### R9. Ultimate universal target avatar deep research (guest)
- **Use when:** auditing a new brand or client for short-form ad creative; you have only a website URL and need a full avatar profile (88 questions) aimed at ad messaging. Guest material: Max Finn, 12-04 TikTok ads.
- **Inputs:** `[WEBSITE URL]`.

```text
Ultimate Universal Target Avatar Deep Research Prompt

CONTEXT: I need you to analyze [WEBSITE URL] and conduct comprehensive target avatar research for this business. First, visit their website and understand their product/service, value proposition, target market, pricing, and unique positioning. Then provide detailed answers about their ideal target avatar so I can create the most profitable ads possible.

YOUR MISSION: After analyzing the business website, answer ALL of the following questions with specific, actionable insights about their ideal customer avatar:

## BUSINESS ANALYSIS FOUNDATION

1. What is this business's core product/service offering and primary value proposition?

2. What industry/market do they operate in, and what's their unique positioning vs. competitors?

3. What pricing model and tier does this business operate in (budget, mid-market, premium, luxury)?

## DEMOGRAPHICS & FOUNDATION

4. What are the specific demographic details (age range, gender, income level, education, location, family status) of their ideal customer?

5. What life stage, career level, or business situation is this avatar typically in when they need this solution?

6. Are they B2B or B2C focused, and what's their decision-making role (individual consumer, business owner, department head, etc.)?

## PAIN POINTS & CHALLENGES

7. What are the top 3-5 specific problems or pain points this avatar experiences that this business solves?

8. What are the emotional and psychological frustrations they feel when dealing with these challenges?

9. What have they tried before to solve these issues, and why didn't those solutions work?

10. What happens if they don't solve this problem (consequences, missed opportunities, continued frustration)?

## GOALS & MOTIVATIONS

11. What are their primary goals and desired outcomes over the next 1-3 years related to this problem area?

12. What specific metrics, results, or life improvements do they use to measure success?

13. What motivates them to take action - avoiding pain, gaining pleasure, achieving status, improving efficiency, or something else?

14. What would their ideal end state look like after using this product/service?

## DECISION-MAKING PROCESS

15. How does this avatar typically research and evaluate solutions in this category before making decisions?

16. Who else is involved in their decision-making process (family, colleagues, bosses, advisors)?

17. What objections or concerns typically prevent them from purchasing solutions like this?

18. What's their typical buying timeline from problem awareness to purchase decision?

## COMMUNICATION & BEHAVIOR

19. Where does this avatar spend their time online and offline (social platforms, websites, communities, physical locations)?

20. What language, terminology, and communication style resonates most with them?

21. What time of day/week are they most likely to engage with content or make purchasing decisions?

22. How do they prefer to be communicated with (email, social media, phone, in-person, etc.)?

## CURRENT SOLUTIONS & COMPETITIVE LANDSCAPE

23. What alternatives, competitors, or current solutions are they using to address their needs?

24. What would make them switch from their current approach to this business's solution?

25. What do they like/dislike about existing options in this market?

26. How do they currently measure or track results in this area?

## VALUE PERCEPTION & PREFERENCES

27. How do they prefer to consume information about solutions in this category (video, text, demos, trials, consultations)?

28. What would they consider a "quick win" vs. a long-term strategic investment?

29. What's their typical budget range and buying cycle for solutions in this price category?

30. How price-sensitive are they, and what factors justify higher prices to them?

## VALIDATION & SPECIFICITY

31. Can you provide specific real examples of companies/people who perfectly represent this avatar?

32. What does their typical day look like, and when does this problem/need surface?

33. What other products/services do they typically buy that indicate they're ideal for this business?

## PSYCHOLOGICAL TRIGGERS & EMOTIONAL DRIVERS

34. What specific words, phrases, or emotional triggers instantly grab their attention in marketing?

35. What are their deepest fears and anxieties related to this problem area?

36. What are their secret desires and aspirations they might not openly admit?

37. What status symbols, social proof elements, or peer validation do they value most?

38. What time-sensitive urgency naturally exists in their world related to this need?

## BUYING PSYCHOLOGY & BEHAVIOR

39. Are they impulse buyers or deliberate researchers, and what's their typical decision timeline?

40. What's the maximum amount they've ever spent on similar solutions, and what justified that investment?

41. What specific outcomes, ROI, or improvements would make price irrelevant to them?

42. Do they prefer to be early adopters or wait for social proof from others?

43. What buying triggers have successfully motivated them in past purchases (scarcity, social proof, authority, reciprocity)?

## MEDIA CONSUMPTION & ATTENTION PATTERNS

44. What specific influencers, thought leaders, publications, or brands do they follow and trust?

45. What type of content format gets them to stop and engage vs. scroll past?

46. What device and platform do they primarily use when researching solutions like this?

47. What's their attention span for different types of content related to this topic?

48. When are they most receptive to marketing messages (time of day, day of week, seasonally)?

## COMPETITIVE INTELLIGENCE & POSITIONING

49. What competitor marketing messages or positioning have they responded to recently?

50. What messaging approaches immediately turn them off or make them distrust brands?

51. What unique angle or perspective on their problem has never been presented to them before?

52. What industry jargon or buzzwords have they become numb to hearing?

53. What contrarian or controversial stance could intrigue them about this topic?

## OFFER OPTIMIZATION & CONVERSION

54. What would be the perfect "irresistible offer" structure for them (discounts, bonuses, guarantees, payment terms)?

55. What's the minimum viable result they'd need to see to consider this solution successful?

56. What risk-reversal or guarantee would completely eliminate their purchase hesitation?

57. What additional bonuses or value-adds would increase perceived value without significantly increasing costs?

58. What pricing strategy and positioning works best for this market segment?

## OBJECTION HANDLING & RESISTANCE

59. What's their most common excuse for not taking action, even when they know they should?

60. What past negative experiences have made them skeptical of solutions in this category?

61. What would others in their life say to discourage them from making this purchase?

62. What internal limiting beliefs prevent them from investing in solutions like this?

63. What specific fears do they have about making the wrong decision or not seeing results?

## LIFETIME VALUE & RELATIONSHIP BUILDING

64. What additional problems or needs emerge after they solve their initial challenge?

65. What's their potential lifetime value including repeat purchases, upgrades, and referrals?

66. What would make them become an advocate who actively promotes this business?

67. What's their natural progression or evolution in this market over time?

68. What complementary products/services would they likely need as they grow or change?

## TESTING & OPTIMIZATION INSIGHTS

69. What specific segments within this target market convert at higher rates?

70. What seasonal, cyclical, or event-driven patterns affect their buying behavior?

71. What specific pain point angles produce the highest engagement in this market?

72. What creative elements, social proof, or messaging themes historically perform best with this audience?

73. What's the optimal marketing frequency before they experience ad fatigue?

## ADVANCED SEGMENTATION & CONTEXT

74. How does their behavior differ based on company size, personal situation, or other key variables?

75. What geographic, cultural, or generational factors influence their decision-making?

76. How do early adopters vs. mainstream adopters in this market behave differently?

77. How does their buying pattern change during different economic conditions or life circumstances?

78. What triggers or events make them actively start looking for solutions like this?

## USAGE AND SUCCESS PATTERNS

79. How would they typically use this product/service in their daily life or business?

80. What would successful implementation and usage look like for them?

81. What support, guidance, or additional resources do they need to be successful?

82. How do they prefer to learn about and onboard with new solutions?

83. What would make them likely to upgrade, expand, or continue their relationship long-term?

BUSINESS-SPECIFIC DEEP DIVE QUESTIONS: 84. Based on this specific business model, what unique motivations drive their ideal customers? 85. What industry-specific challenges or opportunities make this solution particularly valuable? 86. How does this business's unique value proposition appeal to customer psychology? 87. What aspects of this business's positioning, pricing, or approach create specific buyer behaviors? 88. What competitive advantages does this business have that would be most compelling to their avatar?

OUTPUT REQUIREMENTS:

- First, provide a comprehensive analysis of the business based on their website

- Give specific, actionable insights for each question relevant to this particular business

- Include real examples of ideal customers and their situations where possible

- Focus on insights that directly impact ad targeting, messaging, and creative development

- Prioritize psychological triggers and emotional drivers that lead to conversions

- Provide tactical recommendations for each major insight area

- Address both emotional and logical decision-making factors

- Consider the unique aspects of this business's sales process and customer journey

- Highlight the most critical insights for immediate ad creation and campaign optimization

GOAL: Use this research to create highly converting, profitable ads that speak directly to the ideal customer's deepest needs, fears, desires, and decision-making process for this specific business.
```

- **Source:** [12-04 v2 00:56–04:34](../lessons/12-04-tiktok-ads.md); doc `04-1 Unicorn TikTok Creative Prompts.docx` (first tab of "Unicorn Prompts"). Max Finn (guest).
- **Status:** verbatim.
- **Notes:**
  - The guest calls it "83 questions" and says it was built for audits; the doc has 1–83 plus business-specific 84–88. Run it in Claude Deep Research, Gemini Deep Research, Grok and Perplexity and keep every output (guest claim). [12-04 v2 00:56–04:34](../lessons/12-04-tiktok-ads.md)
  - It overlaps R1–R3 but starts from the website, not from research on the market. Use RMBC's R1–R6 for a new offer; use R9 for a fast audit of an existing brand.
  - ⚠ compliance: Q31 asks for "real examples of companies/people who perfectly represent this avatar" and Q65 for lifetime value. Treat named people and numbers as unverified LLM output; never use them as testimonials or as data.

## Mechanism
Pipeline output: one chosen UMP/UMS pair written out in "expanded copy format" (the **UM doc**) that the brief and every asset attach. Steps: ideation → shortlist → evaluation/ranking → expansion. [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md) · [concept](../concepts/unique-mechanism.md) · [framework](../frameworks/ump-ideation-and-evaluation.md). Run M1, M3 and M4 inside the Unique Mechanisms project ([P1](#p1-unique-mechanisms-project)) or a plain chat with the unified research doc attached.

### M1. One-off UMP ideation
- **Use when:** you have the unified research doc and want a long list of candidate mechanisms (UMP + UMS pairs) for a product.
- **Inputs:** `_____PRODUCT____`, `_____NICHE___`, the awareness segment (highlighted "Problem Aware" in the doc), unified research doc attached; optional ingredient list.

```text
Today I want your help coming up with as many Unique Mechanism ideas for a _____PRODUCT____ in the _____NICHE___.

I have attached a research brief that will help you understand the market we are speaking to.

Here is a quick overview of how to understand Unique Mechanisms in the world of direct response and D2C copy:

In a Nutshell:

The unique mechanism explains why our prospect is struggling or suffering to achieve a goal…

And how they can overcome that problem.

At its core, the unique mechanism is always a two-part logical connection.

The Reason It's Important:

Typically by the time our prospect comes to us, they've tried numerous solutions to their problem already. In the past, these other solutions may have not worked at all, worked partially, or worked fully for a period of time (before they stopped working).

Our job as a copywriter is to educate our prospect about the REAL reason why past solutions didn't bring them permanent results. We do this by explaining that their knowledge about the problem is incomplete. They've been missing ONE CRUCIAL PIECE OF INFORMATION, and this "knowledge gap" is what's been holding them back.

There are two parts to the unique mechanism:

1. Unique Mechanism Behind the Problem our Prospect Faces.

2. Unique Mechanism Behind the Solution to that Problem.

It's important to identify the unique mechanism behind both the problem AND the solution.

By showing the unique mechanism behind the problem, you get the prospect to understand why they've failed in the past.

By showing the unique mechanism behind the solution, you get the prospect to believe that our product will bring them success where other alternatives have failed.

======

One thing to pay VERY careful attention to is the levels of Product/Market Awareness we are focusing on. This is important, because the UMP and UMS need to speak to our prospects where they are at. In other words, if the main market segment we are targeting is Problem Aware, it wouldn't make sense to have the UMP/UMS speak to people who are Product Aware or Most aware.

For this exercise, let's specifically focus on people in the market who are Problem Aware.

Please go ahead and get started now.
```

Example #1 fill (Airbnb arbitrage), the only lines that change:

```text
Today I want your help coming up with as many Unique Mechanism ideas for a product in the air BNB arbitrage space. The specific product is _a coaching program and community that shows people how they can lease a property long-term and then manage it as a short-term rental (with the property owner's consent) _

I have attached a research brief that will help you understand the market we are speaking to.

[... identical primer, "In a Nutshell" through "...success where other alternatives have failed.", then the awareness paragraph ...]

For this exercise, let's specifically focus on people in the market who are Problem Aware.

Please go ahead and get started now.
```

Example #2 fill (peptide eye serum, Solution Aware, with ingredients):

```text
Today I want your help coming up with as many Unique Mechanism ideas as possible for a product in the skincare space. The specific product is _a peptide eye serum.

I have attached a research brief that will help you understand the market we are speaking to.

[... identical primer and awareness paragraph ...]

For this exercise, let's specifically focus on people in the market who are Solution Aware.

Additionally, I have included a list of product ingredients for your consideration:

Dipalmitoyl Hydroxyproline

Pistacia Lentiscus Extract

Saccharide Isomerate

Sodium Hyaluronate

Cupuacu Seed Butter and Jojoba Esters

Vitamin C and Vitamin E

Amino acids (Proline, Glycine, and Alanine)

Please go ahead and get started now.
```

- **Source:** [03-02](../lessons/03-02-ump-ideation-with-llms.md); doc `02-2 UMP Ideation With LLMs.docx`. The primer is the handout text from [03-01](../lessons/03-01-unique-mechanisms-overview.md) (`01-1 Unique Mechanism Overview.docx`).
- **Status:** verbatim.
- **Notes:**
  - Name the awareness segment. The first run left it open and outputs drifted toward product-aware buyers; he added the line and re-ran. [03-02 02:07; 40:16; v2 00:00](../lessons/03-02-ump-ideation-with-llms.md)
  - Run in several tools. Gemini (2.5 Pro and Deep Research) won in this lesson; ChatGPT and Claude deep research gave "cute nicknames for really basic stuff". [03:10; 41:50–43:09]
  - Paste keepers into a running "potential mechanisms" doc; don't trust the model's own ranking. Rank with [M3](#m3-mechanism-evaluation-and-ranking). [11:04–12:06; 29:02]
  - Failure mode: a mechanism that forces you to sell something other than the product ("Capital Multiplier"). Flag it. [13:32]

### M2. More like number three
- **Use when:** one idea from M1 fits the target segment and you want more in that direction.
- **Inputs:** the number of the idea you like and why.

```text
Great, I like number three the most. The reason why is because this one speaks the most to problem-aware people versus most of the other ideas you shared, which speak more to product-aware folks, a smaller market segment, so I'd rather focus more on problem-aware people than anyone. With that being said, can you please provide some more unique mechanism ideas along the lines of number three.
```

- **Source:** [03-02 15:54–17:09](../lessons/03-02-ump-ideation-with-llms.md).
- **Status:** reconstructed (Whisper transcript, phrasing approximate).
- **Notes:** known failure: it returned weaker, over-similar ideas and he abandoned it. Re-run M1 with a tighter awareness instruction instead. [03-02 17:09–20:18; v2 00:00](../lessons/03-02-ump-ideation-with-llms.md)

### M3. Mechanism evaluation and ranking
- **Use when:** you have a shortlist doc of mechanism ideas and want them ranked against the market.
- **Inputs:** `PRODUCT`, `NICHE`, the awareness level (all highlighted placeholders); attachments: unified research doc + the shortlist doc.

```text
I am working on some direct response sales copy that will sell a PRODUCT to NICHE.

I'm going to share a few documents with you.

The first is a Unified Research Document that has relevant information for a market that my business will be selling to. It includes information, the level of Product/Market Awareness we'll be speaking to, competitor analysis, and key psychographic information.

The second document has several unique mechanism ideas that could be used in our sales copy when selling our products or services to the market.

Here's a reminder of what a Unique Mechanism is and why it's important in direct response and DTC marketing:

**In a Nutshell:**

The unique mechanism explains *why* our prospect is struggling or suffering to achieve a goal…

And *how* they can overcome that problem.

At its core, the unique mechanism is always a two-part logical connection.

**The Reason It's Important:**

Typically by the time our prospect comes to us, they've tried numerous solutions to their problem already. In the past, these other solutions may have not worked at all, worked partially, or worked fully for a period of time (before they stopped working).

Our job as a copywriter is to educate our prospect about the REAL reason why past solutions didn't bring them permanent results. We do this by explaining that their knowledge about the problem is incomplete. They've been missing ONE CRUCIAL PIECE OF INFORMATION, and this "knowledge gap" is what's been holding them back.

**There are two parts to the unique mechanism:**

1. Unique Mechanism Behind the Problem (UMP) our Prospect Faces.

2. Unique Mechanism Behind the Solution (UMS) to that Problem.

It's important to identify the unique mechanism behind both the problem AND the solution.

*By showing the unique mechanism behind the problem, you get the prospect to understand why they've failed in the past.*

*By showing the unique mechanism behind the solution, you get the prospect to believe that our product will bring them success where other alternatives have failed.*

=======

**Here's what I want you to do:**

Evaluate each unique mechanism idea based on their potential for connecting to our target market and persuading them to buy the product we are selling, and rank them from most likely to succeed to least likely to succeed.

In order to make this evaluation, consider the Unified Research Brief and the beliefs, attitudes, awareness levels, and competitive environment within which our target customer finds themselves.

When making your rankings, keep in mind that our core market is people who are Problem Aware.

Please go ahead and do this now.
```

- **Source:** [03-03](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md); doc `03-3 UMP Evaluation Prompt.docx`. Rankings were run in Claude, ChatGPT and Gemini 2.5 Pro.
- **Status:** verbatim.
- **Also appears:** spoken preview in [03-02 44:22](../lessons/03-02-ump-ideation-with-llms.md) (partial); eye-serum run in [03-04 44:00](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) with the last line changed to "…keep in mind that our core market is people who are Solution Aware." (the doc's Example #2 is the same change).
- **Notes:** run the ranking in 2–3 models and compare; you pick, the model advises.

### M4. Mechanism expansion into VSL copy
- **Use when:** one mechanism is chosen and you need it written as a full UMP/UMS section usable in a VSL (this becomes the UM doc).
- **Inputs:** the UMP and UMS summary of ONE mechanism; awareness level; for Solution Aware, the awareness profile from your own unified research doc; unified research doc attached.

```text
We're going to do an in-depth unique mechanism for a product. I've attached a unified research document that should give you a strong overview of the target market.

Here is a summary of the UMP and UMS:

[PASTE ONE MECHANISM: "The Problem (UMP) - <name>" with its explanation, then "The Solution (UMS) - <name>" with its explanation]

===
For this exercise, let's specifically focus on people in the market who are [Problem Aware | Solution Aware].

[ONLY FOR SOLUTION AWARE: paste the awareness profile block below]

Please go ahead and write the Unique Mechanism section in a format that could be used in a video sales letter.
```

Awareness block pasted in the Solution Aware examples (eye serum; replace with your own research):

```text
Here's how you can understand Solution Aware in this context:

### The Solution Aware (Estimated 40-45% of TAM)

Profile: Representing the largest segment of the market, the Solution Aware consumer has made a significant leap. She knows her problem (e.g., wrinkles, dark circles) and now knows that a category of products—generically referred to as "eye cream" or "eye serum"—exists to address it. Her primary goal is to find the "best" one for her specific issue. However, at this stage, her understanding is typically not rooted in ingredient science. She evaluates products based on brand reputation, price, packaging, key benefit claims (e.g., "brightening," "firming," "hydrating"), and, most importantly, social proof in the form of reviews and recommendations.
```

- **Source:** [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md); doc `04-4 Claude_UMP Expansion Prompt.docx`, which opens "Reminder: Use this Prompt in the Unique Mechanism Claude Project (See Separate Training For How to Set This Project Up)". Four filled examples: 1–2 Airbnb (Problem Aware), 3–4 eye serum (Solution Aware).
- **Status:** verbatim (bracketed lines are the lesson page's fill-in markers).
- **Also appears:** short form at [03-03 20:35](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) (same text, Problem Aware only); spoken version "Go ahead and write this section in a format that could be used in a video sales letter".
- **Notes:**
  - "Estimated 40-45% of TAM" and the persona are that product's data, not defaults. [03-04 Prompts](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - Expect 2–4 rounds of correction (M5–M9). The output usually needs fixes to awareness fit, names and analogies.
  - ⚠ compliance: expansions add proof elements (named studies, percentages, institutions). Mark every one `[VERIFY: study / number]` and substantiate before it enters the UM doc.

### M5. Reframe the mechanism after the first version
- **Use when:** the first expansion is close but the core framing is off; you state the better frame and ask for a new version.
- **Inputs:** your corrected framing in one or two sentences.

```text
I think this is great, but I wonder if it's really an "income gap world" vs "asset gap world". It's more that they think they have an income gap, but what they really have is an asset gap. We show you how to bridge that gap. People don't get rich from income; they get rich from assets. Write another version of the UMP that takes this into consideration.
```

- **Source:** [03-03 26:40–28:19](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) (Airbnb run).
- **Status:** reconstructed (ad-libbed, Whisper-garbled; a pattern, not a quote).

### M6. Combine several mechanisms into one
- **Use when:** several expanded options each have a strong piece and you want the model to merge them around the market's main pains.
- **Inputs:** the main pain categories from research.

```text
If you were going to take these different mechanism options, and combine them into a new mechanism that you thought was the strongest and that speaks to their pain points (which are primarily appearance driven, followed by what they don't like about products), what would you do?
```

- **Source:** [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) (typed on screen).
- **Status:** verbatim.

### M7. Correct an awareness mismatch in the output
- **Use when:** the model's copy assumes knowledge the target segment doesn't have.
- **Inputs:** the offending line quoted back, plus what you specified.

```text
Okay a couple of things. First, you said: "The reason your peptide eye creams haven't worked isn't because peptides don't work. It's because they've been targeting the wrong problem entirely," but I had specified that solution aware people we are talking to aren't necessarily aware of peptide eye creams right?
```

- **Source:** [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) (typed on screen).
- **Status:** verbatim.
- **Notes:** quoting the exact line back and naming the instruction it broke is Stefan's standard correction pattern (see also [U6](#u6-cross-sell-script-and-its-three-feedback-rounds)).

### M8. Pick the mechanism names
- **Use when:** the model offered name options and you choose and adjust them.
- **Inputs:** your chosen names.

```text
I like: the idea of our: Structural Renewal System

I like: "The Targeted Repair Kit" but let's call it a Targeted Repair Complex

And third let's go with: Integrity Locking Compou[nds]
```

- **Source:** [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) (typed on screen; the last word is cut off).
- **Status:** verbatim (last word partial).
- **Notes:** after the picks he continued: "Address number one: now that you agree, let's use collagen architecture breakdown... Let's use the fabric weave analogy." [03-04 1:10:11–1:10:45]

### M9. Ask for more believable names and analogies
- **Use when:** a UMP or UMS name sounds invented or too technical, or the analogy doesn't fit the market.
- **Inputs:** the names and analogy you reject, and why.

```text
Second, I don't love the name "Dermal Disarray", and I'm not sure about the tent analogy. What other more believable, legit-sounding names can we use instead of Dermal Disarray? And what are some other analogies or metaphors we could use instead of a tent, keeping in mind our target market?
```

```text
For the UMS, I don't love "biotensegrity system" as a name; I want something easy to understand. "Protective shield" is okay but kind of generic. What are alternative names for each of these?
```

- **Source:** [03-04 1:08:25; 1:13:18](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md).
- **Status:** reconstructed (spoken, partly garbled; a pattern, not a quote).
- **Notes:** test for every name: "easy to understand", "believable, legit-sounding", fits the target market. Don't over-weight cute names; the UMS must be tangible. [03-02 38:45–40:16](../lessons/03-02-ump-ideation-with-llms.md)

### M10. Weird UMP brainstorm (AgentGPT)
- **Use when:** you want deliberately outside-the-box UMP ideas for brainstorming only, after the standard process.
- **Inputs:** your niche in the "Now we're working on…" sentence; your own example set; the final paragraph rewritten for your niche.

```text
You're a world-class direct response copywriter who specializes in writing ultra-compelling, attention-grabbing, high-converting video sales letter scripts (VSLs).

You're especially good at writing about Unique Mechanisms for health sales letters. As a world-class copywriter you know that the Unique Mechanism is divided into two parts: The Unique Mechanism of the Problem (UMP) and the Unique Mechanism of the Solution (UMS). The UMP reveals a real and surprising cause of the main pain point that a prospective customer is experiencing. It's something unique and differentiated from the market, yet it should intuitively make sense.

The UMP copy often also has specificity and sometimes things like "testable proof". The UMS is how you fix that unique problem. Both contain: Specificity: Using the specificity of certain names (Harvard, Nobel Prize Winning Scientists), numbers (boosted by 110%, skyrocketed fourfold) and other kinds of specifics to convey proof and believability. Think about names and numbers.

Testable Proof = Make an argument or statement that the reader can instantly check for themselves. (I.e. if you're explaining that people don't have great willpower, you could say "That's why gyms are busy in January and empty in July"). Since most readers can instantly verify that, it carries a lot of weight.

You are an absolute master at writing UMPs and UMSs and making sometimes complex topics very compelling and understandable to the average reader, even those who read at a 3rd grade level. And getting them to happily read your sales messages. Now we're working on coming up with new offer ideas for a health supplement in the blood sugar and Type 2 diabetes niche, and we want to generate some really interesting UMP ideas.

For example, one big health supplement product that recently had a lot of success argues that your pineal gland, a tiny organ in the middle of your brain, is actually a secret and powerful tool that allows you to attract wealth and abundance, but right now it's clogged. The UMS is to unclog the pineal gland using ingredients in the supplement. Below are some examples of what big outside the box ideas might look like for manifestation. But please note manifestation is just a random example - and not what the focus of this blood sugar supplement is. I just want to find really interesting and out of the box angles and UMP ideas for blood sugar.

[Example] Problem: Lack of alpha brain waves restricts effective manifestation. Alpha brain waves are associated with a state of "flow" and creativity, which is crucial for effective manifestation.
Solution: A special supplement that can help boost the production of alpha brain waves, thereby enabling effective manifestation. Reasoning: Most people are unaware of the role of brain waves in the manifestation process. Highlighting this little-known fact and offering a solution can make the offer stand out in the marketplace. [End Example]

[Example] Problem: An excess of negative ions in the body inhibits manifestation. Negative ions can disrupt cell function and impair mental clarity, making it challenging to focus on and manifest desires.
Solution: A pioneering supplement fashioned to neutralize negative ions, bolstering mental function and manifestation abilities. [End Example]

[Example] Problem: Lack of coherence between our heart and brain, also known as heart-brain incoherence, can obstruct the flow of energy and impede our manifestation power. Studies by the HeartMath Institute suggest that the heart and brain communicate with each other, and coherence between them can enhance overall wellness and manifestation abilities (McCraty et al., 2009).
Solution: Our supplement contains unique ingredients that promote heart-brain coherence, facilitating a smooth, unobstructed flow of energy, and enhancing our power to manifest our desires. [End Example]

[Example] Problem: Lack of neural pathways for success intentions, making manifestation more challenging. Research shows that the brain can create new neural pathways through visual or verbal repetition, which can increase one's ability to succeed with their intentions. Right now your neural pathways may be blocked and it's stopping you from manifesting
Solution: A revolutionary supplement that aids the brain in creating new neural pathways, thereby improving one's ability to manifest their intentions more effectively. [End Example]

[Example] Problem: A lack of serotonin, the happiness hormone, can make it difficult for individuals to manifest their desires. When our brain lacks enough serotonin, we tend to have negative thoughts and emotions, reducing our manifestation abilities. So basically it's not your fault - your brain can't manifest positive things in a negative state!
Solution: A unique supplement that naturally boosts serotonin levels, thereby improving your mood and enhancing your manifestation abilities. [End Example]

[Example] Problem: Research shows that our manifestation abilities are directly linked to our gut health. An unhealthy gut can lead to a foggy brain and low energy levels, which can hinder our manifesting potential. This is powerful because basically it applies to anyone who suffers from brain fog, feels groggy for hours in the morning, or has mental crashes later in the day. What you don't realize is that there's essentially this cloud or "energetic curtain" wrapped around your brain that is neutering your brain and making manifestation impossible.
Solution: A unique supplement packed with essential probiotics and other vital nutrients to restore gut health, leading to increased clarity and improved manifestation abilities. [End Example]

Your job is to come up with as many unique and compelling UMP ideas as you can. These should be DIFFERENT than the ones shared in the examples. They should be other ideas around law of attraction, manifestation, etc. They should be very unique, outside-the-box, etc. They should be new, interesting, and compelling ideas. You can search the web to add in proof elements or make compelling arguments for these UMP ideas too, just make sure to include citations. Go ahead and give it a try now.
```

- **Source:** [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md); PDF "Alternate 'Weird' AgentGPT UMP Process" (full text).
- **Status:** verbatim.
- **Notes:**
  - Course quirk: the final paragraph asks for manifestation ideas, not blood-sugar ideas. Rewrite it for your niche. [03-05 Prompts](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)
  - Stefan treats the project and this prompt as an experiment: "not what I do all the time". [03-05 00:28; 01:28]
  - ⚠ compliance: the prompt tells the model to add specificity with "names (Harvard, Nobel Prize Winning Scientists), numbers (boosted by 110%, skyrocketed fourfold)" and the examples are fictional health mechanisms (pineal gland "clogged", "negative ions"). Structure only; claims not reusable. Compliant edit: replace the specificity sentence with "Use specificity only from sources I supply or real studies you cite with links; mark anything else [VERIFY]." and add "Health ideas are brainstorm only; no disease claims." Never use an output idea until its mechanism is backed by real evidence.

### M11. Mechanism definition block (input)
- **Use when:** you need a compact, course-worded definition to paste into any prompt or project that must understand UMP/UMS.
- **Inputs:** none.

```text
A unique mechanism explains why the prospect is struggling or suffering to achieve a goal, and how they can overcome that problem. It is always a two-part logical connection:
1. The unique mechanism behind the PROBLEM (why they failed in the past; the "knowledge gap", ONE CRUCIAL PIECE OF INFORMATION they were missing)
2. The unique mechanism behind the SOLUTION (why our product succeeds where alternatives failed; logically connected to the problem)
Find one major, throbbing pain point and try to fix it.
```

- **Source:** [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) (condensed from the Copy Accelerator template and Genesis doc).
- **Status:** derived condensation; wording is the course's. The full primer is inside [M1](#m1-one-off-ump-ideation) and [M3](#m3-mechanism-evaluation-and-ranking).

## Brief
Pipeline output: **Brief 2.0**, the 25-field "New Brief" filled by the Brief Generator project ([P2](#p2-brief-generator-project)) from the unified research doc, the UM doc and (optional) ingredient research, then corrected by you. [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md) · [concept](../concepts/brief-2-0.md) · [framework](../frameworks/brief-generator.md)

### B1. Generate a new brief
- **Use when:** in the Brief Generator project, to turn research and mechanism docs into a full Brief 2.0.
- **Inputs:** brand and product name; product page URL (if any); attachments: UM doc, unified research doc, ingredient research.

```text
I want your help generating a new brief for our brand Opal Beauty's Unity Eye Serum. Here is a current product page where you can pull some inputs:

https://tryopal.com/products/unity-eye-serum

Additionally, I am attaching a UMP and also some market research that you can pull from when writing the brief.

I’m also including a document with the ingredients and relevant studies.

Please go ahead and get started now.
```

Variants of the same prompt (each is the complete file text):

Airbnb arbitrage (no URL; attachments: UMP doc, research, offer overview):

```text
I want your help generating a new brief for our Airbnb Arbitrage Coaching Program.

I am attaching a UMP and also some market research that you can pull from when writing the brief.

I’m also including a document with some additional relevant information.

Please go ahead and get started now.
```

Financial newsletter (the highlighted words are the only per-offer edit; one attachment: the starting-assets doc):

```text
I want your help generating a new brief for a Financial Newsletter VSL.

I'm attaching a document with additional relevant information.

Please go ahead and get started now.
```

- **Source:** [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) doc `Eye Serum Prompt Example.docx`; [05-03](../lessons/05-03-airbnb-arbitrage-example.md) doc `Example Prompt.docx`; [05-05](../lessons/05-05-financial-promo-example.md) course file "Example Prompt".
- **Status:** verbatim.
- **Also appears:** [01-01 ~16:00](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) (closing two lines on screen, partial) and [01-01 13:54](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) (spoken paraphrase, derived: "…If any detail is missing, use placeholders.").
- **Notes:**
  - The model fills gaps with placeholders by design (project instruction). Review every field; replace placeholders with real facts or leave them visibly bracketed.
  - The 25 headings of the output are exactly the New Brief questions ([B10](#b10-the-new-brief-project-knowledge-file)).
  - ⚠ compliance: fields 15 (testimonials), 16 (credibility builders: "Harvard scientists… Tony Robbins endorsed… featured in Forbes"), 17–19 (prices) and 22 (scarcity) invite invention. Add to the prompt: "Use only testimonials, endorsements, press, prices and scarcity found in the attachments; otherwise write [VERIFY: …]."

### B2. Placeholder brief from ingredients only
- **Use when:** you have only an ingredient list and studies (no real offer yet) and want an example brief to react to.
- **Inputs:** ingredient list and studies attached; narrator perspective.

```text
I want your help generating a new brief for a new blood sugar supplement VSL.

I am attaching ingredients list and studies for your reference.

Please use placeholders to come up with the strongest brief possible. I will switch out everything later, but I want to see an example of what this brief can look like.

Let's have this VSL come from the perspective of a woman who has a personal struggle with diabetes (either her own blood sugar is high, or someone close to hers is) and who meets an expert who helps show her the real solution.

Please go ahead and get started now.
```

- **Source:** [05-04](../lessons/05-04-blood-sugar-supplement-example.md); doc "Example Prompt". Spoken version [00:33] differs slightly.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: "use placeholders to come up with the strongest brief possible" produces invented experts, studies and testimonials, and the blood-sugar topic invites disease claims. Use only as a draft skeleton. Before any copy is written, replace every placeholder with real facts or `[VERIFY: …]`; supplement claims stay structure/function ("supports healthy blood sugar levels already in the normal range"), with no "diabetes" treatment claims.

### B3. Revise the brief (pricing, speaker, bonuses)
- **Use when:** the first brief is good; you correct the offer and narrator decisions in one message.
- **Inputs:** pricing display decision, main speaker and their story, expert role, partner brand, bonuses.

```text
This was great overall. Really good job. Here are a few tweaks or pieces of information for revisions.
First off, for the pricing, let's go with the one-time purchase pricing in the VSL and show the subscribe and save options below the VSL.
Second, the main speaker would be Laura. She's a mom of two in Florida.
Dr. Schilling helps explain what's really going on, the UMP and UMS. The whole VSL will come from Laura, recounting what Dr. Schilling shared. Ultimately, Laura partnered with her husband to create Opal Beauty.
Lastly, go with no bonuses.
```

- **Source:** [05-02 19:03–20:19](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md).
- **Status:** reconstructed (spoken; wording approximate).
- **Notes:** ⚠ compliance: "Laura" and "Dr. Schilling" are course personas; Stefan says Dr. Schilling was a paid spokesperson [07-01 v1 39:14] (instructor claim). For our brands the speaker and the expert must be real people who agreed to the role, and their credentials must be verifiable.

### B4. Correct the audience
- **Use when:** the brief narrowed the audience too far.
- **Inputs:** your audience correction.

```text
I think the audience is women and men. I think having it be primarily women is fine, but I wouldn't ignore men.
```

- **Source:** [05-04](../lessons/05-04-blood-sugar-supplement-example.md) (typed in the chat box).
- **Status:** verbatim.

### B5. Second brief version told from the doctor
- **Use when:** you want an alternative brief with a different narrator and discovery story to test.
- **Inputs:** narrator, the story beats, `BRAND` (literal placeholder in the prompt).

```text
This is great, thank you. Now I would like to see a second version of the brief, where it comes from the doctor. Let's have him share the story of a patient who was at her wits end about her high blood sugar. We can tell more about her suffering and then the doctor felt helpless, and decided to go on a quest to figure out why so many like this patient still struggle with high blood sugar despite all the medications, artificial sweeteners and other solutions out there. This ultimately led him to discover the UMP, the UMS, the ingredients, and then he created the formula with the help of BRAND.
```

- **Source:** [01-01 ~17:00](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) (on screen, complete sentence).
- **Status:** verbatim.
- **Also appears:** [05-04 12:36](../lessons/05-04-blood-sugar-supplement-example.md) (same text, cut off at "he created a"; spoken [10:53–11:35] garbled).
- **Notes:** ⚠ compliance: the doctor, the patient and her story are invented. Under repo rules this is a hard stop for real copy unless a real clinician authored or approved the story and the patient case is real and consented. Compliant edit: "…where it comes from [REAL EXPERT, credentials]. Use only the patient story in the attachment; if none, write [VERIFY: real patient story with consent]." Also remove "despite all the medications": the copy must not position a supplement against medication.

### B6. Recovery when the model ignores the attachment
- **Use when:** the brief came back generic because the model did not use the doc you attached.
- **Inputs:** the name of the attached doc.

```text
Well it's the Genetic Royalty Revolution example brief. That's what I'm referring to. This already did some of the legwork for you. Now you just need to put that into the New Brief template, and also fill out the rest of the New Brief Template with placeholder information.
```

- **Source:** [05-05 ~09:52](../lessons/05-05-financial-promo-example.md) (read from screen).
- **Status:** partial (begins mid-thought; the spoken lead-in may differ).
- **Notes:** failure mode: first run ignored the attachment. Name the attachment explicitly in the first prompt ("Use the attached [doc name]…") to avoid it.

### B7. Draft an offer overview with an LLM (training examples only)
- **Use when:** building a practice or case-study offer with no real product (Stefan does this for course examples).
- **Inputs:** offer type; attachments: unified research doc, UMP.

```text
[Offer type, e.g. high-ticket coaching program] sales funnel. Sketch the program details here. I can use it as an example. Also create a fictional spokesperson and other relevant data.
[Attach: unified research doc, UMP]
```

Headings of the resulting offer overview (verbatim headings from "Example Starting Assets_Airbnb Arbitrage"), the attachment for B1's Airbnb variant:

```text
1. Program Title:
2. Spokesperson / Guru Persona: (Name, Archetype, Backstory, Positioning)
3. The Coaching Program Brand & Core Promise: (Brand Name, Core Promise)
4. The Core Curriculum: "The Asset Accelerator™ Blueprint" (Modules 1-8, each with Concept and Deliverables)
5. The High-Ticket Coaching Components (The "Why We're Different")
6. The Offer, Pricing & Guarantee: (Price, Guarantee)
```

- **Source:** [05-03 03:31](../lessons/05-03-airbnb-arbitrage-example.md).
- **Status:** reconstructed (spoken, approximate).
- **Notes:** ⚠ compliance: "create a fictional spokesperson and other relevant data" is a hard stop for real products. For our brands, the offer overview must contain the real offer, price, guarantee and spokesperson; use the headings only as a checklist.

### B8. Ideate a hypothetical offer from a winning VSL (training examples only)
- **Use when:** creating a teaching example modeled on a winning sales letter.
- **Inputs:** the winning VSL attached.

```text
I'm doing a copywriting course where [I show how to use] AI to create different formats of copy. Right now I'm working on long-form copy. I want to do an example in the financial space. [Attached: Agora Financial Secret Trust Fund VSL.pdf] Come up with a hypothetical offer for the financial space that's kind of similar to this one but different enough to be used for teaching purposes. Can you share some ideas?
```

- **Source:** [05-05 00:00–00:31](../lessons/05-05-financial-promo-example.md); follow-up: ask for "an example brief that I can use for a case study" for the chosen option [01:43].
- **Status:** reconstructed (from speech and the visible start of the chat; not a file).
- **Notes:** ⚠ compliance: fictional offers and financial promises are not reusable copy. Use the pattern only to study a structure.

### B9. Update the brief with chosen big ideas
- **Use when:** after brainstorming hooks or big ideas, you lock which ones the VSL will lead with and tease, and push them back into the brief.
- **Inputs:** the chosen big idea, the tease line, any later payoff.

```text
Okay I like the 30 second blood sugar reset ritual. I do like the phrase "The Missing Page From Every Medical Textbook" not as a big idea, but something that can be teased on the lead. And I like my idea of the Himalayan Rice Hack and then later we can pay off that the hack is actually related to a spice or flavoring that gets added to rice. Can you update the brief to incorporate this information for please?
```

- **Source:** [07-01 v6 9:36](../lessons/07-01-long-form-vsl.md) (on screen).
- **Status:** verbatim.
- **Notes:** ⚠ compliance: "The Missing Page From Every Medical Textbook" and a "30 second blood sugar reset ritual" imply medical suppression and fast results. Structure only; claims not reusable. If a ritual or hack is teased, its payoff must be true and substantiated.

### B10. The New Brief (project knowledge file)
- **Use when:** setting up the Brief Generator project ([P2](#p2-brief-generator-project)): upload this blank template as knowledge file #1 (file #2 is the classic VSL outline, in [templates.md](templates.md) and [04-01](../lessons/04-01-vsls-section-overview.md)).
- **Inputs:** none; the generator fills it.

```text
Brief

1. Who’s the Audience?

2. What are the pain points, or biggest fears?
(+ identify the 1-3 HUGE ones, while the rest are secondary)
- Short Term:
-Long Term:

3. So by reversing the pain points/biggest fears, what are the big promises you are going to make about the sales copy they’re watching…how this will change their lives forever?
(These are promises about what they will get from interacting with the sales copy, or for teasing a solution you’ll be showing them in the sales copy).

4. What Does It Look Like When A Prospect’s Pain Points Have Been Solved?
This can include physical, emotional, social and psychological benefits.

5. What solutions for the reader’s problem (s) exist already (and why aren’t they working for them)?

6. What is the Unique Mechanism of the Problem and the Unique Mechanism of the Solution?
Please include enough detail so that when given to an LLM, it could write this whole section without struggling.

7. Is There A Unique Nickname for the Unique Mechanism?
This is something that would be teased early on in the lead of the VSL. For example the “7 second bowel releasing ritual” or the “30 second breakfast hack” or “Paper Flipping” to tease a real estate arbitrage method.

8. (Optional, For Supplements): What are the main ingredients in the formulation.
For each main ingredient, include 2-3 studies showing their efficacy.

9. Bold Product Claims
(What’s the huge promise or promises about the results they’re going to get using this product/solution? Note, this is different than the promises from #3. These are now specific promises and claims about how their life will change for the better once they buy the product):

10. What is the Product?
(This is where we’ll include product details. This might include features and benefits for physical products and programs. It might include fascinations or curiosity bullet teasers for informational programs. The more detail here the better).

11. Background Story + Story of Discovery:
This is often a hero's journey structure. The spokesperson or someone the spokesperson knows was in pain. The spokesperson ends up on a quest to find an answer to their pain point. They end up discovering the unique mechanism, why existing solutions don’t work, etc.

12. Who is the main speaker in the VSL?
Include a quick snapshot of who they are and their credibility.

13. Is there a second speaker or “expert’ who also has a large role in the VSL?

14. Does the spokesperson partner with a brand or company once they’ve discovered the product?
If so, please share information about the brand or company here.

15. List of Testimonials or Social Proof If Available

16. Include any Credibility Builders that can be used in the opening of the sales copy.
This could reference studies about the ingredients, or about the UMP, etc. Perhaps Harvard scientists uncovered the real cause of your problem. Maybe Tony Robbins endorsed this solution? Maybe the program has been featured in Forbes or Good Morning America. Etc.

17. What Is The Normal Retail Price For The Product Being Sold?

18. What Is The Actual Price People Who Watch the VSL Will Pay?

19. If the VSL sells a product with multiple options, what are those options and what is the pricing for each option?

20. What Is The Guarantee?

21. Are There Any Bonuses?
If so please list them out.

22. Please List Out Any Other Scarcity Elements If There Are Any.

23. Please Write Out Specific Future-Paced Results and Benefits People Could Expect To Experience After Using the Product.

24. What Are Common Objections Prospects Might Have When Watching the VSL, and How Can We Answer Them?

25. Are there any specific Hooks or Big Ideas that you think should be tested in the lead of the VSL?
```

- **Source:** [05-01](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md); doc `01-12 The New Brief.docx`. The Classic RMBC Brief (12 fields, `01-11`) is on the same lesson page.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: field 16's examples ("Perhaps Harvard scientists uncovered the real cause… Maybe Tony Robbins endorsed this solution? … featured in Forbes or Good Morning America") are illustrations of the field, not facts to generate. Fields 15, 16 and 22 must hold only real, documented items or `[VERIFY: …]`.

## Claude Project instructions
One project per asset type: a short instruction block plus varied example files in project knowledge; per-task inputs (brief, URL, landing page) go in the chat, not the project. Stefan pastes the same text into the project's description and instructions fields. [05-02 00:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) · [03-05 00:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) · [concept](../concepts/claude-project-recipe.md)

| ID | Project | Knowledge files (course) | Typical first chat prompt |
|---|---|---|---|
| P1 | Unique Mechanisms | 9 PDFs: mechanism definitions with examples, call transcripts, VSL structure, Copy Accelerator UM template, Genesis UM doc, Beverly Hills MD Pinch Test UMP, the "weird" UMP process | [M1](#m1-one-off-ump-ideation), [M3](#m3-mechanism-evaluation-and-ranking), [M4](#m4-mechanism-expansion-into-vsl-copy) |
| P2 | RMBC II Brief Generator | The New Brief (blank) + classic VSL outline | [B1](#b1-generate-a-new-brief) |
| P3 | Claude Long Form VSL Generator | 8 long transcripts (Mitolyn, Synocell, Emma template, Genius Wave, Beverly Hills MD Pinch Test, Agora Secret Trust Fund, Backyard Liberty, biz-opp book-a-call) | [V1](#v1-long-vsl-outline-request) |
| P4 | Claude Medium Length VSL Generator | 5 medium transcripts (Beverly Hills MD, 2× Gundry, Miami MD, Nooro) | [V14](#v14-outline-with-a-length-estimate) |
| P5 | Claude 3-7 Minute VSL Generator | 8 scripts (Akka, City Beauty, Emma, Gundry, Nooro 7-min, Pup Labs, ReActivate, Vital BP) | [V20](#v20-five-3-7-minute-concepts-from-a-brief) |
| P6 | Claude Short Length VSL Generator | 1 combined PDF of 12 short scripts | [V28](#v28-ten-short-vsl-concepts-from-a-product-page) |
| P7 | Hook-heavy Meta ads (ADHD Super-Hook) | Ad breakdowns doc + hook database | [H5](#h5-start-a-hook-heavy-ad-session) |
| P8 | Advertorials | 14 advertorial PDFs (6 short, 4 medium, 4 long), nothing else | [A3](#a3-ten-advertorial-hooks-from-a-source-document) |
| P9 | PDPs | none (Stefan decided not to build one) | [D1](#d1-extract-a-pdp-outline-from-two-product-pages) |
| P10 | Meta captions generator | 10 Meta ad captions | [AD1](#ad1-meta-ad-captions) |
| P11 | Claude Upsell Generator (Longer Scripts) | 5 upsell swipes (Emma, Synocell, Sample Upsell 1, Sabri Suby, Stem Cell Restore) | [U5](#u5-more-of-the-same-upsell-from-a-product-url) |
| P12 | Claude Email Sequence Generator | examples of abandon cart, welcome, promo, reorder and winback series | [E1](#e1-abandon-cart-sequence-with-a-discount-ladder) |

Sources for the knowledge lists: [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md), [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md), [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md), [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md), [09-02 03:00–05:52](../lessons/09-02-claude-project-for-advertorials.md), [12-01](../lessons/12-01-meta-ads.md), [14-03 00:29–00:59](../lessons/14-03-claude-projects-for-upsells.md), [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md).

⚠ compliance (all projects): the course example files are full of invented doctors, testimonials, studies and disease claims. A project models what it is fed. For our brands, load compliant examples (or our own winners) and add one line to every instruction block: "Never invent testimonials, reviews, experts, studies, statistics, results, prices or scarcity. Use only facts from the brief or attachments; where proof is missing write [VERIFY: …]."

### P1. Unique Mechanisms project
- **Use when:** setting up a reusable context for mechanism ideation, evaluation and expansion.
- **Inputs:** none at setup; 9 PDFs in knowledge.

```text
Were going to create a GPT that helps people come up with new Unique Mechanisms for Direct to Consumer and direct response oriented marketing campaigns. I'll upload several documents - the core one will be what Unique Mechanisms are (both types) WITH Examples and we'll have other documents uploaded as well that train you on the process.
```

- **Source:** [03-05 00:58](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) (docx "Claude Project Description and Instructions").
- **Status:** verbatim. Typos "Were" and "GPT" are in the source; the text predates Claude Projects. Replace "GPT" with "assistant" when reusing (derived).
- **Notes:** description and instructions get the same text [03-05 00:28]. Stefan calls this an experiment, "not what I do all the time". [00:28; 01:28]

### P2. Brief Generator project
- **Use when:** setting up the project that turns research + UM docs into Brief 2.0.
- **Inputs:** knowledge: The New Brief ([B10](#b10-the-new-brief-project-knowledge-file)) and the classic VSL outline ([templates.md](templates.md)).

```text
Your Job is to Create New Briefs for Copywriting Projects. These are things that I can give to Claude Projects or other LLMs to have them write copy. We’ll mostly be focused on VSLs here, but I may end up asking you to create a brief for an eCommerce page in the future as well.

I’ve included two documents in your knowledge base for now.

The first is an in-depth brief. It is titled “The New Brief.”

The second is an outline of the classic Video Sales Letter Structure I’ve used for a long time. That one is mostly for reference.

Here’s how this will work:

I will use your chat feature to provide documents that can assist you in writing the brief for a specific product. You’ll then do that. For anything where you don’t have information, you can use placeholders to start.
```

- **Source:** [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md); doc `02-21 Brief Generator_Claude Projects.docx`. Project named "RMBC II Brief Generator" on screen.
- **Status:** verbatim.
- **Notes:** "you can use placeholders to start" is why outputs contain invented names and numbers. Treat every placeholder as `[VERIFY]` until replaced.

### P3. Long Form VSL Generator project
- **Use when:** writing 25–60 minute VSLs.
- **Inputs:** knowledge: 8 long-form transcripts.

```text
New Project Name:
Claude Long Form VSL Generator

Your job is to generate long form video sales letters. They will typically be between 25 minutes and 60 minutes in length. The documents in your knowledge base include transcripts from several long form VSLs which we can model off while writing new VSLs. What you'll want to do is analyze the structure of the various long form VSL examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new long form VSLs.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current long form VSL project is.

One IMPORTANT Note. Please don't try to rush or condense anything. It's very important that if we're writing a long-form VSL, we're matching the structures and lengths of other long-form VSLs (even when it's a compository structure of several VSL examples from your knowledge base). So whenever you run out of space, just prompt me and I'll tell you to continue.

Prompt Example:

Here are a list of inputs for a new VSL that we are going to be writing. After reviewing them, I want you to come up with an outline for a new VSL based on this inputs. When providing this outline, please provide an estimated length for the new VSL. After I have reviewed the outline and approved I will let you know and we can actually write it.
```

- **Source:** [07-01](../lessons/07-01-long-form-vsl.md) doc "Long Form VSL Generator Claude Project_Setup and Prompts" (complete).
- **Status:** verbatim ("compository" and "based on this inputs" are in the source).
- **Also appears:** [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) Project 1 (identical).
- **Notes:** the "Prompt Example" paragraph at the end is the first chat prompt (outline + estimated length, then approval). Stefan also attached his classic outline mid-chat: "I'd experiment with putting it in the Claude project too." [07-01 v1 32:48]

### P4. Medium Length VSL Generator project
- **Use when:** writing 6–16 minute VSLs.
- **Inputs:** knowledge: 5 medium transcripts.

```text
New Project Name:
Claude Medium Length VSL Generator

Your job is to generate medium length video sales letters. They will typically be between 6 minutes and 16 minutes in length. The documents in your knowledge base includes transcripts from several medium length VSLs which we can model off while writing new VSLs. What you'll want to do is analyze the structure of the various medium length VSL examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new medium length VSLs.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current medium length VSL project is.

One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```

- **Source:** [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) Project 2.
- **Status:** verbatim.

### P5. 3-7 Minute VSL Generator project
- **Use when:** writing mini VSLs, usually run as in-feed Meta ads that sell the click.
- **Inputs:** knowledge: 8 scripts of 3–7 minutes.

```text
New Project Name:
Claude 3-7 Minute VSL Generator

Your job is to generate mini video sales letters that are typically 3-7 minutes long. The documents in your knowledge base includes transcripts from several of these VSLs which we can model off while writing new VSLs. What you'll want to do is analyze the structure of the various VSL examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new VSLs. Please note that most of the time, VSLs of this length are run as in-feed ads on meta. Also, they often do not reveal the product they are selling, and instead tease a new solution or breakthrough, with the call to action being to go watch a video or read a report to get information. That being said, at other times, they may mention the product and mention how people can get a discount. I'll typically specify the goal when asking you to write VSL Scripts.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current short VSL project is.

One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```

- **Source:** [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) Project 3; spoken version [02:55–04:24].
- **Status:** verbatim. "the current short VSL project" is a copy-paste leftover in the source; change it to "3-7 minute" if you like.
- **Notes:** state the goal (sell the click vs mention product and discount) in every chat prompt, as the instruction says.

### P6. Short Length VSL Generator project
- **Use when:** writing 1–4 minute VSLs and video ads.
- **Inputs:** knowledge: 1 PDF of 12 short scripts.

```text
New Project Name:
Claude Short Length VSL Generator

Your job is to generate short length video sales letters. They will typically be between 1-4 minutes in length. The documents in your knowledge base includes transcripts from several short VSLs which we can model off while writing new VSLs. What you'll want to do is analyze the structure of the various short length VSL examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new short VSLs.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current short VSL project is.

One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```

- **Source:** [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) Project 4.
- **Status:** verbatim.
- **Also appears:** [07-04 v1 01:00](../lessons/07-04-short-vsl.md) (visible portion only, same opening).

### P7. Hook-heavy Meta ads project (ADHD Super-Hook)
- **Use when:** writing 1–3 minute hook-dense video ads that sell the click to a VSL.
- **Inputs:** knowledge: (1) in-depth ad breakdowns, (2) your hook database; replace "for a Skincare brand".

Project description ("What are you trying to achieve?"):

```text
The goal is to write hook heavy meta ads.

I want these ads to follow what I call an ADHD Super-Hook Framework. What this means is that the ads will have numerous hooks throughout, including several in the beginning. In fact, the first 30 seconds of the ad especially should jump around a good amount.

As we go to write these ads, I want to incorporate numerous hooks into them (as mentioned). I also want to incorporate what I would call "curiosity driven statements."

Curiosity-driven statements would be statements that are like hooks, but they could be anywhere in the video ad, and typically wouldn't be in question format.
```

Project instructions:

```text
The goal is to write hook heavy meta ads for a Skincare brand.

I want these ads to follow what I call an ADHD Super-Hook Framework. What this means is that the ads will have numerous hooks throughout, including several in the beginning. In fact, the first 30 seconds of the ad especially should jump around a good amount.

As we go to write these ads, I want to incorporate numerous hooks into them (as mentioned). I also what to incorporate what I would call "curiosity driven statements."

Curiosity-driven statements would be statements are like hooks, but they could be anywhere in the video ad, and typically wouldn't be in question format.

You will see that document #1 is 1. CA Pro Copy of Ad Breakdowns (In-Depth). This has in-depth breakdowns of successful ads from other brands. You'll notice how hook heavy they are, especially the openings, and how they also incorporate visual elements that are used to continuously hook people in too.

Then you'll see that I've already included a list of hooks and curiosity driven statements as the second document. That document is titled: 4. CA Pro Version_Hook Database.pdf

You'll be tasked at various times with coming up with new hooks and curiosity statements, coming up with new ad concepts, and writing new ads.

Here's something very important: unless I SPECIFICALLY ask you for it, when writing ads do NOT talk about the product in the ad. Instead we want to tease a breakthrough/solution/ritual and the call to action is "you need to watch this" or "check out this video" etc. We're basically "selling the click" meaning we want to sell them on clicking the link, which will take them to the VSL and sell the product on that page.

Also, when writing ads, your goal is to incorporate numerous hooks into the opening and also throughout. You'll also include what I call "curiosity driven statements" where it's not a question, but a statement from the speaker (could be a UGC person, a doctor, or an AI Voiceover etc) that is curiosity heavy and catches someone's attention.
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "6. Claude Project Setup and Prompt Examples".
- **Status:** verbatim (source typos kept: "I also what to").
- **Notes:**
  - The "do NOT talk about the product… selling the click" rule is the core of this project; drop it only when you ask for a product ad. See [sell the click](../concepts/sell-the-click.md).
  - Build the hook database first with [H1](#h1-deep-research-hook-generation)–[H4](#h4-generate-still-more-hooks-from-a-hook-database).
  - ⚠ compliance: a "doctor" speaker in a sell-the-click ad still needs to be a real, credentialed person; otherwise use a UGC creator or voiceover that makes no expert claim.

### P8. Advertorials project
- **Use when:** writing advertorials from sales pages, landing pages, product details or VSL scripts.
- **Inputs:** knowledge: 14 advertorial PDFs only; per-task inputs attached in the chat.

```text
I will be giving you different sales pages, landing pages, product details, or relevant data points, and you will then be writing new advertorials based off the numerous examples that are in your knowledge base. What you'll want to do is analyze the structure of the various advertorial examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new advertorials.
```

- **Source:** [09-02 01:33–02:29](../lessons/09-02-claude-project-for-advertorials.md); process doc 1. Same text in description and instructions.
- **Status:** verbatim.
- **Notes:** run the three-prompt sequence [A3](#a3-ten-advertorial-hooks-from-a-source-document) → [A4](#a4-outline-one-advertorial-angle) → [A5](#a5-write-the-advertorial).

### P9. PDPs (no project)
- **Use when:** you are tempted to build a PDP project.
- **Inputs:** n/a.
- **Source:** [10-01 52:42–53:40](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md).
- **Status:** no project instructions exist in the course files.
- **Notes:** Stefan planned a PDP project "but I don't think you need it. I would just do it the way I did in this video": pick one PDP you like and have Claude model it in a plain chat ([D1](#d1-extract-a-pdp-outline-from-two-product-pages)–[D7](#d7-fallback-when-claude-cannot-fetch-the-page)). Loading many outlines into a project is "dealer's choice".

### P10. Meta captions generator project
- **Use when:** writing Meta ad primary text (captions).
- **Inputs:** knowledge: example captions (the course uses 10, doc `01-2 Meta Ad Captions for Claude Projects`).

```text
I'm going to give you several examples of meta ad captions in your knowledge base. You'll use these and other knowledge you have about meta ad captions to generate new ad captions based on instructions I put in your chat interface.
```

- **Source:** [12-01](../lessons/12-01-meta-ads.md); doc `01-1 Claude Captions Generator Setup` (complete).
- **Status:** verbatim.

### P11. Upsell Generator project (longer scripts)
- **Use when:** writing 6–16 minute upsell or cross-sell video scripts.
- **Inputs:** knowledge: 5 upsell swipes as PDFs.

```text
Claude Upsell Generator (Longer Scripts)

Your job is to generate upsell video scripts. They will typically be between 6 minutes and 16 minutes in length. The documents in your knowledge base includes transcripts from several upsell videos which we can model off while writing new upsells. What you'll want to do is analyze the structure of the various upsell examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new upsells.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current upsell project is.

One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```

- **Source:** [14-03 0:17](../lessons/14-03-claude-projects-for-upsells.md); doc `1. Claude Upsell Generator (Longer Format).docx`.
- **Status:** verbatim.
- **Also appears:** [15-05 00:17](../lessons/15-05-claude-project-for-writing-email-sequences.md) (same text read from screen, with a "New Project Name:" line).
- **Notes:** add our own winning upsells to knowledge over time. [14-03 00:29–00:59]

### P12. Email Sequence Generator project
- **Use when:** writing abandon cart, welcome, promo, reorder and winback sequences.
- **Inputs:** knowledge: example sequences of each type (discount-led and emotion-led).

```text
New Project Name:
Claude Email Sequence Generator

Your job is to create various email sequences for different products and services. These will range from eCom products, to coaching or information products.

You have several documents in your knowledge base that should provide all of the examples you need to write great sequences. You’ll see that there are several examples for:

Abandoned Cart Series

Welcome Email Series (For New Customers)

Special Sales and Promotions Series (Holiday Sales, Flash Sales, etc)

Reorder Series (For Getting A Customer to Order More of a Product Prior to Running Out)

Winback Series (For Getting a Previous Customer to Once Again Become a Customer).

You’ll also notice that some of the sequences focus more heavily on discounting, while some focus more on emotion.

What will happen is that I will give you instructions about the kind of email sequence I’m looking to have written, as well as the product or service or brand we are writing the sequence for. You’ll then select from relevant examples, synthesizing across several of them when necessary, to create a new sequence.
```

- **Source:** [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md); doc 1 `1. Claude Email Sequence Generator Project Setup` (in full).
- **Status:** verbatim.
- **Notes:** each chat prompt names sequence type, length, discount schedule and product URL, then asks for an outline first ([E1](#e1-abandon-cart-sequence-with-a-discount-ladder)–[E4](#e4-abandon-cart-sequence-from-a-brief)).

## VSL drafting and editing
The loop for every length: brief → outline (with time per block and total length) → copy-chief the outline → "write it" → edit → new leads and hooks. Use the project for the length ([P3](#p3-long-form-vsl-generator-project)–[P6](#p6-short-length-vsl-generator-project)). [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md) · [framework](../frameworks/vsl-build-with-claude.md) · [playbook](../playbooks/write-a-vsl-with-claude.md) · lengths: [VSL length bands](../concepts/vsl-length-bands.md)

**Long form (25–60 min)**

### V1. Long VSL outline request
- **Use when:** in the Long Form project with an approved brief; first step of a long VSL.
- **Inputs:** brief attached; target length.

```text
Here's the brief for a new product and brand to write a new long-form VSL that is about 27 minutes in length. Please [give me] an outline for this new VSL that I can look at, and once approved, I'll have you write it.
```

- **Source:** [07-01 v1 28:33](../lessons/07-01-long-form-vsl.md) (captions).
- **Status:** verbatim from captions; "[give me]" is a lesson fill-in.
- **Also appears:** the project's own "Prompt Example" ([P3](#p3-long-form-vsl-generator-project)); spoken long-project version in [05-02 43:17–44:30](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) (reconstructed): "Write a long form VSL for our brand Opal Beauty. Please provide an outline. Tell me the estimated length. Let's shoot for about 25 minutes long."
- **Notes:** he used Sonnet over Opus for speed [07-01 v1 28:33]. Save the approved outline as a PDF so the same outline can go to a second model ([V7](#v7-draft-the-same-outline-in-a-second-model)). [v1 40:12–41:15]

### V2. Lazy swipe test (model one VSL closely)
- **Use when:** you want to see what a near-direct swipe of one proven VSL's structure and length looks like for your product, as a comparison against a composite.
- **Inputs:** brief attached; the named VSL in project knowledge.

```text
I've uploaded the brief for a new VSL that we're going to write. To start, I want to see what it looks like if we very closely model the structure and length of the Mitolyn VSL that's in your project knowledge, but doing it for this new product and brand. Can you do the first 1,000 words of the new VSL following the Mitolyn structure so I can see what that looks like?
```

- **Source:** [07-01 v1 14:49–15:36](../lessons/07-01-long-form-vsl.md) (screen + audio).
- **Status:** verbatim on screen up to "Mitolyn VSL"; the rest from audio.
- **Notes:**
  - Failure modes seen: Sonnet 4 output was "super weird… nonsensical" and invented "Sarah, a 47-year-old working mom from Phoenix"; the cause was a brief that kept calling the narrator "founder of Opal Beauty". Sonnet 3.7 then copied the Mitolyn lead almost line for line ("bizarre structural renewal exploit… six seconds"). [07-01 v1 17:08–24:54](../lessons/07-01-long-form-vsl.md)
  - His verdict: swipe heavily only if it is already *your* proven VSL; otherwise build a composite. See [composite vs swipe](../concepts/composite-vs-swipe.md).
  - ⚠ compliance: a lazy swipe imports the source's claims ("breakthrough studies from Harvard and Yale") and testimonial counts. Copy the structure only; strip every borrowed claim, name and number.

### V3. Model a named VSL from project knowledge (financial)
- **Use when:** the knowledge base holds a VSL in the same category as the new offer and you want its structure kept very close.
- **Inputs:** brief; the name of the knowledge-base VSL.

```text
Here's a brief for a new financial offer. I want you to model off the structure of the Agora Secret Trust Fund sales letter you have in your knowledge base, to write a new VSL Script for the new offer, based on the brief. Please keep the structure very similar, and if you need to do it over multiple outputs that's fine, just prompt me if you run out of space and I'll tell you to continue.
```

Follow-up after the first draft:

```text
That was a good start. I really liked the opening. But let's really swipe the structure of that Secret Trust fund. Let's have it be the same length almost. Let's have a spokesperson who is interviewing Dr. [Vance...]
```

- **Source:** [05-05 13:18–15:16](../lessons/05-05-financial-promo-example.md) (read from screen). Continue message: "Yes, please do!" [18:18]
- **Status:** partial (both truncated on screen; the second is cut off at "Dr.").
- **Notes:** ⚠ compliance: financial VSL swipes carry income and market-prediction claims. Structure only; claims not reusable. Any return, forecast or "secret" must be substantiated and carry the required risk disclosures.

### V4. Outline feedback: promise, future pace, hold back the brand
- **Use when:** the first outline's lead lacks a solution promise or future pacing, or reveals the narrator, expert or brand too early.
- **Inputs:** your structural corrections.

```text
This is good, but we also want to promise a solution, something that's going to fix their eye area, fine lines, crow's feet, etc. It should picture what life is going to look like for them once they've discovered this solution and used it for themselves.
I also don't think we want to do too much about Laura in the lead. I'm going to talk about Dr. Schilling in the speaker credibility section, unless it's only teasing that an anti-aging doctor revealed something shocking. And we don't want to talk about Opal Beauty until much later: not until the end of the product buildup and reveal.
```

- **Source:** [07-01 v1 29:52–32:48](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (spoken; approximate).
- **Notes:** "copy-chiefing the ideas and the plan" before any copy exists. [07-01 v1 38:07] See [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md).

### V5. Attach the classic structure and revise the outline
- **Use when:** the outline's flow is off; you upload your classic VSL outline ([templates.md](templates.md)) as a guide.
- **Inputs:** classic VSL outline attached.

```text
I'm going to share a classic VSL structure with you. Please check this out for a general idea of how the VSL will flow, and then modify your outline accordingly, based on information in the brief.
```

- **Source:** [07-01 v1 32:48](../lessons/07-01-long-form-vsl.md).
- **Status:** verbatim.
- **Notes:** "I wouldn't always do this, but I want to make sure it gets it right." [v1 32:48] For the medium-length variant that keeps your current structure, use [V15](#v15-remix-the-outline-with-the-classic-structure).

### V6. Make the narrator recount the expert's reveal
- **Use when:** the outline or draft does not connect the narrator's search to the expert who reveals the UMP and UMS.
- **Inputs:** narrator, expert, how they met.

Long-form version (outline stage):

```text
This is pretty good. The one thing I want to make sure we incorporate is how her search for truth led her to meet Dr. Schilling. He is the one who reveals the UMP and UMS. We can say he was referred to her by a friend. Dr. Schilling doesn't need to have a speaking role in this VSL. Instead, it can be Laura recounting what he told her about the UMP and UMS.
```

Medium-form version (before writing):

```text
This looks pretty good. When we get to the big revelation, let's make sure Laura talks about how she was introduced to Dr. Schilling, and he's the one who shared the real reason eye creams fail, and the science of the UMP and UMS. It'll still be Laura speaking the whole time, but she can recount what Dr. Schilling said. Please go ahead and start writing the VSL now.
```

- **Source:** [07-01 v1 36:45–37:23](../lessons/07-01-long-form-vsl.md) (screen + audio; screen text stops at "Instead"); [07-02 v1 01:24](../lessons/07-02-medium-length-vsl.md) (on screen).
- **Status:** verbatim (07-01: screen up to "Instead", rest audio; 07-02: on screen).
- **Also appears:** [05-02 24:26–25:57](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) (spoken, approximate). After approval: "Please go ahead and start writing the VSL now."
- **Notes:** ⚠ compliance: "referred to her by a friend" and the doctor's explanations are story inventions in the course. For our brands the expert, the referral and every scientific statement attributed to the expert must be real and approved by that expert.

### V7. Draft the same outline in a second model
- **Use when:** the outline is approved; you want a parallel draft from another model (Gemini 2.5 Pro in Poe in the course) to merge with Claude's.
- **Inputs:** brief + approved outline attached; length; niche.

```text
We're going to write a new VSL for a skincare brand. It's direct response, going to be 27 minutes long, roughly. I'm attaching the brief and also the outline of how I want it to go. Please start writing the VSL right now. If you need to do this over multiple outputs, that's fine. Whenever you run out of room, simply let me know and I'll prompt you to continue.
```

- **Source:** [07-01 v1 41:15–42:30](../lessons/07-01-long-form-vsl.md).
- **Status:** verbatim.
- **Notes:** rationale: "What if Claude's being weird? What if Claude's down?… You need to be kind of multimodal". Merge section by section (the lesson logs which model won each section and why). Claude claimed "8,500 words"; the actual draft was 5,707. Check length yourself. [07-01 v1 41:15–43:39; v2 34:11; v3 01:13](../lessons/07-01-long-form-vsl.md)

### V8. Write the VSL from the approved outline
- **Use when:** the outline is approved (in a new chat, or the outline is a separate file).
- **Inputs:** outline attached (brief already in the chat).

```text
I'm also attaching the outline for the structure. Please go ahead and write the VSL. If you need to do it over multiple outputs, that's fine. Simply tell me when you run out of space and I'll prompt you to continue.
```

- **Source:** [07-01 v5 18:25–19:35](../lessons/07-01-long-form-vsl.md).
- **Status:** verbatim.

### V9. Fix the mechanism focus in a draft
- **Use when:** the draft's mechanism emphasis is wrong but you want to keep part of it.
- **Inputs:** what to keep, what to make the main focus.

```text
Please update these parts based on my feedback. Again, I don't want to get rid of the DEJ altogether. I actually like saying it starts at the DEJ. Just need to make the main focus this collagen architecture breakdown that happens there.
```

- **Source:** [07-01 v1 05:31–09:12](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (first sentence reconstructed; rest quoted from audio).

### V10. Patch ingredients into a multi-step solution
- **Use when:** the draft's product build-up or close does not map the ingredients onto the mechanism steps.
- **Inputs:** which ingredients belong to which step; where they should reappear.

```text
When we get to the product buildup, I'd like these amino acids referenced in this section as part of the three-step solution. We'll want to mention them again in the ingredient section of the close.

One thing that's not clear is which of these ingredients are related to step three. After all, we said it's a three-step system. How can we make this work? We can add other ingredients in the formula as optional.
```

- **Source:** [07-01 v3 26:53–29:55](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (spoken, approximate).
- **Notes:** ⚠ compliance: every ingredient-to-step claim needs ingredient research behind it ([R7](#r7-ingredient-deep-research-claims-tied-to-studies)); "optional" extra ingredients must not get efficacy claims they lack.

### V11. Book-a-call VSL outline (problem aware)
- **Use when:** a high-ticket or coaching offer where the CTA is booking a call and price is not discussed.
- **Inputs:** brief attached; awareness focus; target length.

```text
I'm attaching a brief for an Airbnb Arbitrage Coaching program, and we're going to be doing a book a call VSL for it. This means we will not talk about the price in it, we'll instead hook people in, educate, and the CTA will be to book a call with the spokesperson and his team to get a personalized plan and to see if they're a good fit to work with them.

One important note is I want this VSL to focus on people who are problem aware, more than solution aware. So I don't want it immediately talking about Airbnb Arbitrage or assuming people have tried programs like that in the past.

To start, please give me an outline for a 25 minute book a call VSL. After I approve, we can move [on to writing it].
```

- **Source:** [07-01 v5 05:02–09:24](../lessons/07-01-long-form-vsl.md) (screen 9:00).
- **Status:** partial (first part verbatim on screen; ending in brackets from audio).
- **Notes:**
  - Outline feedback he gave next (reconstructed): add named case-study teasers "like Joey, who quit his job… and Sam, who was doing deliveries for Amazon… For now please just fill these in with placeholders and I'll get real success stories from Mac later", and repeat them through the VSL. [07-01 v5 10:48–12:19](../lessons/07-01-long-form-vsl.md)
  - ⚠ compliance: placeholder success stories must stay visibly bracketed (`[VERIFY: real client story, name, result, consent]`) and be replaced with real, documented ones before launch; income results need typicality disclosures.

### V12. Fix bridges and logic gaps in a draft
- **Use when:** a transition is abrupt or a section raises an objection the copy hasn't earned the right to answer.
- **Inputs:** the section and the objection you feel as a reader.

```text
I think we need a better transition to real estate. It's kind of abrupt. Maybe we need a few lines to shift the mindset of the prospect so that they are focused on, and accepting of, real estate as a good solution. Something like: you probably think about real estate, but normally real estate requires X, Y and Z.

First, this section: my immediate objection is, oh, that's expensive. So maybe we remove it. After all, plenty of properties will come furnished.
Second, I'm not sure this makes sense because we're talking about arbitrage. We have to be clear before this that as more income comes in, they can use it to actually buy properties and own the assets, and even get property managers to do the work for them.
```

- **Source:** [07-01 v5 33:06; 43:25–44:52](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (spoken, approximate).
- **Notes:** the test he applies: read as the prospect and write down "my immediate objection is…". See [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md).

### V13. Doctor-led outline from brief plus classic outline, then ingredient patches
- **Use when:** an expert-narrated supplement VSL; you want the ingredient section built onto the UMS.
- **Inputs:** brief + classic outline attached; ingredient list with doses.

```text
Here's the brief for a new [doctor-led] offer. I've also included my classic sales letter outline. Please use this information plus the instructions in your knowledge to create a compelling outline for this new VSL.

After the last paragraph of the UMS, build on it by mentioning the ingredients: "I also found X ingredient that works by doing Y, and here are studies proving it."
Can we list what the five other compounds are, and for each one include a line about how it helps? Include the dose.
```

- **Source:** [07-01 v6 11:57–31:37](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (spoken, approximate).
- **Notes:** ⚠ compliance: "here are studies proving it" must cite real studies from [R7](#r7-ingredient-deep-research-claims-tied-to-studies); doses must match the label. An expert narrator must be a real clinician who approved the script.

**Medium (6–16 min)**

### V14. Outline with a length estimate
- **Use when:** in the Medium project with a complete brief.
- **Inputs:** brief; target minutes.

```text
I'm going to upload a comprehensive brief for a new VSL. It should give you everything you need to write it. Please review, and then I want you to give me an outline for this new VSL, along with your estimate for how long it'll be. Let's aim for about 18 minutes.
```

- **Source:** [07-02 v1 03:18](../lessons/07-02-medium-length-vsl.md) (on screen).
- **Status:** verbatim.
- **Also appears:** [05-02 24:24](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) (identical, on screen); quoted in [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md).

### V15. Remix the outline with the classic structure
- **Use when:** the outline is good but you want the model to add what your classic outline has, without discarding the current structure.
- **Inputs:** classic outline uploaded.

```text
This looks really good overall. I've uploaded my classic sales letter outline. While we might not be able to go super in-depth on every aspect of this, I think it helps. Can I see another version of the outline that incorporates things that you think should be added or changed based on this document? Because I don't want to be in the exact same structure as the last one. I really liked what I had before.
```

- **Source:** [07-02 v1 08:48–09:29](../lessons/07-02-medium-length-vsl.md) (on-screen opening + SRT). Then: "Let's go ahead and write it." [v1 10:25]
- **Status:** verbatim (opening on screen; tail from SRT).
- **Also appears:** [01-01 ~19:18](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) (on screen; shorter, ends "…based on the document I just uploaded?").

### V16. Swap the spokesperson and background story
- **Use when:** you want a second version of the same VSL from a different narrator with a different discovery story.
- **Inputs:** brief attached; new narrator and story beats.

```text
[Attach the brief.] Please give me an outline. One important note: I want this version to actually not come from Laura. Let's instead have it come from Dr. Blane Schilling. So we'll want to change the spokesperson and the background story. Let's just have it be that Dr. Schilling is an expert. A woman came into his anti-aging medical practice and said something he'd never heard before. She said she wasn't there because she felt tired or old. She actually felt young and full of life inside. She was there because her skin, especially the area around her eyes, didn't match up with how she felt. She looked tired and old even though she still felt in the prime of her life: wise, confident, empowered. Dr. Schilling was surprised by this. He's an anti-aging doctor, not a dermatologist, but he wanted to help, so he promised to do some research for the lady. What he discovered changed everything you think you know about skincare, wrinkles, eye problems, etc.

This is a cool angle I think, because it can talk about how he was able to find the truth because he was coming at the problem from an outsider's perspective.
```

- **Source:** [07-02 v1 03:31–06:55](../lessons/07-02-medium-length-vsl.md) (dictated; the last sentence confirmed on screen at 07:48).
- **Status:** reconstructed (assembled from SRT and the on-screen tail).
- **Notes:** ⚠ compliance: the patient visit and the doctor's discovery are invented. For real copy, use only a true origin story from a real, consenting expert; otherwise keep the narrator as the founder and tell what actually happened.

### V17. Cut an existing VSL to a target length
- **Use when:** you have a longer VSL and need a shorter cut of the same script.
- **Inputs:** existing VSL; target length; what to keep (alternate openings, CTA).

Medium cut:

```text
Here's a VSL I wrote for an Airbnb arbitrage coaching program. Can you take this and do a version that is 16 minutes long? Keep the three options for the openings, since each video would only have one of those options. So that should be taken into account. It should be the same VSL, just strategically cutting things down to make it fit the length.
```

Short cut (book-a-call):

```text
Please make a 2 minute version of this with the CTA to book a call still.
```

- **Source:** [07-02 v2 00:28–01:53; 03:40](../lessons/07-02-medium-length-vsl.md) (dictated; he first said 18 then "let's do 16 minutes"); [07-04 v2 00:31–02:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** 07-02 reconstructed (dictated); 07-04 verbatim.

### V18. Nine-minute book-a-call outline (problem aware)
- **Use when:** a medium-length VSL for a call-booking offer aimed at problem-aware prospects.
- **Inputs:** brief; length; CTA.

```text
Here's the brief for an Airbnb Arbitrage Coaching program. This is for problem aware people, so we don't want to lead out with airbnb arbitrage. Can you please give me the outline for a medium length VSL that's 9 minutes in total. Note the call to action will be to book a call and get a roadmap, not to sell th[e program].
```

- **Source:** [07-02 v2 09:35](../lessons/07-02-medium-length-vsl.md) (on screen; audio [v2 09:03] says "not to sell").
- **Status:** partial (cut off on screen; bracketed completion is the lesson's reading).

### V19. Medium VSL agent template (derived)
- **Use when:** an agent needs a single reusable prompt for medium VSLs with built-in proof and self-check rules.
- **Inputs:** listed in the prompt.

```text
Role: medium-length VSL writer. Inputs: [brief], [target minutes], [narrator: founder | expert | customer], [CTA: buy | book a call | watch longer video], [awareness level], [classic outline].
1) Outline in the classic blocks with a time range per block and your estimated total runtime. Stop for approval.
2) After approval, write the script in the narrator's voice. Use only facts, proof and numbers present in the brief; bracket any claim that needs substantiation.
3) Self-check: every opened loop is paid off; the mechanism appears before minute [X]; one bridge sentence precedes objection handling; list phrases that sound like AI copy.
```

- **Source:** [07-02](../lessons/07-02-medium-length-vsl.md) Prompts, P8.
- **Status:** derived (not a course asset).
- **Notes:** includes the review prompt he used on the lead: [X1](#x1-second-model-review-of-a-lead).

**3–7 minute (mini VSL / in-feed video ad)**

### V20. Five 3-7 minute concepts from a brief
- **Use when:** in the 3-7 Minute project, starting from a long-VSL brief.
- **Inputs:** brief; spokesperson; CTA; whether to name the brand.

```text
This is a VSL Brief for a skincare product. For 3-7 minute VSLs we might not need all of the information here. Right now I want 5 VSL concepts from you. I want them to come from Dr. Schilling as the spokesperson. Set it up with Laura. [Let's assume the CTA is going to be to watch the video. Don't talk about the brand or product at all. Go ahead and give me some concepts now, please.]
```

- **Source:** [07-03 v1 00:30–02:14](../lessons/07-03-3-7-minute-vsl.md).
- **Status:** verbatim for the first two sentences (on screen); the rest is SRT (bracketed text is a reconstruction). "Set it up with Laura" is as captioned; intent unclear.

### V21. Pick a hook and ask for a timed outline
- **Use when:** you chose one concept or hook and want an outline at a specific length.
- **Inputs:** the hook text verbatim; target length.

```text
Okay these are good, but let's use this hook first:
The Department Store Mistake
"Don't make this $400 mistake at the department store... The saleswoman will convince you that more expensive means better results. But when your skin's structure has collapsed, price doesn't matter - THIS is much more important.

Let's do an ad that is roughly 3 minutes and 30 seconds. Please outline it for me now.
```

- **Source:** [07-03 v1 04:53](../lessons/07-03-3-7-minute-vsl.md) (on screen).
- **Status:** verbatim.

### V22. Shorter sibling of a finished ad
- **Use when:** you have a good 3–4 minute ad and want a shorter cut.
- **Inputs:** target length.

```text
This is awesome. Now please do a 1 minute and 30 second version.
```

- **Source:** [07-03 v1 08:32–08:47](../lessons/07-03-3-7-minute-vsl.md).
- **Status:** reconstructed (spoken).

### V23. Video-ad outline from a brief and an opening hook
- **Use when:** you have a brief and a chosen hook and need a sell-the-click ad that sends viewers to the full VSL.
- **Inputs:** brief; length; opening hook; CTA.

```text
Here's a brief for a blood sugar supplement offer. Please come up with an outline for a 3 minute video ad. It will go to the longer VSL, so the CTA of this video ad will be to get people to go watch the full presentation. Let's also make the ad fairly educational while still having lots of curiosity and some promises. Let's use the following as the opening hook: Stop drinking coffee until you see what it's really doing to your blood sugar...
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md); doc `4. Claude Conversation_.docx`.
- **Status:** verbatim.
- **Also appears:** [07-04](../lessons/07-04-short-vsl.md) doc "4. Claude Conversation History" with "1 minute and 30" in place of "3 minute" (otherwise identical).
- **Notes:** ⚠ compliance: blood-sugar hooks ("Stop drinking coffee until you see what it's really doing to your blood sugar") must not imply a disease effect the product treats; supplement copy stays structure/function and any food/drink claim needs a source.

### V24. Attach the forgotten brief and lock earlier sections
- **Use when:** you forgot an attachment, or you want later sections revised without the model rewriting the parts you approved.
- **Inputs:** the brief; the last section to keep unchanged.

```text
So I love this, but here's the brief (which I forgot to attach) so we can make that solution tease dialed in. Please don't change anything up to the Revelation/education section.
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md); doc `4. Claude Conversation_.docx`.
- **Status:** verbatim.
- **Notes:** "Please don't change anything up to [section]" is the lock pattern; it also drives the hook-swap prompts ([H11](#h11-swap-the-hook-keep-the-body)).

### V25. Pre-empt an objection, then write
- **Use when:** the outline names an ingredient or idea the market will misread (here: "golden spice" read as turmeric).
- **Inputs:** the misreading to block.

```text
This looks good. One thing, when we reference the golden spice, please mention that it is not turmeric right away, so people don't think it's another thing selling turmeric.
```

```text
Thanks please write the ad.
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md); doc `4. Claude Conversation_.docx`.
- **Status:** verbatim.

### V26. Fix a "Nope" sequence that makes false denials
- **Use when:** a "You think X? Nope." sequence denies things that are true or makes medical claims.
- **Inputs:** the replacement beliefs to knock down.

```text
I think we have to modify this part. I don't think saying too much sugar doesn't cause diabetes makes sense. Or that those things don't. I think we should focus on maybe like: "think fragrance free cleaners are safe?" "What about natural cleaners?" How about ___.
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md); doc `4. Claude Conversation_.docx`. Nope-sequence structure: [templates.md](templates.md).
- **Status:** verbatim.
- **Notes:** the failure mode: the model wrote that sugar doesn't cause diabetes. Read every "Nope" line as a factual claim. ⚠ compliance: the replacement ("fragrance free cleaners… natural cleaners") still links household products to insulin resistance; needs a real source or must go.

### V27. 3-7 minute agent template (derived)
- **Use when:** an agent needs one reusable prompt for mini VSLs that sell the click.
- **Inputs:** listed in the prompt.

```text
Role: 3-7 minute video-ad writer (mini VSL).
Inputs: [brief], [chosen hook, verbatim], [length], [CTA = watch the full presentation], [narrator].
Output 1: outline with time ranges (hook, problem, mechanism, why alternatives fail, solution tease, proof, CTA), then wait.
Output 2 after approval: the script. Keep brand, price and offer out. Use only proof present in the brief; bracket anything that needs substantiation; no disease, cure or "reverse" claims.
For variants: change only the hook and the hook-specific problem section; keep every section from the mechanism onward identical.
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md) Prompts, Q10.
- **Status:** derived (not a course asset).

**Short (1–4 min)**

### V28. Ten short VSL concepts from a product page
- **Use when:** in the Short project with only a product URL; product-forward ads with a shop-now CTA.
- **Inputs:** product page URL; CTA.

```text
Help me come up with 10 short VSL concepts for:
[product page URL]

Let's have all of them speak about the product and the call to action is to "shop now"
```

- **Source:** [07-04 v1 02:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** verbatim.

### V29. Pick a concept
- **Use when:** choosing one concept from a list to write.
- **Inputs:** concept number.

```text
Great, let's do Concept #5 to start.
```

```text
Let's start with Concept #3 please.
```

- **Source:** [07-04 v1 04:00](../lessons/07-04-short-vsl.md); [07-04 v4 08:00](../lessons/07-04-short-vsl.md) (both on screen).
- **Status:** verbatim.

### V30. Short VSL concepts from a brief
- **Use when:** you have a full brief and want short-ad concepts that use only part of it.
- **Inputs:** brief; count; max length; narrator freedom.

```text
Here's a brief for a VSL for our skincare brand. Please review and then give me 5-10 short VSL concepts you think would be worth testing?
```

```text
here's a VSL Brief. Please give me 5 short VSL concepts that are 2 minutes maximum each. They don't have to come from Laura, and some of what is in the brief won't need to make it into these VSLs since they'll be short.
```

- **Source:** [05-02 33:36](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) (on screen); [07-04 v1 10:00–11:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** verbatim.
- **Notes:** 05-02 follow-ups (spoken, reconstructed): "let's go ahead and start with number six. Please write a three minute VSL ad now for this VSL. Don't reveal the price; instead the call to action will be to visit Opal Beauty's website and save." [34:41]; "Great thanks, now let's do #8 and let's keep it to about 2 minutes." (screen [39:24]).

### V31. Use an earlier hook and write
- **Use when:** you prefer a hook from an earlier run over the model's new ones.
- **Inputs:** the hook text verbatim.

```text
Thanks, let's actually use this hook I came up with earlier.
Concept 2: The Expensive Cream Mistake
"The number one mistake women make with anti-aging creams isn't the amount - it's not understanding what's really happening to your skin. That $200 eye cream? It's targeting the wrong problem entirely."

Go ahead and write it now.
```

- **Source:** [07-04 v1 12:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** verbatim.
- **Notes:** ⚠ compliance: "It's targeting the wrong problem entirely" is a comparative claim against competitors; it needs a substantiated mechanism.

### V32. CTA variants of the same ad
- **Use when:** testing CTAs: shop now vs discount-without-price vs watch-the-presentation (sell the click).
- **Inputs:** CTA and what to reveal.

```text
Okay thanks, let's do another version where the CTA is to click the ad and save up to 57% but we don't reveal the prices.
```

```text
Thanks, and one more version, for this one, let's have the CTA be to go watch the presentation that Dr. Schilling has put together that explains everything. For this one let's not talk about the product specifically, let's instead tease a breakthrough.
```

- **Source:** [07-04 v1 13:00–14:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** verbatim.
- **Notes:** ⚠ compliance: "save up to 57%" only if that discount exists on the landing page at launch. See [sell the click](../concepts/sell-the-click.md).

### V33. Five short VSLs from a brief plus chosen hooks
- **Use when:** you already picked hooks and want one short VSL per hook.
- **Inputs:** brief; count; length; CTA; awareness; hook list.

```text
here's the brief for an air bnb coaching program. Let's do 5 short VSLs that are 2 minutes each. The CTA in each will be to book a call. These 5 minute [sic] VSLs will be going mostly to problem aware people so let's focus most on them.

Here are the hooks I want to use:
Most people work 40 years to afford retirement - but this strategy works in 40 weeks.
Most people think real estate investing requires six figures - this couple started with $3,000.
I realized something was wrong when I asked permission to take my own birthday off.
Stop chasing shiny objects and start building real assets.
What if your rent payment could be generating income for YOU instead?
```

- **Source:** [07-04 v2 03:13–09:00](../lessons/07-04-short-vsl.md) (on screen).
- **Status:** verbatim ("5 minute [sic]" is in the source; he means five 2-minute VSLs).
- **Notes:** ⚠ compliance: hooks like "this strategy works in 40 weeks" and "this couple started with $3,000" are income claims. Use only with documented, typical results and the required earnings disclaimer, or rewrite them as questions without numbers.

### V34. Line-edit an outline, then write
- **Use when:** you want exact wording changes in an outline before the full draft.
- **Inputs:** section name with timing; old text; new text.

```text
Great job, here are the edits I want to make:

SOLUTION TEASE (55-75 seconds)
That's why I spent months researching an ancient Himalayan rice preparation ritual that actually repairs these cellular glucose doors in just 30 seconds a day.

Let's say:

SOLUTION TEASE (55-75 seconds) That's why I spent months researching an ancient Himalayan rice ritual that actually repairs these cellular glucose doors in just 30 seconds a day.

And instead of:
[old paragraph]

Let's say:
[new paragraph]
```

```text
Cool go ahead and write the ad please
```

- **Source:** [07-04](../lessons/07-04-short-vsl.md); doc "4. Claude Conversation History".
- **Status:** verbatim.
- **Notes:** the "instead of: … / Let's say: …" format is the cleanest way to give line edits. ⚠ compliance: "repairs these cellular glucose doors in just 30 seconds a day" is a disease-adjacent efficacy claim; structure only, claim not reusable.

### V35. Ten short concepts from an existing script
- **Use when:** you have a long VSL script and want short sell-the-click ads that drive to it.
- **Inputs:** the script; length; CTA.

```text
here's a script for a financial VSL. Right now I want to write a series of 2 minute long VSL ads that sell the click [so that someone watches, is hooked, and the call to action is to go watch the full presentation.] Please give me 10 short two-minute VSL concepts right now.
```

- **Source:** [07-04 v4 05:35–06:26](../lessons/07-04-short-vsl.md) (screen 06:00; bracketed words from audio).
- **Status:** verbatim with audio fill-ins.

### V36. Tease more, give away less; change the voice
- **Use when:** a short ad reveals too much of the story the full VSL should pay off, or you want a format variant (newscaster voiceover).
- **Inputs:** what to keep teasing; the new voice.

```text
Let's make it more teasing. [Tease] the opportunity, genetic royalties, the FDA decision, etc. Let's not [give away] so much. So just teasing what happened, the FDA and the opportunity, the consequences.
```

```text
Cool. Let's do one with a newscaster voice over
```

- **Source:** [07-04 v4 08:00–09:24](../lessons/07-04-short-vsl.md).
- **Status:** first verbatim with bracketed fill-ins (screen 13:00); second reconstructed from audio [v4 08:45–09:24].
- **Notes:** ⚠ compliance: "the FDA decision" and "genetic royalties" are the course's hypothetical financial offer; any regulatory event or market claim must be real and sourced. A newscaster voice must not imply real news coverage.

**Swipe-file prep**

### V37. Clean up a swiped transcript
- **Use when:** preparing a competitor or reference VSL/upsell transcript for project knowledge or analysis.
- **Inputs:** raw transcript.

```text
Here's a transcript of a video sales letter for a skincare brand. Can you take it and clean it up so it's more readable? [There are] a lot of timestamps and awkward line breaks. ... If you need more to do multiple outputs, just ask me to continue when you're out of space, and I'll keep doing it.
```

```text
Here's a video script, please format it with a break in between each line. You can do it over multiple outputs as needed:

[paste raw transcript]
```

- **Source:** [04-04](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) (spoken near-verbatim); [14-02 v4 15:51–16:53](../lessons/14-02-upsells-case-studies.md) (on screen, Poe).
- **Status:** 04-04 reconstructed (Whisper rendering; "..." marks a gap); 14-02 verbatim.
- **Notes:** in Poe the "continue" request lost context; start a new chat with the unprocessed remainder. [04-04 18:16–19:11](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) Swipes are for structure study only.

## Hooks
Hooks are generated as a **database** (deep research + seed examples), then used for VSL micro-leads and modular ads where the body is locked and only the hook changes. [framework](../frameworks/hook-generation-system.md) · [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md) · library: [hooks.md](hooks.md)

### H1. Deep research hook generation
- **Use when:** building a hook database for a niche from social signals, blogs and market beliefs, using annotated hook-heavy ads as the style reference.
- **Inputs:** your annotated ad transcripts (pasted in the middle); niche and audience; pain points.

```text
I'm going to share the transcripts for several direct response video ads that run on meta. They are annotated to share what's happening on screen during different segments of the ad. What I want you to really pay attention to however is how much curiosity there is. Specifically, there are a TON of "hooks" throughout the VSL. It's constantly keeping the viewer interested and intrigued. In fact, I refer to this style of ad as an ADHD Super-Hook Ad.

[PASTE YOUR ANNOTATED AD TRANSCRIPTS HERE: the lesson's doc has seven breakdowns (Vshred and Svelte), in the form "Ad Script Breakdown #1 - Vshred", "Part I. Opening Hooks and Attention Grabbers", speaker name, spoken line, (visual description)]

====

Now, let's get to your research assignment. What I want you to do is to leverage social media signals, beauty blogs, health and wellness blogs, and other websites to come up with as many different hook-driven statements and questions as you can for a skincare brand that targets women 35+. This can be based on trending skincare routines and rituals, beliefs the market has, etc.

The products the skincare brand sells doesn't matter, because you're only focus is on coming up with tons of different hooks that create curiosity and keep people glued to the video ad script.

That being said though, the general pain points of the market include: wrinkles, under eye bags, puffy bags around their eyes, dark circles around their eyes, etc. Additional pain points include saggy, crepe-like skin, turkey neck, forehead wrinkles, creases, and looking older than they feel.

Please help me come up with as many relevant hook-driven questions and statements that can be used in video ads as possible.

Note that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity.
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "2. Deep Research Hook Generation Prompt" (opening paragraph, ad breakdowns, research assignment).
- **Status:** verbatim (typos kept: "you're only focus"; Stefan: "I didn't even write this in coherent English" [30:57]).
- **Notes:** to change niche, edit "skincare brand that targets women 35+", the pain-point paragraph and "the products the skincare brand sells". [04-10 44:37–45:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### H2. Hook generation for tools that can't read long PDFs (Perplexity)
- **Use when:** the research tool can't take the long ad-breakdown PDF; seed hooks stand in for the transcripts.
- **Inputs:** niche, audience, pain points, 5 seed hooks from your niche.

```text
I want you to do is to leverage social media signals, beauty blogs, health and wellness blogs, and other websites to come up with as many different hook-driven statements and questions as you can for a skincare brand that targets women 35+. This can be based on trending skincare routines and rituals, beliefs the market has, etc.

The products the skincare brand doesn't matter, because you're only focus is on coming up with tons of different hooks that create curiosity and keep peopled glued to the video ad script.

That being said though, the general pain points of the market include: wrinkles, under eye bags, puffy bags around their eyes, dark circles around their eyes, etc. Additional pain points include saggy, crepe-like skin, turkey neck, forehead wrinkles, creases, and looking older than they feel.

Please help me come up with as many relevant hook-drive questions and statements that can be used in video ads as possible.

Note that that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity.

Here are a few examples to get you started:

"Did you know that sleeping on your stomach can cause wrinkles?

"The number one ingredient to look for in an anti-aging cream? It's not what you think."

"Are you using the wrong type of sunscreen? This type is best for your skin."

"What's the difference between anti-aging and moisturizing products anyways?"

"Hold on, using hot water to wash your face might be damaging your skin's barrier"
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "3. Perplexity version".
- **Status:** verbatim (typos kept).
- **Notes:** the call video says he fed the output back with "review these, can come up even more" [04-10 37:55]; the doc's feedback is [H3](#h3-snippets-not-bullets-feedback).

### H3. Snippets, not bullets (feedback)
- **Use when:** the model returns closed-loop fascination bullets instead of short, fragmentary hook lines for multi-speaker ads.
- **Inputs:** none (examples are skincare; swap for your niche).

```text
You know what I don't love about these? A lot of the hooks or curiosity statements are just like "snippets." You seem to be writing fascination/curiosity bullets almost. But in a video ad with a bunch of speakers, a lot of the hooks will be really fragmented. Speaker 1: might say "This is how often you should really be washing your face" and then a different speaker right after might say "What about sunscreen?" and a few lines later in the ad, another person might say "Is your pillowcase accelerating your wrinkles?"

So "imagine" that you're just writing phrases, hooks, and curiosity statements that can be injected throughout different ads. They don't need to be closed-loop Many can be more open-ended, like the first half of a puzzle but not the completed puzzle.
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "3. Perplexity version" (feedback message).
- **Status:** verbatim.

### H4. Generate still more hooks from a hook database
- **Use when:** you have a hook database and want more lines in the same "snippet" style.
- **Inputs:** your hook database, one hook per line.

```text
Below are several hooks and curiosity-driven statements that can be used in video ads for a skincare brand:

Hooks

[PASTE YOUR HOOK DATABASE HERE: one hook per line. The lesson's database has ~90 lines, e.g. "Did you know that sleeping on your stomach can cause wrinkles?", "Stop using hyaluronic acid until you watch this.", "Is that 'natural' face scrub creating micro-tears in your skin?"]

===

Please notice that a lot of the hooks or curiosity statements are just like "snippets." They are NOT fascination/curiosity bullets. This is what I'm looking for right now, because in a video ad with a bunch of speakers, a lot of the hooks will be really fragmented. Speaker 1: might say "This is how often you should really be washing your face" and then a different speaker right after might say "What about sunscreen?" and a few lines later in the ad, another person might say "Is your pillowcase accelerating your wrinkles?"

So "imagine" that you're just writing phrases, hooks, and curiosity statements that can be injected throughout different ads. They don't need to be closed-loop Many can be more open-ended, like the first half of a puzzle but not the completed puzzle.

Please generate as many new hooks and curiosity-driven statements as you can right now.
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "5. prompt for generating still MORE hooks".
- **Status:** verbatim.
- **Notes:** don't copy the lesson's ~90-line skincare database into production ads; it is structure reference only. [04-10 Prompts](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### H5. Start a hook-heavy ad session
- **Use when:** in the hook-ads project ([P7](#p7-hook-heavy-meta-ads-project-adhd-super-hook)), first message for a brand.
- **Inputs:** brand; first half of the VSL; ad length; concept count.

```text
We're going to write some new ads for our skincare brand Opal Beauty. I'm going to upload the fist half of the VSL so you get a little bit more context. Your goal is to write ads that are hook-heavy, have tons of curiosity, leverage the hook database, and ultimately "sell the click" to the VSL. We're also going to make all the ads between 1 and 3 minutes long for now.

To start, can you give me 10 ad concepts where you include the different hooks to be mentioned in the first 30 seconds? I'll then choose and have you write ads from there.
```

- **Source:** [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); doc "6. Claude Project Setup and Prompt Examples".
- **Status:** verbatim ("fist half" is in the source).
- **Notes:** follow-ups spoken on the call (reconstructed): "ad concept number one. Go ahead and write that now" [04:42]; "give me 10 more concepts" and "please do concept number 15 now" [51:21]; transitions fix: "Good job with loading up the opening with hooks. I do think we need some better transitions between some of the hooks. So let's focus on better transitions between hook two and three and between three and four in the opening." [55:12]

### H6. Hook generation for a new niche (problem aware)
- **Use when:** building a hook database for a non-skincare offer with the unified research brief attached.
- **Inputs:** offer; awareness; belief areas to mine; unified research brief; seed hooks (swap for your niche).

```text
I want you to leverage social media signals, blogs, and other websites to come up with as many different hook-driven statements and questions as you can for an Airbnb Arbitrage Coaching program. We are targeting people who are mostly problem aware, but who may not know a lot about Airbnb arbitrage or real estate. This can be based on sentiment, what people believe about side hustles, income, making money, etc, hacks/tricks/loopholes people share, etc. I've attached a Unified Research Brief for you that will share more about the market. Just keep in mind who we are going after, which is, again, mostly problem aware people.

The specifics of the coaching program don't really matter, because your only focus is on coming up with tons of different hooks that create curiosity and keep people glued to the video ad script.

Note that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity.

Here are examples of good hooks and curiosity statements from the skincare space for inspiration:
Stop using hyaluronic acid until you watch this.
The truth about collagen supplements is that they might help your body produce more collagen, but they can't fix THIS specific problem with your skin...
Do you know what happens when your skin loses its 'Velcro effect'...
Most women don't realize this separation is happening beneath their skin...
You need to see this microscopic view of what's happening to your skin cells right now.
I had no idea my skin layers were supposed to look like this...
```

- **Source:** [07-01 v5 00:00–01:06](../lessons/07-01-long-form-vsl.md) (Google Doc on screen 0:42).
- **Status:** partial (verbatim; the seed list continues beyond the frame).
- **Also appears:** blood-sugar version, spoken [07-03 v2 00:00–00:35](../lessons/07-03-3-7-minute-vsl.md) (reconstructed; "basically the same prompt I've used a bunch of times"; saved text not in the files): "For a blood sugar support supplement, we're targeting people who are mostly problem aware and solution aware."
- **Notes:** failure mode: the skincare seed hooks leaked into the Airbnb output. Replace the seed list with examples from the target niche. [07-01 v5 54:02–55:07](../lessons/07-01-long-form-vsl.md)

### H7. Hook generation from an existing script (financial)
- **Use when:** you have a long VSL script and want hooks for short sell-the-click ads, beyond what's in the script.
- **Inputs:** script uploaded; offer; awareness; belief areas; seed hooks (swap for your niche).

```text
I want you to leverage social media signals, blogs, and other websites to come up with as many different hook-driven statements and questions as you can for a financial newsletter promotion. We are targeting people who are mostly problem aware and solution aware. This can be based on sentiment, what people believe about the markets, investing, healthcare and big pharma, and so on.
I've uploaded a copy of the script but your job is NOT to only come up with hooks from the script, rather it is to find tons of different hooks that create curiosity and keep people glued to a shorter video ad that gets people to click a link and go watch the full presentation.
Note that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity
Here are examples of good hooks and curiosity statements from the skincare space for inspiration:
Stop using hyaluronic acid until you watch this.
The truth about collagen supplements is that they might help your body produce more collagen, but they can't fix THIS specific problem with your skin...
Do you know what happens when your skin loses its 'Velcro effect'...
Most women don't realize this separation is happening beneath their skin...
You need to see this microscopic view of what's happening to your skin cells right now.
[the list may continue off-screen]
```

Refocus message after the first output:

```text
Thanks, these are okay. The one thing is: they really are focused on the FDA and like diseases and things like that. I think we want them to be more focused on the investment opportunity as well. So it's not about some new cure. It's about how new technologies or changes in healthcare or this FDA decision [or whatever else] are creating a once-in-a-generation opportunity.
```

- **Source:** [07-04 v4 01:00–04:00](../lessons/07-04-short-vsl.md) (screen; refocus ending from audio [v4 03:39]).
- **Status:** partial (visible text ends where the screen cuts off).
- **Notes:** failure mode: hooks drifted to FDA and disease topics instead of the investment opportunity; the refocus fixed it. ⚠ compliance: same skincare-seed leak risk as H6; "once-in-a-generation opportunity" framing is a financial promise that needs substantiation and disclosures.

### H8. Hook-heavy micro-lead concepts from a finished VSL
- **Use when:** in the hook project, to write new pre-leads or micro-leads for a VSL you already have.
- **Inputs:** the VSL script (PDF); hook database in project knowledge; chosen concept.

```text
Here's a new VSL script I wrote for a skincare serum. Please give me 10 hook-heavy lead concepts I could use for the micro lead. You can pull from the database plus ideas from the VSL. I'll then select the ones I want to turn into new pre-leads or leads.

[follow-up] Can you now do these where they're not all focused on the UMP so much? More for the curiosity. We talk about collagen breaking down. We don't need to talk about collagen architecture.

[follow-up, screen 8:53] ...using eye creams with collagen is a mistake" and some other "mistake" type hooks?

[select] Great job, let's go ahead and do a new micro lead with [concept]. Let's keep it to about the same length as the current pre-lead/micro lead in the VSL I uploaded [as a PDF].
```

- **Source:** [07-01 v4 00:00–08:54](../lessons/07-01-long-form-vsl.md).
- **Status:** reconstructed (brackets from audio; the screenshot shows only the tail of the second follow-up).
- **Notes:** failure mode: concepts leaned on the mechanism jargon ("collagen architecture") instead of curiosity; the second follow-up fixed it.

### H9. ADHD hook ad concepts from a brief
- **Use when:** in a VSL project with a brief, to get hook-dense video-ad concepts.
- **Inputs:** brief; concept count; the chosen concept's lead line; CTA.

```text
Here's the brief for a VSL. I need five ADHD hook ad concepts to choose from.

I like concept number three the most. Let's lead with [that line]. Let's have the CTA be to save 57% off their order when they visit the website. Write the script.
```

- **Source:** [05-02 39:21–41:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md).
- **Status:** reconstructed (spoken, approximate).
- **Notes:** his critique of the result: "this has really run more to sell the solution than to sell the VSL… I probably could have done 'save 57% off to get more information'". [05-02 42:17–43:17] State the CTA type (sell the click vs sell the solution) explicitly.

### H10. Edit a hook (and test a new mechanism on the same ad)
- **Use when:** a hook assumes something untrue for most viewers, or you want the same ad rewritten around a new UMP/UMS.
- **Inputs:** the hook change; the brief with the new mechanism.

```text
Thanks, let's change the hook to be "here's why makeup artists can" vs "your makeup artist" since it's not like everyone has a makeup artist.

Also, I'm playing around with a new mechanism which is included in this brief I'm attaching. I'd like to see another version of this ad that keeps everything else the same but the change mentioned above, and it also modified for the UMP/UMS in the brief.
```

```text
I like this hook but let's do it like this:
What if your rent payment could be generating income for you instead of lining someone else's pocket.
```

- **Source:** [07-04 v1 06:00](../lessons/07-04-short-vsl.md) (first paragraph on screen; second cut off after "I'm playing around with a", rest from audio [v1 06:46–07:21]); [07-04 v2 09:47–10:17](../lessons/07-04-short-vsl.md) (screen 10:00).
- **Status:** first partial (screen + audio); second verbatim.
- **Notes:** "since it's not like everyone has a makeup artist": test every hook's premise against the whole audience.

### H11. Swap the hook, keep the body
- **Use when:** making hook variants of a winning ad: same body from a fixed section onward, new opening hook.
- **Inputs:** the new hook; where the locked body starts (or paste the rest of the outline).

```text
Okay great. Now I want to do another ad where everything after the Revelation/Education section is pretty much the same. But we do a different hook. In this case let's do this hook: Here's what happens to your blood sugar when you skip breakfast...
```

```text
Thanks, and let's do one more version, same instructions as before but let's use this hook:

The shocking connection between your laundry detergent and insulin resistance.
```

```text
Okay great, let's do another version of this ad with a new hook. The hook will be: Why your sleep apnea is making diabetes impossible to control. The rest of the ad from this point on can basically stay the same:
[paste of the rest of the outline]
```

```text
Now let's write another one with a hook about: Don't buy any Big Pharma stocks until you see this.
```

- **Source:** [07-03](../lessons/07-03-3-7-minute-vsl.md) doc `4. Claude Conversation_.docx` (first two); [07-04](../lessons/07-04-short-vsl.md) doc "4. Claude Conversation History" (third); [07-04 v4 11:01–11:16](../lessons/07-04-short-vsl.md) (fourth, audio).
- **Status:** first three verbatim; fourth reconstructed (exact wording uncertain).
- **Notes:** this is the one-variable test from [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md). ⚠ compliance: "sleep apnea is making diabetes impossible to control" and "laundry detergent and insulin resistance" are disease claims; "Don't buy any Big Pharma stocks" is investment advice. Structure only; claims not reusable.

## Advertorials
Workflow: outline a proven advertorial's structure → swipe it for our product, or run the project's three-prompt sequence (hooks → outline → draft) → review → shorter variants → build the page. [framework](../frameworks/advertorial-build.md) · [ad-to-page journey](../concepts/ad-to-page-journey.md)

⚠ compliance (whole section): Stefan on the invented doctor story: "it's an editorial, so you can kind of not, but you'd have to say, hey, this is like a sort of made-up story or composite story" [09-02 53:09](../lessons/09-02-claude-project-for-advertorials.md). Repo rule: **hard stop**. No invented doctors, quotes, studies, statistics or testimonials presented as fact in an advertorial, labelled or not.

### A1. Outline the structure of an advertorial
- **Use when:** you found an advertorial that works and want its structure.
- **Inputs:** the full advertorial text.

```text
Here's an advertorial I just read. Can you please go through it and then create a detailed outline of the structure:

[paste full advertorial text]
```

- **Source:** [09-01 27:50–30:35](../lessons/09-01-advertorials-overview-and-examples.md); doc `3. Claude Process Example_Quick Advertorial Swipe.docx`. Run in the advertorial project or a plain chat.
- **Status:** verbatim.

### A2. Swipe the structure for our product
- **Use when:** straight after A1, in the same chat.
- **Inputs:** brand, product, product page URL (add the brief, research and real proof).

```text
Perfect, thanks this was great. Let's write an advertorial for opal beauty that follows the same structure. Specifically for our Unity Eye Serum:

[product page URL]
```

- **Source:** [09-01 27:50–30:35](../lessons/09-01-advertorials-overview-and-examples.md); same doc.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: Claude's reply listed its "Structure Maintained", including "Personal story (Sarah, 52, marketing executive)", "Expert validation (dermatologist explaining DEJ science)", "Social proof and testimonials", "Personal testing account (week-by-week results)" and "Urgency and scarcity elements". All of these were invented. Compliant edit: append "Use only the facts, testimonials and expert statements in the attached brief; for any structural slot without real proof, write [VERIFY: …] instead of inventing a person, number or quote."

### A3. Ten advertorial hooks from a source document
- **Use when:** in the advertorial project; prompt 1 of 3.
- **Inputs:** `__Document Type____` (landing page copy, a PDF with details, a VSL script); `___Product Type____`; the document attached.

```text
Here is a __Document Type____ for a ___Product Type____. Please analyze it, and then I want you to give me 10 potential hooks for advertorials we could write.
```

As typed in the demo (Norse landing-page PDF attached):

```text
Here is landing page copy for a acne removing product. Please analyze it, and then I want you to give me 10 potential hooks for advertorials we could write.
```

- **Source:** [09-02 16:23–17:28, 23:18](../lessons/09-02-claude-project-for-advertorials.md); process doc 1.
- **Status:** verbatim.

### A4. Outline one advertorial angle
- **Use when:** prompt 2 of 3; pick a hook and ask for an outline at a length, optionally hiding the price.
- **Inputs:** hook number; length (short / medium / long); price note; optional winning ad caption for congruence.

```text
Okay nice, let's go ahead and do #___ first. Can you write out an outline for a ____ length advertorial with that angle? One note is that I don't want to reveal the price, but rather say that readers can save XX%.
```

As typed in the demo, with the congruence paragraph added:

```text
Okay nice, let's go ahead and do #5 first. Can you write out an outline for a medium length advertorial with that angle? One note is that I don't want to reveal the price, but rather say that readers can save XX%.

One thing to bring up is that this type of story has worked really well in the brand's ads. I will copy and paste the ad caption here, so you can make the advertorial congruent with this story.

[PASTE THE BRAND'S WINNING AD CAPTION / STORY HERE]
```

- **Source:** [09-02 26:36, 28:06](../lessons/09-02-claude-project-for-advertorials.md); process doc 1 (the price sentence is highlighted as optional).
- **Status:** verbatim.
- **Notes:** pasting the brand's winning ad story keeps ad and advertorial congruent ([congruence](../concepts/congruence.md)). Record the pasted caption only as beats; don't reuse its lines.

### A5. Write the advertorial
- **Use when:** prompt 3 of 3, after approving the outline.
- **Inputs:** none.

```text
perfect, let's go ahead and write this advertorial now. If you run out of space in a single output and need to do it over multiple outputs that's fine, just let me know and I'll prompt you to continue.
```

- **Source:** [09-02 30:55](../lessons/09-02-claude-project-for-advertorials.md); process doc 1 (template). As typed in the demo: "perfect, let's go ahead and write this advertorial now".
- **Status:** verbatim.

### A6. Shorter version for testing
- **Use when:** you have a long advertorial and want a shorter test variant with the same structure.
- **Inputs:** target reduction.

```text
this is great, really nice job. Can you now do another version of this advertorial that retains the main structure and elements, but that's about 50% shorter so I can have a less lengthy version to also test.
```

- **Source:** [09-02 40:48–41:19](../lessons/09-02-claude-project-for-advertorials.md) (spoken; confirmed on screen in video 2 at 03:48).
- **Status:** verbatim.
- **Notes:** ask for "about N% shorter" rather than editing by hand. [09-02 review checklist](../lessons/09-02-claude-project-for-advertorials.md)

### A7. Second angle in the short format
- **Use when:** writing the next hook from A3's list using the shorter version as the model.
- **Inputs:** hook number and name; audience; the discovery to incorporate.

```text
Great job. Now let's do hook number six, the arctic discovery. For this let's keep it shorter, the short version of the advertorial you just did. Still have the target audience be parents of kids. Frustrated parents of kids with acne, but incorporate this discovery.
```

- **Source:** [09-02 44:37–45:53](../lessons/09-02-claude-project-for-advertorials.md).
- **Status:** reconstructed (Whisper text, cleaned for punctuation). He then simplified the audience to "kids with acne".

### A8. Multi-point review feedback
- **Use when:** the draft has an off-category villain, wrong offer facts, excess length and a logic gap.
- **Inputs:** numbered corrections.

```text
Great job. A few things.
1. Instead of speaking specifically about Big Pharma, let's talk about big skin care companies instead. We can still also reference prescriptions, but I don't want the whole [piece] focused on anti Big Pharma.
2. Next, let's make this about 20% shorter.
3. Third, it's a 60 day guarantee. [fix the guarantee length]
4. Fourth, I want a little more congruency between discovering these plants and the decision to test them against acne bacteria.
```

- **Source:** [09-02 49:51–52:41](../lessons/09-02-claude-project-for-advertorials.md).
- **Status:** reconstructed (from audio; the typed text may differ).
- **Notes:** the numbered-list format is the pattern: villain fit, length, offer facts (guarantee), story logic. The full review checklist is [X4](#x4-advertorial-review-checklist-derived).

### A9. Add a missing motive to the story
- **Use when:** a story step has no reason ("why would he do that?").
- **Inputs:** the motive.

```text
I think what's missing is something like, when Dr. Johansson saw the incredible antimicrobial power of these plants, he immediately thought about acne. Perhaps even say that's because his own teenage sons both suffered from severe acne and nothing they'd tried worked.
```

- **Source:** [09-02 52:10](../lessons/09-02-claude-project-for-advertorials.md) (typed; screen 54:52).
- **Status:** verbatim.
- **Notes:** ⚠ compliance: Dr. Johansson, his sons and the quote that followed were invented by the model; Stefan's own caveat is at [53:09]. Hard stop for our brands. Compliant edit: "Add the motive using only the founder/expert story in the brief; if the brief has none, write [VERIFY: real origin story] and keep the step generic."

### A10. Build the advertorial page in Magic Patterns
- **Use when:** turning approved advertorial copy into a page, modeled on a design screenshot.
- **Inputs:** a full-page screenshot of the design to imitate; the copy; image assets; URLs.

```text
We're going to create a new advertorial. You can model off the design and the screenshot attached. Please do not include the screenshot image in the new advertorial. It's being provided as a design reference only. Here's the copy.

[PASTE ADVERTORIAL COPY HERE]
```

Follow-up edits, in order:

```text
Great job. Let's add an urgency box to the top similar to what's in the screenshot, with copy relevant to the offer and copy on this landing page. Instead of "Beauty News" let's have it say: "Beauty Report". And for the part after the highlighted box that says: Home/Beauty/Luxe Eyelash Growth Serum, let's have it say: "Home/Skincare/Acne Removal"
```

```text
Great job. Let's add the hero image under the headline and sub header. Add the product image where those placeholders are.
```

```text
Great job. The only thing is that the hero image is too big. Let's scale that down so it's about half the current size please.
```

```text
Have the green CTA button link to [BRAND URL]. Where those circles are, [add the images]. Third, at the bottom, add a footer with a privacy policy, contact us and terms of service.
```

```text
For privacy policy, let's have it linked to [URL]. For terms of service, let's have it linked to [URL]. And for contact us, let's change that to say guarantee instead, have that linked to [URL].
```

- **Source:** [09-02 v2 03:21–04:40](../lessons/09-02-claude-project-for-advertorials.md) (initial, spoken near-verbatim); follow-ups [v2 07:02–09:33; screen 09:24], [v2 13:07–14:47], [v2 15:46; screen 16:24], [v2 18:37–19:23], [v2 31:20–32:03].
- **Status:** initial reconstructed (near-verbatim); follow-ups: 1st verbatim (screen, light cleanup), 2nd reconstructed (partly garbled), 3rd verbatim (screen), 4th reconstructed (heavily garbled; paraphrase), 5th reconstructed.
- **Notes:** his tip: "sometimes it gets weird, so you might have to say it again". ⚠ compliance: an "urgency box" needs a real deadline or stock limit; "Beauty Report" styling must not pose as independent news (native-ad disclosure, see [12-02](../lessons/12-02-native-ads.md)).

## PDPs
No project: one chat per page. Extract a templatized outline from a PDP you like → swipe it with our live page or brief → edit. [framework](../frameworks/pdp-build.md) · [10-01](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)

### D1. Extract a PDP outline from two product pages
- **Use when:** one brand has two similar PDPs; you want a reusable section template that captures both.
- **Inputs:** two URLs (web search enabled).

```text
I'm going to share two product page links from a brand with you. They are for two different products, but similar. Please review them, and then I would like for you to create a templatized outline that captures both the structure, and all of the common elements. This should be something someone could use for other products and brands to produce similar Product Pages.

[link 1]
[link 2]
```

- **Source:** [10-01 20:56–22:24](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); doc "2. PDP Outline Creation and Swiping Prompts".
- **Status:** verbatim.
- **Notes:** the output merged the two pages ("it did for one about the other") [24:29]. Save it as a named doc. The extracted Happy Mammoth and Dr. Clean templates are in [templates.md](templates.md).

### D2. Extract a PDP outline from one product page
- **Use when:** you have one PDP to model.
- **Inputs:** one URL.

```text
I'm going to share a product page link from a brand with you. Please review it, and then I would like for you to create a templatized outline that captures both the structure, and all of the common elements. This should be something someone could use for other products and brands to produce similar Product Pages.

[link]
```

- **Source:** [10-01 31:19–33:49](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); same doc (typo "I'm going to a product page link" fixed by the lesson page).
- **Status:** verbatim (typo fixed).
- **Also appears:** [10-02](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md) doc "3. Claude Convo History" (Dr. Clean; identical).

### D3. Swipe the structure for a product with a live page
- **Use when:** after D1/D2, same or new chat; our product already has a PDP.
- **Inputs:** product name; our current PDP URL.

```text
Awesome, so now if we were going to test a new PDP for [product], following this structure, what would it look like? Can you go ahead and write the copy for it and indicate all the other design and structural elements? Here's the current PDP:

[product URL]
```

- **Source:** [10-01 25:45](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); same doc.
- **Status:** verbatim.
- **Also appears:** [10-01 45:06–48:55](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) (sauna structure into Clarifion; "this different product" replaces "[product]").
- **Notes:** ⚠ compliance: the course output invented "I threw away $2,000 worth of eye creams… 25-year-old eyes back at 52", "87% of eye aging" and "eyes age 3x faster" [10-01 26:20–28:31]. Append: "Use only claims, numbers, reviews and ratings that appear on our current page or in the brief; otherwise insert [VERIFY: …]."

### D4. Swipe the structure from a brief
- **Use when:** you want the page built from the brief rather than a live URL.
- **Inputs:** product name; brief attached.

```text
Now, if we were going to test a new PDP for [product], following this structure, what would it look like? Can you go ahead and write the copy for it and indicate all the other design and structural elements? I've attached a brief that should give you all of the information on the [product] you need.
```

- **Source:** [10-01 33:49](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); same doc.
- **Status:** verbatim.
- **Notes:**
  - Failure mode: Claude started coding an HTML artifact; fix with [D5](#d5-stop-claude-from-coding-the-page). [34:37–39:23]
  - He later thought telling it to also visit the live site "probably would have been better". [41:18]
  - ⚠ compliance: the output generated "Elizabeth K., Age 62" and "4.8/5 stars, 3,425+ verified reviews, 5,832+ happy customers, 94% would recommend", none sourced. Layout placeholders only; replace with real review data or `[VERIFY: rating, count]`. [10-01 41:18](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)

### D5. Stop Claude from coding the page
- **Use when:** Claude builds an artifact or HTML instead of writing formatted copy.
- **Inputs:** none.

```text
I don't need you to code or do HTML. I also don't want it in plain text. Instead, can you please just write the copy with formatting. Maybe it's best if you don't do it as an artifact?
```

- **Source:** [10-01 38:37](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); doc label "Prompt for Claude When it Starts Randomly Coding Shit".
- **Status:** verbatim.
- **Notes:** it did not fully stop the artifact in the video [39:23]; he used the copy anyway. Live variant: "Let's have you write the copy and mention, okay, where various go." [34:37] Put the no-code line in the first prompt to prevent it.

### D6. PDP for an offer with no website yet
- **Use when:** same chat as D3, a different offer with only a brief.
- **Inputs:** brief attached.

```text
Nice! Now let's do a PDP for this blood sugar offer. It doesn't have a website yet. Do the exact same thing you did before please!
```

- **Source:** [10-01 42:42](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); same doc.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: blood-sugar PDP copy must stay structure/function; no diabetes or medication claims.

### D7. Fallback when Claude cannot fetch the page
- **Use when:** the fetch fails (robots.txt); you paste the page copy and attach an above-the-fold screenshot.
- **Inputs:** pasted copy; one or more screenshots.

```text
okay here's the copy attached. And here's a screenshot of the above the fold.
```

- **Source:** [10-02 15:35–16:35](../lessons/10-02-in-depth-case-studies-dr-clean-and-calvin-tran.md); doc "3. Claude Convo History".
- **Status:** verbatim.

## Ads
Ad copy in RMBC comes mostly from the VSL and hook prompts above (short VSLs = video ads; [H5](#h5-start-a-hook-heavy-ad-session)–[H11](#h11-swap-the-hook-keep-the-body)). This section holds the captions project, ad analysis and AI-video prompts. [framework](../frameworks/paid-traffic-by-platform.md)

### AD1. Meta ad captions
- **Use when:** in the captions project ([P10](#p10-meta-captions-generator-project)); captions for a product or sell-the-click ad.
- **Inputs:** product; benefits; CTA and offer.

```text
Can you do some ad captions for [eye serum product]? Benefits plus a CTA to save 57% off. And then I can run my link.

Great, thank you. Now can you do some really short ones that are just a few lines and sell the click.
```

- **Source:** [12-01 v2](../lessons/12-01-meta-ads.md).
- **Status:** reconstructed (from speech; "[eye serum product]" is the lesson's reading of a likely mishearing).
- **Notes:** two runs: benefit-led with a discount CTA, then "really short ones" that sell the click. ⚠ compliance: "save 57%" only if the discount is live.

### AD2. Five-question ad analysis
- **Use when:** analysing any ad (ours or a competitor's) before planning variants or hook tests.
- **Inputs:** the ad (script or screenshot); the checklist below.

Checklist (course doc, condensed by the lesson page):

```text
Meta ad analysis
Overarching: You can't talk about ads without assets. You can't get around testing.
1. What is the Objective? Acquire new customers / Generate new leads / Sell the solution / Sell the click / Increase brand and product awareness
2. What is the Product/Market Awareness Level? Unaware / Problem aware / Solution aware / Product aware / Most aware
3. Where do we send people? Advertorial / VSL / long PDP / short PDP / Brand building and awareness / Registration-signup page
4. What is the Format? Ultra short video / Short video / Medium video / Long video / Static
5. Commonalities? Curiosity / Visuals / Education / Emotional / Social proof (UGC, testimonials, etc.) / ???
```

Agent prompt (derived):

```text
For the ad below, fill the five questions, name what is held constant across its variants and what varies, and propose 3 hook tests for the first 3-10 seconds with the rest unchanged.
```

- **Source:** [12-01](../lessons/12-01-meta-ads.md); doc "01-1 Meta Ads Overview and Core Training".
- **Status:** checklist verbatim (condensed); prompt derived (not a course asset).

### AD3. Outline a short ad against a structure doc
- **Use when:** you have a winning short ad transcript and a structure document (e.g. the short-VSL structures in [templates.md](templates.md)) and want its beat outline and a reusable template.
- **Inputs:** the ad transcript; the structure doc in context.

Course lines (on screen and spoken):

```text
Given that structure I just shared, how would you outline this ad?
```

```text
okay great and if we were going to take this outline, and make it broader so it would apply to many [other business opportunities]
```

Agent version (derived):

```text
Here is a short video ad transcript (from Meta). Using the structures in the project knowledge as a reference:
1. Name the structure it matches most closely, and say where it deviates.
2. Outline this specific ad beat by beat (hook, story, mechanism, solution, proof, CTA), with approximate seconds per beat.
3. List any beat the closest existing structure is missing (for example, "how it works" explanation, objection handling, qualifier, risk reversal).
4. Rewrite the outline as a universal template: replace niche nouns, names, numbers and credentials with [slots], and mark which beats are optional.
5. Flag every claim, credential, statistic, testimonial and scarcity line in the ad that would need substantiation if we copied the structure for our own product.
```

- **Source:** [04-09 v2 33:58; 35:46](../lessons/04-09-short-vsls-structures-and-examples.md).
- **Status:** first line verbatim; second partial (typed on screen, bracketed end from audio); agent version derived.

### AD4. Veo 3 vlog prompt generator (guest, fragments)
- **Use when:** generating 8-second AI "vlog" clips to test a hook or angle before paying a creator. Guest material: Max Finn, 12-04.
- **Inputs:** business information or website URL (pasted into the generator in any LLM); output scene goes to Veo 3 (Flow or Gemini).

Fragment 1 (≈07:33):

```text
Choose the most believable vlog moment using this priority order:

TIER 1 - Daily Routine Integration:
- Morning routines, getting ready, meal prep, work setup
- Only use if product naturally fits into these moments
- Focus on authentic daily activities

TIER 2 - Activity/Experience Vlogs:
- Shopping hauls, trying new things, challenges, transformations
- Moments where discovering or using products feels natural
- Focus on genuine reactions and experiences

TIER 3 - Lifestyle Moments:
- Car vlogs, room tours, day-in-the-life, organizing
- Use when specific activities would feel forced
- Focus on casual, conversational moments

INFLUENCER PERSONA MATCHING
Vlogger Selection Criteria:
- MUST authentically represent or appeal to target demographic
- Natural authority/credibility in relevant lifestyle area
- Appearance, age, style must align with product category
- Consider: beauty guru (cosmetics), fitness influencer (health products), tech reviewer (gadgets), lifestyle vlogger (home goods), parent vlogger (family products)

Vlog Style Categories:
- Energetic Creator (Gen Z products): Fast-paced, trendy, excited delivery
- Relatable Sharer (millennial products): Conversational, authentic, friendly
- Aspirational Influencer (luxury items): Polished, confident, sophisticated
- Down-to-Earth Reviewer (practical products): Honest, helpful, genuine

VLOG MOMENT STRATEGY
```

Fragment 2 (≈08:12):

```text
Allow for natural "ums" or pauses if it adds authenticity
Background can show normal room elements but no readable text
CRITICAL REMINDERS
8-SECOND ABSOLUTE LIMIT: Entire vlog moment must complete in 8 seconds. Keep monologue concise - aim for 5-7 seconds.
MID-MOMENT START: Video begins with vlogger already talking - no "hey guys" intro unless it's part of the key message
AUTHENTIC VLOG FEEL: Must feel like a genuine snippet from a longer vlog, not a planned advertisement
NO VISUAL TEXT: Absolutely no captions, overlays, graphics, or written words visible. MUST include explicit VEO 3 instructions against captions in final prompt
NO PRODUCT PROPS: Vlogger should not hold, show, or display physical products. Verbal mention only.
NATURAL SETTINGS: Use realistic, lived-in spaces. Avoid overly perfect or staged environments.
PRONUNCIATION GUIDES: Include phonetic spelling for any brand names that could be mispronounced
PLATFORM AUTHENTICITY: Language and energy should match typical vlog content for that demographic
The goal is creating SAMPLES that feel like authentic vlog moments
Everything must feel spontaneous and genuine - avoid scripted or promotional language The vlogger should naturally represent the target market The moment should feel like it could go viral organically Product mentions should feel like genuine discoveries or recommendations
Now, analyze the business information provided and generate one compelling, authentic vlog video scenario following this framework.
```

- **Source:** [12-04 v4 07:10–09:34](../lessons/12-04-tiktok-ads.md) (on-screen Google Doc, "Veo 3 Vlog Prompt" tab).
- **Status:** partial. Only these two fragments are readable; the rest of this prompt and the Copywriter, Data Analysis, Veo 3 Interview and Multi-Scene prompts are **not in the course files**.
- **Notes:** ⚠ compliance: AI-generated people must never be presented as real customers or testimonials (derived; [12-04](../lessons/12-04-tiktok-ads.md) step 5). "Authentic vlog feel… not a planned advertisement" still needs the platform's paid-partnership / AI-content disclosure.

### AD5. Build a prompt generator for a new video format
- **Use when:** a new ad format goes viral (e.g. day-in-the-life) and you want a generator for it modeled on an existing one.
- **Inputs:** the whole existing generator document; a viral example of the new format.

```text
study this prompt generator and make me a version of this for creating this type of video
```

- **Source:** [12-04 v4 09:06–09:34](../lessons/12-04-tiktok-ads.md) (Max Finn, guest).
- **Status:** reconstructed (his described workflow, not a verbatim prompt).

## Upsells
Formula: reaffirm the purchase → new or expanded problem → irresistible offer ([upsell formula](../concepts/upsell-formula.md)). Two routes: a one-off chat that outlines a swipe and models it (U1–U4), or the Upsell Generator project ([P11](#p11-upsell-generator-project-longer-scripts), U5–U7). [framework](../frameworks/upsell-flow-build.md) · structures: [templates.md](templates.md)

### U1. Outline an upsell swipe's structure
- **Use when:** you have a proven upsell video script and want its structure as a model.
- **Inputs:** the swipe script attached; niche.

```text
Here is a video script for an upsell in the health space.I want you to analyze it and then create an outline for the structure of the script.
```

- **Source:** [14-02](../lessons/14-02-upsells-case-studies.md); doc `Claude Upsell Process_9-10-24.docx` (the RejuvaKnee swipe itself is not in the course files).
- **Status:** verbatim (missing space after "space." is in the source).
- **Notes:** Claude's 12-step outline of the swipe is in [templates.md](templates.md).

### U2. Write a new upsell section by section from the swipe
- **Use when:** after U1; you want a new script modeled on the swipe's structure, length, style and tone.
- **Inputs:** swipe name; product inputs PDF.

```text
Perfect thank you. Now we're going to be writing a new upsell script a different product. I want you to closely model off the Rejuvaknee Upsell as far as structure and length. Also in style and tone. We're going to do this through multiple outputs which means you can go section-by-section and when you write each section, just ask me to tell you to continue. Do not try to condense things, good video scripts are often quite long. Here's the information you should need to do this:

[attach: Fitspresso Inputs for Upsell (pdf)]

Please get started with the very first section. Whenever you run out of space just ask me to continue and I'll tell you to keep going.
```

- **Source:** [14-02](../lessons/14-02-upsells-case-studies.md); same doc.
- **Status:** verbatim ("a different product" missing "for" is in the source).
- **Notes:** between sections the whole continuation prompt is `yes please continue` (Claude ends each section with "Shall I continue with the next section?"). [14-02](../lessons/14-02-upsells-case-studies.md)

### U3. Redirect when the upsell is "more of the same"
- **Use when:** the model invents a new discovery story or a new product when you are selling more units of the product just bought.
- **Inputs:** product name.

```text
So here's where you need to be a little bit more creative, since in this case we're selling more Fitspresso. So we don't need to position and then intro a new product, since what we're doing here is selling them "more of the same."
```

- **Source:** [14-02](../lessons/14-02-upsells-case-studies.md); same doc.
- **Status:** verbatim.
- **Notes:** failure mode: Claude defaults to the swipe's "secret discovery" pattern. Name the upsell type ([upsell formula](../concepts/upsell-formula.md)) in the first prompt.

### U4. Add an expectations timeline
- **Use when:** a stock-up upsell needs a reason to keep using the product over months.
- **Inputs:** product; the periods.

```text
This is great. One thing I'd like to add is maybe a section where it's like "here's what you can expect during your journey with Fitspresso: Your First Week, Your First Month, Your Second Month, Your Third Month, Your Fourth Month, Your Fifth Month, and then Your Sixth Month. - and for each of those we paint a picture of their transformation improving and life getting better and better.
```

- **Source:** [14-02](../lessons/14-02-upsells-case-studies.md); same doc.
- **Status:** verbatim.
- **Notes:** ⚠ compliance: Claude's resulting month-by-month weight-loss numbers had no evidence behind them. Compliant edit: "…for each period describe only what users can expect based on [attached study / label directions]; no numbers unless they come from the attachment; otherwise [VERIFY]."

### U5. More-of-the-same upsell from a product URL
- **Use when:** in the Upsell Generator project; upsell #1 selling more of what was just bought.
- **Inputs:** length; product; product URL.

```text
Please do a 10 minute upsell script for someone who just bought unity eye serum, selling them more of the same.
https://tryopal.com/products/unity-eye-serum
```

Feedback after the first draft:

```text
Thanks. And going back to the Unity Eye Serum - 10 Minute Upsell Script. I liked it, but let's model more heavily off of the Emma and Synocell structure.
```

- **Source:** [14-03 00:59–01:31](../lessons/14-03-claude-projects-for-upsells.md); doc `2. Unity Eye Serum More of the Same.docx`.
- **Status:** verbatim.
- **Notes:** naming the knowledge-base swipes to model ("Emma and Synocell") is the steering move when the first draft drifts.

### U6. Cross-sell script and its three feedback rounds
- **Use when:** upsell #2 cross-selling a different product to the same buyer.
- **Inputs:** length; position in the flow; product URL.

```text
Awesome, good job! Now let's do an 8 minute cross-sell (it will be upsell #2) selling this product:
https://tryopal.com/products/lumessa
```

Feedback 1 (quote the line, state the flaw):

```text
"And I'm absolutely thrilled that you just secured your Unity Eye Serum 6-Month Age-Reversal System...
You've made two incredibly smart decisions today that are going to transform how you look and feel…"

We shouldn't assume they bought the first upsell. People will see this second upsell regardless of if they took #1 or not.
```

Feedback 2:

```text
"What most people don't realize is that your eyes are just one part of your face...
And if you want to look truly youthful and radiant...
You need to address aging on your ENTIRE face with the same level of precision and power."

This doesn't make sense. I'm pretty sure most people do realize that their eyes are just one part of their face.
```

Feedback 3 (tone):

```text
Thanks. Now one more thing, I'd like to see a version of this where the tone is a little more empathetic. Instead of making them feel like shit "your eyes will look good but the rest of you will look old!" let's show more empathy. "A lot of women end up realizing that the one downside is that it highlights other areas of their face that don't look so young. For some of them it might be fine lines around their mouth, or rough uneven texture on their cheeks." Things like that so we're still being persuasive but not calling out any specific woman who watches and assuming things about her.
```

- **Source:** [14-03 02:38; 04:24](../lessons/14-03-claude-projects-for-upsells.md); doc `3.1. Claude Conversation History for Lumessa Cross Sell.docx`.
- **Status:** verbatim.
- **Notes:**
  - Failure modes: assumes the buyer took upsell #1; claims a false "most people don't realize"; shames the viewer. All three recur in LLM drafts: check every upsell for them.
  - ⚠ compliance: "6-Month Age-Reversal System" in the quoted draft is an unsubstantiated claim; strip it.

### U7. Book-a-call upsell for info-product buyers
- **Use when:** the front-end product becomes upsell #1 after a low-ticket info product, with a book-a-call CTA.
- **Inputs:** brief attached; the front-end product just bought (name, price, what it teaches); target length.

```text
Here's information for a product we sell as a front end. Right now we're going to sell it as the first upsell, to people who just took a $27 info product called: "Permissionless Income" that teaches people 27 ways to generate extra income. It was from Mack as well. Now we're going to sell them on this concept and to book a call. Let's make the VSL Script 10-15 minutes long.
```

- **Source:** [14-03 5:12–8:36](../lessons/14-03-claude-projects-for-upsells.md) (read from screen at 8:36). Attachment: the Airbnb VSL brief from [05-03](../lessons/05-03-airbnb-arbitrage-example.md).
- **Status:** verbatim (stray markdown asterisks on screen removed by the lesson page).
- **Notes:** failure mode: the first draft still had a "Here's What This Would Normally Cost" price section; a call-booking upsell should not discuss price. [14-03 08:36](../lessons/14-03-claude-projects-for-upsells.md) ⚠ compliance: income outcomes need typical-results disclosures.

## Email
All prompts run in the Email Sequence Generator project ([P12](#p12-email-sequence-generator-project)): state type, length, discount schedule and product URL; ask for an outline; approve; "write it". [framework](../frameworks/email-sequences.md) · sequence structures: [templates.md](templates.md)

### E1. Abandon cart sequence with a discount ladder
- **Use when:** a 7-day abandon cart sequence for a product with a rising discount.
- **Inputs:** length; discount days and amounts; product URL.

```text
To start, let's do a 7 day abandon cart sequence for Unity Eye Serum. Let's introduce a 20% off discount on Day 3, and increase it to a 40% off Discount on Days 5-7. Can you please outline this sequence for me and then after I approve I'll have you write it.

https://tryopal.com/products/unity-eye-serum
```

Outline feedback (tone):

```text
Okay great, let's go ahead and write it. One note for the tone with Email 1, and in general, let's make sure it is empathetic and supportive. We want to call out pain points, but we want to do it more like: "maybe you've experienced this." Or "Some of our customers share that ____" when talking about negatives. What we don't want to do is make it sound like we're assuming things about the prospect, ie: "Hey you hate how you look in the mirror huh"?"
```

- **Source:** [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md); doc 2 "Claude Projects Example Prompts".
- **Status:** verbatim.
- **Notes:** the tone note ("maybe you've experienced this" / "Some of our customers share that ____") is the reusable fix for accusatory pain copy; add it to the first prompt. ⚠ compliance: "Some of our customers share that…" only with real customer statements.

### E2. Welcome series with cross-sells
- **Use when:** a new-customer welcome sequence that introduces complementary products with codes.
- **Inputs:** email count; which email introduces which product, code and URL; final store-wide offer.

```text
Now let's do a new customer welcome sequence for Unity Eye Serum. Let’s have it be 10 emails.

In email #3, let’s introduce our Opaline Riche Creme as a great compliment to Unity Eye Serum, and give the customer a 20% off code they can use when ordering it.

https://tryopal.com/products/opaline

In email #7 let’s introduce our Sacred Whipped Tallow and also offer a 20% off code.

https://tryopal.com/products/sacred

In email #10 let’s give them a 20% off store wide coupon.

https://tryopal.com/

Please provide an outline of the sequence to me and once I’ve approved it, I’ll have you write it.
```

Feedback on the outline:

```text
Okay nice. For Email 2 let's say "will be shipping soon if it hasn't already."

For email 3: let's make the code Rich20.

For Email 4 it seems like if it's going Day 5 a "one week checkin" doesn't make sense, it's too early. Let's move that to Email 5 (day 10) and move the rest of the emails back correspondingly.

Let's also do a new Email 4 that comes out on Day 5 - please provide suggestions.
```

```text
I think I like Option D the most for Email 4. Let's go ahead and write this sequence please.
```

- **Source:** [15-05 SRT 07:20–16:15](../lessons/15-05-claude-project-for-writing-email-sequences.md); doc 2 and doc 4 (conversation history).
- **Status:** verbatim.
- **Notes:** check send-day logic in every outline (a "one week check-in" on day 5 was the failure he caught). Only promise codes you will honour.

### E3. Site-wide holiday sale
- **Use when:** a short promotional sequence for a dated sale.
- **Inputs:** days; occasion; brand; scope; discount.

```text
Okay awesome job. Now I want to do a 3 Day sale for 4th of July for Opal Beauty. Let's make it site wide (all products), and they can save 30%. Please provide an outline.
```

Feedback:

```text
Thanks but let's do 3 emails on Day 3. Also don't forget about our other two Skus as well:
```

```text
Okay great, go ahead and write it please.
```

- **Source:** [15-05 SRT 16:15–21:25](../lessons/15-05-claude-project-for-writing-email-sequences.md); doc 2 and doc 6 (the two extra SKU URLs follow the first feedback line in the source).
- **Status:** verbatim.
- **Notes:** ⚠ compliance: deadline emails must match the real end time of the sale; no fake extensions.

### E4. Abandon cart sequence from a brief
- **Use when:** the product has a brief rather than a store page (here a financial newsletter).
- **Inputs:** brief; email count.

```text
This is the brief for a financial newsletter product. Please review and then come up with a 7 email abandon cart sequence outline. Once approved I'll have you write the sequence.
```

Feedback after the outline:

```text
Let's offer them an extra 25% off starting on Day 5.
```

- **Source:** [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md); doc 2.
- **Status:** verbatim.

## Funnel and economics
Only one funnel prompt appears in the course; the rest of 13-01 and 16-03 are worksheets and questions (see [funnel selection matrix](../concepts/funnel-selection-matrix.md), [funnel economics](../concepts/funnel-economics.md), [funnel audit](../rubrics/funnel-audit.md)).

### F1. Hidden factors seed prompt
- **Use when:** brainstorming the factors that decide funnel length for an audience of DTC operators (Stefan's prompt to build his training).
- **Inputs:** audience description; the factors you already have.

```text
I'm going to do training for my CA Pro (Copy Accelerator) mastermind members on "Hidden Factors" that determine the best funnel structure to use. This is for D2C business owners and their team members who run businesses doing between $3MM and $300MM a year who sell through funnels, advertorials, video sales letters, eCom landing pages, etc.

Some of the hidden factors I have listed so far include:

Market Awareness Levels -If the market is hyper aware of a solution, you don't need really long copy to sell them your product that offers this solution, it just needs to show why your product is the superior solution.

Demonstrable Proof - if you have a product that works quickly and you can show that in video or pictures, you don't necessarily need long copy either. For example, an instant stain remover like OxiClean. You can just show it working and removing stains a voila, you've proved it works. Meanwhile, if it's a supplement or a training guide etc, you will often need longer copy because you can't just a supplement working instantly. You can include animations that show what it does in the body and that can actually help you do shorter video ads vs. long form Video Sales Letters, but you still need more education.

Pricing - in general, the lower the price point, the less copy is needed. Classic example would be a free + shipping offer. You can
```

- **Source:** [13-01 01:30](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) (ChatGPT o3, on screen).
- **Status:** partial (screen cuts off after "Pricing"; the rest is not in the course files). Typo "a voila" is on screen.
- **Notes:** the finished 15-factor list and scoring bands are in the 13-01 doc; use [F2](#f2-score-an-offer-on-the-15-hidden-factors) to apply them.

### F2. Score an offer on the 15 hidden factors
- **Use when:** choosing a funnel structure (lean, medium, heavy) for an offer.
- **Inputs:** the 15 action-item lines (below, verbatim from the course doc); offer facts: price, traffic source, proof assets, category, device split.

Action-item lines (course doc, verbatim):

```text
1  Rate Level of Awareness From 1-5 with 5 being the Most Aware.
2  Rate Demonstrability of Product Efficacy From 1-5 with 5 Being The Most Demonstrable
3  Rate price point from 1-5, with 5 Being the Lowest Price Point and 1 Being the Highest
4  Rate the Level of Warmness of Your Primary Traffic Source From 1-5, with 5 Being Warmest.
5  Rate Brand Equity/Credibility Reserve from 1-5 with 5 Being Highest Brand Equity or Credibility Reserve
6  Rate Perceived Risk With Your Offer From 1-5, with 5 Being the Lowest Level of Perceived Risk
7  Rate Regulatory/Compliance Load For Your Offer From 1-5, with 5 Being Lowest
8  Rate Your Offer Complexity From 1-5, with 5 Being the Least complex
9  Rate How Important LTV is For Your Offer On a Scale From 1-5, with 5 Being "Least Important"
10 Rate Urgency of Market's Problem From 1-5, with 5 Being Most Urgent
11 Rate Competitive Saturation Of Your Market From 1-5, with 5 Being The Least Saturated.
12 Rate Buying Context & Device Attention Window From 1-5, with 5 Being Lowest Attention Span (and Mobile)
13 Rate Payment Friction From 1-5, with 5 Being Least Friction (ie. Free or very easy checkout)
14 Rate Community and Social Proof Assets for Your Offer From 1-5, with 5 Being The Most Social Proof/Strongest Community
15 Rate the Timeline for Results Customers Get From The Product You're Offering From 1-5, with 5 Being Fastest Results (ie. Instant, Same Day, etc).
```

Agent prompt (derived):

```text
Score this offer on the 15 Hidden Factors using the scale directions below (5 = least copy needed). For each factor give: score, one-line evidence from the product/offer facts I supplied, and "UNKNOWN - need: <fact>" if the facts are missing (do not guess). Then sum, map to Lean (46+), Medium (26-45) or Heavy (<=25), propose the matching chain, list the three lowest-scoring factors, and for each name one lever that could raise it and the test to run. Do not invent proof, stats or compliance clearances.
[paste the 15 action-item lines]
[paste offer, price, traffic source, proof assets, category, device split]
```

- **Source:** [13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) (docx/PDF action items; band thresholds 46+ / 26–45 / ≤25 from the doc's rule of thumb [44:00]).
- **Status:** action items verbatim; prompt derived (not a course asset).

## Review and feedback prompts
Stefan's editing loop: copy-chief the outline, then the draft; get a second model's view; merge section by section; then audit claims. [concept](../concepts/llm-copy-chief-editing.md) · [rubric: VSL review](../rubrics/vsl-review.md) · [rubric: LLM output claim audit](../rubrics/llm-output-claim-audit.md)

### X1. Second-model review of a lead
- **Use when:** you have an alternative opening (hook + micro-lead) and want another model's edit suggestions.
- **Inputs:** the opening pasted.

```text
Here's the start of another version that comes from Dr. Schilling. Is there anything you'd change or edit with it?
```

- **Source:** [07-02 v1 27:56–28:18](../lessons/07-02-medium-length-vsl.md) (dictated).
- **Status:** reconstructed (dictated).
- **Notes:** follow-up for an open loop the draft never closed (reconstructed): "The Morocco thing wasn't paid off right. Is there a different fascination we could use there that would create curiosity, but that does get paid off later in the VSL?" [07-02 v1 29:53–30:37] Check every opened loop is paid off.

### X2. Audit a VSL against the RMBC outline (derived)
- **Use when:** reviewing any VSL draft or competitor VSL for structure gaps, zig-zags and claims needing proof.
- **Inputs:** the script; the classic outline ([templates.md](templates.md)).

```text
You are auditing a VSL script against the RMBC outline (Hook/Microlead, Lead, Background, Discovery, UMP, UMS, Product Build-Up and Reveal, Close, CTAs, FAQ).
For each part, return: (1) start-end timestamp or paragraph range, (2) a verbatim line that proves the part exists, (3) which support points from the outline are present/absent, (4) a one-line fix.
Then list: structural zig-zags (a part that appears, ends, then reappears), claims that need substantiation, and fabricated-looking proof (unverifiable counts, live-viewer numbers, deadlines).
```

- **Source:** [04-01](../lessons/04-01-vsls-section-overview.md) Prompts.
- **Status:** derived (not a course asset).

### X3. VSL straight-line check (derived)
- **Use when:** a fast structural pass on a draft before line editing.
- **Inputs:** the script.

```text
VSL straight-line check
1. List each paragraph/scene with its outline part (Hook, Lead, Background, Discovery, UMP, UMS, Out-of-the-box fails, Product build-up, Reveal, Close, CTA, FAQ).
2. Flag any paragraph that belongs to an earlier part than the one before it (zig-zag).
3. Flag any "random" device: unrelated quiz, extra reason, extra story after the UMS.
4. Check: Does the lead promise ONE core idea, with extra hooks only at the end of the lead?
5. Check: Is the mechanism one cause + one metaphor + one recap sentence?
6. Check: Is there an explicit "why you can't just buy/do this elsewhere" beat before the reveal?
7. Check: Does the build-up use only real development facts?
8. Check: Does the close include features->benefits, future pacing, how to use, price anchor, guarantee, support contact, CTA?
9. List every claim, number, credential, testimonial and scarcity statement that needs proof.
```

- **Source:** [04-02](../lessons/04-02-vsl-fundamentals-classic-structure.md) Prompts.
- **Status:** derived (not a course asset).

### X4. Advertorial review checklist (derived)
- **Use when:** reviewing an LLM advertorial draft before it goes to design.
- **Inputs:** the draft; the live offer; the brief.

```text
- Every statistic and quote: is it on the source page / documented? If not, cut it or bracket it [VERIFY].
- Guarantee length, discount, "what's in the system", ingredient claims: match the live offer exactly.
- Enemy/villain: does it match our category (skincare vs pharma)? Is it needed at all?
- Story logic: for each step ask "why would he/she do that?"; add the missing motive.
- Length: if too long, ask for a shorter version rather than editing by hand; ask for "about" N% shorter.
- Testimonials and doctors: replace placeholders with real, permissioned ones or remove.
- Price: hide it and say "save XX%" unless the offer requires showing price.
```

- **Source:** [09-02 30:24–54:55](../lessons/09-02-claude-project-for-advertorials.md) (derived from the demo).
- **Status:** derived (not a course asset).

### X5. Feedback patterns used across the course
- **Use when:** writing your own correction message to an LLM; pick the pattern, then see the example prompt.
- **Inputs:** the draft and your diagnosis.

| Pattern | What to write | Course examples |
|---|---|---|
| Quote the line, name the flaw | Paste the exact line in quotes, then one sentence on why it's wrong | [M7](#m7-correct-an-awareness-mismatch-in-the-output), [U6](#u6-cross-sell-script-and-its-three-feedback-rounds) |
| Lock what's approved | "Please don't change anything up to [section]" / "everything after [section] is pretty much the same" | [V24](#v24-attach-the-forgotten-brief-and-lock-earlier-sections), [H11](#h11-swap-the-hook-keep-the-body) |
| Line edit | "SECTION (timing) [old] … Let's say: [new]" / "instead of: … Let's say: …" | [V34](#v34-line-edit-an-outline-then-write) |
| Numbered fixes in one message | 1. villain 2. length 3. offer fact 4. logic | [A8](#a8-multi-point-review-feedback), [B3](#b3-revise-the-brief-pricing-speaker-bonuses) |
| Read as the prospect | "my immediate objection is…" / "why would he do that?" | [V12](#v12-fix-bridges-and-logic-gaps-in-a-draft), [A9](#a9-add-a-missing-motive-to-the-story) |
| Awareness fit | "I had specified that [segment] aren't aware of…" | [M7](#m7-correct-an-awareness-mismatch-in-the-output), [V4](#v4-outline-feedback-promise-future-pace-hold-back-the-brand) |
| Tone and empathy | "maybe you've experienced this" instead of assuming; don't make them "feel like shit" | [E1](#e1-abandon-cart-sequence-with-a-discount-ladder), [U6](#u6-cross-sell-script-and-its-three-feedback-rounds) |
| Length by percentage | "about 50% shorter" / "about 20% shorter" | [A6](#a6-shorter-version-for-testing), [A8](#a8-multi-point-review-feedback) |
| Name the model to follow | "model more heavily off of the Emma and Synocell structure" | [U5](#u5-more-of-the-same-upsell-from-a-product-url), [V3](#v3-model-a-named-vsl-from-project-knowledge-financial) |
| Second model | same brief + outline to another model; merge section by section | [V7](#v7-draft-the-same-outline-in-a-second-model), [X1](#x1-second-model-review-of-a-lead) |
| Placeholders for missing proof | "fill these in with placeholders and I'll get real success stories later" → make them `[VERIFY: …]` | [V11](#v11-book-a-call-vsl-outline-problem-aware) |

- **Source:** compiled from the entries linked (derived).
- **Status:** derived index.

## Course blocks not reproduced here
The harvest of RMBC II lesson pages holds 241 fenced blocks. Blocks that are not LLM prompts, project instructions or prompt inputs are kept elsewhere:
- **VSL structures and outlines** (classic "Very Simple Sales Letter Outline", lead, background/UMP, build-up, close, Nooro and MiamiMD medium outlines, short-VSL structures, in-feed vs on-page, nope sequence, UMS beat): [templates.md](templates.md); lessons [04-01](../lessons/04-01-vsls-section-overview.md) to [04-11](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md), [07-03](../lessons/07-03-3-7-minute-vsl.md).
- **Advertorial, PDP, upsell and email structures** (Claude's "Structure Maintained" list, Happy Mammoth and Dr. Clean PDP templates, price-comparison block, RejuvaKnee 12-step outline, Dr. Clean upsell page copy, email skeletons, reorder/winback timing): [templates.md](templates.md).
- **Classic RMBC Brief (12 fields)**: [05-01](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md); see [brief 2.0](../concepts/brief-2-0.md).
- **Upsell idea lists** ("Upsell #1 Big Idea", "What are we selling", improved-version examples): [14-01](../lessons/14-01-upsells-overview.md), [upsell formula](../concepts/upsell-formula.md).
- **Checkout microcopy** ([11-01](../lessons/11-01-checkouts-walkthrough-part-1.md), [11-02](../lessons/11-02-checkouts-walkthrough-part-2.md)), **Google Ads slides** ([12-03](../lessons/12-03-google-ads.md)), **native-ads notes** ([12-02](../lessons/12-02-native-ads.md)), **TikTok weekly testing checklist** ([12-04](../lessons/12-04-tiktok-ads.md)): [checkout optimization](../frameworks/checkout-optimization.md), [paid traffic by platform](../frameworks/paid-traffic-by-platform.md).
- **Funnel rule of thumb, economics questions and worksheets** ([13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md), [14-01](../lessons/14-01-upsells-overview.md), [16-03](../lessons/16-03-funnel-economics-with-spg.md)), **CRO hypothesis template** ([16-01](../lessons/16-01-cro-with-4080-marketing.md)), **VSL benchmark checklist and clincher lines** ([16-05](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)): [funnel economics](../concepts/funnel-economics.md), [cro testing](../frameworks/cro-testing.md), [benchmarks](benchmarks.md).
- **Webinar scripts** (elephant in the room, bridges, price drop, financing, fast-action bonuses, text-in CTA, comment-to-DM; guest Dylan Vanas): [16-04](../lessons/16-04-webinars-live-talk.md), [webinar funnel](../frameworks/webinar-funnel.md).
- **Mid-course pipeline recap**: [08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md), [RMBC pipeline](../concepts/rmbc-pipeline.md).
- **Prompts referenced but not in the course files:** the Claude cleanup prompt for the Beverly Hills script ([04-05 02:38](../lessons/04-05-vsl-product-buildup-and-reveal.md), [04-06 18:30](../lessons/04-06-vsl-closes.md)); the full short-VSL project instruction ([07-04](../lessons/07-04-short-vsl.md)); the rest of the 13-01 seed prompt; the Veo 3 Interview, Multi-Scene, Copywriter and Data Analysis prompts ([12-04](../lessons/12-04-tiktok-ads.md)); the saved blood-sugar hook prompt ([07-03](../lessons/07-03-3-7-minute-vsl.md)). Don't reconstruct them as if they were course text.

## Cross-course notes
| Job | RMBC II (this page) | Evolve Start Here | Tether Lab |
|---|---|---|---|
| Market awareness | [R1](#r1-market-awareness-deep-research): TAM + % per stage via deep research | [P04 awareness-level headline prompt](../../../evolve/start-here/libraries/prompts.md#p04-awareness-level-headline-prompt) | [prompt index](../../../../libraries/prompts.md) |
| Customer psychology research | [R3](#r3-psychographic-deep-research)–[R6](#r6-unified-research-document): RMBC research questions → unified doc | [P06 Desire AI Deep Research](../../../evolve/start-here/libraries/prompts.md#p06-desire-ai-deep-research-prompt) | [customer research stack](../../../../frameworks/customer-research-stack.md) |
| Mechanism | [M1](#m1-one-off-ump-ideation)–[M4](#m4-mechanism-expansion-into-vsl-copy): LLM ideates, ranks and expands UMP/UMS | [P09 New Mechanism Finder](../../../evolve/start-here/libraries/prompts.md#p09-new-mechanism-finder-prompt) | n/a |
| Angles and hooks | [H1](#h1-deep-research-hook-generation)–[H11](#h11-swap-the-hook-keep-the-body): hook database, then hook swaps on a locked body | [P16 Angle Identifier](../../../evolve/start-here/libraries/prompts.md#p16-angle-identifier-prompt), [angle generation prompt](../../../evolve/start-here/frameworks/angle-generation-prompt.md) | [prompt index](../../../../libraries/prompts.md) |

- **Agreement:** all three treat LLM output as a draft that a human directs and fact-checks. Evolve: AI gets you "70, 80% of the way there" and must not invent social proof ([Evolve: AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md)). Stefan: "get a great first draft, tweak, modify, edit, and ship" [07-01 v2 06:38](../lessons/07-01-long-form-vsl.md).
- **What RMBC adds:** one Claude Project per asset type with example files as knowledge; the outline-first gate with a length estimate; "continue" prompts for long assets; a second model for a parallel draft; hook swaps on a locked body.
- **Difference:** Stefan's own prompts repeatedly ask the model to fill gaps with placeholders, invent personas or "use placeholders to come up with the strongest brief possible" ([B2](#b2-placeholder-brief-from-ingredients-only), [B7](#b7-draft-an-offer-overview-with-an-llm-training-examples-only)). Evolve's position is "don't let a prompt invent social proof". **Agent default:** follow Evolve and the repo rule. Placeholders are allowed only as visible `[VERIFY: …]` slots, never as finished copy.

## Related
- Concepts: [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [Composite vs swipe](../concepts/composite-vs-swipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Unique mechanism](../concepts/unique-mechanism.md) · [Brief 2.0](../concepts/brief-2-0.md) · [Compliance red flags](../concepts/compliance-red-flags.md)
- Frameworks: [Deep research workflow](../frameworks/deep-research-workflow.md) · [UMP ideation and evaluation](../frameworks/ump-ideation-and-evaluation.md) · [Brief generator](../frameworks/brief-generator.md) · [VSL build with Claude](../frameworks/vsl-build-with-claude.md) · [Hook generation system](../frameworks/hook-generation-system.md) · [Advertorial build](../frameworks/advertorial-build.md) · [PDP build](../frameworks/pdp-build.md) · [Upsell flow build](../frameworks/upsell-flow-build.md) · [Email sequences](../frameworks/email-sequences.md)
- Libraries: [README](README.md) · [Templates](templates.md) · [Hooks](hooks.md) · [Rules](rules.md) · [Benchmarks](benchmarks.md)
- Rubrics: [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [VSL review](../rubrics/vsl-review.md)
