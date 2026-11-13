---
title: "Reference-first prompting: real references before prompts, @Image mapping, anti-cinematic vocabulary, describe it or the model invents it, one action arc per prompt"
type: concept
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (Camilo's Seedance 2.0 UGC Ad Director skill 020 and roasts 083–084; Narek 090; Caleb Kruse 093; other lessons unattributed)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/021-street-interviews.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/022-for-poppy-users.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/030-generate-realistic-ai-broll.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/033-sora-2-pro-hooks.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/039-skeleton-generating-videos.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/040-advanced-video-prompts.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/054-prompts-frames-chatgpt.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/056-claymation-generating-videos-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/062-talking-objects-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/064-workflow-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/066-zack-d-films-generating-scenes-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
tags: [prompting, references, pinterest, seedance, sora, anti-cinematic, realism, image-to-video, claude-skill]
updated: 2026-11-13
---

# Reference-first prompting
> Collect real visual references (creator look, location, props, product, the format you are imitating) before writing a single prompt, map each one to an `@Image` slot, then write the prompt as a director's brief: phone-camera vocabulary for UGC, every hand and surface described, one action arc per prompt. "Number one important thing is reference not your prompt" (Narek, [L90 11:31](../lessons/090-ai-editing-2026-08-18.md)).

## 🤖 Agent use
- **Use when:** writing any image or video generation prompt (Seedance, Sora 2 Pro, Kling, Nano Banana, Seedream, GPT Image 2), building a prompt-writing Claude skill, or diagnosing a generation that came out wrong.
- **Inputs → outputs:** approved script segment + format target (UGC phone footage / animated style / static) + rights-cleared references (generated creator, own product photos, location and prop photos, format examples) → a named reference set with `@Image` mapping + one prompt per segment (action, hands, expression, surface and what is absent, background, light, camera, audio) + an iteration log.
- **Rules:**
  - **DO** gather references before prompting: "We're basically thinking like a director who's giving… a Hollywood production team… what we want to create" ([L20 03:32](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); "if your reference is good, then prompt is bad, I think it will give you better results" ([L90 42:06](../lessons/090-ai-editing-2026-08-18.md)); "Context is everything" ([L93 10:45](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)).
  - **DO** use clean references only: "clean photos, no emojis, no watermarks" ([L20 01:46–02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); "Seedance recreates everything it sees as physical objects" (skill, [L20 Agent use](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
  - **DON'T** use references that are already AI-generated: "you can actually tell an AI one from a mile away" ([L18 01:54](../lessons/018-realistic-ai-podcasts-tutorial.md)); a member warns Pinterest now holds many AI images, TikTok search is another source ([L83 44:21](../lessons/083-ad-roast-calls-2026-08-17.md)).
  - **DO** map slots explicitly: `@Image1` = creator (same across all segments), `@Image2` = setting, `@Image3` = product (skill, [L20 Reference Image Mapping](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); Max Fusion's Seedance 2.0 takes up to nine images ([L20 04:03–05:01](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
  - **DO** supply a reference for anything specific the model cannot know: a drink, a garment, an on-screen ad; the skill "is not going to know what a good ad looks like" ([L40 00:57](../lessons/040-advanced-video-prompts.md)).
  - **DO** describe everything you need and what must not be there: "If you don't describe it, Seedance invents it — and you get random artifacts" (skill, [L20 Detail Level](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); Seedance 2.0 "follows everything to the T" ([L20 11:28](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md), instructor claim).
  - **DO** keep one action arc per prompt: "don't describe two scene changes in one prompt" (skill, [L20 Seedance 2.0 Facts](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); "One camera move + one action per clip — don't stack moves" ([L39 frame 02:36](../lessons/039-skeleton-generating-videos.md)); edit images in stages, since doing too much in one go "looked weird" ([L18 07:40](../lessons/018-realistic-ai-podcasts-tutorial.md)).
  - **DON'T** use cinematic vocabulary for UGC: "NEVER use the word 'cinematic' anywhere" (skill rule 3, [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); realism prompts exclude "cinematic, professional, studio, perfect" ([L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)).
  - **DO** name the video format for Sora 2 Pro ("selfie FaceTime video", "TikTok video", "get ready with me video"), or results are "really weird videos" ([L25 00:00–00:58](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md), instructor claim); describe the vibe, not "full JSON" ([L33 01:22](../lessons/033-sora-2-pro-hooks.md)).
  - **IF** a generation is close **THEN** edit the prompt and Remix, or edit the image conversationally ("make him look even more sad"), rather than rebuilding ([L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L46 05:18](../lessons/046-script-visualisation-image-creation.md)); **IF** a prop fails twice **THEN** cut it ([L20 09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
- **See also:** [AI realism tells](ai-realism-tells.md) · [Character consistency](character-consistency.md) · [Start/end-frame video](start-end-frame-video.md) · [Prompts library](../libraries/prompts.md) · [AI UGC Seedance workflow](../frameworks/ai-ugc-seedance-workflow.md) · [AI creator compliance](ai-creator-compliance.md)

## Definition
Reference-first prompting is a production order: **references decide identity, look and composition; the prompt decides action, camera, audio and exclusions.** The course's skills encode it: the Seedance 2.0 UGC Ad Director returns Pinterest searches for the creator and each scene before any prompt ([L20 00:54–03:32](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); Narek builds avatar, object and style sheets before generating clips and passes them in reference-to-video mode ([L90 10:14–11:31](../lessons/090-ai-editing-2026-08-18.md)); David builds style skills from extracted frames of a reference ad ([L91 07:44–14:49](../lessons/091-special-guest-recordings-ai-office-hours-david.md)).

## Why it matters
- Text alone cannot pin a face, a pack or a camera feel; references can. Narek ranks references above prompt wording ([L90 11:31; 42:06](../lessons/090-ai-editing-2026-08-18.md)).
- Modern video models obey literally: Seedance 2.0 rendered the wrong straws, stemless and empty glasses and odd hand actions because the prompt left them open ([L20 06:41–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
- Vocabulary sets the look: "cinematic", camera brands and film terms push UGC toward a produced look that reads as an ad ([L20 Anti-Cinematic Rules](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); "lazy prompt 'make me an influencer'" gives a smooth, symmetrical face and blurred background ([L93 34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)).
- References from the real format (a real street interview, a real niche podcast setup) carry the authenticity cues that prompts miss: ambient sound, mic handling, framing ([L21 00:00–00:47](../lessons/021-street-interviews.md); [L18 00:55](../lessons/018-realistic-ai-podcasts-tutorial.md)).

## How to use (steps)
1. **Read the segment like a shoot.** List who, where, props, product placement, camera, audio, and what must not appear ([L20 05:01](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
2. **Collect references per slot.** Creator (generated or licensed; see [compliance](ai-creator-compliance.md) row 1), location, props, product (2+ own photos, [L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)), and one example of the format (real interview, real podcast frame) for composition only. Pinterest searches: demographic + action + setting (skill URL format, [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); "more like this" to get closer ([L20 02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); YouTube Shorts to see what the niche watches ([L18 00:55](../lessons/018-realistic-ai-podcasts-tutorial.md)).
3. **Clean and name.** No emoji, watermark, text overlay, app UI; product images with no background where possible ([L25 02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md)); file names like "creator", "kitchen counter reference" ([L20 02:35–03:32](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
4. **Map slots.** Upload, then reference with `@Image1…` in the prompt; describe the source then the change for swaps ("video one is an ad of a man testing a pillow… replace the man for the woman in image one", [L16 01:31](../lessons/016-clone-broll-ugc-ads.md)).
5. **Write the prompt by block.** Per 5-second block, 3–4 sentences: each hand, exact facial expression, what is on the surface and what is not, background, light source and direction (skill, [L20 Detail Level](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)). Describe in third person ("she is doing this"), not commands ([L62 05:52](../lessons/062-talking-objects-tutorial.md)). Add audio: voice matched to demographic, room tone matched to the setting, natural speech with fillers (skill, [L20 Audio Direction](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
6. **Pick vocabulary for the target** (table below).
7. **Keep one action arc.** Split a second scene change into the next segment or clip.
8. **Generate, read, Remix.** Change one thing per round (camera moves, missing reference, removed prop) and log it ([L20 06:41–11:28](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).

### Vocabulary by target (stage-specific)
| Target | Use | Avoid | Cite |
|---|---|---|---|
| AI UGC video (Seedance, Sora) | `iPhone handheld`, `natural lighting` / `window light`, `UGC style`, `slight camera shake`, `casual`, `authentic`, `9:16`; name the format ("TikTok video", "get ready with me") | `cinematic`, ARRI/RED/Blackmagic, `anamorphic`, `film grain`, `dramatic lighting`, `whip pan`, `dolly`, `gimbal`, `bokeh`, `epic`, `stunning`, `slow motion` | [L20 Anti-Cinematic Rules](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L25 00:00](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| Realistic people stills | "visible pores, real skin texture, underlying shadows, mouth open, a few blemishes", natural light, iPhone feel; "candid photo, TikTok style with uneven angles, as if a friend was recording it" | "cinematic, professional, studio, perfect" | [L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L83 43:20](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Claymation I2V | `[visual] + [camera] + Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon.` | "Disney", "cartoon" as positives | [L56 01:58](../lessons/056-claymation-generating-videos-transitions.md) |
| Crochet diorama | Frame the world as a "stop-motion diorama"; universal positive, negative and I2V closing line | "knitted skin" directly; complex finger poses; "CGI render, Pixar style… studio lighting" (negative list) | [L45 §2, §4](../lessons/045-claude-skill-setup-explanation.md) |
| Skeleton (animated) | The chosen style's character bible verbatim; default style "Bare-Bones Cinematic" (photoreal cinematic world) | Changing the bible mid-ad; dialogue in video prompts | [L37 Style Library; Stage 3](../lessons/037-install-skill-generate-script.md) |
| Claymation stills | Subject + clay material + foreground/midground/background + lighting + "vertical 9:16" + "handcrafted tabletop diorama… stop-motion aesthetic" + fixed negative | Effect elements you will animate later (remove them first) | [L54 01:54; prompt pattern](../lessons/054-prompts-frames-chatgpt.md) |
| Zack-style 3D | Short concept; "you don't have to be super detailed" | Over-prompting transitions (one sentence) | [L64 02:52](../lessons/064-workflow-breakdown.md); [L66 Agent use](../lessons/066-zack-d-films-generating-scenes-transitions.md) |
| B-roll (Kling) | One simple action: "girl observes her jewelry" | Multi-step action | [L30 00:40](../lessons/030-generate-realistic-ai-broll.md) |

"Cinematic" is therefore not banned course-wide: it is banned for UGC and clay/yarn styles and is the default look for the skeleton "Bare-Bones Cinematic" style.

## Examples (cited)
| Generation | What the prompt or reference lacked | Fix | Cite |
|---|---|---|---|
| Gratsi taste test, attempt 1 | Hand actions, prop (cardboard with straws) undefined | Attempt 2: "multiple shots", hand places the bill, pan up; new prop reference | [L20 06:41–09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Gratsi attempt 2 | Stemless and empty glasses, product inconsistency | Removed the prop, showed box and bottle being poured: "I think it'll even convert better" (instructor claim) | [L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Street interview | Emoji added in the prompt "kind of didn't work" | Emojis, subtitles and black-and-white added in the edit instead | [L21 04:12](../lessons/021-street-interviews.md) |
| Skeleton holds a specific ad | Skill could not know the visual | Image step first with a screenshot reference, then animate | [L40 00:57](../lessons/040-advanced-video-prompts.md) |
| Podcast set | Trying all edits in one prompt "looked weird" | Separate edits: face, plant, background colour, clothes | [L18 04:11; 07:40](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| Talking object monologue | Commanding phrasing | "Speaks as an American female in an agitated/threatened way" (third person) | [L62 05:52](../lessons/062-talking-objects-tutorial.md) |

## Common mistakes
- Prompting first and searching references afterwards; the skill's order is references, then prompts ([L20 01:46–05:01](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
- Using the Claude skill without checking it actually ran: "if it's not doing that and it's just giving you an output it's wrong, you need to try again" ([L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); also [L46 01:31](../lessons/046-script-visualisation-image-creation.md)).
- Letting the LLM decide every visual: Narek takes the LLM's idea and adds his own; he claims no LLM would have produced his hazmat-suit idea ([L90 1:06:22–1:08:51](../lessons/090-ai-editing-2026-08-18.md)).
- Uploading face images to Sora 2 Pro or Arcads Video: render fails and may flag the account ([L25 Agent use](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md); [L33 01:23 frame](../lessons/033-sora-2-pro-hooks.md)).
- Faces of real people as references (likeness); see [compliance](ai-creator-compliance.md).
- Over-specifying with JSON for Sora: "very specific, but also not too specific… not full JSON prompt… the overall vibe" ([L33 01:22](../lessons/033-sora-2-pro-hooks.md)).

## Where it's taught
- Seedance 2.0 UGC Ad Director skill (full rules): [L20 00:54–13:33; skill file](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L22 skill text in Poppy](../lessons/022-for-poppy-users.md) · [L21 00:00–04:12](../lessons/021-street-interviews.md)
- References first, sheets, reference-to-video: [L90 09:43–11:31; 42:06; 1:06:22](../lessons/090-ai-editing-2026-08-18.md) · [L93 10:45–12:53; 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) · [L91 07:44–14:49](../lessons/091-special-guest-recordings-ai-office-hours-david.md)
- Reference sourcing and AI-reference warning: [L18 00:00–01:54](../lessons/018-realistic-ai-podcasts-tutorial.md) · [L83 42:50–44:21](../lessons/083-ad-roast-calls-2026-08-17.md)
- Supplying references for specifics: [L40 00:00–00:57](../lessons/040-advanced-video-prompts.md) · [L76 02:48–03:44](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)
- Format words and vibe prompting for Sora: [L25 00:00–02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) · [L33 01:22–04:36](../lessons/033-sora-2-pro-hooks.md)
- Style-specific vocabularies: [L37](../lessons/037-install-skill-generate-script.md) · [L45](../lessons/045-claude-skill-setup-explanation.md) · [L54](../lessons/054-prompts-frames-chatgpt.md) · [L56 01:00–01:58](../lessons/056-claymation-generating-videos-transitions.md) · [L64 02:52](../lessons/064-workflow-breakdown.md) · [L30 00:40](../lessons/030-generate-realistic-ai-broll.md)
- Third-person direction: [L62 05:52](../lessons/062-talking-objects-tutorial.md)

## Cross-course notes
- **Within this course (detail level):** the Seedance skill demands 3–4 sentences per 5 s block ([L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); the Zack-style lesson says "you don't have to be super detailed" ([L64 02:52](../lessons/064-workflow-breakdown.md)); Sora 2 Pro wants simple prompts plus the format name ([L25 00:00](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md)); Narek ranks references over prompt quality ([L90 42:06](../lessons/090-ai-editing-2026-08-18.md)). Agent default: references carry identity and look; prompt detail scales with how literal the model is (long for Seedance 2.0 UGC, short for Sora hooks and 3D transitions).
- **RMBC II:** the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) applies to spoken lines inside video prompts, because Seedance and Sora render dialogue written in the prompt.
- **Shared KB:** [Tether Lab model-image psychology](../../../../concepts/model-image-psychology.md) and [native advertising](../../../../concepts/native-advertising.md) explain why a native, unpolished look matters; this page is the production method for getting it from generators.

## Related
- [AI realism tells](ai-realism-tells.md) · [Character consistency](character-consistency.md) · [Start/end-frame video](start-end-frame-video.md) · [AI ad format catalog](ai-ad-format-catalog.md) · [AI creator compliance](ai-creator-compliance.md)
- [ai-ugc-seedance-workflow](../frameworks/ai-ugc-seedance-workflow.md) · [claude-code-ad-operator](../frameworks/claude-code-ad-operator.md) · [Prompts library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md)
