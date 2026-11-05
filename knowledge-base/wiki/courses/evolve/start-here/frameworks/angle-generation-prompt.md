---
title: "Angle generation prompt (sub-avatar → desire + behavior + gap → ranked angles and direct hooks)"
type: framework
creator: evolve
course: start-here
instructor: "Spencer Pawliw (addressed by name in lesson 79; named in lessons 76 and 79)"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/007-evolve-master-prompt-doc.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/076-how-to-build-sub-avatars.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/078-understanding-ad-definitions.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/079-how-to-come-up-with-ad-angles.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/080-action-item-come-up-with-new-ad-angles.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/082-the-3-testing-methods-part-2.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/083-putting-all-the-planning-together-examples.md
tags: [framework, angles, hooks, headlines, sub-avatars, ai-prompt, claude, concept-vs-angle, direct-hooks, testing-priority]
updated: 2026-11-02
---

# Angle generation prompt
> An angle is the customer's reason to buy. Get it from a sub-avatar (desire → current behavior → the gap the behavior leaves), by hand first, then with the Evolve angle prompt in Claude, which returns 3 ranked angles per sub-avatar, each with a "reason to buy" and 3 direct hooks modelled on winning-ad structures; test Angle 1 / Hook 1 first.

## 🤖 Agent use
- **Use when:** sub-avatars exist and you need angles and hook drafts; checking whether a proposed test is a concept or an angle; ranking what to test first; rescuing a format test ("post-it ads", "us vs them") that has no angle.
- **Inputs → outputs:** product facts (what it does, features, benefits, proven claims only) + 1+ sub-avatar (minimum: desire + behavior; better: + experience, emotion, customer quotes) → per sub-avatar: 3 angles × (reason to buy + 3 hooks + "Inspired by" structure), a priority note and a testing priority; then one concept card per test ([concept planning](concept-planning-and-growth-guide.md)).
- **Rules:**
  - **DO** write the angle for every concept, even a format or iteration test: "Every ad needs an angle, period." [L78 05:44](../lessons/078-understanding-ad-definitions.md)
  - **DO** apply one test: "If the concept doesn't give the customer a reason to buy, it's not an angle yet." [L79 09:14](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DON'T** call Us vs Them, Before & After, Problem-Aware ads or Post-it notes an angle; "the what is the angle". [L79 02:00–05:27](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DO** derive angles product → desires → core avatar → sub-avatars → angle, not product → benefit → angle. [L79 16:21–19:37](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DO** keep hooks direct (the hook states the angle) until advanced. [L79 20:19–22:14](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DON'T** trust the output blindly: "sometimes it can give you bad stuff as well." [L79 26:41](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DO** test the #1 hook of the #1 angle first; "you do not have to test each angle separately", and supporting benefits can go in body copy. [L79 28:32; 32:51](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **DO** copy the structure of the "Inspired by" ad, never its words, product claims or brand. (derived; the reference ads belong to other brands)
  - **DON'T** ship a numeric hook ("Blocks 100% of light", "0% blue light") unless the product facts prove it; bracket it as [verify] otherwise. (derived; repo rule "never invent proof")
  - **IF** a format concept isn't working **THEN** check the angle inside it before blaming the format. [L79 04:29–06:57](../lessons/079-how-to-come-up-with-ad-angles.md)
  - **IF** the output reads generic **THEN** add behavior and experience detail to the sub-avatar: "an AI would likely never write this headline for you unless you actually gave it the context". [L79 30:03](../lessons/079-how-to-come-up-with-ad-angles.md)
- **See also:** [ad definitions](../concepts/ad-definitions.md) · [core and sub-avatars](../concepts/core-and-sub-avatars.md) · [marksman/sniper testing](../concepts/marksman-sniper-testing.md) · [concept planning + Growth Guide](concept-planning-and-growth-guide.md) · Copywriting: [avatars and angles](../../copywriting/concepts/avatars-and-angles.md), [hooks](../../copywriting/concepts/hooks.md), [prompt index P10](../../copywriting/libraries/prompts.md) · Tether: [angle remix](../../../../playbooks/angle-remix.md)

## Definition
| Term | Meaning | Question | Source |
|---|---|---|---|
| Concept | "The big idea. It's what you're testing" (format, iteration, awareness level, or an angle); about us | What are we testing? | [L79 00:31; 06:57](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Angle | "How you choose to sell the product and it must always be defined"; the main reason to buy; about the customer | How do we sell it? | [L79 00:31](../lessons/079-how-to-come-up-with-ad-angles.md); [L78 05:44](../lessons/078-understanding-ad-definitions.md) |
| Hook / headline | "How we're communicating the angle" | How do we get attention? | [L79 20:19](../lessons/079-how-to-come-up-with-ad-angles.md) |
Full vocabulary (3:2:2, batch, variation, format): [ad definitions](../concepts/ad-definitions.md).

## Why it matters
- "Every headline that you write targets an avatar." "Fix your acne" targets everyone, so it is not relatable. [L79 18:15–18:49](../lessons/079-how-to-come-up-with-ad-angles.md)
- Formats only get attention: "if the angle sucks, no one's going to care." [L79 04:29–05:27](../lessons/079-how-to-come-up-with-ad-angles.md)
- "As long as your angles are actionable, writing will become much easier." [L79 23:40](../lessons/079-how-to-come-up-with-ad-angles.md)

## How to use it (steps)

### A. Concept or angle? (gate on every test idea)
| Statement | Verdict | Fix | Source |
|---|---|---|---|
| "Test a video version" | Concept | Name the angle | [L79 09:14–11:09](../lessons/079-how-to-come-up-with-ad-angles.md) |
| "Do an iteration" | Concept | "Iteration of what angle?" | same |
| "Us vs Them" | Concept | Comparing what? | same |
| "Stops tossing and turning" | Angle | — | same |
| "Brings back your energy" | Angle | — | same |
| "Meme static ads" | Concept (format) | "about what?" | [L83 24:48](../lessons/083-putting-all-the-planning-together-examples.md) |
If the concept is "test the X angle", still write the angle a second time for tracking. [L78 07:21–08:12](../lessons/078-understanding-ad-definitions.md)

### B. Manual extraction (do 2-3 by hand first)
1. Copy the sub-avatar's **desire** (what they want).
2. Copy its **behavior** (what they do now to get it).
3. Name the **gap** (why that still falls short).
4. Write the angle as a reason to buy that fills the gap: "better than [behavior]", "[behavior] + our product", "completes your [behavior] setup".
5. Write a second angle that uses the behavior positively.
Worked: sub-avatar "Nose Strip Sleeper" (wants restorative sleep; wears nose strips) → "Better than nose strips"; alt "this combined with nose strips will give you the best sleep of your life". [L79 24:25–25:50](../lessons/079-how-to-come-up-with-ad-angles.md)

### C. Run the prompt
1. Upload the angle prompt doc ("Evolve Enhanced - Angle Identifier", [L7](../lessons/007-evolve-master-prompt-doc.md)) to Claude ("I like Claude for writing"; ChatGPT works). [L79 26:41](../lessons/079-how-to-come-up-with-ad-angles.md)
2. Send product information + sub-avatar profile(s) (input template below). Desire + behavior is enough. [L79 27:36](../lessons/079-how-to-come-up-with-ad-angles.md)
3. Read the ranked output; rewrite weak hooks by hand; check every claim against product facts.
4. Pick Angle 1 / Hook 1; use the other hooks as the remaining creatives or headlines of a 3:2:2. [L79 32:51](../lessons/079-how-to-come-up-with-ad-angles.md)
5. Ask Claude to expand a strong "reason to buy" into a script if needed ("almost a script"). [L79 28:32–29:06](../lessons/079-how-to-come-up-with-ad-angles.md)
6. Log batch #, concept, angle, variations, format in the Growth Guide. [L78](../lessons/078-understanding-ad-definitions.md)

### D. After results
- One angle took the spend → Sniper on it, and reverse-engineer the avatar behind it (surface desire → behavior/product experience → "why" to core desire → hypothesis → verify in research). [L82 02:53–11:58](../lessons/082-the-3-testing-methods-part-2.md)
- No angle spent → check execution before killing the angle ([execution checklist](../rubrics/execution-checklist.md)); then pivot to Angle 2 / Hook 3. [L79 32:51](../lessons/079-how-to-come-up-with-ad-angles.md)

## The prompt (verbatim core)
Situation / Task / Objective, verbatim from the doc ([L79](../lessons/079-how-to-come-up-with-ad-angles.md); same prompt as Evolve Copywriting P10):
```text
**Situation**
You are a direct response marketing strategist specializing in customer avatar analysis and angle development. You work with businesses to identify the most compelling marketing angles based on deep customer psychology, using sub-avatar frameworks to uncover specific pain points, desires, and emotional triggers that drive purchasing decisions.

**Task**
The assistant should analyze the provided product information and sub-avatar profiles to generate targeted marketing angles. For each sub-avatar, identify 3 potential marketing angles by examining their most painful or specific attributes, framing these as problems from their perspective, and converting them into compelling "reason to buy" statements that are relatable. Then provide 3 strategic written hooks/headlines that could be used for each angle for proper implementation. You MUST but the strongest angles and the strongest hooks/headlines up at the top first and make sure to remind the user that they do NOT have to test each angle separately. They can do a concept that tests "multiple angles" with the best hook/headline.

**Objective**
Enable the user to develop data-driven, psychologically-targeted marketing angles that resonate with specific customer segments, allowing them to either test multiple approaches simultaneously or focus resources on the highest-probability angle with multiple execution variations.
```
The doc continues with Knowledge (the concept/angle teaching), Additional Context (16 winning ads: angle → hook, each with a "why this ad works" card) and an Example Of Perfect Output. Full winning-ad list and example output: [L79 Prompts / templates](../lessons/079-how-to-come-up-with-ad-angles.md).

### Agent-safe addendum (derived; append when running it)
```text
Constraints: Use only the product facts provided. Any number, percentage, timeline or comparison not in the facts must appear in [brackets] as "verify". Copy only the structure of the reference ads ("Inspired by"), never their wording, product, brand or claims. Quote customer language only from the sub-avatar evidence provided.
```

### Input template
```text
Product information: <what it does; features; benefits; proven claims with source; offer>
Sub-avatar profile(s):
  Sub-avatar #N: <label in customer lingo>
  Desire: <surface "I want..."> | Behavior: <what they do now> | Experience / Product experience: <...>
  Emotion: <...> | Demographic (only if needed): <...> | Verbatim quotes: <quote — source>
```
Claude's on-screen request: product information plus sub-avatar profiles with core desires, pain points, behaviors, emotional triggers and other Core 5 attributes. [L79 27:20](../lessons/079-how-to-come-up-with-ad-angles.md)

### Output schema
```text
PRIORITY NOTE: (you do NOT have to test each angle separately; which hook first)
SUB-AVATAR #N: <label> ⭐ <rank>
  Angle 1: <name>
    Reason to Buy: <1-2 sentences, customer perspective>
    Hooks: 1) "..." (Inspired by: <ref> - <structure>) 2) ... 3) ...
  Angle 2 / Angle 3: (same)
TESTING PRIORITY: Start with <sub-avatar, angle, hook>. If it hits, run variations; if not, move to <next>.
```
The doc's example output shows one hook per angle; the Task asks for three and the live run produced three. Use three. [L79 limitations note](../lessons/079-how-to-come-up-with-ad-angles.md)

## Hook structures the prompt borrows (structure only)
| Structure | Reference hook (other brands' ads) | Blinds remix in the course | Source |
|---|---|---|---|
| Timeline + outcome elimination | "14+ Hours. No Swelling" | "5 minutes to install. No more snapping." | [L79 20:19; doc](../lessons/079-how-to-come-up-with-ad-angles.md) |
| "This is X. This is Y" | "This is bread. This is breakfast" | "This blocks light. This saves relationships." | same |
| Product redefinition | "This is a meal. Not a protein shake" | "This is a curtain. This is a cooling system." | same |
| Minimal change | "Don't change your life, just change lunch" | "You have the fan. You have the AC. You need this." | same |
| Avatar call-out with identity match | "Moms of 15 year olds" | "Serious about fasting? Serious about darkness." | same |
| Dual timeline | "Drains double chin in 7 days" | "Cool room in 5 minutes. Deep sleep in 8 hours." | same |
| Parallel action | — | "You quit the screens. Now quit the light." | [L79 30:03](../lessons/079-how-to-come-up-with-ad-angles.md) |
Card cautions: "This is NOT [the product]" must connect ("If the dots don't get connected... the ad will flop"); educational fear hooks are "not malicious", no fear-mongering. [L79 cards](../lessons/079-how-to-come-up-with-ad-angles.md)

## Examples

### Angles
| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| Your discipline is being wasted | Restorative sleep; already avoids screens 1 h before bed | Timeline + outcome pairing | Static or video (not specified) | "No screens for 1 hour. No light for 8 hours." | [L79 28:32–31:58](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Complete your sleep protocol | Same sub-avatar; wants the "final environmental piece" | Parallel framing | — | "You control the screens. Control the light." | [L79 frame 33:20](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Better than nose strips | Restorative sleep despite nose-strip use | Desire + behavior + gap | — | (no hook shown) | [L79 24:25](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Stops you snapping at people | Short-fuse sleeper | Timeline + outcome elimination | — | "5 minutes to install. No more snapping." | [L79 doc](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Confidence / Control (dog walking) | Wants dog to stop pulling; embarrassed vs frustrated | "This is X. This is Y" (Nutella template) | Static two-panel | "This is a harness / This is confidence" | [L83 03:14–04:58](../lessons/083-putting-all-the-planning-together-examples.md) |
Claims inside these lines (melatonin, "100% of light") are course examples, not verified facts for any product.

### Angle spectrum (one core desire: better sleep)
Broad: "Want better sleep?" (weak: "broad avatars are usually harder to sell to") → sub-avatar: "Better than nose strips" → sub-avatar with behavior: "No screens for 1 hour. No light for 8 hours." [L79 14:32–15:27; 24:25; 29:06](../lessons/079-how-to-come-up-with-ad-angles.md)

### Rewrites
| Before | After | What changed | Source |
|---|---|---|---|
| "Want better sleep?" | "Better than nose strips" | Desire + behavior + gap of one sub-avatar (self) | [L79 14:32; 24:25](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Concept "Iteration" | Concept: iteration; angle: the reason to buy being iterated | Added the missing angle | [L79 09:14–10:14](../lessons/079-how-to-come-up-with-ad-angles.md) |

## Common mistakes
| Mistake | Fix | Source |
|---|---|---|
| Angle = format ("post-it ads") | Write what the post-it says as the reason to buy | [L79 03:46–04:29](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Stuck debating broad vs specific | Sub-avatar already sets the level; "your angle basically is the avatar" | [L79 12:48–14:32](../lessons/079-how-to-come-up-with-ad-angles.md); [L83 02:16](../lessons/083-putting-all-the-planning-together-examples.md) |
| Indirect, clever hooks from juniors | Direct hooks that state the angle | [L79 21:16](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Testing every angle in its own batch | One concept, 3 hooks, multiple angles if Marksman | [L79 28:32](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Hooks treated as finished ads | "Start thinking about how these can be turned into potential ads" | [L79 33:30](../lessons/079-how-to-come-up-with-ad-angles.md) |
| Desireless sub-avatar fed to the prompt | Every sub-avatar carries a desire | [L76 00:42](../lessons/076-how-to-build-sub-avatars.md) |

## Where it's taught
| Lesson | What | Timestamps |
|---|---|---|
| [7](../lessons/007-evolve-master-prompt-doc.md) | Prompt index ("Angles Prompt") | doc |
| [76](../lessons/076-how-to-build-sub-avatars.md) | Sub-avatar records feeding angles | 17:31–31:41 |
| [78](../lessons/078-understanding-ad-definitions.md) | Concept vs angle; record template | 01:28–12:57 |
| [79](../lessons/079-how-to-come-up-with-ad-angles.md) | Full method, prompt, live run | 00:31–34:26 |
| [80](../lessons/080-action-item-come-up-with-new-ad-angles.md) | Action item | page |
| [82](../lessons/082-the-3-testing-methods-part-2.md) | Reverse-engineer the avatar behind a winning angle | 02:53–11:58 |
| [83](../lessons/083-putting-all-the-planning-together-examples.md) | Angles on concept cards | 02:16–04:58; 24:48 |

## Cross-course notes
- **Evolve Copywriting:** the same prompt is P10 ([prompt index](../../copywriting/libraries/prompts.md); [L67](../../copywriting/lessons/67-how-to-write-image-ads-part-1.md)), with refinements P11 (punchier, sniper "dumb it down"). Persuasion chain (angle → mechanism → authority) in [mini breakthrough memo](../../copywriting/frameworks/mini-breakthrough-memo-and-growth-guide.md). Start Here adds the No Screener live run, the concept-or-angle game and the manual desire/behavior/gap method.
- **Tether Lab:** [angle remix](../../../../playbooks/angle-remix.md) remixes competitor angles; combine by running its teardown, then this page's gap test on our sub-avatars.

## Related
[ad definitions](../concepts/ad-definitions.md) · [core and sub-avatars](../concepts/core-and-sub-avatars.md) · [desire hunt](desire-hunt.md) · [concept planning + Growth Guide](concept-planning-and-growth-guide.md) · [marksman/sniper testing](../concepts/marksman-sniper-testing.md) · [research → first concepts](../playbooks/research-to-first-concepts.md)
