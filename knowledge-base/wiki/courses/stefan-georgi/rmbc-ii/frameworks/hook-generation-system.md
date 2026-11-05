---
title: "Hook Generation System (RMBC II)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
tags: [hooks, hook-database, adhd-super-hook, deep-research, perplexity, claude-project, sell-the-click, hook-swap, nope-ladder, creative-testing, micro-lead]
updated: 2026-11-02
---

# Hook Generation System
> Mass-produce hooks with deep-research LLM prompts, curate them into a hook database, load that database plus annotated winning ads into a Claude Project that writes hook-heavy "sell the click" ads, then multiply any winning script by swapping only the hook and tracking hook/lead/script IDs.

## 🤖 Agent use
- **Use when:** you need many hook lines for in-feed video ads or VSL leads; you are building a hook library for one of our brands; you need 1–3 min hook-heavy ads that send cold traffic to a VSL/presentation; you need hook-swap variants of a script that already works.
- **Inputs → outputs:** destination + CTA, awareness level, audience, pain-point list, 3–7 annotated winning ads, seed hooks, unified research brief or script (optional), first half of the VSL → raw hook lists (several LLMs) → curated **hook database** → Claude Project → 10 concepts with first-30-second hook stacks → written 1–3 min scripts → hook-swap variants → tracked creatives (Script ID, Lead ID, Hook ID).
- **Rules:**
  - **DO** decide the destination before writing a hook: watch a longer presentation, book a call, or shop now. [07-04 v2 00:01–00:31](../lessons/07-04-short-vsl.md)
  - **DO** ask for fragments, not closed-loop fascination bullets: "like the first half of a puzzle but not the completed puzzle". [04-10 38:26–39:22](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DO** run the same research prompt in several LLMs and copy only keepers into one hook database doc. [04-10 32:59; 36:46](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DO** state the awareness level in every hook prompt ("mostly problem aware and solution aware"). [07-03 v2 00:00–00:35](../lessons/07-03-3-7-minute-vsl.md); [07-04 v4 00:00–00:31](../lessons/07-04-short-vsl.md)
  - **DO** keep the product out of sell-the-click ads unless told otherwise, and feed the project only the first half of the VSL (through mechanism, promises, spokesperson). [04-10 47:10; 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DO** paste the chosen hook verbatim and lock the body ("everything after the Revelation/Education section is pretty much the same") for a one-variable hook test. [07-03 v2 08:58–09:35](../lessons/07-03-3-7-minute-vsl.md)
  - **DO** edit every AI script aloud; output is "98% of the way there". [04-10 53:30–54:02](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DO** tag every creative with Script, Lead and Hook IDs. [04-10 56:32–57:38](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DON'T** stack many new hooks onto a proven winner at once; add "one more at a time or two". [04-10 1:01:07–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DON'T** accept generic or "too aggressive" hooks; keep the idea, rewrite the wording. [04-10 34:37; 36:15](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-04 v1 10:49; v4 06:26](../lessons/07-04-short-vsl.md)
  - **DON'T** reuse course hooks, characters, stats or authorities (e.g. "87% of women", "Harvard researchers", "Dr. Schilling"). Copy the pattern, rewrite for our product. Run [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) on every hook.
  - **IF** you change niche **THEN** change only the audience line, the pain-point list, the "product" line and the seed examples; leave the rest. [04-10 44:02–45:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **IF** a hook promises a specific explanation **THEN** the mechanism must pay it off, or change the hook. [07-04 v1 08:09–08:18](../lessons/07-04-short-vsl.md)
- **See also:** [libraries/hooks](../libraries/hooks.md) · [libraries/prompts](../libraries/prompts.md) · [modular-creative-and-hook-swaps](../concepts/modular-creative-and-hook-swaps.md) · [sell-the-click](../concepts/sell-the-click.md) · [vsl-build-with-claude](vsl-build-with-claude.md) · [claude-project-recipe](../concepts/claude-project-recipe.md) · [Evolve: Hooks](../../../evolve/copywriting/concepts/hooks.md)

## What it is
A four-part pipeline Stefan Georgi demonstrated on a live call and reused across the VSL builds:
1. **Generate**: a deep-research prompt run in Perplexity, Gemini, Grok and OpenAI models produces hundreds of hook "fragments" for a market.
2. **Curate**: the best lines go into a flat Google Doc, the **hook database**.
3. **Write**: a Claude Project holding annotated winning ads plus the hook database writes "ADHD Super-Hook" ads: numerous hooks, several in the first 30 seconds, CTA = "you need to watch this". [04-10 45:07–48:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
4. **Multiply**: hold the body fixed and swap the hook, CTA or mechanism one at a time. [07-03 v2 08:58–09:35](../lessons/07-03-3-7-minute-vsl.md); [07-04 v1 13:54–14:45](../lessons/07-04-short-vsl.md)

Why it matters: "it's really going to come back down to the hook a lot" and hooks are "how you can generate endless ads" (instructor claim). [07-04 v1 02:04; 14:45](../lessons/07-04-short-vsl.md) In-feed VSLs open with "Hook or Multiple Hooks (Curiosity Heavy)" before education. [04-11 04:02–05:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)

## Inputs checklist
- [ ] Destination and CTA: presentation / VSL, book a call, or shop now. [07-04 v2 00:01–00:31](../lessons/07-04-short-vsl.md)
- [ ] Awareness level of the target traffic. [07-04 v2 05:47; v4 00:00](../lessons/07-04-short-vsl.md)
- [ ] Audience line + market pain-point list (from the [unified research document](../concepts/unified-research-document.md)).
- [ ] 3–7 annotated winning ads in the target format: speaker, spoken line, on-screen visual; Part I (opening hooks) vs Part II (core message). [04-10 16:05–17:03](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- [ ] 5+ seed hooks in the target style (from our own winners where possible).
- [ ] Optional: unified research brief or an existing script to attach. [07-01 v5 00:00–05:02](../lessons/07-01-long-form-vsl.md); [07-04 v4 00:31–00:50](../lessons/07-04-short-vsl.md)
- [ ] For ad writing: the pre-product half of the VSL / long page. [04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- [ ] Verified claim list for the product (what we can legally say). Missing → list it; do not guess.

## Steps

### Step 1 — Set the job
- **Input:** offer, funnel map.
- **Output:** one line: destination, CTA, awareness, max length, speaker(s), product shown or not.
- **Prompt:** none. Decide it; every later prompt repeats it.
- **Check:** CTA matches what the ad reveals. In 05-02 a hook ad asked to "save 57%" ended up selling the solution, not the VSL: "this has really run more to sell the solution than to sell the VSL". [05-02 42:17–43:17](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) See [sell-the-click](../concepts/sell-the-click.md).

### Step 2 — Collect and annotate swipe ads
- **Input:** hook-heavy video ads in the format (swipe tool + transcript).
- **Output:** "Ad Breakdowns" doc: per ad, line by line: speaker (generic role), line, visual. Mark **Part I. Opening Hooks and Attention Grabbers** vs **Part II** (root / core messaging). Keep a no-screenshot version for LLMs. [04-10 16:05–17:03; Ad Breakdowns doc](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Prompt:** none (manual or contractor work in the course).
- **Check:** each ad shows the devices to copy (speaker switches, commands like "watch this", visual pattern interrupts, repeated curiosity lines, credibility insertion). [04-10 17:03–24:20](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) Copy the device, never the lines or claims.

### Step 3 — Deep-research hook generation (first pass)
- **Input:** annotated ads + audience + pain points + seed hooks.
- **Output:** raw hook lists, one per model.
- **Tool/model:** run in several tools. 04-10 one-run results: Perplexity Deep Research "by far the best… 120 curiosity-driving hooks"; Grok and Gemini "a few good ones"; OpenAI "kind of sucked" at this step. [04-10 32:59–36:46](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) "Perplexity tends to give me the best hooks that I like." [07-01 v5 00:00–05:02](../lessons/07-01-long-form-vsl.md)
- **Prompt (full version, with annotated ads; course doc "2. Deep Research Hook Generation Prompt"; typos as in source):**
```text
I'm going to share the transcripts for several direct response video ads that run on meta. They are annotated to share what's happening on screen during different segments of the ad. What I want you to really pay attention to however is how much curiosity there is. Specifically, there are a TON of "hooks" throughout the VSL. It's constantly keeping the viewer interested and intrigued. In fact, I refer to this style of ad as an ADHD Super-Hook Ad.

[PASTE YOUR ANNOTATED AD TRANSCRIPTS HERE]

====

Now, let's get to your research assignment. What I want you to do is to leverage social media signals, beauty blogs, health and wellness blogs, and other websites to come up with as many different hook-driven statements and questions as you can for a skincare brand that targets women 35+. This can be based on trending skincare routines and rituals, beliefs the market has, etc.

The products the skincare brand sells doesn't matter, because you're only focus is on coming up with tons of different hooks that create curiosity and keep people glued to the video ad script.

That being said though, the general pain points of the market include: wrinkles, under eye bags, puffy bags around their eyes, dark circles around their eyes, etc. Additional pain points include saggy, crepe-like skin, turkey neck, forehead wrinkles, creases, and looking older than they feel.

Please help me come up with as many relevant hook-driven questions and statements that can be used in video ads as possible.

Note that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity.
```
  Edit for our niche: "skincare brand that targets women 35+", the pain-point paragraph, "the products the skincare brand sells". [04-10 44:37–45:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Prompt (short version, used when the tool cannot read the long PDF):** same assignment without the transcripts, ending "Here are a few examples to get you started:" + 5 seed hooks (course doc "3. Perplexity version"). [04-10 31:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Prompt (generalized version with awareness and an attached research brief; Airbnb arbitrage, course Google Doc, verbatim; seed list continues off-screen):**
```text
I want you to leverage social media signals, blogs, and other websites to come up with as many different hook-driven statements and questions as you can for an Airbnb Arbitrage Coaching program. We are targeting people who are mostly problem aware, but who may not know a lot about Airbnb arbitrage or real estate. This can be based on sentiment, what people believe about side hustles, income, making money, etc, hacks/tricks/loopholes people share, etc. I've attached a Unified Research Brief for you that will share more about the market. Just keep in mind who we are going after, which is, again, mostly problem aware people.

The specifics of the coaching program don't really matter, because your only focus is on coming up with tons of different hooks that create curiosity and keep people glued to the video ad script.

Note that for these statements, they can come from a UGC person, a spokesperson of the brand, etc. You don't need to come up with "who" the speaker is though for all of the statements, I'm mostly interested in pure hooks and curiosity.

Here are examples of good hooks and curiosity statements from the skincare space for inspiration:
[SEED HOOKS]
```
  Source: [07-01 v5 00:00–01:06](../lessons/07-01-long-form-vsl.md). The financial-newsletter version attaches the script and adds: "your job is NOT to only come up with hooks from the script, rather it is to find tons of different hooks that create curiosity and keep people glued to a shorter video ad that gets people to click a link and go watch the full presentation." [07-04 v4 00:31–01:00](../lessons/07-04-short-vsl.md)
- **Check:** subject of the hooks matches the product's real promise; seeds are from our niche or clearly labelled as style-only (see failure modes).

### Step 4 — Correct the batch in plain language
- **Input:** first-pass output.
- **Output:** a second batch in fragment form, or refocused on the right subject.
- **Prompt ("snippets" correction, course doc "3. Perplexity version", verbatim):**
```text
You know what I don't love about these? A lot of the hooks or curiosity statements are just like "snippets." You seem to be writing fascination/curiosity bullets almost. But in a video ad with a bunch of speakers, a lot of the hooks will be really fragmented. Speaker 1: might say "This is how often you should really be washing your face" and then a different speaker right after might say "What about sunscreen?" and a few lines later in the ad, another person might say "Is your pillowcase accelerating your wrinkles?"

So "imagine" that you're just writing phrases, hooks, and curiosity statements that can be injected throughout different ads. They don't need to be closed-loop Many can be more open-ended, like the first half of a puzzle but not the completed puzzle.
```
- **Prompt (subject refocus, financial run; on screen, ending from audio):**
```text
Thanks, these are okay. The one thing is: they really are focused on the FDA and like diseases and things like that. I think we want them to be more focused on the investment opportunity as well. So it's not about some new cure. It's about how new technologies or changes in healthcare or this FDA decision [or whatever else] are creating a once-in-a-generation opportunity.
```
  Source: [07-04 v4 02:51–04:00](../lessons/07-04-short-vsl.md)
- **Check:** "you're still sort of the conductor"; the value is in how fast you correct. [07-04 v4 04:17](../lessons/07-04-short-vsl.md)

### Step 5 — Build the hook database
- **Input:** all batches.
- **Output:** one doc: links to each research run at the top, then a flat list of hooks (the course's had ~90–109 lines). [04-10 35:24; 46:18](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Selection rules:** "Not all of them are good… you're picking using your judgment"; limit question-format lines ("I don't like a lot of questions"). [04-10 42:23–43:04](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) Flag hooks that raise a "how's it going to pay it off?" problem. [04-10 07:31](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Agent addition (derived):** add columns Hook ID | text | family | awareness | source model | claim needs proof? (Y/N + `[VERIFY: …]`) | status. Delete any line whose claim we cannot support.

### Step 6 — "Still MORE hooks" expansion (repeatable)
- **Input:** hook database pasted in.
- **Output:** 70–100+ new fragments per run; append keepers.
- **Tool/model:** run in two or more models. Best in 04-10: Gemini 2.5 Pro (experimental) and an OpenAI o1-pro-class model ("about 70" hooks). Stefan is "completely agnostic"; Claude is "probably still better than all the other ones on average" for copy. [04-10 39:22–41:47](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Prompt (course doc "5. prompt for generating still MORE hooks", verbatim):**
```text
Below are several hooks and curiosity-driven statements that can be used in video ads for a skincare brand:

Hooks

[PASTE YOUR HOOK DATABASE HERE: one hook per line]

===

Please notice that a lot of the hooks or curiosity statements are just like "snippets." They are NOT fascination/curiosity bullets. This is what I'm looking for right now, because in a video ad with a bunch of speakers, a lot of the hooks will be really fragmented. Speaker 1: might say "This is how often you should really be washing your face" and then a different speaker right after might say "What about sunscreen?" and a few lines later in the ad, another person might say "Is your pillowcase accelerating your wrinkles?"

So "imagine" that you're just writing phrases, hooks, and curiosity statements that can be injected throughout different ads. They don't need to be closed-loop Many can be more open-ended, like the first half of a puzzle but not the completed puzzle.

Please generate as many new hooks and curiosity-driven statements as you can right now.
```
- **Loop:** run deep research once; run this "as often as needed" ("do another 100"). [04-10 43:04](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### Step 7 — Build the hook-ad Claude Project
- **Input:** Ad Breakdowns doc + hook database (as project knowledge; 23% capacity in the course). [04-10 46:18](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Output:** a project that writes hook-heavy ads from short chat prompts ("I don't have to explain all this context"). [04-10 48:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Prompt (project instructions, course doc "6. Claude Project Setup and Prompt Examples", verbatim; replace "Skincare brand" and file names):**
```text
The goal is to write hook heavy meta ads for a Skincare brand.

I want these ads to follow what I call an ADHD Super-Hook Framework. What this means is that the ads will have numerous hooks throughout, including several in the beginning. In fact, the first 30 seconds of the ad especially should jump around a good amount.

As we go to write these ads, I want to incorporate numerous hooks into them (as mentioned). I also what to incorporate what I would call "curiosity driven statements."

Curiosity-driven statements would be statements are like hooks, but they could be anywhere in the video ad, and typically wouldn't be in question format.

You will see that document #1 is 1. CA Pro Copy of Ad Breakdowns (In-Depth). This has in-depth breakdowns of successful ads from other brands. You'll notice how hook heavy they are, especially the openings, and how they also incorporate visual elements that are used to continuously hook people in too.

Then you'll see that I've already included a list of hooks and curiosity driven statements as the second document. That document is titled: 4. CA Pro Version_Hook Database.pdf

You'll be tasked at various times with coming up with new hooks and curiosity statements, coming up with new ad concepts, and writing new ads.

Here's something very important: unless I SPECIFICALLY ask you for it, when writing ads do NOT talk about the product in the ad. Instead we want to tease a breakthrough/solution/ritual and the call to action is "you need to watch this" or "check out this video" etc. We're basically "selling the click" meaning we want to sell them on clicking the link, which will take them to the VSL and sell the product on that page.

Also, when writing ads, your goal is to incorporate numerous hooks into the opening and also throughout. You'll also include what I call "curiosity driven statements" where it's not a question, but a statement from the speaker (could be a UGC person, a doctor, or an AI Voiceover etc) that is curiosity heavy and catches someone's attention.
```
- **Agent addition (derived, required under repo rules):** append "Use only claims, proof and experts present in the attached documents. Put any statistic, study, credential or testimonial you would want in `[VERIFY: …]` brackets. No disease, cure or drug-comparison claims."
- **Optional:** add repeated viewer commands ("watch this", "you need to see this") to the instructions; the course planned this but did not show results. [04-10 19:57–20:53; 48:07](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### Step 8 — Get concepts, pick, write
- **Input:** first half of the VSL (PDF) attached in a new chat.
- **Output:** 10 concepts (name + 4–5 first-30-second hooks), then a full 1–3 min script with speaker labels and bracketed visuals.
- **Prompt (session opener, same doc, verbatim; typo "fist" in source):**
```text
We're going to write some new ads for our skincare brand Opal Beauty. I'm going to upload the fist half of the VSL so you get a little bit more context. Your goal is to write ads that are hook-heavy, have tons of curiosity, leverage the hook database, and ultimately "sell the click" to the VSL. We're also going to make all the ads between 1 and 3 minutes long for now.

To start, can you give me 10 ad concepts where you include the different hooks to be mentioned in the first 30 seconds? I'll then choose and have you write ads from there.
```
- **Follow-ups (spoken, reconstructed):** "ad concept number one. Go ahead and write that now" [04-10 04:42]; "give me 10 more concepts" / "please do concept number 15 now" [04-10 51:21]; transitions fix (spoken): "Good job with loading up the opening with hooks. I do think we need some better transitions between some of the hooks. So let's focus on better transitions between hook two and three and between three and four in the opening." [04-10 55:12](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Check:** read aloud; fix flow, speaker assignment (e.g. move a line from "Woman" to "Doctor"), wording. [04-10 52:30–54:02](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) Product never named unless asked. Run the claim audit: the course's raw output included "Clinical studies show visible improvements in wrinkle depth" and "I'm never going back to Botox". [04-10 05:37–06:32; 57:00](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### Step 9 — Alternative entry: hooks inside a VSL-length project
Use when you have a brief or script but no hook database yet.
- **3–7 min project:** "Right now I want 5 VSL concepts from you… Let's assume the CTA is going to be to watch the video. Don't talk about the brand or product at all." (partly reconstructed from SRT) [07-03 v1 00:30–02:14](../lessons/07-03-3-7-minute-vsl.md)
- **Short project:** "Help me come up with 10 short VSL concepts for: [product page URL] Let's have all of them speak about the product and the call to action is to "shop now"" [07-04 v1 02:00](../lessons/07-04-short-vsl.md); from a script: "Please give me 10 short two-minute VSL concepts right now." [07-04 v4 05:35–06:26](../lessons/07-04-short-vsl.md)
- **Brief generator:** "I need five ADHD hook ad concepts to choose from" (spoken, approximate). [05-02 39:21–41:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
- **Micro-lead hooks for a long VSL (hook project; verbatim + follow-ups):**
```text
Here's a new VSL script I wrote for a skincare serum. Please give me 10 hook-heavy lead concepts I could use for the micro lead. You can pull from the database plus ideas from the VSL. I'll then select the ones I want to turn into new pre-leads or leads.

[follow-up] Can you now do these where they're not all focused on the UMP so much? More for the curiosity. We talk about collagen breaking down. We don't need to talk about collagen architecture.

[select] Great job, let's go ahead and do a new micro lead with [concept]. Let's keep it to about the same length as the current pre-lead/micro lead in the VSL I uploaded [as a PDF].
```
  Source: [07-01 v4 00:00–08:54](../lessons/07-01-long-form-vsl.md). Result: 3 alternate micro leads pasted above the original for testing. [07-01 v4 08:54–14:56](../lessons/07-01-long-form-vsl.md)
- **Check:** if the project's batch is flat, the course found in-project generation can beat the research tool: "I'd rather just see what Claude comes up with first." [07-04 v4 05:14–07:32](../lessons/07-04-short-vsl.md)

### Step 10 — Hook-swap variants (lock the body)
- **Input:** an approved script/outline + a new hook from the database.
- **Output:** N scripts identical after the hook-specific section.
- **Prompt (3-minute ad, verbatim):**
```text
Okay great. Now I want to do another ad where everything after the Revelation/Education section is pretty much the same. But we do a different hook. In this case let's do this hook: Here's what happens to your blood sugar when you skip breakfast...
```
  Source: [07-03 v2 08:58–09:35](../lessons/07-03-3-7-minute-vsl.md)
- **Prompt (short ad, verbatim):**
```text
Okay great, let's do another version of this ad with a new hook. The hook will be: [NEW HOOK]. The rest of the ad from this point on can basically stay the same:
[paste of the rest of the outline]
```
  Source: [07-04 v3 05:43](../lessons/07-04-short-vsl.md)
- **Other one-lever swaps:** CTA ("let's do another version where the CTA is to click the ad and save up to 57% but we don't reveal the prices") and mechanism ("another version of this ad that keeps everything else the same… modified for the UMP/UMS in the brief"). [07-04 v1 06:46–07:21; 12:15–13:54](../lessons/07-04-short-vsl.md)
- **Check:** the hook's set-up lines (e.g. the "Nope" ladder) still make sense. Template: `[Hook]. You think [belief 1], right? Nope. What about [belief 2]? Nope. How about [belief 3]? Still nope. Here's what's really [doing X]…` [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md)

### Step 11 — Track, test, stack gradually
- **Input:** launched creatives.
- **Output:** tracking sheet with tabs Videos / Script Database / Lead Database / Hook Database; columns Creative, Status, Frame Link, Launch Date, Script ID, Lead ID, Hook ID, Creative Name, Winner?; name pattern `AD0001V15_SC001_LD003_SS5`. [04-10 56:32–57:48](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Test rule:** test hooks, then combine winners; on an ad that already works, "we'd add one more at a time or two". [04-10 1:00:08–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) Hook-level attribution inside a 15–20-hook stack was not solved: "I don't know that we have it down to the hooks specifically." [04-10 58:39](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Check:** winners' hooks go back into the database marked as tested winners (derived).

## Hook families seen in the course (patterns only; claims not reusable)
| Family | Pattern | Course instance (do not reuse wording) | Source |
|---|---|---|---|
| Habit threat + command | "Stop [common habit] until you [see/hear] this" | "Stop washing your face in the shower until you hear this" | [04-10 41:47](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-03 v2 03:25](../lessons/07-03-3-7-minute-vsl.md) |
| Costly mistake | "Don't make this $[X] mistake at [place]…" | "$400 mistake at the department store" | [07-03 v1 03:54–04:53](../lessons/07-03-3-7-minute-vsl.md); [07-01 v4 06:02–08:54](../lessons/07-01-long-form-vsl.md) |
| Nope ladder | Hook → three popular fixes each answered "Nope" → "Here's what's really…" | blood-sugar coffee / breakfast / detergent scripts | [07-03 v2 08:58–12:11](../lessons/07-03-3-7-minute-vsl.md) |
| Everyday-object villain | "The shocking connection between [object] and [problem]" / "Is your [object] secretly sabotaging…" | pillowcase, laundry detergent | [04-10 37:55](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-03 v2 11:04](../lessons/07-03-3-7-minute-vsl.md) |
| Failed-solutions contrast | "[Solution A], [B] and [C] all miss this one [hidden thing]" | "Eye creams, face taping, and Botox all miss this one invisible layer…" | [04-10 43:04](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Mechanism metaphor teaser | "What happens when your [body part] loses its '[metaphor]'…" | "Velcro effect" | [04-10 03:41](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Odd question | Short, unexpected question | "Does your skin have a bedtime?" | [04-10 43:04](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Viewer command + visual promise | "You need to see this [view] of what's happening to your [X] right now" | microscopic-view line | [04-10 04:12](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Time compression | "You may think this takes years… we'll teach it in 60 seconds. Watch this." | V Shred ad | [04-10 18:59](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Big-idea congruent (finance) | Hook built from the offer's big idea rather than generic "mistake" lines | "Don't buy Big Pharma stocks until you see this" | [07-04 v4 00:50–01:23; 11:16–12:19](../lessons/07-04-short-vsl.md) |

Full hook rows: [libraries/hooks](../libraries/hooks.md).

## Decision points
| IF | THEN | Source |
|---|---|---|
| Destination is a longer VSL/presentation | Sell the click: no product, tease the breakthrough, CTA "watch this" | [04-10 47:10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-03 v1 01:47–02:09](../lessons/07-03-3-7-minute-vsl.md) |
| Destination is book-a-call | Take an existing VSL option and ask for "a 2 minute version of this with the CTA to book a call still" | [07-04 v2 00:01–02:00](../lessons/07-04-short-vsl.md) |
| Destination is the product page / shop now | Concepts may speak about the product; CTA "shop now" or discount without prices | [07-04 v1 02:00; 12:15–13:54](../lessons/07-04-short-vsl.md) |
| Ad must not pitch the product | Upload only the first half of the VSL (through UMP, promises, spokesperson) | [04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Ad should name the product | Change the project instruction and supply the full page | [04-10 49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Ad is short (≤3 min) | Lean educational: "lots of curiosity and some promises" | [07-03 v2 01:10; 02:46](../lessons/07-03-3-7-minute-vsl.md) |
| Ad is 3–7 min | Make it "pretty mechanism heavy" | [07-03 v1 04:50–05:16](../lessons/07-03-3-7-minute-vsl.md) |
| Offer has a strong big idea (e.g. finance) | Generate hooks congruent with the big idea, not generic category hooks | [07-04 v4 00:50–01:23](../lessons/07-04-short-vsl.md) |
| Tool cannot read the long transcripts PDF | Use the short prompt with 5 seed hooks instead | [04-10 31:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Research-tool batch is flat | Ask the writing project for 10 concepts directly | [07-04 v4 05:14–07:32](../lessons/07-04-short-vsl.md) |
| An ad already wins | Add 1–2 hooks at a time; do not stack 10 | [04-10 1:01:07–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Body is approved | Vary one lever per variant: hook, CTA, mechanism, or product-vs-tease | [07-04 v1 06:46–14:45](../lessons/07-04-short-vsl.md) |
| A mechanism word could be confused with a saturated category | Neutralize it at first mention ("it's not turmeric") | [07-03 v2 07:06](../lessons/07-03-3-7-minute-vsl.md) |
| Model's runtime label looks short | Check words at ~150 wpm (derived; 07-03 "3-minute" scripts ran ~790–850 words) | [07-03 Agent use](../lessons/07-03-3-7-minute-vsl.md) |

## Failure modes and fixes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Hooks read as closed-loop fascination bullets | Default LLM style | Send the "snippets / first half of a puzzle" correction; use the MORE-hooks prompt | [04-10 32:59–39:22](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Hooks generic | First batch accepted | Rewrite or pull from the database | [07-04 v1 10:49](../lessons/07-04-short-vsl.md) |
| Hooks "too aggressive" or "probably not compliant" | Model chasing shock | Keep the idea, rewrite softer; drop unsupported stats | [04-10 36:15](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-04 v4 02:26–02:36; 06:26](../lessons/07-04-short-vsl.md) |
| Hooks on the wrong subject (disease/FDA for an investment offer) | Prompt sentiment sources too broad | Refocus prompt on the real promise | [07-04 v4 02:51–03:39](../lessons/07-04-short-vsl.md) |
| Output keeps returning another niche's hooks | Seed examples from the old niche left in the hook doc | Swap the seed list; label seeds as style-only or use our own | [07-01 v5 00:42; 52:14–1:05:28](../lessons/07-01-long-form-vsl.md) |
| Ad names the product or ingredients | Full VSL given as context | Give only the pre-product half | [04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Ad sells the solution, not the click | CTA offered a discount on the product | CTA = get more information / watch the presentation | [05-02 42:17–43:17](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Hook promise not paid off | Mechanism swapped under an old hook | Change hook or add the payoff | [07-04 v1 08:09–08:18](../lessons/07-04-short-vsl.md) |
| Hooks raise questions the ad can't answer | Unrelated curiosity line ("sugar and wrinkles") | Cut it or add the payoff | [04-10 07:31](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Nope ladder nonsensical after a hook swap | Model reused the old ladder's logic | Rewrite the three beliefs inside the new hook's villain category | [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md) |
| Solution tease doesn't match the offer | Brief not attached | Attach brief; "Please don't change anything up to the Revelation/education section" | [07-03 v2 04:37–05:10](../lessons/07-03-3-7-minute-vsl.md) |
| Jumpy transitions between stacked hooks | Hook density | Ask for better transitions between named hook numbers | [04-10 55:12](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Hook excludes most viewers | Assumes a situation few have ("your makeup artist") | Generalize ("Here's why makeup artists can…") | [07-04 v1 04:17](../lessons/07-04-short-vsl.md) |
| Invented doctors, studies, stats in output | Model fills proof slots | Replace with `[VERIFY: …]` or real proof; run the claim audit | [04-10 57:00](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-03 v1 02:31; 09:56](../lessons/07-03-3-7-minute-vsl.md) |

## Output contract
1. **Hook database** (doc): header links to each research run; rows `Hook ID | hook | family | awareness | source model | claim check ([VERIFY: …] or "none") | status (new / in test / winner / retired)` (columns beyond the course's flat list are derived).
2. **Concept list:** 10 × `concept name + 4–5 first-30-second hooks`.
3. **Script:** 1–3 min (or the length set in Step 1); speaker labels (UGC person, expert, AI voiceover…), bracketed visual directions, hook stack in the opening, curiosity statements in the body, CTA matching the destination; product absent if selling the click.
4. **Variant set:** N scripts differing in one lever; each with Script ID / Lead ID / Hook ID.
5. **Claim list:** every factual claim in the hooks and script mapped to a source or bracketed.

## Compliance
- The course's hook lists and generated ads contain unsubstantiated or regulated claims: "celebrities are secretly using this instead of Botox", "87% of women", "Harvard researchers", "Clinical studies show…", "I'm never going back to Botox", blood-sugar/insulin-resistance and diabetes claims, weight-loss testimonials from swipe ads, and invented experts ("Dr. Schilling", "Dr. [Expert Name]"). [04-10 Compliance flags](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-03 Compliance flags](../lessons/07-03-3-7-minute-vsl.md); [07-04 compliance table](../lessons/07-04-short-vsl.md) **Structure only; claims not reusable.**
- Stefan himself flags cleanup: "We can't say clinical studies. We're not doing clinical studies with the ingredient." [07-03 v1 09:56](../lessons/07-03-3-7-minute-vsl.md); "I have to confirm if Harvard actually does." [07-03 v1 02:31](../lessons/07-03-3-7-minute-vsl.md); he swaps a checkable "three weeks" for "recent" [07-04 v4 14:09](../lessons/07-04-short-vsl.md). Our rule is stricter: vagueness does not fix a false claim; only true, provable claims ship.
- Compliant pattern: curiosity from real habits, real mechanisms and real customer language; supplements use structure/function wording ("supports healthy [X]") with `[VERIFY: substantiation]`; experts only if real and consenting; no disease, cure, drug-comparison, income or scarcity claims without proof. See [compliance-red-flags](../concepts/compliance-red-flags.md) and [llm-output-claim-audit](../rubrics/llm-output-claim-audit.md).

## Worked examples
- **Opal Beauty / Unity Eye Serum hook-ad project (skincare):** four-model research → ~90-line database → project with 7 annotated ads → 16+ concepts ("The Velcro Effect", "The Microscopic Truth", "The Aging Time Bomb") → scripts edited for transitions and speaker. [04-10 02:45–55:44](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Blood-sugar supplement:** Perplexity research (78 hooks, 14 sections) → coffee hook → 3-min outline → brief attached, body locked → two hook swaps (skip breakfast, laundry detergent) with Nope-ladder fix; 90-second version swaps to a sleep-apnea hook. [07-03 v2 00:00–12:52](../lessons/07-03-3-7-minute-vsl.md); [07-04 v3 00:41–06:17](../lessons/07-04-short-vsl.md)
- **Airbnb arbitrage coaching:** research prompt with the unified research brief attached → five chosen hooks → five 2-minute book-a-call scripts; one hook hand-edited ("…instead of lining someone else's pocket"). [07-01 v5 00:00–05:02](../lessons/07-01-long-form-vsl.md); [07-04 v2 03:13–10:28](../lessons/07-04-short-vsl.md)
- **Financial newsletter:** Perplexity batch too disease-focused → refocus → still flat → Claude project gives 10 two-minute concepts → "more teasing" rewrite → new hook generated while reviewing ("Don't buy Big Pharma stocks until you see this"). [07-04 v4 00:00–15:04](../lessons/07-04-short-vsl.md)
- **Long-form VSL micro leads:** hook project returns "mistake" hooks → three alternate micro leads stacked above the original for testing. [07-01 v4 00:00–14:56](../lessons/07-01-long-form-vsl.md)

## Where it's taught
- [04-10 Using AI to Generate Endless Good Hooks](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md): V Shred breakdown [08:24–28:33]; research pipeline [28:33–45:07]; project [45:07–51:21]; iteration [49:52–56:32]; tracking and testing [56:32–1:02:35].
- [07-03 3-7 Minute VSL](../lessons/07-03-3-7-minute-vsl.md): concepts and hook pick [v1 00:30–05:51]; Perplexity hooks and hook-swap factory [v2 00:00–12:52].
- [07-04 Short VSL](../lessons/07-04-short-vsl.md): hook-first loop [v1 01:12–14:45]; Airbnb hooks [v2 03:13–10:28]; blood-sugar swap [v3 05:43]; financial hook correction [v4 00:00–15:04].
- [07-01 Long-form VSL](../lessons/07-01-long-form-vsl.md): micro-lead hook project [v4 00:00–15:55]; Airbnb hook prompt and lead swap [v5 00:00–05:02; 52:14–1:05:28].
- [05-02 Brief generator](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md): brief field 25 hooks [16:48–17:46]; ADHD hook-ad concepts [39:21–43:17].
- [04-11 VSLs on landing pages vs in-feed](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md): in-feed spine starts with hooks [04:02–05:01].

## Cross-course notes
- **Hook density (disagreement).** Evolve: one sticky hook with emotion, curiosity gap and stakes; "Curious NOT confused"; write a custom bridge per hook ([Evolve: Hooks](../../../evolve/copywriting/concepts/hooks.md), [Evolve: Bridges](../../../evolve/copywriting/concepts/bridges.md)). RMBC: many fragmented hooks, the first 30 seconds "should jump around a good amount" [04-10 45:07–45:41](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); Stefan concedes one script "jumps around a bit… I'd probably still test it" [04-10 50:50](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md). **Agent default:** for UGC/product ads, write one sticky hook + bridge (Evolve). For in-feed sell-the-click ads to a VSL, build the stacked version as a test variant against a single-hook control. Treat stack depth as a test variable, never a settled rule.
- **Hook swaps = one-variable tests.** Agrees with Tether [Iteration vs variation](../../../../concepts/iteration-vs-variation.md), [Creative testing system](../../../../frameworks/creative-testing-system.md) and Evolve [Iteration playbook](../../../evolve/copywriting/frameworks/iteration-playbook.md). RMBC adds locking the body by section name and ID-based tracking (SC/LD/SS).
- **Open loops.** RMBC's "first half of a puzzle" fragments are open loops by design; Evolve says close the loop as late as possible and always pay it off ([Evolve: Open loops](../../../evolve/copywriting/concepts/open-loops.md)). Combine: every fragment needs a payoff somewhere in the ad or on the destination page.
- **AI as idea engine.** Matches Evolve's operator view ([Evolve: AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md)); RMBC adds multi-model research runs and a persistent hook database.
- **Unaware traffic.** RMBC hooks are mostly built for problem/solution-aware traffic; for unaware hooks see [Evolve: Unaware ads](../../../evolve/copywriting/concepts/unaware-ads.md).
- Shared libraries: [Tether hooks library](../../../../libraries/hooks.md) · [Evolve hooks library](../../../evolve/copywriting/libraries/hooks.md) · [Curiosity gap heuristic](../../../../concepts/heuristics/curiosity-gap.md).

## Related
- [modular-creative-and-hook-swaps](../concepts/modular-creative-and-hook-swaps.md) · [sell-the-click](../concepts/sell-the-click.md) · [claude-project-recipe](../concepts/claude-project-recipe.md) · [llm-copy-chief-editing](../concepts/llm-copy-chief-editing.md) · [product-market-awareness](../concepts/product-market-awareness.md) · [unified-research-document](../concepts/unified-research-document.md)
- [vsl-build-with-claude](vsl-build-with-claude.md) · [brief-generator](brief-generator.md) · [deep-research-workflow](deep-research-workflow.md) · [paid-traffic-by-platform](paid-traffic-by-platform.md)
- [libraries/hooks](../libraries/hooks.md) · [libraries/prompts](../libraries/prompts.md) · [libraries/templates](../libraries/templates.md) · [rubrics/llm-output-claim-audit](../rubrics/llm-output-claim-audit.md) · [playbooks/write-a-vsl-with-claude](../playbooks/write-a-vsl-with-claude.md)
