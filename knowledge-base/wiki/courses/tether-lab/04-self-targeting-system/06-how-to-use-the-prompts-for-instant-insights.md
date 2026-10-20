---
title: "How to Use the Prompts for Instant Insights"
type: lesson
course: tether-lab
module: 04-self-targeting-system
order: 6
video_length: "8:44"
sources:
  - raw/tether-lab/_transcripts/4. The Self Targeting System/6. How to Use The Prompts For Instant Insights.txt
  - raw/tether-lab/_transcripts/4. The Self Targeting System/6. How to Use The Prompts For Instant Insights.srt
  - raw/tether-lab/_extracted/4. The Self Targeting System/6_6_How_to_Use_the_Prompts_for_Instant_Insights_The_Sel.md
  - raw/tether-lab/_extracted/4. The Self Targeting System/11. 3-Selves Course - Prompts.md
tags: [prompts, chatgpt, tutorial, three-selves-diagnostic, high-camp-flasks, valence, intensity]
updated: 2026-10-20
---

# How to Use the Prompts for Instant Insights
> Screen-recorded walkthrough of the three prompts in the "3-Selves Course – Prompts" doc, with Prompt 1 run live in ChatGPT on 9 High Camp Flasks ads. Shows what the output looks like and how to read the takeaways.

## 🤖 Agent use
- **Use when:** running the self-scoring prompts (or applying them yourself as an LLM agent) on a batch of competitor or own ads, and turning the output into a test plan.
- **Inputs → outputs:** prompt text plus 9 ad images or copy (plus metrics) → per-ad analysis, summary table, takeaways (dominant self, over-indexed patterns by ad type), recommended self ratio and next test directions.
- **Rules:**
  - DO constrain the analysis with numbers: scores, tables, percentages ("give chat fences"). Never ask an open "what do you see?" [04:18].
  - DO delete the `[INSERT…]` placeholder when uploading images instead of copy [03:14].
  - DO break the takeaways down *by ad type*. Identity-callout ads vs product-hero vs comparison ads can lean to different selves [06:57].
  - IF metrics are available **THEN** use Prompt 2 and adopt its suggested ratio (e.g. 50% Actual / 10% Ought / 40% Ideal) for the next batch [01:32].
  - DO pick the *emotion* ([valence](../../../concepts/valence.md) and [intensity](../../../concepts/intensity.md)) after the self is chosen [02:20].
  - DO use this to iterate **core messaging**, not just format [01:45].
- **See also:** [Three selves prompts](../../../resources/three-selves-prompts.md) · [Three selves diagnostic](../../../frameworks/three-selves-diagnostic.md) · [Valence–intensity diagnostic](../../../frameworks/valence-intensity-diagnostic.md)

## TL;DR
- The doc has **3 prompts**: **(1)** self-discrepancy ad analysis, no performance data · **(2) bonus** self-discrepancy + performance analysis · **(3)** rewrite winning ads for all three selves [00:10]. Full text: [Three selves prompts](../../../resources/three-selves-prompts.md).
- **Prompt 2** goes furthest. It finds which self converts best and **recommends a test ratio** (e.g. "50% actual, 10% ought, the rest ideal") plus next test directions [01:02].
- Teams often know how to iterate **format** but not **core messaging**. That gap is what these prompts fill [01:45].
- **Stack it with [valence](../../../concepts/valence.md) and [intensity](../../../concepts/intensity.md)**: first pick *which self*, then *which emotion* [01:59].
- **Give ChatGPT fences.** Ask for scores, numbers and percentages, or it "comes back with random stuff". That's why every prompt is built on numeric scoring [04:18].
- High Camp result: **Actual** is the most consistent (identity callouts like "wine lovers"), **Ideal** dominates when the product itself is the hero, and **Ought** plays a minor supporting role [06:37].

## Key ideas

### The three prompts [00:10]

![Google Doc "3-Selves Course – Prompts" open at PROMPT 1: Self-Discrepancy Ad Analysis (No Performance Data)](../../../assets/tether-lab/04-self-targeting-system/06-prompts-doc-0000.jpg)
*The prompt doc. The tabs list PROMPT 1 (Self-Discrepancy), BONUS PROMPT 2, PROMPT 3 (Rewrite) and OUTPUT STRUCTURE.*

1. **Prompt 1: Self-Discrepancy Ad Analysis (No Performance Data).** "I've got a random group of ads here for you. Go ahead and score them on a zero to 10 scale based upon what type of self you see in that ad", then write "a short summary paragraph so we can figure out which self is coming out the strongest." [00:18]
2. **Bonus Prompt 2: Self-Discrepancy + Performance Analysis.** "This one is so, so powerful… it's going to analyze to see which self is going to convert the best." It still scores each ad, *and* analyses your key metrics [00:37].
   - Pull metrics from wherever you track them ("motion", meaning the Motion creative-analytics tool, or Facebook) and load them in, mapped to the ads [00:57].
   - Output: a summary, then a suggested **next test direction** and a **ratio for future testing**. Sarah's spoken example: "we need to shift more towards **50% actual, 10% ought and the rest of it needs to be ideal**" [01:32]. *(The prompt's own example ratio is 50% Actual / 30% Ideal / 20% Ought.)*
   - Why it matters: "people get a lot of ads in the ad account, two to three of them are holding up the entirety of that ad account. And then they basically have no idea where to go next. **They try and iterate format, but they don't know how to iterate core messaging**" [01:45].
3. **Prompt 3: Rewrite.** Rewrites a winning ad for all three selves, "so that way you can start to get some good tests and good wins… right off the gate just by switching to a different sense of self" [02:35]. See [lesson 7](07-how-to-rewrite-winning-ads-for-new-selves.md).

### Layer the selves with valence and intensity [01:59]
- "Even better, if you can map yourselves… with **valence and intensity**." If you haven't done the [valence & intensity course](../03-valence-intensity-model/README.md), "please, please, please go take that one", because it shows how to dial emotions up or down.
- Analyse valence and intensity, then map them on top of the three selves: "once we know who we need to talk to, which self, then we can identify **which emotion** we need to actually speak to. And then you can start building a crap ton of working ads instead of just like one to two at a time." [02:20]
- See [Valence–intensity diagnostic](../../../frameworks/valence-intensity-diagnostic.md) and [Emotional zones](../../../concepts/emotional-zones.md).

### Live run: Prompt 1 on High Camp Flasks [02:50]
- She uses only Prompt 1 because this is a demo with no metrics. "If I was doing this in real time though, for a brand… I would a hundred percent want metric data" [03:00].
- **Delete the placeholder** "[INSERT NUMBERED AD COPY HERE]", since she's uploading images rather than pasting copy [03:14].
- **Upload the ads.** She has them as screenshots on her desktop. Sample size: **nine** [03:23].
- ChatGPT analyses the copy (headlines, subheads, bullets) **and the image** [03:40].

![ChatGPT 4o with nine High Camp ad screenshots uploaded above the pasted Prompt 1](../../../assets/tether-lab/04-self-targeting-system/06-chatgpt-upload-0719.jpg)
*Prompt 1 pasted into ChatGPT 4o with the nine ad screenshots attached. This is the setup to copy.*

### Pro tip: why the prompts use numbers [03:50]
- "Chat is really good at **NLP**… natural language processing." It takes what it sees and tries to "bucket everything into… its individual categories."
- "You have to give chat some **fences**. Tell it, I want scores, give me numbers… provide me percentages. Otherwise… if you just say, analyze this and tell me what you see, sometimes it'll just come back with random stuff because it's not quite sure what you're looking for." [04:18]
- "This is the reason why all these prompts are built to work off of… **mathematical, statistical analysis**."

### Reading the output [04:40]
- ChatGPT first extracts everything, then asks whether to proceed. Reply "proceed" or "continue" [04:43].
- It goes ad by ad: a **text summary** ("here's what the text actually says"), then what the text is doing linguistically. It analyses "emotion… descriptive words, adjectives, verbs" and assigns a number "based upon how intense that emotion is and what type of self it's actually aligning with" [04:56].
- At the end comes the **summary table**. Example: **Ad 1 = Actual 8 / Ideal 3 / Ought 2**, "strong identity validation for wine lovers", because ad 1 says **"Rosé All Day"**, which emphasises social enjoyment for wine lovers. "I would agree with this analysis." [05:37]
- Another ad: Actual ~4 / Ideal 7 / Ought 2 [06:10].

![High Camp Flasks Facebook ad "Rosé All Day Anywhere – Meet our best-selling all in one wine flask" with four women toasting outdoors](../../../assets/tether-lab/04-self-targeting-system/06-rose-all-day-ad-0715.jpg)
*Ad 1, "Rosé All Day": scored Actual 8 / Ideal 3 / Ought 2 for identity validation of wine lovers.*

### The takeaways ChatGPT gave [06:37]
"Takeaways on here. This is what I really wanted it to do."
- **Actual Self is the most consistently activated** across the ads, "especially for identity based stuff": wine lovers, outdoorsmen, whiskey drinkers. The brand "is relying heavily on… validation and lifestyle."
- **Ideal Self is used most when elevating the product itself.** "Chat has identified something that I didn't notice, which is the reason why I love having chat do this." [06:57] Ads that call out an identity ("Rosé all day") read as Actual. Ads that hero the product ("May cause excessive compliments… Discover the all-in-one, three piece wine flask") or compare products ("I've tried a lot of flasks, here's the old one… here's the new one") read as **Ideal** [07:18].
  - Sarah's read: "That's really interesting. I might not want to be doing that… if I'm trying to make sure I'm not stagnating on that one point."
- **Ought Self plays only "a minor supportive role"**, showing up in "justifications for better quality or cleaner habits" [07:54].
- Overall, the analysis shows "where I am overusing some of my… emotional tactics… what directions you're **over indexing** on, which I see all the time. So please don't feel bad if you're doing it… **This is how human bias works**" [08:23]. See [heuristics](../../../concepts/heuristics.md).

![High Camp ad "Warning: May Cause Excessive Compliments. Discover the All-In-One 3-Piece Wine Flask"](../../../assets/tether-lab/04-self-targeting-system/06-excessive-compliments-ad-0721.jpg)
*Product-hero ad ("May Cause Excessive Compliments"): ChatGPT flagged this kind of ad as Ideal Self.*

![High Camp ad comparing an old hip flask with the Torch Flask, headed by a customer quote](../../../assets/tether-lab/04-self-targeting-system/06-flask-comparison-ad-0729.jpg)
*Product-comparison ad ("I have tried many flasks over the years…" old flask vs Torch Flask). This is also Ideal Self: the upgrade framing.*

- Questions: Sarah invites people to post in the Skool comments and offers to help analyse their ads [06:21].

## Framework / steps
1. Open the prompt doc and copy **Prompt 1** (or **Prompt 2** if you have metrics).
2. In ChatGPT, paste the prompt. Delete the `[INSERT…]` placeholder if you're uploading images.
3. Attach the 9 ad screenshots (or paste copy or video scripts).
4. When ChatGPT confirms extraction, reply **"proceed"**.
5. Review the per-ad breakdowns, the **summary table**, and especially the **takeaways**.
6. Note your over-indexed self and the self that's barely used. Feed your winners into **Prompt 3** ([lesson 7](07-how-to-rewrite-winning-ads-for-new-selves.md)).

## Knowledge units

**Hooks**
| Hook (verbatim or near) | Heuristic(s) | Emotion / zone | Self targeted | Why it works | Source |
|---|---|---|---|---|---|
| "Rosé All Day Anywhere. Meet our best-selling all in one wine flask." (primary text: "Hey wine lovers! We solved wine's portability problem.") | Social proof ("best-selling"), identity callout | Social enjoyment | Actual (8/3/2) | "Strong identity validation for wine lovers" | [05:37] |
| "Warning: May Cause Excessive Compliments. Discover the All-In-One 3-Piece Wine Flask" | Social proof ("900+ 5-Star Reviews & Counting!"), curiosity "warning" | Pride, anticipation | Ideal (product elevated) | Product-hero framing: who you'll be seen as | [07:22] |
| "I have tried many flasks over the years and there is simply no better solution…" (old flask vs Torch Flask) | Comparison/contrast, testimonial, social proof ("Rated 4.94 stars on 275+ reviews") | Upgrade desire | Ideal (product elevated) | Before/after upgrade framing | [07:28] |

**Ad teardowns**
| Brand / product (niche) | Format | Hook / opening | What works | What fails | Fix suggested | Principle | Source |
|---|---|---|---|---|---|---|---|
| High Camp Flasks, 9-ad set (wine/whiskey flasks) | Statics, Meta | Identity callouts ("Rosé All Day"), product-hero ("May Cause Excessive Compliments"), comparisons | Actual is the most consistent self: "wine lovers, outdoorsmen, whiskey drinkers", validation + lifestyle | Ideal dominates whenever the product is the hero. Ought is only a minor supporting role (quality or cleaner-habit justifications) | Diversify. Sarah: "I might not want to be doing that" (leaning Ideal on product ads) | Diagnose over-indexing by ad type, then fill the missing selves | [06:37]–[07:54] |

**Rules of thumb**
- **DO** give the LLM fences: scores, numbers, percentages [04:18].
- **DO** use Prompt 2's recommended self ratio to plan the next test batch [01:32].
- **IF** 2–3 ads carry the account and you only know how to iterate format **THEN** iterate core messaging by self [01:45].
- **DO** layer self → emotion (valence and intensity) to build "a crap ton of working ads instead of just one to two at a time" [02:30].
- **DON'T** feel bad about over-indexing. It's normal human bias. Fix it [08:23].

## Notable quotes
- "They try and iterate format, but they don't know how to iterate core messaging." [01:50]
- "You have to give chat some fences." [04:18]
- "Chat has identified something that I didn't notice, which is the reason why I love having chat do this." [06:57]
- "This is how human bias works." [08:28]

## How to apply
- [ ] Always ask the LLM for numeric scores and a table, never an open "what do you see?".
- [ ] Read the takeaways for *patterns by ad type* (identity-callout ads vs product-hero ads), not just averages.
- [ ] Once you know the self, choose the emotion (valence and intensity) for each new variant.

## Related
- Brand case files: [High Camp Flasks](../../../brands/high-camp-flasks.md) · [all brands by niche](../../../brands/README.md)
- Tool pages: [ChatGPT](../../../tools/chatgpt.md)
- [Three selves prompts](../../../resources/three-selves-prompts.md) · [Three selves diagnostic](../../../frameworks/three-selves-diagnostic.md) · [Prompt library module](../07-prompt-library/README.md)
- [Valence](../../../concepts/valence.md) · [Intensity](../../../concepts/intensity.md) · [Valence–intensity diagnostic](../../../frameworks/valence-intensity-diagnostic.md)
- Previous: [05](05-run-the-3-selves-diagnostic-on-your-ads.md) · Next: [07 – How to Rewrite Winning Ads for New Selves](07-how-to-rewrite-winning-ads-for-new-selves.md)

## Sources
- Transcript: [6. How to Use The Prompts For Instant Insights.txt](<../../../../raw/tether-lab/_transcripts/4. The Self Targeting System/6. How to Use The Prompts For Instant Insights.txt>)
- Page text: [6_6_How_to_Use_the_Prompts…md](<../../../../raw/tether-lab/_extracted/4. The Self Targeting System/6_6_How_to_Use_the_Prompts_for_Instant_Insights_The_Sel.md>)
- Transcript fixes: "actual ideal and all" [00:04] means Actual, Ideal and Ought. "Rose all day" is "Rosé All Day". "motion" is Motion (analytics tool).
- The live run uses a different set of 9 High Camp ads (wine-flask creatives) from the 3×3 grid shown in lessons 2 and 5. The full summary table from the live run isn't in the captured frames. The numbers above are from narration.
