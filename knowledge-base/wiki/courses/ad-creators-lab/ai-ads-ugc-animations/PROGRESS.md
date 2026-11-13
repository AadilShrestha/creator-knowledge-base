# Ad Creators Lab (AI ads, UGC & animations): progress

Updated: 2026-11-13.

## Current checkpoint
- **Source:** MEGA folder `5Y1lhJKB` (a redistributed copy; reseller "DigiHub Courses"). 224 files, 10,659,391,169 bytes: 96 .mp4, 119 Skool pages (.htm/.html), 7 .pdf (5 are reseller flyers), 5 .txt, 2 .zip (byte-identical), 2 .mogrt, 1 .md, 1 .mp3, 1 .crdownload (a complete MP3).
- **Fetched:** 224/224 in full (`_tools/course_fetch.py`), 0 failures. Originals in `knowledge-base/raw/ad-creators-lab/ai-ads-ugc-animations/originals/` (Git-ignored).
- **Transcribed:** 96/96 videos (faster-whisper large-v3-turbo, CUDA, batched); 93 teaching videos ≈ 895 minutes.
- **Extracted:** 112 Skool pages (102 inline images moved to `raw/.../linked/inline-images/`, one folder per page), 2 PDFs (1 teaching brief + rendered pages), 5 .txt, 1 .md, the skill zip; linked resources fetched: 10 Google Docs (+30 images), 1 Google Sheet (CSV), 3 Drive files (the Seedance UGC skill zip, a style-guide PNG, a duplicate of the Poppy .txt). Index: `raw/.../linked/linked-index.json`.
- **Excluded (9):** 4 copies of the reseller flyer "Read First..pdf", the reseller "HTM file guide.pdf", the reseller "Digihub Courses" page, and 3 misfiled videos from an unrelated real-estate course in the Arcads folder ("Building Your Team", "Finding Attorneys To Help You", "Scaling Your Business"; transcript checked). The second crochet skill zip is a byte-identical duplicate, kept mapped to both lessons with one evidence copy.
- **Not available (recorded on the pages, not blockers):** the Arcads workflow video (L32), Canva "AI Ad Prompt Super-Doc" and "AI Inspo Deck" (L9, L10), the SFX pack Drive folder (L14), Fathom call recordings listed on L85, L88, L89, L92 and the deep links on L93, custom GPT instructions (L54, L62, L65, L98), Poppy boards (L55, L76), Gamma research reports (L99), Miro and Notion boards. The 11 Loom links on lesson pages are the same videos as the local MP4s.
- **Lesson map:** `_work/ad-creators-lab/lesson_map.json`, 110 lessons in 9 modules (`_work/ad-creators-lab/build_map.py` with manual fixes for Levels & Unlocks, call-recording dates and the misfiled Arcads videos). Brief: `_work/ad-creators-lab/LESSON-BRIEF.md`; batches: `batches.json` (13 writer runs).
- **Lesson pages:** 110/110 (lesson 20 hand-written as the reference page; the rest by Sonnet writers), about 175k words, 262 screenshots in `wiki/assets/ad-creators-lab/ai-ads-ugc-animations/`.
- **Synthesis (Opus):** 10 concepts, 12 frameworks, 4 playbooks + hub, 2 rubrics + hub, 7 libraries + hub (91 hooks, 28 angles, 85 teardowns, 61 rewrites, 352 rules, 100 prompts/skills, 145 tool settings); `README.md`, `index.md`, `contradictions.md` (48 rows), `MERGE-NOTES.md`, `log.md`.
- **Shared layer:** AGENTS.md (AI-production row + rule 6), AGENT-GUIDE (course, 9 task rows, rule 9), topic-map (new "AI ad production" section + ACL adds on 9 rows), wiki/contradictions.md (AC1–AC9), playbooks/rubrics/libraries/tools hubs, static-ad-creation, ai-ugc-tools, elevenlabs, meta-andromeda, global index section.
- **Validation:** `tools/kb/check_links.py knowledge-base/wiki` → see log; quote check `_tools/verify_quotes.py`: 878 quoted strings with a timestamp, 650 near the cited time, 20 elsewhere in the transcript, 208 not in the transcript (mostly page, doc or on-screen text and table fragments; spot-checked, one paraphrase fixed in L106); manifest 215/215 non-excluded sources mapped to lesson pages with evidence.
- **Speakers:** Camilo (on screen in many tutorials and both roast calls), Hao "Howie" (L86 [06:12]), Narek (L90 [00:05]), Bianca (L104), guests David (L91) and Caleb Kruse "Mr. Paid Social" (L93). Others unverified.

## Related resource added in the same session
- [Automated AI song-ad pipeline (Loom demo, Boris Vaserv)](../../../resources/ai-song-ad-pipeline-loom.md): raw in `knowledge-base/raw/loom/boris-vaserv-song-ad-pipeline/` (MP4 + transcript). Not part of this course.

## Next action
Done. Optional follow-ups: fetch the Fathom recordings (L85, L89, L92) if access is available; add dedicated `wiki/tools/` pages for Max Fusion, Seedance, Kling, Suno, Poppy and Arcads if agents need more than [tool settings](libraries/tool-settings.md); write a shared page on platform AI-disclosure rules (the course does not cover them).
