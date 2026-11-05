---
title: "Product-market awareness (RMBC II model)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-01-product-market-awareness.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
tags: [rmbc-ii, market-awareness, product-awareness, schwartz, funnel-length, deep-research, vsl-leads]
updated: 2026-11-02
---

# Product-market awareness (RMBC II model)
> Schwartz's five stages with one RMBC twist: "product aware" and "most aware" mean aware of the *category* (similar products), not your brand. You estimate each stage's share with an LLM deep-research prompt, aim cold traffic at problem/solution aware, and let the size of the gap to product-aware decide how much education (mechanism, advertorial, VSL) the funnel needs.

## 🤖 Agent use
- **Use when:** before any brief, ad, advertorial, VSL or PDP; choosing the awareness level to put in a writing prompt; deciding funnel length; diagnosing ads that make "some sales, no scale".
- **Inputs → outputs:** niche, one-line product, geography, optional demographics → TAM estimate, % of TAM per stage from 2+ LLMs, a "majority stage" verdict → the target stage written into the unified research doc and the brief, the list of beliefs that must be educated, and a funnel-length decision.
- **Rules:**
  - **DO** define product aware / most aware at category level when assessing a DTC market: "it's not that they're aware of our product, it's just that they're aware that this category of product exists". [02-01 v2 02:59–03:22](../lessons/02-01-product-market-awareness.md)
  - **DO** run the awareness prompt in at least two LLMs; trust the combined unaware + problem + solution total more than the individual splits. [02-01 v2 21:18–22:59](../lessons/02-01-product-market-awareness.md)
  - **DO** read only the TAM, the % per stage and the final verdict. "You don't need to read all this." [02-01 v2 09:40, 10:45](../lessons/02-01-product-market-awareness.md)
  - **DO** aim cold-traffic copy at problem-aware and solution-aware people; warm traffic, past buyers and retargeting start higher. [02-01 17:01–19:29; v2 27:49–28:20](../lessons/02-01-product-market-awareness.md)
  - **DO** state the awareness level in every writing prompt (brief, VSL outline, short VSL batch, hook research). [07-04 v2 05:47](../lessons/07-04-short-vsl.md); [07-02 v2 09:03](../lessons/07-02-medium-length-vsl.md)
  - **DO** write different messages per stage; never one message for all. [02-01 41:17–44:00](../lessons/02-01-product-market-awareness.md)
  - **DON'T** write direct-response copy to the unaware unless the market already wants the outcome (money, freedom, biz-opp). Unaware → problem aware "is a whole extra step". [02-01 19:29–20:38](../lessons/02-01-product-market-awareness.md)
  - **DON'T** treat the percentages as measurements. They are LLM estimates; even Stefan's own illustrative eye-serum split (40% unaware) disagrees with the course's saved peptide report (5% unaware). [02-01 v2 05:57–25:11](../lessons/02-01-product-market-awareness.md) (derived)
  - **DON'T** send a blind VSL to people who already saw the product: "A blind VSL is basically never going to talk to product aware or most aware." [12-01 39:15–39:43](../lessons/12-01-meta-ads.md)
  - **IF** most of the market is already product aware (GLP-1) **THEN** use a static ad + simple landing page; sell price, trust, convenience. [02-01 34:02–36:28](../lessons/02-01-product-market-awareness.md); [13-01 03:02–07:24](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)
  - **IF** the market is mostly problem aware or unaware of your category (injectable NAD+, tallow skincare, Airbnb arbitrage) **THEN** budget for education: mechanism, big idea, long advertorial or VSL. [02-01 37:26–38:52](../lessons/02-01-product-market-awareness.md)
  - **IF** an ad makes sales but "hasn't crushed" **THEN** check whether it assumes beliefs the audience does not hold yet. [02-01 25:11–26:58](../lessons/02-01-product-market-awareness.md)
- **See also:** [deep-research-workflow](../frameworks/deep-research-workflow.md) · [unified-research-document](unified-research-document.md) · [sell-the-click](sell-the-click.md) · [ad-to-page-journey](ad-to-page-journey.md) · [funnel-selection-matrix](funnel-selection-matrix.md) · [prompts library](../libraries/prompts.md) · [Evolve: market awareness](../../../evolve/copywriting/concepts/market-awareness.md)

## Definition
The five stages as RMBC teaches them (course infographic; the same definitions sit inside the research prompt) [02-01 01:27–02:49](../lessons/02-01-product-market-awareness.md):

| Stage | Course definition | RMBC reading for DTC |
|---|---|---|
| Unaware | "not even aware of a problem or need that your product or service can solve" | Usually not a direct-response target |
| Problem aware | "recognize they have a problem or need but are unaware of potential solutions" | Prime cold-traffic target |
| Solution aware | "know that solutions exist ... not yet aware of your specific solution" | Prime cold-traffic target |
| Product aware | "know about your solution ... evaluating its features and benefits" | **Category-aware**: knows "similar/nearly identical products and brands" |
| Most aware | "highly aware of your solution ... likely to make a purchase decision soon" | Category-aware and close to buying; mostly retargeting |

**The modification.** Even brands doing $20–30M a year are unknown to "the vast majority of people", so brand-level product awareness is near zero for almost everyone; Stefan reads the top two stages as category awareness and writes this into the prompt. [02-01 02:49–03:48](../lessons/02-01-product-market-awareness.md)

**Overlap.** Stage shares do not sum to 100%: in his eye-serum illustration more women are solution aware (~99%, everyone knows eye creams exist) than problem aware (60%). [02-01 14:34–16:21](../lessons/02-01-product-market-awareness.md)

## Why it matters
- It sets funnel length. Stefan's own telehealth company sold GLP-1 with "a simple static ad" plus landing page, while injectable NAD+ funnels built as if people knew NAD+ failed; paid social would have cost "$1,000, $2,000 to make a sale" and he estimates the research would have saved "$100,000 plus, $150,000 plus" (instructor claims). [02-01 32:40–39:25; v2 13:55](../lessons/02-01-product-market-awareness.md)
- It explains stalled ads: his whipped-tallow ad spoke to product-aware readers in a market that mostly did not know tallow can be used on skin. [02-01 21:14–32:10](../lessons/02-01-product-market-awareness.md)
- It is a cross-format input: "not just for VSLs ... but also all the ads, everything else we're doing". [08-01 01:00–01:31](../lessons/08-01-rmbc-ii-mid-course-recap.md)
- It is factor 1 of the 15-factor funnel matrix. [13-01 03:02–08:21](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md)

## How to use (steps)
1. **Fill the prompt:** niche, product (one line), geography, optional demographics. Verbatim "Prompt #1" is on [02-01 Prompts](../lessons/02-01-product-market-awareness.md) and in the [prompts library](../libraries/prompts.md). [02-01 05:42–08:07](../lessons/02-01-product-market-awareness.md)
2. **Run it** in Gemini deep research and ChatGPT deep research (Perplexity, Grok and o-series also work; model access is "not an excuse"). [02-01 v2 04:21–05:57](../lessons/02-01-product-market-awareness.md)
3. **Extract three things:** TAM, % per stage, majority-stage verdict. If the first run gives no percentages, re-ask (the tallow run needed this). [02-01 v2 22:59–24:33](../lessons/02-01-product-market-awareness.md)
4. **Compare models** on the unaware + problem + solution total (Airbnb arbitrage: ~70% in both). [02-01 v2 21:18–22:59](../lessons/02-01-product-market-awareness.md)
5. **Pick the target stage(s)** and write them into the unified research prompt (default "Problem Aware and Solution Aware"; change per market). [02-04 02:10–03:10](../lessons/02-04-unified-research-process.md)
6. **List the beliefs to educate** to move the target to product aware (why this category, why this mechanism). [02-01 26:58; 30:38–32:10](../lessons/02-01-product-market-awareness.md)
7. **Choose the asset with the decision table below**, then confirm with the [funnel-selection-matrix](funnel-selection-matrix.md).
8. **Carry the stage forward** into the brief's audience field ("Problem-aware and solution-aware woman aged 35 to 60" [05-02 04:12](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)) and into every VSL/ad prompt.

### Decision table: awareness → lead, ad, page
| Majority / target stage | What the copy must do | VSL lead | Ad | Page after the ad | Source |
|---|---|---|---|---|---|
| Unaware (only if outcome is already wanted: money, freedom) | Create the problem first; long journey | Story/curiosity lead; webinar or multi-day launch | Curiosity/education | Long VSL or webinar | [02-01 19:29–21:14; 49:13–50:42](../lessons/02-01-product-market-awareness.md); [13-01 factor 1](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) |
| Problem aware | Name the hidden cause, then introduce the mechanism and category; don't lead with the offer | Problem-first; "we don't want to lead out with airbnb arbitrage" | Static or video that sells the click; product hidden | Long advertorial or VSL | [07-02 v2 09:03](../lessons/07-02-medium-length-vsl.md); [07-01 prompt](../lessons/07-01-long-form-vsl.md); [12-01 03:22–07:11](../lessons/12-01-meta-ads.md) |
| Solution aware | Answer "do they really work? aren't they expensive?"; show why other solutions failed (UMP) and why this one works (UMS) | Failed-solutions → mechanism | Comparison or curiosity video; educational reel for high-ticket | Advertorial → PDP, or advertorial → VSL; short registration page for webinars | [02-01 42:22–42:51](../lessons/02-01-product-market-awareness.md); [12-01 40:59–51:50](../lessons/12-01-meta-ads.md); [10-01 05:41–06:46](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Product aware (category) | "Here's why ours is the best ... Other eco-friendly cleaners have this problem. Ours doesn't" | Short; differentiation, proof | Ad that shows the product; results statics | Product page / long PDP | [02-01 42:51–43:24](../lessons/02-01-product-market-awareness.md); [12-01 25:48–27:34; 39:15](../lessons/12-01-meta-ads.md) |
| Most aware | Get out of the way: price, trust, convenience, offer | None needed | Static offer ad | 1–2 page advertorial → short PDP or cart; questionnaire lander (GetThin pattern) | [02-01 32:40–36:28](../lessons/02-01-product-market-awareness.md); [13-01 03:02–08:21](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) |

Showing the product in the ad moves the viewer to "product-aware at least", so the destination must change with it. [12-01 39:15–39:43](../lessons/12-01-meta-ads.md) → [sell-the-click](sell-the-click.md)

Placement also shifts the effective stage: an educational in-feed ad is a "mental warmup", so the on-page VSL behind it can run a full classic lead. [04-11 08:53–09:59](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)

## Examples
| Case | Stage finding | Consequence | Source |
|---|---|---|---|
| Injectable NAD+ (US 18+): ChatGPT o3 Pro unaware 25–30%, problem 50–60%, solution 10–15%, product ~5%, most <1%; Gemini 40–50 / 30–35 / 15–20 / 5–10 / 1–2% | "Very few people are over here" (product/most aware) | Only Google Search gave an acceptable CPA (instructor claim: ~$250–$300); needed VSL/long advertorial | [02-01 v2 06:28–14:54](../lessons/02-01-product-market-awareness.md) |
| GLP-1 telehealth | Nearly everyone has heard of Ozempic | Static ad "save like a hundred bucks off your first month" + landing page (his paraphrase) | [02-01 32:40–36:28](../lessons/02-01-product-market-awareness.md) |
| Whipped beef tallow (Stefan's skincare brand) | Market mostly solution aware; tallow-for-skin niche | First-person product-aware ad sold but "hasn't crushed"; fix = educational advertorial (untested at recording) | [02-01 21:14–32:10](../lessons/02-01-product-market-awareness.md) |
| Airbnb arbitrage coaching | ~70% in unaware+problem+solution; "chasm" between problem and solution aware | VSL prompts say "problem aware more than solution aware ... I don't want it immediately talking about Airbnb Arbitrage" | [02-01 v2 18:42–22:59](../lessons/02-01-product-market-awareness.md); [07-01 prompt](../lessons/07-01-long-form-vsl.md) |
| Eco-cleaning stage ladder | Problem: "what's actually in your household cleaner?" · Solution: "Do they really work? Aren't they expensive?" · Product: "Other eco-friendly cleaners have this problem. Ours doesn't" | Same product, three messages | [02-01 41:49–43:24](../lessons/02-01-product-market-awareness.md) |
| Saved course reports not walked through | Peptide eye serum: TAM 23.66M, majority solution aware; golf driver: majority solution aware | Use fresh research, not the illustrative splits | [02-01 Results](../lessons/02-01-product-market-awareness.md) |

Compliance: GLP-1, NAD+ and the tallow advertorial's dermatologist quotes are course content. Structure only; claims not reusable. Any health claim needs `[VERIFY: substantiation]`; the derm quotes are unverified.

## Common mistakes
- **Product-aware copy to a solution-aware market** (tallow): the ad "assumes these things that turns out aren't true" for most readers. [02-01 31:41–32:10](../lessons/02-01-product-market-awareness.md)
- **Judging the market by yourself:** "You're not the target market. Think about the average person ... at the grocery store, Walmart." [02-01 v2 06:56–07:26](../lessons/02-01-product-market-awareness.md)
- **Reading brand awareness instead of category awareness**, which makes every market look "unaware". [02-01 02:49–03:48](../lessons/02-01-product-market-awareness.md)
- **Leaving the stage out of the prompt:** in the Airbnb lead swap, Claude kept returning off-target hooks until the prompt said "targeted at problem-aware people". [07-01](../lessons/07-01-long-form-vsl.md)
- **Same destination for reveal and blind ads.** [12-01 39:15–39:43](../lessons/12-01-meta-ads.md)
- **Over-trusting one model's split.** Compare at least two. [02-01 v2 21:18](../lessons/02-01-product-market-awareness.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Course overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | Context is king: platform + awareness | 02:05–04:09 |
| [01-02 Foundational knowledge](../lessons/01-02-foundational-knowledge-and-the-state-of-dtc-marketing-in-202.md) | "How aware is the right person of the problem/product?" as a context question | 07:48–10:31; 17:18 |
| [02-01 Product-market awareness](../lessons/02-01-product-market-awareness.md) | Full model, cases, deep-research prompt, saved reports | whole lesson (1:20:01) |
| [02-04 Unified research](../lessons/02-04-unified-research-process.md) | Target-stage line in the merge prompt | 02:10–03:10 |
| [05-02 Brief generator](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Awareness in the brief's audience field | 04:12 |
| [07-01](../lessons/07-01-long-form-vsl.md), [07-02](../lessons/07-02-medium-length-vsl.md), [07-03](../lessons/07-03-3-7-minute-vsl.md), [07-04](../lessons/07-04-short-vsl.md) | Awareness as a VSL/hook prompt parameter | 07-02 v2 08:03–09:36; 07-04 v2 05:47, v4 00:00–00:31 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | Cross-format input | 01:00–01:31 |
| [09-01 Advertorials](../lessons/09-01-advertorials-overview-and-examples.md) | Advertorial must match awareness level | 30:35–32:32 |
| [10-01 PDPs](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | "You have to do the selling somewhere"; selling = educating by stage | 05:41–06:46 |
| [12-01 Meta ads](../lessons/12-01-meta-ads.md) | Ad → awareness → destination map; blind VSL rule | 03:22–55:48 |
| [13-01 Funnel factors](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) | Factor 1 scoring | 03:02–08:21 |

## Cross-course notes
- **Evolve Copywriting** ([market awareness](../../../evolve/copywriting/concepts/market-awareness.md)) says product aware is "biggest it has ever been" and the scale lever, and unaware is "60% or more" and potentially the most scalable. **RMBC** says product/most aware is small when read at category level and unaware is usually not a direct-response target. **Disagreement.** Partly definitional: Evolve's product-aware covers people who tried competitor products; RMBC's research outputs (NAD+, tallow, mastermind) put product aware at ~5–10%. **Agent default:** run the RMBC research prompt for the real market and target whichever stages it shows are largest; for cold traffic start at problem/solution aware; treat unaware as a later scale test, not the launch target.
- **Evolve Start Here** ([market awareness levels](../../../evolve/start-here/concepts/market-awareness-levels.md)) adds the per-level goal/action sheet, the "change what you compare against" rule and an unaware test for AI mislabels. RMBC agrees on level jobs and adds: LLM TAM/% estimates, category-level product awareness, and awareness → funnel length → page type. Use Start Here's unaware test on any RMBC-labelled "unaware" line.
- **Evolve Start Here** [market sophistication](../../../evolve/start-here/concepts/market-sophistication-levers.md) is a separate axis (how many claims the market has seen). RMBC's answer to high sophistication is the [unique mechanism](unique-mechanism.md).
- **Tether** [native advertising](../../../../concepts/native-advertising.md): the advertorial is the education layer RMBC prescribes for problem/solution-aware cold traffic.

## Related
[rmbc-pipeline](rmbc-pipeline.md) · [unified-research-document](unified-research-document.md) · [unique-mechanism](unique-mechanism.md) · [sell-the-click](sell-the-click.md) · [ad-to-page-journey](ad-to-page-journey.md) · [funnel-selection-matrix](funnel-selection-matrix.md) · [classic-vsl-structure](classic-vsl-structure.md) · [vsl-length-bands](vsl-length-bands.md)
