---
title: "Rubric: UGC Script Pre-flight Checklist"
type: rubric
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/playbooks/ugc-script-writing.md
  - knowledge-base/wiki/frameworks/story-frameworks-for-ads.md
  - knowledge-base/wiki/frameworks/skeptic-format.md
  - knowledge-base/wiki/frameworks/visual-weight-hierarchy.md
  - knowledge-base/wiki/contradictions.md
tags: [rubric, checklist, ugc, script, pre-flight, qa, proof, hooks, story-structure, production-readiness]
updated: 2026-10-20
---

# Rubric: UGC Script Pre-flight Checklist
> Run this on every `ugc_script` before it goes to a [creator brief](../playbooks/creator-brief.md). ⛔ items are **blocking**: one "no" sends the script back. Other items are fixes; three or more "no" also send it back. Then score it with the [ad scorecard](ad-scorecard.md) (needs ≥80, no auto-fail).

## 🤖 Agent use
- **Use when:** a script is finished ([UGC script writing](../playbooks/ugc-script-writing.md)), or a creator's draft/edit comes back for review.
- **Inputs → outputs:** `ugc_script` + angle brief + product truth sheet + landing page → the checklist below filled (yes / no / n.a. + note) and a verdict: `pass` / `fix` / `block`.
- **Rules:** answer every item with evidence (line number or beat); n.a. needs a reason; never mark proof items "yes" without a `truth_ref`.
- **See also:** [Ad scorecard](ad-scorecard.md) · [Rules library](../libraries/rules.md) · [Hooks library](../libraries/hooks.md) · [Contradictions](../contradictions.md)

**Source key:** May7 = [Live May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · May21 = [Live May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · J = [Joanna Wallace](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md) · R1 = [Roast #1](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · R2 = [Roast #2](../courses/tether-lab/05-live-recordings/2025-06-25-roast-my-ads-2.md) · Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jul9 = [Live Jul 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · Jul16 = [Live Jul 16](../courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md).

## A. Strategy
- [ ] ⛔ One core message and **one** core emotion; no second emotional claim [R1 0:41:46] ([one core emotion](../concepts/one-core-emotion-per-ad.md)).
- [ ] The emotion is specific (sub-emotion + situation), not an umbrella word [Jun4 0:38:43].
- [ ] Self, zone and TEEP stage are named and consistent with each other (e.g. evaluation copy is situational [R3 0:34:44]).
- [ ] The angle is grounded in real customer evidence (review/Reddit/survey IDs), not invented by an LLM [May14 0:29:57].
- [ ] Ought scripts resolve pressure into relief; Z3/Z4 scripts target a situation or industry belief and end in hope [Jun11 0:20:12–0:21:13; Jun4 0:30:17].

## B. Hook (first 3 s)
- [ ] ⛔ The core message appears in frame 1 (spoken and/or on screen) [R3 0:18:56–0:21:32].
- [ ] The first visual is salient and matches the line; no skin-with-no-context opening for women's products [R3 0:20:31–0:21:08].
- [ ] Hook overlay ≤7 words, ≤3 lines, heaviest element in frame [R1 0:14:42; 0:36:37].
- [ ] 3 hook variants exist, each testing a different message or lever.

## C. Structure and pace
- [ ] A named story framework is followed (steps were pasted into any LLM prompt) [May14 0:50:44–0:52:19].
- [ ] Setup (problem + lived experience) is ~2/3 of the runtime; solution and CTA come in the last scenes [May14 0:19:45].
- [ ] A realism beat exists (doubt, "cautiously at first", imperfect or gradual results); no "overnight" transformation [May14 0:41:04–0:41:54].
- [ ] Beats are timed for the target length (15/30/45/60 s); the master cut can be shortened to 30 s and 15 s [May14 0:45:41–0:46:50].
- [ ] Pace planned at cuts every 2–4 s, with pauses on key lines [May14 0:43:30–0:48:12].

## D. Copy and voice
- [ ] Lines are written in the customer's words (from research) and say "you" more than "we" [R2 0:14:49].
- [ ] The creator is told to say it in their own words; key hook words are fixed [May14 0:22:33].
- [ ] Specific situations "four levels deep" ("every bowl we gave him, he destroyed") instead of general claims [R3 0:33:42].
- [ ] On-screen text matches the creator's expression in each shot (derived from [R2 0:06:23]).
- [ ] Humour, if any, is one type, cast with a performer [J 0:43:04–0:44:08]; shame, if any, sits on a character ([mirror effect](../concepts/mirror-effect.md)) [May21 0:49:15–0:52:00].

## E. Visuals and production notes
- [ ] Every beat has a visual/b-roll note; mechanism beats show ingredients/materials/texture ([sight smell](../concepts/sight-smell.md)) [R1 0:06:19].
- [ ] Props and setting prime the right life stage; no mis-signalling props [R2 0:25:31–0:27:32].
- [ ] Framing, light and grade match the target zone ([tone shifting](../frameworks/tone-shifting.md)).
- [ ] Casting spec (messenger type, face, posture) is stated ([model image psychology](../concepts/model-image-psychology.md)).

## F. Proof and compliance
- [ ] ⛔ Every claim maps to `claims_allowed` in the product truth sheet.
- [ ] ⛔ No fabricated reviews, testimonials, ratings, counts, press, endorsements, results or before/afters ([contradictions](../contradictions.md) row 10).
- [ ] ⛔ No fake scarcity or urgency; any stock/drop/deadline is in `scarcity_real` [Jul9 0:43:49].
- [ ] ⛔ No competitor footage, script lines (5+ consecutive words), characters, catchphrases, trademarks or claims ([fidelity check](../playbooks/angle-remix.md#step-4-fidelity-check-anti-copy-pipeline-design)).
- [ ] Real quotes are labelled as quotes and stay close to the original wording.
- [ ] Numbers are exact and typed ("1,200+ reviews from dairy lovers") [Jul16 0:39:20].
- [ ] No uncited Sarah stats used as fact ("0.48 s", "60,000×", "+13.6%").
- [ ] Regulated categories (supplements, skincare, health): claim wording follows `limits` (e.g. "*not typical results" [Jul16 0:56:36]).
- [ ] No synthetic person gives a testimonial ([AI UGC tools](../tools/ai-ugc-tools.md)).

## G. CTA and landing page
- [ ] Definitive CTA, never "Shop now"/"Learn more" [R1 0:26:52–0:29:09].
- [ ] ⛔ The landing page repeats the script's promise, offer and any claim/badge [R3 0:15:00–0:17:00].
- [ ] The biggest ability crusher is answered on camera or on the page ([Fogg](../frameworks/fogg-behavior-model.md)) [Jul16 0:27:14].
- [ ] Ad vibe (tone, palette, energy) matches the page ([3 Vs](../frameworks/three-vs-of-creative.md)).

## H. Test packaging
- [ ] 3 hooks × 2 bodies; Body B differs from Body A in exactly one way.
- [ ] Offer, CTA, landing page and creator are constant across variants.
- [ ] Names follow `<STAGE>_<EMOTION>_<angle>_ugc_h<n>b<n>_v1`.
- [ ] One learning goal for the test is written down ([test and iterate](../playbooks/test-and-iterate.md)).

## Verdict template
```yaml
ugc_checklist:
  script: SCR-<…>
  blocking_failed: []          # any ⛔ item → block
  other_failed: []             # ≥3 → fix and re-run
  notes: {"B2": "opens on model before message; move headline to frame 1"}
  verdict: pass | fix | block
  scorecard: SC-<…>            # must be ≥80, no auto-fail
```

## Related
[Rubrics hub](README.md) · [Ad scorecard](ad-scorecard.md) · [UGC script writing](../playbooks/ugc-script-writing.md) · [Creator brief](../playbooks/creator-brief.md) · [Story frameworks](../frameworks/story-frameworks-for-ads.md) · [Skeptic format](../frameworks/skeptic-format.md)
