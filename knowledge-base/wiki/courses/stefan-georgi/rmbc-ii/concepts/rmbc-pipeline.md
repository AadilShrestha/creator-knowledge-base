---
title: "The RMBC pipeline (Research → Mechanism → Brief → Copy)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/13-01-hidden-factors-for-optimal-funnel-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-03-funnel-economics-with-spg.md
tags: [rmbc-ii, pipeline, research, unique-mechanism, brief, vsl, claude-projects, workflow]
updated: 2026-11-02
---

# The RMBC pipeline (Research → Mechanism → Brief → Copy)
> RMBC II is four gated stages, each ending in one named document that the next stage takes as input: Unified Research Document → UM doc in expanded copy format → Expanded Brief 2.0 → finished VSL(s) with multiple leads and hooks; every later asset (ads, advertorials, PDPs, upsells, emails) is generated from the brief or the finished VSL.

## 🤖 Agent use
- **Use when:** starting any new offer; deciding which stage a task belongs to; checking whether you have the input document a stage needs; routing an asset request (VSL, advertorial, PDP, ad, upsell, email) to the right framework.
- **Inputs → outputs:** product/offer facts (+ product page URL if it exists) and a target asset → a stage-by-stage plan that names the artifact each stage must hand over, and the first missing artifact to build now.
- **Rules:**
  - **DO** run the stages in order and never start a stage without the previous stage's document: research doc → mechanism doc → brief → copy. [08-01 05:28–06:47](../lessons/08-01-rmbc-ii-mid-course-recap.md); [01-01 04:40–06:33](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
  - **DO** name artifacts exactly as the course does so humans and agents can find them: "Unified Research Document", "Doc With Your UM in Expanded Copy Format", "Expanded Brief 2.0", "Finished VSL(s) of Varying Lengths & With Multiple Leads and Hooks". [08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DO** treat the brief as non-optional: "this is essential, essential for RMBC II". [08-01 03:25–03:53](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DO** act as copy chief at every stage; the LLM does "the heavy writing" and you are "a copy thinker, not a copywriter". [01-01 11:59–12:56](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
  - **DO** loop back: "It's not just a static process... One of the biggest parts of it is the feedback". [08-01 07:29](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DON'T** pick the funnel format by habit. Score the offer with the 15-factor matrix before deciding VSL vs advertorial vs PDP. [01-01 27:34–28:30](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md); see [funnel-selection-matrix](funnel-selection-matrix.md)
  - **DON'T** carry Claude-made demo people, doctors, studies or credentials from any stage into live copy. Replace with `[VERIFY: …]` and real proof. (derived; repo rule "never invent proof")
  - **IF** the brief has no big idea or hook **THEN** ideate one in the project and add it to the brief before drafting (blood-sugar case). [08-01 07:58–08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **IF** one model stalls or hits a limit **THEN** switch models and continue. [08-01 07:58](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **IF** the product is a supplement **THEN** add the ingredient research step (Perplexity) before the brief; health claims still need substantiation. [01-01 07:24](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
- **See also:** [unified-research-document](unified-research-document.md) · [unique-mechanism](unique-mechanism.md) · [brief-2-0](brief-2-0.md) · [claude-project-recipe](claude-project-recipe.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [offer-to-funnel-end-to-end](../playbooks/offer-to-funnel-end-to-end.md) · [prompts library](../libraries/prompts.md)

## Definition
RMBC = **R**esearch, **M**echanism, **B**rief, **C**opy. In RMBC II each letter is a stage with numbered steps and exactly one output document. The course's own recap doc gives the steps verbatim ([08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md)):

| Stage | Steps (recap doc) | Output artifact (hand-off) | Taught in | Framework page |
|---|---|---|---|---|
| **R** Research | 1 Product/Market Awareness Deep Research · 2 Competitor Deep Research · 3 Psychographic Research · 4 Optional: Ingredient Research | **Unified Research Document** (ingredient research stays a separate doc) | Module 02 | [deep-research-workflow](../frameworks/deep-research-workflow.md) |
| **M** Mechanism | 1 UM Ideation · 2 UM Shortlist · 3 UM Evaluation/Ranking · 4 UM Expansion | **Doc with your UM in expanded copy format** (UMP + UMS) | Module 03 | [ump-ideation-and-evaluation](../frameworks/ump-ideation-and-evaluation.md) |
| **B** Brief 2.0 | 1 Upload unified research doc, UM doc, ingredient research (optional) · 2 Create brief in the Claude Project · 3 Give feedback and modifications | **Expanded Brief 2.0** (the ~25-point brief) | Module 05 | [brief-generator](../frameworks/brief-generator.md) |
| **C** Copy (VSL) | 1 Select length (long, medium, 3–7 min, short) · 2 Upload brief to the matching Claude Project · 3 Request outline · 4 Review/modify/tweak · 5 Create copy · 6 Edit outputs · 7 Create additional leads | **Finished VSL(s) of varying lengths with multiple leads and hooks** | Modules 06–07 | [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) |

Module 04 (VSL structure theory) sits between M and B on purpose: "before we got to the brief and then generating copy, it made sense to put a pretty long core training on sales copy" [01-01 09:55–10:27](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md). Stefan calls it "almost like an intermezzo" [08-01 02:29](../lessons/08-01-rmbc-ii-mid-course-recap.md).

## Why it matters
- Each stage removes a class of failure before writing starts: wrong awareness level (R), "me too" product with no believable reason it works (M), thin context for the LLM (B), and generic one-shot drafts (C, outline-first plus copy-chief editing).
- The brief is the "command center": one document that the LLM uses to write "VSLs, ads, advertorials, email sequences, everything else" [01-01 12:56–13:54](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md). Getting it right once feeds every downstream asset.
- Stefan's quality claim, "better than what 99% of copywriters would write on their own", is conditional on "following these processes closely" [08-01 09:56](../lessons/08-01-rmbc-ii-mid-course-recap.md) (instructor claim, no evidence shown; never repeat it in outputs).

## How to use (steps)
1. **Locate yourself.** List which of the four artifacts already exist for this offer. Start at the first missing one. [08-01 How to apply](../lessons/08-01-rmbc-ii-mid-course-recap.md)
2. **R.** Run the awareness, competitor and psychographic deep-research prompts (two LLMs where the lesson says so), then merge them: "combine them into one" [01-01 06:33–07:24](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md). Supplements: run ingredient research too. → [unified-research-document](unified-research-document.md)
3. **M.** Ideate many UMP/UMS candidates, shortlist, evaluate/rank (across several LLMs), expand the winner into copy format in the UM Claude Project. → [unique-mechanism](unique-mechanism.md)
4. **B.** Upload product page URL (if any) + unified research doc + UM doc + ingredient doc to the brief generator; say "use placeholders" for any missing facts; revise by chat. [01-01 13:54–16:51](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) → [brief-2-0](brief-2-0.md)
5. **Choose the funnel** before choosing the asset: score the offer on the 15 factors [13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) and check unit economics [16-03](../lessons/16-03-funnel-economics-with-spg.md). → [funnel-selection-matrix](funnel-selection-matrix.md), [funnel-economics](funnel-economics.md)
6. **C.** Pick the VSL length band, upload the brief to that length's project, get an outline first, approve, draft, edit as copy chief, then write extra leads and hooks. [08-01 recap doc](../lessons/08-01-rmbc-ii-mid-course-recap.md) → [claude-project-recipe](claude-project-recipe.md), [vsl-length-bands](vsl-length-bands.md), [llm-copy-chief-editing](llm-copy-chief-editing.md)
7. **Feed the downstream projects** (table below). Every one takes the brief, the product URL or a finished VSL as its context document.
8. **Audit** every LLM draft for invented proof before use. → [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md)

### How later modules plug in
| Later asset | Input it takes from the pipeline | Output | Lesson | Framework |
|---|---|---|---|---|
| Hooks / short video ads | Market pain points (from R) + seed hooks + annotated winning-ad transcripts → hook database | 10 concepts, full 1–3 min scripts, tracked by script/lead/hook ID | [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) | [hook-generation-system](../frameworks/hook-generation-system.md) |
| Advertorial | "a landing page, sales page, PDF, VSL script or brief" + real ad copy + audience | 10 advertorial hooks → outline → full advertorial → variants | [09-02](../lessons/09-02-claude-project-for-advertorials.md) | [advertorial-build](../frameworks/advertorial-build.md) |
| PDP | Templatized outline from a winning PDP + "our product brief" or product URL | Full PDP copy with design notes | [10-01](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | [pdp-build](../frameworks/pdp-build.md) |
| Meta / native / Google / TikTok ads | Product, offer, target awareness level, destination page type | Ad → objective → awareness → destination map; captions; test list | [12-01](../lessons/12-01-meta-ads.md) | [paid-traffic-by-platform](../frameworks/paid-traffic-by-platform.md) |
| Funnel structure | Offer, price, traffic temperature, proof assets, regulatory category, device split | 15-row score sheet → funnel band | [13-01](../lessons/13-01-hidden-factors-for-optimal-funnel-structure.md) | [funnel-selection-matrix](funnel-selection-matrix.md) |
| Upsells | Product (link or brief), what the buyer just bought, upsell type, target length | Section-by-section upsell script over several "continue" turns | [14-03](../lessons/14-03-claude-projects-for-upsells.md) | [upsell-flow-build](../frameworks/upsell-flow-build.md) |
| Emails | Sequence type, length, discount ladder/timing, product URL or brief | Outline for approval → copy with 2–3 subject options per email | [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md) | [email-sequences](../frameworks/email-sequences.md) |
| Economics check | CPA, AOV, COGS, CVR, LTV | Gross profit per customer, break-even CPA, ranked levers | [16-03](../lessons/16-03-funnel-economics-with-spg.md) | [funnel-economics](funnel-economics.md) |

## Examples
| Run | What it shows | Source |
|---|---|---|
| Opal Beauty "Unity Eye Serum": product page URL + unified research + ingredient research + UMP/UMS → "Unity Eye Serum VSL Brief" in the "RMBC II Brief Generator" project | Full R→M→B hand-off with a real product page as anchor | [01-01 13:54–15:48](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) |
| Blood-sugar supplement, no website: ingredient research only + "use placeholders for now"; v1 "ClickBank style" mother-of-two story, v2 doctor-told patient story; later "no big idea or hook" → ideated in project → ingredient section "really weak" → expanded | Pipeline as a feedback loop, not a one-way pipe. Structure only; the doctor persona and health claims are Claude placeholders, not reusable | [01-01 15:48–16:51](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md); [08-01 07:58–08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md) |
| Medium VSL project: brief + story direction → outline → feedback → upload of his "classic sales letter outline" → revised outline → "write it" at an 18-minute target | Stage C mechanics | [01-01 18:30–19:44](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) |
| Offers run through C at each length (his recollection, hedged "I think"): long = financial, Unity, blood sugar, Airbnb arbitrage; short = all four | Same brief → several lengths | [08-01 04:27–05:28](../lessons/08-01-rmbc-ii-mid-course-recap.md) |

## Common mistakes
- **Skipping to C.** Asking a VSL project to "write a VSL" with no brief. The projects are built to take the brief as their context doc. [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)
- **Treating it as one-way.** Accepting the first brief or draft. Stefan edits "in real time" inside the project and explains why. [08-01 08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)
- **Using the pipeline without understanding the format.** "The brief is only valuable and the projects for VSLs is only valuable if you really understand how VSLs work." [01-01 10:58–11:29](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) Read [classic-vsl-structure](classic-vsl-structure.md) first.
- **Letting placeholders ship.** Demo briefs contain Claude-made speakers ("Dr. [Expert Name], MD"), testimonials and studies. These are hard stops under repo rules until replaced with verified facts. [01-01 17:00 screenshot note](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
- **Defaulting to a VSL.** "VSL" in RMBC II includes "two-minute VSLs that are really just like Meta ads" [08-01 14:08–14:45](../lessons/08-01-rmbc-ii-mid-course-recap.md); the funnel matrix may say a short PDP is right.

## Where it's taught
| Lesson | What it covers | Timestamps |
|---|---|---|
| [01-01 Welcome and course overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | First statement of R→M→B→C; brief generator and VSL project demos; module map | 04:09–19:44; 27:34–28:30 |
| [01-02 Foundational knowledge](../lessons/01-02-foundational-knowledge-and-the-state-of-dtc-marketing-in-202.md) | "Hell to heaven" pipeline diagram; context is king | (diagram referenced at [01-01 19:44–20:52](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)) |
| [02-04 Unified research process](../lessons/02-04-unified-research-process.md) | R-stage hand-off document | whole lesson |
| [05-01 Old vs new brief](../lessons/05-01-the-old-brief-vs-the-new-brief-overview.md) | B-stage document | whole lesson |
| [06-01 Claude VSL projects setup](../lessons/06-01-claude-vsl-projects-setup-overview.md) | C-stage project recipe | whole lesson |
| [08-01 Mid-course recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | Verbatim stage/step/output list; feedback loop | 05:28–09:26; 14:08 |

## Cross-course notes
- **Evolve Start Here** uses one per-brand [research doc](../../../evolve/start-here/concepts/research-doc.md) (V4.0) filled module by module, then a [product overview and mechanism](../../../evolve/start-here/concepts/product-overview-and-mechanism.md) doc. Same "research before writing" principle; different artifact. RMBC adds: deep-research LLM prompts per research type, a separate mechanism ideation/evaluation stage, and the 25-point brief as the single context file for Claude Projects. **Agent default:** if an Evolve research doc already exists, use it as an extra source for the RMBC unified research merge; do not maintain two parallel research docs.
- **Evolve Copywriting** [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md): AI drafts to "70, 80%", the human "operator" owns the last 20–30%. RMBC agrees on the copy-chief role but is more AI-forward ("pretty much all the writing... is done by AI" [01-01 11:59](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)). **Agent default:** follow RMBC's staged process, but keep Evolve's rule that facts and customer language come from real research, never from the model.
- **Tether Lab** playbooks ([ugc-script-writing](../../../../playbooks/ugc-script-writing.md), [customer-research-to-angles](../../../../playbooks/customer-research-to-angles.md)) cover short-form creative; RMBC adds the long-form path (mechanism → brief → VSL/advertorial/PDP) and the post-purchase assets.

## Related
[product-market-awareness](product-market-awareness.md) · [unified-research-document](unified-research-document.md) · [unique-mechanism](unique-mechanism.md) · [brief-2-0](brief-2-0.md) · [claude-project-recipe](claude-project-recipe.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [vsl-length-bands](vsl-length-bands.md) · [ad-to-page-journey](ad-to-page-journey.md) · [funnel-selection-matrix](funnel-selection-matrix.md) · [offer-to-funnel-end-to-end](../playbooks/offer-to-funnel-end-to-end.md)
