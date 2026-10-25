---
title: "AI in copywriting (the operator model)"
type: concept
creator: evolve
course: copywriting
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/02-the-current-state-of-copywriting.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/36-what-about-ai.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/37-evolve-writing-prompts.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/44-prompts-to-help-you-storytell.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/46-the-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/65-banger-static-ads-prompt.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/67-how-to-write-image-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/68-how-to-write-image-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/70-how-to-write-video-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/71-how-to-write-video-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/72-action-item-write-your-video-ad-briefs.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/10-why-you-need-to-write-facts.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/11-why-you-need-to-write-less-fluff.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/12-why-you-need-to-speak-copy-not-write-it.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/13-why-you-need-to-write-at-a-6th-grade-level.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/21-being-aware-of-market-awareness.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/32-how-to-write-ads-that-show-and-dont-tell.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/34-how-to-write-with-labels-customer-language.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/40-what-makes-a-great-story.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/50-how-to-iterate-on-spend-winners.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/51-how-to-iterate-on-breakthroughs.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/53-the-iteration-playbook-formats-styles.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/55-why-you-need-to-position-your-brand.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/56-positioning-exercise.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/59-visual-words.md
tags: [ai, llm, claude, claude-code, prompts, operator, fact-checking, ai-ads, ai-ugc, workflow]
updated: 2026-10-21
---

# AI in copywriting (the operator model)
> AI raises the floor, so AI-only copy becomes average: let AI gather, identify, fill gaps and draft (to "70, 80%"), while the human "operator" owns strategy, facts, customer language and the final 20-30%, directing AI with named copy techniques.

## 🤖 Agent use
- **Use when:** you (an AI agent) are drafting copy, scripts or briefs; deciding which steps to automate; reviewing an AI draft before it reaches a brief; picking which course prompt to run.
- **Inputs → outputs:** strategy already set (avatar, angle, awareness, mechanism, hypothesis) + real research (reviews, Reddit, product doc) + the right course prompt → an AI draft → a line-by-line edited, fact-checked script/ad with customer language, plus a log of which prompt produced it.
- **Rules:**
  - **DO** use AI for what it is good at: "It's phenomenal at identifying things. It's phenomenal at filling in the gaps. And it's amazing at gathering things." [L36 00:44–01:25](../lessons/36-what-about-ai.md)
  - **DON'T** let AI be the strategy: "AI should just never be your sole strategy or your relied upon strategy, at least for now." [L36 00:44–01:25](../lessons/36-what-about-ai.md)
  - **DON'T** ship raw output: "LLMs are trained on predictive words… we are automatically guaranteed to sound like everyone else… if we rely on AI." [L02 09:29](../lessons/02-the-current-state-of-copywriting.md); "the brief or Claude will just give you it and you'll just ship it" is the failure. [L11 06:07–06:37](../lessons/11-why-you-need-to-write-less-fluff.md)
  - **DO** treat the first output as a draft: Claude gets you "70, 80% of the way there"; customer language and research take it to 100%. [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** direct revisions with named techniques, not "make it better": "I need to raise the stakes here" / "the bridge here is lacking the stickiness… Let's re-optimize the bridge." [L36 01:25–02:19](../lessons/36-what-about-ai.md)
  - **DON'T** trust AI facts: it called DPP4 a hormone; "you guys can't blindly trust AI ... it fills in a lot of gaps for you, but it's not always right." [L71 03:40](../lessons/71-how-to-write-video-ads-part-2.md) "Be a marketer, don't be an AI regurgitator." [L68 30:59–32:30](../lessons/68-how-to-write-image-ads-part-2.md)
  - **DO** verify every claim against the product document; drop or soften what you cannot show ("rare" African fruit was dropped). [L71 21:28](../lessons/71-how-to-write-video-ads-part-2.md); [L68 31:58–34:44](../lessons/68-how-to-write-image-ads-part-2.md)
  - **DON'T** let a prompt invent social proof; state your real volume when asked. [L70 12:01–12:44](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** run your own rewrite back through the prompt as a critic: "here's the script that I wrote, let me know where it has issues based off of the prompt". [L71 08:47; 13:45; 18:08](../lessons/71-how-to-write-video-ads-part-2.md)
  - **DO** paste course prompts verbatim and supply their inputs (research, avatar, product, documents); "the more context you give it about who your customer is, the better it's gonna be." [L67 23:40](../lessons/67-how-to-write-image-ads-part-1.md)
  - **DO** label AI-learned conclusions as hypotheses: "this is a hypothesis. This is not fact." Remind the AI and the team. [L46 14:17](../lessons/46-the-10-step-iteration-process.md)
  - **IF** using AI voice or AI actors **THEN** the script must still "speak like a person". [L12 02:05](../lessons/12-why-you-need-to-speak-copy-not-write-it.md)
  - **IF** an AI person narrates **THEN** don't let it claim a human experience ("you're an AI. We know you didn't see it"); "we are not pretending the UGC is a real person". [L53 08:51–09:37](../lessons/53-the-iteration-playbook-formats-styles.md)
  - **IF** a needed course prompt is not in the KB (desires, new information, new mechanism, ad-learnings call analysis) **THEN** say so; do not reconstruct it. [L37](../lessons/37-evolve-writing-prompts.md)
- **See also:** [Prompts library](../libraries/prompts.md) · [Video ad script workflow](../frameworks/video-ad-script-workflow.md) · [Static ad workflow](../frameworks/static-ad-workflow.md) · [Ten-step iteration learnings](../frameworks/ten-step-iteration-learnings.md) · [Labels and customer language](labels-and-customer-language.md) · [Facts over opinions](facts-over-opinions.md) · [Compression and plain language](compression-and-plain-language.md) · [Shared prompt index (Tether Lab)](../../../../libraries/prompts.md) · [ChatGPT tool page (Tether Lab)](../../../../tools/chatgpt.md)

## Definition
The course's stance on AI is an **operator model**: AI is an instrument, and the copywriter is the operator who knows "what good looks like" [L02 07:20](../lessons/02-the-current-state-of-copywriting.md). The program was built to teach the judgment, not to hand out prompts: "The point… was not to give you another copywriting prompt. Because if you ask me, there's enough of them out there." [L36 00:00–00:44](../lessons/36-what-about-ai.md). The skill is then to "communicate with AI the right way" using the course's vocabulary (stakes, bridges, labels, mechanisms) [L36 01:25–02:19](../lessons/36-what-about-ai.md).

## Why it matters
- **AI raises the floor and flattens the field.** "AI can do copywriting", but "the floor is raised on average copy"; when everyone uses it, "Average copywriting becomes the ineffective" [L02 05:09–05:44](../lessons/02-the-current-state-of-copywriting.md). Even "good copywriting with AI just becomes ineffective because everybody is using it" [L02 07:20–07:55](../lessons/02-the-current-state-of-copywriting.md).
- **Proprietary knowledge is the moat.** Even a hypothetical Eugene Schwartz AI would become what "everybody will use"; "That proprietary knowledge… is the skillset that you develop" [L02 07:55–08:25](../lessons/02-the-current-state-of-copywriting.md). Relying solely on AI for execution is one of three causes of "me too" copy [L02 08:25–08:57](../lessons/02-the-current-state-of-copywriting.md).
- **Storytelling needs knowledge AI can't supply.** Those "trying to replace a lot of the stuff with AI" will find it "very hard to actually storytell the right way" without knowing the subject [L40 05:05–05:50](../lessons/40-what-makes-a-great-story.md).
- **AI-made ads are easy to copy.** "When ads are easy to make, it means they're easy to replicate"; native/AI UGC breakthroughs die faster without product differentiation [L51 05:36–07:09; 12:19–15:28](../lessons/51-how-to-iterate-on-breakthroughs.md).
- **Buyers use AI too.** Problem-aware buyers "ask chat GPT" and become solution/product aware in minutes, which shapes market awareness [L21 00:45–01:39](../lessons/21-being-aware-of-market-awareness.md).

## How to use it

### Division of labour (decision table)

| Task | AI does | Human / reviewer does | Source |
|---|---|---|---|
| Research | Scour reviews, Reddit, comments, Urban Dictionary for labels and customer language; rank reviews for story potential | Choose which quotes matter; add manual notes | [L34 08:08–09:25](../lessons/34-how-to-write-with-labels-customer-language.md); [L44 06:20](../lessons/44-prompts-to-help-you-storytell.md) |
| Strategy (avatar, angle, positioning, what to test) | Suggest options, run the positioning worksheet if asked | Decide; fill from real competitor, review and product facts | [L36 00:44–01:25](../lessons/36-what-about-ai.md); [L56 03:23; 04:46–05:41](../lessons/56-positioning-exercise.md) |
| First draft (hooks, scripts, headlines, bullets) | Draft from a verbatim course prompt + documents | Edit line by line to 100% | [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md); [L65](../lessons/65-banger-static-ads-prompt.md) |
| Proofing | Flag abstract words (Visual Words prompt), generic copywriter words, reading grade | Rewrite each flag by hand; check meaning survives | [L59](../lessons/59-visual-words.md); [L34 06:00–06:51](../lessons/34-how-to-write-with-labels-customer-language.md); [L13 00:31–01:05](../lessons/13-why-you-need-to-write-at-a-6th-grade-level.md) |
| Facts | Quick check ("you guys have Claude, so you can go and ask Claude as well"; he asked ChatGPT for typical calorie intake) | Validate against product doc/source before it ships | [L10 03:22–03:53](../lessons/10-why-you-need-to-write-facts.md); [L67 04:13; 09:51](../lessons/67-how-to-write-image-ads-part-1.md) |
| Critique | Re-check your rewrite against the prompt's rules (categorization, specificity, show-don't-tell) | Accept or knowingly reject (he accepted slight categorization "worth the trade-off ... building more trust") | [L71 08:47; 14:43; 18:46](../lessons/71-how-to-write-video-ads-part-2.md) |
| Iteration learnings | Interview you per component, condense your brain dump, write to Growth Guide / patterns / FigJam | Supply true hooks, spend, outcome; challenge the AI's read ("Claude is not always 100% right") | [L47 03:17–09:41](../lessons/47-claude-code-10-step-iteration-process.md) |
| Visual production | AI animation, AI song (Claude → Suno), Nano Banana product images, fal.ai when stock can't show it | Keep visuals congruent with the claim; no fake human experience | [L53 03:58–09:37](../lessons/53-the-iteration-playbook-formats-styles.md); [L68 46:36–50:33](../lessons/68-how-to-write-image-ads-part-2.md); [L72 Visual Execution System](../lessons/72-action-item-write-your-video-ad-briefs.md) |

### The draft-to-final loop (video, L70-71)
1. Answer the prompt's feedback questions (previous scripts, best/worst hook, off metrics, why people did or did not care) before any script. [L70 06:31–09:27](../lessons/70-how-to-write-video-ads-part-1.md)
2. Supply the four documents (Product, New Mechanism, New Information, Customer Data) and real proof volume; say "none" for missing ones. [L70 09:27–12:44](../lessons/70-how-to-write-video-ads-part-1.md)
3. Take the modular output (3 hooks, 3 bridges, 1 hold, 1 CTA) as a 70-80% draft. [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md)
4. Replace generic lines with researched specifics ("kitchen pantry", "something crunchy", "feels like torture"); ask the AI which word customers actually use ("fullness hormone", not "I'm full hormone"). [L71 06:18–06:50; 17:32; 19:33–22:13](../lessons/71-how-to-write-video-ads-part-2.md)
5. Fact-check every term against the product page. [L71 03:40; 21:28](../lessons/71-how-to-write-video-ads-part-2.md)
6. Run the rewrite back through the prompt as critic. [L71 08:47](../lessons/71-how-to-write-video-ads-part-2.md)
7. Budget the time: "one to two really good briefs per day ... one brief, I would say even per day, especially if they're videos." [L71 14:43](../lessons/71-how-to-write-video-ads-part-2.md)

### Claude Code iteration skill (L46-47)
- The 10-step iteration process can run with a Claude Code skill (page: `/ad-iteration`; demo copy `/demo-ingest-ad`) that "stores your data, stores your learnings" and writes them to the Growth Guide. [L46 00:00–00:36](../lessons/46-the-10-step-iteration-process.md); [L47 00:00](../lessons/47-claude-code-10-step-iteration-process.md)
- Prerequisites: a naming scheme (without it "AI is not really going to be able to help you"), the Growth Guide, optional paid Figma for the FigJam board. [L46 01:14–02:05](../lessons/46-the-10-step-iteration-process.md); [L47 00:00–01:32](../lessons/47-claude-code-10-step-iteration-process.md)
- Inputs: one screenshot per hook variation renamed by batch/variation (e.g. `59_v2`), every hook verbatim including voiceover hooks, outcome, ad spend and campaign spend. [L47 00:58–05:12](../lessons/47-claude-code-10-step-iteration-process.md)
- The skill runs MCP checks → folders (`screenshots`, brand, `added`, `patterns`) → hook extraction → outcome/spend → a component review "planned vs hypothesis" (awareness, valence/intensity, desire, avatar, angle, mechanism, belief, positioning, urgency) → brain dump condensed into a learning you approve → write-back → FigJam card → archive. [L47 01:32–11:46](../lessons/47-claude-code-10-step-iteration-process.md)
- Guardrails: "Claude is not always 100% right"; keep client data out of shared skills (NDAs). [L47 00:00; 05:12–05:55](../lessons/47-claude-code-10-step-iteration-process.md) Full procedure: [Ten-step iteration learnings](../frameworks/ten-step-iteration-learnings.md).

### Named course prompts and where they live
Full text is in the lesson pages and indexed in [the course prompts library](../libraries/prompts.md); don't paraphrase them.

| Prompt | Job | Model used on screen | Where the verbatim text is |
|---|---|---|---|
| Project Goal Prompt | Set up a brand AI project grounded in attached research (5 functions incl. ad review on spend, ROAS, hook rate, hold rate, CTR) | not specified | [L37](../lessons/37-evolve-writing-prompts.md) |
| Prompt For Labels / Prompt For Internet | Labels from Urban Dictionary; customer language from reviews/Reddit/comments | Claude | [L34](../lessons/34-how-to-write-with-labels-customer-language.md) |
| Review-scoring story prompt | Score reviews for story potential, return best with hook angles | Claude project or Claude Code | [L44 06:20–07:18](../lessons/44-prompts-to-help-you-storytell.md) |
| Visual Words prompt | Flag abstract verbs/nouns/adjectives/adverbs/clichés | not specified | [L59](../lessons/59-visual-words.md) |
| "$100k Static Ads - Full EVOLVE Prompts" (Banger Static Ads) | Intake → 9 headlines modelled on 11 reference ads → top 3 → image concepts | Claude 3.5 Sonnet (on-screen selector) | [L65](../lessons/65-banger-static-ads-prompt.md) |
| "Evolve Enhanced - Angle Identifier" | 3 angles × 3 hooks per sub-avatar, ranked | Claude | [L67](../lessons/67-how-to-write-image-ads-part-1.md) |
| "EVOLVE OPTIMIZED VIDEO AD SCRIPT - FINAL EDITION" | Feedback loop → 3 hooks/3 bridges/1 hold/1 CTA + strategic explanation | Claude | [L72](../lessons/72-action-item-write-your-video-ad-briefs.md) (used in [L70](../lessons/70-how-to-write-video-ads-part-1.md)-[71](../lessons/71-how-to-write-video-ads-part-2.md)) |
| `/ad-iteration` Claude Code skill | Iteration learnings → Growth Guide/patterns/FigJam | Claude Code | skill files not in course files; demo in [L47](../lessons/47-claude-code-10-step-iteration-process.md) |
| Desires, New Info, New Mechanism, Ad Learnings Call Analysis prompts | — | — | Not included in the course files ([L37](../lessons/37-evolve-writing-prompts.md)) |

Short verbatim prompt (Visual Words, [L59](../lessons/59-visual-words.md)): "Read the following copy. Can you highlight every word or sentence that contains a) Abstract verbs b) Abstract nouns c) Abstract adjectives d) Abstract adverbs e) Cliches"

## Examples

| Situation | What AI did / was used for | Human correction or lesson | Source |
|---|---|---|---|
| Video script draft (weight supplement) | Called DPP4 a hormone | "you guys can't blindly trust AI" | [L71 03:40](../lessons/71-how-to-write-video-ads-part-2.md) |
| Objection line from the prompt | "I know what you're thinking. You've tried supplements before. They didn't work" | "a terrible line ... not specific enough"; find what they actually tried on Reddit | [L70 23:07–24:04](../lessons/70-how-to-write-video-ads-part-1.md) |
| Static bullets (image-first method) | Named hormones the product does not support; "three hormone imbalances" | Changed to "two hormones and one enzyme" (true to product); added glosses like "(hunger hormone)" | [L68 31:58–36:28](../lessons/68-how-to-write-image-ads-part-2.md) |
| Iteration skill read of a hook | Agent said the planned problem-aware hook "reads more unaware" | Instructor agreed and re-labelled; agent "is testing and questioning you" | [L47 05:12–05:55](../lessons/47-claude-code-10-step-iteration-process.md) |
| Static ad prompt demo | Several headlines follow the reference ad almost line for line | Copy the mechanism, not the wording (derived on the lesson page) | [L65](../lessons/65-banger-static-ads-prompt.md) |
| Slide asset | AI-generated monthly-sales screenshot ("this is actually AI... I don't even know how to tell it's fake") | Not evidence; never use AI-made proof in ads | [L55](../lessons/55-why-you-need-to-position-your-brand.md) |
| Format iteration | AI-animated ingredients/solutions/body parts, AI song, AI story, AI UGC narration | Use when the mechanism is hard to visualise; don't fake a human | [L53 03:58–09:37](../lessons/53-the-iteration-playbook-formats-styles.md); [L32 04:31–05:50](../lessons/32-how-to-write-ads-that-show-and-dont-tell.md) |
| Spend winner | Moving an AI-voiceover video to native or AI-animated | "is not going to make it work all of the time"; fix urgency, funnel, stakes, belief first | [L50 17:18](../lessons/50-how-to-iterate-on-spend-winners.md) |

## Common mistakes
- Asking an agent to "write the best ad" before strategy (avatar, angle, awareness) is set. [L36](../lessons/36-what-about-ai.md)
- Copying a prompt and skipping the understanding: the instructor expects most people would "copy the prompt" and not retain the teaching. [L36 01:25–02:19](../lessons/36-what-about-ai.md)
- Shipping the first output; treating 70-80% as done. [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md)
- Accepting AI terminology and numbers without checking the product page. [L71 03:40; 21:28](../lessons/71-how-to-write-video-ads-part-2.md)
- Letting the model assume proof volume ("12,000 women"). [L70 12:01–12:44](../lessons/70-how-to-write-video-ads-part-1.md)
- Building on a copy-and-paste trend (template + LLM + AI face, the "native/camouflage ad" wave) that "is going to die fast". [L02 10:01–10:33](../lessons/02-the-current-state-of-copywriting.md)
- AI UGC that claims first-person experience. [L53 09:37](../lessons/53-the-iteration-playbook-formats-styles.md)
- Treating AI-written learnings as facts instead of hypotheses. [L46 14:17](../lessons/46-the-10-step-iteration-process.md)

## Where it's taught

| Lesson | Timestamps | What it adds |
|---|---|---|
| [02. Current state of copywriting](../lessons/02-the-current-state-of-copywriting.md) | 00:30–01:01; 05:09–10:33 | Why AI-only copy goes average; operator model; "me too" causes |
| [05. Write in the environment](../lessons/05-why-you-need-to-write-in-the-environment.md) | 09:06–10:15 | Templatizing inspiration with AI inside Figma; Claude route not yet built |
| [10. Write facts](../lessons/10-why-you-need-to-write-facts.md) | 03:22–03:53 | Ask Claude when unsure if something is a fact |
| [11. Less fluff](../lessons/11-why-you-need-to-write-less-fluff.md) | 06:07–06:37 | Don't ship what Claude gives you unchallenged |
| [12. Speak copy](../lessons/12-why-you-need-to-speak-copy-not-write-it.md) | 01:35–02:38 | AI voiceovers/actors still need spoken language |
| [13. 6th-grade level](../lessons/13-why-you-need-to-write-at-a-6th-grade-level.md) | 00:31–01:38 | "use Claude with caution"; Hemingway check |
| [21. Market awareness](../lessons/21-being-aware-of-market-awareness.md) | 00:45–01:39 | Buyers ask ChatGPT and move awareness fast |
| [32. Show and don't tell](../lessons/32-how-to-write-ads-that-show-and-dont-tell.md) | 00:53–01:45; 03:33–05:50 | AI to visualise; Ryze "ads that only AI can make" |
| [34. Labels / customer language](../lessons/34-how-to-write-with-labels-customer-language.md) | 06:00–06:51; 08:08–09:25 | Claude for word swaps and label/language research prompts |
| [36. What about AI?](../lessons/36-what-about-ai.md) | 00:00–03:02 | Core stance: identify/fill gaps/gather; never the strategy; direct with technique names |
| [37. Evolve writing prompts](../lessons/37-evolve-writing-prompts.md) | page | Project Goal Prompt; prompt index and availability |
| [40. What makes a great story](../lessons/40-what-makes-a-great-story.md) | 05:05–05:50 | AI can't replace subject knowledge in storytelling |
| [44. Prompts to storytell](../lessons/44-prompts-to-help-you-storytell.md) | 06:20–07:18 | Review-scoring prompt in a Claude project / Claude Code |
| [46. 10-step iteration](../lessons/46-the-10-step-iteration-process.md) | 00:00–02:05; 03:31–04:14; 14:17–16:23 | Claude skill rationale; naming scheme; hypothesis not fact |
| [47. Claude Code iteration](../lessons/47-claude-code-10-step-iteration-process.md) | 00:00–12:46 | Full skill demo and guardrails |
| [50. Spend winners](../lessons/50-how-to-iterate-on-spend-winners.md) | 17:18 | AI format swaps don't fix strategic problems |
| [51. Breakthroughs](../lessons/51-how-to-iterate-on-breakthroughs.md) | 05:36–07:09; 12:19–15:28 | AI/native ads are easy to copy; differentiation needed |
| [53. Formats & styles](../lessons/53-the-iteration-playbook-formats-styles.md) | 03:58–09:37 | Five AI-animated formats, AI song, AI UGC narration ethics |
| [55. Position your brand](../lessons/55-why-you-need-to-position-your-brand.md) | 03:42–05:20 | AI-generated sales screenshot flagged as fake |
| [56. Positioning exercise](../lessons/56-positioning-exercise.md) | 03:23; 04:46–05:41 | Claude may run the worksheet; fill with real facts |
| [59. Visual words](../lessons/59-visual-words.md) | page | Abstract-word detection prompt |
| [65. Banger static ads prompt](../lessons/65-banger-static-ads-prompt.md) | 00:00–07:31 | Two-step static prompt demo in Claude |
| [67. Image ads part 1](../lessons/67-how-to-write-image-ads-part-1.md) | 00:54–01:37; 04:13; 18:02–20:11; 23:40 | Angle prompt; feed context; exact bullet counts; fact sanity checks |
| [68. Image ads part 2](../lessons/68-how-to-write-image-ads-part-2.md) | 14:57–36:28; 46:36–50:33 | Claude rewrites a template ad; correct its claims; Nano Banana images |
| [70. Video ads part 1](../lessons/70-how-to-write-video-ads-part-1.md) | 05:38–24:58 | Running the mega prompt; 70-80% draft |
| [71. Video ads part 2](../lessons/71-how-to-write-video-ads-part-2.md) | 03:40–25:12 | Editing the AI draft to final |
| [72. Video ad briefs](../lessons/72-action-item-write-your-video-ad-briefs.md) | docx | Full video prompt incl. compliance and borrowed-proof rules |

## Cross-course notes
- **Agreement — Tether Lab (Sarah Levinger)**: [ChatGPT tool page](../../../../tools/chatgpt.md) and [Rules library, AI section](../../../../libraries/rules.md) say the same core things: give the model context and fences, attach the actual ad, and "DON'T ship invented proof" (ChatGPT invented "Featured in Outside and Men's Health"). Evolve's equivalents: feed the four documents, state real proof volume, fact-check every term.
- **Different default model**: Tether runs its prompts in ChatGPT and treats [Claude](../../../../tools/claude-ai.md) as the fallback when headlines come back flat; Evolve runs everything in Claude / Claude Code (ChatGPT only for one quick calorie check, [L67 04:13](../lessons/67-how-to-write-image-ads-part-1.md)). Preference, not a principle; agents may use either with the same guardrails.
- **Different prompt style**: Tether's [story frameworks](../../../../frameworks/story-frameworks-for-ads.md) and [UGC script playbook](../../../../playbooks/ugc-script-writing.md) say paste one named framework's steps, or the LLM blends them; Evolve's prompts are long mega-prompts that carry the whole method (feedback loop, Big 4, categorization, proof tiers) and then require human line editing.
- **Disagreement — AI people on screen**: Tether ([Messenger effect](../../../../concepts/heuristics/messenger-effect.md), [Creator brief](../../../../playbooks/creator-brief.md), [AI UGC tools](../../../../tools/ai-ugc-tools.md)): don't use AI UGC avatars for trust-dependent brands; members' Creatify tests "didn't convert". Evolve ([L53 08:51–09:37](../lessons/53-the-iteration-playbook-formats-styles.md); [L12 01:35–02:38](../lessons/12-why-you-need-to-speak-copy-not-write-it.md)): AI voiceover is the default video model and AI UGC narration, AI-animated characters and AI songs are legitimate iteration formats, provided the AI person doesn't pretend to be a real customer. Agent default: AI voiceover and clearly-AI animation are fine; no synthetic person gives a testimonial or first-person result; avoid AI presenters for trust-dependent brands unless tested. Logged in contradictions notes.
- **Within-course tension**: L36 says the program deliberately gives no copy-and-paste prompts and AI "should never be your strategy", yet L37, L44, L65, L67 and L70-72 supply full prompts, including ones that propose angles and a "strategic explanation". Reconcile (derived): the prompts are drafting and analysis tools fed with human-set strategy and real research; the human still chooses the angle and edits the output. Logged in contradictions notes.

## Related
[Labels and customer language](labels-and-customer-language.md) · [Facts over opinions](facts-over-opinions.md) · [Compression and plain language](compression-and-plain-language.md) · [Show, don't tell](show-dont-tell.md) · [Positioning](positioning.md) · [Iteration outcomes](iteration-outcomes.md) · [Value words / Big 4](value-words-big-4.md) · [Iteration playbook](../frameworks/iteration-playbook.md) · [Write a video ad script](../playbooks/write-a-video-ad-script.md) · [Write static image ads](../playbooks/write-static-image-ads.md) · [Iterate on test results](../playbooks/iterate-on-test-results.md)
