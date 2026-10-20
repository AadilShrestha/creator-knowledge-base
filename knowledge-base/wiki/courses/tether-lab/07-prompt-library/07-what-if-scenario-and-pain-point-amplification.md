---
title: "7. What If Scenario + Pain Point Amplification"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 7
sources:
  - raw/tether-lab/7. The Prompt Library/7_What_If_Scenario_+_Pain_Point_Amplification_The_Promp.html
  - raw/tether-lab/_extracted/7. The Prompt Library/7_What_If_Scenario_+_Pain_Point_Amplification_The_Promp.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, what-if, pain-point, agitation, cost-of-inaction, high-ticket, ad-concepts]
updated: 2026-10-20
---

# 7. What If Scenario + Pain Point Amplification
> Generates 3 ad concepts that open with a vivid "What if…" world (dream state, or a dramatic gain/loss), contrast it with the painful present, amplify the cost of staying stuck, and position the brand as "the clear (and often only) path out." The tone is "immersive tension + undeniable clarity", intended "for high-commitment conversions."

## 🤖 Agent use
- **Use when:** higher-priced or high-commitment purchases where the buyer needs emotional urgency to act, the cost of inaction is real and measurable, or a competitor's winner uses "Imagine if…" / split-screen before-after storytelling.
- **Inputs → outputs:** brand + product + URL (+ the dream outcome + the current pain + what inaction costs) → 3 concepts: "What if…" → painful reality → amplified cost → brand as bridge.
- **Rules:**
  - DO make the "What if…" **specific, not vague** (step 1). "What if you woke up at 6:10 without an alarm" beats "What if you felt better."
  - DO quantify the cost of inaction with true numbers: "time, money, confidence, or opportunity" (step 3).
  - DO end on the bridge. The concept must show the brand as the way out, otherwise you've only made people feel bad.
  - DON'T amplify pain beyond what the product fixes. Agitation that outruns the solution is a Zone 4 [misfire](../../../concepts/emotional-misfire.md).
  - DON'T write "only path out" literally if competitors clearly exist. Keep it as framing, not a claim.
- **See also:** [What-if scenario](../../../concepts/heuristics/what-if-scenario.md) · [Pain point amplification](../../../concepts/heuristics/pain-point-amplification.md) · [Loss aversion](../../../concepts/heuristics/loss-aversion.md) · [#8 Contrast + Aspirational Identity](08-contrast-and-aspirational-identity.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [What-if scenario](../../../concepts/heuristics/what-if-scenario.md) + [Pain point amplification](../../../concepts/heuristics/pain-point-amplification.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "narrative-driven, emotionally sharp, and motivational through contrast—perfect for high-commitment conversions" |
| **Funnel** *(derived)* | Mid to bottom funnel: problem-aware buyers weighing a bigger commitment |
| **Best self** *(derived)* | The gap between the [Actual self](../../../concepts/actual-self.md) (stuck now) and the [Ideal self](../../../concepts/ideal-self.md) (the "What if") |
| **Zone** *(derived)* | Alternates Zone 2 (dream) and Zone 3/4 (pain, cost). A deliberate valence swing; see [valence](../../../concepts/valence.md) |
| **Formats named in the prompt** | Cinematic video, split-screen before/after, testimonial monologue, dramatic carousel |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 14–15). Only formatting is normalised.

```text
🎯 Objective:

Create powerful ad concepts that open with a vivid “What If” scenario—pulling the viewer into an alternate world—and then intensify the desire to escape their current situation through Pain Point Amplification. These ads should make the audience feel the gap between where they are and where they could be—and the frustration of staying stuck.

The tone should feel like *immersive tension + undeniable clarity*—a moment of truth delivered with storytelling heat.

---

🧠 Psychology Behind This Prompt:

- “What If” Scenarios activate the imagination. They open a new mental frame—helping the viewer visualize what’s possible, sometimes utopian or dystopian. They make abstract benefits *feel real and emotionally close*.
- Pain Point Amplification deepens discomfort by shining a light on what isn’t working. It makes the current reality feel *unbearably inefficient, slow, costly, or embarrassing*—turning discomfort into motivation.

Together, these tactics elevate emotional urgency. The viewer is drawn into a world they want—while feeling the sting of the one they’re still stuck in.

---

🛠️ Instructions:

1. Begin with a compelling “What if…” scenario. Show them a dream state or dramatic alternate outcome (gain or loss). It should feel specific, not vague.
2. Contrast it with a painful reality. Use language, visuals, or emotion to make their current state feel unsustainable.
3. Amplify the frustration of inaction. Highlight how much time, money, confidence, or opportunity they’re losing.
4. Position your offer as the bridge. The concept should end by showing your brand as the clear (and often only) path out.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  A summary of the imagined outcome + the amplified pain.
- Narrative Angle or Hook
  The “What if…” scenario that kicks it off and the moment of emotional impact.
- Psychological Mechanism in Use
  How the scenario inspires change and how the pain point turns discomfort into urgency.
- Suggested Formats
  Where this works best (e.g., cinematic video, split-screen before/after ad, testimonial monologue, dramatic carousel, etc.)

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Start with a vivid “What if…” idea that rewrites the viewer’s reality
- Highlight the pain or frustration of their current state
- Build emotional urgency around the cost of inaction
- Include the concept summary, narrative angle, psychology notes, and format ideas

The tone should feel narrative-driven, emotionally sharp, and motivational through contrast—perfect for high-commitment conversions.
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
Dream state / alternate outcome (specific): {{what_if_scenario}}
Current painful reality (customer words): {{pain_in_customer_language}}
Cost of inaction (true numbers): {{time_money_confidence_opportunity_lost}}
Target self: {{actual|ideal|ought}} · Format needed: {{format}}
```

## Why the pairing works
- **"What If" scenarios** "activate the imagination. They open a new mental frame—helping the viewer visualize what's possible, sometimes utopian or dystopian. They make abstract benefits *feel real and emotionally close*." (Prompt #7)
- **Pain point amplification** "deepens discomfort by shining a light on what isn't working. It makes the current reality feel *unbearably inefficient, slow, costly, or embarrassing*—turning discomfort into motivation." (Prompt #7)
- "Together, these tactics elevate emotional urgency. The viewer is drawn into a world they want—while feeling the sting of the one they're still stuck in." The scenario pulls; the pain pushes.

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| The purchase is considered or high-ticket and needs emotional momentum | It's a low-price impulse buy. The drama is out of proportion |
| The pain is real, frequent and nameable | The pain is sensitive (grief, illness, trauma). Amplifying it is exploitative |
| You can show a credible "after" (testimonial, demo) | You have no proof of the dream outcome. Use [#11](11-authority-borrowing-and-data-driven-insight.md) to build credibility first |

## Expected output
3 concepts that each "start with a vivid 'What if…' idea that rewrites the viewer's reality", "highlight the pain or frustration of their current state", "build emotional urgency around the cost of inaction", and include the concept summary, narrative angle, psychology notes and format ideas. No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| Utopian "What if…" | Desire for the dream state, made concrete | What-if scenario, [affect heuristic](../../../concepts/heuristics/affect-heuristic.md) | Cinematic video, testimonial monologue | *Illustrative, not from course:* "What if Sunday nights didn't feel like dread?" | Prompt #7 step 1 |
| Dystopian "What if…" | Fear of a future loss | What-if scenario, [loss aversion](../../../concepts/heuristics/loss-aversion.md) | Dramatic carousel | — | Prompt #7 psychology ("sometimes… dystopian") |
| Split-screen gap | The sting of the current reality vs. what could be | Pain point amplification, [contrast](../../../concepts/heuristics/contrast.md) | Split-screen before/after | — | Prompt #7 formats |

## UGC script skeleton *(derived guidance)*
1. **Hook:** "What if…" plus one sensory, specific image of the better world (VO over aspirational b-roll).
2. **Snap back:** a hard cut to the current reality, with real, slightly embarrassing detail.
3. **Amplify:** "Every month you wait, that's [true cost]." On-screen counter.
4. **Bridge:** the product as the way from there to here, shown in use.
5. **CTA:** return to the "What if" image, now attainable.

## PDF vs Skool differences
None in wording. The PDF version is on pages 14–15 (minor spacing: "1.Begin", "2.Contrast").

## Related
- Levers: [What-if scenario](../../../concepts/heuristics/what-if-scenario.md) · [Pain point amplification](../../../concepts/heuristics/pain-point-amplification.md)
- Similar prompts: [#8 Contrast + Aspirational Identity](08-contrast-and-aspirational-identity.md) · [#1 First Principles + Loss Aversion](01-first-principles-thinking-and-loss-aversion.md) · [#12 Micro-Story + Suspense](12-micro-story-and-suspense.md)
- Tone control: [Emotional zones](../../../concepts/emotional-zones.md) · [Valence + Intensity prompts](../../../resources/valence-intensity-prompts.md)

## Sources
- Skool page: [7_What_If_Scenario_+_Pain_Point_Amplification….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/7_What_If_Scenario_+_Pain_Point_Amplification_The_Promp.md>)
- PDF pages 14–15: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
