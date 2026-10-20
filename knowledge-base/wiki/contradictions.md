---
title: "Contradictions & open questions"
type: overview
course: tether-lab
sources:
  - wiki/courses/tether-lab/05-live-recordings/
tags: [lint, contradictions, defaults]
updated: 2026-10-20
---

# Contradictions & open questions
> Places where Tether Lab sources disagree with each other, with the **default an agent should follow** and the reason. Check here whenever two pages give different advice.

## 🤖 Agent use
- **Use when:** two pages disagree, or before you put any number (batch size, scaling %, stats) into a plan or an ad.
- **Inputs → outputs:** a conflicting instruction → the default to apply, plus what to test if it matters.
- **Rules:**
  - **DO** follow the "Agent default" column unless the user or brand context says otherwise.
  - **DO** treat Sarah's uncited statistics (e.g. "+13.6% likability", "5.43× handwritten fonts", "KFC +56%") as anecdotes. Never put them in ad copy.
  - **DON'T** fabricate proof, scarcity or badge numbers, even where a session seems to tolerate it (row 10).
- **See also:** [rules library](libraries/rules.md), [creative testing system](frameworks/creative-testing-system.md), [TEEP journey](frameworks/teep-journey.md).

S = session page links: [May 7](courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · [May 14](courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · [May 21](courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · [Roast #1](courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · [Jun 4](courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · [Jun 11](courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · [Jun 18](courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) · [Chase](courses/tether-lab/05-live-recordings/2025-06-guest-session-02-chase-mohseni.md) · [Roast #2](courses/tether-lab/05-live-recordings/2025-06-25-roast-my-ads-2.md) · [Jul 2](courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) · [Jul 9](courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · [Jul 16](courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · [Roast #3](courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md)

| # | Topic | Position A | Position B | Agent default | Why |
|---|---|---|---|---|---|
| 1 | **TEEP account structure** | May 21 [0:09:28–0:11:31]: campaign = generation, ad set = emotion, all 4 stages inside each ad set | Jun 4 [0:15:38–0:16:41]: one campaign per stage; mixing stages is "very confusing" | **One campaign per stage** (Jun 4) | Jun 11 [0:48:40] backs it: one learning goal per campaign. See [TEEP](frameworks/teep-journey.md) |
| 2 | TEEP on a small budget | Jun 4 [0:39:49]: keep all 4 stages as ad sets | Jun 11 [0:46:34]: skip trigger ads | **Skip trigger ads; fund Exploration / Evaluation / Purchase** | Trigger ads are the most expensive to make work |
| 3 | TEEP details | May 21: 10–15 ads per ad set; "exploration" = weird, entertaining content | Jun 4: ~9 ads; Jun 11 [0:45:32]: exploration = "why we're better" | **~9 ads per ad set; Exploration = entertaining discovery, Evaluation = comparison** | Matches the majority of mentions. The promised TEEP swipe file is not in the course files |
| 4 | Where to start applying psychology | May 7: identity → emotion → tactics, heuristics last | Jun 18 [0:23:02]: "I start with heuristics" | **Plan identity first; ship heuristic tweaks first** | One is the order of importance, the other the order of effort. See [psychology ladder](frameworks/psychology-application-ladder.md) |
| 5 | One emotion vs blended | Roast #1 [0:41:46]: one core emotion per ad | Jun 4 [0:46:18]: blended emotions do really well | **One emotion per ad; blend only two emotions that each won alone** (headline + subhead) | [blended emotions](concepts/blended-emotions.md), [one core emotion](concepts/one-core-emotion-per-ad.md) |
| 5b | Emotions per brand | May 7: one core emotion per brand | Jun 4: ~3 per industry + 1 outlier | **One core *brand* emotion; test ~3 *ad* emotions** | Brand message ≠ ad-level testing |
| 6 | Iterating the core message | May 7 [0:14:42]: "I don't like to iterate the core message" | Jul 9 / Roast #3: iterate winning headlines | **Keep the core message; iterate headline *wording* and primitives** | |
| 6b | Headline-only tests | Jun 11 [0:51:49]: one headline per image is too slow | May 7 [0:13:46]: one creative × 5 headlines | **Use headline tests only to refine a proven concept** | |
| 7 | Testing volume | Chase [0:57:55]: test 3 at a time; 25 ads/month | Sarah: ~9–10 statics per new concept [Jun 11 0:31:50; Jun 18 1:00:16]; 3–5 new ads/week; ~20/month healthy, 50 ceiling | **3–5 new ads per week, batches of 3 per ad set, ~20/month** | Converges across both. See [testing system](frameworks/creative-testing-system.md) |
| 7b | Scaling speed | Jun 18: 10–15%/day | Jun 18 (same answer): +10% every other day | **+10% every other day, faster only if CPA holds** | The conservative option is safer |
| 8 | Video vs statics | Chase [0:04:49]: brands under $5M shouldn't do video | Sarah: move a winning static concept to video | **Static first; video only once a concept has won as a static** | Both agree on statics first |
| 9 | Ad-library run time as a winner signal | CreativeOS lesson: live 90+ days = winner | Jun 11 [0:22:19]: run time isn't proof | **Run time is a weak signal; combine it with variant count, cross-platform presence and repeat spend** | See [competitor teardown](playbooks/competitor-ad-teardown.md) |
| 10 | **Fabricated proof** | Jul 9 [0:43:49]: fake scarcity backfires | Roast #3 [0:15:00]: a made-up "Only 9 sets left" badge praised; Chase [0:19:10]: a badge "can say anything" | **Never fabricate. True counts, real reviews, real stats only** | Platform policy, legal risk, trust. Non-negotiable |
| 11 | "Add to cart" CTA | Roast #1 [0:28:09]: semi-acceptable | Roast #2 [0:48:38]: replace with "Order yours now" | **Use definitive CTAs ("Order yours now", "Get yours")** | [active CTA language](concepts/active-cta-language.md) |
| 11b | Image "sliver" in carousels | Roast #2 [0:33:45]: sliver of the next card is good | Jul 16 [0:48:22]: Jaxxon's split sliver = cognitive load | **Sliver OK as a scroll cue in carousels; avoid split images in a single static** | |
| 11c | Grid | Roast #1 [0:34:26]: keep everything on a grid | Jun 11 [0:54:59]: "statics are all about breaking the grid" | **Text on the grid; let the image or product break it** | [visual weight](frameworks/visual-weight-hierarchy.md) |
| 12 | Discounts / bundles | Jul 9: fine (tariffs) | Jun 18: luxury never discounts or bundles; Jul 16: overused | **Luxury: never. Mass-market: OK, framed with a reason** | [luxury positioning](concepts/luxury-positioning.md), [offers](frameworks/offer-and-bundle-psychology.md) |
| 13 | "Most customers buy" badge placement | Jul 2: first on the 36-pack | Jul 2 (later): on the true best seller | **Only on the true best seller** | Honesty rule (#10) |
| 13b | Show $ savings | Jul 16: show dollar savings | Member data: subscriptions dropped when savings were shown | **Test it; unresolved** | |
| 14 | Hooks from reviews | Roast #1, Joanna, Jun 11: build hooks from reviews | Jun 4 [0:23:59]: reviews alone re-recruit existing buyers | **Use reviews for language; use market research for new-customer angles** | [research stack](frameworks/customer-research-stack.md) |
| 14b | Post-purchase surveys | May 7: complains about them | Jun 4: NPS 1–10 as the first question | **Use short NPS + "what would make it a 10"** | |
| 15 | ChatGPT for ICPs | May 7: list ICPs with ChatGPT, then verify on Reddit | May 14 [0:29:57]: avoid ChatGPT as an ICP generator | **Generate candidates only; never ship without real-customer verification** | |
| 16 | Story frameworks details | May 14 doc: 15 frameworks (skips #12); StoryBrand / Story Spine steps differ between the doc and ChatGPT | — | **Use the doc's steps; paste them into the prompt** | [story frameworks](frameworks/story-frameworks-for-ads.md) |
| 16b | Script order | May 14: script first, pull headlines from it | Jun 11 [0:32:53]: build the script from a winning static | **If a static has won, start from it; otherwise script first** | |
| 17 | Ought self in cold ads | E-book: Awareness = Ideal/Ought | Jun 18: keep Ought until after qualification | **Ads: Actual/Ideal; Ought in retargeting, email and post-qualification** | [three selves](concepts/three-selves.md) |
| 18 | E-book vs video zone map | V&I e-book: axes swapped, quadrant labels inconsistent | Module 3 videos | **Video map is canonical** | [emotional zones](concepts/emotional-zones.md) |
| 19 | Lesson 5 score slide (Module 4) | Slide: Ideal/Ought scores look swapped | Narration | **Narration is canonical** | [three-selves diagnostic](frameworks/three-selves-diagnostic.md) |

## Terminology slips (Sarah's wording vs the research term)
- "Differentiation effect" / "distinction bias" → **Von Restorff effect** ([page](concepts/heuristics/von-restorff-effect.md)).
- "Halo effect" for borrowing Gordon Ramsay's humor → closer to **association / authority borrowing** ([page](concepts/heuristics/authority-borrowing.md)).
- "Ben Franklin effect" and "observer expectancy effect" are used loosely; see their pages.
- Module 2 materials spell "Effect heuristic"; the slides say **affect heuristic** (correct).

## Open questions (sources don't resolve)
- The TEEP swipe file, qualification cheat sheet, Twitter-tips cheat sheet and "science of belief" book list were promised in sessions but are not in the course files.
- The Prompt Library "15 more prompts" ("More to come shortly!") were never published in this copy.
- All quizzes are external Typeform links; their questions were not captured.
- Chase Mohseni's guest session has no recorded date (late June 2025).
