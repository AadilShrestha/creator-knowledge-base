---
title: "VSL Build with Claude Projects"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
tags: [vsl, claude-projects, outline-first, copy-chief, second-model, lead-variants, hook-swap, video-ads, long-form, medium-form, short-form]
updated: 2026-11-02
---

# VSL Build with Claude Projects
> Set up one Claude Project per VSL length, then run every script through the same gated loop: audited brief → timed outline (approved) → draft → copy-chief edit and second-model review → separate lead/hook step → one-variable variants.

## 🤖 Agent use
- **Use when:** writing any VSL or video-ad script from 90 seconds to 60 minutes for our own brand; cutting an existing VSL to a new length; producing hook, CTA, narrator or mechanism variants of a script; reviewing an LLM VSL draft.
- **Inputs → outputs:** finished Brief 2.0 ([brief-generator](brief-generator.md)) + target length + CTA/destination + awareness level + narrator + (optional) classic structure doc + (optional) hook list → approved timed outline → full script → merged/edited master → 3-4 alternate leads or hook-swap variants → claim-audited script with `[VERIFY: …]` marks.
- **Rules:**
  - **DO** finish and audit the brief before opening a VSL project; the projects only consume the brief, they do no research. [06-01 00:00](../lessons/06-01-claude-vsl-projects-setup-overview.md) Read the mechanism as a skeptic and delete lines that break its metaphor. [07-01 v1 00:58](../lessons/07-01-long-form-vsl.md)
  - **DO** use one project per length band with the verbatim instructions below and varied example transcripts as knowledge. [06-01 05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **DO** ask for an outline with timings and a length estimate first; write only after approval. "Once approved, I'll have you write it." [07-01 v1 28:33](../lessons/07-01-long-form-vsl.md) The gate stays even at 3 minutes: "it makes me double check and confirm there's nothing I want to tweak." [07-03 v1 04:50](../lessons/07-03-3-7-minute-vsl.md)
  - **DO** copy-chief the outline (who tells the story, how the expert enters, where the brand first appears, is there a solution promise and future pace) before drafting. [07-01 v1 32:48–38:07](../lessons/07-01-long-form-vsl.md)
  - **DO** run long and medium drafts through a second model and merge by section. [07-01 v1 41:15–43:39](../lessons/07-01-long-form-vsl.md); [07-02 v1 27:56](../lessons/07-02-medium-length-vsl.md)
  - **DO** measure length yourself (word count, script timer). Claude claimed about 8,500 words; actual was 5,707. [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
  - **DO** change one lever per variant (hook, CTA, narrator, mechanism) and say "the rest of the ad from this point on can basically stay the same". [07-04 v3 05:43](../lessons/07-04-short-vsl.md); [07-03 v2 08:58](../lessons/07-03-3-7-minute-vsl.md)
  - **DON'T** ship a swipe. Use a close swipe only of *our own* proven VSL; for anything else use the composite. [06-01 09:15–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-01 v1 24:54](../lessons/07-01-long-form-vsl.md)
  - **DON'T** name the product or brand in the lead; hold the brand until the end of the buildup/reveal. [07-01 v1 31:13–32:48; 47:26](../lessons/07-01-long-form-vsl.md)
  - **DON'T** open loops you never pay off; don't let the lead assume the viewer's state ("you're probably living it too"). [07-02 v1 29:53](../lessons/07-02-medium-length-vsl.md); [07-01 v1 48:29](../lessons/07-01-long-form-vsl.md)
  - **DON'T** keep invented proof, credentials, studies, income figures or scarcity from drafts. Bracket every claim not in the brief as `[VERIFY: …]`. See [Compliance](#compliance).
  - **IF** Claude glitches, returns stale or off-brief output **THEN** run the identical prompt in another model or model version instead of debugging. [07-01 v1 21:45](../lessons/07-01-long-form-vsl.md); [07-02 v2 02:51–03:40](../lessons/07-02-medium-length-vsl.md)
  - **IF** the output stops mid-script **THEN** reply "continue"; the project instructions already invite it. [06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **IF** you already like a long VSL **THEN** cut it down instead of starting from the brief. [07-02 v2 08:03](../lessons/07-02-medium-length-vsl.md)
- **See also:** [hook-generation-system](hook-generation-system.md) · [brief-generator](brief-generator.md) · [Claude project recipe](../concepts/claude-project-recipe.md) · [VSL length bands](../concepts/vsl-length-bands.md) · [Classic VSL structure](../concepts/classic-vsl-structure.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Composite vs swipe](../concepts/composite-vs-swipe.md) · [Prompt library](../libraries/prompts.md) · [VSL review rubric](../rubrics/vsl-review.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [Playbook: write a VSL with Claude](../playbooks/write-a-vsl-with-claude.md)

## What it is
Stefan Georgi's production method for VSLs in RMBC II. The thinking happens upstream (research, mechanism, brief). The VSL step is a gated conversation with a length-specific Claude Project whose knowledge holds example transcripts. The model is told to "analyze the structure… synthesize that knowledge and use that same knowledge, along with your judgement, to produce new" VSLs (the composite method), not to rewrite one letter. [06-01 08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md) The human acts as copy chief at two gates: the outline and the draft. "You're copy-chiefing the ideas and the plan, and then you'll get a chance to copy-chief the final copy as well." [07-01 v1 38:07](../lessons/07-01-long-form-vsl.md)

The four lengths share one loop. They differ in brief usage, hook timing, CTA and how many variants you make:

```
Brief (audited) → Project (by length) → Outline + timing → [copy-chief gate] → Draft (Claude ± second model)
 → Merge + patch → Length check → Leads / hooks (separate step) → One-lever variants → Claim audit → Ship
```

## Inputs checklist
- [ ] **Brief 2.0** for the offer, as a PDF attached to the chat (not in project knowledge). [07-01 v1 11:31](../lessons/07-01-long-form-vsl.md) Built with [brief-generator](brief-generator.md).
- [ ] Brief audited: mechanism consistent with its analogy; "Big ideas to test" and the brief's own hook list removed if leads will be written separately. [07-01 v1 00:58–11:31](../lessons/07-01-long-form-vsl.md)
- [ ] A **big idea** strong enough to justify the length. If the mechanism is plain, add one to the brief first. [07-01 v6 00:00–09:36](../lessons/07-01-long-form-vsl.md)
- [ ] **Target length** in minutes (pick the project from the [length table](#per-length-variants)).
- [ ] **CTA / destination:** buy (price shown), book a call (no price), watch the full presentation, read a report, shop now, or click to save a percentage. [07-04 v2 00:01–00:31; v1 12:15–13:54](../lessons/07-04-short-vsl.md)
- [ ] **Awareness level** of the traffic (e.g. "mostly problem aware"). [07-04 v2 05:47](../lessons/07-04-short-vsl.md); see [product-market awareness](../concepts/product-market-awareness.md)
- [ ] **Narrator:** founder, expert, customer, newscaster. Must be a real person or a disclosed character.
- [ ] Optional: your classic sales-letter outline ([classic VSL structure](../concepts/classic-vsl-structure.md)); a hook list from [hook-generation-system](hook-generation-system.md); an existing VSL to cut down.
- [ ] Real proof only: testimonials, studies on the finished product, review counts, prices and guarantees you can document. Everything else becomes `[VERIFY: …]`.

## Steps

### Step 0 — Set up the four VSL projects (once)
- **Input:** the four instruction texts below + example transcripts per band.
- **Output:** four Claude Projects: Long Form, Medium Length, 3-7 Minute, Short Length VSL Generator.
- **How:** create project → paste the instruction into "What are you trying to achieve?" and the project instructions → add transcripts via "plus" > add content, or drag PDFs. [06-01 05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md) Course loadout: long 8 transcripts, medium 5, 3-7 minute 8 (each with a "Video Length: m minutes s seconds" line, an unproven experiment), short 1 combined doc of 12 scripts. [06-01 01:29; 05:46–06:18](../lessons/06-01-claude-vsl-projects-setup-overview.md)
- **Prompt (project instructions, verbatim):** all four are in [../libraries/prompts.md](../libraries/prompts.md). Long form in full:

```text
New Project Name:
Claude Long Form VSL Generator

Your job is to generate long form video sales letters. They will typically be between 25 minutes and 60 minutes in length. The documents in your knowledge base include transcripts from several long form VSLs which we can model off while writing new VSLs. What you'll want to do is analyze the structure of the various long form VSL examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new long form VSLs.

In general, when you go to write I'll give you various inputs or even an outline and a gameplan, and you'll be able to model off the examples based on the information about whatever the current long form VSL project is.

One IMPORTANT Note. Please don't try to rush or condense anything. It's very important that if we're writing a long-form VSL, we're matching the structures and lengths of other long-form VSLs (even when it's a compository structure of several VSL examples from your knowledge base). So whenever you run out of space, just prompt me and I'll tell you to continue.

Prompt Example:

Here are a list of inputs for a new VSL that we are going to be writing. After reviewing them, I want you to come up with an outline for a new VSL based on this inputs. When providing this outline, please provide an estimated length for the new VSL. After I have reviewed the outline and approved I will let you know and we can actually write it.
```

  The other three swap the band ("between 6 minutes and 16 minutes"; "mini video sales letters that are typically 3-7 minutes long"; "between 1-4 minutes") and drop the "matching the structures and lengths" sentence and the prompt example. The 3-7 project adds this usage paragraph, verbatim:

```text
Please note that most of the time, VSLs of this length are run as in-feed ads on meta. Also, they often do not reveal the product they are selling, and instead tease a new solution or breakthrough, with the call to action being to go watch a video or read a report to get information. That being said, at other times, they may mention the product and mention how people can get a discount. I'll typically specify the goal when asking you to write VSL Scripts.
```

- **Add (our rule, derived from [06-01 07:48–08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md)):** append to every project: "Do not reuse any claims, statistics, studies, credentials, names or testimonials from the knowledge files. Use only facts in the attached brief. Mark anything unverified as [VERIFY: …]." The course examples include aggressive ClickBank offers; Stefan says an LLM "would just make less aggressive claims, especially if you told it to".
- **Tool/model:** Claude Projects (Sonnet 4 and 3.7 on screen). Stefan chose Sonnet over Opus: Opus is "slower. I don't think I need it." [07-01 v1 28:33](../lessons/07-01-long-form-vsl.md)
- **Check before moving on:** each project has the instruction text, examples that fit our compliance level, and the no-claims line.
- **Don't over-tune:** "use the processes rather than try to tweak them." [06-01 04:24–05:16](../lessons/06-01-claude-vsl-projects-setup-overview.md)

### Step 1 — Audit and trim the brief
- **Input:** Brief 2.0.
- **Output:** a revised brief PDF.
- **Actions:**
  - Delete mechanism lines that break the analogy. Example: "hooks that connect your skin layers" inside a weave/fabric metaphor. [07-01 v1 00:58–03:53](../lessons/07-01-long-form-vsl.md)
  - Re-centre nicknames on the main mechanism.
  - Remove "Big ideas to test" and the brief's hook list ("I'm still going to end up writing leads separately"). [07-01 v1 10:26–11:31](../lessons/07-01-long-form-vsl.md)
  - If nothing is big enough to hold a long video, ask the Brief Generator for big-idea options and add the chosen one to the brief.
- **Prompt (big-idea update to the brief, verbatim, [07-01 v6](../lessons/07-01-long-form-vsl.md) screen 9:36):**

```text
Okay I like the 30 second blood sugar reset ritual. I do like the phrase "The Missing Page From Every Medical Textbook" not as a big idea, but something that can be teased on the lead. And I like my idea of the Himalayan Rice Hack and then later we can pay off that the hack is actually related to a spice or flavoring that gets added to rice. Can you update the brief to incorporate this information for please?
```

- **Check before moving on:** the mechanism reads logically to a skeptic. The brief does not repeat the product or brand name where you don't want the model to anchor on it. The 07-01 swipe test produced "super weird" output partly because the brief kept calling the narrator "founder of Opal Beauty". [07-01 v1 20:12](../lessons/07-01-long-form-vsl.md) Unsupported claims in the brief are marked.
- Why: "the brief and the mechanism are important to catch weird stuff before you go to write copy." [07-01 v1 05:31](../lessons/07-01-long-form-vsl.md)

### Step 2 — Choose the mode: composite (default) or swipe
- **Input:** the brief + project knowledge.
- **Output:** a decision. Optionally, a 1,000-word swipe sample used only to see the structure.
- **Prompt ("lazy swipe" test, verbatim, [07-01 v1 15:36](../lessons/07-01-long-form-vsl.md)):**

```text
I've uploaded the brief for a new VSL that we're going to write. To start, I want to see what it looks like if we very closely model the structure and length of the Mitolyn VSL that's in your project knowledge, but doing it for this new product and brand. Can you do the first 1,000 words of the new VSL following the Mitolyn structure so I can see what that looks like?
```

- **Result in the course:** on Sonnet 3.7 the swipe copied the Mitolyn lead almost line for line, including "Harvard and Yale" and the "bizarre … exploit" frame. [07-01 v1 21:45–24:54](../lessons/07-01-long-form-vsl.md)
- **Decision:** a close swipe is fine only for *our own* proven VSL moved to a new category. Otherwise use the composite. [06-01 09:15](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-01 v1 24:54–25:54](../lessons/07-01-long-form-vsl.md)
- The 05-05 financial run used a declared swipe ("model off the structure of the Agora Secret Trust Fund sales letter… keep the structure very similar"). [05-05 14:52](../lessons/05-05-financial-promo-example.md) Treat it as structure study only.
- **Check before moving on:** no competitor lines, names, mechanism names or claims survive.

### Step 3 — Request a timed outline (the gate)
- **Input:** the brief PDF attached in the chat, target length, CTA, awareness, narrator.
- **Output:** an outline with sections, a time per section and the model's length estimate.
- **Prompts (verbatim):**
  - Long, eye serum, [07-01 v1 28:33](../lessons/07-01-long-form-vsl.md) (captions):

```text
Here's the brief for a new product and brand to write a new long-form VSL that is about 27 minutes in length. Please [give me] an outline for this new VSL that I can look at, and once approved, I'll have you write it.
```

  - Medium, [07-02 v1 03:18](../lessons/07-02-medium-length-vsl.md); the same wording is used at [05-02 24:24](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md):

```text
I'm going to upload a comprehensive brief for a new VSL. It should give you everything you need to write it. Please review, and then I want you to give me an outline for this new VSL, along with your estimate for how long it'll be. Let's aim for about 18 minutes.
```

  - Book-a-call, problem-aware, [07-01 v5](../lessons/07-01-long-form-vsl.md) screen 9:00 (the first part is verbatim):

```text
I'm attaching a brief for an Airbnb Arbitrage Coaching program, and we're going to be doing a book a call VSL for it. This means we will not talk about the price in it, we'll instead hook people in, educate, and the CTA will be to book a call with the spokesperson and his team to get a personalized plan and to see if they're a good fit to work with them.

One important note is I want this VSL to focus on people who are problem aware, more than solution aware. So I don't want it immediately talking about Airbnb Arbitrage or assuming people have tried programs like that in the past.

To start, please give me an outline for a 25 minute book a call VSL. After I approve, we can move [on to writing it].
```

- **Tool/model:** the length project. Use Sonnet.
- **Check before moving on:** go to Step 4. Never write from an unreviewed outline.

### Step 4 — Copy-chief the outline; optionally remix against the classic structure
- **Input:** the outline.
- **Output:** the approved outline, saved as its own doc and PDF so it can go to a second model. [07-01 v1 40:12–41:15](../lessons/07-01-long-form-vsl.md); [07-02 v1 10:57](../lessons/07-02-medium-length-vsl.md)
- **Check list (from Stefan's fixes):**
  - The lead promises a solution and future-paces the result. [07-01 v1 29:52](../lessons/07-01-long-form-vsl.md)
  - The founder's whole story is not told in the lead.
  - The brand is held until the end of the buildup.
  - The expert's introduction is explicit (referral, consultation) and the expert delivers the UMP/UMS. [07-01 v1 36:45](../lessons/07-01-long-form-vsl.md)
  - Every teased loop has a planned payoff.
  - Case-study and proof slots are spread through the script ("lots of social proof") as `[placeholder]`. [07-01 v5 10:48–13:18](../lessons/07-01-long-form-vsl.md)
- **Prompts (verbatim):**
  - Feedback on the outline, [07-01 v1](../lessons/07-01-long-form-vsl.md) screen 37:23:

```text
This is pretty good. The one thing I want to make sure we incorporate is how her search for truth led her to meet Dr. Schilling. He is the one who reveals the UMP and UMS. We can say he was referred to her by a friend. Dr. Schilling doesn't need to have a speaking role in this VSL. Instead, it can be Laura recounting what he told her about the UMP and UMS.
```

  - Classic-structure attachment, [07-01 v1 32:48](../lessons/07-01-long-form-vsl.md):

```text
I'm going to share a classic VSL structure with you. Please check this out for a general idea of how the VSL will flow, and then modify your outline accordingly, based on information in the brief.
```

  - Classic-structure remix for a *different* arrangement, [07-02 v1 08:48](../lessons/07-02-medium-length-vsl.md):

```text
This looks really good overall. I've uploaded my classic sales letter outline. While we might not be able to go super in-depth on every aspect of this, I think it helps. Can I see another version of the outline that incorporates things that you think should be added or changed based on this document? Because I don't want to be in the exact same structure as the last one. I really liked what I had before.
```

- **Option:** generate several outlines with different structures, write several VSLs, then choose. [07-01 v1 38:07](../lessons/07-01-long-form-vsl.md)
- **Check before moving on:** you can explain the logical flow section by section ("there's a part that doesn't make sense" gets fixed now, not after drafting).

### Step 5 — Draft (in two models for long and medium)
- **Input:** the approved outline + brief, in the same chat or attached to a new one.
- **Output:** a full draft written over several outputs.
- **Prompts (verbatim):**
  - Claude, inside the approved-outline chat ([07-02 v1 01:24](../lessons/07-02-medium-length-vsl.md) shows a steer folded into the "write" message):

```text
This looks pretty good. When we get to the big revelation, let's make sure Laura talks about how she was introduced to Dr. Schilling, and he's the one who shared the real reason eye creams fail, and the science of the UMP and UMS. It'll still be Laura speaking the whole time, but she can recount what Dr. Schilling said. Please go ahead and start writing the VSL now.
```

  - Outline attached to a new chat, [07-01 v5 18:25–19:35](../lessons/07-01-long-form-vsl.md):

```text
I'm also attaching the outline for the structure. Please go ahead and write the VSL. If you need to do it over multiple outputs, that's fine. Simply tell me when you run out of space and I'll prompt you to continue.
```

  - Second model (Gemini 2.5 Pro via Poe; no project knowledge), [07-01 v1 41:15–42:30](../lessons/07-01-long-form-vsl.md):

```text
We're going to write a new VSL for a skincare brand. It's direct response, going to be 27 minutes long, roughly. I'm attaching the brief and also the outline of how I want it to go. Please start writing the VSL right now. If you need to do this over multiple outputs, that's fine. Whenever you run out of room, simply let me know and I'll prompt you to continue.
```

- **Why two models:** "What if Claude's being weird? What if Claude's down?… You need to be kind of multimodal." [07-01 v1 41:15–43:39](../lessons/07-01-long-form-vsl.md) In the eye-serum run, Gemini wrote the more authentic lead and the better UMP scene. Claude, which had reference VSLs, wrote the better close. [07-01 v2 02:58; v2 29:10](../lessons/07-01-long-form-vsl.md)
- **Check before moving on:** the draft is complete, from the lead through the CTAs and FAQ. Read the leads first, because they carry the hook and the open loops. [07-01 v1 44:48](../lessons/07-01-long-form-vsl.md)

### Step 6 — Edit as copy chief: merge, patch, second-model review
- **Input:** one or two drafts.
- **Output:** one master script.
- **Merge:** compare section by section (pre-lead close, lead opener, future pacing, qualifier, testimonial teases, background, UMP scene, UMS, buildup, close) and keep the better text per section. The full merge log is in [07-01 Key ideas §4](../lessons/07-01-long-form-vsl.md).
- **Patch by chat, not by rewrite.** Prompts (spoken, approximate):
  - Ingredients mapped to the steps, [07-01 v3 26:53–29:55](../lessons/07-01-long-form-vsl.md):

```text
When we get to the product buildup, I'd like these amino acids referenced in this section as part of the three-step solution. We'll want to mention them again in the ingredient section of the close.

One thing that's not clear is which of these ingredients are related to step three. After all, we said it's a three-step system. How can we make this work? We can add other ingredients in the formula as optional.
```

  - Bridge and logic fixes, [07-01 v5 33:06; 43:25–44:52](../lessons/07-01-long-form-vsl.md):

```text
I think we need a better transition to real estate. It's kind of abrupt. Maybe we need a few lines to shift the mindset of the prospect so that they are focused on, and accepting of, real estate as a good solution. Something like: you probably think about real estate, but normally real estate requires X, Y and Z.

First, this section: my immediate objection is, oh, that's expensive. So maybe we remove it. After all, plenty of properties will come furnished.
Second, I'm not sure this makes sense because we're talking about arbitrage. We have to be clear before this that as more income comes in, they can use it to actually buy properties and own the assets, and even get property managers to do the work for them.
```

- **Second-model review of a section,** [07-02 v1 27:56–28:18](../lessons/07-02-medium-length-vsl.md) (dictated). Paste only the opening into Gemini:

```text
Here's the start of another version that comes from Dr. Schilling. Is there anything you'd change or edit with it?
```

- **Line-level checks** (from the 07-01, 07-02 and 07-03 reads):
  - [ ] No "assumes too much" lines that put the viewer on the defensive. [07-01 v1 48:29](../lessons/07-01-long-form-vsl.md)
  - [ ] No word that reveals the format early ("applying" → "using this breakthrough"). [07-01 v3 08:43](../lessons/07-01-long-form-vsl.md)
  - [ ] No narrowing qualifiers ("twice as educated"). [07-01 v5 15:59](../lessons/07-01-long-form-vsl.md)
  - [ ] No AI phrases ("reclaim their vitality"). [07-02 v1 12:36](../lessons/07-02-medium-length-vsl.md)
  - [ ] Every loop paid off. [07-02 v1 29:53](../lessons/07-02-medium-length-vsl.md)
  - [ ] The micro lead ends with a promise. [07-02 v1 26:26](../lessons/07-02-medium-length-vsl.md)
  - [ ] A bridge sits before the objection block. [07-02 v2 13:05](../lessons/07-02-medium-length-vsl.md)
  - [ ] A stance paragraph says what this is *not*. [07-01 v5 23:26](../lessons/07-01-long-form-vsl.md)
  - [ ] A product that could be confused with a saturated category is neutralised on first mention ("not turmeric"). [07-03 v2 07:06](../lessons/07-03-3-7-minute-vsl.md)
  - [ ] Ingredient doses are present. [07-01 v6 26:25–31:37](../lessons/07-01-long-form-vsl.md)
- **Ship threshold:** "get a great first draft, tweak, modify, edit, and ship." [07-01 v2 06:38](../lessons/07-01-long-form-vsl.md)
- **Check before moving on:** run [LLM output claim audit](../rubrics/llm-output-claim-audit.md); see [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md).

### Step 7 — Check the length
- **Input:** the master script.
- **Output:** a word count and runtime.
- Measure with a script timer (Edge Studio "Script Timer & Words" on screen). Don't trust the model: Claude claimed 8,500 words, the actual was 5,707, and the timer said about 31 minutes. [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md) "Claude just skews a little bit, thinks it's a little bit longer than it is." [07-02 v2 01:53](../lessons/07-02-medium-length-vsl.md)
- The error runs both ways (derived): the "3-minute" blood-sugar scripts are about 790-850 words, i.e. 5+ minutes at about 150 wpm. [07-03 Agent use](../lessons/07-03-3-7-minute-vsl.md)
- **Check before moving on:** the runtime sits within the target band, and you have allowed for the leads you will add.

### Step 8 — Leads and hooks as a separate step
- **Input:** the finished script + a hook list.
- **Output:** 3-4 alternate micro leads or pre-leads stacked at the top of the script (options 1-4). [07-01 v4 08:54–14:56](../lessons/07-01-long-form-vsl.md)
- **Procedure and prompts:** use [hook-generation-system](hook-generation-system.md), which covers Perplexity deep-research hooks, the hook project and "mistake"-type follow-ups. Short form of the course pattern, verbatim select message from [07-01 v4](../lessons/07-01-long-form-vsl.md):

```text
Great job, let's go ahead and do a new micro lead with [concept]. Let's keep it to about the same length as the current pre-lead/micro lead in the VSL I uploaded [as a PDF].
```

- **Check before moving on:** each lead fits the body's first beat; leads don't all lean on the mechanism ("more for the curiosity"). [07-01 v4 02:30–05:05](../lessons/07-01-long-form-vsl.md) Re-check the hook file for seed examples left over from another niche: Claude kept returning skincare hooks for an Airbnb offer. [07-01 v5 52:14](../lessons/07-01-long-form-vsl.md)

### Step 9 — One-lever variants and cut-downs
- **Input:** the approved script.
- **Output:** a test set. Each variant changes only the hook, CTA, narrator, mechanism or length.
- **Prompts (verbatim):**
  - Hook swap with a locked body, [07-03 v2](../lessons/07-03-3-7-minute-vsl.md) (doc):

```text
Okay great. Now I want to do another ad where everything after the Revelation/Education section is pretty much the same. But we do a different hook. In this case let's do this hook: Here's what happens to your blood sugar when you skip breakfast...
```

  - CTA swap, [07-04 v1](../lessons/07-04-short-vsl.md) screen 13:00:

```text
Okay thanks, let's do another version where the CTA is to click the ad and save up to 57% but we don't reveal the prices.
```

  - Cut-down of an existing VSL, [07-02 v2 00:28–01:53](../lessons/07-02-medium-length-vsl.md) (dictated):

```text
Here's a VSL I wrote for an Airbnb arbitrage coaching program. Can you take this and do a version that is 16 minutes long? Keep the three options for the openings, since each video would only have one of those options. So that should be taken into account. It should be the same VSL, just strategically cutting things down to make it fit the length.
```

  - Narrator swap: see P3 in [07-02](../lessons/07-02-medium-length-vsl.md) (founder → expert with a new background story, set in the prompt, not the brief). [07-02 v1 03:31–06:55](../lessons/07-02-medium-length-vsl.md)
  - Mechanism swap, keeping everything else: [07-04 v1 06:46–07:21](../lessons/07-04-short-vsl.md).
- **Check before moving on:** the diff between variants is exactly one lever. This is a variation test; see [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md).

### Step 10 — Claim audit and placeholder replacement
- **Input:** every script that is going out.
- **Output:** a script where every claim is either verified from the brief's real sources or marked `[VERIFY: …]` / removed.
- Run [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) and [vsl-review](../rubrics/vsl-review.md). Replace `[placeholder]` testimonials and case studies only with real, documented ones. [07-01 How to apply](../lessons/07-01-long-form-vsl.md)

## Per-length variants

| Band | Project band (instruction text) | Typical use in course | Brief usage | Hook timing | Default CTA | Second model? | Sources |
|---|---|---|---|---|---|---|---|
| Long | 25-60 min | Landing-page VSL; ClickBank-type traffic; book-a-call biz-opp | Full brief, audited; big idea required | Body first; leads after the draft | Buy (price reveal, 3 packages) or book a call | Yes, merge by section | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-01](../lessons/07-01-long-form-vsl.md) |
| Medium | 6-16 min (requests went to 18) | On-page or in-feed; narrator tests | Full brief; narrator override in the prompt | Body first; test leads in front | Buy, or book a call + roadmap | Yes, at least on the lead | [07-02](../lessons/07-02-medium-length-vsl.md) |
| 3-7 min | 3-7 min | "Almost always" in-feed Meta video ads | Brief optional detail, but attach it before mechanism and proof | **Hook first**, then outline | Watch the full presentation / read report; brand and product unnamed | Not shown | [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-03](../lessons/07-03-3-7-minute-vsl.md) |
| Short | 1-4 min (spoken "almost all one to two minutes") | Short in-feed ads | Brief or an existing script; "some of what is in the brief won't need to make it" | **Hook first** or 10 concepts → pick | Shop now / click to save / watch presentation / book a call | Not shown | [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-04](../lessons/07-04-short-vsl.md) |

Course channel note: long VSLs suit ClickBank-type traffic; for Meta "I would probably shoot for a shorter video ad". [07-01 v2 34:11–35:17](../lessons/07-01-long-form-vsl.md) Placement detail: [04-11](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md). Length ranges across sources and the 16-05 benchmarks: [VSL length bands](../concepts/vsl-length-bands.md).

### Long form (25-60 min) — 07-01
- **Sequence:** run Steps 1-10 in full. This is the only band where the course shows the swipe test, the two-model merge and the stacked leads.
- **Course outline (eye serum, 27-minute target):** micro lead 1:00 → lead with open loops 4:00 → background story 4:00 → expert meeting and UMP 4:00 → UMS 4:00 → product buildup and reveal 5:00 → close (details, value) 4:00 → price justification 1:30 → CTAs 1/2/3 → FAQ 1:00. Planned times sum to about 29:45 (derived). [07-01 Steps table](../lessons/07-01-long-form-vsl.md)
- **Book-a-call variant:** no price. Hook and pattern interrupt → problem agitation → case-study teasers repeated through the script → speaker journey → revelation → solution → proof → future pace → who it is / is not for → application process → scarcity → CTA. [07-01 v5 07:43–09:24](../lessons/07-01-long-form-vsl.md)
- **Supplement variant:** after the UMS, add ingredients ("I also found X ingredient that works by doing Y…") and list each compound with a benefit line and its dose. [07-01 v6 20:26–31:37](../lessons/07-01-long-form-vsl.md) The "here are studies proving it" part needs real, product-relevant studies, or it gets cut.
- **Classic structure:** Stefan attached it per chat and did not store it in the project: "I'd rather just do it each time." [07-01 v6 11:00–12:56](../lessons/07-01-long-form-vsl.md)

### Medium (6-18 min) — 07-02
Three pipelines. [07-02 Steps](../lessons/07-02-medium-length-vsl.md)
- **A. Brief → script with a narrator test.**
  1. Outline prompt (Step 3), with the narrator override in the same prompt (P3).
  2. Classic-structure remix (Step 4).
  3. Save the outline; write.
  4. Read aloud.
  5. Second-model review of the opening.
  6. Test other leads in front of the same body ("the body is stable; the lead is the variable").
- **B. Existing long VSL → medium.** Cut-down prompt (Step 9). Keep the alternate openings. If the model drifts (new persona, odd hooks), re-run the identical prompt in another model. [07-02 v2 01:53–05:13](../lessons/07-02-medium-length-vsl.md)
- **C. Brief → 9-minute book-a-call.**
  - Prompt, verbatim, [07-02 v2 09:35](../lessons/07-02-medium-length-vsl.md) (the end of the sentence is cut off on screen):

```text
Here's the brief for an Airbnb Arbitrage Coaching program. This is for problem aware people, so we don't want to lead out with airbnb arbitrage. Can you please give me the outline for a medium length VSL that's 9 minutes in total. Note the call to action will be to book a call and get a roadmap, not to sell th[e program].
```

  - Outline: Hook 0:00-0:30 → Problem agitation → Solution intro → Proof → Mechanism deep dive → Skepticism 7:00-8:00 → CTA 8:00-9:00.
  - Repair the abrupt jump into objections with a bridge. [07-02 v2 13:05–14:18](../lessons/07-02-medium-length-vsl.md)
- **Narrator default:** for health-adjacent mechanism VSLs Stefan leans toward "more like an expert viewpoint", while saying you "could test" the founder. [07-02 v1 10:43](../lessons/07-02-medium-length-vsl.md)

### 3-7 minute — 07-03
1. Concepts or hook list first. Prompt, typed on screen + SRT, [07-03 v1 00:30–02:14](../lessons/07-03-3-7-minute-vsl.md):

```text
This is a VSL Brief for a skincare product. For 3-7 minute VSLs we might not need all of the information here. Right now I want 5 VSL concepts from you. I want them to come from Dr. Schilling as the spokesperson. Set it up with Laura. [Let's assume the CTA is going to be to watch the video. Don't talk about the brand or product at all. Go ahead and give me some concepts now, please.]
```

2. Pick a hook, paste it verbatim, give the length and ask for an outline. Prompt, verbatim, [07-03](../lessons/07-03-3-7-minute-vsl.md) doc:

```text
Here's a brief for a blood sugar supplement offer. Please come up with an outline for a 3 minute video ad. It will go to the longer VSL, so the CTA of this video ad will be to get people to go watch the full presentation. Let's also make the ad fairly educational while still having lots of curiosity and some promises. Let's use the following as the opening hook: Stop drinking coffee until you see what it's really doing to your blood sugar...
```

3. If you forgot the brief, attach it and lock the approved part. Prompt, verbatim:

```text
So I love this, but here's the brief (which I forgot to attach) so we can make that solution tease dialed in. Please don't change anything up to the Revelation/education section.
```

4. Fix the outline (rename the mechanism, add the "not turmeric" line, repair the Nope sequence), then send "Thanks please write the ad." [07-03 v2 06:35–08:05](../lessons/07-03-3-7-minute-vsl.md)
5. Hook-swap variants (Step 9). Then ask for a 1:30 sibling ("Now please do a 1 minute and 30 second version") and a more-mechanism vs less-mechanism cut. [07-03 v1 08:32–10:26](../lessons/07-03-3-7-minute-vsl.md)

- **Skeleton:** Hook + Nope sequence 0:00-0:15 → hook-specific problem 0:15-1:00 → Revelation/Education (UMP) 1:00-2:00 → Proof 2:00-2:30 → CTA 2:30-3:00. Every section after the problem block stays identical across variants. [07-03 Steps](../lessons/07-03-3-7-minute-vsl.md)
- **Nope-sequence template:** "[Hook line]. You think [belief 1], right? Nope. What about [belief 2]? Nope. How about [belief 3]? Still nope. Here's what's really [sabotaging] your [outcome]…". Keep the beliefs logically tied to the hook. [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md)
- 3-7 minute ads are "pretty mechanism heavy" (UMP analogy, why alternatives fail, solution tease). [07-03 v1 04:50](../lessons/07-03-3-7-minute-vsl.md)

### Short (90 s – 4 min) — 07-04
1. Set the destination and the maximum length. [07-04 v2 00:01](../lessons/07-04-short-vsl.md)
2. Load the brief, the product page URL or an existing VSL.
3. State awareness.
4. Get concepts or paste a hook.
5. Outline (optional) or "write it".
6. Edit lines in plain language.
7. Make one-lever variants.
8. Save every script and conversation. [07-04 Steps table](../lessons/07-04-short-vsl.md)

- **Prompts (verbatim):**
  - Concepts from a product page, [07-04 v1](../lessons/07-04-short-vsl.md) screen 02:00:

```text
Help me come up with 10 short VSL concepts for:
[product page URL]

Let's have all of them speak about the product and the call to action is to "shop now"
```

  - Concepts from a brief, [07-04 v1](../lessons/07-04-short-vsl.md) screen 11:00:

```text
here's a VSL Brief. Please give me 5 short VSL concepts that are 2 minutes maximum each. They don't have to come from Laura, and some of what is in the brief won't need to make it into these VSLs since they'll be short.
```

  - Existing VSL cut to a book-a-call ad, [07-04 v2](../lessons/07-04-short-vsl.md) screen 02:00:

```text
Please make a 2 minute version of this with the CTA to book a call still.
```

  - Sell-the-click concepts from a long script, [07-04 v4](../lessons/07-04-short-vsl.md) screen 06:00:

```text
here's a script for a financial VSL. Right now I want to write a series of 2 minute long VSL ads that sell the click [so that someone watches, is hooked, and the call to action is to go watch the full presentation.] Please give me 10 short two-minute VSL concepts right now.
```

- **Tease-don't-teach body** for presentation CTAs: one hook, then 4-5 "TEASE" beats (event, opportunity, consequence, timeline), then an urgent CTA. Fix instruction (audio, partly reconstructed): "Let's make it more teasing… Let's not [give away] so much." [07-04 v4 08:45–09:47](../lessons/07-04-short-vsl.md) See [sell the click](../concepts/sell-the-click.md).
- **Hook relevance edit:** "Your makeup artist can tell your real age" became "Here's why makeup artists can…" because "it's not like everyone has a makeup artist." [07-04 v1 04:17](../lessons/07-04-short-vsl.md)
- **Product-page shortcut:** the short project worked from a live product page URL without a brief. Stefan later re-ran from the brief to swap the mechanism. [07-04 v1 02:00; 06:46](../lessons/07-04-short-vsl.md)

## Decision points

| IF | THEN | Source |
|---|---|---|
| The brief's mechanism contradicts its own analogy, or the brief carries hooks or big ideas you don't want echoed | Fix or delete them in the brief before any VSL prompt | [07-01 v1 00:58–11:31](../lessons/07-01-long-form-vsl.md) |
| The mechanism is plain and nothing would make someone watch 25+ minutes | Add a big idea to the brief first (ritual, hack, teaser line) | [07-01 v6 00:00–09:36](../lessons/07-01-long-form-vsl.md) |
| The source VSL is ours and proven | A close self-swipe into the new category is acceptable | [06-01 09:15](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| The source VSL is a competitor's | Composite only; the swipe test is for viewing structure, never shipping | [06-01 09:15–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md); AGENTS.md |
| Target ≥ 6 min | Body first (outline → draft), leads after | [07-01 v1 10:26–11:31; v4](../lessons/07-01-long-form-vsl.md) |
| Target ≤ 7 min, in-feed | Hook first, pasted verbatim, then outline | [07-03 v1 04:50](../lessons/07-03-3-7-minute-vsl.md); [07-04 v1 02:04](../lessons/07-04-short-vsl.md) |
| Destination is a longer VSL or presentation | No brand or product; tease the breakthrough; CTA "watch the full presentation" | [07-03 v1 01:47](../lessons/07-03-3-7-minute-vsl.md); [07-04 v1 13:54](../lessons/07-04-short-vsl.md) |
| Destination is a call (coaching or biz-opp) | No price; qualification ("who it's not for"); application/roadmap CTA | [07-01 v5 05:02; 47:44](../lessons/07-01-long-form-vsl.md); [07-02 v2 09:03](../lessons/07-02-medium-length-vsl.md) |
| Destination is a product page | Name the product; "shop now" or "click to save X%" (price hidden) | [07-04 v1 12:15–13:54](../lessons/07-04-short-vsl.md) |
| Traffic is mostly problem-aware | Don't lead with the category or vehicle; lead with the problem and insight | [07-01 v5 05:02](../lessons/07-01-long-form-vsl.md); [07-02 v2 09:03](../lessons/07-02-medium-length-vsl.md) |
| You already have a long VSL you like | Cut it down; keep alternate openings | [07-02 v2 00:28; 08:03](../lessons/07-02-medium-length-vsl.md) |
| You want a narrator test | Override the narrator and backstory in the prompt; keep offer and mechanism identical | [07-02 v1 06:55](../lessons/07-02-medium-length-vsl.md) |
| An element could be mistaken for a saturated category (e.g. turmeric) | Neutralise it on first mention | [07-03 v2 07:06](../lessons/07-03-3-7-minute-vsl.md) |
| The hook promises a specific explanation | Check the mechanism pays it off; otherwise change the hook | [07-04 v1 08:09–08:18](../lessons/07-04-short-vsl.md) |
| The draft is decent | Edit and ship; stop agonising over model choice | [07-01 v2 05:30–06:38](../lessons/07-01-long-form-vsl.md) |

## Failure modes and fixes

| Failure | Symptom | Fix | Source |
|---|---|---|---|
| Swipe output nonsensical or a near-copy | Invented "Sarah, 47, Phoenix"; competitor lines and "Harvard and Yale" carried over | Delete and re-upload a cleaned brief; switch model version; abandon the swipe for the composite | [07-01 v1 17:08–24:54](../lessons/07-01-long-form-vsl.md) |
| Brief forgotten | Outline built from the examples alone; solution tease off-offer | Attach the brief; "Please don't change anything up to [section]" | [07-03 v2 04:37–05:10](../lessons/07-03-3-7-minute-vsl.md); [07-02 v1 07:05](../lessons/07-02-medium-length-vsl.md) |
| Model glitch or stale output | Wrong persona ("this guy, Rick"), repeated old output, wrong-niche hooks | Same prompt in another model (Gemini via Poe) or version (Sonnet 4 ↔ 3.7) | [07-02 v2 01:53–05:13](../lessons/07-02-medium-length-vsl.md); [07-01 v5 59:16–1:01:18](../lessons/07-01-long-form-vsl.md) |
| Seed-niche contamination | Hook file still holds skincare seed lines, so the model returns skincare hooks for a biz-opp | Swap the seed examples, or label them "from a different niche" | [07-01 v5 52:14](../lessons/07-01-long-form-vsl.md) |
| Output truncated | Script stops mid-section | Reply "continue" | [06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Length wrong | Model's word or time estimate is off (8,500 claimed vs 5,707 actual; "3-minute" scripts at 790-850 words) | Count words, use a script timer; re-prompt with the target | [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md); [07-03](../lessons/07-03-3-7-minute-vsl.md) |
| Lead assumes the viewer's state | "If you're watching this… you're living it too"; "trapped in the corporate rat race" | Soften to "where a lot of people probably are right now" | [07-01 v1 48:29; v5 24:56](../lessons/07-01-long-form-vsl.md) |
| Curiosity leak | Lead reveals the format or product ("applying this every morning") | Replace with a neutral noun ("using this breakthrough") | [07-01 v1 47:26–48:29](../lessons/07-01-long-form-vsl.md) |
| Unpaid loop | A teased fascination never returns | Ask for a different fascination "that does get paid off later" | [07-02 v1 29:53–30:37](../lessons/07-02-medium-length-vsl.md) |
| Abrupt transition | Jump from mechanism/system into objections, or from "be asset rich" to real estate | Ask for a bridge / mindset-shift lines | [07-02 v2 13:05](../lessons/07-02-medium-length-vsl.md); [07-01 v5 33:06](../lessons/07-01-long-form-vsl.md) |
| Steps not mapped to ingredients | The "three-step system" has only two grounded steps | Ask which ingredients map to each step; re-list them in the close with doses | [07-01 v3 28:22–29:55; v6 31:37](../lessons/07-01-long-form-vsl.md) |
| Illogical Nope sequence | "Too much sugar doesn't cause diabetes? Nope" | Rewrite the beliefs around the hook's own topic | [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md) |
| Hooks all lean on the mechanism | Every lead concept explains the UMP | "More for the curiosity"; ask for "mistake"-type hooks | [07-01 v4 02:30–08:54](../lessons/07-01-long-form-vsl.md) |
| Hook off-promise | Financial hooks about FDA and disease instead of the investment | Refocus on the offer's real promise | [07-04 v4 02:51–03:39](../lessons/07-04-short-vsl.md) |
| Too much explanation in a short ad | Short ad teaches the mechanism instead of selling the click | "Make it more teasing… let's not give away so much" | [07-04 v4 08:45](../lessons/07-04-short-vsl.md) |
| Invented proof | Testimonials, "clinical studies", "Harvard", review counts, income numbers, "before it's taken down" | Delete or `[VERIFY: …]`; real proof only | See [Compliance](#compliance) |

## Output contract
Every run returns:
1. **Outline file** `<offer>_<length>min_outline_v<n>`: sections with planned times, the model's length estimate, the narrator, the CTA and the awareness level.
2. **Script file** `<offer>_<length>min_script_v<n>`: lead options numbered at the top (long and medium), the body, CTAs and FAQ. Our convention, not from the course: put each section header with its target time in brackets.
3. **Change log:** merged-from (model per section), patches applied, measured words and runtime.
4. **Variant set** (3-7 min and short): one row per variant with the lever changed (hook / CTA / narrator / mechanism / length) and everything else identical.
5. **Claim list:** every factual claim with its source in the brief or `[VERIFY: …]`; placeholders listed; the [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) result.

## Compliance
The course runs this framework on a cosmetic eye serum, a blood-sugar supplement, a biz-opp coaching offer and a financial newsletter. The generated scripts contain claims that fail FTC/FDA/Meta rules. The lesson pages list them in full: [07-01 Compliance check](../lessons/07-01-long-form-vsl.md), [07-02](../lessons/07-02-medium-length-vsl.md), [07-03](../lessons/07-03-3-7-minute-vsl.md), [07-04](../lessons/07-04-short-vsl.md). **Structure only; claims not reusable.**

| Course example content | Status | Compliant pattern |
|---|---|---|
| "Harvard"/"Harvard and Yale" researchers; "Dr. Blaine Schilling" endorsement; "Harvard-trained endocrinologist"; "Dr. [Expert Name]" | Personas and credentials from the course world or invented by the model. Stefan himself: "I have to confirm if Harvard actually does" [07-03 v1 02:31](../lessons/07-03-3-7-minute-vsl.md) | Real, consenting expert with documented credentials, or a disclosed fictional character; otherwise `[VERIFY: expert name + credential]` |
| "Reverses", "reversing diabetes", "better than metformin", "stop taking insulin", "repairs cellular glucose doors" | Disease and drug-comparison claims. Stefan: "this isn't compliant. You can't compare yourself to a medication" [07-01 v6 09:35–13:09](../lessons/07-01-long-form-vsl.md) | Structure/function wording ("supports healthy blood sugar levels already within normal range" `[VERIFY: substantiation]`); no disease, cure or drug comparisons |
| "Clinical studies", 32%/39%/134% figures from single-ingredient studies | Ingredient data presented as product results. "We can't say clinical studies" [07-03 v1 09:56](../lessons/07-03-3-7-minute-vsl.md) | Attribute to the ingredient study with its citation, or `[VERIFY: product-level study]` |
| Testimonials (Carol, Elizabeth, Patricia, Margaret…), "5,800 happy customers", "4.8 stars / 3,400 reviews" | Copied from the brief or invented | Real reviews with permission; real counts from the store |
| "$8,000 a month", "$2.3 million portfolio", "85% success rate", students "Sarah… $3,200 monthly" | Biz-opp income claims. Stefan: fake testimonials and income claims are "the one big thing the FTC goes after for a biz opp. But this is for demonstration purposes" [07-01 v5 10:48](../lessons/07-01-long-form-vsl.md) | Documented results + typical-results disclosure; `[VERIFY: …]` |
| Peter Thiel/Mark Cuban investments, "leaked memo", "10x, 20x" | Fabricated endorsements and return promises | Don't use; financial promos need counsel review |
| "Supplies are limited", "sold out twice", "before it's taken down", "only 500 new patients" | Fake scarcity | True deadlines and stock levels only |

**Hard stops under repo rules (AGENTS.md: never invent proof):**
- "For demonstration purposes" placeholders [07-01 v5 10:48](../lessons/07-01-long-form-vsl.md) never reach a live script as anything but `[placeholder]`.
- An LLM "would just make less aggressive claims, especially if you told it to" [06-01 07:48–08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md) is not a safeguard by itself. Run the claim audit every time.

## Worked examples
- **Unity Eye Serum, long form (27-min target).**
  - Brief audit → swipe test (rejected) → outline with three rounds of feedback → Claude and Gemini drafts → section merge → ingredient patch → 5,707 words / about 31 min → three extra micro leads.
  - Final: 6,575 words, four pre-lead options.
  - [07-01 v1–v4](../lessons/07-01-long-form-vsl.md)
- **Airbnb arbitrage, book-a-call (25 min → 16 min → 9 min → 2 min).**
  - Long book-a-call VSL: [07-01 v5](../lessons/07-01-long-form-vsl.md).
  - Cut to 16 min, and a separate 9-min version from the brief: [07-02 v2](../lessons/07-02-medium-length-vsl.md).
  - 2-min cut plus five 2-min hook-led scripts: [07-04 v2](../lessons/07-04-short-vsl.md).
- **Blood-sugar supplement.**
  - Big idea added to the brief → long outline with ingredient patches: [07-01 v6](../lessons/07-01-long-form-vsl.md).
  - 3-min ads with a locked body and three hooks (coffee, skipped breakfast, laundry detergent): [07-03 v2](../lessons/07-03-3-7-minute-vsl.md).
  - 90-s versions: [07-04 v3](../lessons/07-04-short-vsl.md).
- **Eye serum, medium.**
  - Laura-narrated 18-min script, then an expert-narrated version with a patient backstory.
  - Classic-structure remix; Gemini rewrite of the micro lead.
  - [07-02 v1](../lessons/07-02-medium-length-vsl.md)
- **Financial newsletter.**
  - Long VSL as a declared swipe of the Agora structure: [05-05](../lessons/05-05-financial-promo-example.md).
  - Ten 2-min sell-the-click concepts → tease rewrite → newscaster and "Don't buy Big Pharma stocks" variants: [07-04 v4](../lessons/07-04-short-vsl.md).

All five are course examples whose claims are not reusable. Copy the sequence and section beats only.

## Where it's taught
- [06-01 Claude VSL projects setup](../lessons/06-01-claude-vsl-projects-setup-overview.md): four projects [00:00–03:56]; instruction pattern [02:55–04:24]; knowledge inventory [05:46–08:18]; composite vs swipe [08:18–10:13]
- [07-01 Long-form VSL](../lessons/07-01-long-form-vsl.md):
  - brief audit [v1 00:00–11:31]
  - swipe test [v1 12:28–28:33]
  - outline gate [v1 28:33–40:12]
  - two models and merge [v1 40:12–v3 33:03]
  - leads [v4]
  - book-a-call [v5]
  - blood sugar [v6]
  - financial note [v7]
- [07-02 Medium-length VSL](../lessons/07-02-medium-length-vsl.md): narrator swap [v1 02:28–07:58]; classic remix [v1 07:50–11:58]; second-model lead [v1 25:30–31:40]; cut-down [v2 00:00–08:03]; 9-min [v2 08:03–17:58]
- [07-03 3-7 minute VSL](../lessons/07-03-3-7-minute-vsl.md): concepts → hook → outline [v1 00:00–08:04]; shorter and mechanism-depth tests [v1 08:33–11:05]; hook-swap factory [v2 00:00–12:52]
- [07-04 Short VSL](../lessons/07-04-short-vsl.md): destination [v2 00:01]; one-lever variants [v1 10:49–14:45]; hook sources [v4 00:00–01:47]; tease-don't-explain [v4 08:45–15:04]
- Upstream: [05-02 Brief generator, length-project prompts](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) [24:24; 33:36]; [05-05 Financial promo](../lessons/05-05-financial-promo-example.md) [13:18–15:16]
- Structure theory: [04-02](../lessons/04-02-vsl-fundamentals-classic-structure.md) to [04-06](../lessons/04-06-vsl-closes.md); [04-08 medium structures](../lessons/04-08-medium-vsls-structures-and-examples.md); [04-09 short structures](../lessons/04-09-short-vsls-structures-and-examples.md)

## Cross-course notes
- **Evolve Copywriting, [video ad script workflow](../../../evolve/copywriting/frameworks/video-ad-script-workflow.md).** Evolve writes each ad from a short ad brief with a human first draft. RMBC has the model draft from an offer-level brief while the human copy-chiefs. Agreement: both treat the hook as the main test variable and change one thing at a time. RMBC adds the outline gate, the two-model merge and the locked-body hook swap.
- **Evolve, [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md).** Both keep the human as editor. RMBC's position is the stronger one: model output beats "99% of copywriters" (instructor claim, [07-01 v2 05:30](../lessons/07-01-long-form-vsl.md)). Agent default: never ship an unedited first draft; run Step 6 and Step 10.
- **Evolve, [open loops](../../../evolve/copywriting/concepts/open-loops.md), [bridges](../../../evolve/copywriting/concepts/bridges.md), [objection handling](../../../evolve/copywriting/concepts/objection-handling.md).** These match the RMBC edit checks (pay off loops, bridge before objections). Use the Evolve pages for line-level technique.
- **Evolve, [unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md).** The mechanism enters this framework only through the brief; RMBC's mechanism work is in [ump-ideation-and-evaluation](ump-ideation-and-evaluation.md).
- **Tether shared, [iteration vs variation](../../../../concepts/iteration-vs-variation.md).** The hook-swap and CTA-swap steps are variation tests on one variable.

## Related
- Concepts: [RMBC pipeline](../concepts/rmbc-pipeline.md) · [Claude project recipe](../concepts/claude-project-recipe.md) · [Composite vs swipe](../concepts/composite-vs-swipe.md) · [Classic VSL structure](../concepts/classic-vsl-structure.md) · [VSL length bands](../concepts/vsl-length-bands.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Sell the click](../concepts/sell-the-click.md) · [Modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md) · [Brief 2.0](../concepts/brief-2-0.md) · [Compliance red flags](../concepts/compliance-red-flags.md)
- Frameworks: [brief-generator](brief-generator.md) · [hook-generation-system](hook-generation-system.md) · [advertorial-build](advertorial-build.md) · [ump-ideation-and-evaluation](ump-ideation-and-evaluation.md)
- Playbooks: [write-a-vsl-with-claude](../playbooks/write-a-vsl-with-claude.md) · [offer-to-funnel-end-to-end](../playbooks/offer-to-funnel-end-to-end.md)
- Rubrics: [vsl-review](../rubrics/vsl-review.md) · [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md)
- Libraries: [prompts](../libraries/prompts.md) · [templates](../libraries/templates.md) · [hooks](../libraries/hooks.md) · [benchmarks](../libraries/benchmarks.md)
