---
title: "AI UGC with the Seedance 2.0 UGC Ad Director skill (run sheet)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (020: Claude greets \"Hey there, Camilo\"; 021–023 same presenter, unverified)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/021-street-interviews.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/022-for-poppy-users.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
tags: [framework, ai-ugc, seedance, claude-skill, max-fusion, poppy, street-interview, character-consistency, compliance-gate, run-sheet]
updated: 2026-11-13
---

# AI UGC with the Seedance 2.0 UGC Ad Director skill
> A runnable sequence that turns a normal UGC creator brief into a talking AI UGC ad: Claude skill → director's brief → references → 15 s Seedance 2.0 segments in Max Fusion → prompt iteration → frame-chained next segment → edit. Variants: street interview (021) and Poppy host (022).

## 🤖 Agent use
- **Use when:** producing an AI UGC ad (one AI creator talking to camera, native audio) from a script or creator brief; writing Seedance 2.0 reference prompts; making an AI street-interview hook.
- **Inputs → outputs:** approved UGC script or brief + product photo + generated (or licensed) creator face → `directors-brief.md` → reference set → one 15 s clip per segment → edited 9:16 ad.
- **Rules:**
  - **DO** brief the model like a human creator: "treat the video model like an actual UGC creator" [L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DO** confirm Claude reads the skill file before answering; "if it's not doing that… it's wrong, you need to try again" [L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DO** split the script into ≤15 s segments; set 9:16, 15 s, 720p ("We don't want it to look too high definition") [L20 02:35; 05:59](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DO** edit the prompt and press Remix rather than rebuild the job [L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); drop a prop that fails twice [L20 09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DO** chain segments: extract a frame of the approved clip, use it as the next creator reference [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DO** direct the audio for interviews: two distinct voices plus outdoor ambience, against the "tinny, too perfect mic" tell [L21 00:00; 03:13](../lessons/021-street-interviews.md).
  - **DON'T** upload reference photos with emoji, watermarks, text or app UI: "Seedance recreates everything it sees as physical objects" (skill, [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md#prompts--templates-verbatim)).
  - **DON'T** write "cinematic" or film-camera words (skill rule 3 and anti-cinematic list).
  - **DON'T** put emojis, subtitles or B&W in the generation; add them in the edit [L21 04:12](../lessons/021-street-interviews.md).
  - **DON'T** use a stranger's Pinterest photo as the creator's face (course method, **don't execute**); generate the face (Step 5).
  - **IF** a detail is not described **THEN** "Seedance invents it" (skill): describe each hand, the surface, and what is not in frame.
- **See also:** [AI creator compliance](../concepts/ai-creator-compliance.md) · [Reference-first prompting](../concepts/reference-first-prompting.md) · [Character consistency](../concepts/character-consistency.md) · [AI realism tells](../concepts/ai-realism-tells.md) · [AI post-production](ai-post-production.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [Produce an AI UGC ad (playbook)](../playbooks/produce-an-ai-ugc-ad.md) · [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) · [LLM output claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

## What you need before step 1
| Input | Minimum | Source |
|---|---|---|
| Script or creator brief | 5 hooks, body as talking points, B-roll shot list, filming notes (the Gratsi PDF structure) | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md#prompts--templates-verbatim) |
| Product photo | clean packshot, no people | skill ("@Image3 = product photo") |
| Creator face | generated face you own, or a real creator with a signed release covering AI likeness and voice | derived (compliance gate) |
| Skill | "Seedance 2.0 UGC Ad Director" `SKILL.md` (verbatim in L20); plain-text copy for Poppy in L22 | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md#prompts--templates-verbatim), [L22](../lessons/022-for-poppy-users.md#prompts--templates-verbatim) |
| Generator | Max Fusion → Videos → Seedance 2.0 → References (skill also names Jianying) | [L20 04:03](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |

## Compliance gate (step 0, blocks everything after it)
| # | Check | Pass condition | Course example that fails it (**don't execute**) |
|---|---|---|---|
| G1 | Claim audit of the script | Every product, health, result, price and time claim is verified or bracketed `[unverified]` and cut before generation; the AI creator "will say whatever the brief says" ([L20 How to apply](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)) | 021 script: "You wake up the next day feeling totally fine" (hangover-type claim) [L21](../lessons/021-street-interviews.md#prompts--templates-verbatim) |
| G2 | No real-person likeness | Creator face is generated or licensed; Pinterest used only for lighting, framing, wardrobe and setting | Stranger's Pinterest photo as `@Image1` [L20 01:46](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); real interview frame and creator as the scene base [L21 01:45](../lessons/021-street-interviews.md) |
| G3 | No real-person voice | Voice is Seedance-generated from a text description, designed, or licensed | — (020–023 use native generated audio) |
| G4 | AI person not presented as a real customer | First-person story is written as a character, not a testimonial; no invented relationships or "my friend told me" proof | Invented "Italian friend" referral [L21](../lessons/021-street-interviews.md#prompts--templates-verbatim); "My Italian husband bet me $100" persona [L20 PDF hooks](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| G5 | Disclosure | Platform AI-content labelling rules checked for the placement (derived) | — |
Write the result to `claim-audit.md`. Rules and examples: [AI creator compliance](../concepts/ai-creator-compliance.md).

## Run sheet
Tool facts at recording (Aug–Sep 2026). Output file names are a suggested convention (derived).

| # | Step | Tool / model | Exact settings | Input | Output file | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Write the brief | [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) | 5 hooks; body as 2–3 talking points, "not a brand claim"; no "link below"; banned hype words | product facts, offer, customer language | `brief.md` | Body ≤ ~1 min; hooks filmable separately | Product named in hooks → remove unless stated | [L20 PDF](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 2 | Compliance gate | [Claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | G1–G5 above | `brief.md` | `claim-audit.md` | No unverified claim left in spoken lines | — | derived |
| 3 | Install the skill | Claude Desktop | Customize → Skills → + → Create skill → Upload skill (zip); call `/seedance` or "Try in chat" | skill zip | installed skill "Seedance 2.0 UGC Ad Director" | Listed under Skills | Poppy users: attach the text file instead (row 3b) | [L20 00:00](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 3b | (Poppy host) | Poppy → Chat | Connect skill text + script; model Opus 4.7; "execute the skill for this UGC script" | skill `.txt` + `brief.md` | same as row 4 | References match the script | Mismatch → files not attached or skill not run (page) | [L22 00:00](../lessons/022-for-poppy-users.md) |
| 4 | Run the skill | Claude, Opus (021 screen: Opus 4.7) | New chat; upload brief; slash command | `brief.md` | `directors-brief.md` (product, N × 15 s segments, Pinterest searches, per-segment prompts) | Exact skill format; Pinterest links present; every 5 s block 3–4 sentences; audio block with voice + room tone; one action arc per segment; no "cinematic" | Generic output → reply "follow the skill format"; skill not read → new chat, rerun | [L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L21 00:47](../lessons/021-street-interviews.md) |
| 5 | Creator reference | Image model (Nano Banana Pro preferred over GPT Image 2 for realism) | Phone-quality, natural light, casual clothes, no studio, no heavy makeup | Pinterest results as **style** references only | `refs/creator.png` (`@Image1`) | Clean: no emoji, watermark, text, UI; generated face, not the Pinterest person | Studio or magazine look → regenerate with "phone photo, window light" | skill Step 1; [L21 01:45](../lessons/021-street-interviews.md) |
| 6 | Scene, prop, product references | Pinterest ("more like this") + your packshot | One location and one prop reference per segment; name files clearly | `directors-brief.md` Step 2 searches | `refs/sNN-location.jpg`, `refs/sNN-prop.jpg`, `refs/product.png` (`@Image3`) | Clean photos only | Disorganised refs → wrong `@` mapping; "you have to be very organized" | [L20 02:35–03:32](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 7 | Generate segment 1 | Max Fusion → Videos → Seedance 2.0 → References | 9:16, **15 s**, **720p**; up to 9 images (skill: 9 images + 3 videos + 3 audio); `@Image1` creator, `@Image3` product | segment-1 prompt + refs | `clips/s01_v1.mp4` | Read the prompt "as if you were shooting it" first; add product placement by reference if wanted | Duration left at default (7–8 s on screen) → set 15 s | [L20 04:03–05:59](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 8 | Review the take | — | — | `s01_v1.mp4` | `clips/s01_review.md` | Each hand's action; props make sense; product label and shape; every spoken word; voice and room tone; no burned-in text | See failure table | [L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 9 | Iterate | Same job → edit prompt → Remix | Add camera moves ("multiple shots", medium shot, hand places item, pan up); add a missing prop reference | review notes | `clips/s01_vK.mp4` | Shot matches the brief | Prop fails twice → cut it ("I think it'll even convert better", instructor claim) | [L20 06:41–11:28](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 10 | Chain the next segment | Video player frame export → Seedance 2.0 | Prompt starts "same person, slightly closer to the shot" + segment-2 prompt | best frame of approved clip | `refs/creator-s02.png`, `clips/s02_v1.mp4` | Face, hair, wardrobe, light match segment 1 | Drift → re-export a sharper frame; keep `@Image1` the same file across retries | [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| 11 | Edit | Editor (CapCut-like, unnamed) | Reaction matching, product inserts, hook text, captions, zooms, SFX | all approved clips | `edit/ad_v1.mp4` | Sync rechecked after every change | See [AI post-production](ai-post-production.md) | [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| 12 | QA and export | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | 9:16 | `ad_v1.mp4` | `export/ad_v1_final.mp4` | QA pass + gate still true for the final cut | — | derived |

## Prompt anatomy (skill output, per 15 s segment)
1. Header line: `9:16. 15 seconds. Single continuous shot. UGC style. iPhone handheld.` (or "multiple shots" when you need cuts, [L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
2. Mapping: `@Image1 is the creator. @Image3 is the product.`
3. Three timed blocks `[0:00-0:05]`, `[0:05-0:10]`, `[0:10-0:15]`, 3–4 sentences each: camera position, appearance, expression, **each hand**, surface contents and what is **not** there, one light source and direction, background.
4. `Audio:` voice (age, gender, tone, energy), room tone matched to the setting (bathroom reverb, car muffled, outdoors slight wind…), natural speech with fillers, full dialogue in quotes.
Full skill text: [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md#prompts--templates-verbatim). Street-interview prompt as legible on screen: [L21](../lessons/021-street-interviews.md#prompts--templates-verbatim).

## Variant: street-interview hook (021)
| # | Step | Detail | Source |
|---|---|---|---|
| 1 | Study a real interview for feel | Ambience and mic handling make it read "raw, authentic"; copy the format only | [L21 00:00–00:47](../lessons/021-street-interviews.md) |
| 2 | Script | Rapid quiz questions → freeze → cut to confession body | [L21 attachment](../lessons/021-street-interviews.md#prompts--templates-verbatim) |
| 3 | Creator-in-scene still | Nano Banana Pro: generated creator + a street-scene reference you are allowed to use; several generations | [L21 01:45–02:15](../lessons/021-street-interviews.md) |
| 4 | Seedance prompt | Camera "held by the interviewer at arm's length"; face, shoulders up; audio: "Two distinct voices, off-camera interviewer…", "outdoor city ambient" | [L21 02:15–03:13](../lessons/021-street-interviews.md) |
| 5 | Edit | Emojis, subtitles, black-and-white, freeze frame, then cut to body | [L21 04:12](../lessons/021-street-interviews.md) |
Compliant swap for step 3: the course screenshots a real creator's interview and swaps the person in (**don't execute**); build the street frame from a licensed stock still or generate it from a text description.

## Failure → fix
| Symptom | Cause (as stated) | Fix | Source |
|---|---|---|---|
| Hands do odd things; props nonsensical (straws in cardboard) | prompt left hand actions undescribed | Describe each hand; add a prop reference; else cut the prop | [L20 06:41–09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Wrong glassware, empty glasses, product inconsistent | too many objects to track | Simplify the scene (pour shots of box and bottle only) | [L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Random artifacts | undescribed details | "If you don't describe it, Seedance invents it" | skill |
| Objects copied from the reference image (stickers, text) | dirty reference | Use clean photos only | skill |
| Interview sounds like AI | "mic is too perfect", no street sound | Two-voice audio block + city ambience | [L21 00:00; 03:13](../lessons/021-street-interviews.md) |
| Emoji in prompt looked wrong | model renders it | Add emoji in edit | [L21 04:12](../lessons/021-street-interviews.md) |
| Creator changes between segments | new generation, no carried reference | Frame from previous clip as `@Image1`; "same person" | [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Audio and captions drift after edits | timeline edits | Re-sync after each change | [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| Reaction does not match the new line | reaction cut from another moment | Extract audio, isolate voice, re-sit the reaction | [L23 04:04](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |

## Cost and time (at recording, Aug–Sep 2026)
- Credits shown on Max Fusion Seedance 2.0 at 720p: 70 at 7 s [L21 03:02](../lessons/021-street-interviews.md), 80 on the 020 job [L20 05:42](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md), 130 at 13 s ([L16 01:35](../lessons/016-clone-broll-ugc-ads.md)). That is about 10 credits per second (derived); budget ~150 per 15 s take and 3+ takes per segment (derived).
- Edit: 18–19 minutes of live editing for the wine ad [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) (instructor demo, not a benchmark).

## Disagreements and defaults
- **Seedance native voice vs separate voice.** Skill rule 2: Seedance "DOES generate speech… NEVER tell users to add voiceover in post" [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md#prompts--templates-verbatim). Lesson 018 found voices drift across generations unless the voice block is repeated [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md); lesson 015 shows Seedance keeps a source clip's voice on a swap [L15 02:29](../lessons/015-change-creators-with-ai.md). **Default:** keep native audio, paste the identical voice block in every segment, compare segments back to back; if they differ, switch to one ElevenLabs voice + lip-sync ([rizz-model pipeline](rizz-model-ai-ugc-pipeline.md)).
- **Duration.** Narration and skill say 15 s; screens show 7–8 s before he changes it [L20 05:42](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L21 03:02](../lessons/021-street-interviews.md). **Default:** 15 s, set explicitly.
- **Real-scene base for the street interview** (course) vs no real-person likeness (repo). **Default:** repo rule.

## Cross-course notes
- **Tether Lab (shared [AI UGC tools](../../../../tools/ai-ugc-tools.md)):** Sarah warns AI faces erode trust for identity-led brands; Chase warns against flooding an account with 50–100 AI ads. This course assumes AI UGC works and shows no performance data for the wine ad. Default: test AI UGC as one concept among real-creator concepts, not as volume.
- **Shared [UGC script writing](../../../../playbooks/ugc-script-writing.md) / [creator brief](../../../../playbooks/creator-brief.md):** the Gratsi brief structure (hooks filmed separately, body as talking points, B-roll checklist, filming specs) matches the shared brief playbook; this course adds the skill that converts a human brief into model prompts.

## Where it's taught
- [020 Claude skill + Seedance 2.0](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md): install [00:00], skill check [00:54], references [01:46–03:32], Max Fusion settings [04:03–05:59], iteration [06:41–11:28], frame chaining [12:26].
- [021 Street interviews](../lessons/021-street-interviews.md): audio problem [00:00], creator-in-scene [01:45–02:15], prompt and audio [02:15–03:13], edit [04:12].
- [022 For Poppy users](../lessons/022-for-poppy-users.md): Poppy host, Opus 4.7 [00:00–00:57].
- [023 Live editing](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md): reactions [02:16–05:42], hook text and captions [07:34–11:12], zoom and SFX [11:12–11:50].
- [026 Character consistency](../lessons/026-character-consistency.md): same street-interview build, mapped `@image1` [00:47–03:13].

## Related
[Rizz-model pipeline](rizz-model-ai-ugc-pipeline.md) · [Creator swap (compliant)](creator-swap-compliant.md) · [AI post-production](ai-post-production.md) · [Claude Code ad operator](claude-code-ad-operator.md) · [Prompt library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md)
