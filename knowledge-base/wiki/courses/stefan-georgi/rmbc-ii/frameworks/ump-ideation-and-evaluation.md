---
title: "UMP/UMS ideation and evaluation (multi-LLM mechanism process)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-01-unique-mechanisms-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-02-ump-ideation-with-llms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md
tags: [unique-mechanism, ump, ums, ideation, evaluation, expansion, multi-llm, claude-project, awareness, framework]
updated: 2026-11-02
---

# UMP/UMS ideation and evaluation
> Run the ideation prompt on several LLMs, cut the outputs by hand, rank the shortlist with the evaluation prompt on three LLMs, write the top two out as VSL-style mechanism sections, fix names, metaphors and awareness assumptions, then pick one or test both.

## 🤖 Agent use
- **Use when:** a [unified research document](../concepts/unified-research-document.md) exists and you need the mechanism (problem half + solution half) that the brief, VSL, advertorial, PDP or ads will run on; or when an existing mechanism needs a challenger.
- **Inputs → outputs:** unified research doc (PDF) + product line + niche + target awareness segment (+ ingredient list for supplements/skincare) + any live mechanism copy → a "potential mechanisms" doc, three LLM rankings, two VSL-format mechanism sections, renamed and simplified terms, and a decision (one mechanism, or two to test). That output feeds the [brief generator](brief-generator.md).
- **Rules:**
  - **DO** write every mechanism as a pair: UMP (why they failed before) + UMS (why our product succeeds where others failed). "It's important to identify the unique mechanism behind both the problem AND the solution." [03-01 02:01](../lessons/03-01-unique-mechanisms-overview.md)
  - **DO** put the awareness segment in every prompt: "For this exercise, let's specifically focus on people in the market who are Problem Aware." Without it, outputs drift to product-aware people. [03-02 02:07; v2 00:00](../lessons/03-02-ump-ideation-with-llms.md)
  - **DO** run ideation on 2–4 LLMs, deep-research modes included. "You really need to be LLM agnostic." [03-04 27:33–28:40](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DO** judge the idea, not the name: "we could always change the name". [03-04 03:39](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DON'T** keep a mechanism that needs an ingredient, feature or service the product lacks. "We don't have a chronobiology regulator"; on lymphatic congestion: "So I'm making that up." [03-04 24:07–25:44; 32:50–33:30](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DON'T** treat the LLM ranking as the decision. It stands in for experience; it doesn't replace judgment. [03-03 00:00–05:09](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
  - **IF** health or beauty **THEN** prefer simple mechanisms with few cognitive leaps: "I want as few cognitive leaps as possible. I want stuff they kind of know is true, and here's the one thing you were missing." [03-04 19:19–20:50; 30:44](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **IF** you have a live offer **THEN** test both finalists in ads or advertorials and build the VSL on the winner. [03-03 19:34; 48:22](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
  - **IF** health or wellness copy **THEN** don't call the cause "the root cause". "You're really not compliance-wise supposed to … that's a diagnostic thing." [03-01 18:46](../lessons/03-01-unique-mechanisms-overview.md)
  - **DON'T** carry any number, study, client count or ingredient-effect claim from an LLM mechanism draft into copy without a real source. Use `[VERIFY: …]`. (derived; see [Compliance](#compliance))
- **See also:** [Unique mechanism concept](../concepts/unique-mechanism.md) · [Prompts library](../libraries/prompts.md) · [Deep research workflow](deep-research-workflow.md) · [Brief generator](brief-generator.md) · [Product-market awareness](../concepts/product-market-awareness.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [Evolve: unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md)

## What it is
Module 3's procedure for getting from research to one copy-ready mechanism. The LLMs generate volume. The human does the screening: awareness fit, a tangible UMS, fidelity to the product, few cognitive leaps. Cross-LLM ranking is a tiebreaker, and expansion into real copy is the feel test. It matters because every later asset (brief, VSL, advertorial, PDP, ads) carries the mechanism. In Stefan's words, a mechanism can fail just by being aimed at the wrong awareness segment. [03-01 03:22](../lessons/03-01-unique-mechanisms-overview.md); [03-02 05:55](../lessons/03-02-ump-ideation-with-llms.md)

## Inputs checklist
- [ ] Unified research document as a PDF ([deep-research-workflow](deep-research-workflow.md)). [03-02 01:04](../lessons/03-02-ump-ideation-with-llms.md)
- [ ] One-line product description and niche.
- [ ] Target awareness segment, chosen deliberately. Course defaults: biz-op is Problem Aware; the eye serum is Solution Aware because that is "probably the biggest segment". [03-02 v2 00:00](../lessons/03-02-ump-ideation-with-llms.md); [03-04 00:59–02:01](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- [ ] The awareness-profile paragraph for that segment, copied from the unified research doc (needed for expansion). [03-04 57:43–1:00:58](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- [ ] Supplements and skincare: the ingredient list. [03-04 02:01](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- [ ] Any live mechanism's real page copy, so it competes fairly. [03-04 38:37–39:36](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- [ ] Ingredient-claims research ([02-05](../lessons/02-05-ingredient-deep-research.md)) for substantiating the UMS later.
- [ ] Access to at least three LLMs (course: Gemini 2.5 Pro and Deep Research, Perplexity Deep Research, ChatGPT o3-pro, Claude; Poe for multi-model access).

## Steps

### Step 0 — Set up the Unique Mechanisms Claude Project (once)
- **Input:** the nine course PDFs (definition docs, the Genesis SPG process, worked UMP/UMS examples, the VSL outline, a mechanism-training call transcript, example VSLs). For our use, replace them with our own definition doc, compliant mechanism examples and the [classic VSL structure](../concepts/classic-vsl-structure.md).
- **Output:** a project used for expansion (Step 5). Stefan says its own ideation output "weren't actually that good". [03-03 18:23–19:34](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Prompt** (description *and* instructions; verbatim, "GPT" and "Were" are in the source):
```text
Were going to create a GPT that helps people come up with new Unique Mechanisms for Direct to Consumer and direct response oriented marketing campaigns. I'll upload several documents - the core one will be what Unique Mechanisms are (both types) WITH Examples and we'll have other documents uploaded as well that train you on the process.
```
- **Tool/model:** Claude Projects (Sonnet 4 on screen). [03-05 00:00–01:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)
- **Check:** description = instructions ("I just basically took the same thing from the description, put it here" [03-05 00:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)); knowledge files include examples, not only definitions. Stefan says the project is "not what I do all the time" but is "worth experimenting with". [03-05 00:28; 01:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)

### Step 1 — Ideate on several LLMs
- **Input:** research PDF + filled ideation prompt (+ ingredients).
- **Output:** 5–20 named UMP/UMS candidates per model.
- **Prompt:** "LLM One-Off UMP Ideation Prompt" (verbatim template, course doc `02-2 UMP Ideation With LLMs.docx`; fill `_____PRODUCT____`, `_____NICHE___` and the awareness line):
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
  For physical products, append the ingredient block used in the eye-serum fill: "Additionally, I have included a list of product ingredients for your consideration:" followed by the list. [03-02 docx Example #2](../lessons/03-02-ump-ideation-with-llms.md)
- **Optional brainstorm prompt:** the course's "Alternate 'Weird' AgentGPT UMP Process" asks for "really interesting and out of the box" UMPs. Its examples are manifestation-supplement mechanisms (pineal gland, negative ions), and it tells the model to "search the web to add in proof elements… just make sure to include citations". Full text is in [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) and the [prompts library](../libraries/prompts.md). Use it for divergence only. Its examples are not reusable claims.
- **Tool/model:** Airbnb run: Gemini (2.5 Pro and Deep Research) was best, while ChatGPT and Claude deep research gave "cute nicknames for really basic stuff". [03-02 41:50–43:09](../lessons/03-02-ump-ideation-with-llms.md) Eye-serum run: Perplexity Deep Research was best because its ideas were simpler, with Gemini Deep Research second. [03-04 16:59–20:50; 37:21–38:02](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Check before moving on:** you have read every output end to end ("reserve your judgment" [03-02 04:18](../lessons/03-02-ump-ideation-with-llms.md)) and saved each raw output.

### Step 2 — Screen by hand into a "potential mechanisms" doc
- **Input:** all raw outputs.
- **Output:** one running doc (a tab or heading per mechanism), each entry "The Problem (UMP) – <name>" + explanation, then "The Solution (UMS) – <name>" + explanation. [03-04 38:02–39:36](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Screening questions** (the criteria Stefan used; he defers a formal framework):

| Test | Keep if | Source |
|---|---|---|
| Awareness fit | Speaks to the chosen segment, not "too far along in the mental journey" | [03-02 05:55](../lessons/03-02-ump-ideation-with-llms.md) |
| Tangible UMS | It says why this will be different, not only "we're gonna help you through" | [03-02 38:45–40:16](../lessons/03-02-ump-ideation-with-llms.md) |
| Product fidelity | Needs nothing the product doesn't teach, contain or do | [03-02 13:32](../lessons/03-02-ump-ideation-with-llms.md); [03-04 32:50](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Substance | More than "saying something obvious in a fancy way" | [03-02 v2 12:30](../lessons/03-02-ump-ideation-with-llms.md) |
| Cognitive leaps | One missing piece the reader half-believes already | [03-04 30:44](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Hero novelty | Hero ingredient isn't commonplace (vitamin C/E rejected as "not exciting enough") | [03-04 15:03](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Segment breadth | Not tied to a niche sub-group (FIRE followers, guru-aware buyers) unless that group is the target | [03-02 31:19–34:11](../lessons/03-02-ump-ideation-with-llms.md) |

- **Check before moving on:** the live mechanism, if there is one, is in the doc in its real page wording. [03-04 39:36](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) Save the doc as a PDF.

### Step 3 — Rank the shortlist on three LLMs
- **Input:** unified research PDF + shortlist PDF, both uploaded as files, not pasted. [03-03 06:37](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Output:** three ranked lists with reasons; mark the consensus top 2, outliers and each model's watch-outs.
- **Prompt:** evaluation prompt (verbatim, course doc `03-3 UMP Evaluation Prompt.docx`; PRODUCT, NICHE and the awareness level are placeholders):
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
  Solution Aware variant: only the last paragraph changes ("…our core market is people who are Solution Aware."). [03-04 44:00](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Tool/model:** a fresh chat per model. Course runs used Claude (plain chat, or inside the project), ChatGPT o3-pro and Gemini 2.5 Pro. [03-03 05:09–13:56](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Check before moving on:** compare the consensus pick with the research doc's top pain. If a model ranks high for a secondary concern, ask it why (Step 3b).

### Step 3b — Reconcile (optional)
- **Option A:** give all three rankings to one LLM: "here's the rankings for a unique mechanism... which would you pick?" (spoken, approximate). [03-03 18:23](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Option B:** ask the model to justify a ranking that doesn't match the top pain. In the eye-serum run, Gemini argued that fear of irritation is a "meta problem" blocking belief; Stefan conceded it may "influence me to some level". [03-04 46:25–52:00](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Option C:** the "combine them" prompt (verbatim):
```text
If you were going to take these different mechanism options, and combine them into a new mechanism that you thought was the strongest and that speaks to their pain points (which are primarily appearance driven, followed by what they don't like about products), what would you do?
```
  Reject the merge if it adds steps or analogy clutter. Claude's "Triple Collapse Cascade" was rejected because the market "kind of don't like these multi-step systems". [03-04 45:35; 50:00–53:57](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)

### Step 4 — Expand the top 2 into VSL-format mechanism sections
- **Input:** unified research PDF + one mechanism summary + the awareness line (+ the awareness-profile block for Solution Aware).
- **Output:** a VSL-style UMP→UMS section per finalist. It tests feel, not final copy: "see what our mechanism could look like in real copy". [03-03 19:34–21:06](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Prompt:** expansion prompt (verbatim template, course doc `04-4 Claude_UMP Expansion Prompt.docx`; bracketed parts are the fill):
```text
We're going to do an in-depth unique mechanism for a product. I've attached a unified research document that should give you a strong overview of the target market.

Here is a summary of the UMP and UMS:

[PASTE ONE MECHANISM: "The Problem (UMP) - <name>" with its explanation, then "The Solution (UMS) - <name>" with its explanation]

===
For this exercise, let's specifically focus on people in the market who are [Problem Aware | Solution Aware].

[ONLY FOR SOLUTION AWARE: paste the awareness profile block below]

Please go ahead and write the Unique Mechanism section in a format that could be used in a video sales letter.
```
  Awareness block header used in the course: "Here's how you can understand Solution Aware in this context:", followed by the segment profile from your own research doc. The course's eye-serum profile (percentages, persona) is specific to that research; don't reuse it. [03-04 doc Examples 3–4](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Tool/model:** Claude inside the Unique Mechanisms project, with a new chat per mechanism ("I like to keep it clean"). Gemini without a project gave a usable but weaker draft: "this is why I tend to use Claude for copy". [03-03 35:29; 38:34–40:36](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Check before moving on:** the draft doesn't assume knowledge the segment lacks. The first eye-serum draft assumed peptide awareness and failed this check. [03-04 57:43; 1:05:10–1:08:25](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)

### Step 5 — Critique and revise in the same chat
- **Input:** the expansion draft.
- **Output:** V2 with corrected logic, plain names and a metaphor that suits the persona.
- **Prompts used** (verbatim, typed on screen):
```text
Okay a couple of things. First, you said: "The reason your peptide eye creams haven't worked isn't because peptides don't work. It's because they've been targeting the wrong problem entirely," but I had specified that solution aware people we are talking to aren't necessarily aware of peptide eye creams right?
```
```text
I like: the idea of our: Structural Renewal System

I like: "The Targeted Repair Kit" but let's call it a Targeted Repair Complex

And third let's go with: Integrity Locking Compou[nds]
```
  Reconstructed from speech (a pattern, not a quote) [03-04 1:08:25; 1:13:18](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md):
```text
Second, I don't love the name "Dermal Disarray", and I'm not sure about the tent analogy. What other more believable, legit-sounding names can we use instead of Dermal Disarray? And what are some other analogies or metaphors we could use instead of a tent, keeping in mind our target market?
```
  Logic-correction pattern, also reconstructed [03-03 26:40–28:19](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md):
```text
I think this is great, but I wonder if it's really an "income gap world" vs "asset gap world". It's more that they think they have an income gap, but what they really have is an asset gap. We show you how to bridge that gap. People don't get rich from income; they get rich from assets. Write another version of the UMP that takes this into consideration.
```
- **Method:** ask for 5+ alternative names and metaphors, pick, tell the model your picks, and have it rewrite. You don't have to tie every part to the metaphor. [03-04 1:13:18–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Check before moving on:** run the [LLM output claim audit](../rubrics/llm-output-claim-audit.md) on every revised line, and replace stats, client counts and legal assertions with `[VERIFY: …]`.

### Step 6 — Decide
- **Input:** the rankings, the V2 sections, the objection count per finalist.
- **Output:** one mechanism (or two in test), plus the reason it won, recorded for the brief.
- **Order of decision** (Stefan's): (1) existing offer: test both; (2) new offer: sleep on it and explain both to a few people; (3) still unsure: take the consensus #1. Tiebreaker: fewer objections. The permission-based mechanism lost because "you're still serving at the leisure of Airbnb". [03-03 48:22–49:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) "Maybe both will work. So maybe you don't have to agonize over the decision." [03-03 49:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
- **Check before moving on:** the winner fits the 4-line logic flow (next section) and every causal claim in it has a source or a `[VERIFY]` tag.

## Decision points
| IF | THEN | Source |
|---|---|---|
| Outputs skew product-aware | Re-run the base prompt with the awareness line (and the segment breakdown) rather than a follow-up | [03-02 36:15; v2 00:00](../lessons/03-02-ump-ideation-with-llms.md) |
| "Give me more like number three" returns weak near-copies | Drop the follow-up and re-run the base prompt tighter | [03-02 17:09–20:18](../lessons/03-02-ump-ideation-with-llms.md) |
| Physical product (supplement, skincare) | Add the ingredient list; skip mechanisms with no matching ingredient | [03-04 02:01; 07:38](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Biz-op / coaching (Problem Aware or unaware) | A simple core may be framed as more sophisticated ("the trick is making them seem more complex") (instructor claim) | [03-04 19:19–20:50](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Health / beauty | Simpler wins; reject multi-step "systems" and two-leap mechanisms | [03-04 20:19; 53:57](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Segment already knows the cause (solution aware) | Don't rename the cause; concede it and reframe why other solutions fail (golf: "squares the face for you") | [03-01 18:46–21:21](../lessons/03-01-unique-mechanisms-overview.md) |
| A mechanism suits a more aware segment | Shelve it for retargeting / deeper funnel ("keep for deeper funnel retargeting", a model note Stefan read out) | [03-03 13:21](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| LLMs rank high for a non-top pain | Ask the model to justify against the research doc before accepting | [03-04 46:25–52:00](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| A live mechanism already sells | Include it in the shortlist in its real wording; LLM rank does not override sales data (derived: his DEJ mechanism ranked about #5 in all three LLMs) | [03-04 39:36; 53:57](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Offer exists | Test both finalists as ad/advertorial hooks; write the VSL on the winner | [03-03 19:34; 48:22](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Brand-new offer, still torn | Human reactions → gut → consensus #1 | [03-03 48:22–49:23](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Asset is an advertorial that sells the click | Give only "the missing 1%", not full detail | [03-01 08:44–09:47](../lessons/03-01-unique-mechanisms-overview.md) |

## Failure modes and fixes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| "Cute nicknames for really basic stuff" | Weak model or mode for this task | Use Gemini or Perplexity deep research for ideation | [03-02 41:50](../lessons/03-02-ump-ideation-with-llms.md); [03-04 35:30–36:36](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Ideas all aimed at product-aware buyers | No awareness line in the prompt | Add "For this exercise, let's specifically focus on people in the market who are [X] Aware." | [03-02 05:55; v2 00:00](../lessons/03-02-ump-ideation-with-llms.md) |
| Overcomplicated, jargon names ("Elastase Cascade Neutralizer", "Bio-Tensegrity") | Model optimises for sounding scientific | Ask for 5+ plainer names and new metaphors; pick for the persona | [03-04 11:23–13:33; 1:13:18–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Expansion draft assumes knowledge (e.g. "your peptide eye creams") | Awareness level named but not defined | Paste the segment profile from the research doc into the expansion prompt | [03-04 57:43–1:02:08](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Problem frame feels off ("move from income-gap world to asset-gap world") | Model built a two-worlds metaphor rather than a diagnosis | Rewrite as "you think you have X, what you really have is Y" | [03-03 25:25–31:56](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Mechanism needs something the product lacks (portfolio building, lymphatic ingredient, probiotic) | Model ignores product fidelity | Cut it, or flag the mismatch before saving | [03-02 13:32](../lessons/03-02-ump-ideation-with-llms.md); [03-04 26:16; 32:50](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Combined "super-mechanism" with three steps and a construction-crew analogy | Merge prompt stacks every idea | Reject; keep one cause and one fix | [03-04 50:00–53:57](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Models disagree wildly (Capital Multiplier #9 vs #3) | Ranking is opinion, not data | Use consensus across 3 models plus objection count; test if possible | [03-03 11:16–17:45](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Draft contains "after helping hundreds of people…", market-size stats, "completely legal" | Model fabricates proof and legal assertions | Strip; replace with `[VERIFY: …]` or real proof | [03-03 41:18; 43:09–45:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Claude errors or refuses uploads | Attachment issues | Re-upload in a new chat; if attachments fail, see the plain-text PDF fix in [deep-research-workflow](deep-research-workflow.md) | [02-04 16:39–21:42](../lessons/02-04-unified-research-process.md) |

## Output contract
The mechanism doc handed to the [brief generator](brief-generator.md) (derived from the course docs and the 03-01 handout):

| Field | Content | Source |
|---|---|---|
| Target segment | Awareness level + the profile paragraph from the research doc | [03-04 57:43](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Current belief | What the prospect thinks causes the problem ("you thought it was collagen") | [03-01 07:43](../lessons/03-01-unique-mechanisms-overview.md) |
| UMP name + 1-sentence explanation | The missing piece, in plain words | [03-01 06:18; 09:47](../lessons/03-01-unique-mechanisms-overview.md) |
| UMP analogy | One picturable metaphor ("interior designers", "fabric weave") | [03-01 06:18](../lessons/03-01-unique-mechanisms-overview.md); [03-04 1:10:45](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Why past solutions failed | Tied to the UMP | [03-01 02:01](../lessons/03-01-unique-mechanisms-overview.md) |
| UMS name + parts | What the product does to the cause; map each part to a real ingredient/feature | [03-04 1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Proof slots | `[VERIFY: study/source for cause]`, `[VERIFY: ingredient evidence]`, testable-proof line | [03-05 SPG step iii](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) |
| Known objections | From the ranking watch-outs | [03-03 09:16–12:49](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Runner-up | Second mechanism for testing | [03-03 48:22](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |

Four-line logic flow (course "SPG process", Genesis doc in [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)):
```text
i.   The real reason other solutions don't work is because of Y
ii.  When in reality, you need X
iii. Here's the proof (your research and scientific backing)
iv.  Here's how our product enables you to do X
```

## Compliance
- A mechanism is a causal claim. Every UMP cause and every UMS effect must be true and substantiated before it reaches copy. LLM mechanism text is ideation, not evidence. (derived; [AGENTS.md](../../../../../../AGENTS.md) rule 2)
- Course examples are **structure only; claims not reusable**. That covers "collagen loss at 3x the rate", "9 out of 10 eye creams… are essentially expensive moisturizers", the 72-hour hydration lock, cupuacu butter "up to 440% of its own weight", and "inhibits MMPs" (eye serum); "$5,000 to $15,000 to get started", "15 to 35% profit margins" and "after helping hundreds of people" (Airbnb); and colon transit time, DHT blocking collagen and the manifestation-supplement examples (03-05 PDFs). [03-03 Sources and limitations](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md); [03-04 Sources and limitations](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md); [03-05 Examples](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)
- Supplements and cosmetics: write structure/function or appearance wording ("supports", "helps the look of"). Claims that a product rebuilds collagen, inhibits enzymes or treats a condition read as drug claims. Use `[VERIFY: ingredient + dose + study]` from [02-05 ingredient research](../lessons/02-05-ingredient-deep-research.md). See [compliance red flags](../concepts/compliance-red-flags.md).
- Avoid "root cause" and diagnostic phrasing in health copy. [03-01 18:46](../lessons/03-01-unique-mechanisms-overview.md)
- Biz-op: no earnings figures or "passive income" promises without typical-results substantiation (FTC/Meta). Don't use real platforms (Meta, Shopify, Uber, DoorDash) as villains without review. [03-02 Compliance notes](../lessons/03-02-ump-ideation-with-llms.md)
- The "weird" prompt's specificity advice ("Harvard, Nobel Prize Winning Scientists… boosted by 110%") applies only with real, citable names and numbers. Never let the model supply them. [03-05 Templates](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)

## Worked examples
| Case | Segment | Path through the framework | Outcome | Source |
|---|---|---|---|---|
| Airbnb rental-arbitrage coaching (biz-op) | Problem Aware | 19 ideas screened from Gemini, ChatGPT and Claude → shortlist → Claude and ChatGPT both ranked "Asset Gap vs Income Gap" #1 and "Permission-Based Income Trap" #2; Gemini reversed them → both expanded → V1 logic rewritten to "you think you have an income problem. But what you really have is an asset problem." | Gun-to-head pick: Asset Gap (fewer objections) | [03-02](../lessons/03-02-ump-ideation-with-llms.md); [03-03 06:37–49:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Peptide eye serum (skincare) | Solution Aware | Gemini DR (5 concepts) + Perplexity DR (12) + others → 12-item shortlist incl. the live DEJ mechanism → all three LLMs put Lipid Barrier Breach, Dermal Disarray and Chronic Dehydration Debt in the top 3 → expansion needed the awareness block → "Dermal Disarray"/tent renamed "Collagen Architecture Breakdown"/fabric weave; UMS parts renamed Structural Renewal System, Targeted Repair Complex, Integrity Locking Compounds | Top two expanded; the VSL is written later in the course | [03-04 02:35–1:19:14](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Mechanism teardown set (structure only) | Mixed | Miami MD (collagen → fibroblasts), Unity eye serum PDP (DEJ "hooks"), Emma (methane), Performance Golf (face squared for you) | Shows mechanism depth by asset type and awareness | [03-01 04:55–22:29](../lessons/03-01-unique-mechanisms-overview.md) |

Rewrite pattern worth keeping: "You've been trying to solve a(n) [X] problem with a(n) [Y] solution" → "You think you have [X]. What you really have is [Y]." [03-03 21:46; 30:13](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)

## Where it's taught
| Lesson | What it adds | Timestamps |
|---|---|---|
| [03-01 Unique mechanisms overview](../lessons/03-01-unique-mechanisms-overview.md) | Definition, UMP/UMS, awareness fit, four teardowns, "root cause" aside | [01:01–03:22; 04:55–22:29] |
| [03-02 UMP ideation with LLMs](../lessons/03-02-ump-ideation-with-llms.md) | Ideation prompt, multi-LLM run, screening criteria, awareness-line fix | [v1 00:00–46:18; v2 00:00–16:13] |
| [03-03 Evaluation prompt (Airbnb)](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) | Evaluation prompt, three-LLM ranking, expansion, V1→V2 logic fix, decision order | [05:09–49:54] |
| [03-04 Eye-serum walkthrough](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) | Ingredients in ideation, simplicity rule, combine prompt, awareness block, rename/re-metaphor | [00:00–1:19:14] |
| [03-05 Claude Project for mechanisms](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) | Project setup, nine knowledge PDFs, SPG logic flow, "weird" prompt | [00:00–01:28; PDFs] |

## Cross-course notes
- **Who invents the mechanism.** RMBC has the copywriter and the LLMs *generate* candidate cause-and-fix framings from market research, then filter them for product fidelity. Stefan states mechanism quality depends on framing and awareness ("Do I actually like this mechanism a lot? Not really, but it doesn't matter" [03-01 06:18](../lessons/03-01-unique-mechanisms-overview.md)). Evolve Start Here *finds* mechanisms in the product: inventory components, label them "assumed" until research validates them, and check every finder-prompt output against the product page ([product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md)). Evolve Copywriting adds "It doesn't have to be better. It just has to be new" ([unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md)). **Agent default:** run Evolve's product inventory first, then RMBC ideation with the ingredient/feature list attached. Accept only UMS parts that map to a real component and UMP causes with a source.
- **Awareness.** Evolve says lead with a new mechanism in product-aware or sophisticated markets. RMBC screens out product-aware mechanisms when the target is the broad problem-aware market, choosing the segment first for scale (instructor claim at [03-02 34:11](../lessons/03-02-ump-ideation-with-llms.md)). The two are compatible once the segment is fixed. See [Evolve market awareness](../../../evolve/copywriting/concepts/market-awareness.md) and [market awareness levels](../../../evolve/start-here/concepts/market-awareness-levels.md).
- **Plain language.** RMBC's "simple mechanisms win in health and beauty" agrees with Evolve's [compression and plain language](../../../evolve/copywriting/concepts/compression-and-plain-language.md).
- **Tether.** [Perception management](../../../../concepts/perception-management.md) warns not to claim the USP as the use case. That applies to UMS naming here.

## Related
- [Unique mechanism (concept)](../concepts/unique-mechanism.md) · [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Product-market awareness](../concepts/product-market-awareness.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Classic VSL structure](../concepts/classic-vsl-structure.md)
- Upstream: [Deep research workflow](deep-research-workflow.md) · Downstream: [Brief generator](brief-generator.md) · [VSL build with Claude](vsl-build-with-claude.md) · [Advertorial build](advertorial-build.md)
- [Prompts library](../libraries/prompts.md) · [Templates](../libraries/templates.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [Offer to funnel end to end](../playbooks/offer-to-funnel-end-to-end.md)
