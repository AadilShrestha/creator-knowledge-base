---
title: "Claude Code as ad operator: skills as production units, repo and skill layout, feedback loop into the skill file, batch runs, human gates"
type: framework
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Camilo (020, 045; 050 screen-shared from his account); 037 unverified (same screen-share style); David (091, AI office hours); Caleb Kruse 'Mr. Paid Social' (093, guest); Boris Vaserv (Loom resource, outside the course)"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/020-claude-skill-seedance-2-0-ai-ugc.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/037-install-skill-generate-script.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/038-skeleton-generating-images.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/039-skeleton-generating-videos.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/045-claude-skill-setup-explanation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/046-script-visualisation-image-creation.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/050-create-song-style-ad-scripts-with-ai.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/083-ad-roast-calls-2026-08-17.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/090-ai-editing-2026-08-18.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/091-special-guest-recordings-ai-office-hours-david.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md
  - knowledge-base/wiki/resources/ai-song-ad-pipeline-loom.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/concepts/claude-project-recipe.md
tags: [claude-code, claude-skills, agents, automation, ai-production, skill-design, references, feedback-loop, batch-generation, cost-control, qa-agent, human-gates, meta-api, paused-ads, secrets, compliance]
updated: 2026-11-13
---

# Claude Code as ad operator
> A design for running AI ad production with Claude skills, assembled from the course's four shipped skills (Seedance UGC Ad Director, skeleton-ads, Crochet Ad Visuals, the song-script prompt), David's style-skill method, Caleb Kruse's Claude Code studio and the Loom song-ad pipeline: one skill per format, each with a references folder; a brand master-context file the skills read; a feedback loop that writes every production failure back into the skill; batch runs with cost approval, a smoke test and a second-agent QA pass; and seven human gates, the last being a paused upload. Sections marked (derived) are this page's design, not something a lesson shows.

## 🤖 Agent use
- **Use when:** setting up or running Claude (Desktop skills or Claude Code) to produce ad scripts, prompts, images, videos or static batches; writing or improving a format skill; planning a batch run; deciding where a human must approve.
- **Inputs → outputs:** brand master context (product facts, verified and banned claims, offer, model prices), research doc, claim-audited script or concept, real product reference images, reference ads/frames, generation API or MCP access, ad-account token in a secrets store → skill outputs per stage (director's brief, prompts, stills, clips, statics), a cost estimate, a review page, a QA report, paused ads, and a log entry that updates the skill.
- **Rules:**
  - **DO** make one skill per format, as the course does (UGC/Seedance, skeleton, crochet, song; claymation and Pixar skills mentioned) [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L37](../lessons/037-install-skill-generate-script.md); [L45](../lessons/045-claude-skill-setup-explanation.md); [L90 40:39–41:35](../lessons/090-ai-editing-2026-08-18.md).
  - **DO** confirm the skill was read before trusting output: "if it's not doing that and it's just giving you an output it's wrong, you need to try again" [L20 00:54](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L46 01:31](../lessons/046-script-visualisation-image-creation.md).
  - **DO** write the master context first; "skipping the master context" is the first beginner trap [L93 19:50; 48:59](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
  - **DO** build skills from real references and iteration, then have Claude distil the session: "Review this entire Claude Code session… and distill it into a skill that we can call again" [L93 18:31](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); without a reference frame "Claude has no idea how to do a claymation" [L91 56:57](../lessons/091-special-guest-recordings-ai-office-hours-david.md).
  - **DO** estimate cost, get approval, smoke-test one output, then fire batches of 10 [L93 36:11–38:40](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
  - **DO** run a second, separate QA agent on the first agent's output and keep a human final yes/no [L93 50:59–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); review keyframes before paying for video [Loom 05:24; 06:33–07:34](../../../../resources/ai-song-ad-pipeline-loom.md).
  - **DO** claim-audit the script before any audio or visual is generated: once a song exists, a claim fix means redoing every later stage [Loom how-to-apply](../../../../resources/ai-song-ad-pipeline-loom.md).
  - **DO** keep API keys in `.env` or a secrets manager, never in chat; upload ads PAUSED only [L93 46:22–47:25; 50:59](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
  - **DON'T** let a skill forbid asking for missing inputs: the Seedance skill says "Do NOT ask clarifying questions" [L20 skill rule 5](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); repo rule 1 (real inputs first) overrides it. Ask once, in one batch, as skeleton-ads does [L37 Stage 1](../lessons/037-install-skill-generate-script.md).
  - **DON'T** put client data in shared skills (Evolve's skill copy was rebuilt for NDA reasons) [Evolve CW L47 00:00](../../../evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md).
  - **IF** the AI writes visuals **THEN** expect them to be "too simple"; take its idea and add your own [L90 1:06:22–1:08:51](../lessons/090-ai-editing-2026-08-18.md).
- **See also:** [Prompts library](../libraries/prompts.md) (every course prompt and skill) · [Tool settings](../libraries/tool-settings.md) · [AI UGC Seedance workflow](ai-ugc-seedance-workflow.md) · [Animated ad production pipeline](animated-ad-production-pipeline.md) · [Song ad workflow](song-ad-workflow.md) · [AI post-production](ai-post-production.md) · [Static ads process](static-ads-process.md) · [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) · [AI creator compliance](../concepts/ai-creator-compliance.md) · [Reference-first prompting](../concepts/reference-first-prompting.md) · [Character consistency](../concepts/character-consistency.md) · Resource: [AI song-ad pipeline (Loom)](../../../../resources/ai-song-ad-pipeline-loom.md) · Repo skills: [write-ugc-script](../../../../../../.claude/skills/write-ugc-script/SKILL.md), [write-landing-page](../../../../../../.claude/skills/write-landing-page/SKILL.md) · RMBC: [Claude Project recipe](../../../stefan-georgi/rmbc-ii/concepts/claude-project-recipe.md), [LLM copy-chief editing](../../../stefan-georgi/rmbc-ii/concepts/llm-copy-chief-editing.md), [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md)

## 1. What the course shows (evidence)
| Source | Unit | Key mechanics an operator should copy | Lessons |
|---|---|---|---|
| Seedance 2.0 UGC Ad Director | Claude Desktop skill (`/seedance`) | Mandatory rules at top; exact output format; Pinterest reference searches before prompts; `@Image1` creator / `@Image3` product mapping; ≤15 s segments with 5 s timed blocks; anti-cinematic word lists; audio and room-tone rules; model facts (9 images + 3 videos + 3 audio inputs; 4-15 s output) | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| skeleton-ads | Skill with 4 stages in one chat | Trigger phrases in the description; stage-detection table routes by what the user pasted; ends each stage with the exact hand-off; Strategist Playbook (angle choice with one-line rationale); Character Bible pasted verbatim; three-layer consistency (locked text, hero image, reference image 1 not the previous image); per-tool tables; "What you DON'T do"; worked example + swipe file | [L37](../lessons/037-install-skill-generate-script.md); [L38](../lessons/038-skeleton-generating-images.md); [L39](../lessons/039-skeleton-generating-videos.md) |
| Crochet Ad Visuals | Skill, Step 0 → 1 → 2 | Character question first; 5 visual ideas per phrase; Type A/B/C frame decision; universal positive, negative and I2V closing line baked into every prompt; "Known Model Limitations & Workarounds" section written from failed generations; quality-bar storyboard | [L45](../lessons/045-claude-skill-setup-explanation.md); [L46](../lessons/046-script-visualisation-image-creation.md) |
| Song-style ad script prompt | Prompt run in a Claude chat with the research doc attached | Step-by-step questions (genre or "help me pick", length, market); forces one angle and ONE awareness stage before lyrics; 2-3 meaningfully different options with lyrics, Suno style prompt (<25 words), visual idea | [L50](../lessons/050-create-song-style-ad-scripts-with-ai.md) |
| David's style-skill method | Reference frames → tests → feedback → skill | Extract frames; generate tests in several scenes (Nano Banana 2); paste good and bad outputs back and ask for reinforcement; fixes named (more light for clean claymation, skin colour, emotion wording); ask Claude to write the skill once results are consistent; analyse reference ads as three separate layers (visual, audio, script); script first | [L91 05:14–14:49; 41:26–43:53; 55:33–56:57](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| Caleb Kruse's Claude Code studio | Repo: master context + 10 skills + 9 model specs + 37 static templates + 2,000-ad Airtable library | Session → skill distillation; cost per credit in context; plan + estimate + approval + smoke test; batches of 10 to the API; parallel sub-agents; self-healing retries; HTML review page; "AI giveaway" self-QA with V1/V2 doc; session log and architecture doc read at every new session; `.env` token; 5 primary texts × 5 headlines from the account's top copy; paused upload; separate launch-QA agent | [L93 18:31–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| Loom song-ad pipeline | Coordinator skill + workflow skill + CLI + review web app | Fixed stages with approval buttons (song, cast, keyframes); review sub-agent over the storyboard; per-shot redo by timestamp; product references stored once per product; 10 scripts in parallel; secrets manager | [Loom](../../../../resources/ai-song-ad-pipeline-loom.md) |
| Edit skills | Claude Code + MCP (Max Fusion, Higgsfield) | Dial in one edit, then save it as a command (`/claymation edit`: trim first half-second, music, slow zooms, subtitles, caption); Claude Code sends prompts straight to the generator via API/MCP | [L83 50:43–51:41](../lessons/083-ad-roast-calls-2026-08-17.md); [L39 02:39–03:37](../lessons/039-skeleton-generating-videos.md) |

## 2. Architecture (derived from the table above)
| Layer | Holds | Read by | Source pattern |
|---|---|---|---|
| Master context (per brand) | Product facts, verified claims, banned claims, offer, audience, voice, model prices per credit | Every skill, first | [L93 19:50](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| Research doc (per brand) | Customer language, objections, personas (hypotheses) | Script and concept skills | [L50 00:00](../lessons/050-create-song-style-ad-scripts-with-ai.md); [research document protocol](research-document-protocol.md) |
| Format skills | One per format: SKILL.md + references folder | Claude, on trigger | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md), [L37](../lessons/037-install-skill-generate-script.md), [L45](../lessons/045-claude-skill-setup-explanation.md) |
| Service skills | QA, claim audit, cost estimate, publish-paused, edit | Coordinator | [L93](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L83 51:41](../lessons/083-ad-roast-calls-2026-08-17.md) |
| Reference library | Tagged reference ads with recreation notes; Pinterest/real frames per style | Format skills | [L93 24:16–26:54](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| Asset store | Product packshots (once per product), character sheets, hero images | Image/video steps | [Loom 09:37](../../../../resources/ai-song-ad-pipeline-loom.md); [L37 Stage 3](../lessons/037-install-skill-generate-script.md) |
| Generation connectors | API/MCP to image, video, voice, music models | Coordinator | [L39 02:39](../lessons/039-skeleton-generating-videos.md); [L93 18:31](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| Review surface | HTML page or web app per run | Humans | [L93 39:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Loom 03:50; 06:40](../../../../resources/ai-song-ad-pipeline-loom.md) |
| Logs | Session log, architecture doc, results patterns | Every new session | [L93 40:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Evolve CW L47 10:59–11:46](../../../evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md) |

### Proposed layout (derived)
```text
.claude/skills/
  ugc-seedance/        SKILL.md   references/{prompt-rules.md, model-facts.md, known-limitations.md, golden-example.md}
  skeleton-ad/         SKILL.md   references/{style-library.md, character-bibles.md, swipe-file.md, known-limitations.md}
  crochet-ad/          SKILL.md   references/{universal-excerpts.md, lighting.md, known-limitations.md, quality-bar.md}
  song-ad/             SKILL.md   references/{genre-map.md, suno-rules.md, known-limitations.md}
  static-batch/        SKILL.md   references/{templates.md, headline-bank-prompt.md, known-limitations.md}
  ad-qa/               SKILL.md   references/{ai-video-qa-checklist.md, claim-audit.md}
  publish-paused/      SKILL.md   (hard rule: status=PAUSED; never activate)
brands/<brand>/
  master-context.md    claims.md (verified | bracketed | banned)    research-doc.md
  product-refs/        character-refs/        voice-refs/ (consented only)
runs/<yyyy-mm-dd>-<brand>-<format>/
  brief.md  script.md (claim-audited)  cost-estimate.md  prompts/  outputs/  review.html  qa-report.md  decisions.md
logs/
  session-log.md   architecture.md   learnings/<brand>.md
```
The repo's own skills already follow the `SKILL.md` + `references/` split ([write-ugc-script references](../../../../../../.claude/skills/write-ugc-script/SKILL.md): checklist, golden examples, hooks, proof and claims, structures). Keep SKILL.md short and put long tables (style libraries, swipe files, model facts) in references, so each format skill stays readable (derived).

## 3. Skill anatomy: what every format skill must contain
| Section | Why | Course precedent |
|---|---|---|
| Frontmatter `name` + `description` with trigger phrases and hand-off triggers | Claude picks the skill and the stage from the description | skeleton-ads description [L37](../lessons/037-install-skill-generate-script.md) |
| Mandatory rules (top, numbered) | Model reads them first; stops format drift | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L45](../lessons/045-claude-skill-setup-explanation.md) |
| Intake: required inputs + one batch of questions | Repo rule 1; skeleton asks "one tight batch" | [L37 Stage 1](../lessons/037-install-skill-generate-script.md); crochet Step 0 [L45](../lessons/045-claude-skill-setup-explanation.md) |
| Stage detection and hand-offs | One chat, many stages; user knows what to paste next | [L37](../lessons/037-install-skill-generate-script.md) |
| Strategy step that forces angle + one awareness stage | "It can't just be a song for the sake of it" | [L50 01:47](../lessons/050-create-song-style-ad-scripts-with-ai.md); skeleton Strategist Playbook |
| Exact output formats | Copy-paste-ready prompts; easy review | [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Universal excerpts (positive, negative, closing line) | Style consistency across every prompt | [L45 section 2](../lessons/045-claude-skill-setup-explanation.md) |
| Consistency system (character bible, hero reference, product reference) | Same character and pack in every shot | [L37 three-layer system](../lessons/037-install-skill-generate-script.md); [L20 @Image mapping](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) |
| Model facts and per-tool notes, dated | Limits change fast | [L20 Seedance facts](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); [L37 per-tool tables](../lessons/037-install-skill-generate-script.md) |
| Known limitations and workarounds | The feedback loop lands here | [L45 section 4](../lessons/045-claude-skill-setup-explanation.md) |
| Quality bar (one worked example) | Shows the target without becoming a template | [L45](../lessons/045-claude-skill-setup-explanation.md); [L37 Appendix A](../lessons/037-install-skill-generate-script.md) |
| "What you don't do" | Negative rules (no text in images, no dialogue in video prompts, no stacked camera moves) | [L37](../lessons/037-install-skill-generate-script.md) |
| Compliance block (repo addition) | None of the course skills has one | Claim audit; no real likeness or voice without rights; AI people never as customers or experts; bracket unverified facts |

### Course skill conflicts and the operator default
| Topic | Position A | Position B | Default |
|---|---|---|---|
| Clarifying questions | Seedance skill: "Do NOT ask clarifying questions" [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | Crochet Step 0 question [L45](../lessons/045-claude-skill-setup-explanation.md); skeleton "one tight batch" [L37](../lessons/037-install-skill-generate-script.md); song prompt asks step by step [L50](../lessons/050-create-song-style-ad-scripts-with-ai.md) | One batch of questions for missing hard inputs (facts, offer, audience, references); then decide creatively without further questions |
| Speech | Seedance generates dialogue with native lip-sync; "NEVER tell users to add voiceover in post" [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | Skeleton: voiceover recorded separately in ElevenLabs, no dialogue in video prompts [L37](../lessons/037-install-skill-generate-script.md); David: write full script, generate the whole voiceover once, slice, then lip-sync per slice because "voice models are not consistent" [L91 49:12–52:51](../lessons/091-special-guest-recordings-ai-office-hours-david.md) | On-camera AI UGC: native audio per segment, then check voice consistency across segments; if it drifts, or the format is voiceover + B-roll or animated lip-sync, use one full voiceover and slice |
| "Cinematic" | Banned in UGC prompts [L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md); "Non-cinematic" in crochet I2V [L45](../lessons/045-claude-skill-setup-explanation.md); excluded from realism prompts [L93 33:41–34:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | Skeleton style named "Bare-Bones Cinematic"; Veo described as cinematic [L37](../lessons/037-install-skill-generate-script.md) | Ban the word in realism/UGC prompts; allow it only as a named animated style |
| Skill host | Claude Desktop skill upload (Customize → Skills) [L20 00:00](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | Claude Code `~/.claude/skills/<name>/SKILL.md` with API/MCP [L39 02:39–03:37](../lessons/039-skeleton-generating-videos.md); Codex CLI reading skills [Loom 00:45](../../../../resources/ai-song-ad-pipeline-loom.md) | Same SKILL.md works in both; use Claude Code when generation, file handling or batches are needed |

## 4. Building and improving a skill (the feedback loop into the skill file)
| # | Step | Output | Source |
|---|---|---|---|
| 1 | Pick the reference: an ad or format you want to reproduce; extract frames (and audio/video for people, with rights) | `references/` frames | [L91 07:44](../lessons/091-special-guest-recordings-ai-office-hours-david.md); [L93 11:46–12:53](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 2 | Split the reference into layers: visual, audio, script; one skill per layer if needed | Layer notes | [L91 41:26–42:27](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| 3 | Do the task once by hand with Claude, iterating heavily | Working outputs | [L93 18:31](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 4 | Test across several scenes and products to surface edge cases | Test grid | [L91 08:46–13:21; 55:33](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| 5 | For each failure, paste a good and a bad output and ask what makes the good one match; rewrite the rule | Named fixes (lighting, skin colour, emotion wording) | [L91 11:53–13:21](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| 6 | Distil the session into SKILL.md (verbatim prompt in [L93 18:31](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md)) | Skill v1 | [L93](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [L91 55:33](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| 7 | Add a "Known limitations & workarounds" section in the crochet style (failure → workaround) | references/known-limitations.md | [L45 section 4](../lessons/045-claude-skill-setup-explanation.md) |
| 8 | Run on a brand-new product before relying on it (derived) | Pass/fail note | [L91 Steps A.8](../lessons/091-special-guest-recordings-ai-office-hours-david.md) |
| 9 | After every production run: append new failures and fixes to known-limitations; append results and learnings to the brand log; read logs at the start of the next session | Updated skill + log | [L93 40:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Evolve CW L47 10:59–11:46](../../../evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md) |
| 10 | Version the skill file (v1, v2) and note which run caused each change (derived) | Changelog line in SKILL.md | — |

Failure entries worth seeding from the course: drop a prop that fails twice ([L20 09:14](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); describe each hand, the surface and what is NOT in frame ("if you don't describe it, Seedance invents it") ([L20 skill](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); no dense particle clouds, use a few yarn-ball orbs ([L45](../lessons/045-claude-skill-setup-explanation.md)); reference the hero image, not the previous image ([L37](../lessons/037-install-skill-generate-script.md)); no text in generated images ([L37](../lessons/037-install-skill-generate-script.md)); one action arc per prompt ([L20](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md)); more light for a clean claymation look ([L91 11:53](../lessons/091-special-guest-recordings-ai-office-hours-david.md)).

## 5. Batch run protocol
| # | Stage | Agent does | Gate | Source |
|---|---|---|---|---|
| 1 | Load | Read master context, claims file, research doc, skill, logs | — | [L93 19:50; 40:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 2 | Script / concept | Format skill writes script or concepts with angle + awareness stage | **G1** script + [claim audit](../../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) | [L50 01:47](../lessons/050-create-song-style-ad-scripts-with-ai.md); [Loom](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 3 | Cast and references | Character sheet / hero image, product references, voice choice | **G2** cast and likeness rights | [L93 27:54–29:24](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Loom 01:00](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 4 | Plan and cost | Shot list or ad list with models and a credit estimate (credit price from master context) | **G3** cost approval | [L93 37:15](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 5 | Smoke test | Generate one image/clip | Agent check | [L93 38:40](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 6 | Keyframes | Storyboard stills; review sub-agent flags anatomy, direction, continuity, text | **G4** keyframes approved | [Loom 05:24–07:34](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 7 | Generate | Batches of 10; parallel sub-agents; retry malformed calls | — | [L93 37:15–38:40](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Loom 02:04; 10:44](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 8 | Self-QA | "Identify anything that sticks out… as an AI giveaway and then regenerate it"; V1/V2 doc; per-shot redo by timestamp | Agent check | [L93 39:41–40:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); [Loom 09:37](../../../../resources/ai-song-ad-pipeline-loom.md) |
| 9 | Edit and package | Edit skill (cuts, captions, music, SFX); review page | **G5** final cut vs [AI video QA checklist](../rubrics/ai-video-qa-checklist.md) | [L83 51:41](../lessons/083-ad-roast-calls-2026-08-17.md); [L93 39:41](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 10 | Copy | 5 primary texts × 5 headlines per ad, from the account's top copy or rewritten to the creative | **G6** human copy and claims pass | [L93 49:31–50:59; 59:19–1:00:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 11 | Upload | Meta Marketing API, status PAUSED | **G7** human launch | [L93 50:59](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |
| 12 | Launch QA and learn | Separate agent checks launched ads against your manual checklist; results logged; skill updated | — | [L93 50:59–52:27](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) |

Strategy gate G0 sits before all of this: offer, angle choice and taste stay human ("still needs you: strategy and offer, your own judgment and taste… compliance and claims, final review") [L93 55:22](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).

### Volume and economics (instructor claims, at recording Aug-Sep 2026)
- About $0.30 per static, "maybe $65" per finished video vs $150-500 per agency creative; his stack $1,000-2,000/month [L93 52:27–53:55](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Start at "probably 80 image 20 video" and adjust; he does not recommend "dumping a thousand AI ads" into an account [L93 52:27; 1:06:09](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Loom: about one hour from script to finished song ad, "between zero and three mistakes per 100 frames" (presenter claims) [Loom 04:17](../../../../resources/ai-song-ad-pipeline-loom.md).
- Default: generate volume for concept diversity, but launch inside the account structure (Evolve [campaign structure 3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md)) and judge by spend share and money ([KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md)), not by the number of ads shipped.

## 6. Security and account safety
- Ad-account token from a Meta developer app in `.env`; "treat it like your bank password"; a leaked key can "launch a million ads in all of your ad accounts" [L93 46:22–48:26](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md). The Loom pipeline uses a secrets manager (Infisical) [Loom](../../../../resources/ai-song-ad-pipeline-loom.md).
- The publish skill hard-codes PAUSED: "the agent can't accidentally go live" (slide) [L93](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Official Meta MCP cannot upload creatives (at recording); the API can [L93 1:02:15–1:03:42](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Meta's own creative enhancements have invented untrue copy for the guest's offer: check every live ad [L93 59:19](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md).
- Keep client names and data out of shared skills [Evolve CW L47](../../../evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md).

## 7. Compliance gate (none of the course skills contains one; add it to every skill)
| Course practice | Problem | Operator rule |
|---|---|---|
| Stranger's Pinterest photo as the AI creator [L20 01:46–02:35](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | Real, identifiable likeness without permission | Generated, licensed or consented faces only; Pinterest for setting and pose references |
| Cloning a person's face and voice from reference video [L93 09:20–15:46](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | The guest cloned himself (consented); the method works on anyone | Voice/face cloning only with written consent of that person |
| AI people voicing product experiences; fake self-branded products [L93 17:03](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | AI "customers" read as testimonials | Never present AI people as real customers or experts; label AI where required |
| "Meta won't flag AI" [L93 56:54–58:18](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | Not a disclosure exemption (the guest says so too) | Follow platform AI-disclosure and non-deception rules |
| One-for-one recreation of viral or competitor ads [L93 14:16; 41:49](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md); same-product scene-by-scene clone [L91 16:16–18:21](../lessons/091-special-guest-recordings-ai-office-hours-david.md) | Copies the asset | Keep foundations (format, structure, hook type); new script, visuals, claims, offer |
| Demo scripts with health claims (GLP-1, gut "parasites", whitening "in 7 days") [L37](../lessons/037-install-skill-generate-script.md); [L50](../lessons/050-create-song-style-ad-scripts-with-ai.md); [Loom](../../../../resources/ai-song-ad-pipeline-loom.md) | Unsupported claims become audio and video that is expensive to fix | Claim audit at G1, before any generation |
| Celebrity look-alike character [Loom](../../../../resources/ai-song-ad-pipeline-loom.md) | Right-of-publicity risk | No real-person look-alikes |

## Cross-course notes
- **RMBC II** ([Claude Project recipe](../../../stefan-georgi/rmbc-ii/concepts/claude-project-recipe.md)): "one Claude Project per asset type", instructions + knowledge base of varied real examples + staged prompts (outline → approve → write → edit). Same principle as one skill per format with references; RMBC adds the staged approve-then-write rhythm, which maps to G1-G4 here. [LLM copy-chief editing](../../../stefan-georgi/rmbc-ii/concepts/llm-copy-chief-editing.md): the human (or reviewing agent) is the copy chief and a second model reviews, which matches the separate QA agent.
- **Evolve Copywriting** ([lesson 47](../../../evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md), [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md)): a Claude Code `/ad-iteration` skill writes learnings into the Growth Guide and a local `patterns` folder; "Claude is not always 100% right" on awareness labels. AI drafts to 70-80%, the human owns the last 20-30%. Agreement; this page's step 9 log is the same patterns folder.
- **Tether Lab** ([AI UGC tools](../../../../tools/ai-ugc-tools.md)): Sarah and Chase are sceptical that AI UGC volume testing produces signal. Conflicts with 093's "testing velocity" pitch. Default: use agent volume to diversify concepts and formats, and keep the creative judged by spend and money like any other ad.
- **Repo:** the KB's own [write-ugc-script](../../../../../../.claude/skills/write-ugc-script/SKILL.md) and [write-landing-page](../../../../../../.claude/skills/write-landing-page/SKILL.md) skills are the house examples of the SKILL.md + references layout and of a checklist gate inside the skill.

## Where it's taught
| Lesson | Covers | Timestamps |
|---|---|---|
| [020 Claude skill + Seedance 2.0](../lessons/020-claude-skill-seedance-2-0-ai-ugc.md) | Install and verify a skill; Seedance UGC Ad Director full text | 00:00–13:33 |
| [037 Install skill & generate script](../lessons/037-install-skill-generate-script.md) | skeleton-ads full text; stage detection | 00:00–02:28 |
| [038](../lessons/038-skeleton-generating-images.md) / [039](../lessons/039-skeleton-generating-videos.md) Skeleton images and videos | Hero-image chaining; Claude Code + Max Fusion API | 00:00–04:27; 02:39–03:37 |
| [045 Claude skill setup](../lessons/045-claude-skill-setup-explanation.md) / [046](../lessons/046-script-visualisation-image-creation.md) | Crochet Ad Visuals full text; verify skill ran | 00:00–01:32; 00:00–01:31 |
| [050 Song-style ad scripts](../lessons/050-create-song-style-ad-scripts-with-ai.md) | Step-by-step prompt with forced angle + stage | 00:00–05:07 |
| [083 Roast 17 Aug](../lessons/083-ad-roast-calls-2026-08-17.md) | AI edit via Claude Code + MCP; edit command as a skill | 50:12–51:41 |
| [090 AI editing](../lessons/090-ai-editing-2026-08-18.md) | Custom skill per style; LLM visuals too simple | 40:39–41:35; 1:06:22–1:08:51 |
| [091 AI office hours (David)](../lessons/091-special-guest-recordings-ai-office-hours-david.md) | Style-skill reinforcement loop; three layers; lip-sync sequence | 05:14–14:49; 41:26–54:06 |
| [093 Mr Paid Social (Caleb Kruse)](../lessons/093-special-guest-recordings-mr-paid-social-guest-talk.md) | Claude Code studio, batch protocol, QA agents, paused upload | 06:53–1:11:42 |
| [AI song-ad pipeline (Loom)](../../../../resources/ai-song-ad-pipeline-loom.md) | Staged pipeline with gates and review sub-agent | 00:00–13:06 |

## Related
[Prompts library](../libraries/prompts.md) · [Tool settings](../libraries/tool-settings.md) · [Produce an AI UGC ad](../playbooks/produce-an-ai-ugc-ad.md) · [Produce an animated AI ad](../playbooks/produce-an-animated-ai-ad.md) · [Make AI static ads](../playbooks/make-ai-static-ads.md) · [UGC creator operations](ugc-creator-operations.md) · [AI realism tells](../concepts/ai-realism-tells.md)
