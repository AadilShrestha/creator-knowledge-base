# Higgsfield research for this demo

Checked **2026-10-20**. Primary sources are Higgsfield's own guides, not competitor claims or third-party prompt recipes. Agent Reach's Exa route returned official guidance; Jina Reader returned HTTP 403 for the attempted pages, so the pages below were opened through the available web tool. No Higgsfield connection or generation was used.

## Findings and decisions

1. [Higgsfield: How to Make AI UGC Videos](https://higgsfield.ai/blog/how-to-make-ai-ugc-videos), Aug 20, 2026: separates product, creator, script, and format; describes reusable product inputs and changing one test variable at a time. Its current Marketing Studio guide lists clips up to **15 seconds**, so a 30-second demo needs an assembly plan or another verified-capable route. We should not assume a single 30-second call.

2. [Higgsfield: Talking AI Avatar in Claude](https://higgsfield.ai/blog/talking-ai-avatar-inside-claude), Aug 12, 2026: describes a character/identity → start-frame → reusable voice → speech → talking-video pipeline. Its example uses a neutral closed mouth in the starting still and a performance prompt tied to script beats. For this demo, make a short pilot before repeating the identity and voice. Identity training is optional for a first concept; use the connected tools' actual capabilities and costs.

3. [Higgsfield: Consistent Characters and Locations](https://higgsfield.ai/blog/consistent-characters-locations), Jul 27, 2026: recommends explicit reference anchors for both identity and location, rather than expecting repeated text descriptions alone to preserve a scene. For Test Cream, save approved character, bathroom, and product references; reuse them across shots and check for drift.

## What “best prompt” means here

There is no universal prompt proven best across Higgsfield's models and workflows. The recommendation is a production-specific separation of **reference assets**, **exact spoken words**, **shot behavior**, and **final editorial text**. Describe observable actions, framing, lighting, and performance. For this demo, generate complex hand actions as separate inserts, and introduce one deliberate action per shot. That last simplification is our production judgment, not an official universal model requirement.

Image/start-frame prompting establishes identity, wardrobe, room, product, and framing. Motion prompting specifies the action and expression changes. Audio direction carries voice and exact dialogue. A high-level orchestrator request packages the plan, while the execution layer maps it to real tool fields. The Markdown labels in the accompanying prompt pack are organizational headings, not invented API parameters.

## Limits to retain when MCP is connected

- Inspect the live tools for supported models, input slots, reference counts, aspect ratios, audio/lip-sync options, and maximum duration. The blog guides are a snapshot, not the tool schema.
- Use model-supported parameters for format and duration; prompt text alone cannot enforce unsupported settings.
- Check the estimated credits before a pilot or batch. This research does not establish an actual cost for this job.
- Reference reuse reduces drift; review still matters. Do not promise exact hands, label typography, timing, voice, or identity from prompt wording alone.
- This is prompting/production research, not cream efficacy research or a customer/competitor study. Product-specific claims and market validation remain outside the fictional demo's evidence.
