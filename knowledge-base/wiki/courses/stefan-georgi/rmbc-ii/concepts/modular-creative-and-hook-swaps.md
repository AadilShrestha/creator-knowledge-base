---
title: "Modular creative and hook swaps (locked body, swapped hooks, IDs, one-variable tests)"
type: concept
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi; guests Max Finn (12-04 TikTok) and Patrick Stiles (16-05) where labelled"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-10-using-ai-to-generate-endless-good-hooks.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-03-vsl-leads-after-the-opening-hook.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-05-vsl-product-buildup-and-reveal.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-08-medium-vsls-structures-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-04-tiktok-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [hooks, hook-testing, modular-creative, micro-lead, creative-testing, hook-database, nope-ladder, iteration]
updated: 2026-11-02
---

# Modular creative and hook swaps
> Keep a proven body locked and swap only the opening (hook, micro-lead, thumbnail or image); tag every creative with hook, lead and script IDs so winners can be recombined, and add new hooks to a winner one or two at a time.

## 🤖 Agent use
- **Use when:** turning one ad or VSL into many test variants; planning a hook test; building a hook database and creative tracking sheet; briefing editors on which piece to change; diagnosing whether a lift came from the hook or the body.
- **Inputs → outputs:** a proven (or chosen) body script, a hook list, destination and CTA, awareness level → N variants that differ in one variable, each with an ID (script, lead, hook), a test plan, and a continuity check for each swap.
- **Rules:**
  - **DO** hold the body and change the hook: "everything after the revelation/education section is pretty much the same, but we do a different hook." [07-03 v2 08:58–09:35](../lessons/07-03-3-7-minute-vsl.md)
  - **DO** prompt the swap explicitly: paste the new hook verbatim and say "the rest of the ad from this point on can basically stay the same". [07-04 v3 05:43](../lessons/07-04-short-vsl.md)
  - **DO** change one lever per variant (hook, CTA, mechanism depth, product-vs-tease, awareness). [07-04 Agent use](../lessons/07-04-short-vsl.md); [07-03 v1 09:56–10:26](../lessons/07-03-3-7-minute-vsl.md)
  - **DO** test hooks and thumbnails with the rest of a video fixed: "that will have a massive difference on conversion rate". [12-01 00:12:30](../lessons/12-01-meta-ads.md)
  - **DO** test images with copy held constant: "same copy, different images will often have very different results". [12-01 00:06:36](../lessons/12-01-meta-ads.md)
  - **DO** track Script ID, Lead ID and Hook ID per creative ("as we scale… we can modularly combine stuff. This was the winner, take these hooks, take these leads."). [04-10 57:38](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DON'T** stack 10 new hooks on a proven winner; add "one more at a time or two". [04-10 1:01:07–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
  - **DO** re-check term continuity after every opening swap; MiamiMD's body says "stop fibroblast failure" after a new hook that never introduced it. [04-08 v3 14:08](../lessons/04-08-medium-vsls-structures-and-examples.md)
  - **DO** keep the "Nope" ladder logically tied to the hook (laundry hook → cleaners, not "sugar causes diabetes? Nope"). [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md)
  - **IF** the VSL runs in-feed **THEN** expect "dozens and dozens" of micro-leads before one scales. [04-03 39:00–39:27](../lessons/04-03-vsl-leads-after-the-opening-hook.md)
  - **IF** a VSL underperforms **THEN** test leads first; test far more than 5-10. [04-05 30:58–35:38](../lessons/04-05-vsl-product-buildup-and-reveal.md) Guest agrees: "the highest impact split test is always going to be split testing the lead of the video" (guest claim, Patrick Stiles). [16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)
  - **IF** several creatives share one TikTok ad group **THEN** make them near-identical (same video, different hooks) (guest claim, Max Finn). [12-04 v5 04:41–06:09](../lessons/12-04-tiktok-ads.md)
  - **DON'T** let a swapped hook carry a claim the body can't support, or any unverified health/finance claim. (derived; see [compliance-red-flags](compliance-red-flags.md))
- **See also:** [hook-generation-system](../frameworks/hook-generation-system.md) · [sell-the-click](sell-the-click.md) · [classic-vsl-structure](classic-vsl-structure.md) · [cro-testing](../frameworks/cro-testing.md) · [hooks library](../libraries/hooks.md) · [prompts](../libraries/prompts.md)

## Definition
- **Locked body + swapped hook:** one script "root" with several openings. Nooro's medium VSLs: same "root of the sales letter", different "hook or… micro lead that's going to bring you in a different way". [04-02 04:45–06:36](../lessons/04-02-vsl-fundamentals-classic-structure.md)
- **Hook stack:** several hooks in the first seconds. RMBC's "ADHD Super-Hook Ad" has "numerous hooks throughout, including several in the beginning", and the first 30 seconds "should jump around a good amount". [04-10 45:07–45:41](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) TikTok guest version: a text + visual + audio hook stack in the first three seconds, "three shots instead of one" (guest claim, Max Finn). [12-04 v7 04:17–04:45](../lessons/12-04-tiktok-ads.md)
- **Hook IDs:** Opal Beauty "AdCreatives Database" sheet; tabs Videos, Script Database, Lead Database, Hook Database; columns Creative, Status, Frame Link, Launch Date, Script ID, Lead ID, Hook ID, Creative Name, Winner?; name format `AD0001V15_SC001_LD003_SS5`. [04-10 56:32–57:48](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- **Nope ladder:** a contrarian opener that knocks down the usual remedies one by one: "Lifting your legs up is the best way to relieve edema, right? Nope. What about compression socks? Really?" (Nooro); same pattern in Vital BP and ReActivate. [06-01 Examples](../lessons/06-01-claude-vsl-projects-setup-overview.md); [04-02 mini #2 doc](../lessons/04-02-vsl-fundamentals-classic-structure.md) Template: "You think X, right? Nope. What about Y? Nope. How about Z? Still nope. Here's what's really…" [07-03 v2 11:04–12:11](../lessons/07-03-3-7-minute-vsl.md)
- **Modular scenes:** hook, problem, alternative solution, our solution, proof, offer as swappable blocks; "change one scene at a time to turn one winner into many ads" (guest claim, Max Finn). [12-04 v6 01:27–04:49](../lessons/12-04-tiktok-ads.md)

## Why it matters
- Hooks decide reach into the body. Stefan: "it's really going to come back down to the hook a lot"; hooks are "how you can generate endless ads". [07-04 v1 02:04; 14:45](../lessons/07-04-short-vsl.md)
- A locked body makes results readable: if only the hook changed, the hook caused the difference. (derived)
- Big DR advertisers test this way: Golden Hippo / Gundry are "beasts about just testing tons and tons of different little hooks and openings". [04-02 04:45–06:36](../lessons/04-02-vsl-fundamentals-classic-structure.md) Miami MD runs one caption and one video with different thumbnails: "It's really just thumbnails." [12-01 00:17:33–00:19:58](../lessons/12-01-meta-ads.md)
- Repetition in an Ad Library is a weak winner signal: "you can tell that a hook's a big winner and then they'll also be throwing in other hooks" (instructor inference). [12-01 00:21:50](../lessons/12-01-meta-ads.md)

## How to use (steps)
1. **Pick the body.** A proven winner, or one structure from [classic-vsl-structure](classic-vsl-structure.md) / the 3-7 minute skeleton.
2. **Build a hook database.** Run the deep-research hook prompt in several LLMs; paste keepers into one doc; load it into the ads project. [04-10 32:59; 28:33–29:31](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
3. **Mark the swap boundary.** For the 3-7 minute blood-sugar skeleton: Hook 0:00-0:15 (hook + Nope sequence) → Problem Agitation 0:15-1:00 (hook-specific) → Revelation/Education 1:00-2:00 (identical) → Proof 2:00-2:30 (identical) → CTA 2:30-3:00 (identical). [07-03 docx](../lessons/07-03-3-7-minute-vsl.md)
4. **Write variants** that change one thing. Use the prompt pattern below.
5. **Continuity check:** every term, promise and Nope item in the new opening must connect to the locked body. [04-08 v3 14:08](../lessons/04-08-medium-vsls-structures-and-examples.md)
6. **ID and launch.** Name each creative `AD####V##_SC###_LD###_SS#`; mark status and winner. [04-10 57:48](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
7. **Recombine.** Take winning hooks + winning leads; add one or two hooks to a winner at a time and re-test. [04-10 1:00:08–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)

### One-variable test menu (course examples)
| Variable | Course example | Source |
|---|---|---|
| Hook (video, first 3-10 s) | Odorless Cat: same caption, music, body; different video hooks and thumbnails | [12-01 00:07:11–00:12:30](../lessons/12-01-meta-ads.md) |
| Image (static) | Odorless Cat: same caption over several cat images | [12-01 00:02:15–00:06:36](../lessons/12-01-meta-ads.md) |
| Thumbnail | Miami MD: same caption + same 12-14 min video, different thumbnails | [12-01 00:17:33–00:19:58](../lessons/12-01-meta-ads.md) |
| Micro-lead | Nooro edema A "Say goodbye to edema…" vs B "This is why people with edema are switching…" | [04-02 03:05–04:45](../lessons/04-02-vsl-fundamentals-classic-structure.md) |
| Hook (3-7 min ad) | Blood sugar: coffee → skip-breakfast → laundry detergent hook, same body | [07-03 v2 08:58–12:11](../lessons/07-03-3-7-minute-vsl.md) |
| Hook (short ad) | Blood sugar: coffee hook → sleep-apnea hook, same mechanism and CTA | [07-04 v3 05:43](../lessons/07-04-short-vsl.md) |
| CTA / product reveal | Eye serum V2 "save up to 57% but we don't reveal the prices" vs V3 "go watch the presentation", no product | [07-04 v1 12:15–13:54](../lessons/07-04-short-vsl.md) |
| Mechanism depth | "more of the mechanism… versus… less mechanism and is more to the point" | [07-03 v1 09:56–10:26](../lessons/07-03-3-7-minute-vsl.md) |
| Length | 1:30 cut of a 3-7 min script; Nooro same caption with 15, 16, 4 and 2 min videos | [07-03 v1 08:33](../lessons/07-03-3-7-minute-vsl.md); [12-01 00:30:37](../lessons/12-01-meta-ads.md) |
| Spokesperson | Founder → anti-aging doctor; woman → doctor for the night-routine hook | [07-02 v1 02:28–07:58](../lessons/07-02-medium-length-vsl.md); [04-10 54:02](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Awareness | Airbnb ads "going mostly to problem aware people" | [07-04 v2 05:47](../lessons/07-04-short-vsl.md) |

### Prompt patterns (verbatim from the lessons)
Swap request (07-04, blood sugar; from the Claude conversation doc):
```text
[new hook pasted verbatim] … the rest of the ad from this point on can basically stay the same
```
Transitions fix after a hook stack (04-10 [55:12]):
```text
Good job with loading up the opening with hooks. I do think we need some better transitions between some of the hooks. So let's focus on better transitions between hook two and three and between three and four in the opening.
```
Full prompts: [libraries/prompts](../libraries/prompts.md); [04-10](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md); [07-04](../lessons/07-04-short-vsl.md).

## Examples (structure only; claims not reusable)
| Case | Pattern | Source |
|---|---|---|
| Opal Beauty (Stefan's brand) hook-stacked ads | Concept stacks ("Stop using hyaluronic acid until you watch this."…), creative IDs, winner then "stacked three more hooks on top of it" | [04-10 05:37; 58:39–1:00:08](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md) |
| Nooro edema in-feed VSLs | Two openings, one root | [04-02 03:05–06:36](../lessons/04-02-vsl-fundamentals-classic-structure.md) |
| MiamiMD Advanced Crepe Fix | Hook test left a term seam ("fibroblast failure") | [04-08 v3 13:33–14:08](../lessons/04-08-medium-vsls-structures-and-examples.md) |
| Odorless Cat / Miami MD / David Protein | Copy held constant; image, hook, thumbnail or creator varied | [12-01 00:02:15–00:24:07; 00:53:15](../lessons/12-01-meta-ads.md) |
| Blood-sugar 3-min ads | Hook-swap factory with identical revelation, proof, CTA | [07-03 v2 00:00–12:52](../lessons/07-03-3-7-minute-vsl.md) |

## Common mistakes
- Swapping a hook and leaving dangling terms or promises in the body. [04-08 v3 14:08](../lessons/04-08-medium-vsls-structures-and-examples.md); see [congruence](congruence.md).
- Greedy stacking: Stefan admits "I am probably being a little bit greedy" stacking many hooks in new ads. [04-10 1:01:07–1:02:35](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- Not knowing which stacked hook won: "I don't know that we have it down to the hooks specifically"; tag at ad level, then test variants. [04-10 58:39–1:00:08](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md)
- Seed hooks from another niche leaking into a new project (skincare hooks in the Airbnb run). [07-01 v5 54:02–55:07](../lessons/07-01-long-form-vsl.md)
- Writing 3-5 entirely different 300-700 word leads instead of 2+ opening-line options. [04-03 35:22](../lessons/04-03-vsl-leads-after-the-opening-hook.md)
- Accepting generic or "too aggressive" hooks from the model. [07-04 v1 10:49; v4 06:26](../lessons/07-04-short-vsl.md)
- Fixating on small player toggles before testing the lead (guest claim). [16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)

## Where it's taught
- [04-10 Endless good hooks](../lessons/04-10-using-ai-to-generate-endless-good-hooks.md): hook database [28:33–39:22]; super-hook ads [45:07]; IDs and tracking [56:32–57:48]; gradual stacking [58:39–1:02:35].
- [07-03 3-7 minute VSL](../lessons/07-03-3-7-minute-vsl.md): hook-swap test [v2 08:58–09:35]; Nope consistency [v2 11:04–12:11]; skeleton (docx).
- [07-04 Short VSL](../lessons/07-04-short-vsl.md): one-lever variants; swap prompt [v3 05:43].
- [04-02 VSL fundamentals](../lessons/04-02-vsl-fundamentals-classic-structure.md): Nooro two openings [03:05–07:00].
- [04-03 Leads](../lessons/04-03-vsl-leads-after-the-opening-hook.md): opening-line options [35:22]; dozens of micro-leads [39:00].
- [04-05 Build-up and reveal](../lessons/04-05-vsl-product-buildup-and-reveal.md): lead first [30:58–35:38].
- [04-08 Medium VSLs](../lessons/04-08-medium-vsls-structures-and-examples.md): term continuity [v3 14:08].
- [06-01 Claude VSL projects](../lessons/06-01-claude-vsl-projects-setup-overview.md): Nope openers in the example files.
- [12-01 Meta ads](../lessons/12-01-meta-ads.md): image/hook/thumbnail tests [00:02:15–00:24:07].
- [12-04 TikTok ads](../lessons/12-04-tiktok-ads.md) (guest): hook stack, modular scenes, near-identical ad groups [v5–v7].
- [16-05 VSL benchmarks](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) (guest): lead split test first [20:35–21:00].

## Cross-course notes
- **Tether Lab** [iteration vs variation](../../../../concepts/iteration-vs-variation.md) and [creative testing system](../../../../frameworks/creative-testing-system.md): a hook swap on a locked body is a single-variable iteration. **Agreement.** [Test and iterate playbook](../../../../playbooks/test-and-iterate.md) for the test loop.
- **Evolve Copywriting** [iteration playbook](../../../evolve/copywriting/frameworks/iteration-playbook.md) warns against "spamming hook iterations… that you think are better, but they don't convert" when a breakthrough dies; dissect first. RMBC pushes volume of hook swaps. **Agent default:** on a new body, run hook swaps at volume; on a fading winner, diagnose (components, bridge, page) before adding hooks. [Evolve hooks](../../../evolve/copywriting/concepts/hooks.md), [iteration outcomes](../../../evolve/copywriting/concepts/iteration-outcomes.md).
- **Evolve Start Here** [campaign structure 3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md) for how hook variants are grouped in a Meta test.

## Related
[sell-the-click](sell-the-click.md) · [classic-vsl-structure](classic-vsl-structure.md) · [vsl-length-bands](vsl-length-bands.md) · [congruence](congruence.md) · [llm-copy-chief-editing](llm-copy-chief-editing.md) · [hook-generation-system](../frameworks/hook-generation-system.md) · [cro-testing](../frameworks/cro-testing.md) · [hooks library](../libraries/hooks.md)
