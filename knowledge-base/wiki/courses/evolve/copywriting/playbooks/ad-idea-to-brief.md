---
title: "Playbook: ad idea to brief (competitor or own winner → angle → memo → concept brief)"
type: playbook
creator: evolve
course: copywriting
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/03-how-to-guarantee-you-get-better-at-copywriting.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/09-the-importance-of-how-you-say-it.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/17-being-aware-of-avatars.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/18-being-aware-of-angles.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/19-being-aware-of-mechanisms.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/20-being-aware-of-authorities.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/21-being-aware-of-market-awareness.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/22-how-to-finalize-your-ad-ideas.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/46-the-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/51-how-to-iterate-on-breakthroughs.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/56-positioning-exercise.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/57-100-hook-templates-form-winning-ads-deck.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/60-facts-list.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/61-objections-list.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/67-how-to-write-image-ads-part-1.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/68-how-to-write-image-ads-part-2.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/08-the-3-checks-for-great-copywriting.md
tags: [playbook, pipeline, competitor-teardown, angle, breakthrough-memo, concept-brief, growth-guide, copy-the-mechanism, imitation, ideation]
updated: 2026-10-21
---

# Playbook: ad idea to brief
> Turn any raw idea (a competitor ad that is working, our own winner, or a research insight) into a justified, logged concept brief: tear the source down to its components, abstract the persuasion mechanism, rebuild it on our own avatar → angle → mechanism → authority chain with our facts, prove the idea in a Why/What/How memo, pick the format and testing method, then hand a filled brief to the static or video playbook.

## 🤖 Agent use
- **Use when:** a human says "we should do an ad like this", a teardown found a working competitor ad, a research pass surfaced a pain point, or the [iteration playbook](../frameworks/iteration-playbook.md) is not the right tool because this is a new idea.
- **Inputs → outputs:** source (ad link/screenshot/transcript, or research note) + product truth sheet (Master Document: product doc, facts list, objections list, sub-avatars with quotes) + position statement + account history → `ad_idea_brief` (template below): component card of the source, transferable mechanism, our persuasion chain, memo, Roadmap row, concept brief → hand-off to [write static image ads](write-static-image-ads.md) or [write a video ad script](write-a-video-ad-script.md).
- **Rules:**
  - **DO** copy the mechanism, not the asset: carry over the structure (what the ad does), never the competitor's lines, footage, characters, claims or stats. When a copied hook works, find the desire it communicates and write it your way rather than word for word (lesson rule; "executing it with different words to communicate the same thing") [L09 08:19–08:49](../lessons/09-the-importance-of-how-you-say-it.md)
  - **DO** look outside the niche for structures: "you don't just have to steal hooks from your competitors... you can also look across categories and sometimes those are the most powerful ones." [L57 00:54–01:39](../lessons/57-100-hook-templates-form-winning-ads-deck.md); "I'm not a big fan of copying exactly what people are doing in my industry." [L68 11:55–12:34](../lessons/68-how-to-write-image-ads-part-2.md)
  - **DON'T** accept a half-baked pitch ("I saw an ad and then I thought we should do it"): write Why / What / How with evidence. [L22 01:21–04:23](../lessons/22-how-to-finalize-your-ad-ideas.md)
  - **DO** tag the idea's origin: ideation (research), imitation (another brand's ad), iteration (our own ad). [L46 04:14–06:33](../lessons/46-the-10-step-iteration-process.md)
  - **DO** expect copied ads to die fast: if you "just claw and make this for me", competitors copy you back; easy-to-make ads are easy to replicate. [L51 05:36–08:01](../lessons/51-how-to-iterate-on-breakthroughs.md)
  - **DO** use only our verified facts in the chain; any claim without a `truth_ref` is removed (see ⛔ G1–G3 in the [scorecard](../rubrics/copy-checklist-scorecard.md)).
  - **DO** run the swap test on the planned headline: "Never write an ad that a competitor can sign." [L08 13:32](../lessons/08-the-3-checks-for-great-copywriting.md)
- **See also:** [Memo and Growth Guide](../frameworks/mini-breakthrough-memo-and-growth-guide.md) · [Nine-component audit](../frameworks/nine-component-audit.md) · [Positioning exercise](../frameworks/positioning-exercise.md) · [Copy checklist scorecard](../rubrics/copy-checklist-scorecard.md) · [Angles library](../libraries/angles.md) · [Templates library](../libraries/templates.md) · [Ad teardowns library](../libraries/ad-teardowns.md)

## Pipeline position
competitor teardown → **angle → memo → concept brief** (this playbook) → script ([video](write-a-video-ad-script.md)) or static ([static](write-static-image-ads.md)) → quality gate ([scorecard](../rubrics/copy-checklist-scorecard.md)) → test → [iterate](iterate-on-test-results.md).

## Steps
| # | Step | Do | Output | Consult |
|---|---|---|---|---|
| 0 | Load the product truth | Master Document: product doc, facts list (brand / product / market, each with source), objections list (product / angle / claim / belief), sub-avatars with verbatim quotes, new information, new mechanisms; position statement | `truth_sheet` | [L60](../lessons/60-facts-list.md), [L61](../lessons/61-objections-list.md), [L69 template](../lessons/69-action-item-write-your-image-ad-briefs.md), [positioning exercise](../frameworks/positioning-exercise.md) |
| 1 | Classify the source | Ideation / imitation / iteration; which of the five idea sources (customer research, another brand's ads, our own ads, a marketing book, an ad that stopped your scroll) | `origin` | [L46 04:14–06:33](../lessons/46-the-10-step-iteration-process.md); [L03 05:10–06:11](../lessons/03-how-to-guarantee-you-get-better-at-copywriting.md) |
| 2 | Tear down the source | Hooks verbatim; what each line *communicates* (feeling + desire); fill the [nine-component card](../frameworks/nine-component-audit.md) "executed" column; for competitor ads also run Tether's [teardown card](../../../../playbooks/competitor-ad-teardown.md) (zone, self, heuristics, winner signals) | `source_components` | [L09 00:00–08:49](../lessons/09-the-importance-of-how-you-say-it.md); [L03 04:10–04:40](../lessons/03-how-to-guarantee-you-get-better-at-copywriting.md) |
| 3 | Abstract the mechanism | Rewrite the working part as slots, no brand words: e.g. nurse-shoe hook → "use case, product category, made for specific avatar"; "Can't poop?" → "can't + taboo problem"; shampoo → "watch out for these ingredients when buying [product category]" | `transferable_mechanism` | [L57 00:54–01:39](../lessons/57-100-hook-templates-form-winning-ads-deck.md); [templates library](../libraries/templates.md) |
| 4 | Build our chain | Avatar card (desire, experience, emotion, behaviour) → "They want X. But they have the belief Y." → one angle (reason to buy) → mechanism that proves it (visual if possible) → authority signalled before the pitch → awareness level | `persuasion_chain` | [memo framework Part 1](../frameworks/mini-breakthrough-memo-and-growth-guide.md); [L17](../lessons/17-being-aware-of-avatars.md)–[L21](../lessons/21-being-aware-of-market-awareness.md) |
| 5 | Fit + originality check | Every claim in the chain has a `truth_ref`; swap test (a competitor's product in our line → still makes sense? fail); exact-match Google search of the planned headline; categorization check ("like X" → "first/only X that [mechanism]") | pass / rework | [L08 10:59–13:32](../lessons/08-the-3-checks-for-great-copywriting.md); [L58 Q9](../lessons/58-copywriting-checklist-when-writing.md); [L72 Categorization Check](../lessons/72-action-item-write-your-video-ad-briefs.md) |
| 6 | Write the memo | WHY (evidence: the source ad's traction, our account data, research), WHAT (angle + fill-in line), HOW (format + reference link + who appears) | `memo` | [L22 00:50–04:23](../lessons/22-how-to-finalize-your-ad-ideas.md) |
| 7 | Choose format + testing method | Decision table below | `format`, `testing_method` | [L67 01:37–12:27](../lessons/67-how-to-write-image-ads-part-1.md); [L70 03:09–04:07](../lessons/70-how-to-write-video-ads-part-1.md) |
| 8 | Log + rank | Ad Roadmap row (status Working, upvote, batch, desire, sub-avatar, angle, memo, awareness, file type, ad type) | `roadmap_row` | [memo framework Part 3](../frameworks/mini-breakthrough-memo-and-growth-guide.md) |
| 9 | Write the concept brief | Concept/swing, angle(s), testing method, format, variations (messaging + content), sizes, reference ads with "what you like", asset folder, primary text | `concept_brief` | [static workflow brief fields](../frameworks/static-ad-workflow.md); [video card fields](../frameworks/video-ad-script-workflow.md) |
| 10 | Quality gate | Memo gate (below) + scorecard section A and ⛔ G1/G3/G5 on the planned hooks | pass / rework | [copy checklist scorecard](../rubrics/copy-checklist-scorecard.md) |

### Step 7 decision table: format and testing method
| Situation | Format | Testing method | Source |
|---|---|---|---|
| New angle or sub-avatar, direction unknown | Static batch first (cheap, fast) | Marksman: several angles, one hook each | [L67 01:37; 12:27](../lessons/67-how-to-write-image-ads-part-1.md); Tether [static first](../../../../playbooks/static-ad-creation.md) |
| One angle you believe in; first execution failed as an "empty claim" | Video that explains and shows | Sniper: one angle, 3 hook/bridge pairs | [L70 03:09–04:07](../lessons/70-how-to-write-video-ads-part-1.md) |
| Mechanism hard to explain in a still | Video (mechanism animation or demo) | Sniper | [L53 03:58–05:36](../lessons/53-the-iteration-playbook-formats-styles.md) |
| Source is a competitor video that's clearly working | Video in our own execution (different hook, visuals, claims) | Sniper on the mechanism | (derived; Tether allows straight-to-UGC when a competitor's UGC mechanism is the source, [playbooks hub](../../../../playbooks/README.md)) |
| Source is a competitor native/AI ad | Rebuild components in a harder-to-copy format (founder/authority, real creators) | Sniper | [L51 12:19–14:45](../lessons/51-how-to-iterate-on-breakthroughs.md) |
| Our own breakthrough | Not this playbook: use [iterate on test results](iterate-on-test-results.md) | — | [L52](../lessons/52-the-iteration-playbook-script.md) |

### Memo gate (block if any "no")
- WHY names evidence (an ad, a result, or a research finding), not "I saw an ad".
- WHAT states one angle as a reason to buy (not just a concept like "us vs them").
- WHAT names the sub-avatar and the mechanism.
- HOW names the format and a reference (or "ideation, no reference").
- Every claim in WHAT has a `truth_ref`.
- If the source is a competitor ad: the brief uses its structure only (Tether fidelity check: no 5+ consecutive words, footage, characters, trademarks or claims, [angle remix step 4](../../../../playbooks/angle-remix.md)).

## Output: ad idea brief
```yaml
ad_idea_brief:
  id: IDEA-<yyyymmdd>-<nn>
  origin: ideation | imitation | iteration
  idea_source: customer_research | other_brand_ad | our_ad | book | scroll_stopper
  source_ref: "<link / screenshot / research note id>"
  source_teardown:
    hooks_verbatim: ["<...>"]
    communicates: "<feeling + desire, one phrase>"
    components_executed: {awareness: "", valence_intensity: "", desire: "", avatar: "", angle: "", mechanism: "", belief: "", positioning: "", urgency: ""}
    tether_card: "<link to teardown_card if competitor>"
  transferable_mechanism: "<slots only, no brand words>"
  persuasion_chain:
    sub_avatar: {name: "", desire: "", experience: "", emotion: "", behavior: "", quotes: ["<id: quote>"]}
    why_they_care: "They want <...>. But they have the belief <...>."
    angle: "<reason to buy>"
    mechanism: "<...>"
    authority: "<...>"
    awareness: problem | solution | product | unaware | most
    truth_refs: ["<fact ids>"]
  checks: {swap_test: fail_for_competitor, google_exact_match: not_found, categorization: none}
  memo: {why: "<evidence>", what: "<angle + fill-in line>", how: "<format + reference + who>"}
  format: static | video
  testing_method: marksman | sniper
  roadmap_row: {status: Working, upvote: "+1", batch: "BATCH #<n>", file_type: Static | Video, ad_type: Ideation | Imitation | Iteration}
  concept_brief:
    concept_swing: "<what we test>"
    angles: ["<...>"]
    variations: [{id: V1, messaging: "<hook/headline>", content: "<scene / image>"}]
    sizes: ["1080x1920", "1080x1080 safe", "1080x1350 safe"]
    reference_ads: [{link: "", what_we_like: "<structure only>"}]
    asset_folder: "<drive link>"
  handoff: write-static-image-ads | write-a-video-ad-script
  gate: {memo_gate: pass, scorecard_section_A: "<pct>", G1: pass, G3: pass, G5: pass}
```

## Worked example (from the course, abstracted)
- **Source:** our own ad "Negative Framing" (close to $280k spend, per the sheet) + a competitor ad that "did well with the UGC iteration too" → origin: iteration/blend.
- **Transferable mechanism:** lead with what the product *prevents* versus each other solution's negative outcome.
- **WHAT line (template):** "If you are [SUB AVATAR], This [UNIQUE MECHANISM] won't Do X everytime Y Happens which will not cause [THING SUB AVATAR IS SCARED OF]."
- **HOW:** "This will be a video that looks similar to this ad [LINKED HERE]." Result logged: Breakthrough ("NO LEARNINGS + NOT DONE!!!!!!!", sheet). [L22](../lessons/22-how-to-finalize-your-ad-ideas.md)

## Combine with Tether Lab
| Shared page | Use it for | Evolve contributes | Tether contributes |
|---|---|---|---|
| [Competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) | Step 2 on competitor ads | What each line communicates; nine copy components; ad-type tag | Beat map, heuristics, zone, self, TEEP, winner-signal confidence, the abstract "transferable mechanism" |
| [Angle remix](../../../../playbooks/angle-remix.md) | Steps 3–5 | Persuasion chain (angle → mechanism → authority), memo with evidence, swap test | Remix grid (change ≥2 psychology axes), fidelity check F1–F7, fit check, scoring |
| [Static ad creation](../../../../playbooks/static-ad-creation.md) | Hand-off when format = static | Concept brief fields, testing method | Weight map, headline limits, colour/font/face rules |
| [UGC script writing](../../../../playbooks/ugc-script-writing.md) | Hand-off when format = video | Hook/bridge/hold system (via [write a video ad script](write-a-video-ad-script.md)) | Story frameworks, beat sheet, proof ledger |
| [Creator brief](../../../../playbooks/creator-brief.md) | After the script | Card brief fields | Casting, shot list, seed asset |
| [Test and iterate](../../../../playbooks/test-and-iterate.md) | After launch | Outcome labels, issue codes | Learning goal per campaign, self/zone read-outs |
| [Ad scorecard](../../../../rubrics/ad-scorecard.md) · [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) | Step 10 and later gates | ⛔ truth gates, copy craft | Psychology scoring, test packaging |

**In one line:** Evolve = copy craft, the idea memo and the brief; Tether = the psychology lenses (zone, self, heuristics, TEEP) and the anti-copy fidelity check.

**Disagreements to resolve (see contradiction notes):**
- Tether's angle remix requires each variant to change **at least two psychology axes** from the source; Evolve logs "imitation" of a competitor's format or angle as a normal ad type. **Default:** imitations must pass Tether's fidelity check and change the execution (hook words, visuals, claims, proof); changing two psychology axes is required only when the source is a competitor ad, not our own winner.
- Tether ships statics first, then video after a static wins; Evolve moved a losing static angle to video because the static could not explain the claim. **Default:** static first for new angles; go straight to video when the claim needs a mechanism explanation or demonstration, or the source mechanism is itself a proven video.

## Related
[Course playbooks hub](README.md) · [Write static image ads](write-static-image-ads.md) · [Write a video ad script](write-a-video-ad-script.md) · [Iterate on test results](iterate-on-test-results.md) · [Avatars and angles](../concepts/avatars-and-angles.md) · [Unique mechanism](../concepts/unique-mechanism.md)

## Sources and limitations
- Steps 0–10, the decision table and the YAML are pipeline design built on the cited lesson rules. "$280k" and the Breakthrough label are the sheet's example values; the instructor says example rows are made up or anonymised [L22 00:00–00:50].
