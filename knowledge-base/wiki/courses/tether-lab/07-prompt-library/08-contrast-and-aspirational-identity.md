---
title: "8. Contrast + Aspirational Identity"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 8
sources:
  - raw/tether-lab/7. The Prompt Library/8_Contrast_+_Aspirational_Identity_The_Prompt_Library_·.html
  - raw/tether-lab/_extracted/7. The Prompt Library/8_Contrast_+_Aspirational_Identity_The_Prompt_Library_·.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, contrast, before-after, aspirational-identity, ideal-self, transformation, ad-concepts]
updated: 2026-10-20
---

# 8. Contrast + Aspirational Identity
> Generates 3 ad concepts that put the audience's raw "now" state next to their "next-level" self, exaggerate the emotional gap with tone and visuals, and position the brand as the vehicle for the shift: "You don't sell the product—you sell who they become when they use it."

## 🤖 Agent use
- **Use when:** transformation products (fitness, skincare, style, productivity, confidence), before/after-friendly categories, or a competitor's winner is a split-screen / mirror / "POV: one year later" ad.
- **Inputs → outputs:** brand + product + URL (+ the "now" state in customer language + the identity they want) → 3 concepts: now → next-level → brand as bridge.
- **Rules:**
  - DO keep the "now" state "raw and true" (step 1): habits, environments, emotions, not just appearance.
  - DO make it an **identity shift, not a surface-level change** (output instructions). "Becomes someone who…" beats "gets clearer skin."
  - DO check for an [angle rut](../../../concepts/angle-rut.md). This is the most Ideal-self prompt in the library, and Module 4 warns that Ideal-self aspiration is what most brands over-use and what dries up first. Pair every winner with Actual- and Ought-self rewrites ([framework](../../../frameworks/rewriting-ads-for-new-selves.md)).
  - DON'T use before/after visuals that break ad policy (body or skin "before" shaming in restricted categories). Show the contrast through behaviour, environment or emotion instead.
  - DON'T exaggerate the "after" past what customers actually get.
- **See also:** [Contrast](../../../concepts/heuristics/contrast.md) · [Aspirational identity](../../../concepts/heuristics/aspirational-identity.md) · [Ideal self](../../../concepts/ideal-self.md) · [#7 What If + Pain Point](07-what-if-scenario-and-pain-point-amplification.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Contrast](../../../concepts/heuristics/contrast.md) + [Aspirational identity](../../../concepts/heuristics/aspirational-identity.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "emotionally charged, inspiring, and identity-forward—ideal for building long-term brand alignment and action" |
| **Funnel** *(derived)* | Top to mid funnel. Also brand-building |
| **Best self** *(derived)* | [Ideal self](../../../concepts/ideal-self.md): explicitly "the audience's **ideal self-image**" |
| **Zone** *(derived)* | Zone 3 ("now") to Zone 2 ("next level") |
| **Formats named in the prompt** | Before/after video, side-by-side carousels, POV storytelling, mirror ads, internal monologue scripts |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 16–17). Only formatting is normalised.

```text
🎯 Objective:

Create ad concepts that use visual or narrative contrast to expose the gap between the audience’s current state and their ideal identity. Then position your product, service, or brand as the bridge to that transformation.

These ads should evoke a sense of *urgency, inspiration, and emotional friction*—as if the viewer is being called to step into a more powerful version of themselves.

---

🧠 Psychology Behind This Prompt:

- Contrast is a visual and emotional tool that makes differences *feel* dramatic. When you compare two versions of reality—“before” vs. “after,” struggle vs. confidence—it spotlights what’s missing and what’s possible. The emotional weight of the transformation becomes more tangible.
- Aspirational Identity taps into the audience’s ideal self-image. It’s not just about what they want to buy—it’s about who they want to *become*. Great ads speak to this upgraded identity and show that it’s already within reach.

Used together, these tactics move the audience from passive interest to *identity-driven motivation*.

---

🛠️ Instructions:

1. Start by defining the audience’s “now” state. Use relatable frustrations, habits, environments, or emotions. Keep it raw and true.
2. Contrast that with the “next-level” version of themselves. Show what it *looks like and feels like* when they reach that aspirational identity.
3. Use tone and visuals to exaggerate the contrast. Make the emotional difference obvious—so they *feel* it more than they think it.
4. Position your brand as the vehicle for that shift. You don’t sell the product—you sell who they become when they use it.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  A one-sentence contrast between the before and after states.
- Narrative Angle or Hook
  What moment, scene, or transformation do we spotlight?
- Psychological Mechanism in Use
  How contrast intensifies the emotional tension, and how aspiration guides the resolution.
- Suggested Formats
  Where this shines (e.g., before/after video, side-by-side carousels, POV storytelling, mirror ads, internal monologue scripts, etc.)

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Highlight a powerful contrast between who the audience is and who they want to be
- Evoke an identity shift, not just a surface-level change
- Show how your product enables that transformation
- Include concept summary, narrative hook, psychology application, and format suggestion

These concepts should feel emotionally charged, inspiring, and identity-forward—ideal for building long-term brand alignment and action.
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
"Now" state (frustrations, habits, environment, emotions): {{current_state}}
Aspirational identity ("someone who…"): {{ideal_identity}}
Realistic result customers actually report: {{typical_result_from_reviews}}
Ad-policy limits for before/after in this category: {{policy_notes}}
Format needed: {{format}}
```

## Why the pairing works
- **Contrast** "is a visual and emotional tool that makes differences *feel* dramatic. When you compare two versions of reality—'before' vs. 'after,' struggle vs. confidence—it spotlights what's missing and what's possible. The emotional weight of the transformation becomes more tangible." (Prompt #8)
- **Aspirational identity** "taps into the audience's **ideal self-image**. It's not just about what they want to buy—it's about who they want to *become*. Great ads speak to this upgraded identity and show that it's already within reach." (Prompt #8)
- "Used together, these tactics move the audience from passive interest to *identity-driven motivation*." Contrast makes the gap felt ("so they *feel* it more than they think it"); identity makes closing it personal.

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| The product enables a visible or felt transformation | Your account is already all-Ideal-self (check with the [three selves diagnostic](../../../frameworks/three-selves-diagnostic.md)) |
| You need a brand-building concept that also converts | Before/after visuals are restricted in your category (weight loss, some health and skin claims) |
| The audience is aspirational and future-oriented | The buyer is duty-driven (buying for kids, parents, safety). Use [#11](11-authority-borrowing-and-data-driven-insight.md) or an Ought rewrite |

## Expected output
3 concepts that each "highlight a powerful contrast between who the audience is and who they want to be", "evoke an identity shift", "show how your product enables that transformation", and include the concept summary, narrative hook, psychology application and format suggestion. The big idea is "a one-sentence contrast between the before and after states." No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| Now vs. next-level | Desire to become a more powerful version of yourself | Contrast, aspirational identity | Before/after video, side-by-side carousel | "You don't sell the product—you sell who they become when they use it." (principle) | Prompt #8 step 4 |
| Mirror ad | Self-recognition of the "now" state | Contrast, [Actual self](../../../concepts/actual-self.md) → [Ideal self](../../../concepts/ideal-self.md) | Mirror ad, internal monologue script | — | Prompt #8 formats |
| POV transformation | Identity shift over time | Aspirational identity, [goal gradient](../../../concepts/heuristics/goal-gradient-effect.md) | POV storytelling UGC | *Illustrative, not from course:* "POV: you became the friend who's always on time." | Prompt #8 formats |

## UGC script skeleton *(derived guidance)*
1. **Hook:** split-screen or a match cut, "me in March" vs. "me now". Show behaviour and emotion, not only looks.
2. **Now:** the raw, relatable detail (the messy counter, the 3 alarms).
3. **Next-level:** the same moment, done as the person they want to be.
4. **Bridge:** the product as what changed between the two shots.
5. **CTA:** identity language ("Become the person who…").

## PDF vs Skool differences
None in wording. The PDF version is on pages 16–17.

## Related
- Levers: [Contrast](../../../concepts/heuristics/contrast.md) · [Aspirational identity](../../../concepts/heuristics/aspirational-identity.md)
- Self targeting: [Ideal self](../../../concepts/ideal-self.md) · [Angle rut](../../../concepts/angle-rut.md) · [Rewriting ads for new selves](../../../frameworks/rewriting-ads-for-new-selves.md)
- Similar prompts: [#7 What If + Pain Point](07-what-if-scenario-and-pain-point-amplification.md) · [#2 Status Signaling + Open Loop](02-status-signaling-and-open-loop.md)

## Sources
- Skool page: [8_Contrast_+_Aspirational_Identity….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/8_Contrast_+_Aspirational_Identity_The_Prompt_Library_·.md>)
- PDF pages 16–17: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
