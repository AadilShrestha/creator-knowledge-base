---
title: "Deep research workflow (awareness → competitors → psychographics → unified brief → ingredients)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-02-competitor-research-walkthrough-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-03-psychographic-research.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-05-ingredient-deep-research.md
tags: [rmbc-ii, research, deep-research, market-awareness, competitor-research, psychographics, unified-research-brief, ingredient-research, llm-prompts, framework]
updated: 2026-11-02
---

# Deep research workflow (the "R" of RMBC II)
> Run four LLM deep-research passes (product/market awareness, competitors, psychographics, ingredients), merge the first three into one short unified research brief, and attach that brief, never the raw reports, to every later mechanism, brief and copy prompt.

## 🤖 Agent use
- **Use when:** starting work on a new product or offer; before UMP ideation, the brief generator, a VSL, advertorial, PDP, ad set or email sequence; when existing ads "should work" but trickle sales (awareness mismatch).
- **Inputs → outputs:** niche, one-line product, geography, competitor type, one-sentence demo line, ingredient list (if any), mechanism doc (if any) → (1) awareness report with TAM, % per stage and majority stage; (2) competitor profiles + phrase list; (3) Claude-unified psychographic report (+ optional quote doc); (4) **unified research brief** (4 sections); (5) merged ingredient-claims doc with citations, verified or bracketed.
- **Rules:**
  - **DO** run the stages in order: research → mechanism → brief → copy; each later stage takes the earlier document as an input. [01-01 04:40](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
  - **DO** run each deep-research prompt in at least two LLMs (Gemini + ChatGPT by default) and compare; numbers differ but "you'll still have a general gauge." [02-01 v2 21:18](../lessons/02-01-product-market-awareness.md) · [02-03 v2 35:49](../lessons/02-03-psychographic-research.md)
  - **DO** read only what drives copy: TAM, % per stage, majority stage [02-01 v2 09:40](../lessons/02-01-product-market-awareness.md); core messaging, pricing, customer love/dislike [02-02 13:14](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
  - **DO** define product-aware / most-aware at **category** level, not brand level, for small DTC brands. [02-01 v2 02:59](../lessons/02-01-product-market-awareness.md)
  - **DO** aim cold-traffic copy at problem-aware and solution-aware segments; set that line in the unified prompt and change it per market. [02-01 17:01](../lessons/02-01-product-market-awareness.md) · [02-04 02:10](../lessons/02-04-unified-research-process.md)
  - **DON'T** ask the unified brief for TAM, market size, growth or strategy; "it's good knowledge … as a marketer, but not for direct response copy". **DON'T** add an "anything else relevant" item. [02-04 06:48–07:17](../lessons/02-04-unified-research-process.md)
  - **DON'T** leave the Tesla / undecylenic acid / Ancel Keys examples in the psychographic prompt unexamined: the example steers output (Gemini returned "Ancel Keys" for a skincare brief). [02-03 v2 23:50](../lessons/02-03-psychographic-research.md)
  - **DON'T** trust first-pass prices, revenue, guarantees, stats or "quotes": the three models disagreed on the same brands, and quotes drift between passes. Verify at source. [02-02 LLM disagreement table](../lessons/02-02-competitor-research-walkthrough-and-examples.md) (derived)
  - **IF** Claude errors on uploads ("maximum image count") **THEN** rebuild every source as plain text (Ctrl/Cmd+Shift+V into a new doc, delete works cited, export PDF); **IF** it still fails **THEN** run the same prompt on Poe (Claude Sonnet 4) or retry in an hour or two. [02-04 16:39–24:24](../lessons/02-04-unified-research-process.md)
  - **IF** the product has ingredients **THEN** run the ingredient prompt (Perplexity default) after the mechanism exists, once with and once without the mechanism, and merge. [02-05 06:13](../lessons/02-05-ingredient-deep-research.md)
  - **DON'T** reuse any competitor claim, LLM promise, LLM "quote" or study number as copy. They are research leads. Bracket every one as `[VERIFY: …]` until checked (repo rule; see [Compliance](#compliance)).
- **See also:** [Unified research document](../concepts/unified-research-document.md) · [Product-market awareness](../concepts/product-market-awareness.md) · [UMP ideation and evaluation](ump-ideation-and-evaluation.md) · [Brief generator](brief-generator.md) · [Prompts library](../libraries/prompts.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md)

## What it is
RMBC II replaces hand research with five prompt-driven passes. Three of them (awareness, competitor, psychographic) get stacked and merged by Claude into "one very simplified document that we can use as we go to generate various forms of copy with LLMs" [02-04 00:00](../lessons/02-04-unified-research-process.md). Ingredient research adds study-linked claims for supplements and topicals [02-05 00:00](../lessons/02-05-ingredient-deep-research.md).

Why it matters: the awareness verdict decides the funnel length and the opening of every asset (GLP-1, mostly product-aware → static + simple landing page; injectable NAD+, mostly problem-aware → mechanism-led advertorial or VSL) [02-01 32:10–38:52](../lessons/02-01-product-market-awareness.md). The unified brief is the context file every later Claude Project reads. Stefan: "I honestly would not skip the product market awareness thing unless you really know … the answer" (instructor claim of better results after correcting this) [02-02 56:02](../lessons/02-02-competitor-research-walkthrough-and-examples.md).

## Inputs checklist
- [ ] Niche (e.g. skincare, biz-opp, golf).
- [ ] Product in one line (e.g. "peptide eye serum", "injectable NAD+") [02-01 05:42](../lessons/02-01-product-market-awareness.md).
- [ ] Geography (ChatGPT asks for it first anyway) [02-01 v2 01:34](../lessons/02-01-product-market-awareness.md).
- [ ] Optional market details: age, gender, income, exclusions ("amateur golfers; not for professionals") [02-02 38:08](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
- [ ] Competitor type: D2C brands, or coaching programs/platforms/gurus for info offers [02-02 18:10](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
- [ ] One-sentence demo line: who + problem/outcome (e.g. "U.S. women 40+ who have wrinkles, dark spots, or puffy eye bags") [02-03 v2 00:00](../lessons/02-03-psychographic-research.md).
- [ ] Ingredient list from label or supplier spec (supplements/topicals only) [02-05](../lessons/02-05-ingredient-deep-research.md).
- [ ] Mechanism doc (UMP/UMS) if it exists; otherwise run ingredients without it [02-05 01:59](../lessons/02-05-ingredient-deep-research.md).
- [ ] Access to: Gemini Deep Research, ChatGPT deep research, Perplexity, Claude (Poe as backup). Ultra-tier plans are not required [02-01 v2 04:21](../lessons/02-01-product-market-awareness.md).
- [ ] Real customer language (our reviews, comments, Reddit) to verify LLM quotes against (repo rule; see [AGENTS.md](../../../../../../AGENTS.md)).

## Steps

### Step 1 — Product/market awareness deep research
- **Input:** niche, product, geography, optional details.
- **Output:** report → extract three things only: TAM overview, % of TAM per stage, final majority stage. Save the report for Step 6.
- **Tool/model:** Gemini Deep Research (preferred "for this prompt" because of tables and charts) and ChatGPT deep research; Perplexity, o3/o4-mini also work; Grok "a little worse" [02-01 v2 04:21–05:57](../lessons/02-01-product-market-awareness.md).
- **Prompt** (verbatim, course doc "Prompt #1"; fill `YOUR NICHE`, `_PRODUCT_`, `_GEOGRAPHY_`, optional `_DETAILS_`):
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
  The TAM and percentage requests were added after a first tallow run returned no percentages [02-01 v2 22:59](../lessons/02-01-product-market-awareness.md).
- **Check before moving on:** sum unaware + problem + solution per model; if both models land near the same total, trust the gauge even when splits differ (Airbnb: ~70% in both) [02-01 v2 21:51–22:59](../lessons/02-01-product-market-awareness.md). Write the cold-traffic target stage and the list of beliefs to educate (why this category, why this mechanism) at the top of the research notes [02-01 26:58](../lessons/02-01-product-market-awareness.md).
- Library copy: [prompts library](../libraries/prompts.md) (Research stage).

### Step 2 — Competitor research
- **Input:** niche, product, geography, competitor type, optional details.
- **Output:** per-competitor profile (target demo, acquisition funnels, core messaging, ad/landing examples, recurring hooks/angles/big ideas, pricing, customer love/dislike, revenue) + a list of phrases competitors repeat.
- **Tool/model:** Gemini Deep Research first, export to doc; if it lacks claims, ChatGPT (answer its clarifying questions). After the golf run he would "skip perplexity and go right to ChatGPT" [02-02 36:33; 54:56](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
- **Prompt** (verbatim; fill `YOUR NICHE`, `_PRODUCT_`, `_GEOGRAPHY_`, `_DETAILS_`):
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
  Info-offer swap for the second paragraph (verbatim): "Specifically, we're looking for coaching programs, training platforms, and gurus who primarily sell online through Direct Response sales funnels." [02-02 18:10](../lessons/02-02-competitor-research-walkthrough-and-examples.md)
  Phrase-mining add-on (verbatim, golf version; swap the product sentence):
```text
What are the core promises they make to prospective customers? Value props, language they use when selling their clubs, etc? I'm really looking for specific phrases, claims, verbiage used. Basically, if I were selling new golf club that adds distance and fixes a golfer's slice, I'd be looking for phrases, sentences, fragments that we see these competitors repeatedly use that I can use as well.
```
  Run it as a new deep-research run, not only as chat [02-02 29:34–32:27](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
- **Check before moving on:** claims table, objections list (competitor complaints become our objections [02-02 44:55](../lessons/02-02-competitor-research-walkthrough-and-examples.md)) and price ladder exist; every price/revenue figure is marked to verify on the live site.

### Step 3 — Psychographic deep research (22 questions)
- **Input:** demo line.
- **Output:** 2–3 raw reports saved as PDFs + a separate notes doc of interesting lines, stories, stats [02-03 v2 36:55](../lessons/02-03-psychographic-research.md).
- **Tool/model:** Gemini Deep Research + ChatGPT (best "at pulling quotes"); Perplexity optional (shorter, weak on historical/tribe stories); Grok judged "just not very good" [02-03 v2 27:52–35:49; 47:07](../lessons/02-03-psychographic-research.md).
- **Prompt** (verbatim, "03-1 Psychographic Deep Research Prompts", Prompt #1; replace `DEMO/Market Information`; review or replace the Curiosity/Corruption examples so they don't bias results):
```text
I am writing some sales copy targeted towards DEMO/Market Information. I'd like your help doing psychographic research. What are their struggles and pain points? What are their beliefs?

Below is a series of questions I used in the past, as part of my RMBC Method for copywriting, where the R stands for research. This should be a good framework to use while doing research on the demo. I'd love it if you can even provide 'quotes' from folks in this demo by looking at comments on social media, or in forums, etc. Basically we want to hear what they're saying and what they believe. We want to hear answers in their own words!

Here's the list of questions:

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

Has Someone Tried to Solve the Market's Pain Points Before In A Very Unique Way?

What Was The Result?

Is There A Conspiratorial Story Behind Why Old Solutions Didn't Work?

Are There Any Older Attempts to Solve the Problem (Pre-1960) That Are Unique?

What Happened? Were they successful but forgotten? Or were they a failure? Why?

Examples:

1) Nikola Tesla in the energy space. Big energy didn't want his solutions, he was discredited and shamed. His inventions and discoveries were thrown into the ash heap of history until now.

2) U.S. Army tried to cure foot fungus during WWII, surgeon general was on a desperate race because troops were missing service time. Finally succeeded by using Undecylenic Acid. But today we forget how effective it is.

Corruption:

Is There A Belief That the Market's Pain Point Used To Not Exist, Or Used To Not Be So Bad?

Is There A Belief That It's Been Recently Exacerbated By Outside Forces?

If So, What Are Those Forces And What's The Reason Behind Their Presence?

Examples:

Obesity and diabetes being the result of Dr. Ancil Keyes.

This isolated group of people doesn't struggle from whatever condition/pain point that most of us do. In America we DO suffer from this pain point. The reason why is that we are exposed to these outside forces while this isolated group isn't.
```
  ("Ancil Keyes" is the doc's spelling of Ancel Keys.)
- **Check before moving on:** read or skim each report once when the market is new ("there will always be little insights … that might get missed when you summarize") but don't move slow [02-03 v1 01:05–02:33](../lessons/02-03-psychographic-research.md). Open the footnote for any strange lead (tribe, forgotten remedy, conspiracy) [02-03 v2 18:40](../lessons/02-03-psychographic-research.md).

### Step 4 — Merge psychographic reports in Claude
- **Input:** the 2–3 Step 3 PDFs.
- **Output:** one unified psychographic report: one section per question with an "In Her Own Words" quote block; biz-op version also adds executive summary, strategic synthesis, copy angles and a voice-of-customer lexicon (pain/hope/trust words) [02-03 v2 36:55; v3 03:56](../lessons/02-03-psychographic-research.md).
- **Tool/model:** Claude (Sonnet 4 on screen). Keep the prompt generic; no niche needed [02-03 v3 02:41](../lessons/02-03-psychographic-research.md).
- **Prompt** (verbatim, "03-2 Claude Deep Research Summary Prompt"). Header:
```text
I am writing some sales copy targeted towards a specific demographic.

I've had multiple LLMs generate Deep Research reports for me on this demographic, and I am attaching each of those as a PDF here.

What I would like your help with is to go through these reports and then create one unified report that I can use as a reference.

For greater context, here is the prompt I give to LLMs for deep research.
```
  Then the Step 3 prompt from "I'd like your help doing psychographic research…" through the Corruption examples (the doc says "Tesla" instead of "Nikola Tesla"), then:
```text
========

Please go ahead and create the document now.
```
- **Check before moving on:** every heading present; quotes traceable to a source report; copy the output into a doc.

### Step 5 — (Optional) Descriptive-language follow-up
- **Input:** the same deep-research chat from Step 3.
- **Output:** a separate doc of pain-point quotes and desired-outcome descriptors (e.g. themes "overnight" change, "lost its glow"; descriptors "glowing", "dewy", "plump") [02-03 v2 43:23–47:07](../lessons/02-03-psychographic-research.md).
- **Prompt** (verbatim, eye-serum version; swap the highlighted niche text "aging skin, looking older, wrinkles" and "skin that looks youthful and amazing"):
```text
Thanks. Now please continue deep research and leverage social signals like social media, forums, etc to provide the following:

1. As many quotes as possible from women describing their specific pain points around aging skin, looking older, wrinkles, and so on. I want to hear how they think about the specific pain points here in their own words!

2. As many quotes as possible from women describing the opposite: skin that looks youthful and amazing. What adjectives and other descriptors do they use?
```
- **Check before moving on:** discard "quotes" sourced from brand blogs, caption lists or thesauruses, and off-demo posters (he flagged a 25-year-old) [02-03 v2 45:40](../lessons/02-03-psychographic-research.md) (derived filter).

### Step 6 — Plain-text source prep
- **Input:** awareness report, best competitor report(s), Claude psychographic summary, optional descriptive-language doc.
- **Output:** 3–4 plain-text PDFs, no images, no works-cited.
- **Method:** select all → paste into a new doc with Ctrl+Shift+V (Cmd+Shift+V on Mac) → delete works-cited links → rename → download PDF. Skip a weak report (he dropped the Perplexity competitor report) [02-04 17:13–21:42](../lessons/02-04-unified-research-process.md).
- **Check before moving on:** each file opens as text; no duplicate uploads left in the chat.

### Step 7 — Unified research brief
- **Input:** Step 6 PDFs; niche/product/region (optional; leaving them blank "didn't really matter" [02-04 07:55–08:20](../lessons/02-04-unified-research-process.md)); the segment line (default "Problem Aware and Solution Aware").
- **Output:** the unified research brief, four numbered sections (see [Output contract](#output-contract)).
- **Tool/model:** new Claude chat; fallback Poe.com → Claude-Sonnet-4 (~$20/month); Gemini on the same docs gave a brief that "was just not that good" [02-04 21:42–24:24](../lessons/02-04-unified-research-process.md).
- **Prompt** (verbatim, "04-1 Unified Research Document Prompt Process"; change the highlighted segment line per market; replace the weight-loss example lines with compliant examples from a different niche, keeping the "DIFFERENT PRODUCT in a DIFFERENT NICHE" label):
```text
I'm working on a marketing campaign in _NICHE_. The product is _PRODUCT_ and we focus on customers in _REGION_.

So far I have performed research around Product/Market Awareness Levels, Competitors, and Psychographic Research.

I am going to upload several PDFs that contain this research.

What I want you to do is go through these PDFs in-depth and then create one unified research brief that contains all of the key elements that would be needed in order to successfully implement this campaign. Specifically, this will be a unified document that I will share with you and other LLMs for background information and context as we generate additional copy and marketing assets, most of which will be direct response oriented.

I don't need information on TAM size, or even specific strategies that were included in these deep research reports. Instead what I really need are the following:

1. Target Market Demographic Overview

Focus on people who fall into the Problem Aware and Solution Aware Market segments primarily.

2. Target Market Psychographic Overview

What are their problems and pain points?

[Examples, from a DIFFERENT PRODUCT in a DIFFERENT NICHE]

[... nine weight-loss pain-point example lines in the course doc ...]

What are their hopes and dreams?

(Specifically, what does their ideal future state look like where their problem has been solved. What would that look like? How would they look and feel? When they dream and imagine this future, what else is true about their life at this point?)

How do they view themselves more broadly, what language should we use when speaking to them, and what language should we avoid?

What are the Primary Promises we can make to them, and that they would want to hear, when it comes to solving their pain points?

[Examples, from a DIFFERENT PRODUCT in a DIFFERENT NICHE]

[... nine weight-loss promise example lines in the course doc ...]

3. What will their biggest objections be to our marketing campaigns for our product, and how can we address those?

4. What existing solutions has the market tried already? Why are those existing solutions not adequate enough?
```
  The two example blocks are elided here because the course's weight-loss lines contain unsubstantiated claims (e.g. "Lose up to 71 lbs of fat fast", "fat cell hypothermia"); full text is in [02-04 Prompts](../lessons/02-04-unified-research-process.md). They exist only "to give Claude the format" [02-04 03:10–04:10](../lessons/02-04-unified-research-process.md).
- **Check before moving on:** four sections present; no TAM/strategy content; the "existing solutions" section names why each fails (the copy will dismiss them via the mechanism [02-04 15:36](../lessons/02-04-unified-research-process.md)).

### Step 8 — Critical edit of the unified brief
- **Input:** Step 7 output + product facts.
- **Output:** edited brief saved as the campaign's single research doc.
- **Method:** LLMs get you "99 percent of the way there most of the time, 95 percent … for sure" [02-04 14:03](../lessons/02-04-unified-research-process.md). Override the avoid-list when it contradicts the product (an instant eye lift can speak to instant results) and replace generic timelines with your own real result [02-04 14:33](../lessons/02-04-unified-research-process.md). Bracket every promise as `[VERIFY: …]` until proof exists (repo rule).
- **Check before moving on:** run [LLM output claim audit](../rubrics/llm-output-claim-audit.md) on the promises section.

### Step 9 — Ingredient deep research (supplements, topicals)
- **Input:** ingredient list; market overview with pain points (awareness/unified doc); mechanism doc if it exists.
- **Output:** per-ingredient claim list tied to named studies, split into (1) mechanism-supporting and (2) pain-point claims.
- **Tool/model:** Perplexity (Research mode) by default ("I actually perplexied the most for the ingredient research"; fast, "really digestible little chunks"); ChatGPT when claims must tie back to the mechanism (attach unified research + mechanism PDF) [02-05 02:32–06:13](../lessons/02-05-ingredient-deep-research.md).
- **Prompt** (verbatim, "05-2 Ingredient Deep Research Prompt", Prompt V1; source typos kept; replace the ingredient list and "eye serum"):
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
  **V2 (no mechanism):** not a separate file; "basically the same prompt" without the mechanism attachment, claim type 1 not applicable [02-05 01:59](../lessons/02-05-ingredient-deep-research.md).
- **Check before moving on:** run it both with and without mechanism context; the with-mechanism run dropped a headline stat (32% wrinkle reduction) the other runs had [02-05 06:13–07:19](../lessons/02-05-ingredient-deep-research.md).

### Step 10 — Merge and verify ingredient claims
- **Input:** all Step 9 outputs.
- **Output:** one combined ingredient doc (PDF for Claude), organized by ingredient, each claim marked verified or `[VERIFY: study, population, dose]`.
- **Merge header** (verbatim, top of "Combined Ingredient Research_Unity Eye Serum"):
```text
Note for Claude or other LLMs:

This is research on ingredients from two LLMs. As a result, you may see the same study data point twice.
```
  Then a "Perplexity" section followed by a "ChatGPT" section [02-05 Prompts](../lessons/02-05-ingredient-deep-research.md).
- **Check before moving on:** open each cited source; check human vs animal/cell data, dose, product match, journal vs supplier/blog page. The Perplexity example still cited brand and supplier pages despite the NCBI rule [02-05 02:32; 04:43](../lessons/02-05-ingredient-deep-research.md). The lesson's own PDF lists "Verify key claims" as a best practice [02-05 Steps](../lessons/02-05-ingredient-deep-research.md).

### Step 11 — Hand off
- Attach the edited unified brief (not the raw reports) to every later prompt [02-04 00:29; 27:20](../lessons/02-04-unified-research-process.md).
- Mechanism work: [UMP ideation and evaluation](ump-ideation-and-evaluation.md) (the expansion prompt reuses the awareness block from the unified doc).
- Brief: [Brief generator](brief-generator.md) takes product page URL + unified research doc + ingredient research + UMP/UMS [01-01 13:54–14:49](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md).

## Decision points
| IF | THEN | Source |
|---|---|---|
| Most of the market is product-aware at category level (e.g. GLP-1 meds) | Static ad + simple landing page; no VSL needed | [02-01 34:02–36:28](../lessons/02-01-product-market-awareness.md) |
| Most of the market is problem-aware / unaware of the category (e.g. injectable NAD+) | Plan mechanism + big idea + long advertorial or VSL; budget for education | [02-01 37:26–38:52](../lessons/02-01-product-market-awareness.md) |
| Market is mostly unaware | Don't write DR copy to them unless they already want the outcome (biz-opp, money, freedom) | [02-01 19:29–20:38](../lessons/02-01-product-market-awareness.md) |
| Awareness profile differs from the default | Change the unified prompt's segment line (GLP-1: solution-aware; biz-opp: problem-aware, even unaware) | [02-04 02:10–03:10](../lessons/02-04-unified-research-process.md) |
| Offer is info/coaching, not a physical product | Swap the competitor-type line to "coaching programs, training platforms, and gurus" | [02-02 18:10](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| Competitor report has no repeated phrases/claims | Run the phrase-mining add-on as a new deep-research run | [02-02 29:34–32:27](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| One LLM gives thin output | Run the same prompt in another LLM ("usually I just go try a different LLM") | [02-02 33:04](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| One LLM is weak on a psychographic section | Use the other LLM's section for it | [02-03 v2 32:23](../lessons/02-03-psychographic-research.md) |
| Not enough customer language | Run the Step 5 follow-up in the same chat; then cross-check against real reviews | [02-03 v2 42:40](../lessons/02-03-psychographic-research.md) |
| You are modelling a proven VSL/PDP/advertorial | Much research can be shortcut, but do it "in a perfect world"; agent default: still run Step 1 | [02-04 04:10–05:11](../lessons/02-04-unified-research-process.md) · [02-02 56:02](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| Generated avoid-list conflicts with the real product (e.g. instant effect) | Override it with the product's real behaviour | [02-04 14:33](../lessons/02-04-unified-research-process.md) |
| Product has ingredients and no mechanism yet | Run ingredient prompt V2 (no mechanism) now; rerun V1 after mechanism | [02-05 01:59](../lessons/02-05-ingredient-deep-research.md) |
| Claims must tie to the mechanism | Use ChatGPT with unified research + mechanism attached | [02-05 04:43–06:13](../lessons/02-05-ingredient-deep-research.md) |
| Product has no ingredients (biz-opp, coaching, hardware) | Skip Steps 9–10 | [01-01 07:24](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) (derived) |

## Failure modes and fixes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Awareness report has no percentages | Prompt lacked TAM/percentage asks | Use the current prompt with the three "Additionally" items | [02-01 v2 22:59](../lessons/02-01-product-market-awareness.md) |
| Models give different stage splits | LLM estimates, not measurements | Compare unaware+problem+solution totals; treat as a gauge | [02-01 v2 21:18–22:59](../lessons/02-01-product-market-awareness.md) |
| Product-aware copy runs to a solution-aware market; ads trickle | Awareness mismatch (Opal whipped-tallow ad) | Re-run Step 1; educate via advertorial/mechanism | [02-01 21:14–32:10](../lessons/02-01-product-market-awareness.md) |
| Prices, revenue, guarantees differ by model for the same brand | Hallucination / stale data | Verify on the live site before use | [02-02 LLM disagreement table](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| Psychographic output names Ancel Keys for a skincare market | Prompt examples steer the model | Replace or delete the Curiosity/Corruption examples | [02-03 v2 23:50–26:33](../lessons/02-03-psychographic-research.md) |
| Same quote reworded between reports and summary | LLM paraphrase drift | Treat as paraphrase leads; never as testimonials | [02-03 Compliance flags](../lessons/02-03-psychographic-research.md) |
| "Desired outcome" quotes come from brand blogs/caption lists | Follow-up pulls non-customer sources | Discard; replace with real reviews | [02-03 v2 45:40](../lessons/02-03-psychographic-research.md) |
| Unified brief full of TAM, growth, revenue, strategy | Unnumbered first-version prompt | Numbered items + exclusion sentence; no catch-all item | [02-04 06:48–07:17](../lessons/02-04-unified-research-process.md) |
| Claude: "maximum image count" error | Heavy PDFs with images, or overload/limits | Plain-text PDFs (Step 6); retry in 1–2 h; Poe with Claude-Sonnet-4 | [02-04 16:39–24:24](../lessons/02-04-unified-research-process.md) |
| Ingredient output cites supplier pages, magazines, brand blogs | Model ignores the NCBI-only rule | Open every source; drop or bracket non-journal claims | [02-05 02:32; 04:43](../lessons/02-05-ingredient-deep-research.md) |
| Headline stat missing from one ingredient run | Mechanism context narrows the search | Run with and without mechanism; merge | [02-05 06:13–07:19](../lessons/02-05-ingredient-deep-research.md) |
| Downstream LLM double-counts studies | Two tools' outputs merged | Add the merge header note | [02-05 Prompts](../lessons/02-05-ingredient-deep-research.md) |

## Output contract
The framework is done when these files exist:

| File | Contents | Feeds |
|---|---|---|
| `awareness-report` | TAM overview; % per stage per model; majority stage; chosen cold-traffic stage; beliefs to educate | Step 7; funnel choice ([funnel selection matrix](../concepts/funnel-selection-matrix.md)) |
| `competitor-report` | Per competitor: demo, funnels, core messaging, hooks/angles, price, love/dislike, revenue `[VERIFY]`; repeated-phrase list | Step 7; objections; mechanism differentiation |
| `psychographic-unified` | 22-question sections with quote blocks; optional lexicon and angles | Step 7 |
| `descriptive-language` (optional) | Pain-point and desired-outcome quotes, filtered | Step 7 |
| **`unified-research-brief`** | 1. Demographic overview (core demographics, life stage, role, digital behaviour: problem- vs solution-aware searches, platforms, review reliance) · 2. Psychographic overview (pain points: physical/visual, emotional, practical; hopes and dreams / ideal future; language use / avoid; primary promises `[VERIFY]`) · 3. Objections + how to address · 4. Existing solutions + why inadequate | Every later prompt: UMP, brief, VSL, advertorial, PDP, ads, emails |
| `ingredient-claims` (if applicable) | Merge header; per ingredient: mechanism claims, pain-point claims, citation, verified flag | UMP expansion, brief generator |

Schema of section 1–4 derived from the eye-serum walkthrough [02-04 08:20–16:39](../lessons/02-04-unified-research-process.md). See [Unified research document](../concepts/unified-research-document.md).

## Compliance
- Every course run produced aggressive, unsubstantiated material: eye-serum promises ("Visibly reduced crow's feet … in 4 to 8 weeks", "Clinically proven peptide technology that rebuilds collagen from within"), biz-opp promises ("Escape the paycheck-to-paycheck cycle within 6-12 months"), the in-prompt weight-loss lines, cure-suppression stories (Rife, undecylenic acid), blood-sugar outputs with drug-comparison and disease language ("comparable to metformin", HbA1c), and LLM stats with no verified source [02-04 Compliance flags](../lessons/02-04-unified-research-process.md) · [02-03 Compliance flags](../lessons/02-03-psychographic-research.md) · [02-05 Compliance flags](../lessons/02-05-ingredient-deep-research.md). **Structure only; claims not reusable.**
- Compliant pattern:
  - Promises → `[VERIFY: claim, evidence source, date]` until our own data or a valid study on our formula supports them.
  - Supplements → structure/function wording ("supports healthy blood sugar levels already within normal range" style), never disease or drug-comparison claims.
  - Animal/cell studies, or an ingredient study at another dose, do not substantiate our finished product.
  - Competitor phrases are a vocabulary of what the market hears; reuse the pattern, never the line or the number.
  - LLM "quotes" are leads. Copy uses only real reviews/comments we can source.
- The Airbnb competitor report recorded advice to hide intended use from landlords; ethical/legal red flag, never echo [02-02 Sources](../lessons/02-02-competitor-research-walkthrough-and-examples.md).
- Full red-flag list: [Compliance red flags](../concepts/compliance-red-flags.md).

## Worked examples
| Run | What happened | Source |
|---|---|---|
| Injectable NAD+ awareness | ChatGPT o3 Pro: problem-aware 50-60% largest; Gemini 2.5 Pro: unaware 40-50%, targetable market late problem / early solution aware; both agree very few are product/most aware (LLM estimates) | [02-01 v2 06:28–13:22](../lessons/02-01-product-market-awareness.md) |
| Airbnb arbitrage awareness | Splits differ; unaware+problem+solution ≈ 70% in both; Gemini flags a "chasm" needing educational marketing | [02-01 v2 18:42–22:59](../lessons/02-01-product-market-awareness.md) |
| Peptide eye serum report (zip) | Majority solution aware (Unaware 5%, Solution 45%), unlike the 40% unaware illustration in the video; use fresh research | [02-01 Results](../lessons/02-01-product-market-awareness.md) |
| Golf driver competitors | Three models disagree on BombTech and Performance Golf prices/revenue; ChatGPT best for phrases | [02-02 37:35–55:32](../lessons/02-02-competitor-research-walkthrough-and-examples.md) |
| Eye serum psychographics | Gemini + Perplexity + ChatGPT → Claude "Unified Psychographic Profile: U.S. Women 40+…" with quote blocks | [02-03 v2 36:55–41:58](../lessons/02-03-psychographic-research.md) |
| Biz-opp psychographics | Claude summary: four drivers (autonomy, fear of a wasted life, skepticism of authority, hope for a secret key); core unmet need "a trusted filter" | [02-03 v3 03:56–12:56](../lessons/02-03-psychographic-research.md) |
| Eye serum unified brief | 4 PDFs → "Unified Research Brief: Peptide Eye Serum Campaign for U.S. Women 40+"; Stefan edits avoid-list and timeline | [02-04 07:17–16:39](../lessons/02-04-unified-research-process.md) |
| Airbnb unified brief | Image-count error → plain-text PDFs → still failing → Poe/Claude-Sonnet-4 works | [02-04 16:39–27:58](../lessons/02-04-unified-research-process.md) |
| Unity eye serum ingredients | Perplexity bullets with 36 footnotes; ChatGPT ties claims to "Structural Renewal"; merged doc with header | [02-05 02:32–07:19](../lessons/02-05-ingredient-deep-research.md) |
| Blood sugar chew ingredients | 10 ingredients × outcome sections, references [1]-[48]; contains disease/drug-comparison claims (not reusable) | [02-05 07:19–08:49](../lessons/02-05-ingredient-deep-research.md) |

## Where it's taught
- [01-01 04:09–07:24](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md): the four research steps plus ingredients; "combine them into one".
- [02-01](../lessons/02-01-product-market-awareness.md): awareness model, prompt, model comparison, funnel sizing [v1 00:00–51:14; v2 00:00–28:46].
- [02-02](../lessons/02-02-competitor-research-walkthrough-and-examples.md): competitor prompt, variants, phrase mining, LLM choice [00:00–57:09].
- [02-03](../lessons/02-03-psychographic-research.md): 22 questions, Claude merge, descriptive-language follow-up [v1–v3].
- [02-04](../lessons/02-04-unified-research-process.md): unified brief prompt, iteration, troubleshooting [00:00–27:58].
- [02-05](../lessons/02-05-ingredient-deep-research.md): ingredient claims prompt, Perplexity vs ChatGPT, merge [00:00–08:49].

## Cross-course notes
- **Evolve Start Here** keeps one hand-filled [research doc](../../../evolve/start-here/concepts/research-doc.md) fed by the [research stack workflow](../../../evolve/start-here/frameworks/research-stack-workflow.md) (onboarding, 14 manual sources, objections, organized insights). RMBC II generates its equivalent with LLM deep research and a Claude merge. Agent default: run RMBC Steps 1–8 for speed, then fill gaps and verify quotes with Evolve's manual sources (Amazon, Reddit, reviews).
- **Awareness:** both courses say copy gets longer as awareness drops ([Evolve market awareness](../../../evolve/copywriting/concepts/market-awareness.md), [Evolve Start Here awareness levels](../../../evolve/start-here/concepts/market-awareness-levels.md)). Difference: Evolve teaches dedicated unaware ads; RMBC treats unaware as "a whole extra step" outside biz-opp [02-01 19:29](../lessons/02-01-product-market-awareness.md). Agent default: pick the target stage with RMBC's TAM split; treat unaware ads as a deliberate test, not the default cold angle.
- **Customer language:** Evolve collects it from real reviews/comments ([labels and customer language](../../../evolve/copywriting/concepts/labels-and-customer-language.md)); RMBC accepts LLM-gathered quotes. Agent default: LLM quotes are leads; only sourced real language goes into copy.
- **Tether Lab:** [customer research stack](../../../../frameworks/customer-research-stack.md) and [customer research to angles](../../../../playbooks/customer-research-to-angles.md) cover review mining; [competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) and [competitor landscape audit](../../../../playbooks/competitor-landscape-audit.md) go deeper on actual ads than RMBC's report-level competitor pass.
- **Mechanism inputs:** [Evolve product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md) is the manual counterpart of Steps 9–10.

## Related
- Concepts: [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Product-market awareness](../concepts/product-market-awareness.md) · [Unified research document](../concepts/unified-research-document.md) · [Unique mechanism](../concepts/unique-mechanism.md) · [Brief 2.0](../concepts/brief-2-0.md) · [Compliance red flags](../concepts/compliance-red-flags.md) · [Funnel selection matrix](../concepts/funnel-selection-matrix.md)
- Frameworks: [UMP ideation and evaluation](ump-ideation-and-evaluation.md) · [Brief generator](brief-generator.md) · [Hook generation system](hook-generation-system.md)
- Playbooks: [Offer to funnel end to end](../playbooks/offer-to-funnel-end-to-end.md)
- Libraries / rubrics: [Prompts](../libraries/prompts.md) · [Rules](../libraries/rules.md) · [Benchmarks](../libraries/benchmarks.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md)
