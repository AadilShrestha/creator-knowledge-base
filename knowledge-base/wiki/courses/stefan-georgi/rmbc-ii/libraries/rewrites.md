---
title: "Rewrites library: RMBC II (before → after edits, tagged by change type and claim risk)"
type: library
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests David O'Connell (12-03), Max Finn (12-04)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-03-vsl-leads-after-the-opening-hook.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-04-vsl-background-stories-and-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-06-vsl-closes.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-08-medium-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-09-short-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-04-blood-sugar-supplement-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-03-google-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-04-tiktok-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-02-upsells-case-studies.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
tags: [library, rewrites, copy-editing, llm-copy-chief, vsl, advertorial, upsell, compliance, rmbc-ii]
updated: 2026-11-02
---

# Rewrites library: RMBC II

> Every before → after edit in RMBC II (96 harvested rows → 96 entries): Stefan's copy-chief edits to Claude drafts, structure swaps, hook and lead fixes, offer and claim edits, and guest edits to ads, tagged by change type, niche, asset, awareness, length band and claim risk.

## 🤖 Agent use
- **Use when:** editing an LLM draft as copy chief, fixing a weak hook, lead, mechanism name, close or upsell, or explaining to a user why a line should change.
- **Inputs → outputs:** a draft line or section → find rows with the same `Change type` and `Asset` → apply the same move to our line → re-run the claim check.
- **Rules:**
  - **DO** make one change type per edit and name it (verb / visual / promise / self / intensity / structure / claim / offer / mechanism / speaker / length / audience).
  - **DO** cut assumptions about the reader's state ("where you are right now" → "where a lot of people probably are"). [07-01 v5 24:56](../lessons/07-01-long-form-vsl.md)
  - **DO** prefer plain mechanism names over jargon ("Dermal Disarray" → "Collagen Architecture Breakdown"). [03-04 1:08:25–1:10:45](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md)
  - **DO** quote the bad line back to the model and say why it is wrong; that is Stefan's feedback turn. [14-03 03:09](../lessons/14-03-claude-projects-for-upsells.md)
  - **DON'T** treat a softer claim as a compliant claim: "reversing diabetes" → "rapidly lowering blood sugar" still needs substantiation. [07-01 v6 09:35–11:00](../lessons/07-01-long-form-vsl.md)
  - **DON'T** reuse the "after" text of any `do not reuse` row; reuse only the edit move.
  - **IF** scarcity is moved into a script (R090) **THEN** it must be literally true. [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md)
- **See also:** [llm-copy-chief-editing](../concepts/llm-copy-chief-editing.md) · [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) · [hooks](hooks.md) · [templates](templates.md) · [Evolve rewrites](../../../evolve/copywriting/libraries/rewrites.md) · [Tether rewrites](../../../../libraries/rewrites.md)

## How to filter this page

| Column | Values used |
|---|---|
| Change type | verb · visual · promise · self · intensity · structure · claim · offer · mechanism · speaker · length · audience · bridge |
| Niche | skincare · blood sugar · edema device · weight loss · biz-op · financial newsletter · acne · fitness · education · eyewear · dental · supplement (general) · n/a |
| Asset | hook · lead · mechanism name · background story · close · CTA · VSL outline · short VSL · brief · advertorial · upsell script · search/display ad · TikTok ad · guarantee |
| Awareness | unaware · problem · solution · product · most (derived from the asset's audience) |
| Length band | static · ≤60 s · short 1–4 min · 3–7 min · medium 6–16 min · long 25–60 min · page · n/a |
| Claim risk | none · substantiation needed · do not reuse (structure only; claims not reusable) |

Grep tips: `grep "| mechanism |" rewrites.md`, `grep "| upsell script |" rewrites.md`, `grep "| do not reuse |" rewrites.md`.

---

## 1. Mechanism naming and the UMP/UMS (modules 03–04)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R001 | "You're trying to solve an asset gap problem with an income gap solution"; "jump from the income gap world into the asset gap world" (V1) | "You think you have an income problem. But what you really have is an asset problem." "You can't earn your way to wealth. You have to own your way to wealth." (V2) | Two-worlds metaphor → a diagnosis the prospect can accept, plus a plain proof line | mechanism | biz-op | mechanism name | problem | n/a | none | — | [03-03 22:44; 25:25–31:56](../lessons/03-03-ump-evaluation-prompt-and-process-airbnb-arbitrage.md) |
| R002 | "Dermal Disarray" (tent poles collapse) | "Collagen Architecture Breakdown" (fabric loses its tight weave) | Technical name → plainer one; metaphor chosen for the target woman ("grandma knitting") | mechanism | skincare | mechanism name | solution | n/a | substantiation needed | Mechanism must match real ingredient science | [03-04 1:08:25–1:10:45](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| R003 | "Bio-Tensegrity" signal (UMS 1) | "Structural Renewal System" (Structural Renewal Signal) | Jargon → plain "system" term | mechanism | skincare | mechanism name | solution | n/a | none | — | [03-04 1:14:21–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| R004 | "Smart Materials" (amino acids) | "Targeted Repair Complex" | Metaphor-free, ingredient-led label | mechanism | skincare | mechanism name | solution | n/a | none | — | [03-04 1:14:53](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| R005 | "Protective Shield" | "Integrity Locking Compounds" | Generic term replaced | mechanism | skincare | mechanism name | solution | n/a | none | — | [03-04 1:14:21–1:17:47](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| R006 | "The reason your peptide eye creams haven't worked..." | Rewritten for readers who know "eye creams", not "peptide eye creams" | Removed an awareness assumption | audience | skincare | hook | solution | n/a | none | — | [03-04 1:07:06–1:08:25](../lessons/03-04-ideation-validation-and-expansion-walkthrough-eye-serum-exam.md) |
| R007 | Medium VSL opening A: "Say goodbye to edema in your legs…" | Opening B: "This is why people with edema are switching to this genius affordable device. Doing this can make your edema worse. Here's how to solve it." | Promise → warning + switching proof; mechanism moved into the first 30 s; root script unchanged | structure | edema device | hook | problem → solution | medium 6–16 min | substantiation needed | "Switching" needs real data | [04-02 03:05–06:06](../lessons/04-02-vsl-fundamentals-classic-structure.md) |
| R008 | Medium VSL opening B (2 hooks + mechanism) | Mini opening: "Lifting your legs up is the best way… right? Nope." | Dropped credentials and discovery; opens on the remedy debunk | length | edema device | hook | solution | 3–7 min | substantiation needed | — | [04-02 mini #2 doc](../lessons/04-02-vsl-fundamentals-classic-structure.md) |
| R009 | (Beverly Hills lead has no story tease) | "...you're going to be amazed when you see what happened when one of my patients, Linda, used this... I'll share Linda's whole story in just a moment" | Added a tease of the emotional story and a named patient | structure | skincare | lead | problem | long 25–60 min | do not reuse | Named patient must be real and consenting | [04-03 33:05–33:37](../lessons/04-03-vsl-leads-after-the-opening-hook.md) |
| R010 | (same lead, no skepticism line) | "I know it might sound hard to believe this has worked for thousands of women, including a patient of mine named Linda" | Skepticism line + testimonial-style proof in one sentence | structure | skincare | lead | problem | long 25–60 min | do not reuse | "Thousands of women" needs data | [04-03 33:37](../lessons/04-03-vsl-leads-after-the-opening-hook.md) |
| R011 | "a riot going on in your skin" (member's eczema draft) | "a silent, quiet war happening in your skin" / "the invisible war happening on the surface of your skin" | Abstract image → tangible, intuitive one | visual | skincare (eczema) | lead | problem | n/a | none | — | [04-03 44:55–45:52](../lessons/04-03-vsl-leads-after-the-opening-hook.md) |
| R012 | "the metabolism you had when you were young" (older demo) | "the metabolism of your annoyingly skinny friend" (younger demo) | Self comparison → relatable peer, works if the viewer was never skinny | self | weight loss | lead | problem | n/a | none | — | [04-03 41:47–42:14](../lessons/04-03-vsl-leads-after-the-opening-hook.md) |
| R013 | "get back to the metabolism you used to have" (assumes she used to be skinny) | "it's gotten harder since you've gotten older, like after childbirth" (paraphrase) | Removes the "once skinny" assumption | self | weight loss | lead | problem | n/a | none | — | [04-03 40:53–41:20](../lessons/04-03-vsl-leads-after-the-opening-hook.md) |
| R014 | Spokesperson tells their own story with no reference to the viewer | Check-ins: "So I don't know what you think about [the employer], but for a kid like me... Have you ever been in a job like that? Maybe you're in a job like that right now..." | Adds viewer reference to cure "I-syndrome" | self | biz-op | background story | problem | long 25–60 min | none | — | [04-04 50:26–51:25](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) |
| R015 | Mechanism with many invented intermediaries ("BH51... mitochondria... lymphatic... gut") | "DHT is a hormone that destroys collagen in your skin, makes it sag, and gets worse in menopause" | Reduced to two sentences a viewer can repeat | mechanism | skincare | mechanism name | problem | n/a | substantiation needed | Hormone claim needs sources | [04-04 51:54–52:51](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) |

## 2. Closes, offers and guarantees (04-06)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R016 | Six-bottle pitch run as paragraphs of hard sell before the button | "Instead of $69 per bottle... the six month package... what our smartest customers buy, it's just $49 per package... pick whatever package is best for you" | Short AOV reason then immediate CTA; single-unit buyers still invited | offer | supplement (general) | close | product | long 25–60 min | none | Use our real prices | [04-06 14:11–14:38](../lessons/04-06-vsl-closes.md) |
| R017 | Nooro "special offer... 50% discount" (price withheld) | Test showing the price vs only the discount | Price clarity vs curiosity; "seen it both ways" | offer | edema device | close | product | medium 6–16 min | none | Test, no default | [04-06 25:50; 38:14–38:42](../lessons/04-06-vsl-closes.md) |
| R018 | Nooro: "smart people buy more" appears late | Bigger-discount line near the first CTA | Raise AOV at the first ask | structure | edema device | close | product | medium 6–16 min | none | — | [04-06 26:19; 27:16](../lessons/04-06-vsl-closes.md) |
| R019 | "Trial" in the guarantee | "Guarantee", or test the wording | "Trial" can read as an auto-bill | verb | edema device | guarantee | product | n/a | none | — | [04-06 29:36](../lessons/04-06-vsl-closes.md) |
| R020 | "Thank you for watching" ending | Final CTA after the testimonials ("it's John again... click the button") | Last-chance ask after FAQ or social proof | structure | weight loss (info) | CTA | product | long 25–60 min | none | — | [04-06 1:01:54](../lessons/04-06-vsl-closes.md) |

## 3. Big ideas, leads and dimensionalisation (04-07 to 04-10)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R021 | "The new gold rush Trump just unlocked" (what a lesser writer would lead with) | "America's secret trust fund... American birthright" (the actual lead) | Literal mechanism → bigger metaphor that "can breathe" and later unwinds | promise | financial newsletter | lead | unaware | long 25–60 min | do not reuse | Wealth promise; copy the metaphor-first move only | [04-07 1:00:54–1:01:54](../lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md) |
| R022 | "$150 trillion" | "Enough to pay off the national debt four times over... a $1.1 million check per household" | Abstract number → relatable comparisons | visual | financial newsletter | lead | unaware | long 25–60 min | substantiation needed | Comparisons must compute from a real figure | [04-07 24:29–25:11; 29:50](../lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md) |
| R023 | "Fund" | "Asset" (as the piece moves on) | Language shifts quietly as the metaphor unwinds | verb | financial newsletter | VSL body | unaware | long 25–60 min | none | — | [04-07 39:54–40:24; 43:42](../lessons/04-07-long-form-financial-vsl-examples-and-break-downs.md) |
| R024 | Classic lead: ten support points | Four: Call Out Problem / Promise Solution / Educational Component / Contrarian Nature | Cut to four jobs; "educational component" added | structure | edema device | lead | problem | medium 6–16 min | none | — | [04-08 frame 13:54; v2 07:00–09:38](../lessons/04-08-medium-vsls-structures-and-examples.md) |
| R025 | Classic UMP: "should be surprising, possibly even counterintuitive; backed by credibility and proof" | "Explains the root cause in simple, step-by-step detail… a small amount of new information… band-aids, you need surgery" + "Expand the pain point" | Simplified; pain expansion added | structure | edema device | VSL outline | problem | medium 6–16 min | none | — | [04-08 frames 24:24, 47:19; v2 18:08](../lessons/04-08-medium-vsls-structures-and-examples.md) |
| R026 | Classic UMS, then Product Build-Up and Reveal | "Introduce Product AS the Unique Mechanism of the Solution" (Nooro) or "Product Education" + four-line build-up (MiamiMD) | Merged / reordered | structure | edema device; skincare | VSL outline | solution | medium 6–16 min | none | — | [04-08 frames 24:24, 20:54; v2 19:55; v3 15:49](../lessons/04-08-medium-vsls-structures-and-examples.md) |
| R027 | Classic close, ten items | Nooro: future pacing ×4 + objections + crossroads. MiamiMD: testimonials with jobs, AOV tease, two CTAs, "may never see again" | Close re-centred on imagination and objections | structure | edema device; skincare | close | product | medium 6–16 min | none | — | [04-08 frames 35:25–46:19, 29:24–33:18](../lessons/04-08-medium-vsls-structures-and-examples.md) |
| R028 | Claude outline of Epic Real Estate: contrarian hook, authority/opportunity, teased "paper flipping" | Hook; expert-guided transformation story; introduce UMS; explain UMS; future pace; "can't teach it all"; urgent CTA; remind; final CTA | Added "explain the mechanism"; dropped the contrarian frame | structure | real estate | short VSL | solution | short 1–4 min | substantiation needed | Income results need disclosure | [04-09 v2 21:45–27:09](../lessons/04-09-short-vsls-structures-and-examples.md) |
| R029 | Amazon Automation: contrarian #2 "challenging conventional wisdom / personal story authority" | Ten-step Biz Opp Contrarian Structure (hook, opportunity, method, business model, objections, qualification, bridge, urgency, risk reversal, final CTA) | Rebuilt from the ad itself, then generalised | structure | biz-op | short VSL | solution | short 1–4 min | substantiation needed | — | [04-09 v2 32:28–38:21](../lessons/04-09-short-vsls-structures-and-examples.md) |
| R030 | Cat product: older "before / after" outline | Structure #3 with 4A product path and 4B method path | One template handles product sales and info teasers | structure | pet odor | short VSL | problem | short 1–4 min | none | — | [04-09 v2 54:46–58:22](../lessons/04-09-short-vsls-structures-and-examples.md) |
| R031 | "These three foods are triggering your skin's aging time bomb. Your skin's aging accelerator might be in your kitchen right now." | "This aging starter for your skin might be in your kitchen right now." | Wording and flow; "just doesn't like the idea of an aging time bomb" | intensity | skincare | hook | problem | short 1–4 min | substantiation needed | — | [04-10 52:30](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| R032 | Woman says the night-routine hook | Doctor says it | Speaker swapped to the expert | speaker | skincare | hook | problem | short 1–4 min | substantiation needed | Real expert only | [04-10 54:02](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| R033 | Hooks written as closed-loop fascination bullets | Fragments with open loops ("first half of a puzzle") | Output format requested from the model | structure | skincare | hook | n/a | n/a | none | — | [04-10 38:26–39:22](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |

## 4. Briefs (module 05)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R034 | CTA "save 57% off their order when they visit the website" | CTA to "save 57% off to get more information" | Sell the next step (watch/learn), not the product | offer | skincare | CTA | solution | 3–7 min | none | Second thought; not run | [05-02 43:17](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| R035 | Brief pricing with subscribe-and-save in the VSL | One-time pricing in the VSL; subscribe-and-save below the VSL | Simpler offer in the video | offer | skincare | brief | product | n/a | none | — | [05-02 19:03](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| R036 | Main speaker placeholder | Laura narrates what Dr. Schilling explained | First-person narrator plus an expert for UMP/UMS | speaker | skincare | brief | solution | n/a | do not reuse | Fictional doctor in the course; use a real expert or none | [05-02 19:03–20:19](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| R037 | V1: narrator Sarah (caregiver) meets an unnamed endocrinologist | V2: narrator is the endocrinologist; patient "Margaret" second speaker | Speaker/perspective and arc; same mechanism | speaker | blood sugar | brief | problem | n/a | do not reuse | Fictional doctor and patient | [05-04 10:53–15:17](../lessons/05-04-blood-sugar-supplement-example.md) |
| R038 | V1 audience "Women aged 45-65" | V2 "Adults aged 40-70" | Broadened to women and men | audience | blood sugar | brief | problem | n/a | none | — | [05-04 01:38–02:12](../lessons/05-04-blood-sugar-supplement-example.md) |
| R039 | V1 solution: 3 mechanism actions | V2: 4 actions (adds mitochondrial function) | Mechanism expanded; UMS "same" | mechanism | blood sugar | brief | problem | n/a | substantiation needed | — | [05-04 V2 field 6; 13:47](../lessons/05-04-blood-sugar-supplement-example.md) |
| R040 | Promise: "Discover the secret investment strategy that Wall Street doesn't want you to know about" ("a little boring and generic") | "Find out which three tiny companies hold the 'master patents' to the medical revolution" | Specific, curiosity-driven, named mechanism, countable payoff | promise | financial newsletter | brief | unaware | n/a | substantiation needed | — | [05-05 05:19; 09:01](../lessons/05-05-financial-promo-example.md) |
| R041 | "consistent 15-25% annual returns regardless of market conditions" | "Collect 'genetic royalties' on every cure created" | Return promise → mechanism promise (less claim-heavy, still needs compliance review) | claim | financial newsletter | brief | unaware | n/a | substantiation needed | Never promise returns | [05-05 05:48; 08:56](../lessons/05-05-financial-promo-example.md) |

## 5. VSL drafts with Claude (module 07)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R042 | Brief: "The hooks that connect your skin layers at the DEJ break down and disappear." | Deleted | Removed an image that clashes with the weave metaphor | mechanism | skincare | brief | solution | long 25–60 min | none | One metaphor per mechanism | [07-01 v1 00:58](../lessons/07-01-long-form-vsl.md) |
| R043 | Teasers built on a "DEJ breakthrough" | Teasers on the "Structural Renewal System" / collagen architecture breakdown; DEJ only as where it starts | Jargon → metaphor | mechanism | skincare | lead | solution | long 25–60 min | none | — | [07-01 v1 05:31–10:26](../lessons/07-01-long-form-vsl.md) |
| R044 | Brief with "Big ideas to test" and hooks | Both removed | Stops the model anchoring; leads written separately | structure | skincare | brief | n/a | long 25–60 min | none | — | [07-01 v1 10:26–11:31](../lessons/07-01-long-form-vsl.md) |
| R045 | Outline lead includes Laura's story and Dr. Schilling | Lead only teases a "Florida mom" and an "anti-aging doctor"; brand unnamed until after build-up | Keeps curiosity | structure | skincare | VSL outline | solution | long 25–60 min | none | — | [07-01 v1 31:13–32:48](../lessons/07-01-long-form-vsl.md) |
| R046 | Outline: no link between Laura and the doctor | "Search for truth led her to meet Dr. Schilling… referred by a friend… Laura recounting what he told her" | Fixes who speaks and why the doctor appears | bridge | skincare | VSL outline | solution | long 25–60 min | none | — | [07-01 v1 36:45; 37:23](../lessons/07-01-long-form-vsl.md) |
| R047 | Build-up grounds steps 1–2 only | Steps 1–3 each have ingredients; amino acids added; repeated in the close | Makes the system complete | mechanism | skincare | VSL body | solution | long 25–60 min | substantiation needed | — | [07-01 v3 26:53–30:59](../lessons/07-01-long-form-vsl.md) |
| R048 | Airbnb hook: "twice as hard and twice as educated" | "twice as educated" removed | Don't narrow the audience to degree holders | audience | biz-op | hook | problem | long 25–60 min | none | — | [07-01 v5 15:59](../lessons/07-01-long-form-vsl.md) |
| R049 | "trapped in the corporate rat race… where you are right now" | "where a lot of people… probably are right now" | Avoid asserting the viewer's state | self | biz-op | VSL body | problem | long 25–60 min | none | — | [07-01 v5 24:56](../lessons/07-01-long-form-vsl.md) |
| R050 | Airbnb: furnishing step | Removed ("plenty of properties will come furnished") | Removes a cost objection | structure | biz-op | VSL body | solution | long 25–60 min | none | — | [07-01 v5 43:25](../lessons/07-01-long-form-vsl.md) |
| R051 | "reversing diabetes in thousands of Americans" | "rapidly lowering blood sugar… thousands of Americans with diabetes" | More defensible; still needs substantiation | claim | blood sugar | hook | problem | long 25–60 min | do not reuse | Both versions are disease claims for a supplement | [07-01 v6 09:35–11:00](../lessons/07-01-long-form-vsl.md) |
| R052 | "golden spice" | "I'm not talking about turmeric" added | Pre-empts the obvious guess | promise | blood sugar | VSL body | problem | long 25–60 min | none | — | [07-01 v6 16:06](../lessons/07-01-long-form-vsl.md) |
| R053 | Laura-narrated 18-min script (founder quotes Dr. Schilling) | Dr. Schilling narrates; patient "Maria" supplies the story; opens "I'm not a dermatologist…" | Spokesperson, background story, outsider-expert credibility | speaker | skincare | VSL outline | solution | medium 6–16 min | do not reuse | Fictional expert | [07-02 v1 03:16–07:58](../lessons/07-02-medium-length-vsl.md) |
| R054 | First outline: opening hook → … → failed-solutions analysis | 10-block classic structure with timings | Re-arranged against the classic reference | structure | skincare | VSL outline | solution | medium 6–16 min | none | — | [07-02 v1 08:48; 12:11](../lessons/07-02-medium-length-vsl.md) |
| R055 | Micro lead ending "The one I'm about to share with you will change everything." | Adds "In this brief presentation, I will give you the key to making your outer appearance finally match how you feel inside…", a three-item promise list and "see the vibrant, confident, and beautiful woman you know you are" | Explicit promise + future pace | promise | skincare | lead | solution | medium 6–16 min | substantiation needed | Promise list must match evidence | [07-02 v1 12:51; 28:58](../lessons/07-02-medium-length-vsl.md) |
| R056 | Airbnb long VSL (book-a-call) | 16–18 min cut: same openings, qualification/CTA 4–5 → 3–4 min | Trimmed blocks, kept every beat | length | biz-op | VSL outline | problem | medium 6–16 min | none | — | [07-02 v2 08:04](../lessons/07-02-medium-length-vsl.md) |
| R057 | Abrupt jump from "systems and automation" to objections | "this sounds almost too good to be true… so let me address the questions that are probably going through your head" | Added a bridge ("Natural Transition") | bridge | biz-op | VSL body | problem | medium 6–16 min | none | — | [07-02 v2 13:05–14:18](../lessons/07-02-medium-length-vsl.md) |
| R058 | "...price doesn't matter - approach does." | "...price doesn't matter - THIS is much more important." | Vague abstraction → pointing word that opens a curiosity gap | verb | skincare | hook | solution | 3–7 min | none | — | [07-03 v1 03:54 vs 04:53](../lessons/07-03-3-7-minute-vsl.md) |
| R059 | Nope sequence: "You think eating too much sugar causes diabetes, right? Nope. What about not exercising enough? Nope. How about genetics…? Still nope." | "You think fragrance-free cleaners are safe, right? Nope. What about 'natural' cleaning products? Nope. How about those eco-friendly laundry pods? Still nope." | Removed implausible denial; all items inside the hook's villain category | structure | blood sugar | hook | unaware | 3–7 min | do not reuse | After-version still carries an unsupported health link | [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md) |
| R060 | Outline built without the brief | Same outline; Revelation/Education + Proof + CTA rewritten to the brief | Attach the brief and lock earlier sections | structure | blood sugar | VSL outline | problem | 3–7 min | none | — | [07-03 v2 04:37–06:35](../lessons/07-03-3-7-minute-vsl.md) |
| R061 | 3:30 script | 1:30 script | Hook kept; problem merged with authority; mechanism compressed | length | skincare | short VSL | solution | short 1–4 min | substantiation needed | — | [07-03 docx pair](../lessons/07-03-3-7-minute-vsl.md) |
| R062 | Golden spice described only as "precious golden spice" | "…And no, it's not turmeric." | Pre-empts category confusion | promise | blood sugar | short VSL | problem | 3–7 min | none | — | [07-03 v2 07:06](../lessons/07-03-3-7-minute-vsl.md) |
| R063 | "Your makeup artist can tell your real age just by looking at your eyes" | "Here's why makeup artists can tell your real age just by looking at your eyes" | Self (not everyone has a makeup artist); frames an explanation to come | self | skincare | hook | problem | 3–7 min | none | — | [07-04 v1 04:17](../lessons/07-04-short-vsl.md) |
| R064 | "...an ancient Himalayan rice preparation ritual..." | "...an ancient Himalayan rice ritual..." | Phrase tightened | length | blood sugar | short VSL | problem | ≤60 s | none | — | [07-04 v3 01:19](../lessons/07-04-short-vsl.md) |
| R065 | "...a specific golden spice with their rice for centuries - and they have virtually no diabetes despite eating high-carb diets." | Same + "I'm not talking about turmeric here. As a big natural health guy, this golden spice is something I never would have expected." | Negation + personal-surprise line raise curiosity | promise | blood sugar | short VSL | problem | ≤60 s | do not reuse | "Virtually no diabetes" is a disease claim | [07-04 v3 02:22](../lessons/07-04-short-vsl.md) |
| R066 | "What if your rent payment could be generating income for YOU instead?" | "...generating income for you instead of lining someone else's pocket." | Villain/contrast added; "more emotionally charged" | intensity | biz-op | hook | problem | short 1–4 min | substantiation needed | — | [07-04 v2 09:36–10:25](../lessons/07-04-short-vsl.md) |
| R067 | Concept 3 draft explains Big Pharma's "keep you sick" model before the FDA news | Revised: teases the FDA decision, the opportunity and consequences without explaining | Tease level raised | intensity | financial newsletter | short VSL | unaware | short 1–4 min | do not reuse | "Keep you sick" conspiracy claim | [07-04 v4 08:10–09:47](../lessons/07-04-short-vsl.md) |
| R068 | "...the FDA made a quiet announcement three weeks ago" | "recent" instead of "three weeks" | Specific time claim → vaguer claim | claim | financial newsletter | short VSL | unaware | short 1–4 min | substantiation needed | The announcement must exist | [07-04 v4 14:09](../lessons/07-04-short-vsl.md) |

## 6. Advertorials (09-02)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R069 | Arctic draft: "Big Pharma doesn't want you to know" | "major skincare companies don't want you to know about this natural breakthrough" | Enemy matched to the product category | self | acne | advertorial | problem | page | substantiation needed | — | [09-02 49:51–50:27](../lessons/09-02-claude-project-for-advertorials.md) |
| R070 | Researcher finds plants, then tests acne bacteria (no reason) | Researcher's two teenage sons have severe acne; "What if nature had already solved this problem thousands of years ago?" | Motive and emotional stake added | structure | acne | advertorial | problem | page | do not reuse | Invented researcher story; only a real founder story | [09-02 50:27–52:41; 54:52](../lessons/09-02-claude-project-for-advertorials.md) |
| R071 | Medium "Mom Shocked" draft | ~50% shorter, same headline and beats | Cuts medical-failure detail and science; keeps scene, timeline, guarantee | length | acne | advertorial | problem | page | do not reuse | "90% clear in one week" headline is invented | [09-02 41:19–44:02](../lessons/09-02-claude-project-for-advertorials.md) |
| R072 | Long written testimonial section | Screenshot-style testimonials/pictures | Shorter, more credible format | visual | acne | advertorial | problem | page | substantiation needed | Real screenshots only | [09-02 37:37–38:01](../lessons/09-02-claude-project-for-advertorials.md) |
| R073 | Arctic draft at full length | "About 20% shorter" | Loose length target ("about", so 24% or 26% is fine) | length | acne | advertorial | problem | page | none | — | [09-02 50:27](../lessons/09-02-claude-project-for-advertorials.md) |

## 7. Paid ads: Google and TikTok (guests)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R074 | "50% off for one week only" | "50% off for a limited time" | Clearer meaning; say it only if the promo is really time-limited (derived) | claim | supplement (greens) | search/display ad | product | static | none | — | [12-03 v3 19:03](../lessons/12-03-google-ads.md) (guest) |
| R075 | "Try our plan" | "Stop yo-yo dieting for good" | Names a pain and an end state | promise | fitness | search/display ad | problem | static | substantiation needed | — | [12-03 v3 13:35](../lessons/12-03-google-ads.md) (guest) |
| R076 | Competitor guitar search ads: "at home", "private lessons $20/hr", "free first lesson in store" | "Instant Online Guitar Lessons (start learning from home now!)", "Get your first lesson free", "Learn from (professional musician name)", "You'll learn in 30 days or you won't pay" | Speed, free trial, authority, risk reversal; no competitor had all four | offer | education | search/display ad | solution | static | substantiation needed | Musician name real; guarantee honoured | [12-03 v2 13:12–14:59](../lessons/12-03-google-ads.md) (guest) |
| R077 | Shopping title "Ray-Ban Aviators" | "Polarized Ray-Ban Aviators", or "Best Aviators of 2025" (tests) | Keyword/spec detail or a "best of" frame | promise | eyewear | search/display ad | product | static | none | — | [12-03 v4 10:38](../lessons/12-03-google-ads.md) (guest) |
| R078 | Product on white background | Same product on bright yellow/green/red | Visual contrast in the Shopping grid | visual | eyewear | search/display ad | product | static | none | — | [12-03 v4 09:40](../lessons/12-03-google-ads.md) (guest) |
| R079 | One-minute emotional ad ending on the patient crying | Same ad opened on the crying scene; end loops into the start | Payoff moved to the scroll-stop slot | structure | dental | TikTok ad | solution | ≤60 s | substantiation needed | Real patient consent | [12-04 v6 05:43–06:13](../lessons/12-04-tiktok-ads.md) (guest) |
| R080 | Emotional ad with no business face | Version with the dentist on green screen + the crying visual | Authority face + proven format + scroll-stop visual | speaker | dental | TikTok ad | solution | ≤60 s | none | — | [12-04 v6 06:41–07:10](../lessons/12-04-tiktok-ads.md) (guest) |
| R081 | Offer scene: free shipping | Discount, or a bonus stack | Offer scene swapped; three ads | offer | supplement (general) | TikTok ad | product | ≤60 s | none | — | [12-04 v6 04:21–04:49](../lessons/12-04-tiktok-ads.md) (guest) |
| R082 | Problem scene: one framing | Problem shown another way, or a different alternative solution | One scene swapped, rest constant | structure | supplement (general) | TikTok ad | problem | ≤60 s | none | — | [12-04 v6 03:51–04:21](../lessons/12-04-tiktok-ads.md) (guest) |
| R083 | Normal talking video with the product in hand | Problem/solution pairs with colourful props | Visual illustration of each claim | visual | supplement (general) | TikTok ad | problem | ≤60 s | substantiation needed | — | [12-04 BD4 srt 01:20–02:20](../lessons/12-04-tiktok-ads.md) (guest) |
| R084 | Hard "click to buy now" ask | Soft "here's the link if you want to check it out" (description, not a script) | Intensity reduced | intensity | oral care | TikTok ad | product | ≤60 s | none | — | [12-04 v7 10:00–10:32](../lessons/12-04-tiktok-ads.md) (guest) |

## 8. Upsell scripts (14-02, 14-03)

| ID | Before | After | What changed | Change type | Niche | Asset | Awareness | Length band | Claim risk | Note | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R085 | "Dr. Hoffman here..." | "Hey it's Kristi here... on behalf of myself, Dr. Hoffman, and everyone at FitSpresso" | Self: a named team member introduces; doctor as co-sponsor | speaker | weight loss | upsell script | most | medium 6–16 min | substantiation needed | Doctor must be real | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R086 | Three named customers with one-line results | Three customers + "-Before/After-" image slots, a food detail (pasta, tiramisu) and a "THIS CLOSE to dropping $1,600 a month on Ozempic" story | Visual proof slots, specificity, competing-solution anchor | visual | weight loss | upsell script | most | medium 6–16 min | do not reuse | Drug comparison + named customers; real permissioned testimonials only | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R087 | "complete transformation within the first few days" | "By FINALLY making weight loss completely effortless (and even kind of fun)" + list of body areas | Promise reworded; intensity and specificity raised | promise | weight loss | upsell script | most | medium 6–16 min | do not reuse | "Effortless weight loss" | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R088 | A "secret discovery" story (Hollywood stars, Harvard study) and a research-failure story | Removed; "Here's The Truth: Fully Restoring Your Body's Natural Fat-Burning Rhythm Takes Time" | No new product to position since it is more of the same | structure | weight loss | upsell script | most | medium 6–16 min | substantiation needed | Mechanism line needs evidence | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R089 | Pack priced "$414 retail, $234 today, $660 less than retail" (414 − 234 = 180; doesn't reconcile) | "$149 PER bottle... $894... $29 per bottle... $174" + alternative-drug comparison | Consistent per-unit anchor | offer | weight loss | upsell script | most | medium 6–16 min | substantiation needed | Retail anchor must be a real price; drug comparison do not reuse | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R090 | Timer "ONLY AVAILABLE FOR THE NEXT 09:46", 3/6/12-month selector, decline sentence | Scarcity in the script: customers "saying YES... inventory plummeted... 3-6 months to restock" | Scarcity moved into the script | claim | weight loss | upsell script | most | medium 6–16 min | do not reuse | Only if literally true | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R091 | 180-day, email support@ guarantee | "100% Money Back Lifetime Guarantee" with call or email | Risk reversal strengthened | offer | weight loss | guarantee | most | n/a | substantiation needed | Only a guarantee we will honour | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R092 | First week "2-3 pounds"; month list placed late | "2-5 pounds"; month list before the offer under "what you can reasonably expect" | Position and intensity | intensity | weight loss | upsell script | most | medium 6–16 min | do not reuse | Specific weight-loss numbers | [14-02 FitSpresso docs](../lessons/14-02-upsells-case-studies.md) |
| R093 | "I'm absolutely thrilled that you just secured your Unity Eye Serum 6-Month Age-Reversal System... You've made two incredibly smart decisions today" | "I'm absolutely thrilled that you decided to invest in Unity Eye Serum today... You've made an incredibly smart decision" | Funnel logic: don't assume upsell 1 was bought | structure | skincare | upsell script | most | medium 6–16 min | none | — | [14-03 doc 3.1](../lessons/14-03-claude-projects-for-upsells.md) |
| R094 | "What most people don't realize is that your eyes are just one part of your face... You need to address aging on your ENTIRE face" | "What many people discover after seeing amazing results around their eyes is this... When one area of your face looks dramatically younger, it can actually highlight aging in other areas" | Claim made credible (observation, not "most people don't realize") | claim | skincare | upsell script | most | medium 6–16 min | substantiation needed | "Amazing results" needs evidence | [14-03 doc 3.1; 03:09](../lessons/14-03-claude-projects-for-upsells.md) |
| R095 | Contrast copy with a "restored vintage car with a dented body" analogy | "Here's What Many Women Tell Us:" + hair-and-outfit analogy; "some of them mention... fine lines around their mouth... uneven texture on their cheeks" | Self: empathy, no assumption about the viewer; intensity down | self | skincare | upsell script | most | medium 6–16 min | substantiation needed | "Many women tell us" must reflect real feedback | [14-03 doc 3.1; 03:41](../lessons/14-03-claude-projects-for-upsells.md) |
| R096 | First draft quoting program prices ("Here's What This Would Normally Cost") | Script that sells the free "personalized Asset Control Blueprint" call | Call-first, not price-first | offer | biz-op | upsell script | most | medium 6–16 min | none | — | [14-03 08:17–09:49](../lessons/14-03-claude-projects-for-upsells.md) |

**Row count:** 96 entries (R001–R096); one per harvested row (no exact duplicates found).

---

## Edit moves that recur (derived)
| Move | Rows | Rule |
|---|---|---|
| Plain name over jargon for the mechanism | R002–R005, R015, R042–R043 | Name the mechanism so the target buyer could repeat it |
| Remove assumptions about the reader | R006, R012, R013, R048, R049, R063, R093, R095 | Never assert the viewer's state, history or prior purchase |
| Pre-empt the obvious guess | R052, R062, R065 | Add "and no, it's not [obvious answer]" |
| Bridge the jump | R046, R057 | Write the transition line before objections or a new speaker |
| Sell the next step, not the product | R034, R096 | In short ads and call funnels the CTA sells the click or the call |
| Swap one scene/variable at a time | R007, R079–R082 | One change per variant so the test reads |
| Claim softening is not compliance | R041, R051, R068, R090 | Softer wording still needs evidence or deletion |

## Cross-course notes
- **Agreement with [Evolve rewrites](../../../evolve/copywriting/libraries/rewrites.md):** both prefer concrete, sayable language and dropping jargon; Evolve's "says vs communicates" check ([concept](../../../evolve/copywriting/concepts/says-vs-communicates.md)) is the same test Stefan applies to mechanism names.
- **RMBC adds:** model-draft editing (quote the line back, state why) and funnel-logic edits for upsells, which Evolve and Tether do not cover.

## Related
[llm-copy-chief-editing](../concepts/llm-copy-chief-editing.md) · [hooks](hooks.md) · [ad-teardowns](ad-teardowns.md) · [templates](templates.md) · [prompts](prompts.md) · [rules](rules.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [upsell-flow-build](../frameworks/upsell-flow-build.md)
