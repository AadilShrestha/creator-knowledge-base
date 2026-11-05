---
title: "Playbook: offer to funnel end to end (research → mechanism → brief → VSL → ads → presell and PDP → checkout → upsells → emails)"
type: playbook
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests cited per stage (Dynh Nguyen 12-02, David O'Connell 12-03, Max Finn 12-04, Ethan Bence 16-01, Patrick Stiles 16-05)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-02-competitor-research-walkthrough-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-03-psychographic-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-02-ump-ideation-with-llms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/11-02-checkouts-walkthrough-part-2.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
tags: [playbook, end-to-end, rmbc-pipeline, research, unique-mechanism, brief, vsl, advertorial, pdp, checkout, upsell, email, funnel]
updated: 2026-11-02
---

# Playbook: offer to funnel end to end
> The full RMBC II run for a new product or offer: three research documents merged into one, a tested unique mechanism, a Brief 2.0, then every funnel asset (VSL, ads, presell, PDP, checkout, upsells, emails) built from that brief in its own Claude Project, each stage gated before the next starts.

## 🤖 Agent use
- **Use when:** "build the funnel for product X", "take this offer from zero to launch", or any task that needs more than one RMBC asset. For a single asset, jump to its stage; never skip the brief.
- **Inputs → outputs:** product, offer, truth sheet, real customer language, unit economics → `unified-research.pdf` → `um-doc.pdf` → `brief-2.0.pdf` → `funnel-spec` → VSL, ad set, advertorial, PDP, checkout spec, upsell scripts, email sequences, each with a claim-audit block.
- **Rules:**
  - **DO** run research → mechanism → brief → copy in order, and "do not start a stage without the previous stage's output" ([08-01 05:28–06:47](../lessons/08-01-rmbc-ii-mid-course-recap.md); [01-01 04:40–06:33](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)).
  - **DO** treat the brief as non-optional: "this is essential, essential for RMBC II" ([08-01 03:25–03:53](../lessons/08-01-rmbc-ii-mid-course-recap.md)).
  - **DO** iterate with every model output: "It's not just a static process… One of the biggest parts of it is the feedback" ([08-01 07:29](../lessons/08-01-rmbc-ii-mid-course-recap.md)).
  - **DO** learn how each page type works before prompting for it ([01-01 10:58–11:29](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)): open the framework page per stage.
  - **DON'T** use one funnel template for every offer; the chain depends on platform, price and awareness ([01-01 20:52–22:56](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)). Stage 9 decides it.
  - **DON'T** pass any model-made person, number, study or scarcity line downstream. Every stage ends with the [claim audit](../rubrics/llm-output-claim-audit.md).
  - **IF** a model stalls or hits limits **THEN** switch tools ("Claude stopped working, so I switched and used Gemini", [08-01 07:58](../lessons/08-01-rmbc-ii-mid-course-recap.md)).
- **See also:** [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [Write a VSL with Claude](write-a-vsl-with-claude.md) · [Launch a cold-traffic funnel](launch-a-cold-traffic-funnel.md) · [Post-purchase and retention](post-purchase-and-retention.md) · [Prompts library](../libraries/prompts.md) · [Rubrics hub](../rubrics/README.md) · Evolve: [launch a new product end to end](../../../evolve/start-here/playbooks/launch-a-new-product-end-to-end.md)

## Required real inputs (ask for anything missing; list gaps, don't guess)
1. **Product facts:** what it is, how it works, label/ingredients and doses, format, use instructions, time to result the brand can support.
2. **Offer:** price points, packages, guarantee terms, subscription or one-time, bonuses, shipping times.
3. **Truth sheet of proof:** real reviews (count, platform, link), real testimonials with permission, real studies (link, population, dose), real spokesperson/founder story and credentials, real press, real inventory/deadline rules.
4. **Real customer language:** reviews, comments, Reddit threads, support emails, call notes.
5. **Market:** niche, geography, any competitor URLs the user already tracks.
6. **Unit economics:** COGS, target or current CPA, AOV, cash available, rebill/LTV data if any ([16-03 03:46–05:42](../lessons/16-03-funnel-economics-with-spg.md)).
7. **Channels and constraints:** planned traffic sources, regulatory category (supplement, skincare, finance, biz-opp), product page URL if one exists.
8. **Swipe files the user owns or has access to** (VSL transcripts, advertorials, PDPs, upsells, email sequences) for the Claude Project knowledge bases. Structure only.

## Stage map
| # | Stage | Framework / concept to follow | Output artifact | Gate |
|---|---|---|---|---|
| 1 | Product-market awareness research | [deep-research-workflow](../frameworks/deep-research-workflow.md) · [product-market-awareness](../concepts/product-market-awareness.md) | `awareness-report` (TAM, % per stage, majority stage) | Run in ≥ 2 LLMs; % are estimates |
| 2 | Competitor research | [deep-research-workflow](../frameworks/deep-research-workflow.md) | `competitor-profiles` + phrase list | Messaging, pricing, love/dislike present |
| 3 | Psychographic research | [deep-research-workflow](../frameworks/deep-research-workflow.md) | `psychographic-summary` with "in their own words" quotes | Quotes treated as leads, not testimonials |
| 4 | Ingredient research (supplements, skincare) | [deep-research-workflow](../frameworks/deep-research-workflow.md) | `ingredient-claims` (per ingredient, study-tied) | Claim audit C3, C4, C7, C8, C17 |
| 5 | Unified research document | [unified-research-document](../concepts/unified-research-document.md) | `unified-research.pdf` (five sections) | Claim audit C2, C3, C9 |
| 6 | Mechanism ideation, evaluation, expansion | [ump-ideation-and-evaluation](../frameworks/ump-ideation-and-evaluation.md) · [unique-mechanism](../concepts/unique-mechanism.md) | `um-doc.pdf` (chosen UMP/UMS in expanded copy format) | 3-LLM ranking + human judgment; claim audit C3, C8, C18 |
| 7 | Brief 2.0 | [brief-generator](../frameworks/brief-generator.md) · [brief-2-0](../concepts/brief-2-0.md) | `brief-2.0.pdf` (25 fields, `[VERIFY]` placeholders) | Claim audit (all) |
| 8 | Hook database | [hook-generation-system](../frameworks/hook-generation-system.md) | `hook-database` doc | Claim audit C3, C5, C10, C12 |
| 9 | Funnel chain and economics | [launch-a-cold-traffic-funnel](launch-a-cold-traffic-funnel.md) stages 1-3 | `funnel-spec` (chain, channels, CPA ceiling) | [Funnel audit](../rubrics/funnel-audit.md) E + S |
| 10 | VSL (if the chain has one) | [write-a-vsl-with-claude](write-a-vsl-with-claude.md) | master script + leads | Claim audit + [VSL review](../rubrics/vsl-review.md) |
| 11 | Ads | [hook-generation-system](../frameworks/hook-generation-system.md) · [paid-traffic-by-platform](../frameworks/paid-traffic-by-platform.md) · [sell-the-click](../concepts/sell-the-click.md) | ad scripts, statics, captions with hook IDs | Claim audit + Tether [ad scorecard](../../../../rubrics/ad-scorecard.md) |
| 12 | Presell (advertorial / jump page) | [advertorial-build](../frameworks/advertorial-build.md) · [congruence](../concepts/congruence.md) | advertorial(s), one per ad pain point if needed | Claim audit + funnel audit J |
| 13 | PDP | [pdp-build](../frameworks/pdp-build.md) | PDP copy with design notes | Claim audit + Tether [landing-page scorecard](../../../../rubrics/landing-page-scorecard.md) |
| 14 | Checkout | [checkout-optimization](../frameworks/checkout-optimization.md) | checkout spec + microcopy | Funnel audit C |
| 15 | Upsells | [post-purchase-and-retention](post-purchase-and-retention.md) | upsell scripts/pages | Claim audit + funnel audit P |
| 16 | Emails | [post-purchase-and-retention](post-purchase-and-retention.md) | abandon, welcome, promo, reorder, winback sequences | Claim audit |
| 17 | Launch, measure, iterate | [cro-testing](../frameworks/cro-testing.md) · [funnel-economics](../concepts/funnel-economics.md) | test log, bottleneck, next test | VSL review Part 2 + funnel audit T |

## Stages in detail

### Stage 1: product-market awareness
- **Inputs:** niche, product, geography, optional details.
- **Prompt (course, verbatim opening, [02-01](../lessons/02-01-product-market-awareness.md); full text in [prompts library](../libraries/prompts.md)):** "I want your help evaluating the level of Market Awareness for a product in the YOUR NICHE space. The specific product is _PRODUCT_ … please give me a FINAL selection for which stage of Product/Market Awareness the majority of individuals within the market fall."
- **Rules:** define product/most aware at category level ([02-01 v2 02:59–03:22](../lessons/02-01-product-market-awareness.md)); read only TAM, % per stage and the verdict ([v2 09:40](../lessons/02-01-product-market-awareness.md)); run in at least two LLMs ([v2 21:18–22:59](../lessons/02-01-product-market-awareness.md)).
- **Decision:** nearly everyone product-aware → static ad + simple lander, no VSL ([02-01 34:02–36:28](../lessons/02-01-product-market-awareness.md)); mostly problem-aware / unaware of the category → mechanism, big idea, long advertorial or VSL ([37:26–38:52](../lessons/02-01-product-market-awareness.md)).
- **Output:** `awareness-report` + chosen segment(s) (default Problem Aware + Solution Aware, [02-04 02:10–03:10](../lessons/02-04-unified-research-process.md)).

### Stage 2: competitor research
- **Prompt (course, verbatim opening, [02-02](../lessons/02-02-competitor-research-walkthrough-and-examples.md)):** "I want your help doing competitor research for a product in the YOUR NICHE space… Specifically, we're looking for D2C brands who primarily sell online through eCommerce or Direct Response sales funnels." Rewrite the competitor-type line for info offers ([02-02 18:10–18:37](../lessons/02-02-competitor-research-walkthrough-and-examples.md)).
- **Add-on when language is thin:** ask for "specific phrases, claims, verbiage used… that we see these competitors repeatedly use" ([02-02 29:34–31:31](../lessons/02-02-competitor-research-walkthrough-and-examples.md)).
- **Output:** per-competitor messaging, pricing, love/dislike ([02-02 13:14–14:21](../lessons/02-02-competitor-research-walkthrough-and-examples.md)). Competitor phrases are for understanding the market; never copy their lines or claims (repo rule 3).

### Stage 3: psychographic research
- **Prompt:** the 22-question psychographic prompt in four blocks (Demographic Insights, Other Existing Solutions, Curiosity, Corruption) with "in their own words" quotes, in ≥ 2 LLMs, then the Claude merge prompt ([02-03 v2 00:00; 35:49](../lessons/02-03-psychographic-research.md)). Full text: [prompts library](../libraries/prompts.md).
- **Output:** one unified psychographic summary. Quotes are paraphrase leads ([02-03 compliance flags](../lessons/02-03-psychographic-research.md)); supplement them with the user's real customer language (input 4).

### Stage 4: ingredient research (only for ingredient products)
- **Prompt rules:** paste the ingredient list, attach the market overview and (if any) the mechanism; restrict to NCBI/journals, prefer human RCTs; ask for mechanism-supporting and pain-point claims with references ([02-05 00:00–01:59](../lessons/02-05-ingredient-deep-research.md)).
- **Gate:** open every source; check dose, population, human vs animal, who published ([02-05 Agent use](../lessons/02-05-ingredient-deep-research.md)). Record survivors on the truth sheet.

### Stage 5: unified research document
- **Prompt (course, verbatim opening, [02-04](../lessons/02-04-unified-research-process.md)):** "I'm working on a marketing campaign in _NICHE_. The product is _PRODUCT_ and we focus on customers in _REGION_… create one unified research brief…" Use it "as is most of the time" ([02-04 01:25](../lessons/02-04-unified-research-process.md)); set the awareness segments; do not ask for TAM.
- **IF** Claude errors on images **THEN** convert sources to plain-text PDFs or run via Poe ([02-04 16:39–24:24](../lessons/02-04-unified-research-process.md)).
- **Output:** `unified-research.pdf`. Gate: claim audit; its promises are LLM-synthesised leads.

### Stage 6: unique mechanism
1. **Ideate** with the one-off UMP prompt plus the unified doc, naming the awareness segment ("For this exercise, let's specifically focus on people in the market who are Problem Aware.", [03-02 02:07](../lessons/03-02-ump-ideation-with-llms.md)); run several tools; keep a "potential mechanisms" doc ([03-02 11:04–12:06](../lessons/03-02-ump-ideation-with-llms.md)). Optional: a mechanism Claude Project ([03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)).
2. **Evaluate** the shortlist with the evaluation prompt in ≥ 3 LLMs; agreement is a signal, not the decision ([03-03 05:09–17:45; 00:00–05:09](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)).
3. **Expand** the top 2 into VSL-style mechanism copy to test feel ([03-03 19:34–21:06](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md); [03-04](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)).
4. **Decide:** existing offer → test both in ads/advertorials, build the VSL on the winner; new offer → sleep on it, explain to people, else take the mechanism two of three LLMs ranked first ([03-03 48:22–49:54](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)).
- **Output:** `um-doc.pdf` in expanded copy format ([08-01](../lessons/08-01-rmbc-ii-mid-course-recap.md)). Gate: claim audit C3, C8, C18; mechanism explainable in one sentence ([04-02 13:04](../lessons/04-02-vsl-fundamentals-classic-structure.md)).

### Stage 7: Brief 2.0
- **Project:** "RMBC II Brief Generator" with "The New Brief" + classic VSL outline as knowledge; web search on ([05-02 00:00–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)).
- **Prompt (course, verbatim, [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md), placeholders ours):**
  ```text
  I want your help generating a new brief for our brand [Brand]'s [Product]. Here is a current product page where you can pull some inputs:
  [URL]
  Additionally, I am attaching a UMP and also some market research that you can pull from when writing the brief.
  I'm also including a document with the ingredients and relevant studies.
  Please go ahead and get started now.
  ```
- **Revise as "director… copy chief… CMO"** by chat: one-time pricing for the VSL, named speaker, expert, bonuses ([05-02 17:46–23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)). Keep field 3 (teaser promises) separate from field 9 (product claims) ([05-01 08:08–11:09](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md)).
- **Output:** `brief-2.0.pdf`. Gate: claim audit; the course's own generated brief contained "Harvard researchers…", "97% of eye creams fail", "45% wrinkle reduction" with no source ([05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)).

### Stage 8: hook database
- **Prompt:** the deep-research hook prompt (course, verbatim pattern, [07-01 C9](../lessons/07-01-long-form-vsl.md)): "I want you to leverage social media signals, blogs, and other websites to come up with as many different hook-driven statements and questions as you can for [offer]. We are targeting people who are mostly [awareness]… I've attached a Unified Research Brief…" Replace the course's example hooks with examples from our niche, written by us.
- **Rules:** ask for fragments, not closed bullets ([04-10 38:26–39:22](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)); run several LLMs and keep the best in one doc ([04-10 32:59](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)).
- **Output:** `hook-database` with hook IDs.

### Stage 9: funnel chain and economics
Run [launch-a-cold-traffic-funnel](launch-a-cold-traffic-funnel.md) stages 1-3: 15-factor matrix → chain; unit economics → CPA ceiling; channel choice. Output `funnel-spec`. Build only the assets the chain needs.

### Stage 10: VSL
Run [write-a-vsl-with-claude](write-a-vsl-with-claude.md).

### Stage 11: ads
- Decide per ad: sell the click or sell the solution ([12-01 00:03:22](../lessons/12-01-meta-ads.md)); show the product → send to a product page, not a blind VSL ([12-01 00:39:15](../lessons/12-01-meta-ads.md)).
- Mini-VSL ads: 3-7 / short projects ([07-03](../lessons/07-03-3-7-minute-vsl.md), [07-04](../lessons/07-04-short-vsl.md)); feed the hook project only the first half of the VSL when the ad must not pitch the product ([04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)).
- UGC-style scripts: repo skill [write-ugc-script](../../../../../../.claude/skills/write-ugc-script/SKILL.md).
- Track script, lead and hook IDs ([04-10 57:38](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)).

### Stage 12: presell
- **Project:** advertorial Claude Project with varied-niche short/medium/long examples ([09-02 03:00–04:35; 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)).
- **Prompts (course, verbatim, [09-02](../lessons/09-02-claude-project-for-advertorials.md)):** "Here is a [Document Type] for a [Product Type]. Please analyze it, and then I want you to give me 10 potential hooks for advertorials we could write." → "Okay nice, let's go ahead and do #__ first. Can you write out an outline for a ____ length advertorial with that angle? One note is that I don't want to reveal the price, but rather say that readers can save XX%." → "perfect, let's go ahead and write this advertorial now. If you run out of space in a single output and need to do it over multiple outputs that's fine, just let me know and I'll prompt you to continue."
- **Rules:** paste the winning ad's copy for congruence ([09-02 26:24](../lessons/09-02-claude-project-for-advertorials.md)); length follows what the ad revealed ([09-01 36:42–38:00](../lessons/09-01-advertorials-overview-and-examples.md)); label it as an advertorial.
- **Gate:** claim audit (C11 is the usual fail here: [09-02 53:09](../lessons/09-02-claude-project-for-advertorials.md)).

### Stage 13: PDP
- Decide the PDP's job (heavy selling vs branded push) and length from the traffic in front of it ([10-01 00:36–07:44](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)).
- **Prompts (course, verbatim, [10-01](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)):** extract a structure outline from a reference PDP; then "Now, if we were going to test a new PDP for [product], following this structure, what would it look like? Can you go ahead and write the copy for it and indicate all the other design and structural elements? I've attached a brief that should give you all of the information on the [product] you need." If it starts coding: "I don't need you to code or do HTML…"
- **Gate:** claim audit + Tether landing-page scorecard.

### Stage 14: checkout
- Build the checkout spec in [checkout-optimization](../frameworks/checkout-optimization.md): reassurance stack, "one-time purchase · no subscription · no hidden fees" if true, button copy, mobile pass, bump only after an on/off test ([11-02 16:31–19:32](../lessons/11-02-checkouts-walkthrough-part-2.md)).
- **Gate:** funnel audit section C.

### Stages 15-16: upsells and emails
Run [post-purchase-and-retention](post-purchase-and-retention.md).

### Stage 17: launch and iterate
- Fill the economics sheet daily; diagnose in order: step conversion → ad metrics → AOV ([13-01 48:59–53:03](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)).
- VSL: [VSL review Part 2](../rubrics/vsl-review.md). Pages: [CRO testing](../frameworks/cro-testing.md), inside out, EPS metric.

## Artifact hand-off contract
| Artifact | Must contain before the next stage starts |
|---|---|
| `unified-research.pdf` | Demographic and psychographic overviews for the chosen segments, pain points, failed solutions, objections, language; no TAM section |
| `um-doc.pdf` | UMP (real cause) + UMS (macro and micro), nickname, one-sentence version, proof elements each marked SOURCED or `[VERIFY]` |
| `brief-2.0.pdf` | All 25 fields; field 9 claims tied to the truth sheet; every missing fact as `[VERIFY: …]` |
| `funnel-spec` | Matrix score + band + chain, channels, CPA ceiling, break-even CPA |
| Each asset | Claim-audit block at the top; open `[VERIFY]` list |

## Cross-course notes
- **Evolve Start Here** runs Study → Research → Create → Test → Feedback with high creative volume into one Meta CBO ([launch a new product end to end](../../../evolve/start-here/playbooks/launch-a-new-product-end-to-end.md)). RMBC front-loads research, a mechanism and a brief and builds longer pre-sell assets. **Agent default:** use RMBC's research → mechanism → brief for any offer; let the 13-01 matrix decide whether the chain needs RMBC's long assets (low score) or Evolve's PDP + creative-volume model (high score).
- **Mechanism origin:** RMBC generates and ranks mechanisms with LLMs ([03-02](../lessons/03-02-ump-ideation-with-llms.md), [03-03](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md)); Evolve frames the mechanism as something "new" found in product/research ([Evolve unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md)). Default: the mechanism must be true of the product; LLM ideation only proposes names and framings for real product facts. Detail in [unique-mechanism](../concepts/unique-mechanism.md).

## Related
- [Playbooks hub](README.md) · [Rubrics hub](../rubrics/README.md) · [Templates library](../libraries/templates.md) · [Rules library](../libraries/rules.md)
