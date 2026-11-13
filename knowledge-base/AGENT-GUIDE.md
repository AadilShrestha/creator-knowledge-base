---
title: "AGENT-GUIDE: front door for AI agents"
type: overview
creator: synthesis
course: cross-course
sources:
  - knowledge-base/wiki/index.md
  - knowledge-base/wiki/topic-map.md
  - knowledge-base/wiki/playbooks/README.md
  - knowledge-base/wiki/contradictions.md
  - knowledge-base/wiki/courses/evolve/copywriting/README.md
  - knowledge-base/wiki/courses/evolve/start-here/README.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/README.md
tags: [agent-guide, navigation, pipeline, rules, citations]
updated: 2026-11-05
---

# AGENT-GUIDE: read this first
> This knowledge base is reference material for AI agents that make **performance ad creative** for our own DTC brands: tear down competitor ads that are working, work out which angles and psychology make them work, remix the **mechanism** for our product, and produce our own UGC videos, statics, pages and funnels, then test and iterate. It holds four courses:
> - **Tether Lab** by Sarah Levinger: consumer psychology, *why* ads work.
> - **Evolve Copywriting** by Spencer Pawliw: copy craft and iteration, *how to write and fix* ads.
> - **Evolve Start Here** by Spencer Pawliw and Shaun Eng: research, Meta media buying, testing, scaling and creator programs.
> - **RMBC II** by Stefan Georgi: long-form direct response (VSLs, advertorials, PDPs, checkouts, upsells, email), funnel economics and LLM production with Claude Projects.
> - **Ad Creators Lab** (Epic Ads Lab: Camilo, Hao, Narek and guests): **producing ads with AI**: realistic AI UGC, animated formats (skeleton, crochet, claymation, song, talking objects), AI statics, Claude skills for ad production, editing AI footage, ad roasts.

## Folder map
| Path | What's there |
|---|---|
| [wiki/index.md](wiki/index.md) | Catalogue of every page. Start here for lookups |
| [wiki/topic-map.md](wiki/topic-map.md) | **Which course owns each topic** when several cover it, and the conflict row to apply |
| [wiki/overview.md](wiki/overview.md) | Big picture: what the KB knows and what's missing |
| [wiki/playbooks/](wiki/playbooks/README.md) | **Procedures you execute** (teardown → angles → script → brief → test), plus pointers to each course's playbooks |
| [wiki/rubrics/](wiki/rubrics/README.md) | Quality gates: ad scorecard, UGC checklist, landing-page scorecard, plus course rubrics |
| [wiki/frameworks/](wiki/frameworks/) | Runnable diagnostics the playbooks call (zones, selves, TEEP, stories, testing…) |
| [wiki/libraries/](wiki/libraries/README.md) | Harvested, tagged hooks, angles, rewrites, ad teardowns, rules, prompts, plus each course's own set |
| [wiki/concepts/](wiki/concepts/heuristics.md) | One idea per page; `concepts/heuristics/` = 54 heuristic pages |
| [wiki/brands/](wiki/brands/README.md) | Case files by niche: every real ad/page discussed in Tether Lab |
| [wiki/courses/tether-lab/](wiki/courses/tether-lab/README.md) | Lesson and live-session pages with `[h:mm:ss]` citations |
| [wiki/courses/evolve/copywriting/](wiki/courses/evolve/copywriting/README.md) | Evolve Copywriting: 72 lessons plus its own playbooks, frameworks, concepts, libraries and rubric |
| [wiki/courses/evolve/start-here/](wiki/courses/evolve/start-here/README.md) | Evolve Start Here: 175 lessons plus playbooks, frameworks, concepts, libraries (incl. KPI thresholds) and rubrics |
| [wiki/courses/ad-creators-lab/ai-ads-ugc-animations/](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/README.md) | Ad Creators Lab: 110 lessons plus frameworks, concepts, playbooks, rubrics and libraries (prompts, Claude skills, tool settings) for AI ad production |
| [wiki/courses/stefan-georgi/rmbc-ii/](wiki/courses/stefan-georgi/rmbc-ii/README.md) | RMBC II: 58 lessons plus playbooks, frameworks, concepts, libraries (incl. 130 prompts, benchmarks) and rubrics |
| [wiki/tools/](wiki/tools/README.md), [people/](wiki/people/README.md), [resources/](wiki/resources/books.md) | Tools, people, books and prompt PDFs |
| [wiki/contradictions.md](wiki/contradictions.md) | Where sources disagree, with the default to follow |
| `raw/` | Immutable source transcripts and extractions (evidence; don't edit) |

## How to navigate
1. **Task?** Find it in the table below and open that playbook. Follow its numbered steps and output its template.
2. **Topic covered by more than one course** → [topic map](wiki/topic-map.md): follow the owner page, add detail from the others, apply the conflict row.
3. **Playbook step names a framework** → open it for the scoring tables and decision rules.
4. **Need examples** → [libraries](wiki/libraries/README.md) (hooks, angles, rewrites, teardowns, prompts) and [brands](wiki/brands/README.md) for your niche. Grep the large libraries; don't read them top to bottom.
5. **Need the evidence** → the session/lesson page cited, then `raw/` transcripts.
6. **Lookup by name** → [index](wiki/index.md).

## Task → start here
| Task | Start here | Then |
|---|---|---|
| Research a product, market or customer | [SH: research to first concepts](wiki/courses/evolve/start-here/playbooks/research-to-first-concepts.md) | [customer research stack](wiki/frameworks/customer-research-stack.md), [RMBC: deep research workflow](wiki/courses/stefan-georgi/rmbc-ii/frameworks/deep-research-workflow.md) (LLM quotes are leads only) |
| Find angles from customer research | [customer-research-to-angles](wiki/playbooks/customer-research-to-angles.md) | [mindstate mapping](wiki/frameworks/mindstate-emotion-mapping.md), [SH: angle generation prompt](wiki/courses/evolve/start-here/frameworks/angle-generation-prompt.md) |
| Find or test a unique mechanism | [CW: unique mechanism](wiki/courses/evolve/copywriting/concepts/unique-mechanism.md) | [RMBC: UMP/UMS ideation and evaluation](wiki/courses/stefan-georgi/rmbc-ii/frameworks/ump-ideation-and-evaluation.md) |
| Tear down a competitor ad | [competitor-ad-teardown](wiki/playbooks/competitor-ad-teardown.md) | [ad scorecard](wiki/rubrics/ad-scorecard.md) |
| Map a whole competitor landscape / find white space | [competitor-landscape-audit](wiki/playbooks/competitor-landscape-audit.md) | [emotional stagnation](wiki/concepts/emotional-stagnation.md) |
| Turn competitor mechanisms into our angles | [angle-remix](wiki/playbooks/angle-remix.md) | [angles library](wiki/libraries/angles.md) |
| **Write a UGC or video ad script / hooks** (start here) | [write-ugc-script skill](../.claude/skills/write-ugc-script/SKILL.md): one merged Tether + Evolve process with examples, checklist and claim rules | Deeper: [UGC script writing](wiki/playbooks/ugc-script-writing.md), [CW: write a video ad script](wiki/courses/evolve/copywriting/playbooks/write-a-video-ad-script.md), [RMBC: hook generation system](wiki/courses/stefan-georgi/rmbc-ii/frameworks/hook-generation-system.md) |
| Write or fix a hook / line of copy | [CW hooks concept](wiki/courses/evolve/copywriting/concepts/hooks.md), [three copy checks](wiki/courses/evolve/copywriting/concepts/three-copy-checks.md) | [CW templates](wiki/courses/evolve/copywriting/libraries/templates.md), [CW rewrites](wiki/courses/evolve/copywriting/libraries/rewrites.md) |
| Turn an ad idea into a brief (avatar → angle → mechanism → authority) | [CW: ad idea to brief](wiki/courses/evolve/copywriting/playbooks/ad-idea-to-brief.md) | [mini breakthrough memo](wiki/courses/evolve/copywriting/frameworks/mini-breakthrough-memo-and-growth-guide.md) |
| Brief a creator / production (incl. AI UGC decision) | [creator-brief](wiki/playbooks/creator-brief.md) | [AI UGC tools](wiki/tools/ai-ugc-tools.md), [SH: creator frameworks vs scripts](wiki/courses/evolve/start-here/concepts/creator-frameworks-vs-scripts.md) |
| Make a static | [static-ad-creation](wiki/playbooks/static-ad-creation.md) | [visual weight hierarchy](wiki/frameworks/visual-weight-hierarchy.md), [CW: write static image ads](wiki/courses/evolve/copywriting/playbooks/write-static-image-ads.md), [SH: execution checklist](wiki/courses/evolve/start-here/rubrics/execution-checklist.md) |
| Write a VSL (long, medium, 3–7 min, short) | [RMBC: write a VSL with Claude](wiki/courses/stefan-georgi/rmbc-ii/playbooks/write-a-vsl-with-claude.md) | [Brief 2.0](wiki/courses/stefan-georgi/rmbc-ii/concepts/brief-2-0.md), [VSL review](wiki/courses/stefan-georgi/rmbc-ii/rubrics/vsl-review.md) |
| Write an advertorial / pre-sell page | [RMBC: advertorial build](wiki/courses/stefan-georgi/rmbc-ii/frameworks/advertorial-build.md) | [native advertising](wiki/concepts/native-advertising.md), [landing-page scorecard](wiki/rubrics/landing-page-scorecard.md) |
| Write a PDP / landing page | Skill: [write-landing-page](../.claude/skills/write-landing-page/SKILL.md) · [RMBC: PDP build](wiki/courses/stefan-georgi/rmbc-ii/frameworks/pdp-build.md) | [LP psychology audit](wiki/frameworks/landing-page-psychology-audit.md), [landing-page scorecard](wiki/rubrics/landing-page-scorecard.md) |
| Audit a landing page or advertorial | [landing-page-scorecard](wiki/rubrics/landing-page-scorecard.md) | [LP psychology audit](wiki/frameworks/landing-page-psychology-audit.md), [RMBC: congruence](wiki/courses/stefan-georgi/rmbc-ii/concepts/congruence.md) |
| Spec a checkout, upsells or post-purchase email | [RMBC: post-purchase and retention](wiki/courses/stefan-georgi/rmbc-ii/playbooks/post-purchase-and-retention.md) | [checkout optimization](wiki/courses/stefan-georgi/rmbc-ii/frameworks/checkout-optimization.md), [upsell flow build](wiki/courses/stefan-georgi/rmbc-ii/frameworks/upsell-flow-build.md), [email sequences](wiki/courses/stefan-georgi/rmbc-ii/frameworks/email-sequences.md) |
| Plan a cold-traffic funnel and its unit economics | [RMBC: launch a cold-traffic funnel](wiki/courses/stefan-georgi/rmbc-ii/playbooks/launch-a-cold-traffic-funnel.md) | [funnel selection matrix](wiki/courses/stefan-georgi/rmbc-ii/concepts/funnel-selection-matrix.md), [funnel economics](wiki/courses/stefan-georgi/rmbc-ii/concepts/funnel-economics.md), [funnel audit](wiki/courses/stefan-georgi/rmbc-ii/rubrics/funnel-audit.md) |
| Launch a new product end to end | [SH: launch a new product](wiki/courses/evolve/start-here/playbooks/launch-a-new-product-end-to-end.md) | [RMBC: offer to funnel](wiki/courses/stefan-georgi/rmbc-ii/playbooks/offer-to-funnel-end-to-end.md) |
| Set up a Claude Project / prompt an LLM for copy | [RMBC: Claude Project recipe](wiki/courses/stefan-georgi/rmbc-ii/concepts/claude-project-recipe.md) | [LLM copy-chief editing](wiki/courses/stefan-georgi/rmbc-ii/concepts/llm-copy-chief-editing.md), [RMBC prompts](wiki/courses/stefan-georgi/rmbc-ii/libraries/prompts.md) |
| **Check an LLM draft's claims** (every model-written asset) | [RMBC: LLM output claim audit](wiki/courses/stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | [compliance red flags](wiki/courses/stefan-georgi/rmbc-ii/concepts/compliance-red-flags.md) |
| Run Meta media buying (structure, budgets, weekly routine) | [SH: weekly media buying routine](wiki/courses/evolve/start-here/playbooks/weekly-media-buying-routine.md) | [campaign structure 3:2:2](wiki/courses/evolve/start-here/frameworks/campaign-structure-322.md), [KPI thresholds](wiki/courses/evolve/start-here/libraries/kpi-thresholds.md) |
| Audit an ad account | [SH: ad account audit](wiki/courses/evolve/start-here/rubrics/ad-account-audit.md) | [click-based attribution](wiki/courses/evolve/start-here/concepts/click-based-attribution.md) |
| Plan tests / read results / scale | [test-and-iterate](wiki/playbooks/test-and-iterate.md) | [creative testing system](wiki/frameworks/creative-testing-system.md), [SH: winning-ad labels](wiki/courses/evolve/start-here/concepts/winning-ad-labels.md), [SH: scaling rules](wiki/courses/evolve/start-here/frameworks/scaling-rules.md) |
| Decide what to change after a test (loser / KPI winner / spend winner / breakthrough) | [CW: iterate on test results](wiki/courses/evolve/copywriting/playbooks/iterate-on-test-results.md) | [issue codes #1–#14](wiki/courses/evolve/copywriting/frameworks/iteration-issue-codes.md), [iteration playbook](wiki/courses/evolve/copywriting/frameworks/iteration-playbook.md), [SH: learnings review](wiki/courses/evolve/start-here/frameworks/learnings-review.md) |
| Test a page (split test, CRO) | [RMBC: CRO testing](wiki/courses/stefan-georgi/rmbc-ii/frameworks/cro-testing.md) | [RMBC benchmarks](wiki/courses/stefan-georgi/rmbc-ii/libraries/benchmarks.md) |
| Run native, Google or TikTok ads | [RMBC: paid traffic by platform](wiki/courses/stefan-georgi/rmbc-ii/frameworks/paid-traffic-by-platform.md) | [native advertising](wiki/concepts/native-advertising.md) |
| Set up a creator / ambassador program or whitelisting | [SH: creator program setup](wiki/courses/evolve/start-here/playbooks/creator-program-setup.md) | [brand ambassador program](wiki/courses/evolve/start-here/frameworks/brand-ambassador-program.md) |
| Position a brand / find what only we can say | [CW positioning](wiki/courses/evolve/copywriting/concepts/positioning.md) | [positioning exercise](wiki/courses/evolve/copywriting/frameworks/positioning-exercise.md) |
| Find examples in my niche | [brands hub](wiki/brands/README.md) | ad teardown libraries: [Tether](wiki/libraries/ad-teardowns.md), [CW](wiki/courses/evolve/copywriting/libraries/ad-teardowns.md), [SH](wiki/courses/evolve/start-here/libraries/ad-teardowns.md), [RMBC](wiki/courses/stefan-georgi/rmbc-ii/libraries/ad-teardowns.md) |
| Which prompt to use | [prompts library](wiki/libraries/prompts.md), [CW prompts](wiki/courses/evolve/copywriting/libraries/prompts.md), [SH prompts](wiki/courses/evolve/start-here/libraries/prompts.md), [RMBC prompts](wiki/courses/stefan-georgi/rmbc-ii/libraries/prompts.md) | [Prompt Library module](wiki/courses/tether-lab/07-prompt-library/README.md), [ChatGPT](wiki/tools/chatgpt.md), [Claude](wiki/tools/claude-ai.md) |
| Offers, bundles, buy box | [offer & bundle psychology](wiki/frameworks/offer-and-bundle-psychology.md) | [Fogg model](wiki/frameworks/fogg-behavior-model.md), [RMBC: upsell formula](wiki/courses/stefan-georgi/rmbc-ii/concepts/upsell-formula.md) |
| **Make an ad with AI** (AI UGC, animated, AI static): pick the format | [ACL: AI ad format catalog](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/ai-ad-format-catalog.md) → the playbook it names | [ACL: AI creator compliance](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/ai-creator-compliance.md) (always), [ACL playbooks](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/playbooks/README.md) |
| Produce a realistic AI UGC / AI podcast / street-interview ad | [ACL: produce an AI UGC ad](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/playbooks/produce-an-ai-ugc-ad.md) | [Seedance workflow](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/ai-ugc-seedance-workflow.md), [rizz-model pipeline](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/rizz-model-ai-ugc-pipeline.md), [character consistency](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/character-consistency.md) |
| Produce an animated AI ad (skeleton, crochet, claymation, talking object, song) | [ACL: produce an animated AI ad](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/playbooks/produce-an-animated-ai-ad.md) | [animated pipeline](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/animated-ad-production-pipeline.md), [song-ad workflow](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/song-ad-workflow.md), [start/end-frame video](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/start-end-frame-video.md) |
| Make AI static ads | [ACL: make AI static ads](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/playbooks/make-ai-static-ads.md) | [static-ad-creation](wiki/playbooks/static-ad-creation.md) limits stay the default; [static rewrite moves](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/static-rewrite-moves.md) |
| Write prompts for video / image / voice models, or find a course skill | [ACL: reference-first prompting](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/reference-first-prompting.md) | [ACL prompts and skills](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/libraries/prompts.md), [ACL tool settings](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/libraries/tool-settings.md) |
| Edit AI footage so it looks native; QA before publishing | [ACL: AI post-production](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/ai-post-production.md) | [AI video QA checklist](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/rubrics/ai-video-qa-checklist.md), [AI realism tells](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/ai-realism-tells.md) |
| Run ad production with Claude skills / Claude Code | [ACL: Claude Code ad operator](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/claude-code-ad-operator.md) | [AI song-ad pipeline demo](wiki/resources/ai-song-ad-pipeline-loom.md) |
| Review / roast an ad before launch | [ACL: ad roast scorecard](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/rubrics/ad-roast-scorecard.md) | [ACL: winning-ad checklist](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/winning-ad-checklist.md), [ad scorecard](wiki/rubrics/ad-scorecard.md) |
| Find competitor ads by spend, not run time | [ACL: ad spend signal](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/ad-spend-signal.md) | [ACL: research document protocol](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/frameworks/research-document-protocol.md) |
| Two pages disagree | [topic map](wiki/topic-map.md), then [contradictions](wiki/contradictions.md) | — |

CW = Evolve Copywriting · SH = Evolve Start Here · RMBC = RMBC II · ACL = Ad Creators Lab.

## The core lenses (apply to every ad)
| Lens | Question | Values | Run with |
|---|---|---|---|
| Identity first | Which self does it speak to? | Actual / Ideal / Ought (0–10 each) | [three-selves diagnostic](wiki/frameworks/three-selves-diagnostic.md) |
| Emotion | Valence × intensity: which zone, and does it fit the buyer's state? | Z1 feel-good · Z2 hype · Z3 pain whisper · Z4 danger | [valence-intensity diagnostic](wiki/frameworks/valence-intensity-diagnostic.md) |
| Specific emotion | Which purchase emotion, how specific? | 9 mindstates → sub-emotion | [mindstate mapping](wiki/frameworks/mindstate-emotion-mapping.md) |
| Tactics | Which heuristics, stacked how? | 2–3, fluency as base | [heuristics hub](wiki/concepts/heuristics.md) |
| Journey | Which stage is it written for? | Trigger / Exploration / Evaluation / Purchase | [TEEP](wiki/frameworks/teep-journey.md) |
| Behaviour | Motivation, ability or prompt missing? | B = MAP; find the ability crusher | [Fogg](wiki/frameworks/fogg-behavior-model.md) |
| Story | Which structure carries it? | Pixar, In Medias Res, SCQA, Freytag, skeptic… | [story frameworks](wiki/frameworks/story-frameworks-for-ads.md) |
| Layout | What does the eye hit first? | heaviest → next heaviest | [visual weight](wiki/frameworks/visual-weight-hierarchy.md) |

Priority (Sarah): **identity → emotion → behaviour/tactics**; heuristics are "secondary characters".

**Copy lenses (Evolve; apply to every line you write):** three checks (visualise / falsify / nobody else can say it) · facts over opinions · spoken, grade ≤6 · awareness level · hook = emotion + curiosity gap + stakes, then a bridge · show, don't tell · payoff and belief before the pitch. Score with the [copy checklist scorecard](wiki/courses/evolve/copywriting/rubrics/copy-checklist-scorecard.md).

**Funnel lenses (RMBC; apply to every page and long-form asset):** what did the ad already reveal (so how much the page must do) · one congruent promise from ad to page to checkout · the unique mechanism as a cause (problem) and a fix (solution) · unit economics before scale. See [ad-to-page journey](wiki/courses/stefan-georgi/rmbc-ii/concepts/ad-to-page-journey.md) and [funnel economics](wiki/courses/stefan-georgi/rmbc-ii/concepts/funnel-economics.md).

## Non-negotiable rules
1. **Copy the mechanism, not the asset.** Remix angles, structures and psychology. Never reuse competitors' footage, images, exact script lines, characters, catchphrases, trademarks, claims or stats. Use the fidelity check in [angle-remix](wiki/playbooks/angle-remix.md).
2. **Never fabricate** proof, testimonials, reviews, ratings, counts, press, endorsements, experts, results, scarcity or urgency. Every claim needs a `truth_ref` in the product truth sheet ([template](wiki/playbooks/README.md#product-truth-sheet-required-before-remixing)). Course examples that broke this are warnings, not models: Net Positive's invented "Only 9 sets left", ChatGPT's invented press bar, and most RMBC II example briefs, VSLs and advertorials (invented doctors, testimonials and studies; see [RMBC compliance hard stops](wiki/courses/stefan-georgi/rmbc-ii/contradictions.md#compliance-hard-stops-10)).
3. **Audit every LLM draft** with the [LLM output claim audit](wiki/courses/stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) before it leaves your hands. Models invent experts, quotes and numbers by default.
4. **Flag instructors' uncited stats** as anecdotes, never as fact in ad copy or client decks. Sarah's examples: "0.48 s", "0.2 s", "60,000× faster", "+13.6% likability", "5.43×", "KFC +56%". Evolve's "$1M ad", "96% of dog owners" and the GLP-1 percentages are illustrative. RMBC [benchmarks](wiki/courses/stefan-georgi/rmbc-ii/libraries/benchmarks.md) are labelled "(instructor claim)" or "(guest claim)": planning baselines only, quoted with their label; the ⛔ example-claim rows are never reused.
5. **When sources disagree**, follow the owner page in the [topic map](wiki/topic-map.md) and the default in [contradictions](wiki/contradictions.md) (rows X1–X29, S1–S5, R1–R16, AC1–AC9), and say so.
6. **Don't shame the viewer.** Negative zones target situations or industry beliefs and end in relief or hope.
7. **Mark your inferences.** Tags, timings and thresholds that aren't the instructor's are labelled (derived), (wiki tag) or (pipeline design). Keep that labelling in your outputs.
8. **One learning goal per test, one core emotion per ad, one variable per iteration** (bigger swings are fine for brand-new angles; see S1).
9. **AI people are actors, not customers.** No real person's face or voice without written rights (no stranger photos as "creators", no cloned voices, no celebrity look-alikes). AI characters never give first-person results, testimonials or expert verdicts, and no fake comments or reviews in edits. Ad Creators Lab examples often break this: follow [AI creator compliance](wiki/courses/ad-creators-lab/ai-ads-ugc-animations/concepts/ai-creator-compliance.md).

## How to cite
- Cite the wiki page and the video moment: `[Roast My Ads #3](wiki/courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) [0:19:30]`. Lessons use `[mm:ss]`, live sessions `[h:mm:ss]`.
- Course-local pages: Evolve Copywriting cites `[L26 03:15]` = lesson 26 at 03:15; Start Here cites `[L81 12:17]`; RMBC cites `[04-10 45:07]` = module 4, lesson 10, and `[07-01 v2 05:30]` for the second video of a lesson. Documents use page numbers (e-book p.5).
- Quote verbatim lines in quotation marks; label paraphrase, transcription uncertainty and your own derivations.
- In artifacts, cite teardown cards by ID (`TD-…`), customer evidence by item ID (`REV-12`), and claims by `truth_ref`.

## How to add new knowledge
- New courses and sources follow the ingestion contract in the repository root [INGESTION.md](../INGESTION.md) (creator-local paths, manifests, PROGRESS.md) and the schema and ingest workflow in [CLAUDE.md](CLAUDE.md) (page conventions, frontmatter, "Agent use" block, structured tables).
- A new course is wired into this task table, the [topic map](wiki/topic-map.md) and [contradictions](wiki/contradictions.md) as described in INGESTION.md step 6.
- Reusable outputs from your work (a strong teardown card, a new rule learned from a test) go back into the matching [library](wiki/libraries/README.md) with sources, and get logged per CLAUDE.md. Don't edit `raw/`.
