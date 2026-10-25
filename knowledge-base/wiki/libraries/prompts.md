---
title: "Prompt index: every prompt in the Tether Lab wiki"
type: library
creator: sarah-levinger
course: tether-lab
sources:
  - wiki/courses/tether-lab/07-prompt-library/  # 15 lever-pair prompts (verbatim on each page)
  - wiki/resources/valence-intensity-prompts.md
  - wiki/resources/three-selves-prompts.md
  - wiki/frameworks/story-frameworks-for-ads.md
  - wiki/frameworks/customer-research-stack.md
  - wiki/frameworks/mindstate-emotion-mapping.md
  - wiki/tools/chatgpt.md
  - wiki/courses/tether-lab/05-live-recordings/  # spoken prompts in session "Prompts" sections
tags: [library, prompts, chatgpt, llm, index, research, diagnose, ideate, write, rewrite, test]
updated: 2026-10-20
---

# Prompt index
> The master index of every prompt in the wiki (Sarah's course prompts, prompts spoken or shown in live sessions, and the few agent templates the wiki assembled from them), tagged by pipeline job, with the inputs each needs, what it returns and a link to where the verbatim text lives.

## 🤖 Agent use
- **Use when:** any LLM step in the ad pipeline: mining reviews, tagging a competitor's ads, diagnosing a draft's zone or self, generating concepts and hooks, writing a story-structured UGC script, rewriting a winner, making variants.
- **Inputs → outputs:** the job you're on → the [which-prompt table](#which-prompt-for-which-job-if--then) → the prompt's row → open the linked page and paste the **verbatim** text, plus the inputs listed in the row → output to verify and hand to the next step.
- **Rules:**
  - DO paste course prompts verbatim from the linked page. Don't paraphrase them: variants break comparability between tests ([Prompt Library](../courses/tether-lab/07-prompt-library/README.md)).
  - DO add the brand / product / landing-page block "at the very, very bottom" of Prompt Library prompts, and attach the actual ad (screenshot or script) to every diagnostic or rewrite prompt ([rules AI4](rules.md#ai--chatgpt-use)).
  - DO give fences: scores, percentages, a named framework with its steps pasted in ([rules AI1–AI3](rules.md#ai--chatgpt-use)).
  - DON'T ship any stat, testimonial, review, press mention, stock count or deadline an LLM produced until it is checked against real data ([rules X1, AI12](rules.md#ethics--compliance)).
  - DON'T use a prompt marked *derived* as if Sarah wrote it; it's a wiki assembly of her spoken prompts.
- **See also:** [ChatGPT tool page](../tools/chatgpt.md) (failure modes) · [Rules](rules.md) · [Ad teardowns](ad-teardowns.md) · [Hooks](hooks.md) · [Angles](angles.md) · [Rewrites](rewrites.md)

**Job key:** **research** = learn about customers or competitors · **diagnose** = score or classify an existing ad · **ideate** = generate concepts, angles or hooks · **write** = produce a script, headline or asset brief · **rewrite** = transform an existing ad or line · **test** = plan or read tests. **Provenance:** *verbatim* = exact text on the linked page · *as spoken* = transcribed from a session, near-verbatim · *derived* = assembled by the wiki from Sarah's prompts.

## 1. The Prompt Library (15 lever-pair prompts)
Each of #1–#14 returns **3 ad concepts** (Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats). #15 returns 3–5 hooks. Inputs for all: the verbatim prompt + a brand block (`Brand / Product / Website or landing page`) appended at the bottom, optionally audience, self, zone, format, approved claims and the competitor mechanism you are remixing. Full run procedure: [Standard run](../courses/tether-lab/07-prompt-library/README.md#standard-run-for-agents).

| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 1 | First Principles Thinking + Loss Aversion | ideate | Brand block; the entrenched routine you're attacking | 3 concepts: deconstruct the routine + cost of waiting | [#1](../courses/tether-lab/07-prompt-library/01-first-principles-thinking-and-loss-aversion.md#the-prompt-verbatim) |
| 2 | Status Signaling + Open Loop | ideate | Brand block; premium / insider product | 3 concepts: status + curiosity click | [#2](../courses/tether-lab/07-prompt-library/02-status-signaling-and-open-loop.md#the-prompt-verbatim) |
| 3 | Curiosity + Reverse Psychology (demoed in the tutorial) | ideate | Brand block; the bad habit to "encourage" | 3 sarcastic, qualifying TOFU concepts | [#3](../courses/tether-lab/07-prompt-library/03-curiosity-and-reverse-psychology.md#the-prompt-verbatim) |
| 4 | Shock Factor + Transformation Shortcut | ideate | Brand block. Use the Skool text: the PDF's psychology section is wrong | 3 scroll-stop + easy-fix concepts | [#4](../courses/tether-lab/07-prompt-library/04-shock-factor-and-transformation-shortcut.md#the-prompt-verbatim) |
| 5 | Tribal Belonging + Vulnerability | ideate | Brand block; the hidden/embarrassing struggle | 3 confessional / community concepts | [#5](../courses/tether-lab/07-prompt-library/05-tribal-belonging-and-vulnerability.md#the-prompt-verbatim) |
| 6 | Pattern Disruption + Hidden Truth | ideate | Brand block; the category's same-y pattern (from a teardown) | 3 pattern-break + insider-truth concepts | [#6](../courses/tether-lab/07-prompt-library/06-pattern-disruption-and-hidden-truth.md#the-prompt-verbatim) |
| 7 | What If Scenario + Pain Point Amplification | ideate | Brand block; high-commitment purchase | 3 dream-state vs cost-of-inaction concepts | [#7](../courses/tether-lab/07-prompt-library/07-what-if-scenario-and-pain-point-amplification.md#the-prompt-verbatim) |
| 8 | Contrast + Aspirational Identity | ideate | Brand block; a real before/after | 3 transformation concepts (Ideal-heavy: rotate selves after) | [#8](../courses/tether-lab/07-prompt-library/08-contrast-and-aspirational-identity.md#the-prompt-verbatim) |
| 9 | Gamification + Time-Sensitive Offer | ideate | Brand block + a **real** promo window, drop or challenge | 3 game + real-clock concepts | [#9](../courses/tether-lab/07-prompt-library/09-gamification-and-time-sensitive-offer.md#the-prompt-verbatim) |
| 10 | Anonymity + Social Proof | ideate | Brand block + **real** reviews / survey answers | 3 anonymous-voices + volume concepts | [#10](../courses/tether-lab/07-prompt-library/10-anonymity-and-social-proof.md#the-prompt-verbatim) |
| 11 | Authority Borrowing + Data-Driven Insight | ideate | Brand block + **real** stats, studies, press, certifications | 3 proof-led concepts for skeptical buyers | [#11](../courses/tether-lab/07-prompt-library/11-authority-borrowing-and-data-driven-insight.md#the-prompt-verbatim) |
| 12 | Micro-Story + Suspense | ideate | Brand block; a story moment | 3 narrative UGC concepts with a withheld payoff | [#12](../courses/tether-lab/07-prompt-library/12-micro-story-and-suspense.md#the-prompt-verbatim) |
| 13 | Counterintuitive Insight + Specificity | ideate | Brand block + **real** exact numbers / the myth | 3 myth-busting concepts with specifics | [#13](../courses/tether-lab/07-prompt-library/13-counterintuitive-insight-and-specificity.md#the-prompt-verbatim) |
| 14 | Reframing Perception + Emotional Trigger | ideate | Brand block + the target emotion (sets the zone) | 3 reframe + one-emotion concepts | [#14](../courses/tether-lab/07-prompt-library/14-reframing-perception-and-emotional-trigger.md#the-prompt-verbatim) |
| 15 | The "Why Didn't I See This?" Framework (Hindsight Bias + Bounded Rationality; Skool only) | ideate (hooks) | Brand block; the competitor / old way buyers use | 3–5 switching hooks that don't blame the buyer | [#15](../courses/tether-lab/07-prompt-library/15-hindsight-bias-and-bounded-rationality.md#the-prompt-verbatim) |
| 16 | Prompt Library follow-ups (*verbatim*, same chat): "second round" · "Let's do headlines" | ideate / write | The chat that ran #1–#15 | A new batch of concepts, or headlines for them | [Tutorial 04:04](../courses/tether-lab/07-prompt-library/README.md#video-tutorial-how-to-use-the-prompt-library) |
| 17 | Prompt Library follow-ups (*derived*, not from the course): concept → 30-s UGC script; rewrite for a self; shift to a zone | write / rewrite | A chosen concept number | Script with timestamps, on-screen text, B-roll; or a self/zone variant | [Standard run step 5](../courses/tether-lab/07-prompt-library/README.md#standard-run-for-agents) |

## 2. Valence + intensity prompts (diagnose and move the emotion)
| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 18 | Zone diagnostic (*verbatim*): "Analyze the following ad for sentiment. Place it within one of the 4 quadrants on the Valence + Intensity Map." | diagnose | Ad screenshot (optionally the zone-map image) | Quadrant + reasons on valence and intensity | [V&I prompts](../resources/valence-intensity-prompts.md#diagnostic-prompt-from-lesson-4) · [M3 L4 01:30](../courses/tether-lab/03-valence-intensity-model/04-diagnosing-emotional-misfires.md) |
| 19 | Zone diagnostic, custom-GPT form (*verbatim*): "Analyze this ad for valence + intensity. Which zone is this ad in?" | diagnose | Ad screenshot(s); used on 3 AG1 ads | Zone verdict per ad | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jun 11 0:04:30](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| 20 | Alteration → Zone 2, high valence / high intensity ("breakthrough moment… your product is the catalyst") | rewrite | The underperforming ad (screenshot or copy) | Rewritten copy + a celebration/transformation image direction | [V&I prompts](../resources/valence-intensity-prompts.md#high-valence-high-intensity--zone-2-hype) |
| 21 | Alteration → Zone 1, high valence / low intensity ("a sigh of relief they didn't know they needed") | rewrite | The ad | Calm copy + "emotional exhale" image direction | [V&I prompts](../resources/valence-intensity-prompts.md#high-valence-low-intensity--zone-1-feel-good) |
| 22 | Alteration → Zone 4, low valence / high intensity ("about to make a big mistake") | rewrite | The ad; a category where urgency is legitimate. Use with care | Warning copy + "visually wrong" scroll-stop image direction | [V&I prompts](../resources/valence-intensity-prompts.md#low-valence-high-intensity--zone-4-danger-zone) |
| 23 | Alteration → Zone 3, low valence / low intensity ("quietly calling out a truth they've been avoiding") | rewrite | The ad | Longing/ache copy + "gentle ache" image direction | [V&I prompts](../resources/valence-intensity-prompts.md#low-valence-low-intensity--zone-3-pain-point-whisper) |
| 24 | E-book zone starters, Z1–Z4 one-liners (e.g. Z1 "Rewrite as a gentle promise. Something soothing. A sigh of relief.") | rewrite | The ad | Quick zone rewrite | [V&I prompts](../resources/valence-intensity-prompts.md#e-book-prompt-starters-verbatim-shorter-versions) |

## 3. Three-selves prompts (who the ad tells the viewer they are)
| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 25 | Prompt 1: Self-Discrepancy Ad Analysis (No Performance Data) | diagnose | ~9 ads (3 top / 3 mid / 3 flop) as numbered copy, screenshots or video transcripts | 0–10 Actual / Ideal / Ought score per ad + justification, summary table, dominant self | [3-selves prompts](../resources/three-selves-prompts.md#prompt-1-self-discrepancy-ad-analysis-no-performance-data) |
| 26 | Prompt 1, on-screen variant (lesson 5) | diagnose | Same as #25 | Same + "suggestions for balance or re-alignment" | [3-selves prompts](../resources/three-selves-prompts.md#on-screen-variant-of-prompt-1-lesson-5) |
| 27 | Bonus Prompt 2: Self-Discrepancy + Performance Analysis | diagnose / test | Ads + CTR / CVR / ROAS per ad (spreadsheet) | Which self performs, next test direction and a self ratio for the next batch | [3-selves prompts](../resources/three-selves-prompts.md#bonus-prompt-2-self-discrepancy--performance-analysis) |
| 28 | Prompt 3: Rewrite One Ad for All Three Selves | rewrite | One winning ad; offer, CTA and LP held constant. Change the output line to "an ad script" for UGC [M4 L7 02:18] | Full static concepts (headline, subhead, proof, bullets) or scripts, one per self | [3-selves prompts](../resources/three-selves-prompts.md#prompt-3-rewrite-one-ad-for-all-three-selves) · [M4 L7](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md) |
| 29 | E-book one-liners: "Write an ad that validates who the customer already is…" (Actual) · "…who the customer wants to become…" (Ideal) · "…what they should be doing…" (Ought) | write | Product + target self | One quick ad draft for that self | [3-selves prompts](../resources/three-selves-prompts.md#e-book-one-line-prompts-chapter-5) |
| 30 | Actual-self rewrite direction (*as spoken*): "Go after the person they are today and see if we can just align our products with who they are." | rewrite | An Ideal-heavy winner | Present-moment, situational Actual-self copy | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jun 18 0:15:40](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) |

## 4. Story-framework prompts (UGC, influencer, podcast and VSL scripts)
| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 31 | Minimal framework call (*as spoken*): "Please use the Pixar story framework to build this script for me." | write | A concept already in the chat | Script in that framework | [Story recipe #1](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 32 | Core recipe: concept + avatar + framework (*as spoken*: "here's my concept… here's my avatar… use the Pixar story model, write me a script") | write | One concept (from research), an avatar from real data, a named framework | Story-structured UGC script | [Story recipe #2](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 33 | Low-budget idea generator (*as spoken*): "Chat, here's my problem, here's my customer, here's the framework I want you to use to tell the story, give me some ideas." | ideate | Problem, customer, framework | Story ideas | [Story recipe #3](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 34 | Recipe + main character + CTA (*verbatim, on screen*): "We sell dental chews treats and toys for dogs. Write a story using Freytag's Pyramid. Our main character is the vet our dogs go to, and the final CTA - shop now." | write | Product line, framework, main character, CTA | Third-party-narrator script | [Story recipe #5](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 35 | Steering modifiers (*as spoken*): "I want five characters" · "we want it to be really intense" · or no context at all | write | An existing script prompt | Adjusted cast or intensity | [Story recipe #6](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 36 | "Paste the steps" fix (*verbatim, on screen*): "…Write me a story using The Monomyth story framework. For context: The Monomyth – [definition]. FRAMEWORK: Departure / Initiation / Return…" | write | Framework steps pasted from the step tables, "similar to…" line deleted | A script that follows one framework (fixes blending and blandness) | [Paste-the-steps fix](../frameworks/story-frameworks-for-ads.md#the-paste-the-steps-fix) |
| 37 | Anti-pattern (*verbatim*, keep for reference): "We sell healthy, low sugar ice cream, diabetic friendly. Write me a story using The Monomyth. CTA at the end: shop now." | — (don't use) | — | Blended Monomyth/Hero's Journey output: the failure demo | [Story recipe #7](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 38 | Script → static headlines (*as spoken*): "Chat, from this story pull out the deepest emotion and the core message… and then give us headlines for that." | rewrite | A finished story script | Core emotion, core message, static headlines | [Story recipe #4](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 39 | Length ladder (*as spoken*): "Chat, we need to cut this down to 30 seconds." (then 15) | rewrite / test | A 2–3-min script | 30-s, then 15-s cut | [Story recipe #9](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |
| 40 | Agent story-script template (*derived* from #32, #34, #36) | write | Product, concept, avatar, format, framework + pasted steps, main character, CTA | A realistic script with ~2/3 setup and scene directions, no invented proof | [Agent template](../frameworks/story-frameworks-for-ads.md#the-prompt-recipe-verbatim) |

## 5. Research and review-mining prompts
| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 41 | Hidden motivators (*as spoken*): "What are the hidden motivators inside all of our reviews?" | research | ~80 paragraph-length reviews (+ surveys, comments) | Motivators to turn into angles | [Research prompts](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken) · [Roast #1 0:46:04](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) |
| 42 | Read between the lines (*as spoken*): "Chat, what are you seeing here that's between the lines? Show me some stuff that's not obvious." | research | Reviews, survey or quiz data | Context behind the literal words | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jun 11 0:28:44](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| 43 | Map reviews to the nine mindstate emotions (*as spoken*: "Here's the nine emotions I want you to look for…"; *derived* full prompt on the mindstate page) | research | Reviews + the nine-emotion list | Top 3 emotions with share and quotes, plus an outlier | [Mindstate prompts](../frameworks/mindstate-emotion-mapping.md#prompts) · [Jun 4 0:36:36](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| 44 | Humour-type finder (*as spoken*): "Look at all these reviews, tell me what kind of humor these people would probably find funny." | research | Reviews | One humour type to test first | [Research prompts](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken) · [Joanna 0:08:17](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md) |
| 45 | Customer-type list (*as spoken*): "Here's our product, here's the industry, think of all the different type of people that could possibly use this… just give me a list." | research | Product + industry | Candidate customer types: **verify each on Reddit/TikTok before use** ([contradictions #15](../contradictions.md)) | [Research prompts](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken) · [May 7 0:30:31](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) |
| 46 | ICP from real survey data (*as spoken*): "Here's what we found from their lifestyle… give us a good ICP for this so that we can start understanding identity and behavior." | research | Real survey answers (hobbies, family, friends) | An identity/behaviour ICP | [Research prompts](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken) · [May 7 0:20:58](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) |
| 47 | Combined review-mining prompt (*derived* from #41–#43) | research | N reviews | Motivators with quotes, emotion map, outliers, exact customer phrases | [Research stack](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken) |
| 48 | Competitor-library tagging (*as spoken*): "Tell me which emotions are in here, how intense they are, which selves they're currently targeting, and… what the core message is." | research / diagnose | A competitor's ad library (screenshots) | Emotion, intensity, self and core message per ad, so you can go the opposite way | [ChatGPT: How Sarah uses it](../tools/chatgpt.md#how-sarah-uses-it) · [Jun 11 0:41:18](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |
| 49 | Belief → message (*as spoken*): "If we have a person who's negatively triggered by gray hairs but they're optimistic that they can slow the process down, what do we need to say to get them to understand that this product is what will get them that result?" | ideate | The trigger + the belief under the behaviour | Messages that bridge belief to product | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jun 11 0:31:50](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |

## 6. Heuristic, emotion and copy-craft prompts from the sessions
| # | Prompt name | Job | Inputs needed | Output | Link to verbatim text |
|---|---|---|---|---|---|
| 50 | Heuristic selection with context (*as spoken*): "Our customer's a 50 to 75 year old woman. She's experienced a lot of negativity around this type of authority in a medical setting. Which heuristics would you choose for her?" | ideate | Audience + their history with authority | Context-fit heuristics (not just "authority works") | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jul 2 0:19:53](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) |
| 51 | Persona-doc heuristic picker (*as spoken*): "Here's the background information on who we're trying to go after, here's this list of heuristics that I want you to choose from, pick one based on context." | ideate | Persona doc + a heuristic list (e.g. The Decision Lab) | One justified heuristic | [Jul 2 0:31:35](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) |
| 52 | Apply one heuristic (*as spoken*): "Chat, I want to use the observer expectancy effect in my retention emails… how should I use this?" | ideate | Heuristic + channel | Application ideas | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Jul 2 0:22:58](../courses/tether-lab/05-live-recordings/2025-07-02-live-with-sarah.md) |
| 53 | Blend two emotions (*as spoken*): "I have two emotions that my customers feel: nostalgia, and they also want freedom… Chat, blend me, make me a headline." | write | Current emotion + desired emotion, **both already proven** ([contradictions #5](../contradictions.md)) | Blended headline (headline + subhead) | [Mindstate prompts](../frameworks/mindstate-emotion-mapping.md#prompts) · [Jun 4 0:50:27](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| 54 | Variant generator (*as spoken*): "Give me 10 different ways to say 'the coolest lunch in the room'." | rewrite / test | A winning headline | 10 phrasings to test by desire type | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Roast #3 0:43:07](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) |
| 55 | Shorten (*as spoken*): "What's a simple way to say [this]?" | rewrite | One line | A shorter line (4–7 words) | [ChatGPT patterns](../tools/chatgpt.md#prompt-patterns-collected-from-the-sessions) · [Roast #1 0:35:31](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) |
| 56 | Product-as-character art (*as spoken*): "Make some cartoons of gelato as a character… snarky… kind of pissy… kind of mean." | write (visual) | Product + the humour attitude that worked | Mascot / character images | [ChatGPT: How Sarah uses it](../tools/chatgpt.md#how-sarah-uses-it) · [Jun 4 0:33:26](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) |
| 57 | Own-ad performance tagging (*as spoken*): "Three things I want you to look for: which emotion was this, how intense was the emotion, and then which self was this activating." | test | Your ads + CPA / CTR / CVR | Emotion, intensity and self per ad, for the tracking sheet | [ChatGPT: How Sarah uses it](../tools/chatgpt.md#how-sarah-uses-it) · [Jun 11 0:37:08](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) |

## Which prompt for which job (IF → THEN)
| IF you need to… | THEN run | Then hand off to |
|---|---|---|
| Understand why customers buy (have reviews) | #41 hidden motivators + #42 read between the lines, or the combined #47 | #43 emotion map → angles |
| Find the ~3 emotions of a category and an outlier | #43 (paste the nine emotions) | #53 to blend proven ones; Prompt Library #14 for one emotion |
| Find new customer types (no data) | #45, **then verify on Reddit/TikTok** | #46 once you have real survey answers |
| Choose the humour type before writing funny UGC | #44 | #56 if the product becomes the character |
| Tear down a competitor's library | #48 (emotions, intensity, selves, core message) + #19 for the zone of each ad + #25 for the selves | [Ad teardowns](ad-teardowns.md) for precedents; go the opposite way |
| Diagnose why our own ad isn't converting | #18 (zone) and #25 (selves) on the ad | #20–#23 or #28 to move it |
| Our account is stuck in one zone | #19 / #18 on the library, then the alteration prompt for an empty zone (#20–#23) | Test across zones ([rules E10](rules.md#emotion--zones)) |
| Our account over-indexes on one self | #25 (no data) or #27 (with metrics, gives a test ratio) | #28 to rewrite the winner for the other selves |
| Generate new concepts from a competitor's lever pair | The Prompt Library prompt that pairs those levers (#1–#14; see its [decision table](../courses/tether-lab/07-prompt-library/README.md#decision-table-which-prompt-for-which-situation)) | #16 "Let's do headlines", then #40 to script |
| Generate switching / competitor-conquest hooks | Prompt Library #15 | #36 / #40 for the script |
| Pick heuristics that fit this audience | #50 or #51 (with a persona doc and a list) | #52 to apply one; [rules HE](rules.md#heuristics-use) |
| Write a UGC / influencer / fake-podcast script | #32 or the agent template #40; if it blends or goes bland, #36 | #38 for static headlines; #39 for length tests |
| Turn a winning story into statics | #38 | #54 for variants |
| Make variants of a winning headline | #54, then #55 to shorten each | Test one variable at a time ([rules T1–T2](rules.md#testing-iteration--scaling)) |
| Rewrite a winner into another emotional zone | #20 (Z2), #21 (Z1), #22 (Z4), #23 (Z3) with the original ad attached; #24 for a quick pass | #18 to confirm it landed in the target zone |
| Rewrite a winner for another self | #28 (or #30 for Actual) | Self-type test ([rules S11](rules.md#selves--identity)) |
| Read test results by identity | #27 (with metrics) or #57 | Next batch ratio |

## Coverage & gaps
- **Indexed:** 57 entries: the 15 Prompt Library prompts + 2 follow-up rows, 7 valence–intensity prompts, 6 three-selves prompts, 10 story-framework prompts (incl. one anti-pattern and one derived template), 9 research prompts, 8 heuristic/emotion/copy-craft prompts. Verbatim text stays on the linked pages; only one-liners are inlined.
- **Searched:** every fenced code block in the wiki (only the pages above hold prompts; the other blocks are output templates, YAML and diagrams) and every session page's "Prompts…" section and spoken "Chat, …" lines.
- **Known gaps (named in sessions, text not in the course files):** Darian's first-principles-thinking prompt (Jul 2 0:40:13, text not shown); the "proof graphic" prompt being added to the Prompt Library (Jun 18 0:42:22); the "15 more" Prompt Library prompts and lesson "16. More to come shortly!" (empty); the "7 Free psychology ad prompts" from the onboarding call; the planned "psychological modifiers for chat" training; Sarah's custom GPTs (not shared). The PDF version of Prompt Library #4 has a wrong psychology section; use the Skool text.
- **Provenance:** *as spoken* prompts are transcriptions and may differ slightly from what Sarah typed. *Derived* entries (#17, #40, #47, the full #43) are wiki assemblies; label them as such in briefs.
