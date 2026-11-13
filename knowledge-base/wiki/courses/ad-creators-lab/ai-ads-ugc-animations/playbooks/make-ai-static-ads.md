---
title: "Playbook: make AI static ads (research doc → avatar → concept sourcing → angle bank → headline bank → template → AI product image → copy per awareness level → review → claim audit → test)"
type: playbook
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (static module 069–076, speaker not named on screen); Camilo (roast statics 083–084)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/008-how-to-make-diversified-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/069-static-ads-intro.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/070-full-static-ads-creation-process.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/071-making-statics-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/072-static-ads-mistakes-to-avoid-4-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/073-fixing-bad-static-ads-10-51.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/074-fixing-bad-static-ads-2.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/075-fixing-bad-static-ads-3.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/100-why-copying-longest-running-is-bad.md
tags: [playbook, static-ads, ai-images, nano-banana, canva, templates, headline-bank, angle-bank, awareness, benefit-ladder, claims, testing]
updated: 2026-11-13
---

# Playbook: make AI static ads
> The course's static pipeline turned into gated steps: research doc and one avatar, an hour of concept sourcing (competitors + adjacent niches), angle bank by awareness level, headline bank, proven templates, AI-generated product imagery placed with "keep everything else the same", copy written per awareness level inside the template, full-size review, claim audit, then a format-diverse test.

## 🤖 Agent use
- **Use when:** a batch of image ads is needed for a product, a message must be tested cheaply, or a winning video angle should be restated as statics.
- **Inputs → outputs:** research doc + avatar + real product photos + brand kit + template pack → angle bank, headline bank, 10 template concepts, AI product images, finished statics, test plan.
- **Rules:**
  - **DON'T** clone competitor ads blindly: "the fastest way for you to make zero sales and have high CPAs" (instructor claim) [L69 00:00](../lessons/069-static-ads-intro.md). Competitor ads are concept inspiration, never a layout-and-copy clone.
  - **DO** work in templates and swap images; regenerating the whole ad is "good for fast drafts but very slow iterations" [L70 08:17–08:52](../lessons/070-full-static-ads-creation-process.md), and one mistake rerolls everything [L71 00:00](../lessons/071-making-statics-with-ai.md).
  - **DO** write copy inside the template, not in the image model; tell the image model "Keep everything else the same" when swapping a product in [L70 08:52](../lessons/070-full-static-ads-creation-process.md).
  - **DO** build headlines from what customers actually say, "rather than trying to be some kind of genius copywriter" [L72 00:53–01:49](../lessons/072-static-ads-mistakes-to-avoid-4-17.md).
  - **DON'T** trust AI copy output: the on-screen GPT output in L71 contains claims and review counts nobody supplied [L71](../lessons/071-making-statics-with-ai.md). Run the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md).
  - **DON'T** execute the course's invented urgency, testimonials or expert quotes in "after" examples ("last 200 pairs", dentist quote) [L74](../lessons/074-fixing-bad-static-ads-2.md), [L75](../lessons/075-fixing-bad-static-ads-3.md): use only real reasons, real reviews, real experts.
  - **IF** the product is not shown accurately (pack shape, label, orientation) **THEN** fix with an AI edit plus a reference image and an exact instruction before anything ships [L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).
- **See also:** [Static ads process](../frameworks/static-ads-process.md) · [Static rewrite moves](../frameworks/static-rewrite-moves.md) · [Static copy levers](../concepts/static-copy-levers.md) · [Diversification vs variation](../concepts/diversification-vs-variation.md) · [Shared static ad creation playbook](../../../../playbooks/static-ad-creation.md) · [Evolve: write static image ads](../../../evolve/copywriting/playbooks/write-static-image-ads.md) · [Canva](../../../../tools/canva.md) · [ChatGPT](../../../../tools/chatgpt.md) · [Prompts library](../libraries/prompts.md) · [Rewrites library](../libraries/rewrites.md)

## Inputs required up front
| Input | Why | If missing |
|---|---|---|
| Research document (real customer language: pains, desires, moments, objections, failed solutions) | "A singular source of truth" [L70 02:57–03:41](../lessons/070-full-static-ads-creation-process.md); "weak inputs can produce poor creative" [L76 page](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) | Run [research to AI ad concepts](research-to-ai-ad-concepts.md) steps 1–4 first |
| One avatar at "Susan aged 45" specificity | "If you target everybody, you target nobody" [L70 01:59–02:57](../lessons/070-full-static-ads-creation-process.md) | Same |
| Product facts, claims allowed, real proof | Benefits and proof lines trace here | Bracket; no proof element |
| Offer (exact) and price | Offer statics are bottom-of-funnel [L73 05:56](../lessons/073-fixing-bad-static-ads-10-51.md) | No offer statics in the batch |
| Several real product photos (pack, label, format) | AI images must match the real pack [L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) | Block AI product imagery |
| Brand kit (colours, fonts) | Off-brand colours "take away from the perceived value" [L83 23:37](../lessons/083-ad-roast-calls-2026-08-17.md) | Neutral palette; flag |
| Template pack (Canva/Figma) or proven own layouts | Template + swap workflow [L71 00:00–00:53](../lessons/071-making-statics-with-ai.md) | Build 5 format layouts per [L08 02:43](../lessons/008-how-to-make-diversified-ads.md) |
| Landing page | Funnel fit [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md) | Flag |

## The chain
| # | Step | Do | Tool | Output | Gate | Source |
|---|---|---|---|---|---|---|
| 1 | Research check | Confirm the research doc covers psychographics, problems/desires, moments, objections; verbatim quotes only | Research Doc prompt | Research doc | No invented quotes | [L70 00:33–01:59](../lessons/070-full-static-ads-creation-process.md) |
| 2 | Avatar | Pick one avatar; write it with Susan-level specificity | Buyer Avatar GPT (L70 page) or Claude | One avatar | Named, specific person | [L70 01:59–02:57](../lessons/070-full-static-ads-creation-process.md) |
| 3 | Concept sourcing | ≤1 hour: 10 same-niche + 10 adjacent-niche ideas; split ~70% proven by others / 20% own winners / 10% new | Ad-spy tool, Adnova, ChatGPT for adjacent niches; filter by spend, not run time | 20 concept refs with notes | Mechanism noted, not asset | [L70 03:41–06:02](../lessons/070-full-static-ads-creation-process.md); [L100](../lessons/100-why-copying-longest-running-is-bad.md) |
| 4 | Angle bank | Run the Angles Prompt; you choose the mass desire when asked | Claude/ChatGPT | Angles by awareness level | You picked the mass desire | [L70 07:33](../lessons/070-full-static-ads-creation-process.md); [L76 01:50](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 5 | Headline bank | Static Ad Headline Bank Prompt; answer its mass-desire question; one awareness level at a time | Claude (Poppy: "RUN poppy_prompt") | 15+ headlines | Customer words; level 4–5 benefits | [L70 page prompt](../lessons/070-full-static-ads-creation-process.md); [L76 03:54](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 6 | Templates | Pick 10 templates across **different formats** (us-vs-them, product + text, news/unaware, problem-solution, notes app); headline + first line each | Canva/Figma pack | 10 concepts | Zoomed out, they look different | [L70 06:56](../lessons/070-full-static-ads-creation-process.md); [L08 02:43](../lessons/008-how-to-make-diversified-ads.md) |
| 7 | Product image | Separate chat: product photo + scene instruction, square; swap into template with "Keep everything else the same"; or Nano Banana Pro, one prompt per conversation, 3 prompts per reference ad | ChatGPT / Nano Banana Pro / Poppy | Product-in-scene images | Label, shape, orientation correct | [L71 02:36–03:06](../lessons/071-making-statics-with-ai.md); [L76 04:42–06:27](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| 8 | Copy per level | Benefits, negatives (comparison layouts), 5 headlines per awareness level; paste into template fields | Copy GPT with research loaded first | Filled templates | Fits text boxes; brand fonts | [L70 08:52–09:46](../lessons/070-full-static-ads-creation-process.md); [L71 00:53–02:36](../lessons/071-making-statics-with-ai.md) |
| 9 | Review | Full size: packaging, text alignment, product mismatch; phone-size contrast check | Canva preview | Corrected statics | Readable in one second | [L76 07:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md); [L72 01:49–02:48](../lessons/072-static-ads-mistakes-to-avoid-4-17.md) |
| 10 | Rewrite pass | Apply the fix moves below | — | Revised copy | Five-point audit passes | [L72](../lessons/072-static-ads-mistakes-to-avoid-4-17.md)–[L75](../lessons/075-fixing-bad-static-ads-3.md) |
| 11 | Claim audit | [RMBC claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) on every headline, benefit, badge and number | — | Audited set | No unsourced number, review count, ranking, urgency | Repo rule; [L71](../lessons/071-making-statics-with-ai.md) |
| 12 | Score | [Roast scorecard](../rubrics/ad-roast-scorecard.md) (hook = headline + image in frame 1) and optionally shared [ad scorecard](../../../../rubrics/ad-scorecard.md) | — | Scorecards | Pass marks | [L84 37:59](../lessons/084-ad-roast-calls-2026-08-21.md) |
| 13 | Launch + test | Paused upload; format-diverse test; page fit | Ads Manager | Test plan | Human yes/no | [L93 50:59](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |

## Step 10: the fix moves (audit each static)
Five-point audit [L72](../lessons/072-static-ads-mistakes-to-avoid-4-17.md): (1) readable in one second on a phone [00:00; 01:49]; (2) benefit above level 1 [03:25]; (3) something only we can say [02:48]; (4) desire and a next step, not only a price or sale [00:53–01:49]; (5) natural/authentic vs polished template, whichever fits [00:53].

| Move | Before → after pattern | Source |
|---|---|---|
| Benefit ladder to level 4–5 | "You lose weight" → "You can finally wear the dress that has hung in your wardrobe for months" | [L72 03:25](../lessons/072-static-ads-mistakes-to-avoid-4-17.md) |
| Desire headline, not category claim | "Expert care" → "Get your rent on time" | [L73 00:00–01:55](../lessons/073-fixing-bad-static-ads-10-51.md) |
| "Without" line | add "without doing the chasing yourself"; "Hear the birds outside without spending $5000" | [L73 01:27–01:55](../lessons/073-fixing-bad-static-ads-10-51.md); [L74 00:52](../lessons/074-fixing-bad-static-ads-2.md) |
| Bridge CTA | "Ask [brand]" → "Skip the stress. Get the rent." | [L73 01:55](../lessons/073-fixing-bad-static-ads-10-51.md) |
| Show, don't claim | "Voted best" → show the real badge; shoe in a puddle for slip resistance | [L74 01:18](../lessons/074-fixing-bad-static-ads-2.md); [L73 04:35–05:01](../lessons/073-fixing-bad-static-ads-10-51.md) |
| Timeframe for perceived likelihood | product-label headline → benefit + realistic, true timeframe | [L75 01:10; 07:13–07:42](../lessons/075-fixing-bad-static-ads-3.md) |
| Cut vague words | "better", "game changer", "best on the market", "everyone is going crazy" → a specific, verifiable fact | [L83 24:36](../lessons/083-ad-roast-calls-2026-08-17.md); [L73 02:43–03:10; 09:13](../lessons/073-fixing-bad-static-ads-10-51.md); [L72 02:48–03:25](../lessons/072-static-ads-mistakes-to-avoid-4-17.md) |
| Rule of one thing | one idea per static; a strong callout needs nothing else | [L84 01:34–02:04; 05:24](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Specific contrast set | "No crashes, no jitters, no lock-in" → "No needle, no prescription, no crashes" (contrast with the real alternative) | [L83 26:33–27:33](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Ingredient step back | say what the ingredient does before the emotional payoff | [L83 28:04](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Visual craft | brand colours, more contrast / backlight on the pack, clear images of what things are | [L83 23:37–25:35](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Selfish → customer-first | back-of-box feature list → USP shown + objections answered | [L74 05:25–06:44](../lessons/074-fixing-bad-static-ads-2.md); [L73 06:25–07:19](../lessons/073-fixing-bad-static-ads-10-51.md) |
Every move with its examples: [static rewrite moves](../frameworks/static-rewrite-moves.md); copy theory: [static copy levers](../concepts/static-copy-levers.md).

### Compliance on fix moves (don't execute → compliant)
| Course "after" example | Problem | Compliant version | Source |
|---|---|---|---|
| "clearing out our last 200 pairs before summer ends" | Invented stock number | Use a real stock or deadline fact with a true reason; otherwise no urgency | [L74 01:18](../lessons/074-fixing-bad-static-ads-2.md) |
| Invented testimonial / expert quote in rewrites | Fabricated proof | Real review lifted from the brand's site with permission (the method L73 shows) or a real, named expert | [L73 00:58–01:27](../lessons/073-fixing-bad-static-ads-10-51.md); [L74](../lessons/074-fixing-bad-static-ads-2.md) |
| "Sells out fast" | Unverifiable | Show real sell-out evidence or remove | [L75 03:56–04:26](../lessons/075-fixing-bad-static-ads-3.md) |
| 1:1 recreation of a competitor static / its background | Asset copying | Recreate the layout logic only; new image, new copy, our claims | [L71 03:38–04:42](../lessons/071-making-statics-with-ai.md); [L76](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| Health outcome headlines (belly fat, DHT) | Unsubstantiated claims | Substantiate or use a non-outcome angle | [L75](../lessons/075-fixing-bad-static-ads-3.md); [AI creator compliance](../concepts/ai-creator-compliance.md) |

## Step 13: test plan
- Test formats, not wording: three versions that differ in headline concept, colour and body copy at minimum; best is one ad per format [L08 01:56–02:43](../lessons/008-how-to-make-diversified-ads.md).
- Useful A/B pairs from the roasts: clean static without CTA button vs current format [L83 25:35](../lessons/083-ad-roast-calls-2026-08-17.md); product-free (ingredient/mug) vs product-shot static, product-light visuals "draw curiosity" (instructor claim) [L84 06:23](../lessons/084-ad-roast-calls-2026-08-21.md); urgency/offer version vs benefit-led for very aware audiences [L75 05:39](../lessons/075-fixing-bad-static-ads-3.md).
- Page fit: a high-CTR, education-needing static sent to a thin PDP converts poorly; send it to an educating page where each image works as a mini-ad (headline, ingredients, offer, objections) [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md). Build that page with the [write-landing-page skill](../../../../../../.claude/skills/write-landing-page/SKILL.md).
- Read outbound CTR [L78 00:52–01:51](../lessons/078-wine-brand-125k-at-2-24-roas.md); KPIs and breakeven: [KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md). After the readout: MORE / BETTER / NEW [L94 01:30](../lessons/094-research-protocol-start-here.md). Archive winners as templates [L76 08:19](../lessons/076-new-make-static-ads-with-ai-poppy-method.md).

## Conflicts and defaults
| Topic | This course | Other source | Default |
|---|---|---|---|
| Headline length | Headline Bank prompt: "6–10 words max" [L70 page prompt](../lessons/070-full-static-ads-creation-process.md) | Shared static playbook: 4–7 words, ≤3 lines ([static ad creation](../../../../playbooks/static-ad-creation.md)) | Aim 4–7; allow up to 10 only if it reads in one second on a phone |
| Text density | "Brochure effect": dense benefit text works when the promise matches a felt need [L74 07:23](../lessons/074-fixing-bad-static-ads-2.md) | ≤3 call-outs (shared playbook); rule of one thing [L84 05:24](../lessons/084-ad-roast-calls-2026-08-21.md) | One message per static; test a dense "brochure" version only for problem-aware audiences with a strong felt need |
| AI imagery | AI product images in templates [L71](../lessons/071-making-statics-with-ai.md); AI-generated statics at scale [L76](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) | Shared playbook treats AI images as novelty and prefers real shoot assets | AI scene images allowed when the product render matches the real pack exactly; real product photos win any tie |
| Run time as a signal | L76 imports "Longest running" references [L76 01:50–02:48](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) | "That is the worst thing that you can do" [L100 00:00](../lessons/100-why-copying-longest-running-is-bad.md) | Shortlist by spend ([ad-spend signal](../concepts/ad-spend-signal.md)); use long-running ads only as layout references |

## Deliverables template
```markdown
## <Product> — AI static batch <n>
**Avatar:** <one line> · **Mass desire:** <…> · **Awareness levels covered:** <…> · **Offer (exact):** "<…>"
**missing_inputs:** [...] · **verify_before_launch:** [...]

### 1. Copy sheet (the "script")
| ID | Format / template | Awareness | Headline | First line / sub | Benefits or call-outs | Proof element (source) | CTA |
|---|---|---|---|---|---|---|---|

### 2. Prompt pack
| ID | Image model | Product refs used | Prompt (verbatim, incl. "Keep everything else the same") | Edit instructions applied |
|---|---|---|---|---|

### 3. Reference list
| Ref | Type (concept ref / layout ref / product photo / brand kit) | Source + spend or rights | Mechanism borrowed (not asset) |
|---|---|---|---|

### 4. Review / QA log
| ID | Pack shape | Label text | Orientation | Contrast at phone size | Typos | Claims audited | Verdict |
|---|---|---|---|---|---|---|---|

### 5. Test plan
| Ad | Differs by (format / concept / image) | Hypothesis | Metric | Read after | Landing page |
|---|---|---|---|---|---|
Upload PAUSED · Approver: <role> · Roast scorecard per ad: H/C/S/E /20 · Compliance line: pass/fail
```

## Where it's taught
[L08 00:03–02:43](../lessons/008-how-to-make-diversified-ads.md) · [L69 00:00](../lessons/069-static-ads-intro.md) · [L70 00:00–09:46](../lessons/070-full-static-ads-creation-process.md) · [L71 00:00–04:42](../lessons/071-making-statics-with-ai.md) · [L72 00:00–04:13](../lessons/072-static-ads-mistakes-to-avoid-4-17.md) · [L73 00:00–10:38](../lessons/073-fixing-bad-static-ads-10-51.md) · [L74 00:25–08:57](../lessons/074-fixing-bad-static-ads-2.md) · [L75 00:00–07:42](../lessons/075-fixing-bad-static-ads-3.md) · [L76 00:00–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) · roasts [L83 21:53–29:59](../lessons/083-ad-roast-calls-2026-08-17.md), [L84 01:34–08:13](../lessons/084-ad-roast-calls-2026-08-21.md)

## Cross-course notes
- **Tether Lab (shared):** [static ad creation](../../../../playbooks/static-ad-creation.md) owns layout (visual-weight map, headline hierarchy); this playbook adds the AI image workflow and the awareness-level copy bank. Conflicts in the table above.
- **Evolve Copywriting:** [write static image ads](../../../evolve/copywriting/playbooks/write-static-image-ads.md) and [static ad workflow](../../../evolve/copywriting/frameworks/static-ad-workflow.md); [market awareness](../../../evolve/copywriting/concepts/market-awareness.md) places some stages differently from L95 (see [research playbook](research-to-ai-ad-concepts.md#conflicts-and-defaults)).
- **RMBC II:** the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) is the gate for every AI-written headline bank.
