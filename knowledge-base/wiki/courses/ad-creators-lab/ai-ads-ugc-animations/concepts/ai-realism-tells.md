---
title: "AI realism tells: what makes AI ads look and sound fake, and the generation and edit fixes"
type: concept
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (Camilo in 020, 031 where probable, and roasts 083–084; Narek 090; Caleb Kruse 093; Hao/Howie 088 page summary; other lessons unattributed)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/011-native-social-titles-premiere-pro-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/012-make-ai-look-less-fake.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/013-live-edit.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/019-realistic-ai-ugc-the-ad-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/021-street-interviews.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/027-consistent-voices-method-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/028-consistent-voices-method-2.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/029-make-ai-creators-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/033-sora-2-pro-hooks.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/034-fashion-clothing-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/041-skeleton-generating-voices.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/057-claymation-generating-voice-over.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/062-talking-objects-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/071-making-statics-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/073-fixing-bad-static-ads-10-51.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/088-ad-psychology-with-howie-2026-07-29.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/104-bad-ugc.md
tags: [realism, ai-tells, audio, room-tone, camera-shake, skin, hands, on-screen-text, green-screen, posterize-time, captions, safe-zone, qa]
updated: 2026-11-13
---

# AI realism tells
> The specific cues that make viewers read an ad as AI (too-perfect audio, no room tone, locked-off camera, plastic skin, broken hands, garbled text, dead-on flat framing, over-designed captions) and the course's fix for each, at prompt time and in the edit; use it as a QA list, and never as a way to hide synthetic people where disclosure is required.

## 🤖 Agent use
- **Use when:** reviewing a generated clip or still before it enters the edit; briefing an editor on "make it look organic"; writing realism language into prompts; final QA before launch.
- **Inputs → outputs:** raw clips and stills + the voice track + captions → a tell-by-tell verdict (pass / regenerate / fix in edit / hide with a cutaway) and the fix applied; feeds the [AI video QA checklist](../rubrics/ai-video-qa-checklist.md).
- **Rules:**
  - **DO** design the audio, not just the picture: AI interviews fail because "the mic is too perfect. There's no street sound… it just sounds like AI" ([L21 00:00](../lessons/021-street-interviews.md)); prompt room tone that matches the setting (skill, [L20 Audio Direction](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
  - **DON'T** ship a perfect "podcasty" narrator on a story ad: it breaks believability ([L84 27:34–28:27](../lessons/084-ad-roast-calls-2026-08-21.md)); "If it sounds like a YouTuber shouting → it's wrong. If it sounds like a documentary → you're close." (claymation page, [L57](../lessons/057-claymation-generating-voice-over.md)).
  - **DO** grade AI footage down: contrast "to nothing", saturation slightly down, sharpen to about 12, a little Faded Film, plus a subtle Wiggle shake ([L12 01:01–02:57](../lessons/012-make-ai-look-less-fake.md)); static AI shots "look a bit weird" ([L12 02:57](../lessons/012-make-ai-look-less-fake.md); [L31 06:41–07:38](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
  - **DO** prompt real skin: "visible pores, real skin texture, underlying shadows, mouth open, a few blemishes"; never "cinematic, professional, studio, perfect" ([L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)).
  - **DO** keep framing imperfect: "candid photo, TikTok style with uneven angles, as if a friend was recording it" ([L83 43:20](../lessons/083-ad-roast-calls-2026-08-17.md)); dead-on flat angles "give away" AI ([L83 44:21](../lessons/083-ad-roast-calls-2026-08-17.md)).
  - **DO** check hands, props and every spoken word in every take: the first Seedance take had wrong hand actions and words that "don't really make sense" ([L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); avoid complex finger poses in stylised worlds ([L45 §4](../lessons/045-claude-skill-setup-explanation.md)).
  - **DO** remove generated on-screen text from video (Sora adds it; Vmake removes it) ([L25 01:32](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md)) and add all captions, emojis and effects in the edit, not the generation ([L21 04:12](../lessons/021-street-interviews.md); [L42 Agent use](../lessons/042-skeleton-editing-the-video.md)).
  - **DO** keep an imperfect AI talking head small and moving: green-screen it into a bottom corner over B-roll, and cut away from bad seconds ([L31 03:48–04:39; 06:41](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
  - **DON'T** add transitions, VFX or risers to AI UGC: "I wanted it to look like a video that a creator actually made" ([L31 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
  - **DON'T** use realism to deceive: mixing real footage in to prevent "subtle thoughts that this is an AI video" ([L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)) is a disclosure problem; see [AI creator compliance](ai-creator-compliance.md) row 37.
- **See also:** [Reference-first prompting](reference-first-prompting.md) · [Character consistency](character-consistency.md) · [AI post-production](../frameworks/ai-post-production.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [Shared native advertising](../../../../concepts/native-advertising.md)

## Definition
A **realism tell** is any visual, audio or text cue that tells a viewer "this was generated" or "this is an ad" before the message lands. The course's target is phone-filmed realism, "not plastically" polished output, "avoiding SLOP" ([L19 page](../lessons/019-realistic-ai-ugc-the-ad-we-are-making.md)). Tells come from three layers: generation (what the model drew or said), audio (voice and room), and the edit (grade, motion, captions, framing).

## Why it matters
- Hao: "make your ad look as organic as possible"; the ad itself is a schema the viewer filters out ([L86 23:56–24:54](../lessons/086-ad-psychology-with-howie-2026-08-12.md)). AI tells trigger that filter faster than any ad tell.
- Narek: "editing is… the only tool that will make the AI generations less AI sloppy" ([L90 22:11](../lessons/090-ai-editing-2026-08-18.md)).
- Native-looking captions matter: drop shadows, wrong fonts or a line through the middle make the ad "look like ads" instead of organic content ([L11 Agent use, page](../lessons/011-native-social-titles-premiere-pro-1.md)).

## How to use (steps)
1. **Prompt time.** Use phone-camera vocabulary and realism keywords; prompt room tone and two distinct voices for interviews; name the organic format for Sora; keep references free of AI images ([reference-first prompting](reference-first-prompting.md)).
2. **Per-take QA.** Watch each take for the tells in the table; regenerate or remix anything with broken hands, wrong props or wrong words. Generate several versions as standard ([L25 02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md); [L90 12:29](../lessons/090-ai-editing-2026-08-18.md)).
3. **Audio first in the edit.** Build and trim the audio timeline before pictures ([L31 00:00–01:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L90 05:06](../lessons/090-ai-editing-2026-08-18.md)); check sync after every change ([L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md)).
4. **Grade and motion.** Apply the [L12](../lessons/012-make-ai-look-less-fake.md) grade and Wiggle to every AI shot; Posterize Time for claymation ([L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md)).
5. **Hide what can't be fixed.** Cut away, green-screen to a corner, brush in After Effects, reverse a clip, or censor-mosaic a bad element ([L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L90 14:00–20:08](../lessons/090-ai-editing-2026-08-18.md)).
6. **Captions and safe zone last.** Native caption style; keep text and key visuals out of the bottom button/caption area; preview in Meta's Advanced Preview ([L13 13:10](../lessons/013-live-edit.md); [L84 39:05–40:48; 48:24–49:32](../lessons/084-ad-roast-calls-2026-08-21.md)).
7. **Run the [AI video QA checklist](../rubrics/ai-video-qa-checklist.md)** and the [compliance gate](ai-creator-compliance.md).

### Tell → fix table
| Layer | Tell | Fix (prompt / generation) | Fix (edit) | Cite |
|---|---|---|---|---|
| Audio | "Tinny", too-perfect mic, no street sound in interviews | Two distinct voices (off-camera interviewer + interviewee), "outdoor city ambient" | — | [L21 00:00; 03:13](../lessons/021-street-interviews.md); [L26 00:00; 03:13](../lessons/026-character-consistency.md) |
| Audio | No room tone; clean studio sound in a kitchen or bathroom | Room tone per setting: bathroom slight reverb, bedroom soft close acoustics, kitchen open space, car muffled, outdoors slight wind | — | [L20 skill, Audio Direction](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Audio | Robotic or "bot" read | ElevenLabs v3 with emotion tags, Enhance (alpha) | — | [L28 01:43](../lessons/028-consistent-voices-method-2.md); [L41 00:57](../lessons/041-skeleton-generating-voices.md); [L57 01:02–01:58](../lessons/057-claymation-generating-voice-over.md) |
| Audio | Perfect "podcasty" voice on a story ad; announcer tone | Casual: "He speaks like he just discovered something cool, but not over the top. Very realistic."; calm documentary tone for claymation | Redo the voice before touching anything else | [L41 00:57](../lessons/041-skeleton-generating-voices.md); [L57](../lessons/057-claymation-generating-voice-over.md); [L83 36:17](../lessons/083-ad-roast-calls-2026-08-17.md); [L84 27:34–28:27](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Audio | Over-cleaned voice; ambience stripped | Don't run ElevenLabs cleanup on a clean clip ("actually ruins" it); keep natural ambience (088 page summary: turn off background-noise removal) | Music bed masks generated-speech noise ([L67 00:57](../lessons/067-zack-d-films-voice-clone-song.md)) | [L27 00:47](../lessons/027-consistent-voices-method-1.md); [L88 page](../lessons/088-ad-psychology-with-howie-2026-07-29.md) |
| Audio | Unnatural scripted speech | Contractions, fillers, fragments; read aloud; member tip: drop the "g" in "-ing" words | — | [L20 skill, Dialogue Rules](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L83 20:43](../lessons/083-ad-roast-calls-2026-08-17.md); [L84 20:43](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Lip-sync | Mouth breaks on "P" words | Closed-mouth source stills | Cut to B-roll on the bad syllable | [L29 03:37](../lessons/029-make-ai-creators-talk.md) |
| Lip-sync | Imperfect talking head; hovering-mic artifact | Regenerate or change the shot | Green-screen to a corner, moving; swap in an alternative take for the bad second | [L31 03:48; 06:41](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Camera | Locked-off, perfectly still shot | "slight camera shake", "iPhone handheld" | Wiggle: horizontal 1%, vertical up to 3%, speed 30%, scale 105% (values shown) | [L20 Anti-Cinematic Rules](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L12 02:00–02:57](../lessons/012-make-ai-look-less-fake.md) |
| Camera | Dead-on flat angle, perfect framing | "uneven angles, as if a friend was recording it" | Reframe and zoom slightly in the edit | [L83 43:20–44:21](../lessons/083-ad-roast-calls-2026-08-17.md); [L84 39:05–40:48](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Image | Too sharp, high contrast, saturated "very AI-y" look | 720p, not too high definition ("We don't want it to look too high definition") | Contrast to nothing, saturation slightly down, sharpen ~12, a little Faded Film | [L20 05:59](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L12 01:01–02:00](../lessons/012-make-ai-look-less-fake.md) |
| Skin / people | Plastic, airbrushed, symmetrical face | Realism keywords; character sheet "as realistic as possible"; Nano Banana Pro (Camilo's preference) | Skin-tone match when mixing B-roll | [L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md); [L31 02:44–03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Set | "Squeaky clean" mirror, "too brushed, too perfect" surfaces | Real references (Pinterest method), dirt and wear described | — | [L83 42:50](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Hands / props | Wrong hand actions, impossible props, stemless or empty glasses | Describe what each hand does; simplify or remove props that fail twice | Brush fixes in After Effects; reverse clip | [L20 06:41–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L90 14:00–17:05](../lessons/090-ai-editing-2026-08-18.md) |
| Hands (stylised) | Fingers in yarn texture | Simple poses: standing, sitting, single-arm gestures | — | [L45 §4.3](../lessons/045-claude-skill-setup-explanation.md) |
| Text | Overlaid text artifacts in Sora clips | Discard or remove (Vmake, "free for a very short video") | Captions added in edit only | [L25 01:32](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| Text | Garbled or wrong letters in AI statics ("the capital he") | Templates with editable text; Nano Banana Pro for legible on-pack text | Fix text in Canva/Figma | [L73 01:00; 08:15](../lessons/073-fixing-bad-static-ads-10-51.md); [L71 00:00](../lessons/071-making-statics-with-ai.md); [L62 02:31–03:21](../lessons/062-talking-objects-tutorial.md) |
| Product | Wrong packaging in generated statics | Product reference group (2+ photos) | Inspect at full size; AI edit with exact correction | [L76 02:48–03:44; 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| Motion | Clips "too sped up" or "too AI" | Generate more variations | Cut only the good bits | [L34 00:00–01:02](../lessons/034-fashion-clothing-ads.md) |
| Motion (claymation) | Mixed smooth and 12 fps frames | — | Posterize Time on an adjustment layer; screen shows Frame Rate 15.0 (narration says "set to 50"; trust the screen) | [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md) |
| Edit | Transitions, VFX, risers on UGC | — | None: plain creator-style cuts, jump cuts | [L31 04:39; 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Captions | Drop shadow, wrong font, DaVinci-looking captions | — | Native template (Roboto Black classic style); small simple subtitles (Open Sans); Premiere captions max 15 characters, max 2 s, single line | [L11 00:55–02:44](../lessons/011-native-social-titles-premiere-pro-1.md); [L31 05:35](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L90 51:33](../lessons/090-ai-editing-2026-08-18.md) |
| Captions | Key elements under the "Learn more" button or caption area | Keep key visuals centred at generation | Safe-zone template; Meta Advanced Preview | [L84 39:05–40:48; 48:24–49:32](../lessons/084-ad-roast-calls-2026-08-21.md); [L83 34:24](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Delivery (human UGC too) | Read-aloud, forced delivery | — | Reshoot or regenerate; "you can tell she's reading" | [L104 02:19](../lessons/104-bad-ugc.md) |

## Examples (cited)
| Ad | Tells called out | Fix | Cite |
|---|---|---|---|
| AI "dad gift" clip (older man writing) | Sharp, contrasty, static | Four-step grade + Wiggle: "a lot more like iPhone footage" | [L12 00:00–02:57](../lessons/012-make-ai-look-less-fake.md) |
| Rizz jewelry ad | Talking head imperfect; one take with a hovering mic | Green-screen to corners; alternative shot for "Yes, seven" | [L31 03:48–06:41](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Tai Chi app AI UGC (member) | "AI-ish… too brushed, too perfect", "squeaky clean" mirror, flat angles | Pinterest references; candid-angle prompt line | [L83 42:50–44:21](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Wooden-utensils story ad (member) | Podcasty voice, plastic character, flat angle, no B-roll | Redo voice; B-roll cutaways; character sheet; worm-eye / eagle-eye angles | [L84 27:03–32:22](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Gratsi wine segments (raw) | Slow pacing; reactions mismatched to new lines | Extract audio, isolate voice, reuse reactions; tighten; zoom on sips with slurp SFX | [L23 04:04–11:50](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |

## Common mistakes
- Grading but not fixing audio: the ear catches AI before the eye ([L21 00:00](../lessons/021-street-interviews.md)).
- Leaving the AI creator full-screen through an imperfect CTA ([L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
- Generating emojis or captions inside the video ([L21 04:12](../lessons/021-street-interviews.md)).
- Over-applying Wiggle or Faded Film: the default Wiggle "is too much"; fully up Faded Film "raises all the blacks" ([L12 02:00](../lessons/012-make-ai-look-less-fake.md)).
- Treating realism as the goal instead of the message: Hao and David both put the script first ([L86 33:46](../lessons/086-ad-psychology-with-howie-2026-08-12.md); [L91 43:53](../lessons/091-special-guest-recordings-ai-office-hours-david.md)).
- Using realism edits to hide that a person is synthetic ([AI creator compliance](ai-creator-compliance.md) rows 37–38).

## Where it's taught
- Grade and motion: [L12 00:00–02:57](../lessons/012-make-ai-look-less-fake.md) · [L31 06:41–07:38](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) · [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md)
- Audio and voice: [L20 skill Audio Direction, Dialogue Rules](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L21 00:00–03:13](../lessons/021-street-interviews.md) · [L26 00:00; 03:13](../lessons/026-character-consistency.md) · [L27 00:47](../lessons/027-consistent-voices-method-1.md) · [L28 01:43](../lessons/028-consistent-voices-method-2.md) · [L41 00:00–00:57](../lessons/041-skeleton-generating-voices.md) · [L57 00:00–01:58](../lessons/057-claymation-generating-voice-over.md) · [L83 20:43; 36:17](../lessons/083-ad-roast-calls-2026-08-17.md) · [L84 20:43–28:27](../lessons/084-ad-roast-calls-2026-08-21.md) · [L88 page](../lessons/088-ad-psychology-with-howie-2026-07-29.md)
- Skin, framing, set: [L83 42:50–44:21](../lessons/083-ad-roast-calls-2026-08-17.md) · [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) · [L93 33:41–34:56](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)
- Hands, props, text: [L20 06:41–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L25 01:32](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) · [L45 §4](../lessons/045-claude-skill-setup-explanation.md) · [L62 02:31–03:21](../lessons/062-talking-objects-tutorial.md) · [L71](../lessons/071-making-statics-with-ai.md) · [L73 01:00](../lessons/073-fixing-bad-static-ads-10-51.md) · [L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)
- Edit structure: [L23 04:04–11:50](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) · [L31 00:00–08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) · [L42 07:56–08:52](../lessons/042-skeleton-editing-the-video.md) · [L90 14:00–22:11](../lessons/090-ai-editing-2026-08-18.md)
- Captions and safe zone: [L11 00:55–02:44](../lessons/011-native-social-titles-premiere-pro-1.md) · [L13 13:10](../lessons/013-live-edit.md) · [L83 34:24](../lessons/083-ad-roast-calls-2026-08-17.md) · [L84 39:05–49:35](../lessons/084-ad-roast-calls-2026-08-21.md) · [L90 50:41–53:35](../lessons/090-ai-editing-2026-08-18.md)
- Target spec: [L19](../lessons/019-realistic-ai-ugc-the-ad-we-are-making.md); human delivery tells: [L104 02:19](../lessons/104-bad-ugc.md)

## Cross-course notes
- **Tether Lab (shared, agrees):** [native advertising](../../../../concepts/native-advertising.md) and [model-image psychology](../../../../concepts/model-image-psychology.md) make the same case for native, unpolished visuals; this page supplies the AI-specific tells and fixes.
- **Shared static playbook (differs):** [static ad creation](../../../../playbooks/static-ad-creation.md) limits AI imagery to novelty; this course uses AI product images in statics with full-size inspection and AI edits for pack errors ([L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)). Agent default: allowed only when pack, label and text match the real product exactly.
- **Evolve Copywriting:** [write in the environment](../../../evolve/copywriting/concepts/write-in-the-environment.md) covers the copy side of "don't look like an ad"; this page covers production.

## Related
- [Reference-first prompting](reference-first-prompting.md) · [Character consistency](character-consistency.md) · [Start/end-frame video](start-end-frame-video.md) · [AI creator compliance](ai-creator-compliance.md) · [AI ad format catalog](ai-ad-format-catalog.md)
- [ai-post-production](../frameworks/ai-post-production.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [Tool settings](../libraries/tool-settings.md) · [ElevenLabs](../../../../tools/elevenlabs.md)
