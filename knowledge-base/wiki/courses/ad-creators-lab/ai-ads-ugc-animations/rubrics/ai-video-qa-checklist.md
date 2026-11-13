---
title: "AI video QA checklist (yes/no, pre-publish): hands, product, lip-sync and words, on-screen text, realism tells, consistency, safe zone, compliance"
type: rubric
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab (failure modes observed across Camilo's tutorials and roasts, Narek's AI editing call 090 and guest Caleb Kruse 093)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/012-make-ai-look-less-fake.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/015-change-creators-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/029-make-ai-creators-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/034-fashion-clothing-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/039-skeleton-generating-videos.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/041-skeleton-generating-voices.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/051-how-to-generate-ai-songs-for-your-brand.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/058-editing-claymation-step-by-step.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/062-talking-objects-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/076-new-make-static-ads-with-ai-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
tags: [rubric, qa, checklist, ai-video, hands, product-consistency, lip-sync, on-screen-text, ai-realism, safe-zone, compliance]
updated: 2026-11-13
---

# AI video QA checklist
> A yes/no checklist run on every generated clip (shot QA) and again on the finished edit (pre-publish), built from the failure modes the course actually hit: hands and props, product and label drift, lip-sync and wrong words, text artifacts, AI realism tells (look and sound), character and voice drift, sync and safe zone, plus the compliance items that block publication.

## 🤖 Agent use
- **Use when:** after each generation (keep / regenerate / cut), before handing clips to the edit, and before uploading the finished ad.
- **Inputs → outputs:** clip or master + script + product reference photos + reference list → filled checklist, blocker list, verdict, fix per failed item, a row in the shot QA log.
- **Rules:**
  - **DO** watch every clip at full size, once without sound and once with sound ([L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) How to apply; [L76 07:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md)).
  - **DO** compare product shots against the real product photos, not against memory [L84 50:57](../lessons/084-ad-roast-calls-2026-08-21.md).
  - **DO** run a separate QA pass (a second agent or person) on the first agent's output and keep a human final yes/no [L93 50:59–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
  - **DON'T** "just generate and stitch the clips together" [L90 22:11](../lessons/090-ai-editing-2026-08-18.md); fix in post or regenerate.
  - **IF** any ⛔ item is NO **THEN** the clip or ad does not ship. **IF** three or more other items are NO on the master **THEN** revise and re-run (derived).
- **See also:** [AI realism tells](../concepts/ai-realism-tells.md) · [Character consistency](../concepts/character-consistency.md) · [AI post-production](../frameworks/ai-post-production.md) · [AI creator compliance](../concepts/ai-creator-compliance.md) · [Ad roast scorecard](ad-roast-scorecard.md) (execution) · [Tool settings](../libraries/tool-settings.md)

## How to run it
1. **Shot QA (per clip):** sections A–F. Verdict per clip: keep / fix in post / regenerate (same refs, edited prompt) / cut the shot. Log it.
2. **Pre-publish (master):** sections A–H on the finished edit, including safe zone in Meta Advanced Preview and the compliance section.
3. Answer every item YES, NO or N/A, with a timestamp for every NO.

## A. Hands, bodies, motion
| # | Check (YES = pass) | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| A1 | Hands hold and use objects in a way that makes sense (no hands passing through props, no extra or merged fingers) | | Describe what EACH hand does in the prompt; switch to multiple shots with simpler actions | [L20 06:41; skill "Detail Level"](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| A2 | Stylised characters (yarn, clay) avoid complex hand poses | | Standing, sitting, single-arm gestures only | [L45 skill, Known Limitations](../lessons/045-claude-skill-setup-explanation.md) |
| A3 | No impossible motion or body glitch (skin patches, neck bugs, limbs bending wrong) | | Brush/hue fix in post; reverse the clip and generate the opposite motion | [L90 14:00–16:01](../lessons/090-ai-editing-2026-08-18.md) |
| A4 | Props behave physically and stay the same object across the shot | | Drop a prop that fails twice | [L20 09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| A5 | Gestures match what the speaker says | | Prompt gestures per line ("if they're talking about their chest, let them touch") | [L84 23:38](../lessons/084-ad-roast-calls-2026-08-21.md) |

## B. Product and label consistency
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| B1 | Product shape, colour, size and packaging match the real product in every shot | ⛔ | Re-run with several product reference photos; AI edit with a reference image and an exact instruction | [L76 07:20–08:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md); [L84 50:57](../lessons/084-ad-roast-calls-2026-08-21.md) |
| B2 | Label text and logo are correct and legible (or not visible) | ⛔ | Replace with a real product photo/insert in the edit | [L76 07:20](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) |
| B3 | Product-related objects stay consistent between shots (glasses, bottles, servings) | | Simplify the action; add references | [L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| B4 | Product is present in every scene the script needs it in | | Re-run with the product reference attached | [L46 08:14](../lessons/046-script-visualisation-image-creation.md) |
| B5 | Garments: logos, stitching and fit match the real garment | ⛔ | Regenerate or cut | [L34](../lessons/034-fashion-clothing-ads.md) |
| B6 | No other brand's logo or product appears (unless a lawful comparison) | ⛔ | Generic or own-labelled props | [L44](../lessons/044-crochet-the-ad-we-are-making.md) |

## C. Lip-sync, voice and spoken words
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| C1 | Every spoken word matches the approved script (no invented, slurred or nonsense words) | ⛔ | Regenerate; shorten the line; re-prompt dialogue verbatim | [L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| C2 | Brand name, product name and ingredients are pronounced correctly (VO, lyrics) | ⛔ | Respell phonetically in the script; regenerate | [L41](../lessons/041-skeleton-generating-voices.md); [L51 01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| C3 | Mouth movement syncs with audio, including P/B words | | Source still with mouth closed; regenerate | [L29 03:37](../lessons/029-make-ai-creators-talk.md) |
| C4 | Voice fits the character (age, gender, scene); not a "perfect podcasty voice" in a kitchen | | Redo the voice before anything else | [L84 09:53; 27:34–28:27](../lessons/084-ad-roast-calls-2026-08-21.md); [L15 01:38–02:29](../lessons/015-change-creators-with-ai.md) |
| C5 | Same voice across all segments (accent, pace, timbre) | | Prompt voice every scene; or one full VO take, sliced | [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md); [L91 50:13](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| C6 | No unwanted music or model-generated voice in clips meant to be silent | | Prompt "no music"; mute; switch model | [L39 01:28–02:03](../lessons/039-skeleton-generating-videos.md) |
| C7 | IF a platform blocked lip-sync THEN the replacement still syncs | | Same image in Kling/Seedance with words spoken slowly; sync in edit | [L84 35:26–36:24](../lessons/084-ad-roast-calls-2026-08-21.md) |

## D. On-screen text
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| D1 | No generated text artifacts (garbled signs, captions, watermarks) in the footage | ⛔ | Keep text out of image/video prompts ("no text, no captions, no words, no letters, no watermark, no UI"); remove artifacts (Vmake) | [L37 skill](../lessons/037-install-skill-generate-script.md); [L25 01:32](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| D2 | No objects copied from reference-image overlays (emoji, UI, watermarks rendered as physical things) | | Clean references only | [L20 skill](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| D3 | Any text that must be in-image (talking-object labels) is spelled right | ⛔ | Variation prompt with corrected text, or add it in the edit | [L62 03:21](../lessons/062-talking-objects-tutorial.md) |
| D4 | Captions match the audio word for word and are in sync | ⛔ | Recheck sync after each edit | [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| D5 | Caption style native: small simple font, one line, short chunks (e.g. ≤15 characters, ≤2 s) | | Premiere caption preferences | [L31 05:35](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [L90 51:33](../lessons/090-ai-editing-2026-08-18.md); [L42 07:56](../lessons/042-skeleton-editing-the-video.md) |
| D6 | Headline/title text is about this video's topic (no leftover template text) | | Rewrite as a topic headline | [L83 48:46–49:16](../lessons/083-ad-roast-calls-2026-08-17.md) |
| D7 | Style labels are true (don't call it "claymation" if it isn't) | | Remove or correct | [L84 46:27; 50:57](../lessons/084-ad-roast-calls-2026-08-21.md) |

## E. Realism tells (look and sound)
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| E1 | Footage doesn't look too sharp, contrasty or saturated ("very AI-y") | | Lumetri: contrast down, saturation slightly down, sharpen ~12, a little Faded Film | [L12 01:01–02:00](../lessons/012-make-ai-look-less-fake.md) |
| E2 | Handheld clips have natural shake; no dead-static UGC shots | | Wiggle effect | [L12 02:00–02:57](../lessons/012-make-ai-look-less-fake.md); [L31 06:41–07:38](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| E3 | Skin, surfaces and framing aren't "too brushed, too perfect" (squeaky-clean mirror, plastic skin) | | Realism keywords (pores, texture, blemishes; candid, uneven angles); character sheet | [L83 42:50–43:20](../lessons/083-ad-roast-calls-2026-08-17.md); [L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) |
| E4 | Camera angle isn't dead-on flat throughout | | Vary angles; worm's-eye for tense lines | [L83 44:21](../lessons/083-ad-roast-calls-2026-08-17.md); [L84 31:24](../lessons/084-ad-roast-calls-2026-08-21.md) |
| E5 | Audio has room tone / ambience matching the setting; not a tinny, perfect mic | | Prompt room tone and ambience per setting | [L26 00:00; 03:13](../lessons/026-character-consistency.md); [L20 skill "Audio Direction"](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| E6 | UGC edit has no transitions, VFX or risers that a creator wouldn't use | | Remove | [L31 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| E7 | Imperfect AI talking shots are not held full-screen for long | | Shorten; green-screen to a corner over B-roll | [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| E8 | Claymation has a consistent stop-motion frame rate | | Posterize Time adjustment layer, 15 fps | [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md) |
| E9 | References used were real-looking, not already-AI images | | Swap references | [L18 00:00–00:55](../lessons/018-realistic-ai-podcasts-tutorial.md) |

## F. Character and scene consistency
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| F1 | Same face, hair, outfit and body across all segments | | Reuse the character reference; extract a frame from the approved clip as the next reference | [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L26 00:47](../lessons/026-character-consistency.md) |
| F2 | Stylised character identical to the hero image | | Reference the hero, not the previous image; "Keep character facial consistency. No character redesign. No facial feature changes." | [L37 skill](../lessons/037-install-skill-generate-script.md); [L56 01:00](../lessons/056-claymation-generating-videos-transitions.md) |
| F3 | No drift inside a clip (Kling drift on claymation) | | Switch to Seedance for that style | [L90 1:09:39–1:10:20](../lessons/090-ai-editing-2026-08-18.md) |
| F4 | Transitions start and end on the intended frames (end frame = final landed state) | | Fix the end frame or reclassify as Type A | [L45 skill](../lessons/045-claude-skill-setup-explanation.md) |
| F5 | Snapshots used as first frames are sharp | | GPT Image 2 "sharpen and enhance" at 2K/4K | [L90 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md) |
| F6 | Real footage mixed with AI matches skin tone and look | | Pick footage with similar skin tone; licensed footage only | [L31 02:44–03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |

## G. Edit, sync and safe zone (master only)
| # | Check | ⛔ | Fix if NO | Source |
|---|---|---|---|---|
| G1 | Each script line shows its matching visual; named things appear on their word | | Re-cut; generate missing inserts | [L83 47:25](../lessons/083-ad-roast-calls-2026-08-17.md); [L42 01:57](../lessons/042-skeleton-editing-the-video.md) |
| G2 | Audio, captions and picture stay in sync to the end | ⛔ | Recheck after each change | [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| G3 | Key visuals, product and captions sit outside the caption and button overlay zones in every placement | ⛔ | Keep key visuals centred; safe-zone template; zoom in slightly to reframe | [L84 39:05–40:48](../lessons/084-ad-roast-calls-2026-08-21.md); [L83 34:24](../lessons/083-ad-roast-calls-2026-08-17.md) |
| G4 | Checked in Meta Advanced Preview across placements | | Open the ad preview; move text out of overlays | [L84 48:24–49:32](../lessons/084-ad-roast-calls-2026-08-21.md) |
| G5 | Cuts every 2–3 s or justified; consistent slow zoom on shots | | Speed clips to the measured gap; keyframe zooms | [L90 31:37](../lessons/090-ai-editing-2026-08-18.md); [L83 33:29](../lessons/083-ad-roast-calls-2026-08-17.md) |
| G6 | Song or VO starts immediately (no intro) | | Cut to the first lyric/line | [L47 00:00](../lessons/047-crochet-editing-final-video.md) |
| G7 | 9:16 export; hook variants exported | | Re-export | [L20 05:59](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L42 11:53](../lessons/042-skeleton-editing-the-video.md) |

## H. Compliance (all ⛔)
| # | Check | Compliant alternative | Source |
|---|---|---|---|
| H1 | No AI person is presented as a real customer, patient, doctor or expert, and none claims personal results | Narrator, dramatisation, or a real disclosed person | [L80 09:55](../lessons/080-supplement-brand-70k-winning-ad-breakdown.md); [L17](../lessons/017-ai-podcasts-that-look-real-what-we-are-making.md) |
| H2 | Creator face is synthetic, licensed or consented; not a stranger's photo, a real creator or a celebrity look-alike | Synthetic person from a text description | [L20 01:46](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L15](../lessons/015-change-creators-with-ai.md); [L18 02:24](../lessons/018-realistic-ai-podcasts-tutorial.md) |
| H3 | Voice is designed, own or licensed; no cloned real person | Voice Design from a description | [L27](../lessons/027-consistent-voices-method-1.md); [L67](../lessons/067-zack-d-films-voice-clone-song.md); [L29 04:07](../lessons/029-make-ai-creators-talk.md) |
| H4 | No fabricated comments, reviews, counts, ratings or scarcity on screen | Real, permitted comment or none | [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| H5 | Every claim (spoken, sung, captioned) passed the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | Bracket and remove | Repo rule |
| H6 | Music, SFX and footage licensed for paid ads | Licensed library or CapCut library SFX | [L58 03:33](../lessons/058-editing-claymation-step-by-step.md) |
| H7 | No competitor footage, characters or lines | Rebuild the mechanism | [L91 18:21–36:26](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| H8 | AI-content disclosure set per platform rules | — | [L93 56:54–58:18](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |

## Output block (shot QA log row and master verdict)
```yaml
ai_video_qa:
  asset: <clip id | master>
  stage: shot | pre_publish
  model: <model + settings>      # at recording, Aug–Sep 2026
  results:                       # YES / NO / N/A per item; timestamp for every NO
    A: {A1: YES, A2: N/A, A3: NO@0:04 "neck skin patch", A4: YES, A5: YES}
    B: {...}
    C: {...}
    D: {...}
    E: {...}
    F: {...}
    G: {...}                     # master only
    H: {...}                     # master only
  blockers_failed: [<item ids>]
  other_fails: <count>
  verdict: KEEP | FIX_IN_POST | REGENERATE | CUT | SHIP | BLOCK
  fixes: ["<item>: <fix> (source)"]
  credits_used: <n>
  reviewer: <agent id> · human_final: <name/role | pending>
```

## Where it's taught
[L12](../lessons/012-make-ai-look-less-fake.md) · [L15](../lessons/015-change-creators-with-ai.md) · [L18](../lessons/018-realistic-ai-podcasts-tutorial.md) · [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) · [L25](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) · [L26](../lessons/026-character-consistency.md) · [L29](../lessons/029-make-ai-creators-talk.md) · [L31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) · [L34](../lessons/034-fashion-clothing-ads.md) · [L37](../lessons/037-install-skill-generate-script.md) · [L39](../lessons/039-skeleton-generating-videos.md) · [L42](../lessons/042-skeleton-editing-the-video.md) · [L45](../lessons/045-claude-skill-setup-explanation.md) · [L46](../lessons/046-script-visualisation-image-creation.md) · [L51](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) · [L56](../lessons/056-claymation-generating-videos-transitions.md) · [L58](../lessons/058-editing-claymation-step-by-step.md) · [L62](../lessons/062-talking-objects-tutorial.md) · [L76](../lessons/076-new-make-static-ads-with-ai-poppy-method.md) · [L83](../lessons/083-ad-roast-calls-2026-08-17.md) · [L84](../lessons/084-ad-roast-calls-2026-08-21.md) · [L90](../lessons/090-ai-editing-2026-08-18.md) · [L91](../lessons/091-special-guest-recordings-ai-office-hours-david.md) · [L93](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)

## Cross-course notes
- **Tether Lab (shared):** the shared [ad scorecard](../../../../rubrics/ad-scorecard.md) auto-fail AF8 (synthetic person delivering a testimonial) is the same rule as H1; [AI UGC tools](../../../../tools/ai-ugc-tools.md) lists tools. No other course in the KB has an AI-footage QA list; this page owns it.
- **Evolve Start Here:** [execution checklist](../../../evolve/start-here/rubrics/execution-checklist.md) covers concept-level execution before a shoot; this checklist covers generated footage after it.
