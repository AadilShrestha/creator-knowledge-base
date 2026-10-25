---
title: "Prompt index: every prompt and AI instruction in Evolve Copywriting"
type: library
creator: evolve
course: copywriting
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/10-why-you-need-to-write-facts.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/13-why-you-need-to-write-at-a-6th-grade-level.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/34-how-to-write-with-labels-customer-language.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/36-what-about-ai.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/37-evolve-writing-prompts.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/44-prompts-to-help-you-storytell.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/56-positioning-exercise.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/59-visual-words.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/65-banger-static-ads-prompt.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/67-how-to-write-image-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/68-how-to-write-image-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/70-how-to-write-video-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/71-how-to-write-video-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/72-action-item-write-your-video-ad-briefs.md
tags: [library, prompts, claude, chatgpt, ai, research, angles, statics, video-scripts, iteration, labels, storytelling]
updated: 2026-10-21
---

# Prompt index (Evolve Copywriting)
> The index of every prompt and AI instruction in Evolve Copywriting: the written prompts (labels, internet research, project goal, story, review scoring, visual words, Banger static ads, angle, video script), the Claude Code iteration skill, and the instructions Spencer types or speaks to Claude in the live builds. Each row gives the job, inputs, output and a link to where the verbatim text lives.

## 🤖 Agent use
- **Use when:** any LLM step in the ad pipeline: customer-language research, angle generation, story mining from reviews, static headlines, video scripts, rewriting lines, iteration learnings.
- **Inputs → outputs:** the job → the [which-prompt table](#which-prompt-for-which-job) → the prompt row → open the linked lesson section, paste the **verbatim** text and supply the inputs listed → check the output against the rules before using it.
- **Rules:**
  - **DO** paste course prompts exactly, replacing only the placeholders (`BRAND`, `YOURWEBSITE`, `[INSERT AVATAR/NICHE]`, the four document slots). [L37 page](../lessons/37-evolve-writing-prompts.md)
  - **DO** know why a line works before asking AI for it, and review every draft with course terms ("raise the stakes here", "re-optimize the bridge"). [L36 01:25-03:02](../lessons/36-what-about-ai.md)
  - **DON'T** ship the output: Claude gets you "70, 80% of the way there"; finish with customer language and verified claims. [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md) [L71 14:43](../lessons/71-how-to-write-video-ads-part-2.md)
  - **DON'T** trust its facts: it called DPP-4 a hormone and named hormones the product doesn't support. Check every claim against the product doc. [L71 03:40](../lessons/71-how-to-write-video-ads-part-2.md) [L68 30:59-34:44](../lessons/68-how-to-write-image-ads-part-2.md)
  - **DON'T** let it assume social-proof volume ("12,000 women"); give the real number or use the prompt's lower tier / borrowed proof. [L70 12:01-12:44](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DON'T** keep a headline that copies its reference ad line for line (several Banger-prompt outputs do). [Rules SA17](rules.md#8-static-ads)
  - **DON'T** make AI your strategy "for now". [L36 00:44-01:25](../lessons/36-what-about-ai.md)
- **See also:** [Rules → AI use](rules.md#11-ai-use) · [AI in copywriting](../concepts/ai-in-copywriting.md) · [Static ad workflow](../frameworks/static-ad-workflow.md) · [Video ad script workflow](../frameworks/video-ad-script-workflow.md) · Tether Lab's [prompt index](../../../../libraries/prompts.md)

## Which prompt for which job
| Pipeline step | IF you need… | THEN use | Then |
|---|---|---|---|
| Research | Labels the audience calls itself | P01 (Urban Dictionary) or P02 Part 1 | Put the best label in a hook ([hooks §B](hooks.md#b-targeted-label-and-identity-call-outs)) |
| Research | Customer words and sayings vs copywriter words | P02 Part 2, P03 | Word-swap pass ([rewrites §5](rewrites.md#5-labels-and-customer-language)) |
| Research | A standing brand assistant over your research files | P04 | Ask by function; feed post-launch metrics back |
| Angles | 3 angles × 3 hooks per sub-avatar | P10 (+ P11 refinements) | Choose marksman or sniper ([angles §P](angles.md#p-worked-case-appetite-supplement-zend-metaglow)) |
| Story | Story starters for a brand | P05 | [Story rules](rules.md#7-story) |
| Story | The best review to build a story ad on | P06 | Rewrite the top review as a story hook ([templates T169](templates.md#8-story-mini-templates)) |
| Static | Nine bold scroll-stopping headlines + concepts | P09 | Pick top 3; reject near-copies |
| Static | Headline + bullets in a winning ad's format, per sub-avatar | P12–P16 | Ground the claims (P17); image (P18) |
| Video | A modular script (3 hooks, 3 bridges, 1 hold, 1 CTA) | P19 | Edit line by line (P20) |
| Any draft | Flag abstract words and clichés | P08 | Rewrite to concrete |
| Iterate | Learnings from a tested ad, written back to the Growth Guide | P07 | [Iteration rules](rules.md#10-iteration-and-testing) |

## Written prompts (verbatim text in the lesson)
| ID | Prompt | Job | Inputs | Output | Verbatim text |
|---|---|---|---|---|---|
| P01 | **Prompt For Labels** ("cultural language researcher" searching Urban Dictionary) | Find self-identifying labels a niche "owns" | `[INSERT AVATAR/NICHE]` | Curated list: label, definition, why members claim it; prioritise high-upvote terms | [L34 Prompt For Labels](../lessons/34-how-to-write-with-labels-customer-language.md#prompt-for-labels) |
| P02 | **Prompt For Internet** (voice-of-customer research specialist) | Live research across Reddit, forums, reviews, comments | Your brand, product or audience | Part 1: labels (where, how often, identity, hook use) + 2–3 coined labels to own; Part 2: a Customer Language Bank (pain, ideal outcome, products that worked / failed, repeated sayings), each with "generic copywriter version" vs "real customer version"; cited sources | [L34 Prompt For Internet](../lessons/34-how-to-write-with-labels-customer-language.md#prompt-for-internet) |
| P04 | **Project Goal Prompt** | Set up a custom AI project for one e-commerce brand across five functions: customer understanding, competitive analysis, creative ideation, scriptwriting, ad review / feedback loop | `BRAND`, `YOURWEBSITE`; attached knowledge-base files (surveys, personas, competitor data, *Breakthrough Advertising*); later: ad spend, ROAS, hook rate, hold rate, CTR | Grounded answers per function; post-launch learnings and takeaways | [L37 Project Goal Prompt](../lessons/37-evolve-writing-prompts.md#project-goal-prompt) |
| P05 | **Six brand / market story prompts** (credit Davie Fogarty) | Story starters | The product | Answers to six questions (see quote below) | [L44 §A](../lessons/44-prompts-to-help-you-storytell.md#a-six-brandmarket-story-prompts-lesson-page-verbatim) |
| P06 | **AI prompt to find story-worthy reviews** ("direct response copywriter and story analyst") | Score reviews for story potential | All your reviews | Per review: story score 1–10, full quote, elements present (change, stakes, cause & effect, withholding, tension), 2–3 hook angles, emotional stakes, why it works; ranked, [PRIORITY] flags | [L44 §B](../lessons/44-prompts-to-help-you-storytell.md#b-ai-prompt-to-find-story-worthy-reviews-docx-44-prompts-to-help-you-storytelldocx-identical-to-the-linked-google-doc-verbatim) |
| P08 | **Visual words prompt** (credit Harry Dry) | Flag abstract language | The draft | Highlighted abstract verbs, nouns, adjectives, adverbs, clichés | [L59 prompt](../lessons/59-visual-words.md#prompts--templates-verbatim) |
| P09 | **Banger Static Ads prompt** ("$100k Static Ads - Full EVOLVE Prompts"; ~30,000 characters, 11 reference ads) | Bold statics for new customers | Answered one at a time: research doc + reviews; target avatar; product name, features, benefits; confirmation | Step 1: nine headlines (6–8 words), each citing its reference ad, why it stops the scroll, two alternates; Step 2: image description + supporting text for your top 3 | [L65 full prompt](../lessons/65-banger-static-ads-prompt.md#prompts--templates-verbatim) · design notes: [L65 design](../lessons/65-banger-static-ads-prompt.md#the-prompts-design-read-from-the-full-text-below) |
| P10 | **Angle prompt** ("Angle Prompts Used (From Avatar Training)"; "Evolve Enhanced - Angle Identifier" in L37) | Angles from sub-avatars | Product info + sub-avatars with quotes | Per sub-avatar: 3 angles, each a "Reason to Buy" + 3 hooks tagged "Inspired by" a reference ad; sub-avatars ranked; option to test marksman or sniper | [L67 angle prompt](../lessons/67-how-to-write-image-ads-part-1.md#1-angle-prompt-google-doc-angle-prompts-used-from-avatar-training) · worked output: [L67 example](../lessons/67-how-to-write-image-ads-part-1.md#worked-example-from-the-angle-prompt-output-the-prompt-is-meant-to-produce) |
| P19 | **Video script prompt** ("EVOLVE OPTIMIZED VIDEO AD SCRIPT - FINAL EDITION"; "Evolve - Video Script Prompt" in L37) | A 30–45 s modular video ad script for problem- or product-aware buyers | Five feedback-loop answers; four documents (Product, New Mechanism, New Information Output, Customer Data); angle / avatar; hypothesis; real social-proof volume | 3 hooks, 3 bridges, 1 universal hold, 1 universal CTA, how they combine, visuals per line (Gridbank / fal.ai), and a strategic explanation block | [L72 full prompt](../lessons/72-action-item-write-your-video-ad-briefs.md#the-prompt-verbatim) · digest: [L72 digest](../lessons/72-action-item-write-your-video-ad-briefs.md#rule-digest-of-the-prompt-for-fast-lookup-verbatim-text-follows) · walkthrough: [L70 feedback questions and input slots](../lessons/70-how-to-write-video-ads-part-1.md#prompts--templates-verbatim) |

**Short prompts quoted here.** P05, verbatim from lesson 44: "#1 - What is something that everyone thinks is true about your product, but isn't? / #2 - What's something about your product that would frustrate people? / #3 - What's a story that proves your product/service is different from competitors / #4 - What made you angry that you had to create this product? (what is your enemy) / #5 - What do your competitors hope customers never figure out? / #6 - Who is this product NOT for?" [L44 02:43-04:43](../lessons/44-prompts-to-help-you-storytell.md)

P08, verbatim from lesson 59: "Read the following copy. Can you highlight every word or sentence that contains a) Abstract verbs b) Abstract nouns c) Abstract adjectives d) Abstract adverbs e) Cliches". [L59 page](../lessons/59-visual-words.md)

## Skills and tools
| ID | Prompt / tool | Job | Inputs | Output | Where |
|---|---|---|---|---|---|
| P07 | **Claude Code ad-iteration skill** (`/demo-ingest-ad`; production name `/ad-iteration`) | Run the 10-step learnings process on a tested ad | Ads Manager screenshots (one per hook, named `<batch>_v<n>`); verbatim hooks incl. voiceover; outcome; ad and campaign spend; Growth Guide sheet (Google Sheets MCP); FigJam board (Figma MCP) | 9-question learnings interview, hypothesis banner, write-back to the Growth Guide and a `patterns/all-batches.md` file, a FigJam card; iterations for winners | Skill messages and folder layout: [L47 verbatim](../lessons/47-claude-code-10-step-iteration-process.md#prompts--templates-verbatim); the iteration DOCX it follows: [L47 playbook](../lessons/47-claude-code-10-step-iteration-process.md#winning-video-ad-iteration-playbook-docx-video-ad-winner---iteration-playbook). The SKILL.md itself is **not** in the course files |
| P18 | **Nano Banana image prompt** | Replace a template photo with a congruent product image | Ad screenshot with the area outlined; product photo | A new image to drop into the ad (follow-ups: remove background / hand, resize plates) | [L68 §7](../lessons/68-how-to-write-image-ads-part-2.md#7-nano-banana-image-prompt-on-screen-frame-4757) |

## Live instructions typed or spoken to Claude / ChatGPT
Short, situational prompts from the build lessons. Use them as patterns; the exact wording is in the linked sections.

| ID | Instruction | Job | Inputs | Output | Where |
|---|---|---|---|---|---|
| P03 | Word swap (spoken, no written text): give Claude your brief and ask "what are some of the generic copywriter words" and which words "sound more like our customer" | Swap polished words for customer words | Brief + customer research | Word-swap list | [L34](../lessons/34-how-to-write-with-labels-customer-language.md#word-swap-prompt-suggested-in-the-video-not-a-written-prompt) [L34 06:00-06:51](../lessons/34-how-to-write-with-labels-customer-language.md) |
| P11 | Angle refinements in Claude: format request (Concept/Swing → Angle(s)); sniper refinement ("dumb things down... explain how our product actually delivers the mechanism"); "make it pack more of a punch and make it shorter"; "I need three bullet points for this headline... I have attached the inspo ad" | Turn angle output into a static brief and copy | Angle output, inspiration ad, research quotes | Refined angle, punchier headline, bullets | [L67 §4](../lessons/67-how-to-write-image-ads-part-1.md#4-prompts-typed-or-spoken-in-claude-during-the-lesson) [L67 07:18-07:59](../lessons/67-how-to-write-image-ads-part-1.md) [L67 10:38](../lessons/67-how-to-write-image-ads-part-1.md) [L67 18:02](../lessons/67-how-to-write-image-ads-part-1.md) |
| P12 | "hey claude based on this ad, I need 3 headlines + check mark points for each one of my sub avatars... the quotes I pulled are the real ones... 5th grade reading level" | Headlines + bullets in a winning ad's format | Inspiration screenshot, sub-avatars with quotes, Reddit links | 3 headlines per sub-avatar, one bullet list | [L68 §1](../lessons/68-how-to-write-image-ads-part-2.md#1-headlines--bullets-from-an-inspiration-ad-typed-in-claude-on-screen-text-frame-1748) |
| P13 | "write it EXACTLY like the ad itself. Just plugged in with our specific product + customer research" (the headline becomes the template) | Template-fill a proven static | The reference ad | Headline and bullets in the same structure | [L68 §2](../lessons/68-how-to-write-image-ads-part-2.md#2-exactly-like-the-ad-itself-template-fill-on-screen-frames-1947-2007) — see the [conflict note](rules.md#conflicts-at-a-glance) |
| P14 | "how can we implement EVEN more of the research...? write 3 more headlines + subheadings for each sub avatar"; "I personally like 'Constantly chugging water?'" | Push for more research-grounded options | Prior output | More headlines | [L68 §3](../lessons/68-how-to-write-image-ads-part-2.md#3-feedback--more-research-turn-on-screen-frame-2157) |
| P15 | "I REALLY liked... because of how SPECIFIC it is" → "optimize more headlines like that for all three avatars" | Feedback with a reason | A chosen headline + the reason | Headlines in that direction | [L68 §4](../lessons/68-how-to-write-image-ads-part-2.md#4-feedback-on-a-specific-headline-on-screen-frame-2317-truncated-at-the-end-of-the-frame) |
| P16 | "I now need these 3 bullet points for these 3 different sub avatars, please include the emojis as well" | Bullets for finished headlines | Final headlines | Check-mark bullets | [L68 §5](../lessons/68-how-to-write-image-ads-part-2.md#5-bullets-for-the-finished-headlines-on-screen-frame-3048) |
| P17 | "do not call out hormones that our product does not support... review the product document"; "Are there three hormones that Metaglow actually targets...?"; "Can we use a different word other than 'root cause'...?" | Ground claims in the product; compliance wording | Product doc | Corrected mechanism lines | [L68 §6](../lessons/68-how-to-write-image-ads-part-2.md#6-product-grounding-correction-spoken-31583230-and-honesty-check-on-screen-frame-3515) |
| P20 | Script-editing turns: "here's the script that I wrote, let me know where it has issues based off of the prompt"; "does this categorize us?"; "is [ingredient] actually a rare African fruit extract?"; "deep research around customers that you say 'I'm full hormone'"; "I need a specific pain point... from one of the threads"; "give me the visuals" | Line-by-line edit of an AI script | Draft script + the P19 prompt + research | Issues, verified claims, customer phrasing, visuals | [L71](../lessons/71-how-to-write-video-ads-part-2.md#prompts--templates-verbatim) [L71 08:47](../lessons/71-how-to-write-video-ads-part-2.md) [L71 18:08](../lessons/71-how-to-write-video-ads-part-2.md) [L71 21:28-23:06](../lessons/71-how-to-write-video-ads-part-2.md) [L71 25:12](../lessons/71-how-to-write-video-ads-part-2.md) |
| P21 | Sanity check in ChatGPT: what an average woman 35+ eats per day | Validate a number before building a headline on it | The claim | A plausibility check ("good enough for now") | [L67 04:13](../lessons/67-how-to-write-image-ads-part-1.md) [L67 09:51](../lessons/67-how-to-write-image-ads-part-1.md) |
| P22 | "You guys have Claude, so you can go and ask Claude" whether a statement is a fact | Fact vs opinion check | The line | A verdict to verify | [L10 03:22-03:53](../lessons/10-why-you-need-to-write-facts.md) |
| P23 | Simplify with Claude after a Hemingway check ("use Claude with caution... actually analyze it") | Lower the reading grade | The draft | A simpler draft to review | [L13 00:31-01:05](../lessons/13-why-you-need-to-write-at-a-6th-grade-level.md) |
| P24 | Fix instructions in course terms: "I need to raise the stakes here"; "the bridge here is lacking the stickiness... Let's re-optimize the bridge" | Optimise an AI draft | Draft + diagnosis | A targeted rewrite | [L36 01:25-02:19](../lessons/36-what-about-ai.md) |
| P25 | "Create a new avatar for [product] following this prompt" (with the "How To Make Personas/Avatars With Claude" prompt from the Evolve AI classroom) | Avatar before the static prompt | Research files + the persona prompt | An avatar | [L65 00:46-01:36](../lessons/65-banger-static-ads-prompt.md) (persona prompt itself not in the files) |
| P26 | Paste the positioning exercise into a doc or Claude ("if you want to, you totally can") | Fill the four positioning tables | Competitors, reviews, product facts | Brand / feature / problem / differentiator maps | [L56 worksheet](../lessons/56-positioning-exercise.md#prompts--templates-verbatim) [L56 03:23](../lessons/56-positioning-exercise.md) |

## Not available in the course files
Listed by name in lesson 37 or mentioned in lessons; the text was not exported. Don't reconstruct them. [L37 page](../lessons/37-evolve-writing-prompts.md)

| Prompt | Where named | Status |
|---|---|---|
| Desires Prompt ("Evolve - Desire AI Prompts") | L37 | Not exported |
| New Info Prompt ("New Information Prompt Document") | L37 | Not exported (the video prompt P19 expects its output document) |
| New Mechanism Prompt ("New Mechanism Prompt Document") | L37 | Not exported (P19 expects its output) |
| Ads Call Analysis Prompt ("Ad Learnings Call Analysis Prompt", from Chef Karlo) | L37 | Not exported |
| Alex Cooper's prompts | L37 (call recording only) | Not in files |
| "Evolve AI - Prompts" (courtesy of Karlo) | L37 | Outside this course |
| "How To Make Personas/Avatars With Claude" | L65 on screen | Outside this course |
| SKILL.md for `/ad-iteration` | L47 (Drive folder) | Not in files |
| "Basic static ad prompt" (the older one the Banger prompt improves on) | L65 05:13 | Not in files |

Lesson 37's Angles, Static Ads and Video Ads prompts **are** available, as P10, P09 and P19. [L37 availability table](../lessons/37-evolve-writing-prompts.md#the-other-prompts-listed-names-and-what-is-available)

## Coverage and gaps
- **Indexed:** 26 prompt rows (P01–P26): 8 written prompts, 2 skills / tools, 16 live instructions; plus 9 named-but-unavailable prompts.
- **Deliberately not duplicated:** the long prompts (P02, P04, P06, P09, P10, P19) stay on their lesson pages; only P05 and P08 are short enough to quote.
- **Lesson 36** explains why the program first shipped without prompts; later lessons supply them. Treat that as context, not a conflict: the rule is still "AI is not the strategy". [L36 00:00-00:44](../lessons/36-what-about-ai.md)
