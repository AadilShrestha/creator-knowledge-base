---
title: "Playbook: UGC Script Writing (angle brief → test-ready UGC script)"
type: playbook
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/frameworks/story-frameworks-for-ads.md
  - knowledge-base/wiki/frameworks/skeptic-format.md
  - knowledge-base/wiki/frameworks/visual-weight-hierarchy.md
  - knowledge-base/wiki/frameworks/tone-shifting.md
  - knowledge-base/wiki/frameworks/creative-testing-system.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md
tags: [playbook, ugc, script, hooks, beat-sheet, on-screen-text, b-roll, sight-smell, proof, cta, hook-variants, story-frameworks]
updated: 2026-10-20
---

# Playbook: UGC Script Writing
> From one `angle_brief` to a production-ready UGC script: pick a **story framework**, write **hook options**, lay out a **timed beat sheet** (15/30/45/60 s) with ~2/3 setup, add **on-screen text**, **b-roll and visual cues** per beat, **real proof**, a **definitive CTA**, and package **3 hooks × 2 bodies** for testing. Then run the [UGC script checklist](../rubrics/ugc-script-checklist.md) and hand off to the [creator brief](creator-brief.md).

## 🤖 Agent use
- **Use when:** an angle is marked `ship_to_script`, or a winning static needs its video version.
- **Inputs → outputs:** `angle_brief` + product truth sheet + research brief (customer phrases) + target length(s) → `ugc_script` (template below) with 3 hook variants, 2 body variants, timed beats, overlays, shot notes and a proof ledger.
- **Rules:**
  - DO name one framework and paste its steps into the prompt; LLMs blend similar ones (Monomyth → Hero's Journey) [May14 0:50:44–0:52:19].
  - DO always tell the LLM the **main character** and the **final CTA** [May14 0:35:40].
  - DO spend **~2/3 of the runtime on setup** (problem + lived experience); solution and CTA in the last scenes. "The punchline is not the point." [May14 0:19:45–0:20:41]
  - DO add a **realism** beat (skeptical, "cautiously at first", imperfect results); never "it transformed everybody overnight" [May14 0:41:04–0:41:54].
  - DO put the core message in **frame 1** — on screen and/or spoken. A winning static's headline goes in frame 1 verbatim [R3 0:18:56–0:21:32]; build the script from the static's winning message when one exists [Jun11 0:32:53].
  - DO write lines as the creator would say them, and brief them to say it **in their own words** [May14 0:22:33–0:24:30].
  - DO write a definitive CTA, never "Shop now" [R1 0:26:52–0:29:09].
  - DON'T fabricate proof, testimonials, results, scarcity, stats or endorsements (wiki rule from Module 4; [contradictions](../contradictions.md) row 10).
  - DON'T stack two emotions; one core emotion per script ([one core emotion](../concepts/one-core-emotion-per-ad.md)).
- **See also:** [Hooks library](../libraries/hooks.md) · [Rewrites library](../libraries/rewrites.md) · [Prompts library](../libraries/prompts.md) · [Story frameworks](../frameworks/story-frameworks-for-ads.md) · [Skeptic format](../frameworks/skeptic-format.md) · [Native advertising](../concepts/native-advertising.md) · [UGC script checklist](../rubrics/ugc-script-checklist.md) · [Ad scorecard](../rubrics/ad-scorecard.md) · Other creator: [Evolve: write a video ad script](../courses/evolve/copywriting/playbooks/write-a-video-ad-script.md)

**Source key:** May7 = [Live May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · May21 = [Live May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · J = [Joanna Wallace](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md) · R1 = [Roast #1](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jun18 = [Live Jun 18](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) · R2 = [Roast #2](../courses/tether-lab/05-live-recordings/2025-06-25-roast-my-ads-2.md) · Jul9 = [Live Jul 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · Jul16 = [Live Jul 16](../courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md). **(derived)** = our application of a course rule; **(pipeline design)** = our process.

## Procedure

### Step 1: Pick the story framework
Use the [Loadout quick picker](../frameworks/story-frameworks-for-ads.md#quick-picker-decision-table). Short version:

| Angle / stage | Framework | Why (Sarah) |
|---|---|---|
| Cold UGC, nothing is working | **Pixar** | her #1; "fantastic for injecting emotion" [May14 0:06:20; 0:14:43] |
| UGC needing a proof tail | **Story Spine** | "ever since then, people have been asking me…" [May14 0:11:35] |
| Switching from a competitor/habit | **SCQA** | a question reframes the cause [May14 0:08:16] |
| Fake podcast / retargeting | **In Medias Res** | her #2; an open loop [May14 0:09:25; 0:14:20] |
| Slow, organic-feeling arc; character narrator (vet, trainer) | **Freytag's Pyramid** | [May14 0:05:10; 0:42:30] |
| Claim you can demo on camera; skeptical buyers | **Skeptic format** | claim → doubt → test → reluctant concession ([skeptic format](../frameworks/skeptic-format.md)) |
| Founder-led | **Founder's Post** | [May14 0:15:15] |
| Hard close, bottom of funnel | PAS / AIDA | only "really trying to sell hard" [May14 0:07:57] |
| Shame-risky concept | Move the shame onto a character (skit) | [mirror effect](../concepts/mirror-effect.md) [May21 0:49:15–0:52:00] |

Pick the **narrator**: the customer, or someone around them (vet, trainer, neighbour, the pet); each narrator is an avatar test [May14 0:33:17; 0:40:09].

### Step 2: Write hook options (at least 6, keep 3)
Draw patterns from [hooks library](../libraries/hooks.md); fill them with **our** customer's words from the research brief. Course-sourced patterns:

| Pattern | Example from the course | Heuristic(s) | Best stage |
|---|---|---|---|
| Reluctant convert | "I'm gonna be honest… I did not want to like this." [May14 0:18:43] | messenger, curiosity | E2 |
| Guilty habit confession | "You ever buy a skincare product just knowing it's not gonna work… but you do it anyway?" [May14 0:17:40] | in-group, open loop | E1/E2 |
| Mid-rant (In Medias Res) | "No, because explain to me why every skincare brand thinks I'm gullible…" [May14 0:20:56] | open loop, in-group | E2/P |
| Situational "every" | "Every bowl that we gave him, he destroyed." [R3 0:33:42] | specificity | E2 |
| "How I" (risk reduction) | "This is how I [outcome] in [time]" [May7 0:21:48–0:22:46] | authority, risk reduction | E1/E2 |
| Trigger event | "I just got a puppy and nobody warned me about ___" (derived skeleton, [TEEP](../frameworks/teep-journey.md)) | specificity | T |
| Industry truth + smart shopper | "A lot of [these] have nasty stuff in them, and you're a smart shopper for noticing." [Jun11 0:20:12] | validation | E2 |
| Honest admission | "It's probably not going to taste super great, but it dissipates quicker than everybody else." [Jun11 0:25:35] | barrier buster | E2 |
| Identity confrontation | "You're Lactose Intolerant. Start Acting Like It." [R3 0:55:52] | framing, Ought | E2/P |
| Validation | "You know your body the best. If you don't feel right, something's not right." [May21 0:42:33] | validation over authority | E1 |
| Stare into camera | "Did you take your creatine today?" ([observer expectancy](../concepts/heuristics/observer-expectancy-effect.md)) | observer expectancy | P |

Each hook = **spoken line + on-screen text (≤7 words) + first visual**. Each of the 3 kept hooks must state a *different* core message or lever, so the test teaches something ([creative testing](../frameworks/creative-testing-system.md#ugc-application-derived)).

### Step 3: Beat sheet with timings
Timings are **(derived)** from the 2/3-setup rule [May14 0:19:45] and the hook window; adjust to the framework's steps.

| Beat | 15 s | 30 s | 45 s | 60 s | Job |
|---|---|---|---|---|---|
| Hook | 0–2 | 0–3 | 0–3 | 0–3 | Core message in frame 1; stop the scroll |
| Problem / situation | 2–6 | 3–12 | 3–16 | 3–22 | One specific situation, customer words, "four levels deep" [R3 0:33:42] |
| Lived experience / failed attempts + realism | 6–10 | 12–20 | 16–30 | 22–40 | "Expensive ones. Cheap ones." Doubt, the product graveyard |
| Turn: product + mechanism | 10–12 | 20–24 | 30–36 | 40–47 | Why it works; show, don't tell |
| Proof | 12–13.5 | 24–27 | 36–41 | 47–55 | Demo / time sequence / real review; ability crusher answered |
| CTA (+ offer at P stage) | 13.5–15 | 27–30 | 41–45 | 55–60 | Definitive CTA tied to a person or habit |
| Setup share | ~0.67 | ~0.67 | ~0.67 | ~0.67 | |

Length plan: Sarah runs long (2–3 min) as-is first, then cuts to 30 s and 15 s with ChatGPT ("Chat, we need to cut this down to 30 seconds"), keeping avatar tests at a constant length [May14 0:45:41–0:46:50]. Pace: cuts every 2–3 s, up to ~4 s; slow the voice and pause on key lines, "the faster you go through a story the more difficult it is for people to attach emotionally" [May14 0:43:30–0:48:12].

### Step 4: On-screen text
- Frame 1: the hook overlay is the **heaviest element** (largest, highest contrast, calm area of the shot); ≤7 words, ≤3 lines ([visual weight → UGC](../frameworks/visual-weight-hierarchy.md#carry-the-hierarchy-into-ugc-video-derived)) (derived from [R1 0:14:42; 0:36:37]).
- One overlay line per beat; never two emotional claims in one frame.
- Weight the payoff words ("backwards weight") [R1 0:39:40].
- Text must match the creator's expression in that shot (derived from [R2 0:06:23]).
- Periods, not exclamation marks, for deadpan; an ellipsis to pull the viewer on [J 0:19:44–0:20:49; R2 0:51:32] ([font psychology](../concepts/font-psychology.md)).
- Proof overlays (stars, counts) are small "supporting characters", never the hook [R3 0:17:51–0:18:56], and only with true numbers.

### Step 5: B-roll and visual cues per beat
| Beat | Visual moves | Page |
|---|---|---|
| Hook | One salient focal object or an odd first frame (pattern break); close-up = more intensity, wide = calmer; the face shows the hook's emotion; **don't open on skin with no context** (women's products, US) [R3 0:20:31–0:21:08] | [salience](../concepts/heuristics/salience-bias.md), [pattern disruption](../concepts/heuristics/pattern-disruption.md), [model image psychology](../concepts/model-image-psychology.md) |
| Problem | Props and setting that prime the right life stage (newborn props, not a basketball) [R2 0:25:31–0:27:32]; the real mess (cluttered counter, the "product graveyard") [May14 0:17:40] | [hero-image ↔ copy congruence](../concepts/hero-image-copy-congruence.md) |
| Mechanism | Ingredients/materials beside the product so people "smell it through the screen"; texture, pour, fabric moving on a body [R1 0:06:19–0:07:22; R2 0:09:29] | [sight smell](../concepts/sight-smell.md) |
| Proof | One continuous demo shot; time sequence (week 1/2/3; 10/20/40 min) for durability or speed claims [Jul16 0:26:13; 0:28:18] | [Fogg](../frameworks/fogg-behavior-model.md), [skeptic format](../frameworks/skeptic-format.md) |
| CTA | Product in hand; saturated product colour [R3 0:48:30–0:50:35] | [colour psychology](../concepts/color-psychology.md) |
| All | Grade, light and framing match the target zone: Z1 morning light, soft, wide; Z2 saturated, close-up, energy; Z3 muted, "the tension before the solution"; Z4 harsh light, high contrast | [tone shifting](../frameworks/tone-shifting.md) |

### Step 6: Proof without fabrication
Every proof element gets a line in the **proof ledger** with its `truth_ref`.

| Allowed (if true) | Never |
|---|---|
| On-camera demo of a real claim | Faked or edited test results |
| Real customer quote, labelled as a quote, close to the original wording | Invented testimonials, composite "customers", "real user quote" on a line no customer wrote |
| Exact, typed numbers ("1,200+ reviews from dairy lovers") | Rounded-up or invented counts, untyped "thousands of women" |
| Real press/expert relationship | Press logos or "dermatologist-approved" you can't document |
| Real limited drop, real deadline, real occasion ("the Fourth of July sale") [R3 0:46:24] | "Only 9 left" that isn't true [R3 0:15:00; Jul9 0:43:49] |
| The creator's own honest experience, including doubt | "Overnight" transformations; Sarah's uncited stats in copy ([contradictions](../contradictions.md)) |
| A guarantee or $0 trial you actually offer ([risk-reduction hooks](../concepts/risk-reduction-hooks.md)) | |

### Step 7: CTA language
- Spoken + end card: definitive ("See how it works", "Get yours", "Order yours now") — never "Shop now", "Learn more" [R1 0:27:05–0:28:09; R2 0:47:34–0:49:14] ([active CTA language](../concepts/active-cta-language.md)).
- Tie it to a person's approval or a habit: "Want your vet to be pleasantly surprised at your dog's next checkup?" [May14 0:42:30].
- Purchase stage: the real offer, with a reason ("drop" language, occasion) ([offer psychology](../frameworks/offer-and-bundle-psychology.md)).
- The CTA promise must match the landing page ([landing-page scorecard](../rubrics/landing-page-scorecard.md)).

### Step 8: Build the test variants (pipeline design on course rules)
- **3 hooks × 2 bodies = 6 cuts.** Hooks: same body, different first 3 s (each a different message or lever). Bodies: same hook, one change only — the framework, the proof order, or the narrator.
- Everything else constant: creator, offer, CTA, landing page, length.
- Name: `<STAGE>_<EMOTION>_<angle>_ugc_h<1-3>b<1-2>_v1` (pattern from [TEEP](../frameworks/teep-journey.md#output-templates)).
- If it fails later, the fix order is speed → hook → story → creator [May14 0:44:50–0:45:41] ([test and iterate](test-and-iterate.md)).

### Step 9: Generate with an LLM (optional)
Assembled prompt (derived from Sarah's recipe [May14 0:17:42; 0:36:30; 0:51:31]; see [story frameworks](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim)):
```text
We sell <product + one-line what it does>.
Concept: <core_message from the angle brief>.
Avatar: <buyer + situation, from real research; quote 2 customer phrases>.
Write me a <length>-second UGC script using the <Framework> story framework.
Our main character is <narrator>. The final CTA: <definitive CTA>.
For context: <Framework> — FRAMEWORK: <paste the steps, nothing else>. Follow only this framework.
Target emotion: <specific sub-emotion>, Zone <n> (<valence>, <intensity>), speaking to the <self> self.
Spend about two-thirds of the script on setup before the product appears. Include scene directions,
on-screen text (max 7 words per overlay) and b-roll notes per scene. Keep it realistic: skepticism,
nuance, no "overnight" claims. Use ONLY these facts and proof: <claims_allowed + real_quotes>.
Do not invent reviews, stats, endorsements, scarcity or results.
```
Then give 3 alternative hooks; then "pull out the deepest emotion and the core message… then give us headlines" for the static version [May14 0:25:06].

## Output: UGC script
```markdown
### UGC script: <SCR-ANG-nn-v1> · <product> · <angle name>
- From angle: ANG-<nn> · Mechanism kept: "<…>" · Source cards: TD-<…>
- Target: <buyer + situation> · Self: <A/I/O> · Zone: <Z> · Emotion: <sub-emotion> · TEEP: <stage>
- Framework: <name> (steps pasted: yes) · Narrator: <…> · Length: <15/30/45/60 s> · Heuristics: <slug, slug>
- Core message (frame 1): "<…>"

#### Hooks (test 3)
| # | Spoken (creator's words) | On-screen text (≤7 words) | First visual | Lever / message tested |
|---|---|---|---|---|
| H1 | "…" | "…" | … | … |
| H2 | | | | |
| H3 | | | | |

#### Body A (control)
| Beat | Time | Framework step | Spoken (say it your way) | On-screen text | Visual / b-roll / props | Delivery (energy, pace, expression) |
|---|---|---|---|---|---|---|
| Problem | 3–12 s | … | … | … | … | … |
| Lived experience + realism | … | | | | | |
| Turn: product + mechanism | … | | | | | |
| Proof | … | | | | | |
| CTA | … | | | | | |

#### Body B (one change vs A: <framework | proof order | narrator>)
<same table>

#### Proof ledger
| Line / visual | Proof type | truth_ref | Verified by |
|---|---|---|---|

- Setup share: <0.xx> · Cut pace target: 2–4 s · Message in frame 1: yes
- CTA: "<…>" · Landing page: <url> · Page repeats the promise/claims: yes/no
- Variants & names: <STAGE>_<EMOTION>_<angle>_ugc_h1b1_v1 … h3b2 (6 cuts)
- Lengths: <master> → 30 s → 15 s
- Checklist: [UGC script checklist](../rubrics/ugc-script-checklist.md) passed ☐ · Scorecard ≥ 80 ☐
```

## Quality gates
- [ ] [UGC script checklist](../rubrics/ugc-script-checklist.md) passes; [ad scorecard](../rubrics/ad-scorecard.md) ≥ 80 with no auto-fail.
- [ ] Every claim and proof line has a `truth_ref`.
- [ ] No line matches the source competitor ad (fidelity F1–F3 from [angle remix](angle-remix.md#step-4-fidelity-check-anti-copy-pipeline-design)).
- [ ] 3 hooks test 3 different things; Body B differs from Body A in exactly one way.

## Related
[Playbooks hub](README.md) · [Angle remix](angle-remix.md) · [Creator brief](creator-brief.md) · [Static ad creation](static-ad-creation.md) · [Test and iterate](test-and-iterate.md) · [Micro-story](../concepts/heuristics/micro-story.md) · [Open loop](../concepts/heuristics/open-loop.md) · [Humor in ads](../concepts/humor-in-ads.md) · [Fluency mechanism](../concepts/fluency-mechanism.md) · [ElevenLabs](../tools/elevenlabs.md) · [ChatGPT](../tools/chatgpt.md)
