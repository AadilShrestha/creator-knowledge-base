---
title: "Playbook: write a VSL with Claude (brief → outline → draft → second model → merge → leads → gates)"
type: playbook
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; Patrick Stiles (16-05 benchmarks, guest) for the post-launch stage"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-03-vsl-leads-after-the-opening-hook.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-01-the-old-brief-vs-the-new-brief-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [playbook, vsl, claude-projects, outline-first, second-model, merge, leads, hooks, cut-downs, compliance]
updated: 2026-11-02
---

# Playbook: write a VSL with Claude
> Run this when asked "write a VSL for product X" (any length, in-feed or on-page): confirm real inputs, lock placement and length, set up the length-band Claude Project, get an approved outline, draft over several outputs, run a second model and merge by section, write separate leads, measure length, then pass the claim audit and VSL review before anything is recorded.

## 🤖 Agent use
- **Use when:** the task is a VSL script, a mini-VSL video ad (1-7 min), a cut-down of an existing VSL, or a batch of lead/hook variants over a VSL body.
- **Inputs → outputs:** finished Brief 2.0 + truth sheet + placement/length/CTA/narrator decisions + example transcripts for the project → approved outline (saved file) → merged master script with 3-4 alternate leads → claim-audit block + VSL-review block → optional cut-downs and short-ad variants.
- **Rules:**
  - **DO** refuse to start without a brief: "It's really important that you did if you're doing VSLs especially" ([06-01 00:00](../lessons/06-01-claude-vsl-projects-setup-overview.md)); the projects "only consume the brief; they do not do research" (same page).
  - **DO** get an outline with an estimated length and approve it before any draft ([07-01 v1 28:33](../lessons/07-01-long-form-vsl.md); [07-03 v1 04:50](../lessons/07-03-3-7-minute-vsl.md)).
  - **DO** act as copy chief, not typist: "I basically copy chief it in the Claude project in real time" ([08-01 08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)); "you're still sort of the conductor" ([07-04 v4 04:17](../lessons/07-04-short-vsl.md)).
  - **DO** keep two models available: "this is why you need to have multiple models, and you're screwed if you don't" ([07-02 v2 02:51–03:40](../lessons/07-02-medium-length-vsl.md)).
  - **DO** measure length yourself (≈150 spoken words/min, derived): model estimates were off by thousands of words ([07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)).
  - **DON'T** over-tune the setup: "use the processes rather than try to tweak them" ([06-01 04:24–05:16](../lessons/06-01-claude-vsl-projects-setup-overview.md)).
  - **DON'T** ship an unread draft: "It's doing 99% of the work for you, so just use your brain" ([14-03 10:44](../lessons/14-03-claude-projects-for-upsells.md)).
  - **DON'T** let any example proof (doctors, patients, testimonials, study numbers, scarcity) survive: every course run produced them. Gate: [LLM output claim audit](../rubrics/llm-output-claim-audit.md).
  - **IF** the copy is decent **THEN** ship the edited draft: "get a great first draft, tweak, modify, edit, and ship" ([07-01 v2 06:38](../lessons/07-01-long-form-vsl.md)).
- **See also:** [VSL build with Claude (framework)](../frameworks/vsl-build-with-claude.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [Classic VSL structure](../concepts/classic-vsl-structure.md) · [VSL length bands](../concepts/vsl-length-bands.md) · [Composite vs swipe](../concepts/composite-vs-swipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Hook generation system](../frameworks/hook-generation-system.md) · [Prompts library](../libraries/prompts.md) · [VSL review](../rubrics/vsl-review.md) · Repo skill: [write-ugc-script](../../../../../../.claude/skills/write-ugc-script/SKILL.md) (short UGC ads)

## Required real inputs (ask the user for anything missing; do not guess)
| # | Input | Why it is needed | If missing |
|---|---|---|---|
| 1 | **Finished Brief 2.0** (25 fields) with the mechanism (UMP/UMS) and its nickname | The VSL projects only consume the brief ([06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)); field list in [Brief 2.0](../concepts/brief-2-0.md) | Run stages 1-4 of [offer-to-funnel-end-to-end](offer-to-funnel-end-to-end.md) first |
| 2 | **Truth sheet**: product facts, label/doses, real offer, prices, packages, guarantee, real reviews (count, platform, link), real testimonials with permission, real studies (link, population, dose), real spokesperson and credentials, real scarcity rules | Every claim must trace here ([AGENTS.md](../../../../../../AGENTS.md) rule 2) | List each missing item; the script will carry `[VERIFY: …]` |
| 3 | **Placement**: in-feed ad, on-page VSL, or both | Different spines and leads ([04-11 04:02–05:01; 11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)) | Ask; do not assume |
| 4 | **Funnel type and CTA**: straight sale, book-a-call, upsell, or tease → watch longer presentation | Changes the close (book-a-call: "will not talk about the price", [07-01 C10](../lessons/07-01-long-form-vsl.md)) | Ask |
| 5 | **Target length** | Picks the project ([06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)) | Use Stage 2 table |
| 6 | **Awareness level** of the target traffic | Must be stated in the prompt ([07-04 v2 05:47](../lessons/07-04-short-vsl.md); [07-01 C10](../lessons/07-01-long-form-vsl.md)) | Take from the unified research doc ([product-market awareness](../concepts/product-market-awareness.md)) |
| 7 | **Narrator**: founder, expert, customer, host + expert, and whether they are real and consenting | Narrator changes the background story ([07-02 v1 03:31–06:55](../lessons/07-02-medium-length-vsl.md)) | Default to the real founder; never an invented expert |
| 8 | **Example VSL transcripts** for project knowledge (long: 8, medium: 5, 3-7: 8, short: one combined doc) | Composite modelling ([06-01 05:46–06:18](../lessons/06-01-claude-vsl-projects-setup-overview.md)) | Ask the user for their swipe file; structure only |
| 9 | **Hook database / customer language** (real reviews, comments, Reddit) | Leads are written separately ([07-01 v4](../lessons/07-01-long-form-vsl.md); [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)) | Build one in Stage 9 |

## Stages

### Stage 1: audit the brief
- **Inputs:** Brief 2.0, truth sheet. Ask the user for the brief if absent.
- **Follow:** [Brief 2.0](../concepts/brief-2-0.md) · [brief-generator](../frameworks/brief-generator.md).
- **Do:** read the mechanism "as a skeptical prospect would" and delete lines that break the metaphor ([07-01 v1 00:58–01:58](../lessons/07-01-long-form-vsl.md)); strip "Big ideas to test" and hook lists if leads will be written separately ([07-01 v1 10:26–11:31](../lessons/07-01-long-form-vsl.md)); if no strong big idea exists, ideate it in the project and update the brief ([08-01 07:58–08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)).
- **Prompt (course, verbatim, [07-01 C13](../lessons/07-01-long-form-vsl.md) pattern):**
  ```text
  Okay I like the [big idea A]. I do like the phrase "[phrase]" not as a big idea, but something that can be teased on the lead. [Other decision]. Can you update the brief to incorporate this information please?
  ```
- **Output:** cleaned brief v2 saved as a file ("save the first good brief to a document before revising" [05-02 17:46](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)).
- **Gate:** [claim audit](../rubrics/llm-output-claim-audit.md) on the brief. Every unverified proof line becomes `[VERIFY: …]`. BLOCK = stop.

### Stage 2: lock placement, length band and project
- **Inputs:** placement, funnel type, CTA, awareness, target length.
- **Follow:** [VSL length bands](../concepts/vsl-length-bands.md) · [sell the click](../concepts/sell-the-click.md).

| Need | Project | Target | Notes |
|---|---|---|---|
| Straight-sale on-page VSL | Long Form VSL Generator | 20-35 min (16-05 sweet spot; generator allows 25-60) | 45+ min is the worst-converting band for straight sale (guest claim, [16-05 35:17–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| Book-a-call VSL | Long Form or Medium | ~25 min (course run; guest best 25 / worst 60) | No price; CTA = book a call for a plan ([07-01 C10](../lessons/07-01-long-form-vsl.md)) |
| Mid-length on-page or in-feed | Medium Length VSL Generator | 6-16 min (ask ~18 if you want ~16: Claude "estimates a little low", [05-02 23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)) | Can be cut from a long VSL you like ([07-02 v2 08:03](../lessons/07-02-medium-length-vsl.md)) |
| In-feed Meta ad that teases | 3-7 Minute VSL Generator | 3-7 min | CTA "watch the video"; no brand/product ([07-03 v1 01:47–02:09](../lessons/07-03-3-7-minute-vsl.md)) |
| Short ad | Short Length VSL Generator | 1-4 min (mostly 1-2) | Hook is the main variable ([07-04 v1 02:04](../lessons/07-04-short-vsl.md)) |

- **Project setup:** one project per band; paste the instruction text into "What are you trying to achieve?" and project instructions; add example transcripts ([06-01 05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md)). Verbatim instruction texts: [VSL build with Claude](../frameworks/vsl-build-with-claude.md) and [prompts library](../libraries/prompts.md). Keep the line "Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue." ([06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md)).
- **Derived addition** to every project's instructions (not in the course): `Never invent people, credentials, testimonials, reviews, counts, studies, percentages, prices, deadlines or stock levels. Use only facts in the brief; where a proof element is needed and missing, write [VERIFY: what is needed].`
- **Output:** a one-line spec: `placement | funnel | CTA | awareness | narrator | target min | project`.
- **Gate:** user confirms the spec.

### Stage 3: swipe or composite
- **Follow:** [Composite vs swipe](../concepts/composite-vs-swipe.md).
- **Rule:** new brand → composite ([07-01 v1 12:28–14:49; 25:54](../lessons/07-01-long-form-vsl.md)). Close swipe only of **our own** winning VSL ("it's my VSL and I want to swipe my VSL"); another brand's letter is "maybe too close for comfort" ([06-01 09:15–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md)). Repo rule 3: copy the mechanism, not the asset.
- **Optional test prompt (course, verbatim, [07-01 C1](../lessons/07-01-long-form-vsl.md)):** "Can you do the first 1,000 words of the new VSL following the [VSL name] structure so I can see what that looks like?" Use only on our own VSL.
- **Output:** mode = composite | own-swipe.

### Stage 4: outline with estimated length
- **Inputs:** brief v2 attached in the same message (forgetting it forced a redo, [07-02 v1 07:05](../lessons/07-02-medium-length-vsl.md); [07-03 v2 04:37–05:10](../lessons/07-03-3-7-minute-vsl.md)).
- **Follow:** [classic VSL structure](../concepts/classic-vsl-structure.md).
- **Prompt (course, verbatim, [07-02 P1](../lessons/07-02-medium-length-vsl.md); same as [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)):**
  ```text
  I'm going to upload a comprehensive brief for a new VSL. It should give you everything you need to write it. Please review, and then I want you to give me an outline for this new VSL, along with your estimate for how long it'll be. Let's aim for about [N] minutes.
  ```
  Add in the same message: narrator and background-story choice ([07-02 P3](../lessons/07-02-medium-length-vsl.md)), awareness level, and CTA. Book-a-call (course, verbatim, [07-01 C10](../lessons/07-01-long-form-vsl.md)): "This means we will not talk about the price in it, we'll instead hook people in, educate, and the CTA will be to book a call…". Mini-VSL ad (course, verbatim, [07-03 Q5](../lessons/07-03-3-7-minute-vsl.md)): "Please come up with an outline for a [3] minute video ad. It will go to the longer VSL, so the CTA of this video ad will be to get people to go watch the full presentation. Let's also make the ad fairly educational while still having lots of curiosity and some promises. Let's use the following as the opening hook: [hook]".
- **Output:** timed outline.

### Stage 5: copy-chief the outline
- **Follow:** [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md); [VSL review](../rubrics/vsl-review.md) S1-S13, S18, S21.
- **Check:** promise + future pace in the lead; who tells the story; how the expert is introduced; brand not before the reveal ([07-01 v1 29:52–38:07](../lessons/07-01-long-form-vsl.md)); every loop has a payoff; the mechanism is one sentence.
- **Prompts (course, verbatim):**
  - Attach the classic outline ([07-01 C4](../lessons/07-01-long-form-vsl.md)): "I'm going to share a classic VSL structure with you. Please check this out for a general idea of how the VSL will flow, and then modify your outline accordingly, based on information in the brief."
  - Remix for a second version ([07-02 P4](../lessons/07-02-medium-length-vsl.md)): "…Can I see another version of the outline that incorporates things that you think should be added or changed based on this document? Because I don't want to be in the exact same structure as the last one."
  - Lock earlier sections ([07-03 Q6](../lessons/07-03-3-7-minute-vsl.md)): "Please don't change anything up to the [section] section."
- **Output:** approved outline, saved as its own file (e.g. "<product> VSL V2 outline", [07-02 v1 10:57–11:58](../lessons/07-02-medium-length-vsl.md)).
- **Gate:** user approves the outline.

### Stage 6: draft over multiple outputs
- **Prompt (course, verbatim, [07-01 C11](../lessons/07-01-long-form-vsl.md)):**
  ```text
  I'm also attaching the outline for the structure. Please go ahead and write the VSL. If you need to do it over multiple outputs, that's fine. Simply tell me when you run out of space and I'll prompt you to continue.
  ```
  Reply "continue" when the model stops ([06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md)).
- **IF** the model glitches or returns stale output **THEN** switch model/version rather than debug ([07-01 v1 21:45; 43:39](../lessons/07-01-long-form-vsl.md)).
- **Output:** draft A.

### Stage 7: second model, then merge by section
- **Prompt to the second model (course, verbatim, [07-01 C6](../lessons/07-01-long-form-vsl.md)):**
  ```text
  We're going to write a new VSL for a [category] brand. It's direct response, going to be [N] minutes long, roughly. I'm attaching the brief and also the outline of how I want it to go. Please start writing the VSL right now. If you need to do this over multiple outputs, that's fine. Whenever you run out of room, simply let me know and I'll prompt you to continue.
  ```
- **Merge:** read the leads first, then compare lead, background, UMP, UMS, build-up, close; keep the best per section ([07-01 v1 44:48; v3 02:44–30:59](../lessons/07-01-long-form-vsl.md)). Model with the reference VSLs usually writes the better close ([07-01 v2 29:10](../lessons/07-01-long-form-vsl.md)).
- **Patch prompts (course patterns, [07-01 C7, C12](../lessons/07-01-long-form-vsl.md)):** "One thing that's not clear is which of these ingredients are related to step three…"; "I think we need a better transition to [topic]. It's kind of abrupt…"; "my immediate objection is, oh, that's expensive. So maybe we remove it."
- **Lead review in another model ([07-02 P5](../lessons/07-02-medium-length-vsl.md)):** "Here's the start of another version that comes from [narrator]. Is there anything you'd change or edit with it?"
- **Output:** merged master script.

### Stage 8: measure length
- Word count ÷ 150 ≈ minutes (derived); or a script timer ([07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)). Accept "a little short" if all beats survive ([07-02 v2 05:54](../lessons/07-02-medium-length-vsl.md)).
- **Output:** measured length logged in the review block.

### Stage 9: leads and hooks (separate step)
- **Follow:** [hook generation system](../frameworks/hook-generation-system.md) · [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md).
- **Prompt (course, verbatim, [07-01 C8](../lessons/07-01-long-form-vsl.md)):**
  ```text
  Here's a new VSL script I wrote for a [product]. Please give me 10 hook-heavy lead concepts I could use for the micro lead. You can pull from the database plus ideas from the VSL. I'll then select the ones I want to turn into new pre-leads or leads.
  ```
  Then: "Great job, let's go ahead and do a new micro lead with [concept]. Let's keep it to about the same length as the current pre-lead/micro lead in the VSL I uploaded."
- **Rules:** give 2-3+ opening options, not 3-5 different 700-word leads ([04-03 35:22](../lessons/04-03-vsl-leads-after-the-opening-hook.md)); for in-feed expect "dozens and dozens" of micro-leads ([04-03 39:00–39:27](../lessons/04-03-vsl-leads-after-the-opening-hook.md)); reject generic or "too aggressive" hooks ([07-04 v1 10:49; v4 06:26](../lessons/07-04-short-vsl.md)); read hooks aloud for reach ("Here's why makeup artists can tell…", [07-04 v1 04:17](../lessons/07-04-short-vsl.md)).
- **Output:** 3-4 pre-lead options pasted at the top of the master script, each with a lead ID ([04-10 57:38](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)).

### Stage 10: quality gates
1. [LLM output claim audit](../rubrics/llm-output-claim-audit.md) on the full script and every lead. BLOCK → fix and re-run.
2. [VSL review](../rubrics/vsl-review.md) Part 1. < 70% → back to Stage 5; 70-84% → fix listed defects; ≥ 85% → record.
- **Output:** final script with both scoring blocks at the top and an open-`[VERIFY]` list for the user.

### Stage 11: derivatives (optional)
| Derivative | Prompt (course, verbatim) | Cite |
|---|---|---|
| Cut-down of the master | "Can you take this and do a version that is [N] minutes long? Keep the three options for the openings, since each video would only have one of those options… It should be the same VSL, just strategically cutting things down to make it fit the length." | [07-02 P6](../lessons/07-02-medium-length-vsl.md) |
| Short concepts from the brief | "Please give me 5 short VSL concepts that are 2 minutes maximum each… some of what is in the brief won't need to make it into these VSLs since they'll be short." | [07-04 prompt 4](../lessons/07-04-short-vsl.md) |
| Shorter sibling | "This is awesome. Now please do a 1 minute and 30 second version." | [07-03 Q3](../lessons/07-03-3-7-minute-vsl.md) |
| Hook swap, same body | "Now I want to do another ad where everything after the Revelation/Education section is pretty much the same. But we do a different hook. In this case let's do this hook: [hook]" | [07-03 Q8](../lessons/07-03-3-7-minute-vsl.md) |
| CTA variant | "let's do another version where the CTA is to click the ad and save up to [real %] but we don't reveal the prices." | [07-04 prompt 6](../lessons/07-04-short-vsl.md) |
| On-page version of an in-feed winner | Keep the body; write a classic lead | [04-11 11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md) |

Each derivative re-runs Stage 10. One variable per variant ([07-03 v2 08:58–09:35](../lessons/07-03-3-7-minute-vsl.md)).

### Stage 12: after launch
- Pull player data and run [VSL review Part 2](../rubrics/vsl-review.md): conversion vs 1.78%, engagement 33% / 28% / 3%, unmute 40% / 7 s, 47% of conversions at the end (guest claims, [16-05](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).
- Test leads first; add clincher copy after the CTA; set a thumbnail; captions.

## Failure modes seen in the course runs
| Failure | Seen in | Prevention |
|---|---|---|
| Brief not attached → outline built from examples, solution tease off-offer | [07-02 v1 07:05](../lessons/07-02-medium-length-vsl.md); [07-03 v2 04:37–05:10](../lessons/07-03-3-7-minute-vsl.md) | Attach brief in the same message |
| Model overstates length | [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md); [07-03](../lessons/07-03-3-7-minute-vsl.md) (3-min scripts ran 790-850 words) | Stage 8 |
| Unpaid loop | [07-02 v1 29:53](../lessons/07-02-medium-length-vsl.md) | VSL review S18 |
| Illogical Nope sequence | [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md) | Rewrite around beliefs the hook actually raises |
| Invented doctor, patients, studies, counts, scarcity | [07-02](../lessons/07-02-medium-length-vsl.md), [07-03](../lessons/07-03-3-7-minute-vsl.md), [07-04](../lessons/07-04-short-vsl.md) compliance flags | Derived instruction line (Stage 2) + claim audit |
| Hook topic drifts from the product promise | [07-04 v4 02:51–03:39](../lessons/07-04-short-vsl.md) | Refocus prompt on the real promise |

## Related
- [Offer to funnel end to end](offer-to-funnel-end-to-end.md) · [Launch a cold-traffic funnel](launch-a-cold-traffic-funnel.md) · [Playbooks hub](README.md) · Evolve: [write a video ad script](../../../evolve/copywriting/playbooks/write-a-video-ad-script.md) (short UGC-style scripts; RMBC adds the long-form VSL machinery)
