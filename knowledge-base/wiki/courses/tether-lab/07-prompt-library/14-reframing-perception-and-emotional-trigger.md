---
title: "14. Reframing Perception + Emotional Trigger"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 14
sources:
  - raw/tether-lab/7. The Prompt Library/14_Reframing_Perception_+_Emotional_Trigger_The_Prompt_.html
  - raw/tether-lab/_extracted/7. The Prompt Library/14_Reframing_Perception_+_Emotional_Trigger_The_Prompt_.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, reframing, emotional-trigger, belief-change, validation, ad-concepts]
updated: 2026-10-20
---

# 14. Reframing Perception + Emotional Trigger
> Generates 3 ad concepts that take something familiar (a problem, habit or identity), reframe what it *means*, and then attach one named emotion (relief, shame, pride, guilt, joy, regret, resentment…) so the shift is felt, not just understood. Target thought: *"Wait… I've been looking at this all wrong."*

## 🤖 Agent use
- **Use when:** the audience has normalised a problem ("it's just genetics", "everyone's tired"), you need to change *how they feel* about a behaviour, or a competitor's winner is a "You thought X? Try again…" ad. It's also the most flexible prompt for steering a concept into a chosen [emotional zone](../../../concepts/emotional-zones.md): pick the trigger emotion first.
- **Inputs → outputs:** brand + product + URL (+ the belief/behaviour to reframe + the target emotion) → 3 concepts: original belief → flip → emotion → brand as "truth-teller or liberator."
- **Rules:**
  - DO choose **one** emotion per concept and name it in the fill-in. The prompt lists "relief, shame, liberation, guilt, joy, regret, pride, resentment".
  - DO map the emotion to a zone before generating: relief/pride/joy are high valence; guilt/shame/regret/resentment are low valence. Check the result with the [V+I diagnostic prompt](../../../resources/valence-intensity-prompts.md).
  - DO use Sarah's belief-change principle: get people to "question: is what you believe actually real?" ([July 9 session](../05-live-recordings/2025-07-09-live-with-sarah.md) [0:54:54]).
  - DON'T use shame/guilt as the *final* emotion. Land on validation ("deeply validating" is the prompt's own target).
  - DON'T confuse it with the [framing effect](../../../concepts/heuristics/framing-effect.md) (same facts, different presentation). Reframing changes the *meaning* of the problem itself. See [reframing](../../../concepts/heuristics/reframing.md).
- **See also:** [Reframing](../../../concepts/heuristics/reframing.md) · [Emotional trigger](../../../concepts/heuristics/emotional-trigger.md) · [Valence](../../../concepts/valence.md) · [Emotional promise](../../../concepts/emotional-promise.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Reframing](../../../concepts/heuristics/reframing.md) (perception) + [Emotional trigger](../../../concepts/heuristics/emotional-trigger.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "emotionally intelligent, perspective-shifting, and deeply validating—like ads that speak the truth people didn't know they needed" |
| **Funnel** *(derived)* | Top to mid funnel (problem reframing, category education) |
| **Best self** *(derived)* | Any. Guilt/duty triggers hit the [Ought self](../../../concepts/ought-self.md), pride/joy the [Ideal self](../../../concepts/ideal-self.md), relief/validation the [Actual self](../../../concepts/actual-self.md) |
| **Zone** *(derived)* | Set by the chosen trigger emotion (see [emotional zones](../../../concepts/emotional-zones.md)) |
| **Formats named in the prompt** | "You thought X? Try again…" video, emotion-forward testimonial, confessional copy post, visual metaphor carousel |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 28–29). Only formatting is normalised.

```text
🎯 Objective:

Develop ad concepts that take something familiar—like a problem, habit, or identity—and reframe it in a way that changes how the audience *feels* about it. Then, use an emotional trigger (frustration, guilt, pride, relief, shame, desire, etc.) to heighten the impact and prompt immediate resonance or action.

These ads should make the audience think, *“Wait… I’ve been looking at this all wrong”*—and feel something powerful because of it.

---

🧠 Psychology Behind This Prompt:

- Reframing is a classic persuasion tool—it helps people shift from one belief to another by changing the context or the emotional angle. Instead of fighting resistance head-on, it offers a new lens. “What if your problem isn’t what you think it is?”
- Emotional Triggers amplify that shift. Whether it’s relief, pride, embarrassment, nostalgia, or even righteous anger, emotions drive memory and action. When people feel *seen and stirred*, they’re more likely to click, engage, or buy.

Together, these tactics help you change minds by changing meaning, then motivate action by amplifying feeling.

---

🛠️ Instructions:

1. Identify a belief, behavior, or problem your audience thinks they understand. This could be something they’ve normalized, ignored, or misunderstood.
2. Reframe it to reveal a deeper truth. Show that what they thought was “fine” is actually keeping them stuck—or that what they dismissed is the key to moving forward.
3. Pair it with an emotional trigger. Tap into a core feeling: relief, shame, liberation, guilt, joy, regret, pride, resentment, etc.
4. Position your offer as the outcome of this reframe. You’re not just selling a product—you’re selling *clarity, validation, and a new perspective.*

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  What is being reframed, and what emotion is being stirred?
- Narrative Angle or Hook
  How do we introduce the original belief—and flip it?
- Psychological Mechanism in Use
  How the shift in perception + feeling drives engagement and re-evaluation.
- Suggested Formats
  Best expressions (e.g., “You thought X? Try again…” video, emotion-forward testimonial, confessional copy post, visual metaphor carousel, etc.)

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Reframe a common belief or identity in a fresh, emotionally relevant way
- Trigger a specific feeling that drives urgency or reflection
- Position the brand as the “truth-teller” or liberator of this new view
- Include the concept summary, narrative hook, psychological mechanisms, and format suggestions

These concepts should feel emotionally intelligent, perspective-shifting, and deeply validating—like ads that speak the truth people didn’t know they needed.
```

### Fill-in block (append at the very bottom)
Per Sarah's tutorial, add the brand at the very bottom ([01:01]–[01:58]).

```text
Brand: {{brand_name}}
Product: {{product_name}} ({{one_line_description}})
Website / landing page: {{url_or_pasted_page_copy}}
```

Optional agent context *(wiki addition)*:

```text
Belief / behaviour / problem to reframe: {{normalised_belief}}
Emotion to trigger (pick one per concept): {{relief|pride|joy|liberation|guilt|shame|regret|resentment|nostalgia}}
Target zone: {{zone_1|zone_2|zone_3|zone_4}} · Target self: {{actual|ideal|ought}}
Format needed: {{format}}
```

## Why the pairing works
- **Reframing** "is a classic persuasion tool—it helps people shift from one belief to another by **changing the context** or the emotional angle. Instead of fighting resistance head-on, it offers a new lens. 'What if your problem isn't what you think it is?'" (Prompt #14)
- **Emotional triggers** "amplify that shift. Whether it's relief, pride, embarrassment, nostalgia, or even righteous anger, emotions drive memory and action. When people feel *seen and stirred*, they're more likely to click, engage, or buy." (Prompt #14)
- "Together, these tactics help you **change minds by changing meaning**, then **motivate action by amplifying feeling**."
- It fits the course's core claim that buying is decided by the emotional, subconscious brain ([subconscious vs conscious mind](../../../concepts/subconscious-vs-conscious-mind.md)). Sarah's July 9 "belief changer" example: "You don't have to just go bald… I know people just say it's genetics. It's not. You can reverse it." [0:54:54–0:55:50]

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| The audience has normalised or misread their problem | The audience already sees the problem correctly. Go straight to solution/proof |
| You want to control the emotional zone of a concept precisely | You can't stand behind the new meaning (e.g. "it's not genetics" with no evidence) |
| A tone-shift of an existing winner is needed (same offer, new meaning) | Shame-heavy categories (body, parenting) where the trigger could backfire |

## Expected output
3 concepts that each "reframe a common belief or identity in a fresh, emotionally relevant way", "trigger a specific feeling that drives urgency or reflection", "position the brand as the 'truth-teller' or liberator of this new view", and include the concept summary, narrative hook, psychological mechanisms and format suggestions. The big idea answers "What is being reframed, and what emotion is being stirred?" No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| "You thought X? Try again…" | Being misled about your own problem | Reframing, emotional trigger | Talking-head video | "You thought X? Try again…" (format named in prompt) | Prompt #14 formats |
| "What if your problem isn't what you think it is?" | Hope that the problem is solvable | Reframing, [hidden truth](../../../concepts/heuristics/hidden-truth.md) | Confessional copy post, visual-metaphor carousel | "What if your problem isn't what you think it is?" | Prompt #14 psychology |
| Belief changer | Control over something assumed fixed | Reframing, relief | Emotion-forward testimonial | "You don't have to just go bald… people just say it's genetics. It's not. You can reverse it." | [July 9 session](../05-live-recordings/2025-07-09-live-with-sarah.md) [0:54:54] |

## PDF vs Skool differences
None in wording. The PDF version is on pages 28–29 and is the last prompt in the PDF.

## Related
- Levers: [Reframing](../../../concepts/heuristics/reframing.md) · [Emotional trigger](../../../concepts/heuristics/emotional-trigger.md) · [Framing effect](../../../concepts/heuristics/framing-effect.md)
- Emotion tools: [Valence](../../../concepts/valence.md) · [Intensity](../../../concepts/intensity.md) · [Tone-shifting](../../../frameworks/tone-shifting.md) · [Valence + Intensity prompts](../../../resources/valence-intensity-prompts.md)
- Similar prompts: [#15 Hindsight Bias + Bounded Rationality](15-hindsight-bias-and-bounded-rationality.md) · [#6 Pattern Disruption + Hidden Truth](06-pattern-disruption-and-hidden-truth.md) · [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md)

## Sources
- Skool page: [14_Reframing_Perception_+_Emotional_Trigger….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/14_Reframing_Perception_+_Emotional_Trigger_The_Prompt_.md>)
- PDF pages 28–29: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
