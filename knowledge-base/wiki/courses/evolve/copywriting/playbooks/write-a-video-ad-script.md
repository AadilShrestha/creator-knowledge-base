---
title: "Playbook: write a video ad script (concept brief → 3 hook/bridge pairs + 1 hold + 1 CTA → editor or creator brief)"
type: playbook
creator: evolve
course: copywriting
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/70-how-to-write-video-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/71-how-to-write-video-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/72-action-item-write-your-video-ad-briefs.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/23-the-framework-behind-great-hooks.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/27-how-to-write-a-bridge.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/28-how-to-prevent-handle-objections-in-writing.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/29-how-to-pitch-without-rejection.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/34-how-to-write-with-labels-customer-language.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/05-why-you-need-to-write-in-the-environment.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/11-why-you-need-to-write-less-fluff.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/53-the-iteration-playbook-formats-styles.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/67-how-to-write-image-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/68-how-to-write-image-ads-part-2.md
tags: [playbook, video-ads, ugc, script-writing, hook-bridge-hold, mega-prompt, product-truth, creator-brief, editor-brief, quality-gate]
updated: 2026-10-21
---

# Playbook: write a video ad script
> From a concept brief to a test-ready short video: close the feedback loop from the last test, gather the four documents, draft (with the course's mega prompt or by hand) three hook/bridge pairs, one universal hold and one CTA, then spend the real effort editing line by line with customer language and verified facts, add visuals last, and hand the editor (or creator) a card brief. Includes a (derived) path for on-camera UGC creators.

## 🤖 Agent use
- **Use when:** a concept brief from [ad idea to brief](ad-idea-to-brief.md) says `format: video`; a static concept needs its video version; an iteration needs a new script.
- **Inputs → outputs:** concept brief + memo + product truth sheet (facts with sources) + last test learnings + four documents (Product, New Mechanism, New Information, Customer Data) + execution model → `video_script` (template below) + card brief → quality-gate result → hand-off to editor or [creator brief](../../../../playbooks/creator-brief.md).
- **Rules:**
  - **DO** complete the feedback loop first (five questions) and say how the answers change the script. [L70 06:31–09:27](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** treat the AI draft as 70–80%: "You need to ... get it to a hundred percent." [L70 24:58](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** verify every number and term on the product page before the script ships (the AI draft said GLP-1 +68%; the final says 56% "because of what was on the website"). [L71 25:12](../lessons/71-how-to-write-video-ads-part-2.md)
  - **DON'T** let any model or creator invent proof volume, testimonials or authorities; use the real social-proof tier. [L70 12:01–12:44](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** keep hold and CTA identical across the three hook/bridge variants so the test isolates the opening. [L72 Modular Output Check](../lessons/72-action-item-write-your-video-ad-briefs.md)
  - **DO** write in the environment: one card per hook/bridge, one hold card; "for hooks it's an absolute non-negotiable." [L05 04:42](../lessons/05-why-you-need-to-write-in-the-environment.md)
  - **DO** take a break and reread before shipping; the agency's writer briefs Thursday/Friday and rereads Monday, often "Oh God, I got to rewrite this whole thing". [L68 43:12–44:46](../lessons/68-how-to-write-image-ads-part-2.md); [L11 08:13](../lessons/11-why-you-need-to-write-less-fluff.md)
  - **DO** copy the mechanism, not the asset, when the concept came from a competitor ad (⛔ G5).
- **See also:** [Video ad script workflow](../frameworks/video-ad-script-workflow.md) · [Copy checklist scorecard](../rubrics/copy-checklist-scorecard.md) · [Static ad workflow product-truth QA](../frameworks/static-ad-workflow.md#product-truth-qa) · [Prompts library](../libraries/prompts.md) · [Hooks library](../libraries/hooks.md) · [Rewrites library](../libraries/rewrites.md) · concepts: [hooks](../concepts/hooks.md), [bridges](../concepts/bridges.md), [objection handling](../concepts/objection-handling.md), [pitch transition](../concepts/pitch-transition.md), [show don't tell](../concepts/show-dont-tell.md), [labels and customer language](../concepts/labels-and-customer-language.md)

## Steps
| # | Step | Do | Output | Consult |
|---|---|---|---|---|
| 1 | Intake | Read the concept brief and memo; confirm angle, sub-avatar, mechanism, authority, awareness (Problem- or Product-Aware for this prompt) | brief summary | [memo framework](../frameworks/mini-breakthrough-memo-and-growth-guide.md) |
| 2 | Feedback loop | Answer the five questions (tested before? best/worst hook? off metrics? why cared or not? new learnings?); "N/A" if untested | `feedback` | [workflow: five questions](../frameworks/video-ad-script-workflow.md#the-five-feedback-questions-verbatim-from-the-prompt) |
| 3 | Hypothesis | Same desire; what changes; what you will show instead of tell | `hypothesis` (becomes "Growth Guide Notes") | [L70 03:09–05:38](../lessons/70-how-to-write-video-ads-part-1.md) |
| 4 | Documents | Product doc, New Mechanism, New Information, Customer Data; write "none" for missing ones; pull 10–20 verbatim customer lines (Reddit/reviews) | `inputs` | [L70 09:27–12:01](../lessons/70-how-to-write-video-ads-part-1.md); [L68 00:00–03:32](../lessons/68-how-to-write-image-ads-part-2.md) |
| 5 | Pick the execution model | AI voiceover + B-roll (course default) · on-camera creator (derived path below) · founder/authority delivery · AI animated format | `execution` | [L72 Visual Execution System](../lessons/72-action-item-write-your-video-ad-briefs.md); [L53](../lessons/53-the-iteration-playbook-formats-styles.md) |
| 6 | Draft | Run the mega prompt ([L72 verbatim](../lessons/72-action-item-write-your-video-ad-briefs.md#the-prompt-verbatim)) in a fresh chat/project, or write by hand to the same structure; confirm the true social-proof tier | 3 hooks, 3 bridges, 1 hold, 1 CTA, visuals, strategic explanation | [workflow: structure](../frameworks/video-ad-script-workflow.md#structure-and-timing-prompt) |
| 7 | Modular check | 3/3/1/1; hold and CTA identical; 30–45 s; one Objection → Claim → Proof → Benefit cycle | pass / redo | [L72](../lessons/72-action-item-write-your-video-ad-briefs.md) |
| 8 | Hooks | Each hook has gap + emotion + stakes; one slightly lower-valence "self-check" hook; the three hooks use three different entry points (discovery, contrarian, pain validation) | 3 hooks | [L23](../lessons/23-the-framework-behind-great-hooks.md); [L71 01:24–04:13](../lessons/71-how-to-write-video-ads-part-2.md); [hooks](../concepts/hooks.md) |
| 9 | Bridges | One per hook (~to 8 s); pick a pattern: mechanism, escalate problem, escalate desire, reposition problem, allude to new information, set a timeline; show the escalation; no reassurance ("it's extremely common") | 3 bridges | [L27 02:15–09:02](../lessons/27-how-to-write-a-bridge.md); [L52 07:24–10:40](../lessons/52-the-iteration-playbook-script.md) |
| 10 | Hold | Specific objection (name real past attempts) → reason-why → claim with the unique mechanism ("first/only X that ...") → proof (real study / real tier) → benefit as behaviour → CTA with loop closure and risk reversal | 1 hold + CTA | [L28](../lessons/28-how-to-prevent-handle-objections-in-writing.md); [L29](../lessons/29-how-to-pitch-without-rejection.md); [L71 08:47–13:45](../lessons/71-how-to-write-video-ads-part-2.md) |
| 11 | Line-by-line edit | Replace every generic line with a research specific; customer word + clinical word; voice matches format (third person for AI VO); rerun through the prompt ("let me know where it has issues"; "does this categorize us?") | revised script | [workflow: editing pass](../frameworks/video-ad-script-workflow.md#the-editing-pass-lesson-71) |
| 12 | Product-truth QA | T1–T10: numbers, terms, supported benefits, unverifiable adjectives, studies needed, compliance words, social-proof tier, empty claims, congruence, grade ≤ 6 | QA log | [static workflow T1–T10](../frameworks/static-ad-workflow.md#product-truth-qa) |
| 13 | Visuals last | Ask for visuals only after the copy is locked; one instruction per line: source, avatar demographic, action/emotion, setting, text overlay; show behaviour, not concepts | visuals | [L71 25:12](../lessons/71-how-to-write-video-ads-part-2.md); [L72](../lessons/72-action-item-write-your-video-ad-briefs.md) |
| 14 | Card brief | Fill the card fields (client, batch id, type, sizes, link, variations "3 HOOKS / 1 HOLD / 3 TOTAL ADS", concept + Growth Guide notes, Hook 1–3 cards, Hold card, optional visuals) | card brief | [L72 card template](../lessons/72-action-item-write-your-video-ad-briefs.md#brief-card-set-fill-in-template) |
| 15 | Break, reread, gate | Rest (20 min to a day); reread aloud; run the quality gates below | gate result | [L68 39:59–44:46](../lessons/68-how-to-write-image-ads-part-2.md) |
| 16 | Name, log, hand off | Ad names with batch (and `ITER#N_BATCH#ORIG#` if an iteration); Roadmap status → Filming; log spin-off concepts | named brief | [ten-step learnings](../frameworks/ten-step-iteration-learnings.md#naming-format-verbatim-l46-page) |

Time budget the course models: "one brief, I would say even per day, especially if they're videos" [L71 14:43](../lessons/71-how-to-write-video-ads-part-2.md).

## (Derived) Path for on-camera UGC creators
The course prompt is built for "B-roll compilation + AI voiceover... No talking heads" [L72](../lessons/72-action-item-write-your-video-ad-briefs.md). For a creator who films themselves:
1. Keep steps 1–4, 7–12 unchanged (same copy system, same truth gates).
2. Step 5: choose the messenger on purpose (peer with the same problem, insider, expert, founder); an identified authority should deliver it themselves when possible [L53 11:13–13:09](../lessons/53-the-iteration-playbook-formats-styles.md).
3. Steps 8–10: write first-person lines only where they are true for this creator; otherwise use the third-person authority frame ("Scientists call it...") [L71 16:01](../lessons/71-how-to-write-video-ads-part-2.md).
4. Step 13: replace stock-footage instructions with a shot list (setting, prop, action, expression, on-screen text per line); B-roll only for mechanism or impossible-to-film moments; film the behaviours the script shows.
5. Step 14: add to the card brief: locked words (hook lines, every claim and number), "say the rest in your own words", do/don't list, deliverables (3 hook/bridge openings + 1 hold, each as separate takes). Hand off with Tether's [creator brief](../../../../playbooks/creator-brief.md).
6. Packaging: 3 hook/bridge pairs × 1 hold = 3 cuts; when a hook wins, test a second hold (one change) — this becomes Tether's 3 hooks × 2 bodies.

## Output: video script
```yaml
video_script:
  id: SCR-<batch>-<nn>
  concept_ref: IDEA-<...>
  client: "<brand>"
  batch: "SBATCH#<n>"                 # must match the roadmap
  execution: ai_vo_broll | on_camera_creator | founder_authority | ai_animated
  awareness: problem | product
  length_s: 30-45
  feedback_loop: {tested_before: "N/A | <...>", best_hook: "", off_metrics: "", why_cared: "", new_learnings: ""}
  growth_guide_notes: "<hypothesis paragraph>"
  hooks:
    - id: H1
      copy: "<spoken hook>"
      on_screen_text: "<≤7 words>"
      entry_point: discovery | contrarian | pain_validation | self_check
      bridge: ["<line>", "<line>"]
      visual: "VISUAL: <source> - <avatar demographic> <action/emotion>, <setting>. Text overlay: \"<...>\""
    - id: H2
    - id: H3
  hold:
    objection: "<specific past attempts>"
    reason_why: "<why they failed / mechanism gap>"
    claim: "<first/only ... that [mechanism]>"
    proof: "<study or real tier, with truth_ref>"
    benefit: "<behaviour, shown>"
    secondary_benefit: "<optional, <3 s>"
  cta: "<loop closure + risk reversal + value-framed price; no fake scarcity>"
  visuals_hold: ["<one per beat>"]
  locked_words: ["<hook lines>", "<every number/claim>"]       # creator path
  truth_log:
    - {line: "<...>", claim: "<...>", truth_ref: "<fact id / page / study>", status: verified}
  social_proof_tier: "<10,000+ | 1,000-10,000 | 100-1,000 | 10-100 | <10/borrowed | none>"
  checks: {modular: pass, copy_scorecard: "<pct>, gates pass", tether_ad_scorecard: "<score>", ugc_checklist: "<pass|fix|block|n.a.>"}
  spin_off_concepts: ["<logged idea>"]
  naming: "<Batch#..._<concept>_ITER#N_BATCH#ORIG#_...>"
```

## Quality gates (all must pass)
1. **⛔ gates G1–G6** of the [copy checklist scorecard](../rubrics/copy-checklist-scorecard.md) (truth, terms, no fabricated proof, no fake urgency/danger, mechanism not asset, honest first person).
2. **Copy checklist scorecard ≥ 80%**, with A3 (hook), A4 (mechanism), A5 (authority), D4 (show don't tell), D8 (objections) at least 2.
3. **Modular packaging** (E): 3/3/1/1, identical hold and CTA, 30–45 s, a visual and text overlay per line.
4. **Tether [ad scorecard](../../../../rubrics/ad-scorecard.md) ≥ 80, no auto-fail** (criterion 9b story structure for video).
5. **Creator path only:** Tether [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) verdict `pass` (see the setup-share default below).

## Combine with Tether Lab
| Shared page | Use it for | Evolve contributes | Tether contributes |
|---|---|---|---|
| [UGC script writing](../../../../playbooks/ugc-script-writing.md) | Story-led creator scripts | Feedback loop, four documents, hook/bridge/hold modules, editing pass, Big 4, categorization and social-proof rules | Story frameworks (Pixar, Story Spine, SCQA, In Medias Res, Skeptic), beat sheet by length, on-screen text rules, proof ledger, CTA language |
| [Creator brief](../../../../playbooks/creator-brief.md) | Hand-off on the creator path | Locked claims, the card brief fields | Casting/messenger, face and tone, shot list, props, deliverables matrix, seed asset, AI-UGC limits |
| [Competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) | When the concept came from a competitor video | Hooks verbatim, nine components | Beat map, winner signals, transferable mechanism |
| [Angle remix](../../../../playbooks/angle-remix.md) | Upstream angle | Persuasion chain, memo | Self/zone shifts, fidelity check |
| [Test and iterate](../../../../playbooks/test-and-iterate.md) | After launch | Outcome labels and iteration lists | Learning goal, read-outs by self/zone/TEEP, scaling |
| [Ad scorecard](../../../../rubrics/ad-scorecard.md) · [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) | Gates 4–5 | Copy craft and ⛔ truth gates come first | Psychology and production readiness |

**In one line:** Evolve = copy craft, the modular test design and the editor brief; Tether = psychology lenses (one core emotion, zone, self, heuristics, story framework) and creator production.

**Disagreements and agent defaults (logged in the contradiction notes):**
| Topic | Evolve | Tether | Default |
|---|---|---|---|
| Test packaging | 3 hook/bridge pairs × 1 hold [L70 15:59–16:39](../lessons/70-how-to-write-video-ads-part-1.md) | 3 hooks × 2 bodies ([UGC script writing](../../../../playbooks/ugc-script-writing.md)) | Launch 3 hook/bridge × 1 hold; after a hook wins, test a second body/hold with one change |
| Setup share | Hook 0–3, bridge 3–8, claim at ~11–16 s of 30–45 s | ~2/3 of runtime on setup before the product | Evolve timing for 30–45 s AI-VO/B-roll; Tether's setup share for story-led creator UGC; in both, run Evolve's "Extended Problem Section" as an early iteration |
| Hook length | Prompt: ~5 words, max 2 lines; Spencer's final hooks 13–17 words | On-screen overlay ≤ 7 words | On-screen text ≤ 7 words; the spoken hook may run longer if hook + bridge ≤ ~8 s and the first sentence stands alone |
| Social-proof wording | Tier words allowed ("thousands of women" for 1,000–10,000) | Exact, typed numbers; "thousands love it" is weak/untyped | Use the exact documented number when you have it; tier words only when the documented count is inside the tier; never round up |
| Emotions | Hit 2–3 of the Big 4 values per section | One core emotion per ad | Compatible: one core emotion (zone), 2–3 value words that serve it |

## Related
[Course playbooks hub](README.md) · [Ad idea to brief](ad-idea-to-brief.md) · [Write static image ads](write-static-image-ads.md) · [Iterate on test results](iterate-on-test-results.md) · [Video ad script workflow](../frameworks/video-ad-script-workflow.md) · [Open loops](../concepts/open-loops.md) · [Raising the stakes](../concepts/raising-the-stakes.md)

## Sources and limitations
- Course steps come from lessons 70–72 (the instructor ran Claude Sonnet 4.5 per the on-screen selector, [L72 limitations](../lessons/72-action-item-write-your-video-ad-briefs.md)). The step numbering, the creator path, the YAML and the gate thresholds are pipeline design.
- The final course script has no published results; treat it as a craft example, not proof of performance.
