---
title: "AI post-production: edit order, realism treatment, fixes, captions and sound for AI ads (run sheet)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "unverified (011–013 narrator not named); Camilo (probable, 023, 031, 042, 047); Narek (090)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/011-native-social-titles-premiere-pro-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/012-make-ai-look-less-fake.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/013-live-edit.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/047-crochet-editing-final-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/058-editing-claymation-step-by-step.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
tags: [framework, post-production, editing, premiere-pro, capcut, after-effects, lumetri, wiggle, posterize-time, captions, sfx, ai-realism, compliance-gate, run-sheet]
updated: 2026-11-13
---

# AI post-production
> Editing is "the only tool that will make the AI generations less AI sloppy" [L90 22:11](../lessons/090-ai-editing-2026-08-18.md). One order of work fits every AI ad: audio first → clips placed on the words → fix generation bugs in post → pacing → format treatment (phone realism for AI UGC; stop-motion for claymation; music-video motion for songs) → captions → music and SFX → CTA → export. This page holds the exact settings the course shows and which recipe to use for which footage.

## 🤖 Agent use
- **Use when:** editing or briefing an editor on AI UGC, animated or song ads; checking a cut for AI tells; picking caption, grade and SFX settings.
- **Inputs → outputs:** generated clips + voiceover/song + licensed music and SFX + audited script → `edit/ad_vN.mp4` and hook variants.
- **Rules:**
  - **DO** build the audio timeline first and cut it tight; then fit pictures to it [L31 00:00–01:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L42 00:00](../lessons/042-skeleton-editing-the-video.md); [L58 00:00](../lessons/058-editing-claymation-step-by-step.md); [L90 06:04](../lessons/090-ai-editing-2026-08-18.md).
  - **DO** show the named thing on the word it is spoken [L42 01:57](../lessons/042-skeleton-editing-the-video.md); B-roll "over the exact words it illustrates" [L13 03:54–09:41](../lessons/013-live-edit.md).
  - **DO** cut to a new visual every 2–3 s; generate the model minimum (3 s) and speed it up to the gap [L90 30:31–31:37](../lessons/090-ai-editing-2026-08-18.md).
  - **DON'T** "just generate and stitch the clips together" [L90 22:11](../lessons/090-ai-editing-2026-08-18.md).
  - **DO** for AI UGC: lower contrast, lower sharpness, a little faded film, subtle wiggle [L12 01:01–02:57](../lessons/012-make-ai-look-less-fake.md); no transitions, VFX or risers [L31 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md).
  - **DO** for claymation: Posterize Time 15 fps on an adjustment layer [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md); speed-curve seams [L58 01:29–03:33](../lessons/058-editing-claymation-step-by-step.md).
  - **DO** keep captions one line, minimal words, inside the safe zone [L42 07:56–10:49](../lessons/042-skeleton-editing-the-video.md); [L13 13:10](../lessons/013-live-edit.md); fix brand/technical words by hand [L90 53:35](../lessons/090-ai-editing-2026-08-18.md).
  - **DON'T** let captions or audio drift; recheck sync after every change [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md).
  - **DON'T** overlay a generated TikTok comment as social proof (course device, **don't execute**) [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); don't use YouTube-ripped SFX [L58 03:33](../lessons/058-editing-claymation-step-by-step.md).
- **See also:** [AI realism tells](../concepts/ai-realism-tells.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [AI creator compliance](../concepts/ai-creator-compliance.md) · [UGC creator operations](ugc-creator-operations.md) · [Native advertising](../../../../concepts/native-advertising.md) · [Seedance workflow](ai-ugc-seedance-workflow.md) · [Rizz-model pipeline](rizz-model-ai-ugc-pipeline.md) · [Animated pipeline](animated-ad-production-pipeline.md) · [Song-ad workflow](song-ad-workflow.md)

## Pick the recipe by footage
| Footage | Recipe | Treatment | Avoid | Source |
|---|---|---|---|---|
| AI UGC meant to pass as phone video | 012 grade + wiggle; 031 creator-simple rules; 023 reaction/insert matching; 011 native hook text | Contrast down, sharpen ~12, faded film a little, wiggle; green-screen imperfect talking heads small | Transitions, VFX, risers, high contrast | [L12](../lessons/012-make-ai-look-less-fake.md), [L31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md), [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md), [L11](../lessons/011-native-social-titles-premiere-pro-1.md) |
| Real UGC A-roll + studio B-roll, direct response | 013 13-step live edit | Contrast/saturation/brightness up on a few shots; whip transition + whoosh; Warp Stabilizer; "Shop now" end card | Tutorial openers as hooks | [L13](../lessons/013-live-edit.md) |
| Narrated animated (skeleton, Zack style) | 042 | VO first, cut on the noun, matched zoom direction, contrast shot (B&W old way), identity caption | Jarring zoom-static-zoom | [L42](../lessons/042-skeleton-editing-the-video.md) |
| Song-driven animated (crochet, singing) | 047 | Start on first lyric, lock song, inserts for long lyrics, keyframed drift + slight zoom | Song intro left in | [L47](../lessons/047-crochet-editing-final-video.md) |
| Claymation | 058 + 090 | Speed curve flash out/in at seams, SFX per action, Posterize Time 15 fps | Model-generated audio | [L58](../lessons/058-editing-claymation-step-by-step.md), [L90](../lessons/090-ai-editing-2026-08-18.md) |

## Compliance gate (before export)
| # | Check | Pass condition | Course example that fails it (**don't execute**) |
|---|---|---|---|
| G1 | On-screen text and captions match the audited script | No new claims added in hook text, end cards or caption keywords | Caption keyword "cellulite, natural remedy" [L65](../lessons/065-script-to-prompt-generator.md) (edit-stage text) |
| G2 | No fake engagement or proof overlays | No generated comments, fake review cards, fake counters | Generated TikTok comment PNG on the hook [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| G3 | Footage, music, SFX, templates licensed | Licence on file for third-party footage, music, SFX | Real third-party iPhone B-roll [L31 02:44–03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); SFX from a YouTube downloader [L58 03:33](../lessons/058-editing-claymation-step-by-step.md); a brand's product footage used for an exercise [L13](../lessons/013-live-edit.md) |
| G4 | Disclosure not defeated | Realism treatment improves quality; it is not used to hide AI where the platform requires a label | Mixing real footage to avoid "subtle thoughts that this is an AI video" [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| G5 | Edit-stage censoring is not a claim | Mosaic/blur used only to hide a bad render, never to imply "too graphic to show" | Mosaic over a bad result [L90 18:23–20:08](../lessons/090-ai-editing-2026-08-18.md) (acceptable as a render fix) |

## Run sheet
Settings at recording (Aug–Sep 2026). Premiere Pro 2025 unless stated; CapCut equivalents where the lesson used CapCut.

| # | Step | Tool | Exact settings | Input | Output | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Project + reframe | Premiere | Drag A-roll to New Item; Sequence → Auto Reframe Sequence → Vertical 9:16, Analyze clips on | clips | sequence `ad_vN` | 9:16 | 4K B-roll zoomed in → right-click Set to Frame Size | [L13 01:02; 05:32](../lessons/013-live-edit.md) |
| 2 | Audio master | Premiere / CapCut | Import VO or song; split at gaps (S) and close them; lock audio track; cut song intro | `vo.mp3` / `song.mp3` | locked audio track | Natural pacing, no AI artifacts | Line hurts pacing → delete it (031 cut "the boutique $180") | [L31 00:58](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L42 00:00](../lessons/042-skeleton-editing-the-video.md); [L47 00:00](../lessons/047-crochet-editing-final-video.md); [L90 06:04](../lessons/090-ai-editing-2026-08-18.md) |
| 3 | Hook | — | Desire/identity line, not a tutorial opener; in AI UGC a long hook take then fast cuts; three things happen in the first seconds (animated) | best opening takes | hook section | Hook appeals to a self/desire | Tutorial opener → cut ("looks too much") | [L13 01:02–02:22](../lessons/013-live-edit.md); [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L42 01:57](../lessons/042-skeleton-editing-the-video.md) |
| 4 | Place clips on words | Q / W ripple trims (Q left of playhead, W right) | Start clips at the movement, not frame 0; jump cuts inside long takes | clips | rough cut | Named thing appears on its word | Clip too long → start at movement, speed up | [L13 02:22–03:54](../lessons/013-live-edit.md); [L42 00:58–03:59](../lessons/042-skeleton-editing-the-video.md) |
| 5 | Retime | Speed/Duration; Time Remapping | 60 fps footage → 50%; 3 s AI clips sped up to the measured gap (In/Out points); speed ramp via nest → Time Remapping → Speed keyframes | rough cut | timed cut | Visual changes every 2–3 s | — | [L13 08:20; 18:29](../lessons/013-live-edit.md); [L90 30:31–31:06; 36:43](../lessons/090-ai-editing-2026-08-18.md) |
| 6 | Fix generation bugs | After Effects / Premiere | Brush skin/neck bugs; Hue/Saturation to recolour; reverse a clip to get an impossible motion; mosaic over an unusable render; replace a single bad second with another shot while voice continues | flagged clips | fixed clips | No visible glitch at phone size | Bug in one second of a good line → cut-away for that second | [L90 14:00–20:08](../lessons/090-ai-editing-2026-08-18.md); [L31 06:41](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| 7 | Reaction + insert matching (UGC) | Premiere | Extract audio, isolate voice, re-sit a reaction under another line; insert product shots on their line | reaction clips | cut | Reactions fit the words | Sync loss → re-sync after each change | [L23 02:16–05:42; 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| 8 | Motion continuity (animated) | Keyframes (scale + position) | Neighbouring shots share zoom direction; cut dead frames; slow zoom on still shots; music-video drift left/right with slight zoom | timed cut | cut | No zoom → static → zoom jumps | Jarring cut → trim or regenerate | [L42 03:03; 05:54](../lessons/042-skeleton-editing-the-video.md); [L47 03:27](../lessons/047-crochet-editing-final-video.md) |
| 9 | Realism treatment (AI UGC) | Lumetri Color + Effects | Basic: Contrast to minimum, Saturation slightly down, Highlights up optional. Creative: Sharpen ~12, Faded Film a little. Effects → Impact Motion Effects → **Wiggle**: Complexity 59, Horizontal 1.0%, Vertical 3.0%, Wiggle Speed 30%, Min Scale 105%, Max Scale 100%, Scale Speed 25 (final on screen) | clips | graded clips | "looks… like iPhone footage" | Default wiggle "a bit much" → reduce ranges/speed | [L12 01:01–03:00](../lessons/012-make-ai-look-less-fake.md); [L31 06:41–07:38](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| 9b | Stop-motion treatment (claymation) | Adjustment layer over the sequence | **Posterize Time, Frame Rate 15.0** + colour correction | sequence | stylised sequence | Consistent stepped motion | Mixed smooth/12 fps clips → one posterize layer unifies | [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md) |
| 9c | Seam hiding (transition clips) | CapCut → Speed → Curve | "Flash out" on outgoing clip, "flash in" on incoming; drag ramp to the trigger word | transition clips | seams | Speed peak on the word | Ramp starts too early → move ramp point right | [L58 01:29–03:33](../lessons/058-editing-claymation-step-by-step.md) |
| 9d | Imperfect AI talking head | Ultra Key / green screen | Talking clip small, bottom-left/right, moving; stills of her behind | talking clips | composite | Not full-frame if lip-sync is weak | — | [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| 10 | Hook text | `.mogrt` "Native Social Titles" (Graphics Templates → +) | Classic style, **Roboto Black**, native colour, Background Style 1/2; keep off face and product | hook line | hook title | No drop shadow, wrong font, middle line, "DaVinci look" | Hand-built box → use the template | [L11 00:00–02:44](../lessons/011-native-social-titles-premiere-pro-1.md) |
| 11 | Captions | Premiere: Text → Transcribe → Create captions from transcript | Captioning Preferences: max **15 characters**, max **2 s**, single line; save first caption as a style ("Subs 1"); resize into the Instagram safe zone | VO | caption track | ~90% right; fix brand words | Drift after edits → resync | [L90 50:41–53:35](../lessons/090-ai-editing-2026-08-18.md); [L13 13:10](../lessons/013-live-edit.md) |
| 11b | Caption look by format | — | AI UGC: small, simple, Open Sans [L31 05:35]; animated: one line, thick stroke, no template, 2–3 words matched to speech + identity caption "POV…" [L42 07:56–10:49]; songs: 1–3 words per sung word [L49 frames] | — | — | Two lines only inside safe zones | — | [L31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L42](../lessons/042-skeleton-editing-the-video.md); [L49](../lessons/049-singing-animation-the-ads-we-re-making.md) |
| 12 | Music | Licensed library | Low under VO ("never… too loud"); per section: playful hook, tech/educational under features, playful on the pain line, rising "high note" into CTA; claymation "sneaky… jazz"; Zack style "sneak" genre | sections | music track | VO intelligible | — | [L42 00:00](../lessons/042-skeleton-editing-the-video.md); [L13 13:10–16:09](../lessons/013-live-edit.md); [L90 24:09](../lessons/090-ai-editing-2026-08-18.md); [L67 00:57](../lessons/067-zack-d-films-voice-clone-song.md) |
| 13 | SFX | CapCut Audio → Sound effects / licensed pack | One per physical action (drink, pour, cloth hit, slurp on sips); thick liquid pour on transitions; whoosh under any whip | cut | SFX tracks | Model audio muted where replaced | Model audio adds random music → mute, add SFX yourself ("full control") | [L58 03:33–05:44](../lessons/058-editing-claymation-step-by-step.md); [L23 11:12](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md); [L13 17:18](../lessons/013-live-edit.md) |
| 14 | CTA | — | "Shop now" card or end card after final VO; logo last | — | end card | CTA not lost | — | [L13 17:18–19:56](../lessons/013-live-edit.md) |
| 15 | Review passes | — | Watch once muted (pacing), once with sound (audio); phone-size check; [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | `ad_vN` | QA notes | Gate G1–G5 | Only bad seams → regenerate those clips only | [L23 How to apply](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md); [L58 How to apply](../lessons/058-editing-claymation-step-by-step.md) |
| 16 | Export + variants | Premiere / CapCut | H.264, 9:16, ~30 fps (013 page); 1080×1920 (skeleton skill); 2–3 hook variants | — | `export/ad_vN_hookX.mp4` | — | — | [L13 step 13](../lessons/013-live-edit.md); [L42 11:53](../lessons/042-skeleton-editing-the-video.md) |

## Snapshot enhancement (feeds generation, done in post)
GPT Image 2: "up-res and sharpen and enhance this image", 2K or 4K, before using a last-frame snapshot as the next first frame [L90 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md).

## Time budgets (instructor claims)
- Real UGC DR edit: "less than half an hour" [L13 19:56](../lessons/013-live-edit.md).
- Skeleton edit: ~10 min plus a few minutes of extra generations [L42 07:56](../lessons/042-skeleton-editing-the-video.md).
- Claymation ad: one to 1.5 days at the agency; "four hours is fair" for one minute [L90 48:58–49:40](../lessons/090-ai-editing-2026-08-18.md).

## Disagreements and defaults
- **Grade direction.** AI footage: contrast down, saturation slightly down [L12 01:01](../lessons/012-make-ai-look-less-fake.md) vs DR edit of real footage: add contrast, saturation, brightness [L13 17:18](../lessons/013-live-edit.md). **Default:** by footage type (recipe table).
- **Transitions.** Whip + whoosh on each transition [L13 17:18](../lessons/013-live-edit.md) vs "no transitions, no VFX, no risers" [L31 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); Narek: built-in transitions are basic, ask the model for a camera-based transition (match cut, whip pan) [L90 57:48–59:16](../lessons/090-ai-editing-2026-08-18.md). **Default:** none for organic-looking AI UGC; in-camera/generated transitions for animated; editor transitions only for polished DR edits.
- **Posterize Time value.** Spoken "set to 50" vs on-screen Frame Rate 15.0 [L90 38:20](../lessons/090-ai-editing-2026-08-18.md). **Default:** 15 (screen; within the 12–15 fps claymation range he states).
- **Caption stroke.** Thick stroke [L42 08:52](../lessons/042-skeleton-editing-the-video.md) vs skeleton skill "thin dark outline" ([L37](../lessons/037-install-skill-generate-script.md#prompts--templates-verbatim)). **Default:** whichever stays legible on the background; test both as a hook variant.

## Cross-course notes
- **Shared [native advertising](../../../../concepts/native-advertising.md):** the 011 rule (ads with wrong text styling "look like ads") is the same native principle; this course supplies the exact template and font.
- **Evolve ([iteration outcomes](../../../evolve/copywriting/concepts/iteration-outcomes.md)):** hook variants exported at step 16 are variations of one concept; see [Diversification vs variation](../concepts/diversification-vs-variation.md) before counting them as new tests.

## Where it's taught
- [011 Native social titles](../lessons/011-native-social-titles-premiere-pro-1.md) [00:00–02:44] · [012 Make AI look less fake](../lessons/012-make-ai-look-less-fake.md) [00:00–03:00] · [013 Live edit](../lessons/013-live-edit.md) [00:00–19:56] · [023 Live editing AI UGC](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) [00:00–18:50] · [031 Rizz editing breakdown](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) [00:00–08:47] · [042 Skeleton editing](../lessons/042-skeleton-editing-the-video.md) [00:00–11:53] · [047 Crochet editing](../lessons/047-crochet-editing-final-video.md) [00:00–04:08] · [058 Claymation editing](../lessons/058-editing-claymation-step-by-step.md) [00:00–05:44] · [090 Narek AI editing](../lessons/090-ai-editing-2026-08-18.md) [05:06–59:16].

## Related
[AI realism tells](../concepts/ai-realism-tells.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [UGC creator operations](ugc-creator-operations.md) · [Tool settings](../libraries/tool-settings.md)
