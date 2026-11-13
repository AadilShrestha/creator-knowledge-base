---
title: "Playbook: produce an AI UGC ad (intake → script → claim audit → references → generation → QA → edit → test)"
type: playbook
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (AI UGC tutorials 012–031 and roasts 083–084); Narek (090); guests David (091) and Caleb Kruse (093)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/008-how-to-make-diversified-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/012-make-ai-look-less-fake.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/013-live-edit.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/015-change-creators-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/017-ai-podcasts-that-look-real-what-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/018-realistic-ai-podcasts-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/019-realistic-ai-ugc-the-ad-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/021-street-interviews.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/022-for-poppy-users.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/026-character-consistency.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/027-consistent-voices-method-1.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/028-consistent-voices-method-2.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/029-make-ai-creators-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/030-generate-realistic-ai-broll.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/033-sora-2-pro-hooks.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/078-wine-brand-125k-at-2-24-roas.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/080-supplement-brand-70k-winning-ad-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/081-turning-400-ad-to-13k-spender.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/094-research-protocol-start-here.md
tags: [playbook, ai-ugc, seedance, sora, rizz, kling, elevenlabs, max-fusion, references, character-consistency, editing, qa, testing, compliance]
updated: 2026-11-13
---

# Playbook: produce an AI UGC ad
> Twelve gated steps that turn a concept card and real product inputs into a tested AI UGC video: intake, path choice, script, claim audit, director's brief, references, voice, generation, shot QA, edit, final scoring, paused upload and test plan. Built from the course's Seedance director workflow (020–023), the rizz-model chain (024–031) and the roast feedback (083–084).

## 🤖 Agent use
- **Use when:** a concept needs a human-looking creator (talking head, GRWM, taste test, podcast, street interview) or voiceover + B-roll with people, and the footage will be AI-generated.
- **Inputs → outputs:** concept card + product facts + offer + audience + real customer language + product photos → script with 3 hooks, director's brief, prompt pack, reference list, generated clips, edited 9:16 ad, shot QA log, test plan.
- **Rules:**
  - **DO** brief the video model "like an actual UGC creator": the same brief a human would get [L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md). The AI creator says whatever the brief says, so the brief passes the claim audit first.
  - **DO** decide the script before the visuals [L91 43:53](../lessons/091-special-guest-recordings-ai-office-hours-david.md), and generate the whole voiceover in one go, never in pieces [L91 50:13](../lessons/091-special-guest-recordings-ai-office-hours-david.md).
  - **DO** put references before prompts: "number one important thing is reference not your prompt" [L90 11:31](../lessons/090-ai-editing-2026-08-18.md).
  - **DO** expect 4–5 takes per scene [L90 12:29](../lessons/090-ai-editing-2026-08-18.md) and iterate the prompt with Remix rather than restarting [L20 06:41](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **DON'T** let an AI character claim personal results or act as a real customer, patient or expert [L80 09:55](../lessons/080-supplement-brand-70k-winning-ad-breakdown.md); [AI creator compliance](../concepts/ai-creator-compliance.md).
  - **DON'T** use a stranger's photo (Pinterest), a real creator's face or a cloned real voice as your AI creator, even though the course demos do ([L20 01:46](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md), [L15](../lessons/015-change-creators-with-ai.md), [L27](../lessons/027-consistent-voices-method-1.md)): **don't execute**; compliant path in step 6.
  - **IF** a prop or action fails twice **THEN** cut it from the shot [L20 09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
  - **IF** the voice sounds like a "perfect podcasty" narrator that doesn't fit the scene **THEN** redo the voice before anything else [L84 27:34–28:27](../lessons/084-ad-roast-calls-2026-08-21.md).
- **See also:** [AI UGC Seedance workflow](../frameworks/ai-ugc-seedance-workflow.md) · [Rizz-model AI UGC pipeline](../frameworks/rizz-model-ai-ugc-pipeline.md) · [Creator swap (compliant)](../frameworks/creator-swap-compliant.md) · [AI post-production](../frameworks/ai-post-production.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [Ad roast scorecard](../rubrics/ad-roast-scorecard.md) · [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) · [Shared UGC script writing](../../../../playbooks/ugc-script-writing.md) · [AI UGC tools](../../../../tools/ai-ugc-tools.md) · [ElevenLabs](../../../../tools/elevenlabs.md)

## Inputs required up front
Collect these before step 3. If any is missing, write it in the `missing_inputs` list of the deliverables and continue only with what is verified; bracket every unverified fact.

| Input | Why | If missing |
|---|---|---|
| Concept card (angle, awareness stage, avatar, format) | Sets hook, structure and path | Run [research to AI ad concepts](research-to-ai-ad-concepts.md) |
| Product facts: what it is, how it works (mechanism), usage, price | Every spoken claim traces here | Ask once; bracket and list "verify before generating" |
| Offer and guarantee, exact wording | CTA must state it exactly | Leave `[OFFER]` placeholder; no invented discount |
| Claims allowed / forbidden (regulated category?) | Health, results and money claims get blocked | Treat every outcome claim as forbidden until confirmed |
| Real customer language (5–20 verbatim lines, with source) | Hooks in the customer's own words [L83 12:46](../lessons/083-ad-roast-calls-2026-08-17.md) | Say the angle is a hypothesis; mine reviews per [L97](../lessons/097-customer-research-protocol-1.md) |
| Real proof that exists (review count, rating, studies, press) | Only proof source | No proof lines at all |
| Product photos: several angles, clean background | Product consistency in every clip [L25 02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) | Block generation of product shots |
| Creator identity you have rights to (see step 6) | Likeness compliance | Generate a synthetic person from a text description |
| Tool access and budget (Max Fusion / Seedance, Sora 2 Pro, Kling, ElevenLabs, editor) | Path choice and cost | Path V (voiceover + B-roll) needs the fewest tools |
| Landing page URL | Ad ↔ page fit [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md) | Flag; can't judge funnel fit |

## Step 2 decision: choose the production path
First classify the concept with one question: "is the character's mouth moving?" Lip-sync, voiceover + B-roll, or a mix; voiceover + B-roll is "90 percent easily" of AI ads because it is easier [L91 01:24–02:49](../lessons/091-special-guest-recordings-ai-office-hours-david.md).

| Path | Use for | Chain | Lessons |
|---|---|---|---|
| **S: Seedance director** | One creator on camera with native dialogue and room sound; demos, taste tests, story monologues | Claude "Seedance 2.0 UGC Ad Director" skill → references → Seedance 2.0 in 15 s segments → frame-chain → edit | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md), [L21](../lessons/021-street-interviews.md), [L22](../lessons/022-for-poppy-users.md) (Poppy), [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md); [framework](../frameworks/ai-ugc-seedance-workflow.md) |
| **R: Rizz-model chain** | Phone-style creator story with a long hook, talking inserts and lifestyle B-roll | Sora 2 Pro hook → same character as stills → voice (clone own clip or Voice Design) → Rizz talking clips → Kling B-roll → edit | [L24 00:48](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md) to [L31](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md); [framework](../frameworks/rizz-model-ai-ugc-pipeline.md) |
| **P: Podcast / street interview** | Two speakers or interviewer + subject | Edited real-style set frame → speaker B by flipping and changing identity → Kling/Seedance with voice prompted every time | [L18](../lessons/018-realistic-ai-podcasts-tutorial.md), [L21](../lessons/021-street-interviews.md), [L26](../lessons/026-character-consistency.md) |
| **V: Voiceover + B-roll** | Mechanism or story told by narrator; lowest lip-sync risk | Script → one full ElevenLabs VO → B-roll stills → image-to-video → edit | [L91 02:49; 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md), [L30](../lessons/030-generate-realistic-ai-broll.md) |
| Creator swap of an existing ad | Only on **our own** or fully licensed ads | Frame → identity edit → same pose → voice replaced | [L15](../lessons/015-change-creators-with-ai.md), [L16](../lessons/016-clone-broll-ugc-ads.md); [compliant version](../frameworks/creator-swap-compliant.md) |

Default (derived): path V when the claim needs heavy visual proof or the budget is small; path S for a single on-camera creator; path R only when a Sora-style phone hook is the point of the concept. Model choice per format is contested (see Conflicts).

## The chain
| # | Step | Do | Output | Gate |
|---|---|---|---|---|
| 1 | Intake | Fill the inputs table; write avatar, awareness stage, market and offer at the top of the doc [L83 11:18](../lessons/083-ad-roast-calls-2026-08-17.md) | `intake` block + `missing_inputs` | No claim without a source or bracket |
| 2 | Path | Mouth-moving test; pick S / R / P / V | `path` | Path fits tools and budget |
| 3 | Script | Run the [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md), then apply the AI-specific edits below | Script + 5 hook candidates, 3 kept | Every line has a visual; read-aloud test passed |
| 4 | Claim + compliance audit | [RMBC claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) on the script; compliance gate below | Audited script | Zero fabricated proof; AI character makes no personal-result claim |
| 5 | Director's brief | Split into ≤15 s segments; one action arc per segment; describe each hand, expression, surface, and what is **not** in frame | Segment table + prompts | Each prompt passes the anti-cinematic list |
| 6 | References | Creator identity (lawful), character sheet, scene, prop and product references, named and filed | Reference list | Clean images only; product refs from several angles |
| 7 | Voice | Native-audio direction (S, P) or one full ElevenLabs VO (R, V) | Voice spec or VO file | Voice matches the character; brand names pronounced right |
| 8 | Generate | Test short, then full segments; 4–5 takes; Remix; chain segments by extracted frame | Clip set | Cost approved before batches |
| 9 | Shot QA | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) per clip | Shot QA log | No blocker item failed |
| 10 | Edit | Audio first, pictures to audio; de-AI grade; captions; safe zone | 9:16 master + hook variants | Sync rechecked after every change |
| 11 | Score | Full QA checklist on the master + [roast scorecard](../rubrics/ad-roast-scorecard.md) + shared [ad scorecard](../../../../rubrics/ad-scorecard.md) if required | Filled scorecards | Pass marks in the rubric pages |
| 12 | Launch + test | Upload PAUSED; human yes/no; test plan; read results into MORE / BETTER / NEW | Test plan + readout | Landing page fits the ad |

## Step details

### Step 3: script edits for AI production
Start from the shared skill's output, then:
- **Hooks:** build an open loop, not an obvious statement; "saying you have a weak pelvic floor is not an open loop" [L83 16:30](../lessons/083-ad-roast-calls-2026-08-17.md). Juxtaposition "how to [desire] without [linked pain]" is the course's quick win (instructor claim) [L80 07:28–08:22](../lessons/080-supplement-brand-70k-winning-ad-breakdown.md). See [hook schema and open loops](../concepts/hook-schema-and-open-loops.md).
- **Hooks as separate shots:** the course brief asks for 5 hooks, filmed separately so editors can build variations, no product in hooks unless stated (Gratsi brief, [L20 page](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
- **Twist the knife:** say why earlier solutions failed in the viewer's situation before the product appears [L83 40:27](../lessons/083-ad-roast-calls-2026-08-17.md).
- **Show each line:** every line names its visual ("association and showing not telling") [L83 47:25](../lessons/083-ad-roast-calls-2026-08-17.md); turn "I tried everything" into shown attempts [L84 10:52](../lessons/084-ad-roast-calls-2026-08-21.md). Hook words and hook visuals must agree [L81 06:43–07:36](../lessons/081-turning-400-ad-to-13k-spender.md).
- **Spoken English:** read it aloud line by line, natural speech, "drop the g" (member tip) [L84 20:43](../lessons/084-ad-roast-calls-2026-08-21.md); prompt gestures that match the words [L84 23:38](../lessons/084-ad-roast-calls-2026-08-21.md).
- **Cut vague words:** "better", "game changer" [L83 24:36; 41:20](../lessons/083-ad-roast-calls-2026-08-17.md).
- **Segment fit:** Seedance renders at most 15 s per clip, so each segment's dialogue must fit 15 s [L20 02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md). Rizz clips are per line [L29](../lessons/029-make-ai-creators-talk.md).

### Step 4: compliance gate (don't execute → compliant version)
| Course tactic | Status | Compliant version | Source |
|---|---|---|---|
| AI hosts or creators presented as real customers ("since we joined this group", "Italian husband" bet story) | **Don't execute** | Dramatisation framing, a first-person line that is true for a real person, or a narrator; label AI people where required | [L17](../lessons/017-ai-podcasts-that-look-real-what-we-are-making.md), [L19](../lessons/019-realistic-ai-ugc-the-ad-we-are-making.md) |
| AI character claiming results ("I lost 200 pounds" is the course's own counter-example) | **Don't execute** | AI characters carry information "as long as they're not making any claims" | [L80 09:55](../lessons/080-supplement-brand-70k-winning-ad-breakdown.md) |
| AI doctor or "patient" telling a medical story | **Don't execute** | Real, disclosed expert, or no expert; no unsupported medical claims | [L84](../lessons/084-ad-roast-calls-2026-08-21.md) limitations |
| Fake TikTok-comment PNG over the hook | **Don't execute** | A real comment used with permission, or a question caption written as the brand | [L31 02:44](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| "Meta won't flag AI" | Not a licence | Follow platform AI-disclosure and non-deception rules | [L93 56:54–58:18](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
Full list: [AI creator compliance](../concepts/ai-creator-compliance.md).

### Step 5: director's brief and prompt rules
- Path S: install the skill (Claude Desktop → Customize → Skills → + → Upload skill), upload the audited brief, and check Claude reads the skill first; "if it's not doing that… it's wrong, you need to try again" [L20 00:00–00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md). Poppy users: "Execute the skill for this UGC script." on Opus 4.7 [L22](../lessons/022-for-poppy-users.md). The skill text is on [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); index in [prompts library](../libraries/prompts.md).
- Anti-cinematic vocabulary: use "iPhone handheld, natural lighting, UGC style, slight camera shake, 9:16"; never "cinematic", camera brands, "dramatic lighting", "bokeh" and the rest of the skill's list ([L20 skill](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); [reference-first prompting](../concepts/reference-first-prompting.md).
- Detail: 3–4 sentences per 5-second block: each hand, facial expression, surface and what's not there; Seedance "follows everything to the T", so vague prompts produce random details [L20 11:28](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md).
- One action arc per prompt; no two scene changes in one prompt ([L20 skill, Seedance facts](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)).
- Path R hook (Sora 2 Pro): name the format ("selfie FaceTime video", "TikTok video", "get ready with me video") or results are "really weird" [L25 00:00–00:58](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md); concept, setting, time-of-day light, when the product appears [L33 02:18–04:36](../lessons/033-sora-2-pro-hooks.md).
- Camera: dead-on flat angles "give away" AI [L83 44:21](../lessons/083-ad-roast-calls-2026-08-17.md); for tense or sad lines put the angle lower (worm's-eye) [L84 31:24–32:22](../lessons/084-ad-roast-calls-2026-08-21.md).

### Step 6: references (lawful identity first)
| Reference | How | Source |
|---|---|---|
| Creator identity | **Compliant default:** a synthetic person generated from a text description (age, look, wardrobe), or a consenting creator / licensed stock with ad-use rights. **Don't execute:** picking a stranger's Pinterest photo [L20 01:46–02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) or editing a real creator's face [L15](../lessons/015-change-creators-with-ai.md); Pinterest "now contains a lot of AI images" anyway [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) | [AI creator compliance](../concepts/ai-creator-compliance.md) |
| Character sheet | Multiple angles, same outfit and body, per video [L93 27:54–29:24](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); avatar sheet before clips [L90 11:00](../lessons/090-ai-editing-2026-08-18.md); fixes a "plastic" look [L84 30:22](../lessons/084-ad-roast-calls-2026-08-21.md) | [Character consistency](../concepts/character-consistency.md) |
| Image realism | Ask for "candid photo, TikTok style with uneven angles, as if a friend was recording it" [L83 43:20](../lessons/083-ad-roast-calls-2026-08-17.md); "visible pores, real skin texture… a few blemishes", never "cinematic, professional, studio, perfect" [L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | [AI realism tells](../concepts/ai-realism-tells.md) |
| Scene and props | One reference per scene and prop, clearly named ("creator", "kitchen counter reference") [L20 02:35–03:32](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); real-looking sets in your niche, not AI-looking ones [L18 00:00–00:55](../lessons/018-realistic-ai-podcasts-tutorial.md); no famous set [L18 02:24, 04:11](../lessons/018-realistic-ai-podcasts-tutorial.md) | |
| Product | Several real product photos, background removed where possible [L25 02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md); Sora rejects images with a human face [L33 page](../lessons/033-sora-2-pro-hooks.md) | |
| Cleanliness | No emoji, watermarks, text overlays or app UI: "Seedance recreates everything it sees as physical objects" ([L20 skill](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)) | |
| Mapping | Max Fusion → Seedance 2.0 → References, up to nine images, `@Image1 is the creator` [L20 04:03–05:01](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | [Reference-first prompting](../concepts/reference-first-prompting.md) |

### Step 7: voice
- Paths S and P: prompt the voice every generation (accent, speed, mic sound, echo, volume when moving off-mic, delivery), or the speaker "is going to sound different" across scenes [L18 05:08](../lessons/018-realistic-ai-podcasts-tutorial.md). Direct two distinct voices and ambient sound for interviews; a "tinny" perfect mic with "no street sound" reads as AI [L26 00:00; 03:13](../lessons/026-character-consistency.md).
- Paths R and V: one full-script ElevenLabs take, cleaned of dead air, then sliced [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md). Voice Design from a description (age, country, speed, background), compare with the target until "you can't hear a difference", Enhance (alpha) before generating [L28 00:00–01:43](../lessons/028-consistent-voices-method-2.md). Instant clone only from audio you own (your own generated hook clip, under 10 MB, music removed) [L27 00:00–00:47](../lessons/027-consistent-voices-method-1.md); never a real person's voice.
- Describe speakers by observable traits ("speaks very fast"), not medical conditions ([L28](../lessons/028-consistent-voices-method-2.md) derived rule).
- Match voice to character: a male voice on a female creator "ruins it a little" [L84 09:53, 11:50](../lessons/084-ad-roast-calls-2026-08-21.md); a face swap keeps the source voice, so replace it [L15 01:38–03:19](../lessons/015-change-creators-with-ai.md).

### Step 8: generation settings (at recording, Aug–Sep 2026)
| Path | Model / setting | Source |
|---|---|---|
| S | Seedance 2.0 on Max Fusion: 9:16, 15 s, 720p ("We don't want it to look too high definition") | [L20 05:59](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| R hook | Sora 2 Pro: 12 s, 1080p, many versions; remove text artifacts (Vmake) | [L25 01:32–02:05](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| R talking | Rizz on Max Fusion from a still; mouth-closed source image; v3 emotion tags | [L29 00:51–03:37](../lessons/029-make-ai-creators-talk.md) |
| B-roll | Kling 2.6, 5 s, 9:16, very simple prompts ("girl observes her jewelry") | [L30 00:00–00:40](../lessons/030-generate-realistic-ai-broll.md) |
| P | Test with ~5 s clips first; edit the set image in stages, not one prompt | [L18 05:08; 07:40](../lessons/018-realistic-ai-podcasts-tutorial.md) |
Procedure: generate segment 1 → review → edit prompt (camera moves, what each hand does, missing references) → Remix [L20 06:41–09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) → when approved, extract a frame as the creator reference for segment 2 ("same person, slightly closer to the shot") [L20 12:26](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md). Smoke-test one output and get cost approval before a batch [L93 36:11–38:40](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md). Full settings and credit costs: [tool settings](../libraries/tool-settings.md).

### Step 10: edit
| Do | Source |
|---|---|
| Build the audio timeline first, trim it, then fill pictures to it | [L31 00:00–01:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Pick the best reaction per line; isolate voice to rebind a reaction to new audio | [L23 02:16–04:04](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| Put B-roll over the exact words it shows; prefer B-roll with movement | [L13 03:54–09:41](../lessons/013-live-edit.md) |
| Add B-roll cutaways under any talking claim | [L84 29:23](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Don't dwell on an imperfect AI talking shot; green-screen it to a corner over B-roll | [L31 03:48](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Jump cuts; small simple subtitles (Open Sans); no transitions, VFX or risers | [L31 04:39–08:47](../lessons/031-realistic-ai-ugc-rizz-model-editing-breakdown.md) |
| Lumetri: contrast down, saturation slightly down, sharpen ~12, a little Faded Film, Wiggle for hand shake | [L12 01:01–02:57](../lessons/012-make-ai-look-less-fake.md) |
| Hook caption that "sound[s] like a story" and adds to the video | [L83 32:29](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Slow zoom in every shot; zoom in builds tension, zoom out releases | [L83 33:29](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Recheck audio and caption sync after each edit | [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |
| Keep key visuals centred; safe-zone template; check Meta Advanced Preview | [L84 39:05–40:48; 48:24–49:32](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Export 2–3 hook variants | [L42 11:53](../lessons/042-skeleton-editing-the-video.md) |
Details: [AI post-production](../frameworks/ai-post-production.md).

### Step 12: test plan
- Upload PAUSED; separate QA pass; human final yes/no [L93 50:59–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Diversify: different hook **and** different B-roll per variant, not a 3–5 s hook swap alone [L08 03:33–04:26](../lessons/008-how-to-make-diversified-ads.md); see [diversification vs variation](../concepts/diversification-vs-variation.md).
- Read outbound CTR, not CTR (all) [L78 00:52–01:51](../lessons/078-wine-brand-125k-at-2-24-roas.md); a high hook rate alone does not pick the winner [L80 04:11](../lessons/080-supplement-brand-70k-winning-ad-breakdown.md), [L81 04:28](../lessons/081-turning-400-ad-to-13k-spender.md). Thresholds and breakeven: [KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md), [KPI thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md).
- If Meta won't spend on a variant, change the hook audio or lengthen the hook (instructor claim) [L83 35:20–36:17](../lessons/083-ad-roast-calls-2026-08-17.md).
- If the body sells but the hook rate is low, put new visual and copy hooks on the same body at once [L81 08:30–09:24](../lessons/081-turning-400-ad-to-13k-spender.md).
- High CTR with weak conversion on an education-heavy ad: fix the page, not the ad; use the [write-landing-page skill](../../../../../../.claude/skills/write-landing-page/SKILL.md) for an educating PDP [L84 02:57–04:54](../lessons/084-ad-roast-calls-2026-08-21.md).
- After the readout: MORE (variations), BETTER (hooks/brief), NEW (research) [L94 01:30](../lessons/094-research-protocol-start-here.md). Campaign structure: [3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md); shared [test and iterate](../../../../playbooks/test-and-iterate.md).

## Failure → fix
| Symptom | Fix | Source |
|---|---|---|
| Hands and props do odd things | Describe each hand; switch "single continuous shot" to "multiple shots" with camera moves; drop the prop | [L20 06:41–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Product shape or glasses change between shots | Add product references; simplify the action | [L20 09:14–10:15](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Sora won't keep the same face | Don't re-prompt Sora; recreate the person as stills and continue in other models | [L25 02:54](../lessons/025-realistic-ai-ugc-rizz-model-generating-realistic-hook.md) |
| Lip-sync struggles on P words | Source image with mouth closed; regenerate | [L29 03:37](../lessons/029-make-ai-creators-talk.md) |
| Platform rejects a lip-sync clip on privacy grounds | Same image in Kling or Seedance, words spoken slowly, sync in edit | [L84 35:26–36:24](../lessons/084-ad-roast-calls-2026-08-21.md) |
| Interview sounds tinny | Prompt two voices and city ambience | [L26 03:13](../lessons/026-character-consistency.md) |
| Footage too sharp and static | Grade down and add Wiggle | [L12](../lessons/012-make-ai-look-less-fake.md) |
| A model fails a motion | Reverse the clip and generate the opposite motion | [L90 16:01](../lessons/090-ai-editing-2026-08-18.md) |
| Edit "everything got out of sync" | Recheck sync after each change | [L23 09:26](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) |

## Conflicts and defaults
| Topic | Position A | Position B | Default |
|---|---|---|---|
| Best video model for talking people | Seedance 2.0 default ([L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); Kling 3.0 Pro beat Seedance for podcast speaker ([L18](../lessons/018-realistic-ai-podcasts-tutorial.md)) | Google Omni "taking the crown" for podcast/talk formats [L84 51:30](../lessons/084-ad-roast-calls-2026-08-21.md) | All single-test instructor claims; run a 5 s test on two models and keep the better take |
| Seedance audio | Native dialogue with lip-sync (L20 skill) | A face swap keeps the source voice, so replace it [L15 01:38–03:19](../lessons/015-change-creators-with-ai.md) | Native audio for generated scenes; replace voice on any swap |
| Hook-only iteration | "This doesn't work anymore" [L08 03:33–04:26](../lessons/008-how-to-make-diversified-ads.md) | The hook was the only difference between ~$13.6K and ~$477 spend [L81 07:36](../lessons/081-turning-400-ad-to-13k-spender.md) | New tests: diversify concept, hook and B-roll. Proven body with low hook rate: iterate hooks on that body |

## Deliverables template
```markdown
## <Product> — AI UGC ad: <concept name>
**Path:** S | R | P | V · **Awareness:** <stage> · **Avatar:** <one line> · **Offer (exact):** "<…>"
**missing_inputs:** [<item>, …]  · **verify_before_generating:** [<bracketed facts>]

### 1. Script (audited)
| # | Time | Spoken line | On-screen text (≤7 words) | Visual | Claim source / [bracket] |
|---|---|---|---|---|---|
Hooks kept (3, different levers): H1 … H2 … H3 …
Claim audit: passed <date> · AI-character results claims: none · Proof used: <list or "none">

### 2. Prompt pack
| Segment | Duration | Model + settings | References (@Image map) | Prompt (verbatim) | Voice / audio direction |
|---|---|---|---|---|---|

### 3. Reference list
| Ref ID | Type (creator / sheet / scene / prop / product) | File name | Source + rights (synthetic / licensed / own) | Used in |
|---|---|---|---|---|

### 4. Shot QA log  (from ai-video-qa-checklist)
| Clip | Take | Model | Blockers failed | Other fails | Verdict (keep / regen / cut) | Fix applied | Credits |
|---|---|---|---|---|---|---|---|

### 5. Test plan
| Variant | What differs (hook / B-roll / ending / format) | Hypothesis | Primary metric | Read after | Next step if win / lose |
|---|---|---|---|---|---|
Upload: PAUSED · Human approver: <name/role> · Landing page: <url> (fit checked: yes/no)
Roast scorecard: H _/5 C _/5 S _/5 E _/5 = _/20 · Compliance line: pass/fail
```

## Where it's taught
[L08 00:03–04:26](../lessons/008-how-to-make-diversified-ads.md) · [L12 00:00–02:57](../lessons/012-make-ai-look-less-fake.md) · [L13](../lessons/013-live-edit.md) · [L15 00:03–03:19](../lessons/015-change-creators-with-ai.md) · [L16](../lessons/016-clone-broll-ugc-ads.md) · [L17](../lessons/017-ai-podcasts-that-look-real-what-we-are-making.md) · [L18 00:00–07:40](../lessons/018-realistic-ai-podcasts-tutorial.md) · [L19](../lessons/019-realistic-ai-ugc-the-ad-we-are-making.md) · [L20 00:00–13:33](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) · [L21](../lessons/021-street-interviews.md) · [L22](../lessons/022-for-poppy-users.md) · [L23](../lessons/023-18-mins-uncut-live-editing-ai-ugc-video.md) · [L24–L31](../lessons/024-realistic-ai-ugc-rizz-model-the-video-we-are-making.md) · [L33](../lessons/033-sora-2-pro-hooks.md) · [L83](../lessons/083-ad-roast-calls-2026-08-17.md) · [L84](../lessons/084-ad-roast-calls-2026-08-21.md) · [L90](../lessons/090-ai-editing-2026-08-18.md) · [L91](../lessons/091-special-guest-recordings-ai-office-hours-david.md) · [L93](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)

## Cross-course notes
- **Tether Lab (shared):** script structure, hooks and proof rules stay with [UGC script writing](../../../../playbooks/ugc-script-writing.md) and the [UGC script checklist](../../../../rubrics/ugc-script-checklist.md); the shared [ad scorecard](../../../../rubrics/ad-scorecard.md) auto-fails a synthetic person delivering a testimonial (AF8), which matches this playbook's compliance gate.
- **Evolve Copywriting:** [show, don't tell](../../../evolve/copywriting/concepts/show-dont-tell.md) and [open loops](../../../evolve/copywriting/concepts/open-loops.md) agree with the roast feedback; Evolve keeps hook iteration as a core move ([iteration outcomes](../../../evolve/copywriting/concepts/iteration-outcomes.md)) where L08 says hook-only swaps no longer work.
- **RMBC II:** the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) is mandatory on the AI director's prompt pack too, because dialogue lives inside the video prompts.
