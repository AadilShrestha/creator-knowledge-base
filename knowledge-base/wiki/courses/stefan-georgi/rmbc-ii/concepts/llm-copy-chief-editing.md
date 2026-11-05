---
title: "LLM copy-chief editing"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/08-01-rmbc-ii-mid-course-recap.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/02-04-unified-research-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
tags: [rmbc-ii, copy-chief, editing, llm-workflow, multi-model, claim-audit, placeholders, vsl]
updated: 2026-11-02
---

# LLM copy-chief editing
> The human (or reviewing agent) is the copy chief, not the typist: audit the brief, copy-chief the outline, let a model draft, edit it section by section, get a second model's review or a parallel draft, merge the best sections, keep unproven proof as placeholders, then run a claim audit before anything ships.

## 🤖 Agent use
- **Use when:** any RMBC draft (brief, VSL, advertorial, PDP, ad, upsell, email) comes back from a model; deciding whether to accept, patch, re-run or merge; before handing copy to a human or a recording.
- **Inputs → outputs:** brief + approved outline + draft(s) from 1–2 models → section-by-section edit notes → merged master → placeholder list (`[VERIFY: …]`) → claim-audited draft ready for human sign-off.
- **Rules:**
  - **DO** audit the brief before writing: "the brief and the mechanism are important to catch weird stuff before you go to write copy". Delete lines that break the metaphor; strip sections you don't want echoed (brief hook list, "big ideas to test"). [07-01 v1 00:00–11:31](../lessons/07-01-long-form-vsl.md)
  - **DO** copy-chief the outline before the draft: "you're copy-chiefing the ideas and the plan, and then you'll get a chance to copy-chief the final copy as well". [07-01 v1 38:07](../lessons/07-01-long-form-vsl.md)
  - **DO** give specific, reasoned feedback in the same chat ("I basically copy chief it in the Claude project in real time" and explain why). [08-01 08:27](../lessons/08-01-rmbc-ii-mid-course-recap.md)
  - **DO** run a second model: either a parallel full draft from the same brief + outline (Gemini 2.5 Pro via Poe), or a review of one section ("Is there anything you'd change or edit with it?"). [07-01 v1 41:15–43:39](../lessons/07-01-long-form-vsl.md); [07-02 v1 27:56–29:21](../lessons/07-02-medium-length-vsl.md)
  - **DO** merge by section (pre-lead, lead, future pace, background, UMP, UMS, buildup, close), choosing per section and stating why. [07-01 v3 02:44–33:03](../lessons/07-01-long-form-vsl.md)
  - **DO** patch gaps with targeted prompts rather than full rewrites ("which ingredients map to step three?"). [07-01 v2 29:10; v3 26:53–30:59](../lessons/07-01-long-form-vsl.md)
  - **DO** check every open loop is paid off; replace teases that aren't ("The Morocco thing wasn't paid off right"). [07-02 v1 29:53–30:37](../lessons/07-02-medium-length-vsl.md)
  - **DO** read lines aloud as the viewer: "Your makeup artist can tell your real age" → "Here's why makeup artists can tell your real age" ("it's not like everyone has a makeup artist"). [07-04 v1 04:17](../lessons/07-04-short-vsl.md)
  - **DO** keep missing proof as placeholders: "fill these in with placeholders and I'll get real success stories ... later". Never replace a placeholder with invented people or results. [07-01 v5 10:48–12:19](../lessons/07-01-long-form-vsl.md)
  - **DO** verify facts the model pulled from sources (he checks "95%" and the guarantee length against the page). [09-02 30:24–30:55; 49:51](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** measure length yourself (Claude: ~8,500 words; actual 5,707; script timer ~31 min). [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
  - **DON'T** ship unread AI copy: "It's doing 99% of the work for you, so just use your brain." [14-03 10:44](../lessons/14-03-claude-projects-for-upsells.md)
  - **DON'T** agonize: "get a great first draft, tweak, modify, edit, and ship". [07-01 v2 06:38](../lessons/07-01-long-form-vsl.md)
  - **IF** a model returns weird or stale output **THEN** switch model/version and re-run the identical prompt. [07-02 v2 02:51–05:13](../lessons/07-02-medium-length-vsl.md); [07-01 v1 21:45](../lessons/07-01-long-form-vsl.md)
  - **IF** a line is "too aggressive" or "probably not compliant" (Stefan's words on his own outputs) **THEN** cut it; under repo rules that is a hard stop, not a style note. [07-04 v4 02:26–06:26](../lessons/07-04-short-vsl.md)
- **See also:** [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) · [claude-project-recipe](claude-project-recipe.md) · [compliance-red-flags](compliance-red-flags.md) · [vsl-review](../rubrics/vsl-review.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [Evolve: AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md)

## Definition
"Pretty much all the writing ... the heavy writing, is done by AI. And then we are more of the commander ... the boss, we're the copy chief." "You're a copy thinker, not a copywriter." [01-01 11:59–12:56](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) The model is a junior writer who "can write at the level of an absolute world-class legendary copywriter" when the brief is clean [07-01 v1 05:31](../lessons/07-01-long-form-vsl.md); the copy chief's job is judgment, logic, congruence and truth.

### The editing loop
| Step | Action | Prompt pattern (verbatim or near) | Source |
|---|---|---|---|
| 0 Brief audit | Remove metaphor breaks, off-strategy hooks, anything you don't want echoed; re-attach as PDF | — | [07-01 v1 00:00–11:31](../lessons/07-01-long-form-vsl.md) |
| 1 Outline review | Fix narrator, expert intro, brand-reveal point, missing promise; optionally upload your classic outline | "This looks really good overall. I've uploaded my classic sales letter outline ... Can I see another version of the outline ...?" | [01-01 19:18](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md); [07-01 v1 29:52–38:07](../lessons/07-01-long-form-vsl.md) |
| 2 Draft | Model A writes over several outputs | "please start writing the VSL ... If you need to do this over multiple outputs, that's fine ... I'll prompt you to continue." | [07-01 C6](../lessons/07-01-long-form-vsl.md) |
| 3 Edit as copy chief | Section-by-section notes in the same chat | "This was great overall ... Here are a few tweaks" | [05-02 19:03](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| 4 Second-model review | Paste one section into model B | "Is there anything you'd change or edit with it?" | [07-02 P5](../lessons/07-02-medium-length-vsl.md) |
| 5 Two-model merge (long form) | Parallel draft in model B from same brief + outline; pick per section | Same writing prompt in Poe/Gemini | [07-01 v1 41:15–v3 33:03](../lessons/07-01-long-form-vsl.md) |
| 6 Gap patches | Targeted asks | "After all, we said it's a three-step system. How can we make this work?" | [07-01 v3 28:22–29:55](../lessons/07-01-long-form-vsl.md) |
| 7 Leads/hooks | Separate project; 3–4 micro-lead options on top | — | [07-01 v4](../lessons/07-01-long-form-vsl.md) |
| 8 Placeholders → verify | Every person, number, study, quote, rating, deadline = `[VERIFY: …]` until real | — | [07-01 v5 10:48](../lessons/07-01-long-form-vsl.md) |
| 9 Claim audit | Run the rubric | — | [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) |

## Why it matters
- Models get you "99 percent of the way there most of the time, 95 percent of the way there for sure" but "you do need to be a critical thinker still". [02-04 14:03](../lessons/02-04-unified-research-process.md)
- Two models fail differently: Claude "hits the direct response beats" and had reference closes; Gemini read "more authentic" but had no reference VSL so its close was weaker. Merging beats either alone. [07-01 v2 02:58; 29:10](../lessons/07-01-long-form-vsl.md)
- "Multimodal" is also resilience: "What if Claude's being weird? What if Claude's down?" [07-01 v1 41:15–43:39](../lessons/07-01-long-form-vsl.md)
- Every course output contains invented proof (testimonials, doctors, review counts, study percentages). The copy chief is the only gate. [10-01 Compliance check](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); [09-02 38:01](../lessons/09-02-claude-project-for-advertorials.md)

## How to use (steps)
1. **Brief audit** (read the mechanism as a skeptical prospect). [07-01 v1 00:58–05:31](../lessons/07-01-long-form-vsl.md)
2. **Outline review** against [classic-vsl-structure](classic-vsl-structure.md): who tells the story, where the expert appears, where the brand is first named (end of buildup), does the lead end on a promise.
3. **Draft** in model A; for long form, the same brief + outline in model B.
4. **Section-by-section pass** with this checklist (derived from Stefan's edits):
   - Assumes the viewer's state? ("you're probably living it too" puts them "on the defensive") [07-01 v1 48:29–49:33](../lessons/07-01-long-form-vsl.md)
   - Reveals the product too early? ("applying this every morning" → "using this breakthrough") [07-01 v1 47:26–48:29](../lessons/07-01-long-form-vsl.md)
   - Specific enough? (keep "Botox, retinoids ... $3,000" over generic "$200 miracle serums") [07-01 v3 11:07–13:17](../lessons/07-01-long-form-vsl.md)
   - Every loop paid off? [07-02 v1 29:53](../lessons/07-02-medium-length-vsl.md)
   - Every promised step grounded in a real ingredient/feature? [07-01 v3 28:22](../lessons/07-01-long-form-vsl.md)
   - Logic insult or shaming? ("make them feel like shit" → "a more empathetic version that still persuades") [14-03 02:38–04:11](../lessons/14-03-claude-projects-for-upsells.md)
   - Assumptions about prior purchases? ("We shouldn't assume they bought the first upsell") [14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md)
   - Pricing and timing consistent? ("Pricing is off on this.") [15-05 20:16](../lessons/15-05-claude-project-for-writing-email-sequences.md)
   - Congruent story steps? ("why would he do that?") [09-02 50:27–52:41](../lessons/09-02-claude-project-for-advertorials.md)
5. **Second-model review** of the weakest section (usually the lead); adopt only if better.
6. **Merge** into a master doc; log which model won each section and why.
7. **Placeholders:** list every unverified item; route to the human for real proof.
8. **Claim audit** and length check; then make variants (shorter cuts, new leads/hooks).

## Examples
| Case | Edit made | Source |
|---|---|---|
| Unity brief: "hooks that connect your skin layers at the DEJ" inside a fabric-weave mechanism | Deleted: "there's no reason for that ... I don't want that in my copy" | [07-01 v1 00:58](../lessons/07-01-long-form-vsl.md) |
| 27-min Unity VSL, Claude vs Gemini | Merge log: Gemini pre-lead close and lead opener; Claude future-pace block, failed-solutions specificity, UMS steps and close; Gemini UMP scene | [07-01 v3 03:44–33:03](../lessons/07-01-long-form-vsl.md) |
| Medium VSL lead sent to Gemini | Gemini kept the hook, rewrote the micro lead with a promise; adopted: "I like that a little bit more" | [07-02 v1 27:56–29:21](../lessons/07-02-medium-length-vsl.md) |
| Hook ads: first pass all UMP-heavy, not using the hook database | "More for the curiosity ... We don't need to talk about collagen architecture" | [07-01 v4 02:30–05:05](../lessons/07-01-long-form-vsl.md) |
| ADHD hook scripts | "98% of the way there"; "common sense tweaks you would make if you're reading out loud"; ask for better transitions by hook number | [04-10 53:30–55:12](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Airbnb book-a-call outline | Case-study teasers as placeholders; Stefan: "the one big thing the FTC goes after for a biz opp ... fake testimonials and fake income claims" | [07-01 v5 10:48](../lessons/07-01-long-form-vsl.md) |
| Financial short VSL hook ($4 trillion secret) | "This is too aggressive"; "probably not compliant" | [07-04 v4 02:26–06:26](../lessons/07-04-short-vsl.md) |

Course drafts contain invented proof ("Elizabeth K., Age 62", "4.8/5 stars, 3,425+ verified reviews", "Dr. Erik Johansson", "87%"/"92%" figures). Structure only; claims not reusable. [10-01](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md); [09-02](../lessons/09-02-claude-project-for-advertorials.md)

## Common mistakes
- **Editing copy before fixing the brief**: errors propagate into every asset. [07-01 v1 05:31](../lessons/07-01-long-form-vsl.md)
- **Accepting the first draft unread.** [14-03 10:44](../lessons/14-03-claude-projects-for-upsells.md); [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md)
- **Over-editing**: "You can destroy yourself with possibilities." [07-01 v2 05:30](../lessons/07-01-long-form-vsl.md)
- **Filling placeholders with plausible fakes** instead of leaving them bracketed. [07-01 v5 10:48](../lessons/07-01-long-form-vsl.md)
- **Treating "hypey" as fine because "it tends to work"** (Stefan on a scarcity fascination [07-02 v1 30:08–31:17](../lessons/07-02-medium-length-vsl.md)): if the scarcity is not real, cut it.
- **Trusting model self-reports** of length or completeness. [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
- **Repeating the "better than 99% of copywriters" claim** in any output (instructor claim, no evidence). [07-01 v2 05:30](../lessons/07-01-long-form-vsl.md); [08-01 09:56](../lessons/08-01-rmbc-ii-mid-course-recap.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | Copy chief / copy thinker; outline revision | 11:59–12:56; 18:30–19:44 |
| [02-04 Unified research](../lessons/02-04-unified-research-process.md) | Critical thinking on LLM output | 14:03–15:36 |
| [04-10 Hooks](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) | 98% rule, read aloud | 53:30–55:12 |
| [05-02 Brief generator](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Brief revision by chat | 17:46–23:00 |
| [07-01 Long form](../lessons/07-01-long-form-vsl.md) | Brief audit, outline review, two-model merge, patches, placeholders | v1 00:00–v5 12:19 |
| [07-02 Medium](../lessons/07-02-medium-length-vsl.md) | Second-model lead review; loop payoff | v1 25:30–31:40 |
| [07-03 3–7 min](../lessons/07-03-3-7-minute-vsl.md) | Placeholder credentials in generated proof | v2 07:05 |
| [07-04 Short](../lessons/07-04-short-vsl.md) | Plain-language corrections; "too aggressive" | v1 04:17; v4 02:26–06:26 |
| [08-01 Recap](../lessons/08-01-rmbc-ii-mid-course-recap.md) | Feedback is the process | 07:29–09:26 |
| [09-02 Advertorials](../lessons/09-02-claude-project-for-advertorials.md) | Claim check vs source; congruence fix | 30:24–52:41 |
| [10-01 PDPs](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | "edit, copy chief" for PDPs | 44:06–44:37 |
| [14-03 Upsells](../lessons/14-03-claude-projects-for-upsells.md) | Logic and empathy edits | 02:38–10:44 |
| [15-05 Emails](../lessons/15-05-claude-project-for-writing-email-sequences.md) | Strategist role; pricing audit | 12:30–20:16 |

## Cross-course notes
- **Evolve Copywriting** [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md): AI drafts to "70, 80%"; human owns the last 20–30%. **RMBC** puts AI at "98%"/"99%" of the work. **Agent default:** budget editing as if the draft is 70–80% done; the RMBC figure is an instructor claim and the course's own outputs needed brief fixes, merges and claim removal every time.
- **Evolve Copywriting** [three copy checks](../../../evolve/copywriting/concepts/three-copy-checks.md) and [says vs communicates](../../../evolve/copywriting/concepts/says-vs-communicates.md) give named checks to use in step 4.
- **Tether** [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) is the short-form equivalent of the section pass.

## Related
[claude-project-recipe](claude-project-recipe.md) · [composite-vs-swipe](composite-vs-swipe.md) · [brief-2-0](brief-2-0.md) · [compliance-red-flags](compliance-red-flags.md) · [classic-vsl-structure](classic-vsl-structure.md) · [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) · [vsl-review](../rubrics/vsl-review.md)
