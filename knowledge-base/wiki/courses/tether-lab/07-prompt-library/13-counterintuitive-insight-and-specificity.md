---
title: "13. Counterintuitive Insight + Specificity"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 13
sources:
  - raw/tether-lab/7. The Prompt Library/13_Counterintuitive_Insight_+_Specificity_The_Prompt_Li.html
  - raw/tether-lab/_extracted/7. The Prompt Library/13_Counterintuitive_Insight_+_Specificity_The_Prompt_Li.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, counterintuitive, myth-vs-truth, specificity, cognitive-dissonance, education, ad-concepts]
updated: 2026-10-20
---

# 13. Counterintuitive Insight + Specificity
> Generates 3 ad concepts that flip a belief the audience holds ("a truth that sounds *wrong* at first, but clicks when explained") and anchor it in exact numbers, comparisons or examples so it's "credible and actionable." Target reaction: "I've never thought of it that way before."

## 🤖 Agent use
- **Use when:** the category runs on myths or "rules" your product breaks, you have precise numbers (minutes, %, grams, counts), or a competitor's winner is a "myth vs truth" / "Actually…" ad.
- **Inputs → outputs:** brand + product + URL (+ the belief to flip + exact supporting specifics) → 3 concepts: belief → counterintuitive truth → specific anchor → brand as enabler.
- **Rules:**
  - DO pick a belief that's "flawed, outdated, or too simplistic" (step 1), but stay "without being contrarian for its own sake" (step 2).
  - DO anchor with real, exact numbers and comparisons. Specificity is what makes a bold claim believable, so a vague or invented number defeats the lever.
  - DO make the brand "the enabler of this new way of thinking" (step 4): give people a way to act on the insight.
  - DON'T stack more than one counterintuitive claim per ad. One flip, one proof.
  - DON'T confuse specific with complicated. Keep it readable ([processing fluency](../../../concepts/heuristics/processing-fluency.md)).
- **See also:** [Counterintuitive insight](../../../concepts/heuristics/counterintuitive-insight.md) · [Specificity](../../../concepts/heuristics/specificity.md) · [#1 First Principles + Loss Aversion](01-first-principles-thinking-and-loss-aversion.md) · [#11 Authority + Data](11-authority-borrowing-and-data-driven-insight.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Counterintuitive insight](../../../concepts/heuristics/counterintuitive-insight.md) + [Specificity](../../../concepts/heuristics/specificity.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "surprising, immediately useful, and built to spread" |
| **Funnel** *(derived)* | Top of funnel (shareable insight) through mid funnel (education) |
| **Best self** *(derived)* | [Actual self](../../../concepts/actual-self.md) (smart, curious) and [Ought self](../../../concepts/ought-self.md) (doing it correctly) |
| **Zone** *(derived)* | Zone 2 (surprise, "aha") or a mild Zone 3 (realising you were wrong) |
| **Formats named in the prompt** | Tweet-style carousel, "myth vs truth" video hook, stat + truth combo email, bold headline with micro-copy follow-up |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 26–27). Only formatting is normalised.

```text
🎯 Objective:

Create scroll-stopping ad concepts that challenge your audience’s assumptions using a counterintuitive insight—a truth that sounds *wrong* at first, but clicks when explained. Pair this with specificity: vivid details, numbers, examples, or language that makes the insight feel credible and actionable.

These ads should feel like a *mental shortcut to rethinking something familiar*—backed by undeniable proof or clarity.

---

🧠 Psychology Behind This Prompt:

- Counterintuitive Insights are sticky because they challenge what people believe to be true. When an ad begins with “actually…” or flips a cultural norm, it creates cognitive dissonance—a kind of tension that demands resolution.
- Specificity is what makes bold claims believable. The more exact, tangible, or measurable the language, the more *trustworthy and actionable* the message becomes. Specifics turn insight into impact.

Used together, these tactics produce ads that surprise the viewer *and* give them something they can actually use or remember.

---

🛠️ Instructions:

1. Start with a belief your audience holds—but that’s flawed, outdated, or too simplistic. This could be a best practice, a “rule,” or a popular myth.
2. Flip it with a counterintuitive truth. Introduce a new mental model, stat, or belief that contradicts the norm—without being contrarian for its own sake.
3. Anchor the insight in something specific. Use real numbers, comparisons, or examples to make the message *undeniable and practical.*
4. Frame your brand as the enabler of this new way of thinking. You’re not just revealing the insight—you’re giving people a way to act on it.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  What’s the counterintuitive insight, and what common belief does it challenge?
- Narrative Angle or Hook
  What’s the sharp opening line or visual metaphor that grabs attention?
- Psychological Mechanism in Use
  How the mental dissonance (counterintuition) + exact detail (specificity) create clarity and persuasion.
- Suggested Formats
  Ideal placements (e.g., tweet-style carousel, “myth vs truth” video hook, stat + truth combo email, bold headline with micro-copy follow-up)

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Challenge a well-known belief with a smarter, unexpected insight
- Use ultra-specific examples or data to make it feel real and applicable
- Position the brand as the next step after understanding the insight
- Include the concept summary, narrative structure, psychology notes, and format ideas

These ads should feel surprising, immediately useful, and built to spread—the kind of thing people say, “I’ve never thought of it that way before.”
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
Belief / myth / "rule" to flip: {{belief}}
Exact specifics we can prove (numbers, comparisons, examples): {{specifics_with_sources}}
Target self: {{actual|ought|ideal}} · Format needed: {{format}}
```

## Why the pairing works
- **Counterintuitive insights** "are sticky because they challenge what people believe to be true. When an ad begins with 'actually…' or flips a cultural norm, it creates **cognitive dissonance**—a kind of tension that demands resolution." (Prompt #13)
- **Specificity** "is what makes bold claims believable. The more exact, tangible, or measurable the language, the more *trustworthy and actionable* the message becomes. Specifics turn insight into impact." (Prompt #13)
- "Used together, these tactics produce ads that surprise the viewer *and* give them something they can actually use or remember." The flip creates the tension; the specifics resolve it credibly.

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| A widely held category belief is wrong or outdated, and you can show it | The "flip" is just contrarian with no proof |
| You have exact, provable numbers | Claims would need clinical substantiation you don't have |
| You want shareable, save-worthy content (carousels, tweet-style) | The audience is low-awareness and doesn't hold the belief yet |

## Expected output
3 concepts that each "challenge a well-known belief with a smarter, unexpected insight", "use ultra-specific examples or data", "position the brand as the next step after understanding the insight", and include the concept summary, narrative structure, psychology notes and format ideas. No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| "Actually…" | Wanting to be right / not fooled | Counterintuitive insight, cognitive dissonance | "Myth vs truth" video hook | "actually…" (opener named in the prompt) | Prompt #13 psychology |
| Tweet-style flip | A shareable "aha" | Counterintuitive insight, specificity | Tweet-style carousel | Target reaction: "I've never thought of it that way before." | Prompt #13 |
| Exact-number proof | Trust through precision | Specificity, [framing](../../../concepts/heuristics/framing-effect.md) | Bold headline + micro-copy follow-up, stat + truth email | *Illustrative, not from course:* "Washing your face twice a day removes 0 extra dirt but 2x the barrier lipids." (made-up example. Use real data) | Prompt #13 step 3 |

## PDF vs Skool differences
None in wording. The PDF version is on pages 26–27.

## Related
- Levers: [Counterintuitive insight](../../../concepts/heuristics/counterintuitive-insight.md) · [Specificity](../../../concepts/heuristics/specificity.md)
- Similar prompts: [#1 First Principles + Loss Aversion](01-first-principles-thinking-and-loss-aversion.md) · [#3 Curiosity + Reverse Psychology](03-curiosity-and-reverse-psychology.md) · [#6 Pattern Disruption + Hidden Truth](06-pattern-disruption-and-hidden-truth.md) · [#11 Authority + Data](11-authority-borrowing-and-data-driven-insight.md)
- Live-session evidence for specificity: the [July 9 session](../05-live-recordings/2025-07-09-live-with-sarah.md) (situational specificity)

## Sources
- Skool page: [13_Counterintuitive_Insight_+_Specificity….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/13_Counterintuitive_Insight_+_Specificity_The_Prompt_Li.md>)
- PDF pages 26–27: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
