---
title: "The Claude Project recipe"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/14-03-claude-projects-for-upsells.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/15-05-claude-project-for-writing-email-sequences.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/05-05-financial-promo-example.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md
tags: [rmbc-ii, claude-projects, prompting, llm-workflow, outline-first, knowledge-base, composite]
updated: 2026-11-02
---

# The Claude Project recipe
> One Claude Project per asset type (and per VSL length): a short instruction paragraph ("analyze the structure ... synthesize ... use your judgement"), a knowledge base of varied real examples, per-job facts given in the chat (brief, URL), then staged prompts: outline first → approve → write → "continue" → edit. The same recipe builds the UM, brief, VSL, hook, advertorial, PDP, upsell and email generators.

## 🤖 Agent use
- **Use when:** setting up any RMBC generator (or an equivalent agent context / system prompt + reference files); deciding what goes in instructions vs knowledge vs chat; sequencing prompts for a long asset; a model condenses or truncates.
- **Inputs → outputs:** asset type + length band + 5–20 example files (varied niches, real copy) + per-job brief/URL → a reusable project → outline (with estimated length) → approved → full draft over several "continue" turns → edited draft.
- **Rules:**
  - **DO** make one project per asset type and per VSL length band; don't mix lengths in one knowledge base. [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **DO** keep instructions short and in the 4-part pattern: role + length band; what the knowledge files are; "analyze ... synthesize ... along with your judgement"; how inputs arrive + "don't rush or condense". Put the same text in description and instructions. [06-01 02:55–05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md); [03-05 00:28](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md)
  - **DO** fill knowledge with varied examples across niches and lengths; "the content is not as important as the structure or like the syntax". Don't load only your own niche: make the model "work harder". [09-02 05:52–06:23; 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** label sections inside your example files (HOOK, LEAD, UMP, UMS ...) so the model learns structure. (derived from the annotated Emma/Genius Wave/Mitolyn files [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md))
  - **DO** give per-job facts in the chat (brief, product URL, research), never in project knowledge; enable web search for URLs. [05-02 01:02–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)
  - **DO** ask for an outline (with estimated length/timings) first and write only after approval: "After I have reviewed the outline and approved I will let you know and we can actually write it." [06-01 long-form prompt](../lessons/06-01-claude-vsl-projects-setup-overview.md); [15-05 02:10–02:43](../lessons/15-05-claude-project-for-writing-email-sequences.md); [09-02 27:01–27:45](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** keep "Please don't try to rush or condense anything ... whenever you run out of space just prompt me and I'll tell you to continue" in every long-output project, and reply "continue". [06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md); [14-03 00:00–00:29](../lessons/14-03-claude-projects-for-upsells.md)
  - **DO** state goal, CTA, awareness level and max length in each job prompt; the 3–7 project says "I'll typically specify the goal". [06-01 03:38](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-04 v2 05:47](../lessons/07-04-short-vsl.md)
  - **DO** add "Do not reuse any claims, statistics, studies or credentials from the examples; use only the facts in the brief" to job prompts when examples are aggressive. (derived; [06-01 07:48–08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md))
  - **DON'T** over-tune: "use the processes rather than try to tweak them"; tweaks give "incremental gains". [06-01 04:24–05:16](../lessons/06-01-claude-vsl-projects-setup-overview.md)
  - **IF** the model ignores an attachment **THEN** re-upload it and name it ("That's what I'm referring to"). [05-05 07:05–09:52](../lessons/05-05-financial-promo-example.md)
  - **IF** Claude starts writing HTML/artifacts for page copy **THEN** stop it and tell it not to code. [10-01 38:37–39:22](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md)
  - **IF** a model stalls, glitches or hits limits **THEN** switch model/host (Sonnet 4 → 3.7, Claude → Gemini or Poe) rather than debug. [07-01 v1 21:45; 43:39](../lessons/07-01-long-form-vsl.md)
  - **IF** an ad must not pitch the product **THEN** feed only the first half of the VSL (through UM, promises, spokesperson). [04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **See also:** [composite-vs-swipe](composite-vs-swipe.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [prompts library](../libraries/prompts.md) · [brief-2-0](brief-2-0.md) · [vsl-length-bands](vsl-length-bands.md)

## Definition
A Claude Project = instructions + knowledge files + chats that inherit both. In RMBC II each project is a "recipe" for one asset type [08-01 recap](../lessons/08-01-rmbc-ii-mid-course-recap.md). Stefan's setup steps: "create new project, you name it ... What are you trying to achieve? Copy this, paste it in ... hit plus, add content, or just drag and drop PDFs". [06-01 05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md) By the ads module: "you should understand and be like a master of Claude projects so you can set them up for anything". [01-01 26:38–27:34](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)

### Three layers: what goes where
| Layer | Contains | Never contains | Source |
|---|---|---|---|
| Instructions (= description) | Role, length band, what the files are, "analyze → synthesize → judgement", "don't rush or condense ... continue" | Product facts, a single example to rewrite | [06-01 02:55–04:24](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Knowledge files | Varied real examples (transcripts, pages, sequences), templates (New Brief, classic VSL outline), hook database | The current product's brief | [06-01 05:46–08:18](../lessons/06-01-claude-vsl-projects-setup-overview.md); [05-02 00:00–01:02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Chat (per job) | Brief / URL / research PDFs, goal, CTA, awareness, length, staged requests and feedback | — | [05-02 01:02–03:07](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |

### The instruction pattern (derived from the four VSL projects)
```text
Your job is to generate [ASSET TYPE]. They will typically be between [X] and [Y] [minutes/words] in length.
The documents in your knowledge base include [examples of ASSET TYPE] which we can model off while writing new ones.
What you'll want to do is analyze the structure of the various [ASSET TYPE] examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new [ASSET TYPE].
In general, when you go to write I'll give you various inputs or even an outline and a gameplan.
One IMPORTANT Note. Please don't try to rush or condense anything. Instead, whenever you run out of space just prompt me and I'll tell you to continue.
```
Verbatim originals for all four VSL projects: [06-01 Prompts](../lessons/06-01-claude-vsl-projects-setup-overview.md) and the [prompts library](../libraries/prompts.md).

### Projects built in the course
| Project | Knowledge files | Per-job input | Staged prompts | Source |
|---|---|---|---|---|
| Unique Mechanisms | 9 PDFs: UM definitions with examples, worked UMP/UMS, ideation prompt, VSL structure, swipes | Unified research doc + mechanism summary + awareness | Ideate → evaluate (other LLMs) → expand top 2 | [03-05](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) |
| RMBC II Brief Generator | "The New Brief" + classic VSL outline | Product URL, UMP, research, ingredients; "Please go ahead and get started now." | Brief → save → revise by chat | [05-02](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Long Form VSL Generator | 8 transcripts (6–11k words each, 3 annotated) | Brief | Outline + estimated length → approve → write → continue | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Medium Length VSL Generator | 5 transcripts | Brief + target minutes | Same | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| 3-7 Minute VSL Generator | 8 transcripts with "Video Length" lines | Brief + goal (tease vs sell) | Same | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Short Length VSL Generator | 1 combined doc of 12 scripts | Brief or existing VSL + 1 hook + CTA + awareness + max length | Concepts (5–10) → script → one-lever variants | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-04](../lessons/07-04-short-vsl.md) |
| ADHD/hook ad project | Instructions + ad breakdowns + hook database | First half of VSL + pain points | 10 concepts → full 1–3 min scripts → edit → tracked IDs | [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Advertorial project | Real advertorials, short/medium/long, varied niches (saved copies) | Landing page / sales page / brief + winning ad caption | Prompt 1: 10 hooks → Prompt 2: hook # + outline at length → Prompt 3: write → 50% shorter variant | [09-02](../lessons/09-02-claude-project-for-advertorials.md) |
| PDP process | Extracted structure outlines saved per page | Outline + our brief or URL | Templatize a winning PDP → write ours; "don't code" | [10-01](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) |
| Claude Upsell Generator | 5 swipe PDFs | Product link or brief, what they just bought, upsell type, number, length | Section by section over "continue" turns | [14-03](../lessons/14-03-claude-projects-for-upsells.md) |
| Claude Email Sequence Generator | 15 sample sequences | Sequence type, length, discount ladder, URL or brief, tone | Outline → approve → write with 2–3 subject lines each | [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md) |

## Why it matters
- Instructions stay stable; only the chat changes per job, so one setup produces "endless" assets. [09-02](../lessons/09-02-claude-project-for-advertorials.md); [15-05](../lessons/15-05-claude-project-for-writing-email-sequences.md)
- Many varied examples + "synthesize" yields a composite rather than a near-copy of one letter, which Stefan says avoids being "too close for comfort" with another brand's work. [06-01 08:18–10:13](../lessons/06-01-claude-vsl-projects-setup-overview.md) → [composite-vs-swipe](composite-vs-swipe.md)
- Outline-first catches structural errors (who tells the story, where the brand first appears, "zigs and zags") before thousands of words are written. [07-01 v1 32:48–38:07](../lessons/07-01-long-form-vsl.md); [09-02 27:01–27:45](../lessons/09-02-claude-project-for-advertorials.md)
- The "continue" line prevents condensed long-form output (less critical now: "Claude just has really long outputs now", but kept). [06-01 03:56](../lessons/06-01-claude-vsl-projects-setup-overview.md)

## How to use (steps)
1. **Pick the asset and band.** One project each (VSL bands: see [vsl-length-bands](vsl-length-bands.md)).
2. **Write instructions** with the 4-part pattern; paste into description and instructions. [06-01 05:46](../lessons/06-01-claude-vsl-projects-setup-overview.md)
3. **Load knowledge:** varied, real, saved copies (live pages get taken down [09-02 03:00–04:35](../lessons/09-02-claude-project-for-advertorials.md)); label sections; optionally add running time to each transcript (unproven experiment, "I'm wondering" [06-01 01:29](../lessons/06-01-claude-vsl-projects-setup-overview.md)).
4. **Open a chat per job:** brief/URL + goal + CTA + awareness + length + "don't reuse example claims".
5. **Stage 1 – outline:** "come up with an outline ... provide an estimated length ... After I have reviewed the outline and approved I will let you know". [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)
6. **Stage 2 – review outline as copy chief:** fix narrator, flow, brand-reveal point; optionally upload your own reference outline and ask for a revised version. [01-01 18:30–19:44](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md)
7. **Stage 3 – write:** "Let's go ahead and write it"; "if you need to do this over multiple outputs, that's fine ... I'll prompt you to continue". [07-01 v1 41:15–42:30](../lessons/07-01-long-form-vsl.md)
8. **Stage 4 – continue** until complete; measure length yourself (Claude said ~8,500 words; actual 5,707). [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
9. **Stage 5 – edit and vary:** [llm-copy-chief-editing](llm-copy-chief-editing.md); then leads/hooks/shorter versions as separate requests.

## Examples
| Case | Recipe element shown | Source |
|---|---|---|
| Medium VSL for Unity serum: brief → "give me an outline ... along with your estimate for how long it'll be. Let's aim for about 18 minutes" (Claude "estimates a little low") | Outline-first with target length | [05-02 23:00–25:57](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Short VSLs: "Here's a brief ... give me 5-10 short VSL concepts you think would be worth testing?" | Concepts before scripts | [05-02 33:36](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| Financial long form: attachment ignored → re-upload + "That's what I'm referring to" → "this is why you gotta stand on top of it" | Attachment check | [05-05 07:05–09:52](../lessons/05-05-financial-promo-example.md) |
| Email: "Can you please outline this sequence for me and then after I approve I'll have you write it." | Outline gate in a non-VSL project | [15-05 02:10–02:43](../lessons/15-05-claude-project-for-writing-email-sequences.md) |
| Upsell: "We shouldn't assume they bought the first upsell" | Correcting logic in chat | [14-03 02:38](../lessons/14-03-claude-projects-for-upsells.md) |
| Hook ads: only first half of VSL fed so the ad sells the click | Controlling what the model can see | [04-10 48:57–49:52](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |

## Common mistakes
- **Over-tuning the setup** "as a distraction from actually doing the work". [06-01 04:24–05:16](../lessons/06-01-claude-vsl-projects-setup-overview.md)
- **One-niche knowledge base:** produces topic copies, not structure transfer. [09-02 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)
- **Writing without an outline:** long drafts with structural "zigs and zags". [09-02 27:01–27:45](../lessons/09-02-claude-project-for-advertorials.md)
- **Leaving anchoring sections in the brief** (brief's own hook list) when leads will be written separately: strip them. [07-01 v1 10:26–11:31](../lessons/07-01-long-form-vsl.md)
- **Trusting model length estimates.** [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)
- **Shipping example-derived proof:** every course project output contains invented testimonials, doctors, studies or numbers ("to be compliant, you would obviously want to put real testimonials" [09-02 38:01](../lessons/09-02-claude-project-for-advertorials.md)).
- **Stale hook database:** Airbnb lead swap kept returning skincare hooks because the hook doc still held skincare seed examples. [07-01](../lessons/07-01-long-form-vsl.md)

## Where it's taught
| Lesson | Coverage | Timestamps |
|---|---|---|
| [01-01 Overview](../lessons/01-01-welcome-to-rmbc-ii-and-in-depth-course-overview.md) | Projects per asset; outline-first demo | 16:51–19:44; 26:38–27:34 |
| [03-05 UM project](../lessons/03-05-creating-a-claude-project-for-unique-mechanisms.md) | Same text in description + instructions; 9 PDFs | 00:28–01:28 |
| [05-02 Brief generator](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Knowledge vs chat inputs; hand-off prompts | 00:00–03:07; 23:00–33:36 |
| [06-01 VSL projects setup](../lessons/06-01-claude-vsl-projects-setup-overview.md) | Four projects, instruction pattern, inventory, don't over-tune | 00:00–11:17 |
| [07-01](../lessons/07-01-long-form-vsl.md)–[07-04](../lessons/07-04-short-vsl.md) | Live staged runs | 07-01 v1 28:33–42:30 |
| [04-10 Hooks](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) | Hook project | 45:07–57:38 |
| [09-02 Advertorials](../lessons/09-02-claude-project-for-advertorials.md) | Varied-niche knowledge; 3-prompt loop | 01:33–44:02 |
| [10-01 PDPs](../lessons/10-01-pdp-overviews-and-claude-processes-for-writing-new-ones.md) | Structure extraction; "don't code" | 38:37–53:12 |
| [14-03 Upsells](../lessons/14-03-claude-projects-for-upsells.md) | Continue turns; build your own projects | 00:00–10:44 |
| [15-05 Emails](../lessons/15-05-claude-project-for-writing-email-sequences.md) | Outline gate; strategist role | 00:00–23:12 |

## Cross-course notes
- **Evolve Copywriting** [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md): "The point ... was not to give you another copywriting prompt"; the skill is directing AI with named techniques. RMBC is prompt- and project-heavy. They agree the human owns judgment and facts. **Agent default:** use RMBC's project recipe as the mechanics, and Evolve's named techniques (stakes, bridges, labels, mechanisms) as the vocabulary for feedback turns.
- **Evolve Start Here** [angle generation prompt](../../../evolve/start-here/frameworks/angle-generation-prompt.md) is a single-prompt tool; RMBC splits generation into project + staged chat. Use the RMBC staging for anything over ~300 words.
- **Repo** [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) is the UGC equivalent; for short VSLs the RMBC short-length project recipe adds the brief-first and one-lever-variant steps.

## Related
[composite-vs-swipe](composite-vs-swipe.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [brief-2-0](brief-2-0.md) · [vsl-length-bands](vsl-length-bands.md) · [modular-creative-and-hook-swaps](modular-creative-and-hook-swaps.md) · [vsl-build-with-claude](../frameworks/vsl-build-with-claude.md) · [prompts library](../libraries/prompts.md)
