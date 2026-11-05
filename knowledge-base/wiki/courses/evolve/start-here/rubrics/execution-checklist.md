---
title: "Execution checklist (the 13 execution checks, strategy-vs-execution test, benchmarks, retest limits)"
type: rubric
creator: evolve
course: start-here
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/088-the-execution-problem.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/081-the-3-testing-methods-part-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/082-the-3-testing-methods-part-2.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/083-putting-all-the-planning-together-examples.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/128-how-to-do-learnings-questions.md
tags: [rubric, execution, execution-problem, script-qa, failed-ad-diagnosis, hook-rate, hold-rate, ctr, hemingway, strategy-vs-execution, retest-limits]
updated: 2026-11-02
---

# Execution checklist
> Spencer's 13 reasons a well-planned ad still fails, as a pass/fail rubric for any draft or losing ad, plus the three-format test that separates a bad angle (strategy) from bad words and visuals (execution), the soft-metric benchmarks, and the "three tries per angle" limit.

## 🤖 Agent use
- **Use when:** QA of any script, static or brief before launch; diagnosing an ad that lost although the avatar and angle were researched; deciding whether to retest an angle or move on.
- **Inputs → outputs:** the draft or losing ad (script, on-screen text, visuals), its avatar and angle, customer language from research, metrics if live (hook rate, hold rate, CTR, ROAS, CPA) → a 13-row scorecard (Pass / Fail + fix), a verdict "strategy vs execution", and the next test (re-execute, new format, Sniper batch, or move on).
- **Rules:**
  - **DO** assume execution before strategy when the angle came from research: "some marketers move on from angles... simply due to the fact that they just don't know how to actually execute them." [L88 03:34](../lessons/088-the-execution-problem.md)
  - **DO** run all 13 checks on every draft; write one fix per Fail. [L88 10:30-26:54](../lessons/088-the-execution-problem.md)
  - **DO** test one angle in three formats before judging it: all three fail → likely strategy; one gives direction → execution. [L88 27:24-28:21](../lessons/088-the-execution-problem.md)
  - **DO** validate your execution with proven structures (your account's winners, then industry winners) before testing new avatars/angles. [L88 28:21-29:15](../lessons/088-the-execution-problem.md)
  - **DON'T** live or die by soft benchmarks (hook ≥25%, hold ≥30% of hook, CTR ≥1%); "focus on what actually matters, which is ROAS and CPA". [L88 31:47-33:16](../lessons/088-the-execution-problem.md)
  - **IF** three honest executions of an angle fail **THEN** move to a different angle. [L88 33:16-34:04](../lessons/088-the-execution-problem.md)
  - **DO** also pass the Copywriting truth gates (no fabricated proof, no fake urgency, copy the mechanism not the asset) before shipping: [copy checklist scorecard](../../copywriting/rubrics/copy-checklist-scorecard.md).
- **See also:** [Learnings review](../frameworks/learnings-review.md) · [Rewrite losers and iterate](../frameworks/rewrite-losers-and-iterate.md) · [Ad account audit](ad-account-audit.md) · [Marksman/Sniper testing](../concepts/marksman-sniper-testing.md) · [Ad definitions](../concepts/ad-definitions.md) · Copywriting: [Copy checklist scorecard](../../copywriting/rubrics/copy-checklist-scorecard.md), [Three copy checks](../../copywriting/concepts/three-copy-checks.md) · Tether Lab: [UGC script checklist](../../../../rubrics/ugc-script-checklist.md), [Ad scorecard](../../../../rubrics/ad-scorecard.md)

## Definition
"The execution problem is basically when your angle is correct and you do understand your avatar. However, the way that you executed the ad, AKA the words you wrote and the content you used... was not good enough to actually convert the customer." [L88 05:11-06:02](../lessons/088-the-execution-problem.md) Execution is the variable on top of concept, angle, variation, format and testing method, and "this is the biggest variable" [L88 02:43](../lessons/088-the-execution-problem.md). Instructor evidence (claims): a template ad that failed scaled to $15,000/day a month later with different copy and images; a replicated socks template took a client from ~$200/day to $700/day [L88 07:23-09:07](../lessons/088-the-execution-problem.md).

## How to score
1. Score each check **Pass (1) / Fail (0) / N/A** (check 3 is video only). Write the evidence (the exact line or shot) for every Fail.
2. **Gate first:** any Copywriting truth gate failing (G1-G6 in the [copy checklist scorecard](../../copywriting/rubrics/copy-checklist-scorecard.md)) blocks shipping regardless of score.
3. **Threshold (derived; the course gives none):** ≤10 of applicable checks passed = rewrite before launch; 11-12 = fix the Fails, then ship; 13 = ship. For a live losing ad, the Fails are the iteration list.
4. Then run the strategy-vs-execution test (below) if the ad already lost.

## The 13 checks

| # | Check (doc wording, phrased as a pass) | Pass criterion | Fail signal | Fix | Cite |
|---|---|---|---|---|---|
| 1 | Copy has emotional impact | Reads like "an internal conversation your avatar would have in their own head"; specific, felt lines | Generic outcome ("lose weight") | Make it specific and felt ("lose the muffin top for good"; "14+ hours of no swelling") | [L88 10:30-13:21](../lessons/088-the-execution-problem.md) |
| 2 | Creates curiosity | A reason to stop and to click; an open loop | Nothing unanswered; viewer has no reason to watch or click | Open loop or curiosity word ("This is bread / This is breakfast"; "I accidentally lost…") | [L88 13:21-14:57](../lessons/088-the-execution-problem.md) |
| 3 | Creates suspense (video) | A promised reward that arrives at the end | Hook, then nothing to wait for; or the promised payoff never comes ("click baited") | Preview the payoff early and deliver it ("three red flags that your child has a vitamin deficiency" pattern) | [L88 14:57-17:18](../lessons/088-the-execution-problem.md) |
| 4 | Simple (grade 6 or lower) | Hemingway grade ≤6 | Jargon; post-graduate grade ("metabolic gummies") | AI rewrite to grade 5-6 ("gummies for your tummy" = grade 3); "Don't try to be smart" | [L88 17:18-18:41](../lessons/088-the-execution-problem.md) |
| 5 | No empty claims | Every claim has a reason to believe the customer cares about | "The best X", "better than Y", or a mechanism name nobody understands | Replace with real, checkable proof | [L88 18:41-19:38](../lessons/088-the-execution-problem.md) |
| 6 | No bossy claims | Gives a reason before asking for attention | "Stop scrolling and watch this", "watch these next five seconds" | "If you have [X], give me five seconds and I'll show you how to get rid of it" | [L88 19:38-20:36](../lessons/088-the-execution-problem.md) |
| 7 | No repetitive claims | The claim is said in a way competitors don't | Same claim, same words as the category (check the Ad Library) | New way to say it | [L88 20:36-21:28](../lessons/088-the-execution-problem.md) |
| 8 | Spoken, not written | Sounds natural read aloud / via AI voice | Page language; stiff AI voiceover | Voice-to-text, or AI "rewrite so it sounds spoken" (loose, casual, pauses) | [L88 21:28-22:25](../lessons/088-the-execution-problem.md) |
| 9 | Written for the customer | Customer's exact words and tone | Written in the marketer's taste ("I'm not the avatar") | Pull lines from research (reviews, Reddit) | [L88 22:25-23:23](../lessons/088-the-execution-problem.md) |
| 10 | Angle specific enough | Uses the avatar work; a specific person and situation | Template headline pasted with the avatar research ignored | Rewrite from sub-avatar lines ("Go to the gym late to avoid everyone") | [L88 06:02-06:42; 23:23-24:19](../lessons/088-the-execution-problem.md) |
| 11 | Angle not crowded (or out-communicated) | Either a less-used angle or clearly better communication than competitors | The whole market runs the same angle and your copy is not better | Out-communicate or change the angle | [L88 24:19-25:16](../lessons/088-the-execution-problem.md) |
| 12 | Editing style fits the demographic | Style matches what this demographic watches and what converts for them | Style you like (e.g. science-visual VSL for an audience whose converting ads are casual car-and-matcha creators) | Copy the demographic's native style; "it just matters what performs" | [L88 25:16-25:55](../lessons/088-the-execution-problem.md) |
| 13 | Format fits (and copy matches its difficulty) | Format chosen for the message; easy formats carry stronger copy | Static picked because it was easy; generic template + AI headline like "thousands" of others | Test another format; "the easier the format is, the better the messaging and copy has to be" | [L88 25:55-27:24](../lessons/088-the-execution-problem.md) |

## Strategy vs execution test (run after a loss)

| Result of one angle across 3 formats (e.g. product photo + headline; static graphic like us-vs-them; voiceover + B-roll) | Verdict | Next | Cite |
|---|---|---|---|
| All 3 fail | "Likely… strategy" (could still be execution for some) | New angle, or back to research | [L88 27:24-28:36](../lessons/088-the-execution-problem.md) |
| 2 fail, 1 gives direction / 1 fails, 2 give direction / 1 wins | Execution | Communicate it better: Sniper batch, other formats | [L88 27:24-28:36](../lessons/088-the-execution-problem.md) |
| Research-based angle lost | Suspect execution | Re-execute | [L82 16:13-17:12](../lessons/082-the-3-testing-methods-part-2.md) |
| Product-first angle lost | "People just don't care" | Go back to customer research | [L82 16:13-17:12](../lessons/082-the-3-testing-methods-part-2.md) |

## Soft benchmarks (signals, not verdicts)

| Metric | Benchmark | Note | Cite |
|---|---|---|---|
| Hook rate | ≥25% | "There are ads with 50% hook rates that suck and ads with 20% hook rates that crush" | [L88 31:47-33:16](../lessons/088-the-execution-problem.md) |
| Hold rate | ≥30% of hook rate (7.5%; "at least 8%" at a 25% hook) | Defined as ThruPlays ÷ impressions, not 3-second plays | [L88 31:47-32:17](../lessons/088-the-execution-problem.md) |
| CTR | ≥1% | — | [L88 32:17](../lessons/088-the-execution-problem.md) |
| Decision metrics | ROAS and CPA | Below benchmarks = "what you said or showed is likely not resonating" | [L88 32:17-33:16](../lessons/088-the-execution-problem.md) |

Other values in the course: Copywriting treats hook rate <30% as the hook failing and lists "low" as CTR <1%, hook <25%, hold <5% ([Iteration outcomes](../../copywriting/concepts/iteration-outcomes.md)). Column formulas: [KPIs and columns](../frameworks/kpis-and-columns.md). **Agent default:** use the L88 numbers as triage flags only and label the definition used.

## Retest limits

| Question | Rule | Cite |
|---|---|---|
| When to write off an angle | Marksman fail + confident → Sniper batch 2 → batch 3 only if a feedback loop confirms an execution flaw → then move on ("angle, not avatar") | [L88 33:16-34:04](../lessons/088-the-execution-problem.md) |
| How many avatars | One, maybe two, both under and above $100K/month | [L88 34:04-34:48](../lessons/088-the-execution-problem.md) |
| Concepts per winning angle | "As many as you want"; watch iteration overload | [L88 34:48-35:34](../lessons/088-the-execution-problem.md) |
| Vastly different avatar | Don't clone the script: "Would this script… actually make sense to this person?" | [L88 29:15](../lessons/088-the-execution-problem.md) |

## Scoring template
```text
Ad / draft: [ ]   Angle: [ ]   Avatar: [ ]   Format: [ ]   Status: [draft | live loser]
Truth gates (Copywriting G1-G6): [all pass | blocked by Gx]
 1 Emotional impact ........ P/F  evidence: [ ]  fix: [ ]
 2 Curiosity ............... P/F
 3 Suspense (video) ........ P/F/NA
 4 Grade ≤6 (Hemingway: _) . P/F
 5 No empty claims ......... P/F
 6 No bossy claims ......... P/F
 7 No repetitive claims .... P/F  (Ad Library checked: Y/N)
 8 Spoken ................... P/F
 9 Customer's words ........ P/F
10 Specific angle .......... P/F
11 Angle not crowded / out-communicated ... P/F
12 Style fits demographic .. P/F
13 Format fits ............. P/F
Score: _ / _ applicable → [rewrite | fix and ship | ship]
If live: hook _% hold _% CTR _% ROAS _ CPA _ → signals only
Strategy-vs-execution: formats tried [ ] → verdict [strategy | execution]
Tries on this angle: [1 | 2 | 3] → next: [re-execute | Sniper | new format | move on]
```

## Worked example (derived from the L122 humidifier loser)
Ad: "If you have a humidifier at home, let me show you something that actually blew my mind…" got ~$10 spend [L122 08:45-12:19](../lessons/122-how-to-do-learnings-part-1-losers.md). Team diagnosis mapped to checks (derived): **#1 Fail** (no germaphobe callout; the top performer named the felt moment "that feeling when you take a look inside"); **#2/#3 weak** ("hook's too long"; first clip held ~5 s vs 3 s on the winner, "Very slow"); **#10 Fail** (no sub-avatar label; team proposed "nursery room must have", "studio apartment must have"). Next: re-execute the same angle with a new hook (execution), not a new angle.

## Overlap with other checklists
| This rubric | Same idea elsewhere |
|---|---|
| #1, #9 | Copywriting checklist Q1 "Who am I writing this for?"; [Labels and customer language](../../copywriting/concepts/labels-and-customer-language.md); L128 Q5/Q7 (label, relatable) |
| #2, #3 | [Open loops](../../copywriting/concepts/open-loops.md); L128 Q1 (hook and keep hooked) |
| #4, #8 | Copywriting checklist Q11 (6th grade), Q13 (door-to-door); [Compression and plain language](../../copywriting/concepts/compression-and-plain-language.md) |
| #5, #7, #11 | [Three copy checks](../../copywriting/concepts/three-copy-checks.md) (falsifiable; nobody else can say it); Copywriting issue code #5 empty claims |
| #12, #13 | L128 Q4 (native to platform), Q8 (doesn't look like an ad); [every ad format](../lessons/089-every-ad-format-that-you-can-use.md) |
| whole list | L128's 14 questions in [Learnings review](../frameworks/learnings-review.md#procedure-d-the-14-questions-pre-launch-qa-and-post-test-diagnosis) |

## Where it's taught
- [L88](../lessons/088-the-execution-problem.md): definition [05:11-06:02], templates and evidence [06:02-09:42], the 13 checks [10:30-27:24], format test and proven structures [27:24-30:10], study method [30:10-31:47], benchmarks [31:47-33:16], FAQs and retest limits [33:16-35:34].
- [L81 07:40-08:37](../lessons/081-the-3-testing-methods-part-1.md): Sniper's three variations of one angle remove the "execution problem".
- [L82 16:13-17:12](../lessons/082-the-3-testing-methods-part-2.md): research-based loser = execution; product-first loser = "people just don't care".
- [L83 13:43-14:42; 28:57-31:58](../lessons/083-putting-all-the-planning-together-examples.md): "most people suck at execution"; handoff to L88.
- [L128](../lessons/128-how-to-do-learnings-questions.md): the 14 video-brief questions (complementary).

## Cross-course notes
- **Evolve Copywriting:** the [copy checklist scorecard](../../copywriting/rubrics/copy-checklist-scorecard.md) is a *different* 13-question list (L58, writing QA, scored 0-2/0-3 with blocking truth gates). Run that for scripts you write; run this one to diagnose why a planned angle lost. They agree on grade-6 language, spoken copy, customer words and specific claims.
- **Evolve Copywriting:** L88's "repetitive claims" and "angle said by everyone else" correspond to the "nobody else can say it" check in [Three copy checks](../../copywriting/concepts/three-copy-checks.md).
- **Tether Lab (shared):** the [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) and [ad scorecard](../../../../rubrics/ad-scorecard.md) score emotion, self-targeting and heuristics, which L88 covers only as "emotional impact". Use them together for UGC scripts.

## Related
[Learnings review](../frameworks/learnings-review.md) · [Rewrite losers and iterate](../frameworks/rewrite-losers-and-iterate.md) · [KPIs and columns](../frameworks/kpis-and-columns.md) · [Ad account audit](ad-account-audit.md) · [Marksman/Sniper testing](../concepts/marksman-sniper-testing.md) · [Ad definitions](../concepts/ad-definitions.md) · [Rubrics index](README.md)
