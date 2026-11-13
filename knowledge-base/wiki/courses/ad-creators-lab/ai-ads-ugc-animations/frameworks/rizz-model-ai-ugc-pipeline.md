---
title: "Rizz-model AI UGC pipeline: Sora 2 Pro hook → stills → voice → lip-sync → B-roll → edit (run sheet)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (probable, unverified: ?via=camilo affiliate links; speaker not self-introduced in 024–033)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/027-consistent-voices-method-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/028-consistent-voices-method-2.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/029-make-ai-creators-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/030-generate-realistic-ai-broll.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/033-sora-2-pro-hooks.md
tags: [framework, ai-ugc, rizz, sora-2-pro, elevenlabs, voice-design, lip-sync, kling, premiere-pro, compliance-gate, run-sheet]
updated: 2026-11-13
---

# Rizz-model AI UGC pipeline
> A six-tool chain for a story-style AI UGC ad when one model cannot do it all: Sora 2 Pro makes a realistic hook, Nano Banana Pro rebuilds the same creator as stills, ElevenLabs makes one consistent voice, Rizz lip-syncs the stills, Kling 2.6 makes B-roll, Premiere Pro assembles with "creator-simple" editing. Face and voice are produced separately, so each has its own consistency step.

## 🤖 Agent use
- **Use when:** the ad needs one AI creator across a hook, talking sections and B-roll (wear test, day-in-the-life, story arc) and Seedance's single-model route ([Seedance workflow](ai-ugc-seedance-workflow.md)) is not enough; when a hook clip cannot be re-generated with the same face.
- **Inputs → outputs:** claim-audited story script + product packshot (no people) → hook clip → creator stills → saved voice → full-script MP3 → talking clips + B-roll clips → 9:16 ad (~44 s in the demo, [L31 02:32](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)).
- **Rules:**
  - **DO** run the chain in order: hook → same character as stills → voice → talking → B-roll → edit [L24 00:48](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md).
  - **DO** put the format in every Sora prompt ("selfie FaceTime video", "TikTok video", "get ready with me"); without it, "really weird videos" [L25 00:00–00:58](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) (instructor claim).
  - **DON'T** upload any image with a face to Sora 2 Pro or Arcads: the render fails and can flag the account ([L25 page rule](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md#prompts--templates-verbatim); [L33 01:23](../lessons/033-sora-2-pro-hooks.md)).
  - **DON'T** re-prompt Sora for the same person: "You can't use the same face even if you prompt it the same way" [L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md).
  - **IF** the hook audio is over ~10 s **THEN** instant-clone it [L27](../lessons/027-consistent-voices-method-1.md); **IF** shorter **THEN** Voice Design [L28 00:00](../lessons/028-consistent-voices-method-2.md).
  - **DO** pick closed-mouth stills for lip-sync; open mouths fail on "P" words [L29 03:37](../lessons/029-make-ai-creators-talk.md).
  - **DO** cut audio first, then fill pictures [L31 00:00–01:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); no transitions, VFX or risers [L31 08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md).
  - **DON'T** add a generated "TikTok comment" overlay (course hook device, **don't execute**: fake social proof) [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md).
  - **DON'T** clone or design-to-match any real person's voice; only the AI creator's own generated hook voice or a licensed voice [L27 limits](../lessons/027-consistent-voices-method-1.md).
- **See also:** [Character consistency](../concepts/character-consistency.md) · [AI realism tells](../concepts/ai-realism-tells.md) · [AI creator compliance](../concepts/ai-creator-compliance.md) · [AI post-production](ai-post-production.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [ElevenLabs](../../../../tools/elevenlabs.md) · [AI UGC tools](../../../../tools/ai-ugc-tools.md) · [LLM output claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

## Pipeline map (at recording, Aug–Sep 2026)
| Stage | Tool / model | Why this tool (instructor) | Lesson |
|---|---|---|---|
| Hook | Max Fusion → Sora 2 Pro (or Arcads → Video → Sora 2 Pro) | trained on organic viral video, looks native (instructor claim) | [25](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md), [33](../lessons/033-sora-2-pro-hooks.md) |
| Creator stills | Max Fusion Images → Nano Banana Pro | Sora cannot repeat a face and rejects face uploads | [29 00:00](../lessons/029-make-ai-creators-talk.md), [31 05:35](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Voice | ElevenLabs instant clone or Voice Design; TTS Eleven v3 (alpha) | "coherent, congruent voices" | [27](../lessons/027-consistent-voices-method-1.md), [28](../lessons/028-consistent-voices-method-2.md) |
| Talking clips | Max Fusion → Rizz (ElevenLabs connected) | lip-sync from a still, "biggest selling point" (instructor claim) | [29](../lessons/029-make-ai-creators-talk.md) |
| B-roll | Max Fusion → Kling 2.6 | fewer credits than Veo 3.1 | [30](../lessons/030-generate-realistic-ai-broll.md) |
| Edit | Premiere Pro | — | [31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |

## Compliance gate (step 0, blocks everything after it)
| # | Check | Pass condition | Course example that fails it (**don't execute**) |
|---|---|---|---|
| G1 | Claim audit of the full script, including tagged TTS script | Every price, durability, warranty, scarcity and result claim verified or cut | "14 Karat PVD Gold—which literally cannot tarnish", "Lifetime color warranty", "$180 vs $35", "This sale ends in 48 hours… before we sell out—again" [L27 script](../lessons/027-consistent-voices-method-1.md#prompts--templates-verbatim) (024 transcript says 18 karat: the demo does not even agree with itself [L24 00:00](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md)); hair oil "miracle", "I wasted $3,000", "the industry buried" [L25](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md#prompts--templates-verbatim) |
| G2 | No real-person likeness | Creator is generated by the pipeline; any real iPhone B-roll is licensed | Real third-party iPhone footage mixed in [L31 02:44–03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| G3 | No real-person voice | Voice cloned only from the AI hook clip you generated, or designed | — (course clones an AI hook voice: allowed) |
| G4 | AI person not presented as a real customer | Story framed as a character/dramatisation; no fabricated relationships, test results or comments presented as real | "My boyfriend just spent $300…" personal story [L24 00:00](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md); generated TikTok comment PNG [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); AI-generated "tarnished" competitor jewelry shown as wear-test proof [L30 01:00–01:37](../lessons/030-generate-realistic-ai-broll.md) |
| G5 | Disclosure | Platform AI labelling followed; do not use real footage to hide that the creator is AI ("subtle thoughts that this is an AI video" [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md)) | Mixing real and AI footage to avoid detection [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
Compliant alternative to the wear-test proof: run the test for real and film it, or show the product only and state the verified spec; label dramatised comparisons.

## Run sheet
| # | Step | Tool / model | Exact settings | Input | Output file | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Story script | [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) | Hook + day-by-day proof beats + CTA; plan one visual per beat | product facts, customer language | `script.md` | Every claim listed | — | [L24 How to apply](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md) |
| 2 | Compliance gate | [Claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | G1–G5 | `script.md` | `claim-audit.md` | Nothing unverified spoken or shown | — | derived |
| 3 | Hook clip | Max Fusion → Videos → Sora 2 Pro | **9:16, 12 s, 1080p**; Upload image = product only, background removed | prompt: format + creator (age, look) + setting + action + exact line | `hook/hook_vN.mp4` (≥3 versions) | Format reads native; product shape right; no baked-in text | No format words → odd results; baked-in subtitles → remove (Vmake, free for short clips) or discard; "Something went wrong" tile → regenerate | [L25 00:00–02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| 3b | (Arcads route) | Arcads → project → **Video** → Sora 2 Pro (not Talking Actors) | 9:16, 12 s, 1080p; template for a ready look **or** product image (a template "couldn't… hold the product") | layered prompt: concept → product context → scene → light/time → when product appears | `hook/hook_vN.mp4` | No JSON prompt; "very specific, but also not too specific" | Face upload → "content could not be processed" flag | [L33 00:00–04:36](../lessons/033-sora-2-pro-hooks.md) |
| 4 | Pick hook, extract assets | Video player | Export audio only (<10 MB); screenshot a clean creator frame | best hook | `hook/hook.mp4`, `hook/hook_audio.m4a`, `refs/creator-frame.png` | Clip length noted (8 or 12 s) | — | [L25 steps 4–5](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| 5 | Creator stills | Max Fusion → Images → Nano Banana Pro | Creator frame as reference; one still per talking line and per B-roll beat | `refs/creator-frame.png` + scene description | `stills/NN-scene.png` | Same face, hair, jewelry/product in every still | Drift → regenerate from the same reference, not from the previous output (derived from the hero-reference rule, [L38](../lessons/038-skeleton-generating-images.md)) | [L29 00:00–00:51](../lessons/029-make-ai-creators-talk.md); [L31 04:39–05:35](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| 6a | Voice, hook ≥ ~10 s | ElevenLabs → Voices → Instant clone | Upload audio only; remove music only if the clip has music (cleanup on a clean clip "ruins" it) | `hook_audio.m4a` | voice `<brand>-creator-v1` | Test line sounds like the hook | Video file too large → audio-only export | [L27 00:00–01:46](../lessons/027-consistent-voices-method-1.md) |
| 6b | Voice, hook < ~10 s | ElevenLabs → Voice Design | One-line description: age, accent, pace, tone (use "speaks very fast", not a medical label); 350 credits per generation; 3 previews | observed traits of the hook voice | voice `<brand>-creator-v1` | A/B the hook line vs each preview: "If you can't hear a difference, then it's perfect" | Mismatch → adjust prompt, regenerate | [L28 00:00–01:43](../lessons/028-consistent-voices-method-2.md) |
| 7 | Full-script audio | ElevenLabs Text to Speech | Model **Eleven v3 (alpha)**; audio tags per line (`[thoughtful]`, `[annoyed]`, `[surprised]`, `[excited]`, `[fast]`); **Enhance (alpha)**; screen shows Stability 0% | `script.md` (audited) | `audio/full-script.mp3` | "doesn't sound like a bot" | Flat read → add tags, Enhance, regenerate | [L27 00:28](../lessons/027-consistent-voices-method-1.md); [L28 01:43](../lessons/028-consistent-voices-method-2.md) |
| 8 | Talking clips | Max Fusion → still → ⋯ → Generate video → **Rizz** (or save as actor) | Audio script → Generate speech with your ElevenLabs voice (v3 alpha); emotion tag dropdown (curious, examining, disappointed); optional gesture prompt; one clip per line | closed-mouth front-facing still + line | `talk/NN_vK.mp4` (≥3 variants) | Lip-sync on P words; eyes alive; cost per clip logged (~5 credits short clip in his run) | Mouth breaks → closed-mouth still, change framing, regenerate | [L29 00:51–03:37](../lessons/029-make-ai-creators-talk.md) |
| 9 | B-roll | Max Fusion → still → Generate video → **Kling 2.6** | **9:16, 5 s** (3 credits; 10 s "uses too many credits"); one action sentence + emotion | scene still | `broll/NN.mp4` | Matches the beat; model audio muted | Kling voice ≠ creator → mute; prop/hand wrong → new still or re-roll, don't rescue in the prompt | [L30 00:00–01:37](../lessons/030-generate-realistic-ai-broll.md) |
| 10 | Edit | Premiere Pro | Audio first; long hook then fast vlog cuts; her face recurs; talking head green-screened small in a corner; jump cuts; Open Sans small subtitles; wiggle on static shots; licensed music; no transitions/VFX/risers | all clips + `full-script.mp3` | `edit/ad_v1.mp4` | Reads as a creator-made video | Bad second in a generated line → replace only that shot, keep voice continuous (e.g. CTA "Yes, seven" cutaway) | [L31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| 11 | QA + export | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | 9:16 | `ad_v1.mp4` | `export/ad_v1_final.mp4` | Gate still true | — | derived |

## Sora 2 Pro hook prompt patterns
- Max Fusion (025): `[FORMAT: TikTok / selfie FaceTime / GRWM] of [creator: age, look, accent] [setting] [action]. This is what she says: "[line]"`. Verbatim hair-oil example (claims unusable) and ten page prompts: [L25](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md#prompts--templates-verbatim).
- Arcads (033) layers: concept line → product context → scene and person → mood and light ("soft lighting as if it's 11 in the morning") → product timing ("show the product toward the end"); "as if he had other people helping him" for a higher-production look [L33 03:14–04:36](../lessons/033-sora-2-pro-hooks.md).
- Strip product claims from prompts before voicing ("very good for people who are very stressed out" is unverified) [L33 03:46](../lessons/033-sora-2-pro-hooks.md).

## Failure → fix
| Symptom | Fix | Source |
|---|---|---|
| Sora output has random subtitles/text | Remove in Vmake or discard | [L25 01:32](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| Same prompt, different woman | Stop re-prompting Sora; rebuild the creator as stills | [L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| "Content flagged" on upload | Remove faces from uploads; product/background only | [L33 01:23](../lessons/033-sora-2-pro-hooks.md) |
| Cloned voice sounds off after cleanup | Skip noise/music removal on clean clips | [L27 00:47](../lessons/027-consistent-voices-method-1.md) |
| Rizz mouth glitches | Closed-mouth source still; regenerate; shorter line | [L29 02:38–03:37](../lessons/029-make-ai-creators-talk.md) |
| AI talking head not perfect | Green-screen it small; cut to B-roll and back to her face | [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| CTA clip has a hovering mic / bad audio | Alternative shot for that line; cut back to her for the rest | [L31 06:41](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Static shot looks fake | Premiere Wiggle (settings in [AI post-production](ai-post-production.md)) | [L31 06:41–07:38](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Viewer loses track of who is talking | Show her face repeatedly: "Don't just cut to other B-roll" | [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |

## Disagreements and defaults
- **Kling 2.6 vs Veo 3.1 for B-roll:** Kling for volume and credits; Veo "a lot more credits… more complicated" [L30 01:37](../lessons/030-generate-realistic-ai-broll.md) (instructor claim). Talking-object tests rate Veo 3.1 best for lip-sync [L62 07:39](../lessons/062-talking-objects-tutorial.md). **Default:** Kling 2.6 for silent B-roll; Veo only where on-camera speech must be native.
- **Lesson 026 video vs title:** the video shows the Seedance street interview, not the jewelry creator's stills method [L26 Sources](../lessons/026-character-consistency.md); step 5 is reconstructed from [L29](../lessons/029-make-ai-creators-talk.md) and [L31 05:35](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md). No prompt for the stills is shown: gap.

## Cross-course notes
- **Tether Lab ([AI UGC tools](../../../../tools/ai-ugc-tools.md)):** "Humans are master pattern recognizers when it comes to faces and voices" (Sarah). This course's answer is to minimise face time (green screen, quick cuts) and add phone shake; that reduces tells but does not settle the trust question. Test against a real-creator version.
- **Shared [UGC script writing](../../../../playbooks/ugc-script-writing.md):** the day-by-day wear test is a demonstration structure; it is only honest if the test happened.

## Where it's taught
- [024](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md) target ad and chain [00:00–00:48] · [025](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) Sora hook, format words [00:00–00:58], settings [02:05], face problem [02:54] · [026](../lessons/026-character-consistency.md) still-from-reference [01:45–02:15] · [027](../lessons/027-consistent-voices-method-1.md) instant clone [00:00–01:46] · [028](../lessons/028-consistent-voices-method-2.md) Voice Design [00:00–01:43] · [029](../lessons/029-make-ai-creators-talk.md) Rizz [00:51–03:37] · [030](../lessons/030-generate-realistic-ai-broll.md) Kling B-roll [00:00–01:37] · [031](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) edit [00:00–08:47] · [033](../lessons/033-sora-2-pro-hooks.md) Arcads Sora hooks [00:00–04:36].

## Related
[Seedance workflow](ai-ugc-seedance-workflow.md) · [Creator swap (compliant)](creator-swap-compliant.md) · [AI post-production](ai-post-production.md) · [Produce an AI UGC ad](../playbooks/produce-an-ai-ugc-ad.md) · [Tool settings](../libraries/tool-settings.md) · [Prompt library](../libraries/prompts.md)
