---
title: "Creator swap and clone-the-winner: the course method and the compliant version (run sheet)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "unverified (same presenter and Max Fusion tooling as 020, probably Camilo)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/015-change-creators-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/016-clone-broll-ugc-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
tags: [framework, creator-swap, clone-winning-ads, seedance, nano-banana-pro, kling, ai-podcast, voice-design, compliance-gate, run-sheet]
updated: 2026-11-13
---

# Creator swap and clone-the-winner (compliant version)
> The course swaps the person in a proven talking-head or B-roll clip for an AI-generated one (Nano Banana Pro frame edit → Seedance 2.0 reference-video job → voice fix) and builds podcast ads from real podcast frames. This page gives the exact method, marks the parts that copy someone else's asset or likeness as **don't execute**, and gives the version our agents run: swap only inside our own rights-cleared footage, otherwise rebuild the mechanism from a brief.

## 🤖 Agent use
- **Use when:** a talking-head or UGC clip we own has a proven script/angle and we want the same ad with a different creator look; or a competitor ad is winning and someone asks to "clone" it; or we are building a two-host AI podcast ad.
- **Inputs → outputs:** source clip + rights record + audited script → rights decision → swapped clip with a generated face and a designed voice, **or** a mechanism brief that goes to the [Seedance workflow](ai-ugc-seedance-workflow.md).
- **Rules:**
  - **DO** run the rights decision (table below) before touching a clip; the lesson never says whose pillow ad the 016 demo is [L16 Compliance](../lessons/016-clone-broll-ugc-ads.md).
  - **DO** edit a screenshot of the source frame, not a blank image, and keep the same pose and arm position: "this one where the arm is the same as the original one will work" [L15 00:03; 00:59–01:38](../lessons/015-change-creators-with-ai.md).
  - **DO** trim the source to 2–15 s and ≤50 MB [L16 00:30](../lessons/016-clone-broll-ugc-ads.md); set the output "one second above the length of the video" [L15 01:38](../lessons/015-change-creators-with-ai.md).
  - **DO** replace the voice when the face changes: Seedance keeps the source voice; a swapped woman "doesn't sound like a girl" [L15 02:29](../lessons/015-change-creators-with-ai.md). Design a voice and reference it as `@Audio1` [L15 02:29–03:19](../lessons/015-change-creators-with-ai.md).
  - **DO** describe attributes only in face prompts; never "look like xyz" (page example, [L15](../lessons/015-change-creators-with-ai.md)).
  - **DON'T** swap faces on another brand's or creator's ad (course framing "clone winning ads", **don't execute**): the swap keeps their script, visuals and claims [L15 Compliance](../lessons/015-change-creators-with-ai.md).
  - **DON'T** keep a real podcast host's face, set or voice; change "as much of the image as possible", face to "the opposite of what it is" [L18 02:24–03:16](../lessons/018-realistic-ai-podcasts-tutorial.md), and verify the result resembles no one.
  - **DO** make one change per image-edit prompt: "When I tried to do too much in one go, it looked weird" [L18 07:40](../lessons/018-realistic-ai-podcasts-tutorial.md).
  - **DO** paste the same voice block (accent, speed, mic, echo, volume change off-mic, delivery) into every podcast clip [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md).
- **See also:** [AI creator compliance](../concepts/ai-creator-compliance.md) · [Diversification vs variation](../concepts/diversification-vs-variation.md) · [Character consistency](../concepts/character-consistency.md) · [Seedance workflow](ai-ugc-seedance-workflow.md) · [Shared competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) · [LLM output claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

## Rights decision (step 0)
| Source clip | Allowed action | Why |
|---|---|---|
| Our ad, creator's contract covers AI modification of face **and** voice | Swap per run sheet A; generated face + designed voice | rights cleared |
| Our ad, contract silent on AI modification | Don't swap; produce a new clip from the same brief ([Seedance workflow](ai-ugc-seedance-workflow.md)) or get a signed addendum | likeness/voice use not licensed (derived) |
| Competitor's or any third party's ad | **Don't swap.** Run sheet B: tear down → mechanism brief → new script, new visuals, our claims | copying the asset; a new face does not make it ours ([L15](../lessons/015-change-creators-with-ai.md), [L16](../lessons/016-clone-broll-ugc-ads.md) compliance) |
| Real podcast or interview frame as a look reference | Composition/mood only; run sheet C with full likeness removal and set changes | [L18 Compliance](../lessons/018-realistic-ai-podcasts-tutorial.md) |
Record the decision in `rights.md` (source, owner, licence/release reference, decision).

## Compliance gate (applies to A, B and C)
| # | Check | Pass condition | Course example that fails it (**don't execute**) |
|---|---|---|---|
| G1 | Claim audit | The reused script's claims are verified; a proven script is not a proven claim | — (scripts not shown in 015/016) |
| G2 | No real-person likeness | New face generated, resembles no real person; no "look like [name]" | "Change his face to look like xyz" (page template) [L15](../lessons/015-change-creators-with-ai.md); real podcast host frame [L18 02:24](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| G3 | No real-person voice | Source creator's voice not kept on a different face; no cloned host voice | Seedance keeps the source voice by default [L15 02:29](../lessons/015-change-creators-with-ai.md) |
| G4 | AI person not a real customer | No testimonial framing for the swapped creator or AI hosts | AI hosts voicing proof lines ([L18 08:36–09:07](../lessons/018-realistic-ai-podcasts-tutorial.md); see 017) |
| G5 | Disclosure | Platform AI labelling checked (derived) | — |

## Run sheet A: swap the creator in our own rights-cleared clip (015, 016)
Settings at recording (Aug–Sep 2026).

| # | Step | Tool / model | Exact settings | Input | Output file | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Rights + gate | — | table above | source clip | `rights.md`, `claim-audit.md` | Both pass | — | derived |
| 2 | Trim source | any editor | 2–15 s, ≤50 MB, 9:16 | source clip | `swap/source.mp4` | Speaker clearly framed | Too long → trim (demo cut to 13 s) | [L16 00:30](../lessons/016-clone-broll-ugc-ads.md) |
| 3 | Screenshot a pose frame | player | frame with hands/arms visible | `source.mp4` | `swap/frame.png` | Pose representative of the clip | — | [L15 00:03](../lessons/015-change-creators-with-ai.md); [L16 00:47](../lessons/016-clone-broll-ugc-ads.md) |
| 4 | New creator image | Max Fusion → Images → **Nano Banana Pro** (GPT Image 2 judged less real) | Short replacement command, attributes only; same gender; ≥2 variants | `frame.png` | `swap/creator_vN.png` | Same arm position; lighting like a phone photo; resembles no real person | Pose differs → "would not work", pick the matching variant | [L15 00:03–01:38](../lessons/015-change-creators-with-ai.md); [L16 00:56–01:18](../lessons/016-clone-broll-ugc-ads.md) |
| 5 | Voice for the new face | Max Fusion "design a new voice" (or ElevenLabs Voice Design) | Text description of age, gender, tone; sample line | description | `swap/voice.mp3` (`@Audio1`) | Fits the new face | "Replace voice" stock search is the fallback; he prefers design | [L15 02:29](../lessons/015-change-creators-with-ai.md) |
| 6 | Reference-video job | Max Fusion → Videos → **Seedance 2.0 → References** | `@Video1` + `@Image1` (+ `@Audio1`); length = source + 1 s; 9:16; 720p (13 s = 130 credits on screen) | prompt below | `swap/clip_vN.mp4` | Script verbatim, lip-sync, realism | "content… flagged by a content checker" → change inputs; voice unchanged → add `@Audio1` line | [L15 01:51; 00:22](../lessons/015-change-creators-with-ai.md); [L16 01:31–01:35](../lessons/016-clone-broll-ugc-ads.md) |
| 7 | Review + QA | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | — | `clip_vN.mp4` | `swap/clip_final.mp4` | Gate still true | — | page step 7 |
| 8 | Test | ad account | Run against the original as a creator variant | final clip | test log | Treat as a variation of one concept, not a new concept ([Diversification vs variation](../concepts/diversification-vs-variation.md)) | — | derived |

Prompt patterns (verbatim from the course):
```text
Replace the man for a black guy similar age without glasses
Change this to a blonde woman with a green pajama top
@Video1 is an ad of a man testing a pillow. Replace the man for the woman in @Image1
Replace the man in @Video1 with the woman from @Image1. Change the voice to match @Audio1
```
Structure: describe the source ("`@Video1` is an ad of …"), state the change, point to the image (and audio) reference [L16 01:31](../lessons/016-clone-broll-ugc-ads.md). Course note: "Your audience pool gets larger as more people will buy because of different formats" [L15 01:38](../lessons/015-change-creators-with-ai.md) (instructor claim, no data).

## Run sheet B: "clone a winner" we don't own (compliant replacement)
| # | Step | Output |
|---|---|---|
| 1 | Tear down the winner: hook type, on-screen text pattern, shot order, pacing, demo, proof type, CTA ([shared teardown playbook](../../../../playbooks/competitor-ad-teardown.md)) | `teardown.md` |
| 2 | Write the mechanism brief: e.g. 016's "problem-first on-screen hook, in-bed demo, product test" ([L16 Compliance](../lessons/016-clone-broll-ugc-ads.md)) | `mechanism-brief.md` |
| 3 | New script with our product facts and customer language ([write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md)); no lines, characters or claims from the source | `script.md` |
| 4 | Gate + produce with a generated creator ([Seedance workflow](ai-ugc-seedance-workflow.md)) or a real creator | clips |

## Run sheet C: two-host AI podcast ad (018)
| # | Step | Tool / model | Exact settings | Input | Output file | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Find a niche podcast look | Pinterest (click through "related"), YouTube Shorts search (e.g. "peptides podcast") | Real, popular-looking setups only | niche keywords | `refs/podcast-look-*.jpg` | Not AI-made ("you can actually tell an AI one from a mile away") | AI-made refs → discard | [L18 00:55–01:54](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| 2 | Remove likeness, speaker A | Nano Banana Pro (GPT Image 2 too sharp, loses camera texture) | One edit per prompt: (1) face/hair/glasses, (2) set (plant, background colour), (3) clothes | ref screenshot | `podcast/A_vN.png` | Face unrecognisable; camera texture kept; set not iconic | Too many changes at once → artefacts; iconic set rejected → change plant/background/clothes in separate edits | [L18 02:24–04:11; 07:40](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| 3 | Speaker B | Nano Banana Pro | "Flip the creator horizontally and change it to be a [age] [gender], [hair], [glasses], [look]" | `A_final.png` | `podcast/B_vN.png` | Same plane, facing A, distinct identity | Background change fails → several tries | [L18 06:02–06:56](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| 4 | 5 s voice tests | Seedance 2.0 References or **Kling 3.0 Pro** (start frame) | ~5 s; voice block (template below) in every prompt | still + line | `podcast/A_test.mp4` | Accent, mic sound consistent | Seedance vs Kling: "the best one was the Kling one" (one test) | [L18 04:11–06:56](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| 5 | Full lines + reactions | same model | Reactions with simple prompts ("laughs first then says…") | stills + audited lines | `podcast/A_NN.mp4`, `podcast/B_NN.mp4` | Voice identical across generations | Voice drifts → the voice block was edited; restore it | [L18 07:40–08:36](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| 6 | Stitch | editor | Hook clip A → B challenge → A proof; cut-aways | clips | `edit/podcast_v1.mp4` | Hook first; tight | — | [L18 08:36–09:43](../lessons/018-realistic-ai-podcasts-tutorial.md) |

Voice block (page template, verbatim):
```text
The creator speaks in a [accent] accent at [speed]. The voice sounds like it's coming from a podcast mic with little echo and reverberation. As her mouth moves away from the microphone, the audio changes in volume. She speaks [delivery style].
She says: "[line]"
```
Keep accent choices non-stereotyped (lesson page caution); prefer neutral descriptors of pace and tone.

## Disagreements and defaults
- **Best model for a talking podcast host:** Kling 3.0 Pro beat Seedance 2.0 in 018 [06:56](../lessons/018-realistic-ai-podcasts-tutorial.md); 015/016/020 default to Seedance 2.0. Single tests (instructor claims). **Default:** run the 5 s test on both, keep the better one.
- **Voice consistency method:** prompt the voice per clip (018 preference, "to save so much time" [06:02](../lessons/018-realistic-ai-podcasts-tutorial.md)) vs clone/replace voice in Max Fusion (same lesson) vs design a voice as `@Audio1` (015). **Default:** designed voice as `@Audio1` when the tool accepts audio references; otherwise identical voice block per clip.

## Where it's taught
- [015 Change creators with AI](../lessons/015-change-creators-with-ai.md): frame edit [00:03–01:38], Seedance job [01:51], voice fix [02:29–03:19].
- [016 Clone B-roll UGC ads](../lessons/016-clone-broll-ugc-ads.md): limits [00:30], edit [00:56], prompt [01:31], settings [01:35].
- [018 Realistic AI podcasts](../lessons/018-realistic-ai-podcasts-tutorial.md): references [00:55], likeness removal [02:24–04:11], voice prompting [05:08], speaker B [06:02], stitch [08:36–09:43].

## Related
[Seedance workflow](ai-ugc-seedance-workflow.md) · [Rizz-model pipeline](rizz-model-ai-ugc-pipeline.md) · [AI post-production](ai-post-production.md) · [Research document protocol](research-document-protocol.md) · [Prompt library](../libraries/prompts.md)
