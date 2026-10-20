---
title: "ChatGPT"
type: tool
course: tether-lab
sources:
  - raw/tether-lab/_transcripts/4. The Self Targeting System/6. How to Use The Prompts For Instant Insights.txt
  - raw/tether-lab/_transcripts/4. The Self Targeting System/7. How to Rewrite Winning Ads For New Selves .txt
  - raw/tether-lab/_transcripts/3. The Valence & Intensity Model/4. Diagnosing Emotional Misfires.txt
  - raw/tether-lab/_transcripts/3. The Valence & Intensity Model/5. Fixing The Tone Without Rebuilding the ad.txt
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
  - raw/tether-lab/_transcripts/5. Recordings/May 2025/5. Live With Sarah!.txt
  - raw/tether-lab/_transcripts/5. Recordings/May 2025/4.Live With Sarah!.txt
  - raw/tether-lab/_transcripts/5. Recordings/May 2025/3. Live With Sarah!.txt
  - raw/tether-lab/_transcripts/5. Recordings/May 2025/1. Guest Session 01 Jonna Wallace!.txt
  - raw/tether-lab/_transcripts/5. Recordings/May 2025/2. Roast my Ads #1.txt
  - raw/tether-lab/_transcripts/5. Recordings/June 2025/5. Live With Sarah!.txt
  - raw/tether-lab/_transcripts/5. Recordings/June 2025/4.Live With Sarah! - June 11, 2025 - Recordings.txt
  - raw/tether-lab/_transcripts/5. Recordings/June 2025/3. Live With Sarah!.txt
  - raw/tether-lab/_transcripts/5. Recordings/July 2025/4. Live With Sarah! - July 02, 2025 - Recordings.txt
  - raw/tether-lab/_transcripts/5. Recordings/July 2025/1. Roast My Ads #3 July 23, 2025 - Recordings.txt
tags: [tool, llm, chatgpt, prompts, custom-gpt, research, nlp, review-mining, copywriting, scripts, ad-analysis]
updated: 2026-10-20
---

# ChatGPT
> Sarah's main working tool. She uses it (GPT-4o, plus a **custom GPT she has trained since 2022/23**) to classify ads by zone and self, mine reviews, draft story scripts, rewrite winners for other selves and zones, and spin out headline variants. Every course prompt is written for it. Her two big warnings: **give it fences** (scores, numbers, a framework), and **don't trust what it invents** (ICPs, social proof, stats).

## 🤖 Agent use
- **Use when:** any LLM step in the ad pipeline: tagging a competitor's ads (emotion, intensity, self, core message), mining reviews, generating concepts/hooks from a lever pair, writing a story-structured UGC script, rewriting a winner into another zone or self, making 10 ways to say a winning line.
- **Inputs → outputs:** ad screenshots / transcripts / reviews + a verbatim course prompt + real brand context → scored tables, concepts, scripts, headline lists. Always followed by human (or agent) verification.
- **Rules:**
  - **DO give the LLM fences.** Ask for scores, numbers, percentages or a named framework. "If you just say, analyze this and tell me what you see, sometimes it'll just come back with random stuff" ([Self-Targeting L6 04:18](../courses/tether-lab/04-self-targeting-system/06-how-to-use-the-prompts-for-instant-insights.md)).
  - **DO paste the framework itself** when you name one. Without it, ChatGPT blends similar frameworks (Monomyth turned into Hero's Journey) ([May 14 0:50:38–0:52:19](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md)).
  - **DO give "giant context"**: a dialled-in persona doc plus the list to choose from. Generic "which heuristic works for X" returns only basics ([July 2 0:19:48–0:20:56; 0:31:29](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md)).
  - **DO attach the actual ad** (screenshot or script) to every diagnostic or rewrite prompt ([Valence + Intensity prompts](../resources/valence-intensity-prompts.md)).
  - **DO ask it to "read between the lines"** when mining reviews. By default it reads word for word and misses context ([June 11 0:27:40–0:29:47](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md)).
  - **DON'T ship invented proof.** In the Self-Targeting L7 demo, ChatGPT wrote "Featured in Outside and Men's Health" for High Camp Flasks; the final ad used the brand's real "As seen in" bar ([L7](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md)). Same for stats, testimonials, stock counts and deadlines ([Prompt Library #9–#11](../courses/tether-lab/07-prompt-library/README.md)).
  - **DON'T use it to invent ICPs from nothing.** "Chat is training you… it's going to take your internal bias" ([May 14 0:29:57](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md)). A candidate list is fine only if you verify each type on Reddit and TikTok ([May 7 0:30:31–0:32:06](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md)).
  - **DON'T assume it can emote.** "Chat is not built to emote… you have to actually tell it how to build you ads and headlines that are emotional" ([May 7 0:52:50](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md)). Specify zone, intensity and self.
- **See also:** [Prompt Library](../courses/tether-lab/07-prompt-library/README.md) · [Valence + Intensity prompts](../resources/valence-intensity-prompts.md) · [3-Selves prompts](../resources/three-selves-prompts.md) · [Story frameworks for ads](../frameworks/story-frameworks-for-ads.md) · [Claude](claude-ai.md) · [Tools hub](README.md)

## How Sarah uses it

| Job | How (as taught) | Where |
|---|---|---|
| **Diagnose an ad's zone** | Custom GPT trained on the valence-intensity model; on-screen prompt "Analyze this ad for valence + intensity. Which zone is this ad in?" (verdicts for 3 AG1 ads: all Zone 1) | [June 11 0:04:30](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · [M3 L4 01:30](../courses/tether-lab/03-valence-intensity-model/04-diagnosing-emotional-misfires.md) |
| **Diagnose which self** | 9 ad screenshots + Prompt 1 (0–10 scores per self) in GPT-4o; Bonus Prompt 2 with performance data | [M4 L5–L6](../courses/tether-lab/04-self-targeting-system/06-how-to-use-the-prompts-for-instant-insights.md) · [3-Selves prompts](../resources/three-selves-prompts.md) |
| **Rewrite a winner** | Zone alteration prompts (M3) or Prompt 3 (rewrite for the other two selves, M4) | [M3 L5](../courses/tether-lab/03-valence-intensity-model/05-fixing-the-tone-without-rebuilding-the-ad.md) · [M4 L7](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md) |
| **Generate concepts** | One of 15 lever-pair prompts, brand line added "at the very, very bottom", iterate ("second round", "Let's do headlines") in a Temporary chat | [Prompt Library tutorial](../courses/tether-lab/07-prompt-library/README.md) |
| **Write story scripts** | "Here's my concept… here's my avatar… use the Pixar story model, write me a script"; paste the framework if it blends | [May 14 0:15:31–0:22:22](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| **Script → static headlines** | "From this story pull out the deepest emotion and the core message… then give us headlines" (asking for Pixar headlines directly confuses it) | [May 14 0:25:11](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| **Mine reviews** | Map reviews to the 9 *Marketing to Mindstates* emotions, take the top 3; ask for "hidden motivators"; ~80 paragraph-length reviews | [June 4 0:36:36](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · [Roast #1 0:46:04–0:48:07](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) |
| **Tag competitor ads** | "Tell me which emotions are in here, how intense they are, which selves they're currently targeting, and… the core message", then go the opposite way | [June 11 0:41:18](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| **Tag own ad performance** | "Which emotion was this, how intense was the emotion, and then which self was this activating", logged next to CPA/CTR/CVR | [June 11 0:37:08–0:39:12](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| **Variants of a winner** | "Give me 10 different ways to say 'the coolest lunch in the room'" (OmieBox) | [Roast #3 0:43:07](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) |
| **Shorten copy** | "What's a simple way to say [this]?" | [Roast #1 0:35:31](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) |
| **Pick a humour type** | "Look at all these reviews, tell me what kind of humor these people would probably find funny" | [Joanna Wallace 0:08:17](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md) |
| **Character/mascot art** | "Make some cartoons of gelato as a character… snarky… kind of pissy… kind of mean" | [June 4 0:33:26](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |

### Sarah's custom GPT
- She has trained her own GPT "since chat was a thing" and won't share it yet: "a little scared, that's my brain in there" ([July 2 0:23:03–0:23:45](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md)).
- She uses a valence-intensity GPT for zone reads ([June 11 0:04:30](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md)). She never tags ads alone: "I've been doing this for like 10 years now and I can't always identify it" ([June 11 0:37:08](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md)).
- Planned: a GPT that matches heuristics from The Decision Lab list to a brand or industry ([July 9 0:50:55](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md)); a "psychological modifiers for chat" training ([May 7 0:52:50](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md)).
- When ChatGPT can't write good headlines or apply a heuristic well, she switches to [Claude](claude-ai.md) ([July 2 0:30:29](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md)).

## Prompt patterns collected from the sessions
Verbatim where shown on screen, otherwise as spoken. Full verbatim course prompts live on the linked resource pages.

| Pattern | Prompt | Source |
|---|---|---|
| Zone diagnostic | "Analyze the following ad for sentiment. Place it within one of the 4 quadrants on the Valence + Intensity Map." | [M3 L4 01:30](../courses/tether-lab/03-valence-intensity-model/04-diagnosing-emotional-misfires.md) |
| Zone diagnostic (GPT) | "Analyze this ad for valence + intensity. Which zone is this ad in?" | [June 11 0:04:30](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| Customer-type list | "Here's our product, here's the industry, think of all the different type of people that could possibly use this… just give me a list." → verify on Reddit/TikTok | [May 7 0:30:31](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) |
| ICP from real data | "Here's what we found from their lifestyle… give us a good ICP for this so that we can start understanding identity and behavior." | [May 7 0:20:58](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) |
| Story script | "Chat, here's my problem, here's my customer, here's the framework I want you to use to tell the story, give me some ideas." | [May 14 0:23:20](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| Forced framework | "…Write me a story using The Monomyth story framework. For context: The Monomyth – [definition]. FRAMEWORK: Departure / Initiation / Return…" | [May 14 0:51:31](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| Length ladder | "Chat, we need to cut this down to 30 seconds." (then 15) | [May 14 0:46:05](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| Emotion mapping | "Here's the nine emotions I want you to look for, go ahead [and map these reviews]" | [June 4 0:36:36](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| Blend two emotions | "I have two emotions that my customers feel: nostalgia, and they also want freedom… Chat, blend me, make me a headline." | [June 4 0:50:27](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| Between the lines | "Chat, what are you seeing here that's between the lines? Show me some stuff that's not obvious." | [June 11 0:28:44](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| Belief → message | "If we have a person who's negatively triggered by gray hairs but they're optimistic that they can slow the process down, what do we need to say…?" | [June 11 0:31:50](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| Actual-self rewrite | "Go after the person they are today and see if we can just align our products with who they are" | [June 18 0:15:40](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) |
| Heuristic selection | "Our customer's a 50 to 75 year old woman. She's experienced a lot of negativity around this type of authority in a medical setting. Which heuristics would you choose for her?" | [July 2 0:19:53](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) |
| Apply one heuristic | "Chat, I want to use the observer expectancy effect in my retention emails… how should I use this?" | [July 2 0:22:58](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) |
| Hidden motivators | "What are the hidden motivators inside all of our reviews?" | [Roast #1 0:46:04](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) |
| Variant generator | "Give me 10 different ways to say 'the coolest lunch in the room'." | [Roast #3 0:43:07](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) |

## Failure modes seen in the course
| What happened | Lesson | Source |
|---|---|---|
| Invented press proof ("Featured in Outside and Men's Health") in a rewrite | Verify every proof claim; swap in real proof | [M4 L7](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md) |
| Blended Monomyth with Hero's Journey ("very ad-like") | Paste the framework; delete "similar to…" lines | [May 14 0:50:38](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) |
| "Sometimes it makes it up" on customer types | Verify on Reddit/TikTok before testing | [May 7 0:31:08](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) |
| Review analysis only finds people who already bought | Add market and behaviour research to find customers "who haven't found us yet" | [June 4 0:23:59–0:25:00](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| A guilt concept ("you've been choosing what's easy, not what's right") that shamed pet owners | Wrap guilt in a story character (mirror effect) and add "No shame…" | [May 21 0:49:15](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) |
| Open "what do you see?" analysis returns "random stuff" | Ask for scores and percentages | [M4 L6 04:18](../courses/tether-lab/04-self-targeting-system/06-how-to-use-the-prompts-for-instant-insights.md) |

## Where it's mentioned
Module 3 lessons 4–5 and bonus prompts; Module 4 lessons 5–7 and prompt doc; Module 7 (all 15 prompts); live sessions [May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md), [May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md), [May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md), [May 23](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md), [May 28](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md), [June 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md), [June 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md), [June 18](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md), [July 2](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md), [July 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md), [July 23](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md).

## Related
[Claude](claude-ai.md) · [The Decision Lab](the-decision-lab.md) · [Sarah Levinger](../people/sarah-levinger.md) · [Customer research stack](../frameworks/customer-research-stack.md) · [Mindstate emotion mapping](../frameworks/mindstate-emotion-mapping.md) · [Valence–intensity diagnostic](../frameworks/valence-intensity-diagnostic.md) · [Three selves diagnostic](../frameworks/three-selves-diagnostic.md)
