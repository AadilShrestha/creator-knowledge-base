---
title: "Character consistency: one AI creator or character, the same face, body, product and voice across every clip"
type: concept
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (Camilo in 020, 045–046 and 084; Narek 090; David 091; Caleb Kruse 093; other lessons unattributed)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/015-change-creators-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/021-street-interviews.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/027-consistent-voices-method-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/028-consistent-voices-method-2.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/029-make-ai-creators-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/038-skeleton-generating-images.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/054-prompts-frames-chatgpt.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/055-prompts-frames-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/056-claymation-generating-videos-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/065-script-to-prompt-generator.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/066-zack-d-films-generating-scenes-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/088-ad-psychology-with-howie-2026-07-29.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
tags: [character-consistency, character-bible, character-sheet, reference-images, frame-chaining, voice-consistency, nano-banana, seedance, elevenlabs]
updated: 2026-11-13
---

# Character consistency
> Video and image models redraw a person or character from scratch on every generation, so consistency comes from what you feed them, not from repeating the prompt: lock one reference image (or a multi-angle character sheet plus a verbatim character bible), edit from it instead of regenerating, chain clips through their last frames, and make the voice from one source in one pass.

## 🤖 Agent use
- **Use when:** any AI ad shows the same person, mascot or product in more than one clip or still (AI UGC segments, rizz-model chain, podcast speakers, skeleton, crochet, claymation, talking objects, Zack-style scenes).
- **Inputs → outputs:** an approved, rights-cleared creator or character (generated from text or licensed) + product photos + script segments → a locked reference set (hero image or character sheet, product reference group, character bible text, voice ID) + per-clip generation inputs that carry it + a QA check per clip.
- **Rules:**
  - **DO** generate the hero image or character sheet first and wait for it; every later shot references it: "even if we prompt it exactly the same… there will be some differences" without the reference ([L38 01:52–02:50](../lessons/038-skeleton-generating-images.md)).
  - **DO** paste the locked character bible text into every image prompt word for word; "Don't change the skeleton's look, eyes, or proportions mid-ad" (skeleton skill, [L37 Stage 3](../lessons/037-install-skill-generate-script.md)).
  - **DO** build a multi-angle character sheet (same outfit and body) when the character must appear from different angles ([L93 27:54–29:24](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)); Narek builds an avatar sheet plus object sheets before any clip ([L90 11:00–11:31](../lessons/090-ai-editing-2026-08-18.md)).
  - **DO** edit from the reference instead of regenerating from text: "you just want to change it to editing so that you get the same consistency" ([L54 02:26–02:56](../lessons/054-prompts-frames-chatgpt.md)); "the character will change" otherwise ([L54 02:26](../lessons/054-prompts-frames-chatgpt.md)).
  - **DO** carry a person into the next segment by extracting a frame from the approved clip and using it as the new reference ([L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L90 12:29; 17:40](../lessons/090-ai-editing-2026-08-18.md)); sharpen a blurry snapshot first ([L90 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md)).
  - **DO** add "Keep character facial consistency. No character redesign. No facial feature changes." to every image-to-video prompt with a character ([L56 01:00](../lessons/056-claymation-generating-videos-transitions.md)).
  - **DO** make the voice once: write the whole script, generate the whole voiceover in one pass, then slice; "voice models are not consistent… different accents… different pacing… entirely different voices" when generated in pieces (David, [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md)).
  - **IF** you must generate audio per clip (Seedance native dialogue) **THEN** prompt the full voice spec every time: accent, speed, mic sound, echo, volume change off the mic ([L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md)).
  - **DON'T** re-prompt Sora 2 Pro for the same person: "You can't use the same face even if you prompt it the same way" ([L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md)); move to stills ([L26](../lessons/026-character-consistency.md)).
  - **DON'T** lock a real person's face or voice as the reference: generated or licensed only ([AI creator compliance](ai-creator-compliance.md) rows 1, 9).
- **See also:** [Start/end-frame video](start-end-frame-video.md) · [Reference-first prompting](reference-first-prompting.md) · [AI realism tells](ai-realism-tells.md) · [Animated ad production pipeline](../frameworks/animated-ad-production-pipeline.md) · [Rizz-model pipeline](../frameworks/rizz-model-ai-ugc-pipeline.md) · [ElevenLabs](../../../../tools/elevenlabs.md)

## Definition
Character consistency = the same identity (face shape, skin, hair, body, outfit or bone/yarn/clay style), the same product (pack, label, colour) and the same voice (timbre, accent, pace, mic sound) across every generated clip and still in one ad. The course treats it as an input problem: the model cannot remember, so you hand it the same visual and audio anchors each time.

## Why it matters
- Viewers must recognise that every clip is the same person: Camilo's rizz edit shows the creator's face many times, "Don't just cut to other B-roll" ([L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
- Drift reads as AI and breaks the story; Narek: Kling "drifts a lot", Seedance has fewer minor-detail errors ([L90 1:09:39–1:10:20](../lessons/090-ai-editing-2026-08-18.md), instructor claim).
- Product drift is a claim risk: wrong glasses, empty glasses and an inconsistent product forced re-prompts in the Gratsi build ([L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); Poppy statics need several product images "so generated ads match the real pack" ([L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)).
- Voice drift is the most audible tell: "you don't want anything to sound like a bot including the audio" ([L28 01:43](../lessons/028-consistent-voices-method-2.md)).

## How to use (steps)
1. **Create the identity once.** Generated from a text description (age, look, wardrobe), or a licensed image. For animated styles use the skill's character bible ([L37 Stage 3](../lessons/037-install-skill-generate-script.md); crochet skill Step 0, [L45](../lessons/045-claude-skill-setup-explanation.md)). Base the description on the research avatar: "Make sure don't make things up" ([L46 01:31](../lessons/046-script-visualisation-image-creation.md)).
2. **Make the anchor image.** Hero image (neutral full-body, even light, plain background) for animated characters ([L38 01:52](../lessons/038-skeleton-generating-images.md)); multi-angle character sheet for realistic people ([L93 27:54](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md)). Save as "character reference" with a clear file name ([L20 02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L26 00:47](../lessons/026-character-consistency.md)).
3. **Make the product anchor.** Two or more product photos grouped as "image references" ([L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)); attach to every frame where the product appears ([L46 07:15; 08:14](../lessons/046-script-visualisation-image-creation.md)).
4. **Place the character in each scene by editing, not regenerating.** Nano Banana Pro edit: "replace the girl on the street for the middle-aged woman and change the background to be New York" ([L26 01:45](../lessons/026-character-consistency.md)); or image-editing mode with the reference + scene prompt ([L54 02:26–02:56](../lessons/054-prompts-frames-chatgpt.md)); or Poppy: disconnect old reference, connect the first character image, add "Keeping the character the same" ([L55 05:02–05:50](../lessons/055-prompts-frames-poppy-method.md)).
5. **Chain states.** For the next state of the same scene, make a variation of the previous image and describe only what changes ([L65 01:48–02:45](../lessons/065-script-to-prompt-generator.md); [L66 00:00–00:55](../lessons/066-zack-d-films-generating-scenes-transitions.md)).
6. **Animate with the anchors attached.** Seedance 2.0: `@Image1` = creator, same across all segments ([L20 skill, Reference Image Mapping](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); I2V prompts carry the consistency sentence ([L56 01:00](../lessons/056-claymation-generating-videos-transitions.md)).
7. **Chain clips.** Extract the last (or a clean) frame of the approved clip as the next clip's reference or first frame; sharpen first if blurry ([L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L90 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md)).
8. **Lock the voice.** Pick one voice route (table below), generate the full voiceover in one pass, slice per clip.
9. **QA** each clip against the anchors: face, outfit, product label, voice. Regenerate or remix; don't hide drift with cuts unless the face stays recognisable ([L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).

### Visual consistency methods
| Method | How | Best for | Cite |
|---|---|---|---|
| One reference image reused | Same creator image as `@Image1` in every Seedance segment | AI UGC, street interview | [L20 skill; 04:03–05:01](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L21 02:15–03:13](../lessons/021-street-interviews.md) |
| Character bible + hero image | Locked text block pasted verbatim into every prompt + hero image as reference | Skeleton and other mascots | [L37 Stage 3](../lessons/037-install-skill-generate-script.md); [L38 01:52–03:20](../lessons/038-skeleton-generating-images.md) |
| Character / avatar sheet | Multi-angle sheet, same outfit and body; also object and style sheets | Realistic people across angles; reference-to-video | [L93 27:54–29:24](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L90 10:14–11:31](../lessons/090-ai-editing-2026-08-18.md); [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Edit, don't regenerate | Switch to image editing with the first character image as reference | Claymation, crochet, any still series | [L54 02:26–02:56](../lessons/054-prompts-frames-chatgpt.md); [L55 05:02–05:50](../lessons/055-prompts-frames-poppy-method.md); [L46 05:18; 07:15](../lessons/046-script-visualisation-image-creation.md) |
| Variation of previous image | Three-dot menu → Generate variation, then describe only the next state | Zack-style scene chains | [L65 01:48–02:45](../lessons/065-script-to-prompt-generator.md); [L66 00:00–00:55](../lessons/066-zack-d-films-generating-scenes-transitions.md) |
| Frame extraction | Save a frame from the approved clip as the next reference or first frame | Multi-segment UGC; animated chains | [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L90 12:29; 17:40](../lessons/090-ai-editing-2026-08-18.md) |
| Same-pose edit of a source frame | Screenshot the original frame, edit the face, keep the pose | Creator swap on our own footage | [L15 00:03–01:38](../lessons/015-change-creators-with-ai.md) |
| Mirrored second speaker | Flip speaker A's edited image and change identity so both face each other | Two-person podcast | [L18 06:02–06:56](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| Consistency sentence in I2V | "Keep character facial consistency. No character redesign. No facial feature changes." | Every animated clip with a character | [L56 01:00](../lessons/056-claymation-generating-videos-transitions.md) |
| Model-specific locks | Nano Banana 2: attach hero, "keep its exact face, eyes, and bone style"; GPT image: same chat; Midjourney `--cref … --cw 100`, `--sref`, `--seed` | When switching image tools | [L37 Stage 3 table](../lessons/037-install-skill-generate-script.md) |

### Voice consistency methods
| Method | When | Settings / steps | Cite |
|---|---|---|---|
| ElevenLabs instant clone of the hook audio | Generated hook ≥ about 10 s (Sora 12 s) | Export audio only (video files capped at 10 MB); skip music cleanup on clean clips; name and save | [L27 00:00–01:46](../lessons/027-consistent-voices-method-1.md) |
| ElevenLabs Voice Design | Hook too short to clone (8 s) or no source | Describe age, country, speed, background; compare 3 previews to the hook; Enhance (alpha) | [L28 00:00–01:43](../lessons/028-consistent-voices-method-2.md) |
| One-pass voiceover, then slice | Lip-sync or voiceover ads with many clips | Whole script → whole VO → remove dead air → slice → slice + start frame per clip | [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md); [L90 05:06–07:00](../lessons/090-ai-editing-2026-08-18.md) |
| Full voice spec in every prompt | Native-audio models generating per clip (Seedance 2.0) | Accent, speed, mic sound, echo, volume change off-mic, delivery; test with ~5 s clips | [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md); [L20 skill, Audio Direction](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Same project in one tool | Google Flow / Omni talk-show build (member) | Same Flow project "helped keep voice consistent" | [L84 20:43–22:37](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Saved voice into lip-sync | Rizz talking clips | Choose the saved ElevenLabs voice, v3 alpha, emotion tags per line | [L29 01:41](../lessons/029-make-ai-creators-talk.md) |

## Examples (cited)
| Build | Consistency problem | Fix used | Cite |
|---|---|---|---|
| Rizz jewelry ad | Sora 2 Pro won't regenerate the hook face | Recreate the character as stills (Nano Banana Pro), then Rizz lip-sync | [L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md); [L26 01:45–02:15](../lessons/026-character-consistency.md) |
| Gratsi segment 2 | New segment must match the creator | Frame extracted from segment 1; prompt "same person, slightly closer to the shot" | [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Skeleton community ad | Skeleton changed between shots | Hero first; character bible + scene section + hero node per shot: "the character looking consistent… exactly what we wanted" | [L38 02:11–03:20](../lessons/038-skeleton-generating-images.md) |
| Crochet ad | Forgot the character reference once "and it didn't look as good"; forgot the product once | Always attach both references | [L46 08:14–09:03](../lessons/046-script-visualisation-image-creation.md) |
| Claymation hangover scene | Face and bedroom differed between hungover and recovered shots | Re-ran with the first character image connected, "Keeping the character the same" | [L55 05:02–05:55](../lessons/055-prompts-frames-poppy-method.md) |
| Wooden-utensils story ad | Plastic-looking character | Character sheet "as realistic as possible", Nano Banana Pro over GPT Image (Camilo's preference) | [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) |

## Common mistakes
- Re-typing the same prompt and expecting the same face ([L38 02:11–02:50](../lessons/038-skeleton-generating-images.md); [L54 02:26](../lessons/054-prompts-frames-chatgpt.md)).
- Pasting the skill's character description as a generation prompt: "This isn't a prompt. Don't use it as a prompt. It doesn't work." ([L46 01:31](../lessons/046-script-visualisation-image-creation.md)).
- Generating the voiceover clip by clip, so accent and pace change ([L91 50:13](../lessons/091-special-guest-recordings-ai-office-hours-david.md)).
- Applying the ElevenLabs cleanup to a clip with no music: it "actually ruins" it ([L27 00:47](../lessons/027-consistent-voices-method-1.md)).
- Swapping the face but not the voice: a gender swap keeps the source voice ([L15 01:38–02:29](../lessons/015-change-creators-with-ai.md)).
- Wide-open-mouth source stills for lip-sync: "P" words break; pick closed-mouth stills ([L29 03:37](../lessons/029-make-ai-creators-talk.md)).
- Locking a stranger's face from Pinterest as the creator reference ([L20 01:46](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) as taught); see [compliance](ai-creator-compliance.md) row 1.

## Where it's taught
- Reference image and frame chaining in AI UGC: [L20 01:46–05:01; 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L21 01:45–03:13](../lessons/021-street-interviews.md) · [L26 00:47–02:15](../lessons/026-character-consistency.md) · [L24 00:48](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md) · [L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md)
- Character bible and hero image: [L37 Stage 3](../lessons/037-install-skill-generate-script.md) · [L38 00:00–03:20](../lessons/038-skeleton-generating-images.md)
- Crochet character reference: [L45 skill Step 0](../lessons/045-claude-skill-setup-explanation.md) · [L46 01:31; 02:37; 05:18; 07:15–09:03](../lessons/046-script-visualisation-image-creation.md)
- Edit-from-reference stills: [L54 02:26–02:56](../lessons/054-prompts-frames-chatgpt.md) · [L55 05:02–05:50](../lessons/055-prompts-frames-poppy-method.md) · [L65 01:48–02:45](../lessons/065-script-to-prompt-generator.md) · [L66 00:00–00:55](../lessons/066-zack-d-films-generating-scenes-transitions.md)
- I2V consistency sentence: [L56 01:00](../lessons/056-claymation-generating-videos-transitions.md)
- Sheets: [L90 10:14–11:31](../lessons/090-ai-editing-2026-08-18.md) · [L93 27:54–30:14](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) · [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md)
- Product references: [L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L46 08:14](../lessons/046-script-visualisation-image-creation.md) · [L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)
- Voice: [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md) · [L27 00:00–01:46](../lessons/027-consistent-voices-method-1.md) · [L28 00:00–01:43](../lessons/028-consistent-voices-method-2.md) · [L29 01:41; 03:37](../lessons/029-make-ai-creators-talk.md) · [L84 20:43–22:37](../lessons/084-ad-roast-calls-2026-08-21.md) · [L90 05:06–07:00](../lessons/090-ai-editing-2026-08-18.md) · [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md) · [L88 page](../lessons/088-ad-psychology-with-howie-2026-07-29.md)
- Edit-level recognition: [L31 02:44–04:39](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)

## Cross-course notes
- **Within this course (disagreement on image model):** Narek prefers Nano Banana for avatars (GPT Image 2 results "so dark") and GPT Image 2 for storyboards ([L90 07:58; 08:44](../lessons/090-ai-editing-2026-08-18.md)); the claymation lessons say Nano Banana 2 beats Nano Banana Pro ([L54 00:55](../lessons/054-prompts-frames-chatgpt.md); [L55 02:17](../lessons/055-prompts-frames-poppy-method.md)); the UGC, podcast, static and roast lessons prefer Nano Banana Pro for realism ([L15 00:03–00:59](../lessons/015-change-creators-with-ai.md); [L26 02:15](../lessons/026-character-consistency.md); [L76 05:37–06:27](../lessons/076-new-make-static-ads-with-ai-poppy-method.md); [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md)). Agent default: Nano Banana Pro for realistic people and product packs; Nano Banana 2 or Seedream for stylised clay/yarn worlds; always test two models on the hero image before batching. All instructor claims at recording.
- **Within this course (voice route):** the Seedance UGC skill says "NEVER tell users to add voiceover in post" because Seedance lip-syncs natively ([L20 skill rule 2](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); David says to generate the whole voiceover in one pass because voice models drift between generations ([L91 50:13](../lessons/091-special-guest-recordings-ai-office-hours-david.md)); the skeleton skill keeps dialogue out of video prompts ([L39 Agent use](../lessons/039-skeleton-generating-videos.md)). Agent default: one-pass voiceover for any ad longer than one clip; native Seedance dialogue only for single-segment hooks, with the full voice spec repeated.
- **Shared KB:** no other course in the KB teaches AI character consistency; [AI UGC tools](../../../../tools/ai-ugc-tools.md) and [ElevenLabs](../../../../tools/elevenlabs.md) cover the tools only.

## Related
- [Start/end-frame video](start-end-frame-video.md) · [Reference-first prompting](reference-first-prompting.md) · [AI realism tells](ai-realism-tells.md) · [AI creator compliance](ai-creator-compliance.md) · [AI ad format catalog](ai-ad-format-catalog.md)
- [ai-ugc-seedance-workflow](../frameworks/ai-ugc-seedance-workflow.md) · [rizz-model-ai-ugc-pipeline](../frameworks/rizz-model-ai-ugc-pipeline.md) · [animated-ad-production-pipeline](../frameworks/animated-ad-production-pipeline.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [Prompts library](../libraries/prompts.md)
