---
title: "Unique mechanism (UMP + UMS) in RMBC II"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-01-unique-mechanisms-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-02-ump-ideation-with-llms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-04-vsl-background-stories-and-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-08-medium-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
tags: [rmbc-ii, unique-mechanism, ump, ums, mechanism-ideation, evaluation, llm, knowledge-gap]
updated: 2026-11-02
---

# Unique mechanism (UMP + UMS) in RMBC II
> A two-part logical connection: the UMP (the real, previously missing reason the prospect's past attempts failed) and the UMS (the one thing our product does about that reason). RMBC II generates many candidates with LLMs, screens them by hand for awareness fit and simplicity, ranks the shortlist across several LLMs, then expands the top two into VSL-format copy to judge them in context.

## 🤖 Agent use
- **Use when:** before a brief, VSL, advertorial, PDP or ad needs a "why this is different" core; auditing a page for "where is the UMP and UMS?"; an offer is "fatiguing".
- **Inputs → outputs:** unified research doc + product facts (ingredient list / features / process) + target awareness level → long candidate list (several LLMs) → hand-screened shortlist doc → cross-LLM ranking → top-2 expanded VSL sections → one chosen, renamed, plain-language "UM doc in expanded copy format" for the brief generator.
- **Rules:**
  - **DO** write both halves: "It's important to identify the unique mechanism behind both the problem AND the solution." UMP = why they failed; UMS = why ours succeeds "where other alternatives have failed". [03-01 02:01–03:22](../lessons/03-01-unique-mechanisms-overview.md)
  - **DO** frame it as a knowledge gap, "the missing 1%": "you thought it was collagen, it's actually fibroblasts". [03-01 07:43; 09:47](../lessons/03-01-unique-mechanisms-overview.md)
  - **DO** state the awareness segment in every ideation, evaluation and expansion prompt; without it, outputs drift to product-aware readers or assume knowledge ("peptide eye creams"). [03-02 02:07; 40:16](../lessons/03-02-ump-ideation-with-llms.md); [03-04 57:43–1:02:08](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DO** run ideation and evaluation in several LLMs: "You really need to be LLM agnostic." [03-04 27:33–28:40](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md); [03-03 05:09–13:56](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
  - **DO** keep only mechanisms the product can actually deliver: "do we have this ingredient? ... So I'm going to skip this one"; on a lymphatic idea, "So I'm making that up." [03-04 07:38; 32:50–33:30](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DO** prefer simple, few-leap mechanisms in health/beauty: "I want as few cognitive leaps as possible. I want stuff they kind of know is true, and here's the one thing you were missing." [03-04 20:19–20:50; 30:44](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DON'T** make it so complex the prospect cannot repeat it after hearing it "one or two times". [04-04 51:54–53:44](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md)
  - **DON'T** reject an idea for a bad name ("we could always change the name") or keep one for a cute name; test whether the UMS is tangible. [03-04 03:39](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md); [03-02 38:45–40:16](../lessons/03-02-ump-ideation-with-llms.md)
  - **DON'T** treat the LLM ranking as the decision; it substitutes for experience, not judgment. [03-03 00:00–05:09](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
  - **DON'T** call the cause "the root cause" in health copy: "that's a diagnostic thing ... you're not supposed to." [03-01 18:46](../lessons/03-01-unique-mechanisms-overview.md)
  - **IF** the audience already knows the cause (solution aware, golf slice) **THEN** concede it and put the novelty in why other solutions fail. [03-01 20:14](../lessons/03-01-unique-mechanisms-overview.md)
  - **IF** you have a live offer **THEN** test the top two mechanisms in ads/advertorials first and build the VSL on the winner; **IF** new and unsure **THEN** sleep on it, explain both to a few people, else take the one two of three LLMs ranked first. [03-03 19:34; 48:22–49:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
  - **IF** an offer feels "fatigued" but the mechanism is good **THEN** change hooks and angles, not the mechanism: "if you have a good mechanism, it can last you for a really long time." [04-08 v2](../lessons/04-08-medium-vsls-structures-and-examples.md)
  - **DON'T** ship any study, percentage, physiology claim or "I helped hundreds of people" line from LLM mechanism text; mark `[VERIFY: …]` and substantiate via [ingredient research](../lessons/02-05-ingredient-deep-research.md). (derived; [03-03](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md), [03-04 compliance](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md))
- **See also:** [ump-ideation-and-evaluation](../frameworks/ump-ideation-and-evaluation.md) · [unified-research-document](unified-research-document.md) · [brief-2-0](brief-2-0.md) · [classic-vsl-structure](classic-vsl-structure.md) · [compliance-red-flags](compliance-red-flags.md) · [prompts library](../libraries/prompts.md) · [Evolve: unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md)

## Definition
Course definition (03-01 docx, repeated inside the evaluation prompt) [03-01 01:01–03:22](../lessons/03-01-unique-mechanisms-overview.md):
- "The unique mechanism explains *why* our prospect is struggling or suffering to achieve a goal... And *how* they can overcome that problem."
- "At its core, the unique mechanism is always a two-part logical connection."
- Prospects have tried solutions that "may have not worked at all, worked partially, or worked fully for a period of time (before they stopped working)". The copywriter's job: "educate our prospect about the REAL reason why past solutions didn't bring them permanent results ... They've been missing ONE CRUCIAL PIECE OF INFORMATION".

| Part | Job | Template (derived) | Example |
|---|---|---|---|
| **UMP** (mechanism of the problem) | "get the prospect to understand why they've failed in the past" | "You thought [known cause]; it's actually [missing piece]." + one plain analogy | Miami MD: "it's actually your failing fibroblasts"; fibroblasts are "like your skin's interior designers" [03-01 06:18](../lessons/03-01-unique-mechanisms-overview.md) |
| **UMS** (mechanism of the solution) | "get the prospect to believe that our product will bring them success where other alternatives have failed" | "[Product] [single action verb] [missing piece] so [result]." | "Once you recharge your fibroblasts ... smoother, tighter, and firmer" [03-01 06:18](../lessons/03-01-unique-mechanisms-overview.md) |

Wrap-up rule: "what's the real reason they haven't found a solution yet? What's the real cause of their problem? ... the solution is to address the real cause." [03-01 22:29](../lessons/03-01-unique-mechanisms-overview.md)

## Why it matters
- Every VSL, PDP and most advertorials and ads carry one; mechanisms are "pretty universally applicable" to moving a prospect from A to B. [03-01 22:29](../lessons/03-01-unique-mechanisms-overview.md)
- It answers the main objection the unified doc surfaces: "I tried other products and they didn't work" / "why should I switch?". [02-04 15:36–16:39](../lessons/02-04-unified-research-process.md)
- It is a brief field ("unique mechanism and its nicknames") and the M-stage hand-off document. [01-01 14:49–15:48](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md); [08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md)
- PDPs still need it: "You have to do the selling somewhere"; check that the page carries UMP and UMS. [10-01 05:41–06:46](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)

## How to use (steps)
1. **Set up** the Unique Mechanisms Claude Project: instructions = description text; knowledge = the nine PDFs (definitions with examples, worked UMP/UMS, ideation prompt, VSL structure, swipes). [03-05 00:28–01:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)
2. **Ideate:** product + niche + mechanism primer + "For this exercise, let's specifically focus on people in the market who are [Problem Aware]." + unified research doc (+ ingredient list for formulated products). Run in Gemini (2.5 Pro / Deep Research), Perplexity, ChatGPT, Claude. [03-02 01:04–03:10](../lessons/03-02-ump-ideation-with-llms.md); [03-04 02:01](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
3. **Screen by hand** ("reserve your judgment" until all are read). Drop: wrong-awareness ideas ("too far along in the mental journey"), niche-segment ideas, ideas needing ingredients/features you lack, known-hero ingredients ("not exciting enough"), duplicates. [03-02 04:18–05:55; 31:19–34:11](../lessons/03-02-ump-ideation-with-llms.md); [03-04 15:03](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
4. **Save** keepers into one "potential mechanisms" doc; include your current live mechanism's real page copy for a fair comparison. [03-02 11:04–12:06](../lessons/03-02-ump-ideation-with-llms.md); [03-04 38:37–39:36](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
5. **Evaluate:** the fixed evaluation prompt with the unified doc + shortlist doc as files, last line set to the target awareness level, on 3 LLMs. Treat agreement as signal. If a ranking rests on a minor pain point, ask the LLM to justify it against the research. [03-03 05:09–17:45](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md); [03-04 46:25–52:00](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
6. **Expand the top two** with the expansion prompt ("write the Unique Mechanism section in a format that could be used in a video sales letter"), pasting the awareness profile block. [03-03 19:34–21:06](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)
7. **Critique and rename in the same chat:** fix logic, audience assumptions, names and metaphors; ask for 5+ alternatives, choose, have the model rewrite. [03-04 1:07:06–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
8. **Substantiate:** every physiological claim in UMP/UMS → `[VERIFY: study, dose, population]` via ingredient research; drop what cannot be supported. (derived; [02-05](../lessons/02-05-ingredient-deep-research.md))
9. **Hand off** the "UM doc in expanded copy format" to the brief generator. [08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md)

## Examples
All examples are course content. Structure only; claims not reusable (physiology and efficacy statements are unverified).

| Product (niche) | Format | UMP | UMS | Lesson point | Source |
|---|---|---|---|---|---|
| Miami MD crepey skin | Advertorial → VSL | "not collagen loss" → failing/lazy fibroblasts | "recharge your fibroblasts" | Advertorial gives the gap, not full detail; it sells "the qualified click" | [03-01 04:55–10:50](../lessons/03-01-unique-mechanisms-overview.md) |
| Stefan's Unity eye serum | PDP | Skin layers separate at the dermal-epidermal junction; "hooks disappear" | Penetrate to the DEJ, support the connection | Micro UMP/UMS can sit in a PDP intro | [03-01 10:50–15:32](../lessons/03-01-unique-mechanisms-overview.md) |
| Emma Relief (bloating) | PDP 3-step diagram | Bad bacteria → methane → slowed gut nerves | "stops the production of methane gas at the source" | Add one unknown link to a known cause; "root cause" wording flagged | [03-01 15:32–17:37](../lessons/03-01-unique-mechanisms-overview.md) |
| Performance Golf slice driver | "Caveman" FAQ page | Open face at impact (already known) | "squares the face for you without needing any training" | Solution-aware: novelty is in why other fixes fail | [03-01 17:37–22:29](../lessons/03-01-unique-mechanisms-overview.md) |
| Airbnb arbitrage coaching | Evaluation run | "Asset Gap vs Income Gap" (Claude + ChatGPT #1); "Permission-Based Income Trap" #2 | — | Cross-LLM agreement; then rewrite logic to "you think you have an income problem, but what you really have is an asset problem" | [03-03 13:56–30:13](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| Peptide eye serum (solution aware) | Full run | Shortlist incl. Lipid Barrier Breach, Dermal Disarray, Chronic Dehydration Debt, DEJ Collapse | Expanded and renamed: "Dermal Disarray" → "Collagen Architecture Breakdown"; "Bio-Tensegrity signal" → "Structural Renewal System" | Rename jargon to plain terms for the target reader | [03-04 41:20–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| Blood-sugar brief | Brief generator | — | Claude "even created a unique mechanism that wasn't bad" | LLM can propose a UM inside the brief (see conflict below) | [01-01 15:48–16:51](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) |
| Nooro (medium VSL) | In-feed VSL | Same mechanism "for quite a while now" | — | Good mechanisms last; refresh hooks instead (instructor claim) | [04-08 v2](../lessons/04-08-medium-vsls-structures-and-examples.md) |

Mechanism anecdote: Stefan ran the ideation prompt for a client VSL, got "several really good mechanisms", and the LLMs all picked his own favourite: "great confirmation" (one case; instructor claim). [08-01 02:00–02:29](../lessons/08-01-rmbc-ii-mid-course-recap.md)

## Common mistakes
- **Wrong awareness target:** first Airbnb run with no awareness line drifted to product-aware ideas. [03-02 02:07; 40:16](../lessons/03-02-ump-ideation-with-llms.md)
- **"Give me more like #3" follow-ups:** returned weaker, over-similar ideas; re-run the base prompt with a tighter awareness line instead. [03-02 17:09–20:18](../lessons/03-02-ump-ideation-with-llms.md)
- **Mechanisms the product can't deliver** (chronobiology regulator: "kind of bullshit. We don't have a chronobiology regulator"). [03-04 24:07–25:44](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Ideas that force a different product** ("Capital Multiplier" implies buying a property portfolio). [03-02 13:32](../lessons/03-02-ump-ideation-with-llms.md)
- **Jargon names in customer copy** ("Elastase Cascade Neutralizer": "you'd be like, what the f*** are you talking about"). [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
- **Over-explaining in an advertorial** that only sells the click. [03-01 08:44–09:47](../lessons/03-01-unique-mechanisms-overview.md)
- **Diagnostic wording** ("root cause") in health copy. [03-01 18:46](../lessons/03-01-unique-mechanisms-overview.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | Ideate, evaluate, expand; "popularized back in 2018-19" (instructor claim) | 07:24–09:55 |
| [03-01 UM overview](../lessons/03-01-unique-mechanisms-overview.md) | Definition, four live pages | 00:00–23:58 |
| [03-02 UMP ideation](../lessons/03-02-ump-ideation-with-llms.md) | Ideation prompt, screening | 01:04–44:22 |
| [03-03 Evaluation (Airbnb)](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) | Evaluation prompt, expansion, decision rules | 00:00–49:54 |
| [03-04 Eye serum walkthrough](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) | Full run, renaming | 00:00–1:19:14 |
| [03-05 UM Claude Project](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) | Project setup, nine PDFs | 00:00–01:28 |
| [04-04 Background stories and UMs](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) | Where the UM sits in a VSL; repeatability test | 51:54–53:44 |
| [04-08 Medium VSLs](../lessons/04-08-medium-vsls-structures-and-examples.md) | Mechanism longevity | v2 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | M-stage steps; cross-LLM confirmation anecdote | 02:00–02:29; 05:28–06:47 |
| [10-01 PDPs](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | UMP/UMS check on PDPs | 05:41–06:46 |

## Cross-course notes
- **Evolve Copywriting** [unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md): one job, "inspire hope"; three types to *find* in the product (new, unspoken, renamed); inventory every real component; "[claim] because [mechanism]"; verify against the product doc. **Agrees** with RMBC on: mechanism explains why past solutions failed; plain language; renaming is legitimate.
- **Disagreement: who invents the mechanism.** RMBC has LLMs ideate dozens of problem-side mechanisms from market research, and lets the brief generator invent one ("Claude even created a unique mechanism that wasn't bad" [01-01 15:48–16:51](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)); the UMP is often a named *story about the cause* ("Chronic Dehydration Debt", "Asset Gap vs Income Gap"). Evolve and Start Here ([product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md), [sophistication levers](../../../evolve/start-here/concepts/market-sophistication-levers.md)) say a new mechanism "needs a real product difference" (ingredient, process, delivery form, unadvertised feature) and warn that AI "makes educated guesses". **Agent default:** use RMBC's LLM ideation for *candidates*, but keep a candidate only if (a) the UMS maps to an ingredient, feature or process the product actually has, and (b) every UMP physiology/finance statement can be substantiated; otherwise treat it as Evolve's "new information" angle with sourced facts, or drop it. Mechanisms invented by a model with no product basis are a hard stop.
- **Evolve Start Here** [sophistication levers](../../../evolve/start-here/concepts/market-sophistication-levers.md): a new mechanism is lever 1 for stage-3+ markets; RMBC's UMP side overlaps with Evolve's "new information" lever (why previous mechanisms failed).
- **Tether** [fluency mechanism](../../../../concepts/fluency-mechanism.md) supports RMBC's "few cognitive leaps / repeat it after one or two hearings" rule.

## Related
[rmbc-pipeline](rmbc-pipeline.md) · [product-market-awareness](product-market-awareness.md) · [unified-research-document](unified-research-document.md) · [brief-2-0](brief-2-0.md) · [classic-vsl-structure](classic-vsl-structure.md) · [compliance-red-flags](compliance-red-flags.md) · [ump-ideation-and-evaluation](../frameworks/ump-ideation-and-evaluation.md) · [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md)
