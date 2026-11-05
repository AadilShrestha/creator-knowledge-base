---
title: "RMBC II: shared integration notes"
type: overview
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests per lesson (12-02 to 12-04, 16-01, 16-02, 16-04, 16-05)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/README.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/libraries/rules.md
  - knowledge-base/wiki/courses/evolve/start-here/MERGE-NOTES.md
  - knowledge-base/wiki/courses/evolve/copywriting/MERGE-NOTES.md
tags: [integration, cross-course, shared-pages]
updated: 2026-11-05
---

# RMBC II: shared integration notes
> What to merge into shared cross-creator pages later, which course owns which topic, and where RMBC II conflicts with Evolve and Tether Lab. Routing applied 2026-11-05; see Done.

## Done (2026-11-05)
- Hub linked from the global [index](../../../index.md), [overview](../../../overview.md), the [AGENT-GUIDE](../../../../AGENT-GUIDE.md) task table and the [topic map](../../../topic-map.md).
- Shared [playbooks](../../../playbooks/README.md), [libraries](../../../libraries/README.md) and [rubrics](../../../rubrics/README.md) hubs point at this course's own.
- Cross-course conflicts copied to the global [contradictions](../../../contradictions.md) page with attribution (rows R1–R16).
- Overlapping pages in all four courses link each other under "In other courses".
- **Decision:** the shared pages proposed below were not written as merged copies. The [topic map](../../../topic-map.md) names one owner page per topic instead, so each definition lives in one place.
- People and tools listed in the shared [people](../../../people/README.md) and [tools](../../../tools/README.md) hubs (rows, not separate pages).

## RMBC concepts that should become shared pages
| Proposed shared page | RMBC source | Merge with | Why |
|---|---|---|---|
| `concepts/claude-project-recipe.md` | [Claude Project recipe](concepts/claude-project-recipe.md), [composite vs swipe](concepts/composite-vs-swipe.md), [prompts](libraries/prompts.md) | Copywriting [AI in copywriting](../../evolve/copywriting/concepts/ai-in-copywriting.md), [prompts](../../evolve/copywriting/libraries/prompts.md); Start Here [prompts](../../evolve/start-here/libraries/prompts.md); Tether [prompts](../../../libraries/prompts.md), [Claude tool page](../../../tools/claude-ai.md) | The only full LLM-production method in the KB; every course has prompts, none has the project setup |
| `concepts/llm-copy-chief-editing.md` | [LLM copy-chief editing](concepts/llm-copy-chief-editing.md) | Copywriting [AI in copywriting](../../evolve/copywriting/concepts/ai-in-copywriting.md), [three copy checks](../../evolve/copywriting/concepts/three-copy-checks.md), [copy checklist scorecard](../../evolve/copywriting/rubrics/copy-checklist-scorecard.md); Tether [UGC script checklist](../../../rubrics/ugc-script-checklist.md) | Every agent task ends with editing a model draft; RMBC has the loop, Evolve has the edit vocabulary |
| `concepts/compliance-red-flags.md` + `rubrics/claim-audit.md` | [compliance red flags](concepts/compliance-red-flags.md), [LLM output claim audit](rubrics/llm-output-claim-audit.md), [rules §16](libraries/rules.md) | [AGENTS.md](../../../../../AGENTS.md) rules 2–3; Start Here ⛔ index in [rules](../../evolve/start-here/libraries/rules.md); Copywriting [facts over opinions](../../evolve/copywriting/concepts/facts-over-opinions.md); Tether [validation over authority](../../../concepts/validation-over-authority.md) | The most complete claim-type list in the KB; it should gate every course's output, not just RMBC's |
| `concepts/funnel-economics.md` | [funnel economics](concepts/funnel-economics.md), [benchmarks § funnel economics](libraries/benchmarks.md) | Start Here [KPIs and columns](../../evolve/start-here/frameworks/kpis-and-columns.md) (breakeven ROAS), [KPI thresholds](../../evolve/start-here/libraries/kpi-thresholds.md), [product research screen](../../evolve/start-here/frameworks/product-research-screen.md), [revenue-stage focus](../../evolve/start-here/concepts/revenue-stage-focus.md); Tether [offer and bundle psychology](../../../frameworks/offer-and-bundle-psychology.md) | CPA/AOV/COGS math (RMBC) and ROAS-from-margin targets (Evolve) are the same equation in two units; LTV use conflicts |
| `concepts/congruence.md` | [congruence](concepts/congruence.md), [ad-to-page journey](concepts/ad-to-page-journey.md) | Tether [hero image and copy congruence](../../../concepts/hero-image-copy-congruence.md), [native advertising](../../../concepts/native-advertising.md), [landing page psychology audit](../../../frameworks/landing-page-psychology-audit.md); Start Here [awareness levels](../../evolve/start-here/concepts/market-awareness-levels.md) (page-type matrix); Copywriting [write in the environment](../../evolve/copywriting/concepts/write-in-the-environment.md) | Tether covers visual congruence, RMBC topic and experience congruence across the whole chain |
| `frameworks/funnel-structure.md` | [funnel selection matrix](concepts/funnel-selection-matrix.md), [ad-to-page journey](concepts/ad-to-page-journey.md), [sell the click](concepts/sell-the-click.md) | Start Here [awareness levels](../../evolve/start-here/concepts/market-awareness-levels.md), [campaign structure 3:2:2](../../evolve/start-here/frameworks/campaign-structure-322.md) (3:2:2:2 page tests); Tether [TEEP journey](../../../frameworks/teep-journey.md) | Three different page-choice rules (15 factors, awareness matrix, TEEP stage); no shared page |
| `concepts/unique-mechanism.md` | [unique mechanism](concepts/unique-mechanism.md), [UMP/UMS ideation and evaluation](frameworks/ump-ideation-and-evaluation.md) | Copywriting [unique mechanism](../../evolve/copywriting/concepts/unique-mechanism.md); Start Here [product overview and mechanism](../../evolve/start-here/concepts/product-overview-and-mechanism.md), [sophistication levers](../../evolve/start-here/concepts/market-sophistication-levers.md); Tether [perception management](../../../concepts/perception-management.md) | Three courses define it; RMBC adds the UMP/UMS split and LLM ranking, Evolve the product-difference test |
| `concepts/market-awareness.md` (already proposed in [Copywriting merge notes](../../evolve/copywriting/MERGE-NOTES.md)) | [product-market awareness](concepts/product-market-awareness.md) | Copywriting [market awareness](../../evolve/copywriting/concepts/market-awareness.md); Start Here [awareness levels](../../evolve/start-here/concepts/market-awareness-levels.md); Tether [TEEP journey](../../../frameworks/teep-journey.md) | Add RMBC's category-level "product aware" and the TAM-split research prompt to the planned merge |
| `frameworks/customer-research-stack.md` (extend) | [deep research workflow](frameworks/deep-research-workflow.md), [unified research document](concepts/unified-research-document.md) | Tether [customer research stack](../../../frameworks/customer-research-stack.md); Start Here [research stack workflow](../../evolve/start-here/frameworks/research-stack-workflow.md), [research doc](../../evolve/start-here/concepts/research-doc.md) | Add the LLM deep-research pass as a fast first step whose quotes and stats are leads to verify |
| Shared hooks page (already proposed in [Copywriting merge notes](../../evolve/copywriting/MERGE-NOTES.md)) | [hook generation system](frameworks/hook-generation-system.md), [modular creative and hook swaps](concepts/modular-creative-and-hook-swaps.md) | Copywriting [hooks](../../evolve/copywriting/concepts/hooks.md), [bridges](../../evolve/copywriting/concepts/bridges.md); Tether [iteration vs variation](../../../concepts/iteration-vs-variation.md), [hooks library](../../../libraries/hooks.md) | Add hook / lead / script IDs and the locked-body swap rule; hook density conflicts (below) |
| `frameworks/page-testing.md` | [CRO testing](frameworks/cro-testing.md) | Start Here [campaign structure 3:2:2](../../evolve/start-here/frameworks/campaign-structure-322.md) (page tests), [KPI thresholds](../../evolve/start-here/libraries/kpi-thresholds.md); Tether [creative testing system](../../../frameworks/creative-testing-system.md) | Only RMBC covers on-site split testing; test-method conflict with Evolve (below) |
| `libraries/benchmarks.md` | [benchmarks](libraries/benchmarks.md) | Start Here [KPI thresholds](../../evolve/start-here/libraries/kpi-thresholds.md) | One shared number lookup with source and claim status per row |
| Shared libraries (extend) | [hooks](libraries/hooks.md), [angles](libraries/angles.md), [ad teardowns](libraries/ad-teardowns.md), [rewrites](libraries/rewrites.md), [rules](libraries/rules.md), [prompts](libraries/prompts.md), [templates](libraries/templates.md) | Tether [shared libraries](../../../libraries/README.md); Evolve course libraries | Harvest rows with their claim-risk tags; keep ⛔ rows out of the shared lookups |

Course-only, no merge partner: [VSL length bands](concepts/vsl-length-bands.md), [classic VSL structure](concepts/classic-vsl-structure.md), [Brief 2.0](concepts/brief-2-0.md), [upsell formula](concepts/upsell-formula.md), [email sequences](frameworks/email-sequences.md), [checkout optimization](frameworks/checkout-optimization.md), [webinar funnel](frameworks/webinar-funnel.md). Link them from the shared hubs as they are.

## Who owns what
The owner page holds the definition; the other courses link to it and add only their numbers, settings and examples.

| Topic | Owner | Others add |
|---|---|---|
| Long-form VSLs (structure, leads, length bands, closes) | RMBC II ([classic VSL structure](concepts/classic-vsl-structure.md), [VSL build with Claude](frameworks/vsl-build-with-claude.md)) | — |
| Advertorials / pre-sell pages | RMBC II build ([advertorial build](frameworks/advertorial-build.md)) | Tether: [native advertising](../../../concepts/native-advertising.md) concept (shared page stays the definition) |
| PDP / landing page | Split: RMBC owns the build procedure ([PDP build](frameworks/pdp-build.md)); Tether owns the psychology audit and scorecard ([LP psychology audit](../../../frameworks/landing-page-psychology-audit.md), [LP scorecard](../../../rubrics/landing-page-scorecard.md)) | Start Here: page tests, awareness × page-type matrix |
| Checkout, upsells, email, webinars | RMBC II only | Tether: [offer and bundle psychology](../../../frameworks/offer-and-bundle-psychology.md) for bundles and anchoring |
| Funnel structure and unit economics | RMBC II ([funnel selection matrix](concepts/funnel-selection-matrix.md), [funnel economics](concepts/funnel-economics.md)) | Start Here: breakeven / scaling ROAS from margin, product screen |
| LLM production (Claude Projects, copy-chief loop) | RMBC II ([Claude Project recipe](concepts/claude-project-recipe.md), [LLM copy-chief editing](concepts/llm-copy-chief-editing.md)) | Copywriting: named techniques for feedback turns, 70–80% draft budget |
| Compliance claim types and the claim audit | RMBC II ([compliance red flags](concepts/compliance-red-flags.md), [claim audit](rubrics/llm-output-claim-audit.md)) until a shared page exists | Start Here and Copywriting ⛔ rows; Tether validation over authority |
| Research | Start Here (manual 14-source research doc) | RMBC: LLM deep-research pass and unified merge; Tether: customer research stack |
| Market awareness and unique mechanism definitions | Evolve Copywriting | RMBC: category-level awareness, TAM split, UMP/UMS split, LLM ideation and ranking |
| Short-form ad scripts, UGC, statics | Evolve Copywriting + Tether ([write-ugc-script skill](../../../../../.claude/skills/write-ugc-script/SKILL.md)) | RMBC: hook generation system, hook-swap IDs, short VSL band |
| Platform mechanics: native, Google, TikTok | RMBC II only (guest lessons 12-02 to 12-04) | Tether: native advertising concept |
| Meta account structure, labels, scaling | Start Here | RMBC: 12-01 and 16-02 opinions only |
| Ad testing and iteration | Start Here (testing, scaling) and Copywriting (iteration method) | RMBC: locked-body hook swaps; Tether: one variable per test |
| Page-level CRO testing | RMBC II ([CRO testing](frameworks/cro-testing.md)) | Start Here: 3:2:2:2 page-fit signal |

## Conflicts with Evolve
Agent defaults are taken from the RMBC concept and library pages. Rows are logged in [contradictions](contradictions.md).

| Topic | RMBC II | Evolve | Agent default |
|---|---|---|---|
| Size of "product aware" | Small at category level (~5–10% in the course's research outputs); unaware is usually not a DR target ([product-market awareness](concepts/product-market-awareness.md)) | Product aware is "biggest it has ever been"; unaware "60% or more", potentially the most scalable ([market awareness](../../evolve/copywriting/concepts/market-awareness.md)) | Run the RMBC research prompt on the real market; start cold traffic at problem/solution aware; unaware as a deliberate later test |
| Who invents the mechanism | LLMs ideate cause-and-fix framings; the brief generator may invent one ([unique mechanism](concepts/unique-mechanism.md)) | Mechanism needs a real product difference; AI "makes educated guesses" ([product overview and mechanism](../../evolve/start-here/concepts/product-overview-and-mechanism.md)) | LLMs for candidates only; keep one only if the UMS maps to a real ingredient, feature or process and the UMP can be substantiated |
| Source of customer language | LLM deep-research reports supply quotes ([unified research document](concepts/unified-research-document.md)) | Real reviews, Reddit, calls ([labels and customer language](../../evolve/copywriting/concepts/labels-and-customer-language.md)) | LLM quotes are leads; only sourced real language goes into copy |
| How much of the work AI does | "98%" / "99%" of the work (instructor claim) | Drafts to "70, 80%"; human owns the rest ([AI in copywriting](../../evolve/copywriting/concepts/ai-in-copywriting.md)) | Budget editing as if the draft is 70–80% done |
| Hook density | First 30 seconds "should jump around a good amount" ([hook generation system](frameworks/hook-generation-system.md)) | One sticky hook plus a custom bridge; "Curious NOT confused" ([hooks](../../evolve/copywriting/concepts/hooks.md)) | UGC / product ads: one sticky hook + bridge. In-feed sell-the-click ads to a VSL: stacked hooks as a test variant against a single-hook control |
| Hooks on a fading winner | Add hook swaps at volume ([modular creative](concepts/modular-creative-and-hook-swaps.md)) | Don't spam hook iterations; dissect first ([iteration playbook](../../evolve/copywriting/frameworks/iteration-playbook.md)) | New body: swap hooks at volume. Fading winner: diagnose components, bridge and page first |
| Page choice | By what the ad revealed, unit economics and platform; hold one PDP constant ([ad-to-page journey](concepts/ad-to-page-journey.md)) | By awareness level; test ≥2 pages per batch ([awareness levels](../../evolve/start-here/concepts/market-awareness-levels.md)) | RMBC decides whether a pre-sell is needed and its length; Evolve decides what to split-test; never change ad and page in one test |
| Page-test method | Only a random on-site split is a split test; two ad sets per page "is not a split test" (16-01 guest, [CRO testing](frameworks/cro-testing.md)) | 3:2:2:2: same ads duplicated with a new URL in one ad set ([campaign structure 3:2:2](../../evolve/start-here/frameworks/campaign-structure-322.md)) | On-site URL split for page decisions; 3:2:2:2 as a page-fit signal only |
| LTV in bidding | LTV can justify a negative day-0 CPA (16-03) | Skip LTV tooling under ~$50k/month; blended ROAS ([KPI thresholds](../../evolve/start-here/libraries/kpi-thresholds.md)) | Judge on day-0 gross profit and blended CPA/ROAS; LTV only with our own cohort data and cash runway |
| Meta account structure | Guest: test every campaign type and placement (16-02) | One broad CBO, each concept a 3:2:2 ad set | Evolve 3:2:2; 16-02 is one guest's opinion |
| TikTok test structure | Guest: one ad group per weekly batch, one creative per group (12-04) | 3:2:2 ad sets inside one CBO (Meta) | 3:2:2 on Meta, the guest's batch structure on TikTok |
| Soft metrics | VSL engagement checkpoints and native CTR targets locate leaks | Hook / hold / CTR are diagnostic only; decide on ROAS and CPA | Decide on CPA, ROAS or earnings per session; engagement only to find the leak |
| Brief | Brief 2.0: 25-field long-form offer brief | Short-form creative brief ([video ad script workflow](../../evolve/copywriting/frameworks/video-ad-script-workflow.md)) | Complementary: single UGC ad → Evolve/Tether brief; VSL or multi-asset funnel → Brief 2.0 first |

Aligned: page tests run 7–14 days and at least one business cycle (RMBC 16-01 and Start Here); every claim needs a mechanism behind it (complementary to UMP + UMS).

## Conflicts and overlaps with Tether Lab
| Topic | RMBC II | Tether Lab | Status |
|---|---|---|---|
| Authority | Brief and VSL narrators lean on named experts and doctors (rules BR12), often model-invented | Peer validation beats authority ([validation over authority](../../../concepts/validation-over-authority.md)) | Conflict (derived). Default: real peer validation; an expert only if real, named with consent and verifiable |
| Opening focus | Fragmented, fast-moving first 30 seconds | [One core emotion per ad](../../../concepts/one-core-emotion-per-ad.md) | Conflict (derived). Default: one emotional promise; fragmented opening as a test variant |
| Customer language | LLM-gathered quotes | [Customer research stack](../../../frameworks/customer-research-stack.md): real reviews and surveys | Conflict; Tether's sources win, LLM quotes are leads |
| Hook swaps | Locked body, swapped hooks, tracked by ID | [Iteration vs variation](../../../concepts/iteration-vs-variation.md), [creative testing system](../../../frameworks/creative-testing-system.md): one variable per test | Agree; RMBC adds ID tracking |
| CRO scope | One big lever per funnel step; "don't do a button color test" (16-01) | One variable at a time on a proven winner | Compatible: one variable, chosen big |
| Native and pre-sell | Advertorial length set by what the ad revealed; Claude Project loop | [Native advertising](../../../concepts/native-advertising.md) | Agree; shared concept stays the definition |
| Landing pages | Length by traffic temperature; extract and rebuild a working PDP structure | [LP psychology audit](../../../frameworks/landing-page-psychology-audit.md), [hero image and copy congruence](../../../concepts/hero-image-copy-congruence.md) | Complementary: RMBC builds, Tether audits |
| Competitor assets | Composite by default, but 05-05 demos a close swipe; native guest: no "rip and run one-to-one" | [Competitor ad teardown](../../../playbooks/competitor-ad-teardown.md), [angle remix](../../../playbooks/angle-remix.md) | Agree on copy the mechanism; Tether's remix fidelity check replaces the 05-05 swipe |
| Briefs | Brief 2.0 is the copy brief upstream | [Creator brief](../../../playbooks/creator-brief.md) is the production brief | Complementary: fill the creator brief from verified Brief 2.0 fields |
