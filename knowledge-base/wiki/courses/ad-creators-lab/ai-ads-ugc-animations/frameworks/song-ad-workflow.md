---
title: "Song-ad workflow: research → song script → Suno → timing → visuals → edit (run sheet)"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "unverified (050: Claude greets \"Afternoon, Camilo\"; 051: Suno account camilo593); Loom demo by Boris Vaserv (external resource)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/049-singing-animation-the-ads-we-re-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/050-create-song-style-ad-scripts-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/051-how-to-generate-ai-songs-for-your-brand.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/052-hall-of-fame-singing-ads.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/044-crochet-the-ad-we-are-making.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/047-crochet-editing-final-video.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/resources/ai-song-ad-pipeline-loom.md
tags: [framework, song-ads, singing-ads, suno, claude-prompt, genre-map, awareness-stage, lyrics, animated-ads, compliance-gate, run-sheet]
updated: 2026-11-13
---

# Song-ad workflow
> A song ad is a micro music video whose lyrics are the ad script. The course's chain: a Claude prompt turns research into 2–3 song scripts (lyrics, Suno style prompt, visual idea) after you pick genre, length, angle and one awareness stage; Suno renders the song; the visuals come from the animated pipeline (crochet is the demoed case); the edit is cut to the lyrics. The [Loom song-ad pipeline](../../../../resources/ai-song-ad-pipeline-loom.md) shows the same stages automated with human approval gates.

## 🤖 Agent use
- **Use when:** making a singing/rap/jingle-style animated ad; deciding genre by audience; turning research into lyrics; generating the track in Suno; planning one visual per lyric line.
- **Inputs → outputs:** research doc or website (minimum), target market, verified product facts → `options.md` (2–3 song scripts) → audited `lyrics-final.txt` + `style.txt` → `song-final.mp3` → `timing.csv` → clips → edited ad.
- **Rules:**
  - **DO** make it an ad, not "a song for the sake of it": pick an angle and ONE awareness stage before lyrics [L50 01:47–02:44](../lessons/050-create-song-style-ad-scripts-with-ai.md).
  - **DO** choose genre by audience ("I wouldn't do hip-hop or dubstep for like 50 year old moms") [L51 00:58–01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md); the prompt's genre map covers 20 audiences [L50 prompt](../lessons/050-create-song-style-ad-scripts-with-ai.md#prompts--templates-verbatim).
  - **DO** put the unique mechanism in the lyrics (he added "peroxide powder" and "coconut comfort") [L50 04:34](../lessons/050-create-song-style-ad-scripts-with-ai.md).
  - **DO** claim-audit lyrics **before** Suno: once the song exists, a claim fix means redoing every later stage ([Loom resource](../../../../resources/ai-song-ad-pipeline-loom.md)).
  - **DON'T** name real artists or songs in the Suno style box; Suno rejects it [L51 01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md). Don't pass artist names to Claude either (the lesson does: **don't execute**).
  - **DO** listen end to end and check every product and ingredient word; respell phonetically if mispronounced [L51 01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md).
  - **DO** start the video at the first lyric, not the song intro [L47 00:00](../lessons/047-crochet-editing-final-video.md).
  - **DON'T** name competitor brands in lyrics or on props (course example names three fragrance houses, **don't execute**) [L51 frames](../lessons/051-how-to-generate-ai-songs-for-your-brand.md); [L44 00:15](../lessons/044-crochet-the-ad-we-are-making.md).
  - **IF** characters must visibly sing (mouth moving) **THEN** this is a lip-sync job, not voiceover + B-roll [L91 01:24–02:49](../lessons/091-special-guest-recordings-ai-office-hours-david.md); the course does not demo singing lip-sync (gap).
- **See also:** [AI song-ad pipeline (Loom)](../../../../resources/ai-song-ad-pipeline-loom.md) · [Animated ad production pipeline](animated-ad-production-pipeline.md) · [AI post-production](ai-post-production.md) · [Evolve: market awareness](../../../evolve/copywriting/concepts/market-awareness.md) · [Evolve: unique mechanism](../../../evolve/copywriting/concepts/unique-mechanism.md) · [LLM output claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md)

## Compliance gate (step 4 below; blocks Suno and every later step)
| # | Check | Pass condition | Course example that fails it (**don't execute**) |
|---|---|---|---|
| G1 | Claim audit of lyrics, style idea and visual idea | Time-bound results, health effects and price comparisons verified or cut | Coffee causes "jitters and anxiety", "blocking their way" [L49 00:00](../lessons/049-singing-animation-the-ads-we-re-making.md); "Whiter in a week… Seven days" [L50 04:00](../lessons/050-create-song-style-ad-scripts-with-ai.md); "$35 last eight hours straight", "Used to spend $1,200 every single year" [L44](../lessons/044-crochet-the-ad-we-are-making.md); Loom demo "parasites", "biofilm shield" ([resource](../../../../resources/ai-song-ad-pipeline-loom.md)) |
| G2 | No real-person likeness | Cast invented | Celebrity look-alike singer in the Loom demo ([resource](../../../../resources/ai-song-ad-pipeline-loom.md)) |
| G3 | No real-person voice or style imitation | Style described by genre, tempo, vocal type, production; no artist names | Asking Claude for a hip-hop style "sound like [artist]" [L51 00:58](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| G4 | No competitor names / trademarks | Generic wording ("designer perfume") | "Baccarat, Tom Ford, Creed Aventus too" lyric [L51 00:30](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| G5 | Rights | Suno plan whose terms cover commercial use (verify current terms; derived) | — |

## Run sheet
Tool facts at recording (Aug–Sep 2026). File names are a suggested convention (derived).

| # | Step | Tool / model | Exact settings | Input | Output file | Check | Common failure → fix | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Gather source | — | Pain points, objections, solutions; website URL is the required minimum | research doc / site | `research.md` | Target market stated (else the prompt asks: "moms 50+, dads 40…") | No research and no site → prompt stops | [L50 00:00–00:53](../lessons/050-create-song-style-ad-scripts-with-ai.md) |
| 2 | Run the song prompt | Claude (Opus 4.8 "Low" on screen) | Paste prompt + research; "run this prompt"; answer Step 2 (genre or "help me pick", length 15/30/60 s) and Step 3 (angle + one awareness stage) | `research.md` | `song/options.md` (2–3 options: concept, LYRICS, SUNO STYLE PROMPT, VISUAL IDEA) | Options differ in POV, mood or hook; hook lands in first 5 s; 4–8 syllables/line; angle not brand name | Weak angle → "what other angles / stages can we do?" | [L50 00:53–03:38](../lessons/050-create-song-style-ad-scripts-with-ai.md); prompt [L50](../lessons/050-create-song-style-ad-scripts-with-ai.md#prompts--templates-verbatim) |
| 3 | Refine | Same chat | Add the unique mechanism in ≥1 verse and the chorus; length rule: 15 s hook + one chorus; 30 s verse-chorus-verse-chorus; 60 s full song | chosen option | `song/lyrics-draft.txt`, `song/style.txt` | Mechanism present; style prompt ≤25 words, no banned words ("cinematic", "stunning"…) | Jingle feel ("buy buy buy") → ask for a real verse/chorus | [L50 04:34](../lessons/050-create-song-style-ad-scripts-with-ai.md); prompt rules 1–10 |
| 4 | Compliance gate | [Claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | G1–G5 | draft lyrics + visual idea | `song/lyrics-final.txt`, `claim-audit.md` | Pass | — | derived; [Loom](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 5 | Suno setup | suno.com, **Pro plan** (~$10/month; 2,500 credits vs ~50 free, best model paid-only) | Create → **Advanced**; model v5.5 on screen | — | — | Paid tier active | Free plan "very limiting" (instructor claim) | [L51 00:00–00:30](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| 6 | Generate | Suno | Lyrics box ← `lyrics-final.txt`; Styles box ← descriptive style (genre, vocal, BPM, mood, production); optional negative style; 2–4 takes per genre; try a second genre on the same lyrics | lyrics + style | `song/take-<genre>-NN.mp3` | ICP would "want to consume" it | Style rejected → remove artist/song names; prompt enhancer can expand a short style | [L51 00:58–02:44](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| 7 | Listen-through | — | Whole song; every brand and ingredient word | takes | `song/review.md` | Product name pronounced ("he said Penrose Body Butter perfectly"); lyrics make sense | Mispronounced (page warns on "ashwagandha") → respell, regenerate; like it → upvote + Remix for variants | [L51 01:39–02:44](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| 8 | Export | Suno | Download MP3 | best take | `song/final.mp3` | — | — | [L51 02:44](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) |
| 9 | Timing | Editor | Cut the intro; mark each lyric line start/end | `final.mp3` | `timing.csv` | A new visual roughly every 3 s ("every three seconds you need something new", Loom) | — | [L47 00:00](../lessons/047-crochet-editing-final-video.md); [Loom 03:12](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 10 | Visual plan + cast | Crochet Ad Visuals skill (song-to-visual demo) or `skeleton-ads` Stage 2 | One shot per lyric phrase; cast fixed (lead + small group in the 049 sample) | `lyrics-final.txt` + `timing.csv` | `shotlist.md`, `refs/hero.png` | Every phrase covered | Under-covered lyric → ask the skill for "five fresh ideas" for that half-phrase | [L45](../lessons/045-claude-skill-setup-explanation.md); [L47 01:13](../lessons/047-crochet-editing-final-video.md); [L49 00:35](../lessons/049-singing-animation-the-ads-we-re-making.md) |
| 11 | Keyframes + review gate | per [animated pipeline](animated-ad-production-pipeline.md) steps 6–8 | Hero + product refs on every frame | `shotlist.md` | `frames/` | Second-model review before video spend (Loom) | Bad hand physics, wrong facing → fix frame | [Loom 05:24–07:34](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 12 | Clips | animated pipeline steps 9–11 | Audio off in the video model (the song is the audio) | frames | `clips/NN.mp4` | — | Model adds music → mute | [L46 09:03](../lessons/046-script-visualisation-image-creation.md) |
| 13 | Edit | Editor | Lock the song track; clips to lyrics; speed-adjust inserts; keyframed drift + slight zoom; word-level captions (1–3 words) | clips + `final.mp3` | `edit/song-ad_v1.mp4` | "literally looks like a music video" | Intro left in → cut to first lyric | [L47 00:00–03:27](../lessons/047-crochet-editing-final-video.md); [L49 frames](../lessons/049-singing-animation-the-ads-we-re-making.md) |
| 14 | QA + review | [AI video QA checklist](../rubrics/ai-video-qa-checklist.md); then internal review with specific questions (hook, visual clarity, transitions) | — | `song-ad_v1.mp4` | `export/song-ad_final.mp4` | Gate still true | Redo one shot → point to its timestamp, re-render only that shot (Loom) | [L52 page](../lessons/052-hall-of-fame-singing-ads.md); [Loom 09:37](../../../../resources/ai-song-ad-pipeline-loom.md) |

## Song script anatomy (from the prompt)
- Angle formats: "Stops [pain point]"; "[Desired state] without [common objection]"; "[Product] does what [alternative] can't" [L50 prompt](../lessons/050-create-song-style-ad-scripts-with-ai.md#prompts--templates-verbatim). Rewrite the third format without a competitor's brand name (the prompt's example names one).
- Awareness: pick one of unaware / problem / solution / product / most aware; the demo chose solution aware for "Whiter teeth in seven days without the zaps" [L50 01:47–02:44](../lessons/050-create-song-style-ad-scripts-with-ai.md).
- Style prompt formula: `[genre], [vocal style], [tempo/BPM], [mood], [production style]`, ≤25 words (prompt rule 7). Demo: "upbeat pop, bright female lead, 124 BPM, playful and confident, modern polished production" [L50 04:00](../lessons/050-create-song-style-ad-scripts-with-ai.md).
- Sample structure (049): rhymed couplets → problem escalation → "the old habit was the problem" reveal → switch to product [L49 00:00–00:35](../lessons/049-singing-animation-the-ads-we-re-making.md) (derived).

## Automation map (Loom reference architecture)
| Course step | Loom stage | Human gate in Loom |
|---|---|---|
| 2–4 song script + audit | (script supplied, kept "exactly as written") | — |
| 5–8 Suno | Song | Approve song |
| 10 cast | Visual style + cast | Approve cast |
| 9 timing | Timing (lyrics aligned to audio) | — |
| 10 shot list | Visual plan (~30 min, "the longest part") | optional |
| 11 keyframes | Product references + keyframes + review sub-agent | Approve keyframes; fix 2–3 bad shots |
| 12 clips | Videos | optional per clip |
| 13 edit | Final ad, clean and captioned | Redo by timestamp |
Speeds and error rates in the Loom are the presenter's claims; no performance data is shown ([resource](../../../../resources/ai-song-ad-pipeline-loom.md)). For building it as skills: [Claude Code ad operator](claude-code-ad-operator.md).

## Disagreements and defaults
- **Length:** prompt offers 15/30/60 s; the demo settles on 30–45 s [L50 00:53](../lessons/050-create-song-style-ad-scripts-with-ai.md). **Default:** 30 s first; one 15 s cut-down.
- **Style prompt length:** "under 25 words" (050 prompt rule 7) vs a ~40-word hip-hop style that worked [L51 01:30](../lessons/051-how-to-generate-ai-songs-for-your-brand.md). **Default:** start ≤25 words; lengthen only if the genre is off.
- **Artist references:** "you can definitely not… give it music that sounds like a certain rapper" [L51 01:39](../lessons/051-how-to-generate-ai-songs-for-your-brand.md) vs the instructor naming artists to Claude to get the style [L51 00:58](../lessons/051-how-to-generate-ai-songs-for-your-brand.md). **Default:** no artist names anywhere.

## Where it's taught
- [049 The ads we're making](../lessons/049-singing-animation-the-ads-we-re-making.md): sample song ad [00:00–00:38].
- [050 Song-style scripts](../lessons/050-create-song-style-ad-scripts-with-ai.md): prompt run [00:00], genre and length [00:53], angle + awareness [01:47–03:38], output and mechanism [03:38–04:34].
- [051 AI songs in Suno](../lessons/051-how-to-generate-ai-songs-for-your-brand.md): setup [00:00], style prompt [00:58], checks [01:39], export/remix [02:44].
- [052 Hall of fame](../lessons/052-hall-of-fame-singing-ads.md): review questions only.
- [044](../lessons/044-crochet-the-ad-we-are-making.md), [045](../lessons/045-claude-skill-setup-explanation.md), [047](../lessons/047-crochet-editing-final-video.md): rap song + crochet visuals, edit to lyrics.
- [Loom song-ad pipeline](../../../../resources/ai-song-ad-pipeline-loom.md) [00:00–10:44].

## Related
[Animated ad production pipeline](animated-ad-production-pipeline.md) · [AI ad format catalog](../concepts/ai-ad-format-catalog.md) · [Hook schema and open loops](../concepts/hook-schema-and-open-loops.md) · [Prompt library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md)
