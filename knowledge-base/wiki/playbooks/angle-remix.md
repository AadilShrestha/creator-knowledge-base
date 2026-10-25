---
title: "Playbook: Angle Remix (teardown cards → our own angle briefs)"
type: playbook
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/frameworks/rewriting-ads-for-new-selves.md
  - knowledge-base/wiki/frameworks/tone-shifting.md
  - knowledge-base/wiki/frameworks/story-frameworks-for-ads.md
  - knowledge-base/wiki/frameworks/mindstate-emotion-mapping.md
  - knowledge-base/wiki/courses/tether-lab/07-prompt-library/README.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md
tags: [playbook, angles, remix, make-it-our-own, self-shift, zone-shift, heuristic-stack, story-framework, fidelity-check, claim-check, scoring, angle-brief]
updated: 2026-10-20
---

# Playbook: Angle Remix
> "Take what's working and make it our own." Keep the competitor's **mechanism**, then deliberately change the **self, zone, heuristic stack, emotion, story framework, messenger, format and TEEP stage** to generate N variants for *our* product. Every variant passes a **fidelity check** (not a copy), a **fit check** (true for our product) and a **score**. Output: an `angle_brief` list for [UGC scripts](ugc-script-writing.md) and [statics](static-ad-creation.md).

## 🤖 Agent use
- **Use when:** you have 1+ teardown cards (and ideally an opportunity list or research brief) and need new angles for our product.
- **Inputs → outputs:** [teardown cards](competitor-ad-teardown.md) + [opportunity list](competitor-landscape-audit.md) (optional) + [research brief](customer-research-to-angles.md) (recommended) + **product truth sheet** ([template](README.md#hand-off-artifacts)) + N (default 8) → `angle_brief` list, scored and ranked, top 3–5 marked `ship_to_script`.
- **Rules:**
  - DO start from a proven mechanism, never a blank page [M4 L7 00:18].
  - DO create variants by moving a winner to a *different* self or zone ([rewriting for new selves](../frameworks/rewriting-ads-for-new-selves.md), [tone shifting](../frameworks/tone-shifting.md)); "net new" at volume is a myth [Chase 0:21:38].
  - DO use the selves and zones the niche **doesn't** use ([landscape audit](competitor-landscape-audit.md)); go opposite on message, colour, size, tone [Jun11 0:42:22–0:44:31].
  - DON'T copy their scripts first; build from the core message that won (yours or theirs, abstracted) [Jun11 0:32:53–0:33:57].
  - DO use only our verified claims and proof. DON'T ship LLM-invented proof (ChatGPT wrote "Featured in Outside and Men's Health" in the L7 demo) [M4 L7].
  - DO keep one core emotion per angle ([one core emotion](../concepts/one-core-emotion-per-ad.md)); blend only emotions that each won alone ([contradictions](../contradictions.md) row 5).
  - DO make Ought angles resolve pressure into relief [M4 L4 05:36], and keep Ought mostly for retargeting/qualified traffic ([contradictions](../contradictions.md) row 17).
- **See also:** [Prompt library](../courses/tether-lab/07-prompt-library/README.md) · [Prompts library](../libraries/prompts.md) · [Angles library](../libraries/angles.md) · [Hooks library](../libraries/hooks.md) · [Rewrites library](../libraries/rewrites.md) · [Ad scorecard](../rubrics/ad-scorecard.md) · Other creator: [Evolve: ad idea to brief](../courses/evolve/copywriting/playbooks/ad-idea-to-brief.md)

**Source key:** M4 L7 = [Rewrite winning ads for new selves](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md) · M4 L4 = [The 3 selves](../courses/tether-lab/04-self-targeting-system/04-the-3-selves-that-drive-every-buying-decision.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jul9 = [Live Jul 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · Jul16 = [Live Jul 16](../courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) · Chase = [Chase Mohseni](../courses/tether-lab/05-live-recordings/2025-06-guest-session-02-chase-mohseni.md) · PL = [Prompt library](../courses/tether-lab/07-prompt-library/README.md). **(pipeline design)** = our process.

## Procedure

### Step 1: Pick source mechanisms
- Take cards with `winner_signals.confidence` = high/medium. A `low` card may be used only together with customer evidence from the research brief (pipeline design).
- Copy each card's `transferable_mechanism.statement`, `keep` and `fit_preconditions`. Check the preconditions against the product truth sheet now; drop mechanisms that would require a claim we can't make.

### Step 2: Write the remix grid (pipeline design)
Each variant changes **at least 2 axes** from the source and keeps the mechanism. Pick values from these tables:

| Axis | Options | How to move it | Page |
|---|---|---|---|
| Self | Actual / Ideal / Ought | Shift table: promise, verb ("already / become / should"), identity callout, proof type | [rewriting for new selves](../frameworks/rewriting-ads-for-new-selves.md#shift-table-what-changes-when-you-move-to-each-self) |
| Zone | Z1–Z4 | Lever 1 verbs → lever 2 visuals → lever 3 emotional promise | [tone shifting](../frameworks/tone-shifting.md#the-three-levers) |
| Heuristic stack | 2–3 levers, fluency as base | Pick a lever pair; run the matching prompt | [heuristics hub](../concepts/heuristics.md), [prompt library decision table](../courses/tether-lab/07-prompt-library/README.md) |
| Emotion | 9 mindstates → 3 nuances each | esteem → confidence / control / appeal | [mindstate mapping](../frameworks/mindstate-emotion-mapping.md) |
| Story framework | Pixar, Story Spine, SCQA, In Medias Res, Freytag, Hero's Journey, Founder's Post… | Loadout quick picker | [story frameworks](../frameworks/story-frameworks-for-ads.md#quick-picker-decision-table) |
| Messenger | customer, skeptic, founder, employee, expert, character around the customer (vet, trainer, the pet) | Each narrator is an avatar test [May14 0:33:17; 0:40:09] | [messenger effect](../concepts/heuristics/messenger-effect.md), [validation over authority](../concepts/validation-over-authority.md) |
| Format | static, GIF/carousel, UGC talking head, skeptic test, fake podcast, founder, skit, advertorial | Static first; climb only after a static wins | [creative testing](../frameworks/creative-testing-system.md), [skeptic format](../frameworks/skeptic-format.md), [native advertising](../concepts/native-advertising.md) |
| TEEP stage | T / E1 / E2 / P | Stage jobs and UGC skeletons | [TEEP](../frameworks/teep-journey.md#ugc-script-skeletons-per-stage-derived) |

**Default generation recipe (N = 8):**
1. 3 self-shift variants (Actual / Ideal / Ought) of the source mechanism, offer held constant [M4 L7].
2. 2 zone-shift variants into zones the landscape audit marked empty.
3. 1 heuristic-pair variant from the Prompt Library (paste the prompt verbatim, add our brand block at the bottom [PL 01:01–01:58]).
4. 1 framework/messenger variant (e.g. their testimonial → our In Medias Res fake podcast, or a vet-narrated Freytag) [story frameworks, competitor teardown use].
5. 1 "opposite" variant: flip message scale, palette and tone vs the category [Jun11 0:43:27].

For each, write the **core message** in one sentence and **3 hook seeds** (spoken line + on-screen text). Pull hook *patterns* from [hooks library](../libraries/hooks.md); pull real customer phrases from the research brief.

### Step 3: Make the emotion specific
Replace every umbrella emotion with a sub-emotion and a situation ("boardroom-level confidence"; "defeated by failed solutions" → "every bowl we gave him, he destroyed") [Jun4 0:38:43; R3 0:33:42]. If the source winner's headline won but didn't scale, split it into desire *types* and make one variant per type [R3 0:43:07–0:46:24].

### Step 4: Fidelity check (anti-copy) (pipeline design)
Every variant must pass all of these:

| # | Check | Fail if… |
|---|---|---|
| F1 | Wording | Any 5+ consecutive words match the competitor's transcript, headline or primary text (ignore generic phrases like "link in bio") |
| F2 | Signature lines | It reuses their catchphrase, slogan, named character, mascot or series name ("go off, Gordy"-type lines) |
| F3 | Marks | It contains their brand, product names, logos, packaging, or a parody of them |
| F4 | Visual signature | It recreates their distinctive frame (same set, wardrobe, colour block, layout, shot order) closely enough that a viewer could mistake it for theirs |
| F5 | Claims | It repeats any item from `their_claims` or a number/stat/award of theirs |
| F6 | Footage | It needs any of their footage, images, audio or music |
| F7 | Distance | It changes fewer than 2 axes from the source (Step 2) |

Fix and re-check; after two failed fixes, drop the variant.

### Step 5: Fit check (truth) (pipeline design, grounded in course rules)
For every claim, proof element and badge in the variant, map it to the product truth sheet:

| Element | Allowed only if | Course rule |
|---|---|---|
| Benefit / result claim | Listed in `claims_allowed` with evidence | "Do not invent reviews, stats or endorsements" ([story prompt template](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim)) |
| Review / testimonial line | It is a real customer quote, in `real_quotes`; label it as a real quote | Never put a "real user quote" label on a line no customer wrote ([research stack](../frameworks/customer-research-stack.md)) |
| Number (reviews, sold, customers) | Exact true number, ideally **typed** ("350,000 tea drinkers") | [Jul16 0:39:20] via [Fogg](../frameworks/fogg-behavior-model.md) |
| Scarcity / urgency | Real stock limit, real drop, real deadline or real occasion | Fake scarcity backfires [Jul9 0:43:49]; [contradictions](../contradictions.md) row 10 |
| Authority | Real expert/press relationship; the right *type* of authority for this audience | [validation over authority](../concepts/validation-over-authority.md) |
| Demo | The product actually survives the test on camera | [skeptic format](../frameworks/skeptic-format.md) |
| Self/zone fit | Ought variants resolve into relief; Z3/Z4 target situations or industry beliefs, not self-worth | [M4 L4 05:36]; [Jun11 0:20:12–0:21:13] |

Also name the **biggest ability crusher** the angle must answer ([Fogg](../frameworks/fogg-behavior-model.md)) and check the landing page can carry the promise ([landing-page scorecard](../rubrics/landing-page-scorecard.md)).

### Step 6: Score (pipeline design)
| Criterion | Weight | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| Customer evidence | 3 | none | 1 anecdote | several quotes | repeated, emotionally intense (Reddit-level) |
| White space / distinctiveness | 3 | the category's default | common | rare | nobody does it |
| Truth & proof strength | 3 | needs unverified claims | weak proof | real proof | demonstrable on camera |
| Emotional specificity | 2 | umbrella emotion | named | sub-emotion | sub-emotion + situation |
| Mechanism fidelity (keeps what made source work) | 2 | lost | partial | mostly | fully |
| Test cost / readiness | 1 | pro shoot | UGC shoot | static | headline swap |
| Ethics risk (inverse) | 1 | shames the viewer | risky | handled | none |

Score = Σ(weight × points) / 45 × 100. Ship ≥70 to scripting; 55–69 revise once; <55 drop. Any F-check or truth failure = not eligible regardless of score.

### Step 7: Assign the test slot
Group the top 3–5 by **one learning goal** (self, zone, emotion, stage or heuristic). Don't mix goals in one test [Jun11 0:48:40–0:49:43] → hand to [test and iterate](test-and-iterate.md).

## Output: angle brief list
```yaml
angle_briefs:
  - id: ANG-<nn>
    source_cards: [TD-<…>]
    opportunity: OPP-<nn> | none
    mechanism_kept: "<placeholder statement>"
    axes_changed: {self: "ideal→actual", zone: "Z1→Z3", framework: "testimonial→In Medias Res", messenger: "", format: "", teep: "", heuristics: ""}
    core_message: "<one sentence>"
    target:
      buyer: "<who, in which situation (from research)>"
      self: actual | ideal | ought
      zone: Z1 | Z2 | Z3 | Z4
      mindstate: "<…>"
      specific_emotion: "<sub-emotion + situation>"
      teep_stage: T | E1 | E2 | P
    heuristic_stack: [<slug>, <slug>]   # 2-3, fluency as base
    story_framework: "<…>"
    messenger: "<…>"
    format_first: static | ugc | both
    hook_seeds:
      - spoken: "<…>"
        on_screen: "<≤7 words>"
    proof_plan:
      - element: "<review quote | demo | number | authority>"
        truth_ref: "<product truth sheet id>"
    ability_crusher: "<…> → answered by <…>"
    landing_page_fit: ok | needs_change: "<…>"
    checks: {fidelity: pass, truth: pass, ethics: pass}
    score: <0-100>
    learning_goal: self | zone | emotion | stage | heuristic | format
    status: ship_to_script | revise | drop
```

## Worked mini-example (course material, abstracted)
Source mechanism (from Milky, [R3 0:55:52–1:00:02](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md); case [Milky](../brands/milky.md)): *"Identity confrontation: 'You're <condition/goal>. Start acting like it.' beside the trigger object, Zone 3–4, Ought."* Darian remixed the structure live for low-carb pasta: "You're on a diet. Start acting like it." [1:00:00]. That's a **category transfer** keeping the mechanism. Our remix would go further than Darian's: change ≥2 axes, e.g. Actual-self, Zone 3 with empathy first ("I know you don't want to be <X>, but you are, honey" is Sarah's own next-test softener [0:59:01]) → rewritten in our words, plus a skeptic-UGC format and a real-review proof element. Check F1: our line must not reuse "Start acting like it" verbatim if it becomes the competitor's signature line in our niche.

## Quality gates
- [ ] N variants written; each changes ≥2 axes and keeps the mechanism.
- [ ] All pass F1–F7 and the truth table; every proof element has a `truth_ref`.
- [ ] Every emotion is a sub-emotion + situation.
- [ ] Top 3–5 share one learning goal.
- [ ] No Ought or Z3/Z4 angle shames the viewer; each ends in relief or hope.

## Related
[Playbooks hub](README.md) · [Competitor ad teardown](competitor-ad-teardown.md) · [Landscape audit](competitor-landscape-audit.md) · [Customer research → angles](customer-research-to-angles.md) · [UGC script writing](ugc-script-writing.md) · [Static ad creation](static-ad-creation.md) · [Iteration vs variation](../concepts/iteration-vs-variation.md) · [Angle rut](../concepts/angle-rut.md) · [Mirror effect](../concepts/mirror-effect.md) · [Risk-reduction hooks](../concepts/risk-reduction-hooks.md) · [Switching behavior](../concepts/switching-behavior.md)
