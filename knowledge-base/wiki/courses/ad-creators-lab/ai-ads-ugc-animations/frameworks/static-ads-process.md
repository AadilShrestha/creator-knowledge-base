---
title: "Static ads process: research → angle bank → headline bank → template → AI image (with the prompt library)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "unverified for 069-075 (presenter not named; Epic Ads Lab shirt on screen); 076 screen-shared from the Camilo Poppy account (unverified); Camilo for the roast inputs (083-084); Caleb Kruse for the Claude Code static batch (093)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/069-static-ads-intro.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/070-full-static-ads-creation-process.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/071-making-statics-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/100-why-copying-longest-running-is-bad.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/101-how-to-find-ads-based-on-ad-spend.md
  - knowledge-base/wiki/playbooks/static-ad-creation.md
tags: [static-ads, process, research-doc, avatar, angle-bank, headline-bank, awareness-levels, canva-templates, poppy, nano-banana-pro, chatgpt-image, prompt-library, ai-imagery, compliance]
updated: 2026-11-13
---

# Static ads process (Ad Creators Lab)
> The course's static pipeline in eight gated steps: one research document and one avatar, ≤1 hour of concept research (70/20/10, adjacent niches), an angle bank and headline bank by awareness level, then copy written into editable templates while AI produces only the image layer. Two production routes exist (Canva/Figma template + image swap, 070-071; Poppy reference generation in Nano Banana Pro, 076). Where it conflicts with the shared [static ad creation playbook](../../../../playbooks/static-ad-creation.md), the playbook's limits are the default.

## 🤖 Agent use
- **Use when:** producing a batch of AI-assisted static image ads for one product; choosing between "template + swap" and "generate from reference ads"; finding the course's research, angle, headline and teardown prompts.
- **Inputs → outputs:** product facts (verified claims list), real customer language (Reddit, TikTok comments, own and competitor reviews), 2+ real packshots, a template pack or 2-4 spend-qualified reference statics → research doc + 1 avatar → angle bank by awareness level → headline bank (one mass desire at a time) → 10 concepts with headline, first line, benefits → image layer → finished statics → claim audit and fidelity check.
- **Rules:**
  - **DO** build from one research document and one chosen avatar, "a singular source of truth" [L70 02:57–03:41](../lessons/070-full-static-ads-creation-process.md); copying competitor ads without it is "the fastest way… to make zero sales" (instructor claim) [L69 00:00](../lessons/069-static-ads-intro.md).
  - **DO** cap concept research at 1 hour: 10 competitor + 10 adjacent-niche ideas, split about 70% proven elsewhere / 20% own winners / 10% new (instructor rule of thumb) [L70 03:41; 06:02](../lessons/070-full-static-ads-creation-process.md).
  - **DO** write copy in an editable template and let AI generate only the image; regenerating a whole ad rerolls text and sizing on every edit [L70 08:17–08:52](../lessons/070-full-static-ads-creation-process.md); [L71 00:00](../lessons/071-making-statics-with-ai.md).
  - **DO** answer the Headline Bank prompt's mass-desire question yourself; letting the AI pick "sometimes" gives bad output [L76 01:50](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).
  - **DO** work one awareness level per prompt run [L76 04:42–05:37](../lessons/076-new-make-static-ads-with-ai-poppy-method.md); [L70 08:52–09:46](../lessons/070-full-static-ads-creation-process.md).
  - **DO** attach several real packshots as references and compare every output at full size; fix pack errors with an exact edit plus a correct reference [L76 02:48–03:44; 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).
  - **DON'T** ship any number, review count, study or "patented" claim the model wrote: the course's own GPT output invented "5,400+ 4.8-star reviews" for a generic product [L71 00:54–02:19](../lessons/071-making-statics-with-ai.md).
  - **DON'T** pick reference ads by "longest running" (the 076 demo does); choose by spend and duplicates ([L100](../lessons/100-why-copying-longest-running-is-bad.md), [L101](../lessons/101-how-to-find-ads-based-on-ad-spend.md)) and copy the layout mechanism only.
  - **IF** the headline bank returns 8-10-word lines **THEN** cut to 4-7 words (playbook default); keep a longer line only when it is a verbatim customer phrase that still reads in one second (derived default, see [Disagreements](#where-this-agrees-and-disagrees-with-the-shared-static-playbook)).
  - **IF** a static gets high CTR but weak conversion **THEN** check the landing page before the ad: an education-needing callout sent to a thin PDP fails there [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md).
- **See also:** [Static rewrite moves](static-rewrite-moves.md) · [Research document protocol](research-document-protocol.md) · [Make AI static ads playbook](../playbooks/make-ai-static-ads.md) · [Static copy levers](../concepts/static-copy-levers.md) · [Ad spend signal](../concepts/ad-spend-signal.md) · [Prompts library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md) · Shared: [static ad creation](../../../../playbooks/static-ad-creation.md), [ad scorecard](../../../../rubrics/ad-scorecard.md) · Evolve: [static ad workflow](../../../evolve/copywriting/frameworks/static-ad-workflow.md), [write static image ads](../../../evolve/copywriting/playbooks/write-static-image-ads.md) · RMBC: [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

## Route decision
| Situation | Route | Why | Source |
|---|---|---|---|
| You have (or can buy) proven layout templates in Canva/Figma | **A. Template + image swap** | Copy stays editable; only the product image is generated; "many cheap variants that can be easily tested" | [L70 08:52–10:30](../lessons/070-full-static-ads-creation-process.md); [L71](../lessons/071-making-statics-with-ai.md) |
| You need many styles fast and have a chat + image model in one workspace (Poppy or equivalent) | **B. Reference generation** | Research, headline bank, reference ads and image model in one board; 4 references × 3 prompts = 12 images per awareness level | [L76](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| You run Claude Code with an image API | **C. Agent batch** (see [Claude Code ad operator](claude-code-ad-operator.md)) | 37 layout templates; Nano Banana for photoreal elements, ChatGPT Image 2 for typography/UI mimicry; ~$0.30 per image (instructor claim) | [L93 29:24–30:52; 36:11–40:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| "Recreate this competitor ad in ChatGPT with my product" | **Reject** | "Good for fast drafts but very slow iterations"; text and sizing drift; 1:1 copy risk | [L70 08:17](../lessons/070-full-static-ads-creation-process.md) |

## Procedure
| # | Step | Tool (at recording, Aug-Sep 2026) | Input → output | Check before next step | Source |
|---|---|---|---|---|---|
| 1 | Research document | Research Doc prompt in ChatGPT/Claude; Reddit, TikTok comments, own + competitor Amazon reviews | raw customer data → categorized insights (pains, failed solutions, desires, objections, misconceptions, golden nuggets, language notes, personas) | Every quote traceable to raw data; no invented quotes | [L70 00:00–01:59](../lessons/070-full-static-ads-creation-process.md); full protocol: [research document protocol](research-document-protocol.md) |
| 2 | One avatar | Buyer Avatar GPT (link only; instructions not in course files) | research doc → 3 avatars, choose 1 at "Susan, 45" specificity | Avatar fields trace to quotes; desire stated | [L70 01:59–03:41](../lessons/070-full-static-ads-creation-process.md) |
| 3 | Concept research | Ad-spy site, Adnova (beta), ChatGPT for adjacent niches | niche → 10 competitor + 10 adjacent ideas in ≤1 h | 70/20/10 split; ideas chosen by spend, not run time | [L70 03:41–06:56](../lessons/070-full-static-ads-creation-process.md); [L101](../lessons/101-how-to-find-ads-based-on-ad-spend.md) |
| 4 | Angle bank | "Angles Prompt" (finds mass desires, asks you to choose, organises by awareness level) | research doc → angles per level (most, product, solution, problem, unaware) | You chose the mass desire | [L70 07:33](../lessons/070-full-static-ads-creation-process.md) |
| 5 | Headline bank | Static Ad Headline Bank prompt (Claude Opus 4.6 in Poppy; any chat model) | chosen mass desire → ≥15 ranked headlines with 2 alternates each, exported by awareness level and angle | Cut to 4-7 words; strip invented proof (see compliance) | [L70 prompt](../lessons/070-full-static-ads-creation-process.md#static-ad-headline-bank-prompt); [L76 03:44–04:42](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 6 | Pick 10 concepts / references | Route A: template pack (Us vs Them, hook + 3 benefits). Route B: in-tool Facebook Ads search, Images filter | angle bank → 10 templates, or 2-4 reference statics + 2+ real packshots | References spend-qualified; layout only, no lines/claims kept | [L70 06:56; 08:52](../lessons/070-full-static-ads-creation-process.md); [L76 01:50–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 7 | Copy per concept | Copy GPT with research doc loaded ("Ad Copywriter Pro") | template screenshot + avatar → 10 headlines + 10 benefits; or benefits/negatives + 5 headlines per awareness level | Each benefit matches a real product fact | [L71 00:53–02:36](../lessons/071-making-statics-with-ai.md); [L70 09:20–09:46](../lessons/070-full-static-ads-creation-process.md) |
| 8 | Image layer | Route A: ChatGPT image in a separate chat, square. Route B: Nano Banana Pro ("Best-Image" in the picker), one prompt per conversation for parallel runs | packshot + scene instruction → product image; or reference + headline → full static | Pack shape, lid, label, orientation, text alignment at full size | [L71 02:36–03:38](../lessons/071-making-statics-with-ai.md); [L76 05:37–07:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 9 | Repair | AI edit or chat with a correct reference | wrong output + real packshot + exact instruction → fixed image | Repeat until pack matches | [L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 10 | Assemble and finish | Canva/Figma | text + image → static; resize, brightness, brand colours | Brand palette (off-brand stickers "take away from perceived value"); contrast; typos | [L71 03:38–04:42](../lessons/071-making-statics-with-ai.md); [L83 23:37–25:35](../lessons/083-ad-roast-calls-2026-08-17.md) |
| 11 | Gate | [Claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md), [ad scorecard](../../../../rubrics/ad-scorecard.md), fidelity check | finished statics → pass / fix list | No invented proof; no 1:1 competitor layout + copy | [L76 page notes](../lessons/076-new-make-static-ads-with-ai-poppy-method.md); shared playbook quality gates |

### Prompts typed in the videos (near-verbatim; full texts live in the lessons)
- Image swap: "Replace the image of the can with the product image… Keep everything else the same." [L70 08:52](../lessons/070-full-static-ads-creation-process.md)
- Copy per level: "Based on this concept and the angle bank, give me the benefits and negatives… one set for each awareness level. Also give five headlines." [L70 09:20–09:46](../lessons/070-full-static-ads-creation-process.md)
- Template copy: "I am making a creative in this style [screenshot]. Come up with 10 headlines and 10 benefits I can use for my [avatar]." [L71 step 2](../lessons/071-making-statics-with-ai.md)
- Scene: "Put this product on a kitchen counter with a clear mug of coffee next to it." [L71 03:06](../lessons/071-making-statics-with-ai.md)
- Reference generation: "Let's focus on awareness level solution and study the static ad examples from the Facebook ads folder and create three image prompts for each example using the images of the [brand]…" [L76 04:42–05:37](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)
- Repair: "change the serving method of the image with the pasta so it looks like the image with the white background" [L76 07:31](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)

## Prompt library index (what the course ships for statics)
| Prompt | Job | Where the full text is | Caution |
|---|---|---|---|
| Product info creation prompt | Feature → benefit → desire → core need → pain → struggle → objection → handling → ICP table | [L70](../lessons/070-full-static-ads-creation-process.md#product-info-creation-prompt) | Fill from verified facts only |
| Research Doc creation prompt | Raw audience data → categorized insights + personas | [L70](../lessons/070-full-static-ads-creation-process.md#research-doc-creation-prompt); same prompt in [L97](../lessons/097-customer-research-protocol-1.md) | Its "rewrite clunky golden nuggets" clause can fabricate quotes; keep verbatim |
| Angles Prompt | Mass desires → angle bank by awareness level | Described in [L70 07:33](../lessons/070-full-static-ads-creation-process.md); text not in course files | — |
| Static Ad Headline Bank prompt | ≥15 headlines, 6-10 words, ranked, 2 alternates, awareness-level export | [L70](../lessons/070-full-static-ads-creation-process.md#static-ad-headline-bank-prompt); identical `.txt` in [L76](../lessons/076-new-make-static-ads-with-ai-poppy-method.md#static-ad-headline-bank-prompt) | Its example lines "12,000+ customers already trust [product]", "Experts trust it", "[product] is almost gone" are invented proof/scarcity: **don't execute** |
| Ad Analysis & Opportunity Extraction | Teardown of 5 competitor + 5 other-niche ads → weaknesses, opportunities, transferable ideas | [L70](../lessons/070-full-static-ads-creation-process.md#ad-analysis--opportunity-extraction-prompt) | Pair with the shared [competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) card |
| Comprehensive Market Research prompt | 9-step, 25+ page, every claim linked to a source URL | Condensed in [L70](../lessons/070-full-static-ads-creation-process.md#market-research-prompt-structure-condensed) | Check that cited URLs exist |
| Scripting / Hook / B-roll / Editing / Repair / Bulletproof script prompts | Video, not statics | [L70](../lessons/070-full-static-ads-creation-process.md#briefing-prompts-scripting-hook-filming-b-roll-editing-guideline) | Use the repo [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) for scripts |

## Failure fixes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Editing one word rerolls the whole image | Full-ad generation | Move copy into a template; generate image layer only | [L71 00:00](../lessons/071-making-statics-with-ai.md) |
| Generated pack differs from the real box (lid, shape) | Model invents product detail | Attach real packshots as a reference group; AI edit with correct reference and an exact change | [L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| Generic or "AI-sounding" headlines | AI chose the mass desire; weak research | Answer the desire question; feed real research ("weak inputs can produce poor creative") | [L76 01:50; page](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| Pack blends into background | Low contrast | Regenerate with "more contrast… a backlight" | [L83 25:35](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Looks "made on Canva" | Off-brand colours | Brand palette only (example: brand gold + black text) | [L83 23:37](../lessons/083-ad-roast-calls-2026-08-17.md) |
| High CTR, low CVR | Education-needing ad, thin PDP | Education-led page or listicle/advertorial; PDP images as mini-ads | [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Static reads as retargeting | Product-heavy visual | Test a product-light version (mug + ingredient list) | [L84 06:23](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Batch drifts into AI giveaways | No QA pass | Second-pass prompt: "identify anything that sticks out… as an AI giveaway and then regenerate it" | [L93 39:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |

## Compliance gate (run before any static ships)
- [ ] Every number, rating, review count, ranking, "patented/clinically backed" line traces to a verified source; otherwise cut ([L71](../lessons/071-making-statics-with-ai.md) shows the model inventing them).
- [ ] No headline-bank example proof carried over ("12,000+ customers", "Experts trust it", "almost gone"): **don't execute**; replace with a true count, a real expert, or nothing.
- [ ] Product layer built from our own real packshots; no third-party product in a style-match (the 071 demo used another brand's face cream) [L71 limitations](../lessons/071-making-statics-with-ai.md).
- [ ] Reference ads used for layout type and angle only; composition, props, copy, palette and claims changed; no competitor marks (076 asks the model to "technically recreate images like these": keep to mechanism) [L76 02:48](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).
- [ ] No AI-generated people presented as customers, experts or testimonial givers (see [AI creator compliance](../concepts/ai-creator-compliance.md)).
- [ ] Category rules checked: alcohol, health, weight loss and supplements need substantiation; wine "health relief, headaches" desires in 076 are not claims we can make [L76 limitations](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).

## Where this agrees and disagrees with the shared static playbook
The shared [static ad creation playbook](../../../../playbooks/static-ad-creation.md) (Tether Lab) owns statics in the [topic map](../../../../topic-map.md). This course adds the AI production pipeline; it does not override the playbook's limits.

| Topic | This course | Shared playbook | Agent default |
|---|---|---|---|
| Statics as cheap message tests | Agrees: "with tight budget test statics" [L86 1:12:21](../lessons/086-ad-psychology-with-howie-2026-08-12.md); templates make "cheap variants" [L70 10:30](../lessons/070-full-static-ads-creation-process.md) | "Dirt cheap to run and dirt cheap to make" | Same |
| Customer language in headlines | Agrees: "from the customer's own mouth" (Headline Bank) | Keep candidates in customer language | Same |
| One message | Agrees: "rule of one thing" [L84 05:24](../lessons/084-ad-roast-calls-2026-08-21.md) | One core emotion, one headline, one CTA | Same |
| Headline length | 6-10 words max (Headline Bank prompt, [L70](../lessons/070-full-static-ads-creation-process.md#static-ad-headline-bank-prompt)) | 4-7 words, ≤3 lines | 4-7 words; ≤10 only for a verbatim customer phrase that reads in one second (derived) |
| Call-out count | Template with 5 benefits + 5 negatives (Us vs Them, [L70 09:01 frame](../lessons/070-full-static-ads-creation-process.md)); 3 benefits ([L71](../lessons/071-making-statics-with-ai.md)); 5 call-outs and dense text in rewrites ([L74](../lessons/074-fixing-bad-static-ads-2.md), [L75](../lessons/075-fixing-bad-static-ads-3.md)) | ≤3 call-outs, each ≤3 lines | ≤3; comparison tables may list more rows if each is one short line (derived); dense "brochure" layouts only as a labelled test (see [rewrite moves](static-rewrite-moves.md#m20-brochure-effect-dense-copy-when-the-headline-hooks-a-felt-need)) |
| AI imagery | AI product scenes in templates (071), full statics generated from competitor references in Nano Banana Pro (076), 50-ad agent batches (093) | Asset source = shoot file, video still, render; "AI image (novelty only)"; fidelity check against cloning | Product must come from real packshots as references and pass a full-size fidelity check; AI scenes/backgrounds allowed; no AI people as customers; no 1:1 recreation |
| Badges and proof | Headline Bank examples and 074-075 "after" examples include invented scarcity, testimonials and an expert quote | "Only true badges"; badge claims repeated on the landing page | Playbook rule; course examples: **don't execute** |
| Reference selection | 076 sorts by "Longest running" | Fidelity check; winner signals via [teardown](../../../../playbooks/competitor-ad-teardown.md) | Spend and duplicates ([ad spend signal](../concepts/ad-spend-signal.md)); longest-running = layout reference only, labelled BOFU |

## Cross-course notes
- **Evolve Copywriting:** [static ad workflow](../../../evolve/copywriting/frameworks/static-ad-workflow.md) has the same split (angle-first route vs image-first route borrowing a proven structure) and the same product-truth QA ([write static image ads](../../../evolve/copywriting/playbooks/write-static-image-ads.md), GLP-1 68% vs 56% case). Agreement on "borrow structure, never words". This course adds the AI image layer and the Poppy/agent routes.
- **Evolve Start Here:** research doc and avatar steps are covered more deeply in [research doc](../../../evolve/start-here/concepts/research-doc.md) and [core and sub-avatars](../../../evolve/start-here/concepts/core-and-sub-avatars.md) (desire-first avatars vs this course's demographic "Susan, 45"). Use Evolve's desire-first build when the two differ.
- **RMBC II:** every LLM-written headline bank goes through the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md); the 14 claim types in [compliance red flags](../../../stefan-georgi/rmbc-ii/concepts/compliance-red-flags.md) cover the headline-bank example lines.
- **Tether Lab:** layout, colour, fonts, faces and the variation ladder stay in the [static ad creation playbook](../../../../playbooks/static-ad-creation.md) and [format variation ladder](../../../../frameworks/format-variation-ladder.md); this course says nothing about visual weight.

## Where it's taught
| Lesson | What it adds | Timestamps |
|---|---|---|
| [069 Static ads intro](../lessons/069-static-ads-intro.md) | Intention over imitation; single source of truth | 00:00 |
| [070 Full static ads creation process](../lessons/070-full-static-ads-creation-process.md) | Full pipeline, 70/20/10, adjacent niches, 1-hour cap, template + swap, the Google-Doc prompt library | 00:00–10:46 |
| [071 Making statics with AI](../lessons/071-making-statics-with-ai.md) | Template population, product scene, background style-match | 00:00–04:42 |
| [076 Poppy method](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) | Headline Bank in Poppy, Facebook Ads references, Nano Banana Pro, repair | 00:00–08:52 |
| [083 Roast 17 Aug](../lessons/083-ad-roast-calls-2026-08-17.md) | Crochet statics: clarity, brand colour, contrast, CTA-button test | 21:53–29:59 |
| [084 Roast 21 Aug](../lessons/084-ad-roast-calls-2026-08-21.md) | Strong callout statics, page fit, product-light test | 01:34–08:13 |
| [093 Mr Paid Social](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | 50-static agent batch, 37 templates, self-QA | 29:24–41:50 |

## Related
[Static rewrite moves](static-rewrite-moves.md) · [Winning-ad checklist](winning-ad-checklist.md) · [Claude Code ad operator](claude-code-ad-operator.md) · [Ad roast scorecard](../rubrics/ad-roast-scorecard.md) · [Rewrites library](../libraries/rewrites.md) · [Diversification vs variation](../concepts/diversification-vs-variation.md)
