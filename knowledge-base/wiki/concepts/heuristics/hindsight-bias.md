---
title: "Hindsight Bias"
type: concept
course: tether-lab
sources:
  - raw/tether-lab/_extracted/7. The Prompt Library/15_The_‘Why_Didn’t_I_See_This_’_Framework_The_Prompt_Li.md
tags: [lever, hindsight-bias, cognitive-bias, hooks, realization, prompt-library]
updated: 2026-10-20
---

# Hindsight Bias

> **"Our brain's favorite lie: 'I knew it all along.'"** (Prompt Library #15, "The 'Why Didn't I See This?' Framework"). Expose a common mistake in retrospect so the viewer feels they "should've caught it—but didn't", then hand them the obvious fix.

## 🤖 Agent use
- **Use when:** writing hooks for a product that replaces an outdated habit or tool, when the category's common mistake is visible once named, or when tearing down "you ever notice…?" competitor ads.
- **Inputs → outputs:** a widespread mistake or outdated method in the category → a hindsight hook (step 1) → a [bounded-rationality](bounded-rationality.md) absolution (step 2) → a low-friction alternative (step 3). Prompt #15 asks for 3–5 hooks.
- **Rules:**
  - DO make the mistake feel obvious *in retrospect*: "Make the reader feel like they should've caught it—but didn't." (#15 step 1)
  - DO follow it straight away with absolution. Make them "feel smart for surviving, not stupid for struggling" (#15 step 2).
  - DO end on "a low-friction alternative—something that feels so rational, it's irrational not to try it now" (#15 step 3).
  - DO update date-bound example lines to the current year before using them ("designed in 2004", "What worked in 2020 won't win in 2025").
  - DON'T leave the viewer in "I should have known". Without step 2 it lands as blame.
- **See also:** [Prompt #15: The "Why Didn't I See This?" Framework](../../courses/tether-lab/07-prompt-library/15-hindsight-bias-and-bounded-rationality.md) · [Bounded rationality](bounded-rationality.md) · [Counterintuitive insight](counterintuitive-insight.md) · [Reframing](reframing.md)

## Definition
"Hindsight Bias – our brain's favorite lie: 'I knew it all along.'" (Prompt Library #15, Skool page only. The prompt isn't in the PDF.)

The framework's goal: "These hooks should make people realize they've been missing something obvious—then hand them a clear, low-friction upgrade they'll feel smart for choosing."

## The three-step hook framework (#15)
1. **Trigger "Wait, Why Didn't I See This?"** with hindsight bias. Expose a common mistake in retrospect.
2. **"Show How the Brain Made the Best of a Bad Menu"** with [bounded rationality](bounded-rationality.md). They didn't fail, they chose from bad or incomplete options.
3. **"Offer a Simpler, Smarter Path Forward."** A low-friction alternative.

## Hooks (verbatim examples from Prompt #15)
*Emotion/zone and self columns are wiki tags (derived). The source doesn't specify them.*

| Hook (verbatim or near) | Heuristic(s) | Emotion / zone | Self targeted | Why it works | Source |
|---|---|---|---|---|---|
| "You ever notice how nobody actually finishes their protein powder?" | Hindsight bias | Wry recognition, Zone 3 (wiki tag) | Actual (wiki tag) | Names a shared, obvious-in-retrospect failure | Prompt Library #15 (Skool page), step 1 |
| "Of course the old way didn't work. It was designed in 2004." | Hindsight bias, reframing | Relief, Zone 1 (wiki tag) | Actual (wiki tag) | "Of course" makes the failure feel predictable and blames the method, not the user. Update the year | Prompt Library #15 (Skool page), step 1 |
| "Turns out, 'add to cart' doesn't mean 'buy.' You knew that, right? | Hindsight bias | Recognition, Zone 3 (wiki tag) | Actual (wiki tag) | "You knew that, right?" invites the I-knew-it-all-along feeling. Closing quote missing in source | Prompt Library #15 (Skool page), step 1 |
| "You weren't doing it wrong. You just didn't know there was another option." | Bounded rationality | Relief, Zone 1 (wiki tag) | Actual (wiki tag) | Absolves the past choice and opens the door to a new one | Prompt Library #15 (Skool page), step 2 |
| "You made the best choice… with what you thought you had." | Bounded rationality | Validation, Zone 1 (wiki tag) | Actual (wiki tag) | Validates, then hints the options were incomplete | Prompt Library #15 (Skool page), step 2 |
| "This isn't about willpower. It's about better inputs." | Bounded rationality, reframing | Relief, Zone 1 (wiki tag) | Ought → Actual (wiki tag) | Moves the cause from character to inputs | Prompt Library #15 (Skool page), step 2 |
| "What worked in 2020 won't win in 2025. This will." | Temporal contrast, hindsight | Momentum, Zone 2 (wiki tag) | Ideal (wiki tag) | Dates the old way and makes switching feel current. Update the years | Prompt Library #15 (Skool page), step 3 |
| "One simple change. One giant leap for your sanity." | Processing fluency, transformation shortcut | Relief/hope, Zone 1–2 (wiki tag) | Ideal (wiki tag) | Low friction + big outcome | Prompt Library #15 (Skool page), step 3 |
| "The smart choice isn't always obvious. Until now." | Hindsight bias, curiosity | Satisfaction, Zone 1 (wiki tag) | Actual (wiki tag) | Lets the viewer feel smart for choosing now | Prompt Library #15 (Skool page), step 3 |

## Deploy in a UGC script
*Derived guidance.*

| Script slot | Pattern | Visual cue |
|---|---|---|
| Hook | A step-1 line said as a wry observation | Creator holding the half-used old product (the unfinished protein tub) |
| Problem / absolution | A step-2 line, warm tone | Creator nodding, "same" energy |
| Mechanism + CTA | A step-3 line + product | One-step demo of the product |

## Spot it in a competitor ad
- Openers: "You ever notice…", "Of course X didn't work", "Turns out…", "You knew that, right?", "Nobody actually…".
- Tag: `lever-hindsight-bias`. Add `lever-bounded-rationality` if the ad absolves the viewer.

## Common mistakes
- Stopping at step 1, so the viewer feels stupid and scrolls.
- A "mistake" that isn't widely shared. The hook needs instant recognition.
- Dated year references left unchanged.

## Pairs with
- **[Bounded rationality](bounded-rationality.md)** (Prompt #15).
- **[Counterintuitive insight](counterintuitive-insight.md)**, **[Reframing](reframing.md)**, **[First principles thinking](first-principles-thinking.md)**: Prompt #1 also aims for "Of course—why didn't I see this before?"
- **[Transformation shortcut](transformation-shortcut.md)** and **[Processing fluency](processing-fluency.md)** for step 3.

## Where it's taught
- [Prompt Library #15: The "Why Didn't I See This?" Framework](../../courses/tether-lab/07-prompt-library/15-hindsight-bias-and-bounded-rationality.md) (Skool page only)

## Related
[Bounded rationality](bounded-rationality.md) · [Reframing](reframing.md) · [Counterintuitive insight](counterintuitive-insight.md) · [Actual self](../actual-self.md) · [Heuristics hub](../heuristics.md)
