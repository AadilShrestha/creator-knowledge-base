---
title: "Ad Creators Lab: AI ads, AI UGC and animated ads (course hub)"
type: course
creator: ad-creators-lab
course: ai-ads-ugc-animations
instructor: "Ad Creators Lab / Epic Ads Lab coaches: Camilo (ad roasts, most tutorials where shown), Hao a.k.a. Howie (ad psychology), Narek (AI editing), Justin (copy, page-only); guests David (L91) and Caleb Kruse 'Mr. Paid Social' (L93); others unverified"
sources:
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/manifest.json
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/PROGRESS.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/001-watch-this-if-you-want-to-win.md
  - knowledge-base/wiki/courses/ad-creators-lab/ai-ads-ugc-animations/lessons/004-meet-the-team.md
tags: [ai-ads, ai-ugc, animated-ads, seedance, kling, sora, nano-banana, elevenlabs, claude-skills, statics, ad-roasts, creators]
updated: 2026-11-13
---

# Ad Creators Lab: AI ads, AI UGC and animated ads
> The Skool course of the agency Epic Ads Lab (September 2026 snapshot): 110 lessons in 9 modules, 93 videos (about 895 minutes), with the Claude skills, prompts and Google Docs that come with them. It teaches how to **produce** ads with AI (realistic AI UGC, AI podcasts and street interviews, skeleton / crochet / claymation / song / talking-object animated ads, AI statics), how to review them (ad roasts, ad psychology calls, winning-ad breakdowns) and how to research, brief and hire around that production.

## 🤖 Agent use
- **Use when:** making an ad with AI video, image or voice tools; writing prompts or a Claude skill for ad production; keeping an AI character or voice consistent; editing AI footage so it looks native; making AI statics; reviewing an ad before launch; finding competitor ads by spend.
- **Inputs → outputs:** a finished, claim-audited script or brief + product photos + real customer language → reference pack, prompt pack per shot, generated clips/images, QA log, edit plan, test plan.
- **Rules:**
  - **DO** start at the [format catalog](concepts/ai-ad-format-catalog.md) to pick the format, then follow its framework or [playbook](playbooks/README.md).
  - **DO** run every script through the [RMBC claim audit](../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) **before** generating anything, and every production plan through [AI creator compliance](concepts/ai-creator-compliance.md). Many course examples use invented testimonials, AI "customers", cloned real voices, strangers' faces and unsupported health claims: reuse the method, never those assets or claims.
  - **DO** write the script with the knowledge base's script methods first ([write-ugc-script skill](../../../../../.claude/skills/write-ugc-script/SKILL.md)); this course is strongest on production, not on research or copy depth.
  - **DO** run the [AI video QA checklist](rubrics/ai-video-qa-checklist.md) on every generated ad before it goes live.
  - **DON'T** treat model rankings, credit costs or spend/ROAS figures as facts: they are single tests or instructor claims from Aug–Sep 2026 ([tool settings](libraries/tool-settings.md) lists the conflicts).
  - **IF** two lessons (or this course and another) disagree **THEN** apply the [contradictions](contradictions.md) default and say which row you used.
- **See also:** [course index](index.md) · [playbooks](playbooks/README.md) · [rubrics](rubrics/README.md) · [libraries](libraries/README.md) · [contradictions](contradictions.md) · [AGENT-GUIDE](../../../../AGENT-GUIDE.md) · [topic map](../../../topic-map.md)

## Start here (by agent task)
| Task | Course page | Combine with |
|---|---|---|
| Pick an AI ad format | [AI ad format catalog](concepts/ai-ad-format-catalog.md) | Evolve: [ad definitions](../../evolve/start-here/concepts/ad-definitions.md) |
| Check an AI ad plan for legal / platform risk | [AI creator compliance](concepts/ai-creator-compliance.md) | RMBC: [claim audit](../../stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md) |
| Produce a realistic AI UGC ad | [playbook: produce an AI UGC ad](playbooks/produce-an-ai-ugc-ad.md) · [Seedance workflow](frameworks/ai-ugc-seedance-workflow.md) · [rizz-model pipeline](frameworks/rizz-model-ai-ugc-pipeline.md) | [write-ugc-script skill](../../../../../.claude/skills/write-ugc-script/SKILL.md) · shared [AI UGC tools](../../../tools/ai-ugc-tools.md) |
| Re-make a winning ad with a new creator (compliantly) | [creator swap, compliant](frameworks/creator-swap-compliant.md) | shared [angle remix](../../../playbooks/angle-remix.md) |
| Produce an animated ad (skeleton, crochet, claymation, talking object, explainer style) | [playbook: produce an animated AI ad](playbooks/produce-an-animated-ai-ad.md) · [animated ad pipeline](frameworks/animated-ad-production-pipeline.md) · [character consistency](concepts/character-consistency.md) · [start/end-frame video](concepts/start-end-frame-video.md) | |
| Produce a song ad | [song-ad workflow](frameworks/song-ad-workflow.md) | shared [AI song-ad pipeline (Loom)](../../../resources/ai-song-ad-pipeline-loom.md) |
| Write prompts for video / image models | [reference-first prompting](concepts/reference-first-prompting.md) · [prompts library](libraries/prompts.md) · [tool settings](libraries/tool-settings.md) | |
| Edit AI footage so it looks native | [AI post-production](frameworks/ai-post-production.md) · [AI realism tells](concepts/ai-realism-tells.md) | |
| Make AI static ads | [playbook: make AI static ads](playbooks/make-ai-static-ads.md) · [static ads process](frameworks/static-ads-process.md) · [static rewrite moves](frameworks/static-rewrite-moves.md) · [static copy levers](concepts/static-copy-levers.md) | shared [static ad creation](../../../playbooks/static-ad-creation.md) (its limits stay the default) |
| Research and find competitor ads by spend | [playbook: research to AI ad concepts](playbooks/research-to-ai-ad-concepts.md) · [research document protocol](frameworks/research-document-protocol.md) · [ad spend signal](concepts/ad-spend-signal.md) | Evolve: [research stack workflow](../../evolve/start-here/frameworks/research-stack-workflow.md) |
| Review an ad before launch | [ad roast scorecard](rubrics/ad-roast-scorecard.md) · [winning-ad checklist](frameworks/winning-ad-checklist.md) · [AI video QA checklist](rubrics/ai-video-qa-checklist.md) | shared [ad scorecard](../../../rubrics/ad-scorecard.md) |
| Hooks: open loops, schema, diversification | [hook schema and open loops](concepts/hook-schema-and-open-loops.md) · [diversification vs variation](concepts/diversification-vs-variation.md) · [hooks library](libraries/hooks.md) | Evolve Copywriting hooks; shared [meta andromeda](../../../tools/meta-andromeda.md) |
| Run ad production with Claude skills / Claude Code | [Claude Code ad operator](frameworks/claude-code-ad-operator.md) | shared [AI song-ad pipeline (Loom)](../../../resources/ai-song-ad-pipeline-loom.md) |
| Brief, review and hire UGC creators and editors | [UGC creator operations](frameworks/ugc-creator-operations.md) | shared [creator brief](../../../playbooks/creator-brief.md) |

## Curriculum (110 lessons, 9 modules)
| Module | Lessons | What it gives an agent |
|---|---|---|
| 1. How To Win (onboarding) | [001–007](lessons/001-watch-this-if-you-want-to-win.md) | Community admin; agency claims (instructor claims) |
| 2. The Toolbox | [008–014](lessons/008-how-to-make-diversified-ads.md) | Diversified ads under Andromeda, making AI look less fake, native captions, a full live edit |
| 3. AI UGC | [015–035](lessons/015-change-creators-with-ai.md) | Creator swaps, AI podcasts, Seedance + Claude skill UGC ([L20](lessons/020-claude-skill-seedance-2-0-ai-ugc.md)), street interviews, Poppy, the rizz-model pipeline (Sora hook → stills → ElevenLabs voice → lip-sync → B-roll → edit), Arcads |
| 4. AI Animated Ads | [036–068](lessons/036-skeleton-the-ads-we-re-making.md) | Skeleton (Claude skill, [L37](lessons/037-install-skill-generate-script.md)), crochet (Claude skill, [L45](lessons/045-claude-skill-setup-explanation.md)), singing/song ads, claymation, talking objects, explainer-style ads; hall-of-fame examples |
| 5. Static Ads | [069–076](lessons/069-static-ads-intro.md) | Full static process with a prompt library (L70 doc), AI statics, three static-fix sessions, Poppy method |
| 6. 7-Figure Vault | [077–082](lessons/077-7-figure-vault-watch-first.md) | Five winning-ad breakdowns with scripts, metrics and iterations (wine, intimacy, supplement, hook swap $400 → $13K, men's skincare) |
| 6. Call Recordings | [083–093](lessons/083-ad-roast-calls-2026-08-17.md) | Two ad-roast calls, two ad-psychology calls (Hao), an AI-editing call (Narek), AI office hours (David), a Claude Code + Arcads production talk (Mr. Paid Social); other calls are only Fathom links (not in the files) |
| 7. Research Protocol | [094–102](lessons/094-research-protocol-start-here.md) | Research document, market awareness, why spend beats "longest running", Trendtrack and Adnova |
| 8. Hiring Talent | [103–110](lessons/103-video-editors.md) | Creator brief template, bad UGC review, UGC scripts and concepts, sourcing creators, editors and prices |

## Course pages
- **Concepts (10):** [format catalog](concepts/ai-ad-format-catalog.md) · [AI creator compliance](concepts/ai-creator-compliance.md) · [character consistency](concepts/character-consistency.md) · [start/end-frame video](concepts/start-end-frame-video.md) · [reference-first prompting](concepts/reference-first-prompting.md) · [AI realism tells](concepts/ai-realism-tells.md) · [diversification vs variation](concepts/diversification-vs-variation.md) · [hook schema and open loops](concepts/hook-schema-and-open-loops.md) · [static copy levers](concepts/static-copy-levers.md) · [ad spend signal](concepts/ad-spend-signal.md)
- **Frameworks (12):** [Seedance AI UGC](frameworks/ai-ugc-seedance-workflow.md) · [rizz-model pipeline](frameworks/rizz-model-ai-ugc-pipeline.md) · [creator swap, compliant](frameworks/creator-swap-compliant.md) · [animated ad pipeline](frameworks/animated-ad-production-pipeline.md) · [song ads](frameworks/song-ad-workflow.md) · [AI post-production](frameworks/ai-post-production.md) · [static ads process](frameworks/static-ads-process.md) · [static rewrite moves](frameworks/static-rewrite-moves.md) · [research document protocol](frameworks/research-document-protocol.md) · [winning-ad checklist](frameworks/winning-ad-checklist.md) · [UGC creator operations](frameworks/ugc-creator-operations.md) · [Claude Code ad operator](frameworks/claude-code-ad-operator.md)
- **Playbooks (4):** [hub](playbooks/README.md) · **Rubrics (2):** [hub](rubrics/README.md) · **Libraries (7):** [hub](libraries/README.md): 91 hooks, 28 angles, 85 teardowns, 61 rewrites, 352 rules, 100 prompts and skills, 145 tool settings.

## Claude skills installed in this repo
The three complete course skills are installed as project skills, verbatim, with a repo-rules header that overrides their conflicting parts (stranger photos as creators, "don't ask questions", example health claims):
- [seedance-ugc-director](../../../../../.claude/skills/seedance-ugc-director/SKILL.md): UGC script → Seedance 2.0 prompt pack ([L20](lessons/020-claude-skill-seedance-2-0-ai-ugc.md))
- [skeleton-ad-director](../../../../../.claude/skills/skeleton-ad-director/SKILL.md): skeleton progression ads ([L37](lessons/037-install-skill-generate-script.md))
- [crochet-ad-visuals](../../../../../.claude/skills/crochet-ad-visuals/SKILL.md): crochet diorama storyboards ([L45](lessons/045-claude-skill-setup-explanation.md))

## Don't execute
Course tactics that break repo rules, with the compliant version in [AI creator compliance](concepts/ai-creator-compliance.md):
- Faces of real people found on Pinterest or in other brands' ads as AI "creators" (L15, L16, L20, L26, L40); cloning a real creator's voice (L67).
- AI hosts or "customers" stating results or testimonials as if real (L17, L19, L80, L83); fake comment overlays (L31); invented testimonials, expert quotes and scarcity in static "after" examples (L74, L75); "pretend to be the founder" (L106).
- Unsupported health or results claims in example scripts (L37, L59, L62–L66, L75, L80, L81, L90 and others).
- 1:1 recreation of a competitor's ad (L76); sound effects ripped from YouTube (L58).

## Provenance and limits
- Source: a redistributed copy of the course (MEGA folder, 224 files, 10.66 GB). Nine files are excluded: reseller flyers and guide (DigiHub) and three misfiled videos from an unrelated real-estate course found in the Arcads folder. See [PROGRESS](PROGRESS.md) and [manifest](manifest.json).
- Not in the files: the Arcads workflow video (L32), the Canva "prompt super-doc" and inspo deck (L9, L10), the SFX pack, most Fathom call recordings (L85, L88, L89, L92), several custom GPT instructions and Poppy boards. Linked Google Docs and the public Drive skill were fetched.
- Machine transcription (Whisper large-v3-turbo). Tool names are often misheard; lesson pages note the fixes.
- Affiliate links in the course (Max Fusion, Trendtrack, Adnova, Poppy) are marked on the lesson pages.
