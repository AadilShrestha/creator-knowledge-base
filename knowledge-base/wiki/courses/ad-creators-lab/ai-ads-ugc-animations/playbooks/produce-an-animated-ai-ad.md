---
title: "Playbook: produce an animated AI ad (style pick → script → per-line visuals → character bible → keyframes → start/end video → voice or song → edit → QA → test)"
type: playbook
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (skeleton, crochet, song, claymation, talking-object and Zack D style tutorials where shown; several animated lessons are unattributed); Narek (090); David (091)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/036-skeleton-the-ads-we-re-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/038-skeleton-generating-images.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/039-skeleton-generating-videos.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/040-advanced-video-prompts.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/041-skeleton-generating-voices.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/042-skeleton-editing-the-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/044-crochet-the-ad-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/047-crochet-editing-final-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/049-singing-animation-the-ads-we-re-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/050-create-song-style-ad-scripts-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/051-how-to-generate-ai-songs-for-your-brand.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/053-the-ads-we-are-making-claymation-style.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/054-prompts-frames-chatgpt.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/055-prompts-frames-poppy-method.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/056-claymation-generating-videos-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/057-claymation-generating-voice-over.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/058-editing-claymation-step-by-step.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/059-swipe-file-claymation-ad-scripts.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/062-talking-objects-tutorial.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/063-what-we-are-making-zack-d-films-style.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/064-workflow-breakdown.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/065-script-to-prompt-generator.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/066-zack-d-films-generating-scenes-transitions.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/067-zack-d-films-voice-clone-song.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/084-ad-roast-calls-2026-08-21.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
tags: [playbook, animated-ads, skeleton, crochet, claymation, talking-objects, zack-d-style, song-ads, character-bible, start-end-frame, seedance, kling, elevenlabs, suno, editing, qa]
updated: 2026-11-13
---

# Playbook: produce an animated AI ad
> One procedure for every animated format the course teaches (skeleton, crochet, claymation, talking objects, "Zack D Films" style 3D explainer, singing/song): pick the style, write and audit the script, give every line a visual, lock a character bible, make keyframes, animate start/end-frame pairs on the cheapest model first, add voice or song, edit to the audio, QA, test.

## 🤖 Agent use
- **Use when:** a concept card calls for a stylised, non-human or illustrated format, or a realistic AI person would be a compliance or uncanny-valley risk.
- **Inputs → outputs:** concept card + product facts + product photos + research avatar → audited script, per-line visual table, character bible + hero image, keyframes, video prompts, voice or song, edited 9:16 ad, shot QA log, test plan.
- **Rules:**
  - **DO** write and audit the script first; the voiceover is "the main drive of what our ad will become" [L90 05:06](../lessons/090-ai-editing-2026-08-18.md), and visuals are "not the crux of your ad" [L91 43:53](../lessons/091-special-guest-recordings-ai-office-hours-david.md).
  - **DO** approve one hero character image before any other image, then reference the hero (not the previous image) in every later frame ([L38](../lessons/038-skeleton-generating-images.md); skeleton skill in [L37](../lessons/037-install-skill-generate-script.md)); "otherwise it will change" [L46 07:15, 09:03](../lessons/046-script-visualisation-image-creation.md).
  - **DO** start each stage on the cheapest model (Seedream for images, Seedance 1.5 Pro for video) and move up only for failures or finals [L46 03:28, 06:16](../lessons/046-script-visualisation-image-creation.md); [L56 05:07](../lessons/056-claymation-generating-videos-transitions.md).
  - **DO** keep clips short (3–4 s) with audio off at 720p; sound goes in the edit [L56 01:00; 07:12–08:13](../lessons/056-claymation-generating-videos-transitions.md).
  - **DON'T** put captions, words, labels or watermarks into image or video prompts; captions are added in the editor ([L37 skill](../lessons/037-install-skill-generate-script.md); [L38](../lessons/038-skeleton-generating-images.md)).
  - **DON'T** clone or imitate a named creator's voice or style-with-voice ([L67](../lessons/067-zack-d-films-voice-clone-song.md)), name real artists in song prompts ([L51](../lessons/051-how-to-generate-ai-songs-for-your-brand.md)), or rip SFX from YouTube ([L58 03:33](../lessons/058-editing-claymation-step-by-step.md)): **don't execute**.
  - **DON'T** keep the demo scripts' health and result claims (GLP-1, hair/muscle loss, IGF-1, testosterone, cellulite, "$1,000/day"): they are course examples, not usable claims ([L37 00:57](../lessons/037-install-skill-generate-script.md), [L65](../lessons/065-script-to-prompt-generator.md), [L59](../lessons/059-swipe-file-claymation-ad-scripts.md)).
  - **IF** a model fails a motion **THEN** reverse the clip in the editor and generate the opposite motion [L90 16:01](../lessons/090-ai-editing-2026-08-18.md).
- **See also:** [Animated ad production pipeline](../frameworks/animated-ad-production-pipeline.md) · [Song ad workflow](../frameworks/song-ad-workflow.md) · [Start/end-frame video](../concepts/start-end-frame-video.md) · [Character consistency](../concepts/character-consistency.md) · [AI post-production](../frameworks/ai-post-production.md) · [AI ad format catalog](../concepts/ai-ad-format-catalog.md) · [Prompts library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md) · [AI song-ad pipeline (Loom)](../../../../resources/ai-song-ad-pipeline-loom.md) · [ElevenLabs](../../../../tools/elevenlabs.md)

## Inputs required up front
| Input | Why | If missing |
|---|---|---|
| Concept card (angle, awareness stage, avatar) | Picks the style and hook | Run [research to AI ad concepts](research-to-ai-ad-concepts.md) |
| Product facts + mechanism | Animated formats sell by **showing** the mechanism [L84 46:27, 50:03](../lessons/084-ad-roast-calls-2026-08-21.md) | Bracket the mechanism; no visual of an unverified effect |
| Claims allowed / forbidden | Demo scripts in this module are claim-heavy | Treat outcome claims as forbidden |
| Real customer language + failed solutions | Talking-object scripts attack a misconception from failed solutions [L62 00:00–01:40](../lessons/062-talking-objects-tutorial.md) | Hypothesis label; mine per [L97](../lessons/097-customer-research-protocol-1.md) |
| Research avatar | The character is described from research: "Make sure don't make things up" [L46 01:31](../lessons/046-script-visualisation-image-creation.md) | Generic character; flag |
| Product photos (pack, label, several angles) | Product must look like the real one [L84 50:57](../lessons/084-ad-roast-calls-2026-08-21.md) | No product-in-frame shots |
| Offer, CTA, landing page | End card and funnel fit | `[OFFER]` placeholder |
| Tools + budget (Claude skills, Max Fusion or similar, ElevenLabs, Suno for songs, editor) | Model ladder and credits | Flag; keep to cheapest models |

## Step 2 decision: pick the style
| Style | What it is | Fits (from course) | Script engine | Images → video | Lessons |
|---|---|---|---|---|---|
| Skeleton | Skeleton character acts out "What happens if you ___? Day 1 … Day 30" | Body/health effects shown on bones; four styles: X-Ray (health/body), Dressed (wearable), Mascot (playful), Bare-Bones (default) [L38](../lessons/038-skeleton-generating-images.md) | `skeleton-ads` Claude skill, 4 stages [L37](../lessons/037-install-skill-generate-script.md) | Seedream 4.5 hero → per-shot; Seedance 1.5 Pro → Kling 2.6 → Kling 3.0 Pro [L39 00:58](../lessons/039-skeleton-generating-videos.md) | [L36–L43](../lessons/036-skeleton-the-ads-we-re-making.md) |
| Crochet | Knitted characters, yarn "orbs" as the effect | Problem → mechanism → fix → social payoff in six lines [L44](../lessons/044-crochet-the-ad-we-are-making.md); avoid complex hands in yarn ([L45 skill](../lessons/045-claude-skill-setup-explanation.md)) | "Crochet Ad Visuals" skill, `/crochet add visuals` [L46 01:31](../lessons/046-script-visualisation-image-creation.md) | Seedream frames → Seedance 1.5 Pro 5 s start/end [L46](../lessons/046-script-visualisation-image-creation.md) | [L44–L48](../lessons/044-crochet-the-ad-we-are-making.md) |
| Claymation | Stop-motion clay scenes with transitions | Before/after transformation per line | Claymation GPT [L54](../lessons/054-prompts-frames-chatgpt.md) or Poppy board [L55](../lessons/055-prompts-frames-poppy-method.md) | Nano Banana 2 stills → start = N, end = N+1, Seedance then Kling 3.0 Pro [L56](../lessons/056-claymation-generating-videos-transitions.md) | [L53–L60](../lessons/053-the-ads-we-are-making-claymation-style.md), [L90](../lessons/090-ai-editing-2026-08-18.md) |
| Talking object | A product, ingredient or failed solution speaks | Attacking a misconception about a failed solution [L62](../lessons/062-talking-objects-tutorial.md); objection Q&A for services [L83 36:47](../lessons/083-ad-roast-calls-2026-08-17.md) | Object Talk GPT or your own Claude prompt [L62 01:40](../lessons/062-talking-objects-tutorial.md) | Seedream / Nano Banana image (4–6 variants) → Seedance for timing → Veo or Kling for lip-sync, 8–10 s [L62 02:31–09:04](../lessons/062-talking-objects-tutorial.md) | [L61–L62](../lessons/062-talking-objects-tutorial.md) |
| "Zack D" style 3D explainer | 3D-animated body/science explainer with start/end-frame transitions | Mechanism explainers; product reveal held to the end [L83 46:42](../lessons/083-ad-roast-calls-2026-08-17.md) | Audio / Text / Visual table [L64 01:52](../lessons/064-workflow-breakdown.md) + script-to-prompt GPT [L65](../lessons/065-script-to-prompt-generator.md) | Start frame → end frame as a variation → Seedance 1.5 Pro transition [L66](../lessons/066-zack-d-films-generating-scenes-transitions.md) | [L63–L68](../lessons/063-what-we-are-making-zack-d-films-style.md) |
| Song / singing | Lyrics ad with animated or lip-synced visuals | Problem couplets, escalation, product last [L49](../lessons/049-singing-animation-the-ads-we-re-making.md) | Song script prompt in Claude [L50](../lessons/050-create-song-style-ad-scripts-with-ai.md) → Suno [L51](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) | Any style above, cut to lyrics [L47](../lessons/047-crochet-editing-final-video.md) | [L49–L52](../lessons/049-singing-animation-the-ads-we-re-making.md), [song workflow](../frameworks/song-ad-workflow.md) |
Awareness stage, cost and time per format: [AI ad format catalog](../concepts/ai-ad-format-catalog.md). Don't label an ad as a style it isn't ("claymation" on a non-claymation video) [L84 46:27, 50:57](../lessons/084-ad-roast-calls-2026-08-21.md).

## The chain
| # | Step | Do | Output | Gate |
|---|---|---|---|---|
| 1 | Intake | Fill inputs; avatar, awareness, market, offer at top [L83 11:18](../lessons/083-ad-roast-calls-2026-08-17.md) | `intake` + `missing_inputs` | No unbracketed claim |
| 2 | Style | Pick from the table | `style` | Style shows the mechanism |
| 3 | Script | Style engine (skill/GPT/prompt) + [write-ugc-script skill](../../../../../../.claude/skills/write-ugc-script/SKILL.md) line edit | Script + VO line list | Read aloud; every line visual |
| 4 | Claim audit | [RMBC claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | Audited script | Demo claims removed |
| 5 | Visual table | One visual per line / phrase | Audio / Text / Visual table | Every noun shown on its word |
| 6 | Character bible + hero | Describe from research; generate, approve, save as reference | Bible text + hero image | Hero approved before any shot |
| 7 | Keyframes | Start frame per line; end frame only where state changes (Type B) | Numbered stills | Same character, product correct, no text |
| 8 | Voice or song | ElevenLabs Voice Design + v3, or Suno song | VO / song file | Names pronounced; licence clear |
| 9 | Video | Start/end-frame pairs, short clips, cheap model first | Clips | Cost approved; 4–5 takes max per shot before rethink |
| 10 | Shot QA | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | Shot QA log | No blocker failed |
| 11 | Edit | Audio master; clips per line; zooms, ramps, SFX, captions, style pass | 9:16 master + hook variants | Safe zone, sync |
| 12 | Score + test | [Roast scorecard](../rubrics/ad-roast-scorecard.md); paused upload; test plan | Scorecard + test plan | Pass marks; human yes/no |

## Step details

### Step 3: script
- Skeleton: install the skill (Claude → Customize → Skills → + → Upload skill), give the research doc or product page text, confirm the "examine skill" step appears, ask for another style if the first is generic [L37 00:00–00:57](../lessons/037-install-skill-generate-script.md). Skill output: 5–7 beats, ~110–160 words for 30–60 s, second person present tense, no corporate words ([L37 skill](../lessons/037-install-skill-generate-script.md)).
- Song: run the song prompt with the research file attached; choose genre by audience, length by platform (prompt offers 15 / 30 / 60 s; demo 30–45 s), angle and awareness by funnel position; refine for the unique mechanism [L50 00:00–04:34](../lessons/050-create-song-style-ad-scripts-with-ai.md).
- Talking object / Zack D: list 3–5 failed solutions and pick the clearest misconception [L62 00:00–01:40](../lessons/062-talking-objects-tutorial.md); write hooks + body as usual, then a table Audio / Text / Visual [L64 00:45–01:52](../lessons/064-workflow-breakdown.md).
- Reveal: hold or blur the product until the sale is made [L83 46:42](../lessons/083-ad-roast-calls-2026-08-17.md); keep a reason to watch past 10 seconds [L84 43:28](../lessons/084-ad-roast-calls-2026-08-21.md).
- Don't rely on the LLM for the visual idea: take its idea and add your own (instructor claim) [L90 1:06:22–1:08:51](../lessons/090-ai-editing-2026-08-18.md).

### Step 5: per-line visual table
- Skeleton: paste the final script back to get the concept board; "you don't have to follow any of this verbatim" [L37 01:46](../lessons/037-install-skill-generate-script.md). Abstract benefit → visible physical image (skill table, [L37](../lessons/037-install-skill-generate-script.md)).
- Crochet: pick one of five visuals per phrase ("Phrase 1: 2, Phrase 2: 4") [L46](../lessons/046-script-visualisation-image-creation.md).
- Show the mechanism, not text: scent blobs mixing, particles bouncing off a barrier [L84 46:27; 50:03](../lessons/084-ad-roast-calls-2026-08-21.md); make each "I tried that" line a shown attempt [L84 10:52](../lessons/084-ad-roast-calls-2026-08-21.md).
- Budget 2–3 extra shots for contrast pairs and lines with no visual [L42 04:58–06:54](../lessons/042-skeleton-editing-the-video.md); [L47 01:13](../lessons/047-crochet-editing-final-video.md).

### Step 6–7: character bible and keyframes
- Character description is not a prompt: "Don't use it as a prompt. It doesn't work." [L46 01:31](../lessons/046-script-visualisation-image-creation.md). Generate the character image (3 variants, Seedream) and save it as the reference [L46 02:37](../lessons/046-script-visualisation-image-creation.md).
- Keep the same character by **editing** from the saved reference, not regenerating [L54](../lessons/054-prompts-frames-chatgpt.md); fix drift by reconnecting the first character image and adding "Keeping the character the same" [L55 05:02–05:50](../lessons/055-prompts-frames-poppy-method.md).
- Attach the product photo whenever the product is in frame; he forgot once and redid it [L46 08:14](../lessons/046-script-visualisation-image-creation.md).
- Frame type per shot (Crochet skill): **Type A** start frame only, motion self-contained (default when unsure); **Type B** start + end frame, state changes; **Type C** start frame only, held or subtle motion. End frames are final landed states, never mid-motion ([L45 skill](../lessons/045-claude-skill-setup-explanation.md)). See [start/end-frame video](../concepts/start-end-frame-video.md).
- Zack D / claymation transitions: end frame = a variation of the start image, or the next scene's still [L65 01:48–02:45](../lessons/065-script-to-prompt-generator.md); [L66 00:00–00:55](../lessons/066-zack-d-films-generating-scenes-transitions.md); [L56](../lessons/056-claymation-generating-videos-transitions.md).
- Exact item a character must hold (a garment, a screen): give a screenshot reference to Nano Banana Pro [L40](../lessons/040-advanced-video-prompts.md); use licensed or self-shot clips, not a stranger's UGC.
- Edit a close frame conversationally ("make him look even more sad") rather than re-prompting [L46 05:18](../lessons/046-script-visualisation-image-creation.md).

### Step 8: voice or song
- Voice: ElevenLabs → Voice Design; prompt demographic + delivery, calm not over the top; Text to Speech → Eleven v3 with tags → Enhance → Generate; check brand-name pronunciation [L41](../lessons/041-skeleton-generating-voices.md), [L57](../lessons/057-claymation-generating-voice-over.md). Whole script in one take [L91 50:13](../lessons/091-special-guest-recordings-ai-office-hours-david.md).
- Zack D lesson clones a well-known creator's voice from YouTube [L67](../lessons/067-zack-d-films-voice-clone-song.md): **don't execute**. Compliant: describe a voice in Voice Design; licensed music bed covering paid ads; keep the licence.
- Song: Suno → Create → Advanced; paste lyrics; style prompt written with Claude: genre + vocal + tempo + mood + production, no artist names [L51 00:58–01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md); generate several takes; listen end to end for product name and ingredients [L51 01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md); download MP3 [L51 02:44](../lessons/051-how-to-generate-ai-songs-for-your-brand.md). Full flow: [song ad workflow](../frameworks/song-ad-workflow.md).

### Step 9: video generation (at recording, Aug–Sep 2026)
| Rule | Source |
|---|---|
| Start = scene N, end = scene N+1 for transitions; 9:16, 3–4 s, audio off, 720p, not Pro | [L56 00:00–08:13](../lessons/056-claymation-generating-videos-transitions.md) |
| Claymation prompt = visual direction + camera direction + "Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon." | [L56 01:58](../lessons/056-claymation-generating-videos-transitions.md) |
| Add "Keep character facial consistency. No character redesign. No facial feature changes." when a character appears | [L56 01:00](../lessons/056-claymation-generating-videos-transitions.md) |
| Name one camera move (static / slight push-in / slow pan / arc); don't stack moves or put dialogue in video prompts | [L56 01:00](../lessons/056-claymation-generating-videos-transitions.md); [L39 skill Stage 4](../lessons/039-skeleton-generating-videos.md) |
| Ladder: Seedance 1.5 Pro (~8 credits per 4 s in L39; ~1 credit vs Kling 3.0 Pro 2.4 per 4 s in L56) → Kling 2.6 → Kling 3.0 Pro for finals | [L39 00:58–01:28](../lessons/039-skeleton-generating-videos.md); [L56 01:00; 05:07](../lessons/056-claymation-generating-videos-transitions.md) |
| Seedance 1.5 may add music: prompt for none or use Kling | [L39 01:28–02:03](../lessons/039-skeleton-generating-videos.md) |
| 4–5 takes per scene; chain by snapshotting the last frame as the next first frame; sharpen a blurry snapshot in GPT Image 2 at 2K/4K first | [L90 12:29; 17:40; 43:35–44:55](../lessons/090-ai-editing-2026-08-18.md) |
| Generate the model minimum (3 s) and speed it to the measured gap | [L90 30:31–31:06](../lessons/090-ai-editing-2026-08-18.md) |
| Claude / Claude Code can drive generation through a Higgsfield or Max Fusion MCP/API | [L39 02:39](../lessons/039-skeleton-generating-videos.md); [Claude Code ad operator](../frameworks/claude-code-ad-operator.md) |
Credit figures differ between lessons and date fast; use [tool settings](../libraries/tool-settings.md).

### Step 11: edit
| Do | Source |
|---|---|
| VO (or song) on the timeline first; strip pauses; lock the audio layer | [L90 06:04](../lessons/090-ai-editing-2026-08-18.md); [L58 00:00](../lessons/058-editing-claymation-step-by-step.md) |
| Song: start at the first lyric, not the intro | [L47 00:00](../lessons/047-crochet-editing-final-video.md) |
| Place clips line by line; show the named thing on its word | [L42 00:58–01:57](../lessons/042-skeleton-editing-the-video.md) |
| Cut every 2–3 s | [L90 31:37](../lessons/090-ai-editing-2026-08-18.md) |
| Keyframed slow zooms / drifts; matched zoom direction | [L42 03:03–05:54](../lessons/042-skeleton-editing-the-video.md); [L47 03:27](../lessons/047-crochet-editing-final-video.md) |
| Speed-curve flash out / flash in on seams, ramp aligned to the key word | [L58 01:29–03:33](../lessons/058-editing-claymation-step-by-step.md) |
| Licensed SFX per action, mixed under the voice | [L58 03:33–05:44](../lessons/058-editing-claymation-step-by-step.md) |
| Claymation: Posterize Time on an adjustment layer, 15 fps on screen | [L90 37:26–39:02](../lessons/090-ai-editing-2026-08-18.md) |
| Captions: one line, thick stroke, 2–3 words [L42 07:56–10:49](../lessons/042-skeleton-editing-the-video.md); Premiere max 15 characters, 2 s, single line [L90 51:33](../lessons/090-ai-editing-2026-08-18.md); identity caption ("POV …") [L42 10:49](../lessons/042-skeleton-editing-the-video.md) | |
| Fix glitches in post (brush skin colour, hue, reverse) instead of only regenerating | [L90 14:00–15:31; 22:11](../lessons/090-ai-editing-2026-08-18.md) |
| Music matching the style ("sneaky… jazz" for claymation) | [L90 24:09](../lessons/090-ai-editing-2026-08-18.md) |
| Export and make 2–3 hook variants | [L42 11:53](../lessons/042-skeleton-editing-the-video.md) |
Time budget (instructor claim): about four hours per one-minute claymation ad [L90 49:40](../lessons/090-ai-editing-2026-08-18.md); Narek delivers in one to one and a half days [L90 48:58](../lessons/090-ai-editing-2026-08-18.md).

### Step 12: test
Same rules as the [AI UGC playbook test plan](produce-an-ai-ugc-ad.md#step-12-test-plan): paused upload, concept-level diversity [L08](../lessons/008-how-to-make-diversified-ads.md), outbound CTR, hook iteration on proven bodies, MORE / BETTER / NEW [L94 01:30](../lessons/094-research-protocol-start-here.md). For animated formats also test a product-light version against a product-heavy one [L84 06:23](../lessons/084-ad-roast-calls-2026-08-21.md).

## Failure → fix
| Symptom | Fix | Source |
|---|---|---|
| Character changes between shots | Reference the hero, not the previous image; edit from reference | [L37 skill](../lessons/037-install-skill-generate-script.md); [L54](../lessons/054-prompts-frames-chatgpt.md) |
| Kling drifts on claymation | Use Seedance for claymation | [L90 1:09:39–1:10:20](../lessons/090-ai-editing-2026-08-18.md) |
| Unwanted music in a clip | Prompt "no music" or switch to Kling | [L39 01:28](../lessons/039-skeleton-generating-videos.md) |
| Yarn hands look wrong | Simplify poses: standing, sitting, single-arm gestures | [L45 skill](../lessons/045-claude-skill-setup-explanation.md) |
| Text in a talking-object image wrong | Variation prompt: bigger, corrected text; or add text in the edit | [L62 03:21](../lessons/062-talking-objects-tutorial.md); [L65](../lessons/065-script-to-prompt-generator.md) |
| Lyric with no shot | Ask the skill for new visuals for that phrase; generate an insert; speed to fit | [L47 01:13–02:21](../lessons/047-crochet-editing-final-video.md) |
| Low shot angle loses a figure | Keep legible framing | [L84 44:23](../lessons/084-ad-roast-calls-2026-08-21.md) |

## Conflicts and defaults
| Topic | Position A | Position B | Default |
|---|---|---|---|
| Best animation model | Kling 3.0 Pro "the best" [L39 00:58](../lessons/039-skeleton-generating-videos.md); Kling 3.0 "best quality" for claymation finals [L56](../lessons/056-claymation-generating-videos-transitions.md) | "Seedance 1.5 was better" than 2.0 in crochet, Kling "way nicer" [L46 09:03](../lessons/046-script-visualisation-image-creation.md); Seedance over Kling for claymation because Kling drifts [L90 1:09:39](../lessons/090-ai-editing-2026-08-18.md) | Cheapest model first; compare two finalists on the failed shot only |
| Script vs visuals first | Script first, visuals are a tool [L91 43:53](../lessons/091-special-guest-recordings-ai-office-hours-david.md); VO is the master [L90 05:06](../lessons/090-ai-editing-2026-08-18.md) | Animated lessons often open with the visual style ([L36](../lessons/036-skeleton-the-ads-we-re-making.md), [L53](../lessons/053-the-ads-we-are-making-claymation-style.md)) | Audited script first; style choice may come before the script, shots after it |
| Posterize Time value | "set to 50" spoken | Frame Rate 15.0 on screen [L90 38:20](../lessons/090-ai-editing-2026-08-18.md) | 15 fps |
| Song length | Prompt offers 15 / 30 / 60 s | Demo 30–45 s [L50 00:53](../lessons/050-create-song-style-ad-scripts-with-ai.md) | 30 s for cold traffic tests, 45–60 s only if retention holds (derived) |

## Deliverables template
```markdown
## <Product> — animated AI ad: <style> / <concept>
**Awareness:** <stage> · **Avatar:** <one line> · **Offer (exact):** "<…>"
**missing_inputs:** [...] · **verify_before_generating:** [...]

### 1. Script (audited) + visual table
| # | VO / lyric line | On-screen text | Visual (frame type A/B/C) | Duration | Claim source / [bracket] |
|---|---|---|---|---|---|

### 2. Character bible
<one paragraph from research; hero image file; product reference files>

### 3. Prompt pack
| Shot | Start-frame prompt | End-frame prompt (Type B only) | Video prompt (direction + camera + suffix) | Model / duration / res / audio | Refs |
|---|---|---|---|---|---|
Voice: <Voice Design description, model, tags> · Song: <style prompt, no artist names, Suno take id>

### 4. Reference list
| Ref ID | Type (hero / product / scene / style) | File | Source + rights | Used in shots |
|---|---|---|---|---|

### 5. Shot QA log
| Shot | Take | Model | Blockers failed | Other fails | Verdict | Fix | Credits |
|---|---|---|---|---|---|---|---|

### 6. Test plan
| Variant | Differs by | Hypothesis | Metric | Read after | Next step |
|---|---|---|---|---|---|
Music/SFX licences: <list> · Upload PAUSED · Approver: <role>
Roast scorecard: H _/5 C _/5 S _/5 E _/5 = _/20 · Compliance line: pass/fail
```

## Where it's taught
Skeleton [L36–L43](../lessons/036-skeleton-the-ads-we-re-making.md) · crochet [L44–L48](../lessons/044-crochet-the-ad-we-are-making.md) · song [L49–L52](../lessons/049-singing-animation-the-ads-we-re-making.md) · claymation [L53–L60](../lessons/053-the-ads-we-are-making-claymation-style.md) · talking objects [L61–L62](../lessons/062-talking-objects-tutorial.md) · Zack D style [L63–L68](../lessons/063-what-we-are-making-zack-d-films-style.md) · AI editing [L90](../lessons/090-ai-editing-2026-08-18.md) · roasts of animated ads [L83 45:20–50:12](../lessons/083-ad-roast-calls-2026-08-17.md), [L84 41:37–51:30](../lessons/084-ad-roast-calls-2026-08-21.md) · guest [L91](../lessons/091-special-guest-recordings-ai-office-hours-david.md)

## Cross-course notes
- **Tether Lab (shared):** [format variation ladder](../../../../frameworks/format-variation-ladder.md) and [humor in ads](../../../../concepts/humor-in-ads.md) cover when a stylised format helps; this playbook adds the production method.
- **Evolve Copywriting:** [show, don't tell](../../../evolve/copywriting/concepts/show-dont-tell.md) and [unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md) are the reason these formats work: they make the mechanism visible.
- **RMBC II:** the [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) runs on lyrics too; song prompts produce time claims ("in 7 days") that need substantiation ([L50](../lessons/050-create-song-style-ad-scripts-with-ai.md)).
