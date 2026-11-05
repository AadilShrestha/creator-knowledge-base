---
title: "Composite vs swipe"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-08-medium-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-09-short-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-02-foundational-knowledge-and-the-state-of-dtc-marketing-in-202.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
tags: [rmbc-ii, swipe, composite, structure, claude-projects, originality, compliance]
updated: 2026-11-02
---

# Composite vs swipe
> A "lazy swipe" tells an LLM to rewrite one winning letter for your product, which lands "too close for comfort" and drags in the original's claims; a composite loads many varied examples and asks the model to analyze their structures, synthesize, and write new copy from your brief. RMBC II's default is the composite: transfer structure and syntax, never topic, lines or proof.

## 🤖 Agent use
- **Use when:** choosing how to use a winning competitor VSL, advertorial, PDP, short ad or upsell as a model; loading a Claude Project's knowledge; a client asks to "just swipe [brand]".
- **Inputs → outputs:** 1 or more reference assets + our brief → decision (composite / structure-extraction / own-asset swipe) → a structure outline with `[slots]` → new copy built only from our brief's facts.
- **Rules:**
  - **DO** default to the composite: "analyze the various structures, synthesize that knowledge, and use that same knowledge along with your judgment to produce new long-form VSLs" ("one of the really key phrases"). [06-01 08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **DO** for a new brand, use the composite rather than a close model of one winner. [07-01 v1 12:28–14:49; 25:54](../lessons/07-01-long-form-vsl.md)
  - **DO** load varied niches; "the content is not as important as the structure or like the syntax". Don't fill the knowledge base with your own niche. [09-02 05:52–06:23; 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** extract structure, not copy: "you're just taking the structure ... you're trying to get the outline of the structure", and give Claude the real brief so the output isn't "such a swipe that you're like, oh God, this is dumb". [10-01 53:12](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **DO** generalise extracted outlines: ask the model to make the outline broader "so it would apply to many" offers. [04-09 v2 33:58–36:53](../lessons/04-09-short-vsls-structures-and-examples.md)
  - **DON'T** swipe one asset blind: "if you just swipe one ... I really thought that video wasn't very good ... so you want to see the different hooks and then go back to the root." [04-02 07:00](../lessons/04-02-vsl-fundamentals-classic-structure.md)
  - **DON'T** swipe across placements: a long Gundry in-feed VSL swiped for an on-page funnel "never works for them"; "you bomb for your client and don't get hired again." [04-11 v2 00:00–01:56](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)
  - **DON'T** carry any line, character, mechanism name, statistic, study, credential or testimonial from a reference into our copy. (Repo rule: copy the mechanism, not the asset.)
  - **IF** the winner is *our own* asset and we want it in a new category **THEN** a close structure swipe is acceptable ("it's my VSL and I want to swipe my VSL"); still rewrite every claim from the new brief. [06-01 09:15](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-01 v1 24:54](../lessons/07-01-long-form-vsl.md)
  - **IF** you are writing for a client or a competitor's asset is the model **THEN** composite only; close swipes are "landmines that you need to dodge". [06-01 09:15–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **IF** reference copy is aggressive (ClickBank-style) **THEN** use it for structure only and tell the model "use only the facts in the brief"; an LLM "would just make less aggressive claims, especially if you told it to". [06-01 07:48–08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md)
- **See also:** [claude-project-recipe](claude-project-recipe.md) · [classic-vsl-structure](classic-vsl-structure.md) · [compliance-red-flags](compliance-red-flags.md) · [templates library](../libraries/templates.md) · [Tether: competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md)

## Definition
| | Lazy swipe (old process) | Composite (RMBC II process) |
|---|---|---|
| Input | One winning letter + your brief | Many varied examples in project knowledge + your brief |
| Instruction | "rewrite this winning sales letter with these briefs but basically model and swipe the structure really closely" [06-01 08:49–09:15](../lessons/06-01-claude-vsl-projects-setup-overview.md) | "analyze the structure ... synthesize that knowledge ... along with your judgement, to produce new [VSLs]" [06-01 instructions](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| What transfers | Structure, length, often lines, names, claim patterns | Structure and syntax patterns across many winners |
| Risk | "too close for comfort"; disputes with the original's owner; inherited claims | Lower overlap (instructor-stated risk reduction, not legal advice) |
| When Stefan still uses it | Own VSL into a new category; teaching demos (financial) | Default for new brands and client work |

Composite in Stefan's words: "synthesize the information and essentially create a composite. We avoid a lot of those problems because it's going to take the best, or at least good elements from all of these sales letters ... and then create new stuff." [06-01 09:45–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md)

**Structure over topic:** the advertorial knowledge base should span niches because "the content is not as important as the structure or like the syntax" [09-02 05:52–06:23](../lessons/09-02-claude-project-for-advertorials.md).

## Why it matters
- A one-letter swipe imports the original's mechanism names and claims. In the Mitolyn test, Sonnet 3.7 turned "a bizarre purple peel exploit backed by breakthrough studies from Harvard and Yale ... takes just six seconds" into "a bizarre structural renewal exploit ... six seconds ..." with "the same testimonial count pattern". [07-01 v1 21:45–24:54](../lessons/07-01-long-form-vsl.md)
- Swipes fail when context differs: placement (in-feed vs on-page), journey and economics. [04-11 v2 00:00–01:56](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)
- Direct response does run on modelling: "the simplest way to write effective copy ... is to just model what other successful brands selling similar products or services are already doing" [01-02 26:19–27:20](../lessons/01-02-foundational-knowledge-and-the-state-of-dtc-marketing-in-202.md); "so much of it is swiping or modeling off what already works to get a draft one" [04-08 v3 09:51](../lessons/04-08-medium-vsls-structures-and-examples.md). The composite keeps the benefit (proven structure) without the copy.

## How to use (steps)
1. **Collect 5–20 references** across niches and lengths; save copies (pages get taken down). [09-02 03:00–04:35](../lessons/09-02-claude-project-for-advertorials.md)
2. **Label sections** in each (HOOK, LEAD, UMP, UMS, BUILD-UP, REVEAL, CLOSE) or extract a beat outline per asset; generalise to `[slots]`. [04-09 v2 33:58–36:53](../lessons/04-09-short-vsls-structures-and-examples.md)
3. **Load them as project knowledge** with the composite instruction. [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) → [claude-project-recipe](claude-project-recipe.md)
4. **Give only our brief** as facts; add "Do not reuse any claims, statistics, studies, names or credentials from the knowledge files."
5. **Outline first**; check the outline is ours (our mechanism, our narrator, our proof slots). [07-01 v1 28:33](../lessons/07-01-long-form-vsl.md)
6. **If a single model is required** (our own winner): "model the structure, length, everything else of this existing VSL, but for a new market and product" [07-01 v1 13:46](../lessons/07-01-long-form-vsl.md), then rename every lifted term (Stefan: "structural renewal exploit" → "three-step skin unifying system") [07-01 v1 25:54–27:26](../lessons/07-01-long-form-vsl.md).
7. **Overlap check** (derived): compare draft to each reference; any shared distinctive phrase, character, mechanism name or number → rewrite or delete.
8. **Claim audit**: [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md).

## Examples
| Case | Mode | Outcome / lesson | Source |
|---|---|---|---|
| Unity eye serum long VSL: "very closely model the structure and length of the Mitolyn VSL" | Lazy swipe test | Sonnet 4: "super weird ... nonsensical", invented "Sarah, a 47-year-old working mom from Phoenix"; Sonnet 3.7: near line-for-line copy. Verdict: fine only for your own winner; use composite for a new brand | [07-01 v1 12:28–27:26](../lessons/07-01-long-form-vsl.md) |
| Financial "Genetic Royalty" VSL: "Let's really swipe the structure of Secret Trust Fund. Have it be the same length." | Structure swipe (teaching demo) | "a really direct swipe now"; parts "don't make sense" and need rewriting; Stefan: "I know it's not compliant". Structure only; claims not reusable (cures, 5x–10x returns, fictional expert) | [05-05 14:06–16:49](../lessons/05-05-financial-promo-example.md) |
| Four VSL generator projects (8/5/8/12 examples) | Composite | Default C-stage method | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Advertorial project knowledge: short/medium/long, varied niches | Composite | "make the model work harder" | [09-02 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md) |
| PDP structure extraction from winning pages, saved as outlines | Structure extraction | Outline + our brief; "there's not like ... you just have to test stuff" | [10-01 41:18–53:12](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Seven short-VSL structures extracted from real ads | Structure extraction | Templates with slots; don't force ads into templates | [04-09 v2 15:13–36:53](../lessons/04-09-short-vsls-structures-and-examples.md) |
| Upsell project: model "structure, length, style and tone of a named swipe" from 5 PDFs | Named-swipe within a composite set | Draft only; edit every line | [14-03 00:00–00:59](../lessons/14-03-claude-projects-for-upsells.md) |

## Common mistakes
- **One reference, close model, for a new brand.** [07-01 v1 25:54](../lessons/07-01-long-form-vsl.md)
- **Same-niche knowledge base:** produces topic copies. [09-02 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)
- **Swiping across placement** (in-feed → on-page). [04-11](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)
- **Keeping lifted mechanism names or voices** ("avocados for health? No, like, wrong"). [04-11 v2 01:34–01:56](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)
- **Treating a messy brief as the swipe's fault:** the Mitolyn test went "weird" partly because the brief kept calling Laura "founder of Opal Beauty"; fix the brief, then retry. [07-01 v1 20:12](../lessons/07-01-long-form-vsl.md)
- **Hunting the one perfect page to swipe.** [10-01 50:31](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-02 Foundations](../lessons/01-02-foundational-knowledge-and-the-state-of-dtc-marketing-in-202.md) | Model what works | 26:19–27:20 |
| [04-02 VSL fundamentals](../lessons/04-02-vsl-fundamentals-classic-structure.md) | Don't swipe just one | 07:00 |
| [04-08 Medium VSLs](../lessons/04-08-medium-vsls-structures-and-examples.md) | Swiping for draft one | v3 09:51 |
| [04-09 Short VSLs](../lessons/04-09-short-vsls-structures-and-examples.md) | Structure extraction chain | v2 15:13–38:51 |
| [04-11 In-feed vs on-page](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md) | Why swiping Golden Hippo/Gundry fails | v2 00:00–01:56 |
| [05-05 Financial promo](../lessons/05-05-financial-promo-example.md) | Direct structure swipe demo | 14:06–16:49 |
| [06-01 VSL projects](../lessons/06-01-claude-vsl-projects-setup-overview.md) | Composite vs swipe definition | 07:18–10:13 |
| [07-01 Long form](../lessons/07-01-long-form-vsl.md) | Lazy swipe test | v1 12:28–27:26 |
| [09-02 Advertorial project](../lessons/09-02-claude-project-for-advertorials.md) | Structure over topic; varied niches | 05:52–06:23; 12:14–12:46 |
| [10-01 PDPs](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | Extract structure; brief prevents dumb swipes | 41:18–53:12 |
| [14-03 Upsells](../lessons/14-03-claude-projects-for-upsells.md) | Named swipe in project | 00:00–00:59 |

## Cross-course notes
- **Within RMBC (conflict):** 06-01 and 07-01 make the composite the default and limit close swipes to your own assets, while 05-05 demonstrates a direct structure swipe of a third-party winner ("you could do something pretty close to this, tweak it and modify it ... and potentially have yourself a banger" [16:30–16:49]) and 01-02 says to start from a proven structure. **Agent default:** composite always for our brands; single-asset structure swipe only of our own winning asset; never near-verbatim text from any third party.
- **Repo rule / Tether:** "Copy the mechanism, not the asset" ([AGENTS.md](../../../../../../AGENTS.md)); Tether's [competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) and [angle remix](../../../../playbooks/angle-remix.md) playbooks are the short-form version of the same structure-extraction step.
- **Evolve Copywriting** [static ad workflow](../../../evolve/copywriting/frameworks/static-ad-workflow.md) and Evolve Start Here [creator frameworks vs scripts](../../../evolve/start-here/concepts/creator-frameworks-vs-scripts.md) likewise reuse frameworks, not scripts.

## Related
[claude-project-recipe](claude-project-recipe.md) · [classic-vsl-structure](classic-vsl-structure.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [compliance-red-flags](compliance-red-flags.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [advertorial-build](../frameworks/advertorial-build.md) · [pdp-build](../frameworks/pdp-build.md)
