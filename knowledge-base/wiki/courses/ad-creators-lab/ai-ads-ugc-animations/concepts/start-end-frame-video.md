---
title: "Start/end-frame video: first- and last-frame image-to-video, transitions, chaining and the Type A/B/C frame decision"
type: concept
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (Camilo's Crochet Ad Visuals skill 045; Narek 090; claymation and Zack-style tutorials unattributed)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/030-generate-realistic-ai-broll.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/039-skeleton-generating-videos.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/040-advanced-video-prompts.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/056-claymation-generating-videos-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/058-editing-claymation-step-by-step.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/062-talking-objects-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/064-workflow-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/065-script-to-prompt-generator.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/066-zack-d-films-generating-scenes-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
tags: [start-end-frame, first-last-frame, image-to-video, transitions, frame-chaining, kling, seedance, claymation, crochet, zack-d-films]
updated: 2026-11-13
---

# Start/end-frame video
> Give the video model the still where a shot starts and, only when the scene lands in a different stable state, the still where it ends; the model animates between them. Chain clips by reusing each clip's last frame as the next first frame, keep clips 3–4 s, and test on the cheapest model before the final.

## 🤖 Agent use
- **Use when:** animating stills into clips for any animated format (skeleton, crochet, claymation, talking objects, Zack-style), building scene-to-scene transitions, continuing an action across clips, or fixing a motion the model refuses to generate.
- **Inputs → outputs:** ordered, consistent stills (one per script beat, see [character consistency](character-consistency.md)) + voiceover timing → a Type A/B/C decision per shot → start frame (+ end frame for Type B) + one I2V prompt per shot → 3–4 s clips sped or slowed to the voiceover in the edit.
- **Rules:**
  - **DO** decide the frame type per shot (crochet skill, [L45 Step 2](../lessons/045-claude-skill-setup-explanation.md)): **Type A** start frame only, motion self-contained; **Type B** start + end frame, the state changes; **Type C** start frame only, held shot with subtle motion. "Default to Type A when unsure — fewer images, modern I2V handles full motion arcs from one keyframe."
  - **DO** make end frames "FINAL LANDED states — never mid-motion. If action resolves back to start, use Type A." ([L45 skill rule 7](../lessons/045-claude-skill-setup-explanation.md)).
  - **DO** for a scene-to-scene transition put scene N as the start frame and scene N+1 as the end frame: "This creates the transition between them" ([L56 00:00–02:57](../lessons/056-claymation-generating-videos-transitions.md)).
  - **DO** chain: "every clip's end frame is the next clip's start" ([L66 01:58](../lessons/066-zack-d-films-generating-scenes-transitions.md)); continue a scene by snapshotting the last frame and using it as the next first frame ([L90 12:29; 17:40](../lessons/090-ai-editing-2026-08-18.md)); sharpen a blurry snapshot first (GPT Image 2, "sharpen and enhance", 2K or 4K) ([L90 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md)).
  - **DO** keep clips 3–4 s; "we don't need to have anything like 10 seconds long, especially for Kling" ([L56 01:00](../lessons/056-claymation-generating-videos-transitions.md)). Generate the model minimum (3 s) and speed it up to the gap you measured; cut a new clip every 2–3 s ([L90 29:24–32:07](../lessons/090-ai-editing-2026-08-18.md)).
  - **DO** write the I2V prompt as `[Visual direction] + [camera direction] + [style suffix]` with one named camera move (static / slight push-in / slow pan left / arc right) ([L56 01:00–01:58](../lessons/056-claymation-generating-videos-transitions.md)); describe only the motion and camera, because "Each still is the first frame, so the look is already locked… One camera move + one action per clip — don't stack moves" (skeleton skill output, [L39 frame 02:36](../lessons/039-skeleton-generating-videos.md)).
  - **DO** end every prompt with "Animation must start at the first frame" inside the style suffix ([L56 01:58](../lessons/056-claymation-generating-videos-transitions.md); crochet I2V closing line, [L45 §2.3](../lessons/045-claude-skill-setup-explanation.md)).
  - **DO** test on the cheapest model first: Seedance 1.5 Pro ≈ 1 credit vs Kling 3.0 Pro ≈ 2.4 credits per 4 s at recording ([L56 05:07; 07:36](../lessons/056-claymation-generating-videos-transitions.md)); finalise on the better model when quality matters.
  - **DON'T** pay for audio or Pro tier on clips: audio off, 720 ([L56 07:12–08:13](../lessons/056-claymation-generating-videos-transitions.md)); add SFX in the edit ([L58 05:44](../lessons/058-editing-claymation-step-by-step.md)).
  - **IF** the model cannot do a motion **THEN** generate the opposite motion and reverse the clip in the editor ([L90 16:01–17:05](../lessons/090-ai-editing-2026-08-18.md)).
- **See also:** [Character consistency](character-consistency.md) · [Reference-first prompting](reference-first-prompting.md) · [Animated ad production pipeline](../frameworks/animated-ad-production-pipeline.md) · [AI post-production](../frameworks/ai-post-production.md) · [Tool settings](../libraries/tool-settings.md)

## Definition
**Start/end-frame video** (also "first/last frame") is image-to-video generation where you supply the opening frame and, optionally, the closing frame of the clip. The model fills the motion between them. Narek's three generation modes place it in context ([L90 09:43–10:14](../lessons/090-ai-editing-2026-08-18.md)): text-to-video only for quick B-roll; **image-to-video** for control of composition, character and action (his hangover ad used "first and last image only", [L90 11:00](../lessons/090-ai-editing-2026-08-18.md)); reference-to-video, the most powerful, with storyboards, avatar sheet, object sheet, style sheet, audio and video references.

## Why it matters
- Composition, character and product stay locked because the frame is the input, not the prompt; the prompt only has to carry motion ([L39 frame 02:36](../lessons/039-skeleton-generating-videos.md)).
- Transitions between script beats become one generation instead of a hard cut, which is the claymation and Zack-style look ([L56 00:00](../lessons/056-claymation-generating-videos-transitions.md); [L66 00:55–01:58](../lessons/066-zack-d-films-generating-scenes-transitions.md)).
- "Almost every software has it" ([L64 00:00](../lessons/064-workflow-breakdown.md)), so the method survives tool changes.
- Short clips at the model minimum keep credits low and match the 2–3 s cutting rhythm ([L90 31:37](../lessons/090-ai-editing-2026-08-18.md)).

## How to use (steps)
1. **Order the stills to the script** (one per beat; reorder on the canvas before animating, [L55 05:50](../lessons/055-prompts-frames-poppy-method.md)). Remove effect elements from stills that you want to animate in later ([L54 01:54](../lessons/054-prompts-frames-chatgpt.md)).
2. **Classify each shot** with the decision table below.
3. **Make missing end frames** from the start frame, so only the state changes: Generate variation with the start frame attached, paste the end-frame prompt ([L65 01:48–02:45](../lessons/065-script-to-prompt-generator.md)); "Only the state of the cantaloupe has changed" (prompt, [L65](../lessons/065-script-to-prompt-generator.md)).
4. **Write the I2V prompt**: visual direction (what happens between frames, in one sentence when it's more than a zoom, [L56 02:57–04:29](../lessons/056-claymation-generating-videos-transitions.md)) + one camera move + the style suffix + the character consistency sentence if a character appears ([L56 01:00](../lessons/056-claymation-generating-videos-transitions.md)).
5. **Set duration** at the model minimum or 3–4 s; 9:16; audio off; 720p.
6. **Test cheap, finalise better** (Seedance 1.5 Pro → Kling 3.0 Pro; skeleton: Seedance 1.5 Pro first, Kling 3.0 Pro "the best one for these", Kling 2.6 the credit saver, [L39 00:58](../lessons/039-skeleton-generating-videos.md)). Expect 4–5 attempts on hard scenes ([L90 12:29](../lessons/090-ai-editing-2026-08-18.md)).
7. **Chain**: snapshot the approved clip's last frame → sharpen → next clip's first frame ([L90 12:29; 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md)).
8. **Edit to the voiceover**: speed ramps ("flash out" / "flash in") hide the joins ([L58 01:29–03:33](../lessons/058-editing-claymation-step-by-step.md)); match motion direction between neighbours, since zoom-in → static → zoom-in is "a jarring cut" ([L42 03:03](../lessons/042-skeleton-editing-the-video.md)).

### Type A / B / C decision (crochet skill, [L45 Step 2](../lessons/045-claude-skill-setup-explanation.md))
| Shot behaviour | Type | Frames | I2V prompt carries | Example in the skill |
|---|---|---|---|---|
| Action happens and resolves; starts and ends in the same visual state | A | Start only | Full motion arc | Yarn vapor erupts and dissipates; a flame ignites and burns out |
| Scene lands in a different stable state | B | Start + end (end = final landed state) | The transition | Bottle on counter → bottle in hand; neutral → grimace |
| Held or near-still hero shot | C | Start only | Subtle motion (fiber sway, slow push, breath) | Character poses; product glows |
| Unsure | A | Start only | Full arc | "Default to Type A when unsure" |
| Scene N must morph into scene N+1 in the edit | B (transition) | Scene N + scene N+1 | How one becomes the other | Clay layers peel away to reveal the stomach ([L56 04:43 frame](../lessons/056-claymation-generating-videos-transitions.md)) |

### Model minimums and clip lengths stated (at recording, Aug–Sep 2026)
| Model / tool | Length used or stated | Note | Cite |
|---|---|---|---|
| Any I2V model (Narek) | Minimum 3 s; speed up to fit | New clip every 2–3 s | [L90 29:24–32:07](../lessons/090-ai-editing-2026-08-18.md) |
| Kling multi-shot | Shot lengths set inside one clip, total at least 3 s (member explanation) | Narek prefers cutting manually; multi-shot only with a storyboard | [L90 45:28–46:32; 1:00:46–1:01:50](../lessons/090-ai-editing-2026-08-18.md) |
| Claymation transitions (Seedance 1.5 Pro, Kling 3.0 Pro) | 3–4 s | 4 s ≈ 2.4 credits Kling 3.0 Pro, ≈ 1 credit Seedance 1.5 | [L56 01:00; 05:07; 07:36](../lessons/056-claymation-generating-videos-transitions.md) |
| Skeleton clips | 4 s in the example; "like 8" credits per 4 s Seedance 1.5 Pro | Push-in or small move only | [L39 00:58–01:28](../lessons/039-skeleton-generating-videos.md) |
| Kling 2.6 B-roll | 5 s (10 s "uses too many credits") | 3 credits per 5 s | [L30 00:00–00:34](../lessons/030-generate-realistic-ai-broll.md) |
| OpenArt Kling 2.6 start/end frame | 5 s, audio on/off | Alternative tool | [L64 00:37 frames](../lessons/064-workflow-breakdown.md); [L56 08:08 frame](../lessons/056-claymation-generating-videos-transitions.md) |
| Seedance 2.0 | 4–15 s per generation (skill fact) | Used for UGC segments and concept camera moves | [L20 skill, Seedance 2.0 Facts](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L40 00:57](../lessons/040-advanced-video-prompts.md) |
| Talking objects | Script length must fit clip length: Veo cut the line at 8 s; Kling at 10 s likely needed | "increase the length or shorten the script" | [L62 06:48–07:39](../lessons/062-talking-objects-tutorial.md) |

## Examples (cited)
| Shot | Frames supplied | Prompt / move | Result | Cite |
|---|---|---|---|---|
| Fruit juice fills the glass (Zack style) | Fruit still + woman-drinking still | "smooth sciencey transition where the juice from the fruit goes down to fill her glass" | Clip goes "from section to section" | [L66 00:55–01:59](../lessons/066-zack-d-films-generating-scenes-transitions.md) |
| Hangover-to-recovered (claymation) | Two clay frames | "The camera stays still as a star trail goes around the character from the bottom of his torso to the top of his head…" + suffix | Kling 3.0 Pro, 4 s, 2.4 credits | [L56 07:36 frame](../lessons/056-claymation-generating-videos-transitions.md) |
| Vomit, then shocked reaction | Image A first frame only; then last frame snapshotted as next first frame | "this person to vomit in the toilet", then "look shocked" | 4th or 5th attempt best | [L90 12:29–13:27](../lessons/090-ai-editing-2026-08-18.md) |
| Hazmat character shows the liver | Could not generate "shows the liver and drops it down" | Generated the reverse, reversed in the editor | Shot usable; last frame chained onward | [L90 16:01–17:05](../lessons/090-ai-editing-2026-08-18.md) |
| Burst into a new scene | Image B; Nano Banana removes everything but a solid background to make image A | First and last frame both supplied | Burst transition | [L90 20:40–21:12](../lessons/090-ai-editing-2026-08-18.md) |
| Camera through a room to a skeleton still | End on an existing still | "Camera zooms through the room and ends up with image one." Seedance 2.0, References, 7 s, 720p | Concept camera move | [L40 00:00–00:57](../lessons/040-advanced-video-prompts.md) |
| Crochet sniff → grimace | Start + end (Type B) | Character sniffs wrist, grimaces; camera locked; I2V closing line | Skill's worked example | [L45 Quality Bar](../lessons/045-claude-skill-setup-explanation.md) |

## Common mistakes
- End frame mid-motion ("hand reaching", "vapor mid-dissipation"): reclassify as Type A or push to the resolved state ([L45 Step 2](../lessons/045-claude-skill-setup-explanation.md)).
- Stacking camera moves or adding dialogue to an I2V prompt; the voiceover is recorded separately (skeleton skill, [L39 Agent use](../lessons/039-skeleton-generating-videos.md)).
- 10 s clips "just because": wasted credits and slow pacing ([L56 01:00](../lessons/056-claymation-generating-videos-transitions.md); [L30 00:00](../lessons/030-generate-realistic-ai-broll.md)).
- Leaving model audio on: costs credits and needs audio descriptions; SFX in the edit give "full control" ([L58 05:44](../lessons/058-editing-claymation-step-by-step.md)).
- Feeding a low-resolution snapshot as the next first frame: quality compounds down the chain ([L90 43:35](../lessons/090-ai-editing-2026-08-18.md)).
- Mismatched motion between adjacent clips ([L42 03:03](../lessons/042-skeleton-editing-the-video.md)).
- "Just generate and stitch the clips together" without post fixes ([L90 22:11](../lessons/090-ai-editing-2026-08-18.md)).

## Where it's taught
- Frame-type decision and I2V rules: [L45 skill Steps 2, §2.3, §4](../lessons/045-claude-skill-setup-explanation.md) · [L46 03:28; 06:16](../lessons/046-script-visualisation-image-creation.md)
- Claymation transitions: [L56 00:00–08:13](../lessons/056-claymation-generating-videos-transitions.md) · [L58 01:29–05:44](../lessons/058-editing-claymation-step-by-step.md)
- Zack-style chains: [L64 00:00–00:45](../lessons/064-workflow-breakdown.md) · [L65 00:52–02:45](../lessons/065-script-to-prompt-generator.md) · [L66 00:00–01:59](../lessons/066-zack-d-films-generating-scenes-transitions.md)
- Skeleton stills to clips: [L39 00:00–02:39](../lessons/039-skeleton-generating-videos.md) · [L40 00:00–00:57](../lessons/040-advanced-video-prompts.md) · [L42 03:03](../lessons/042-skeleton-editing-the-video.md)
- Narek's chaining, reversing, minimums: [L90 09:43–21:12; 29:24–32:07; 43:35–46:32; 1:00:46–1:01:50](../lessons/090-ai-editing-2026-08-18.md)
- Lip-sync slices with a start frame: [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md)
- Clip lengths: [L30 00:00](../lessons/030-generate-realistic-ai-broll.md) · [L62 06:48–07:39](../lessons/062-talking-objects-tutorial.md)

## Cross-course notes
- **Within this course (model choice):** Kling 3.0 Pro is "the best one for these" for skeleton ([L39 00:58](../lessons/039-skeleton-generating-videos.md)) and the final-quality model for claymation ([L56 06:10](../lessons/056-claymation-generating-videos-transitions.md)); Narek prefers Seedance over Kling for claymation because Kling "drifts a lot" ([L90 1:09:39–1:10:20](../lessons/090-ai-editing-2026-08-18.md)); in one crochet start/end test "Seedance 1.5 was better" than 2.0 and Kling was "way nicer" with no music ([L46 09:03](../lessons/046-script-visualisation-image-creation.md)). Agent default: test the same start/end pair on Seedance 1.5 Pro and Kling 3.0 Pro, keep whichever holds the character; all instructor claims, single tests.
- **Within this course (frame default):** the claymation lesson pairs every clip as start = scene N, end = scene N+1 ([L56 00:00–02:57](../lessons/056-claymation-generating-videos-transitions.md)); the crochet skill defaults to start frame only ([L45](../lessons/045-claude-skill-setup-explanation.md)). Agent default: Type B only when the shot must land in a different state or morph into the next scene; otherwise Type A.
- **Shared KB / other courses:** no other course in the KB covers image-to-video frame control; [Loom song-ad pipeline](../../../../resources/ai-song-ad-pipeline-loom.md) runs storyboard keyframes → per-shot clips with a review agent checking "bad hand physics" before rendering, the same stage order automated.

## Related
- [Character consistency](character-consistency.md) · [Reference-first prompting](reference-first-prompting.md) · [AI realism tells](ai-realism-tells.md) · [AI ad format catalog](ai-ad-format-catalog.md)
- [animated-ad-production-pipeline](../frameworks/animated-ad-production-pipeline.md) · [ai-post-production](../frameworks/ai-post-production.md) · [produce-an-animated-ai-ad](../playbooks/produce-an-animated-ai-ad.md) · [Prompts library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md)
