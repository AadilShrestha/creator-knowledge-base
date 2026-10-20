---
title: "Valence + Intensity Prompts"
type: prompt
course: tether-lab
module: 03-valence-intensity-model
sources:
  - raw/tether-lab/3. The Valence & Intensity Model/9. Valence + Intensity - Prompts.pdf
  - raw/tether-lab/_extracted/3. The Valence & Intensity Model/9. Valence + Intensity - Prompts.md
  - raw/tether-lab/_extracted/3. The Valence & Intensity Model/8. Diagnose Why Your Ads Aren't Working.md
  - raw/tether-lab/_transcripts/3. The Valence & Intensity Model/4. Diagnosing Emotional Misfires.txt
  - raw/tether-lab/_transcripts/3. The Valence & Intensity Model/5. Fixing The Tone Without Rebuilding the ad.txt
tags: [prompts, chatgpt, tone-shifting, emotional-zones, copywriting, image-direction]
updated: 2026-10-20
---

# Valence + Intensity Prompts
> Every prompt from [Tether Lab Module 3](../courses/tether-lab/03-valence-intensity-model/README.md), **verbatim**: one diagnostic prompt that places an ad on the map, and four "alteration prompts" that rewrite an ad (copy + image direction) into each emotional zone. The e-book's shorter "prompt starters" are included too.

## 🤖 Agent use
- **Use when:** classifying an ad's zone with an LLM, or generating zone-specific copy and image direction for remixes, variants and briefs.
- **Inputs → outputs:** ad screenshot/script (+ target zone) → zone classification, or rewritten copy + image concept for that zone.
- **Rules:** DO attach the original ad to every alteration prompt. DO run the diagnostic prompt (or the [diagnostic framework](../frameworks/valence-intensity-diagnostic.md)) before choosing a prompt. DO use the image half of each prompt for creator/production briefs. DON'T paraphrase the prompts when reusing them. They're verbatim course assets.
- **See also:** [Tone-shifting](../frameworks/tone-shifting.md) · [Prompt library](../courses/tether-lab/07-prompt-library/README.md)

By [Sarah Levinger](../people/sarah-levinger.md). Source PDF: "Valence + Intensity Prompts" (3 pages). Also see the course-wide [Prompt library](../courses/tether-lab/07-prompt-library/README.md).

## Workflow overview
1. **Diagnose** with the [diagnostic prompt](#diagnostic-prompt-from-lesson-4). Which zone is the ad in?
2. Decide the **target zone** (see [Valence-Intensity diagnostic](../frameworks/valence-intensity-diagnostic.md)).
3. **Rewrite** with the matching [alteration prompt](#the-four-alteration-prompts-verbatim). Paste it into ChatGPT **together with the underperforming ad**, "that way chat has good context for what we're currently working with, and what we need to move towards" ([lesson 5](../courses/tether-lab/03-valence-intensity-model/05-fixing-the-tone-without-rebuilding-the-ad.md) [06:52–07:05]).
4. Use the returned copy **and image ideas** to build a variant. Test it, and repeat until it lands ([lesson 6](../courses/tether-lab/03-valence-intensity-model/06-map-and-move-your-messaging.md)).

## Diagnostic prompt (from lesson 4)
Shown on screen in [lesson 4](../courses/tether-lab/03-valence-intensity-model/04-diagnosing-emotional-misfires.md) [01:30]. It isn't in the PDF.

```text
Analyze the following ad for sentiment. Place it within one of the 4 quadrants on the Valence + Intensity Map.
```

**How to use:** attach a screenshot of the ad. Optionally also attach a screenshot of the [valence/intensity map](../concepts/emotional-zones.md). Otherwise ChatGPT can use its own knowledge, "because this is a well-known psychology model" [01:39–01:55]. Expect an answer like the one Sarah got for the Copper Cow ad: a quadrant plus reasons on valence (sentiment, emotions like "enjoyment, indulgence, surprise, and delight") and intensity (urgency, drama, arousal, colour, lighting).

![Diagnostic prompt in ChatGPT](../assets/tether-lab/03-valence-intensity-model/04-sentiment-prompt-0130.jpg)
*The diagnostic prompt typed into ChatGPT in lesson 4 [01:30].*

## The four alteration prompts (verbatim)
Reproduced exactly from the PDF, in PDF order (page 1: high valence; page 2: low valence). The first sentence is bold in the original. Each prompt has three parts: **(1) a rewrite frame, (2) an emotional question about the copy, (3) an image direction.**

### High Valence, High Intensity → Zone 2 (hype)
```text
Rewrite this ad as if the reader is about to have their breakthrough moment — and your product is the catalyst.

What success, win, or identity shift would make them instantly light up? Now imagine the image as a celebration or transformation — what would make someone feel unstoppable just by seeing it?
```
- **When:** you want positive emotion with more energy: launches, performance products, achievement, momentum, getting people to *move*. This is the Z1 → Z2 shift Sarah recommends for the cozy coffee ad.
- **Sarah's gloss:** "Success, winning, very high intensity, and like aspirational marketing… something that would instantly make them light up… feel unstoppable just by seeing it." [07:06–07:32]
- **Example output (on screen):** "This coffee? Straight-up dopamine in a mug."

### High Valence, Low Intensity → Zone 1 (feel-good)
```text
Rewrite this ad as if your product is a sigh of relief they didn't know they needed.

What gentle promise or soothing outcome would make them finally feel seen?
Now imagine the image as an emotional exhale — what would feel so calming it makes them pause and breathe?
```
- **When:** you want customers to "feel okay inside": wellness, luxury, intimacy, safety, belonging. Also use it to calm an ad that's too intense or is causing anxiety.
- **Sarah's gloss:** "A sigh of relief, something they didn't know they needed, a gentle promise, something soothing… an emotional exhale, so it feels calm." [06:29–06:46]
- **Example output (on screen):** "Finally, a coffee that slows you down—in the best way."

![Zone 1 prompt slide from the video](../assets/tether-lab/03-valence-intensity-model/05-zone1-prompt-0600.jpg)
*The Zone 1 prompt as shown in lesson 5 [06:00], word for word the same as the PDF.*

### Low Valence, High Intensity → Zone 4 (danger zone)
```text
Rewrite this ad as if the reader is about to make a big mistake — and your product is the only thing that stops it.

What fear or frustration would make them snap to attention? Now imagine the image is an interruption in their feed — what would feel visually wrong enough to force the scroll to stop?
```
- **When:** high-stakes categories (health/safety, financial risk) and limited-time offers. **Use with care**: "we're not trying to trigger people's traumas."
- **Sarah's gloss:** images that "interrupt the feed… something that feels visually wrong… that looks weird. Mostly so that we could kind of stop that scroll." [08:19–08:31]
- **Example output (on screen):** "The coffee you should have gifted—before it sold out."

### Low Valence, Low Intensity → Zone 3 (pain-point whisper)
```text
Rewrite this ad as if your product is quietly calling out a truth they've been avoiding.

What subtle disappointment, nostalgia, or emptiness would make them reflect instead of scroll?
Now imagine the image as a gentle ache — what visual would whisper, "This used to mean something"?
```
- **When:** soft problem awareness, before/after contrast, setting up relief, thoughtful buyers. Sarah advises against it in **saturated industries** because "a lot of marketers live" there.
- **Sarah's gloss:** "Disappointment, nostalgia, a little bit of emptiness… that ache of like, this used to mean something. I wish it meant something again… we're not trying to make people feel bad. We just want to increase longing in them." [07:36–08:07]
- **Example output (on screen):** "It's 2025. Why are we still drinking stale beans?"

![Prompts PDF page 1](../../raw/assets/tether-lab/pdf-pages/9-Valence-+-Intensity---Prompts/p02.png)
*PDF page 1: High Valence/High Intensity and High Valence/Low Intensity prompts.*

![Prompts PDF page 2](../../raw/assets/tether-lab/pdf-pages/9-Valence-+-Intensity---Prompts/p03.png)
*PDF page 2: Low Valence/High Intensity and Low Valence/Low Intensity prompts.*

## E-book "prompt starters" (verbatim, shorter versions)
From the e-book's Chapter 6 ([summary](diagnose-why-your-ads-arent-working-ebook.md#chapter-6-map--move-your-messaging)):

```text
Zone 1: "Rewrite as a gentle promise. Something soothing. A sigh of relief."
Zone 2: "Rewrite as a breakthrough. The reader is unstoppable. Make them feel electric."
Zone 3: "Rewrite as an ache. Quiet disappointment. A truth they've avoided."
Zone 4: "Rewrite as a snap warning. They're about to mess up. Make it matter."
```
"Match your visuals too. Calm lighting vs. jarring contrast matters more than you think."

## Results from the course: one ad through all four prompts
![Four rewrites on the map](../assets/tether-lab/03-valence-intensity-model/05-four-zone-rewrites-map-0830.jpg)
*The Copper Cow Coffee ad rewritten into each zone, from [lesson 5](../courses/tether-lab/03-valence-intensity-model/05-fixing-the-tone-without-rebuilding-the-ad.md) [08:30].*

## Tips (from the course)
- Always include the **original ad** in the chat so the model knows the starting point. [L5 06:52]
- No zone is right or wrong. Pick the one that matches your customer's emotional context. [L5 08:31]
- After rewriting, check the visual treatment matches the zone (morning light/pastels for Z1, bold/energetic for Z2, sighs and tension for Z3, harsh/high-contrast/"visually wrong" for Z4). [e-book ch. 3]
- Keep iterating: "Keep testing, using those prompts." [L6 02:19]

## Related
- [Tone-shifting](../frameworks/tone-shifting.md) · [Valence-Intensity diagnostic](../frameworks/valence-intensity-diagnostic.md) · [Emotional zones](../concepts/emotional-zones.md) · [Emotional promise](../concepts/emotional-promise.md)
- [Bonus page: Valence + Intensity Prompts](../courses/tether-lab/03-valence-intensity-model/09-bonus-valence-intensity-prompts.md) · [Prompt library](../courses/tether-lab/07-prompt-library/README.md)

## Sources
- PDF: [9. Valence + Intensity - Prompts.pdf](../../raw/tether-lab/3.%20The%20Valence%20&%20Intensity%20Model/9.%20Valence%20+%20Intensity%20-%20Prompts.pdf)
- Extracted text: [9. Valence + Intensity - Prompts.md](../../raw/tether-lab/_extracted/3.%20The%20Valence%20&%20Intensity%20Model/9.%20Valence%20+%20Intensity%20-%20Prompts.md)
- Lesson 4 transcript (diagnostic prompt): [4. Diagnosing Emotional Misfires.txt](../../raw/tether-lab/_transcripts/3.%20The%20Valence%20&%20Intensity%20Model/4.%20Diagnosing%20Emotional%20Misfires.txt)
- Lesson 5 transcript (usage): [5. Fixing The Tone Without Rebuilding the ad.txt](../../raw/tether-lab/_transcripts/3.%20The%20Valence%20&%20Intensity%20Model/5.%20Fixing%20The%20Tone%20Without%20Rebuilding%20the%20ad.txt)
