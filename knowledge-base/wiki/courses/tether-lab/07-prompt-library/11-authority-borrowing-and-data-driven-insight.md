---
title: "11. Authority Borrowing + Data-Driven Insight"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 11
sources:
  - raw/tether-lab/7. The Prompt Library/11_Authority_Borrowing_+_Data_Driven_Insight_The_Prompt.html
  - raw/tether-lab/_extracted/7. The Prompt Library/11_Authority_Borrowing_+_Data_Driven_Insight_The_Prompt.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, authority, halo-effect, data, statistics, proof, skeptical-audience, ad-concepts]
updated: 2026-10-20
---

# 11. Authority Borrowing + Data-Driven Insight
> Generates 3 ad concepts that lead with a trusted stat, source or expert point of view, turn it into a usable insight, and position the brand as the **applier** of that insight ("You're not claiming the idea; you're making it actionable"). The tone is "smart, elevated, and trustworthy—designed for skeptical minds."

## 🤖 Agent use
- **Use when:** the audience is skeptical, analytical or performance-minded, the product has real research, certifications, expert endorsements or press, or a competitor's winner is a "1 stat that changed how I…" / expert-quote ad.
- **Inputs → outputs:** brand + product + URL + **real stats with sources** + any expert/institution association you're allowed to cite → 3 concepts: stat → insight → brand as applier.
- **Rules:**
  - DO supply the stats and sources yourself. LLMs invent plausible statistics. **Verify every number before it goes in a script or static.** Sarah's own rule from a live session: "Don't fabricate data" ([July 9 session](../05-live-recordings/2025-07-09-live-with-sarah.md)).
  - DO "use the data to fuel insight—don't just display it" (step 2). Stat → so what → therefore.
  - DO keep it "sharp, minimal, and confident. Let the logic lead—don't oversell" (step 4).
  - DON'T imply endorsement you don't have. "Borrowed authority" means citing a real, attributable source, not dressing a creator up as a doctor.
  - DON'T make this the only angle. Heuristics 101 notes authority is "very expected in DTC" ([authority bias](../../../concepts/heuristics/authority-bias.md)).
- **See also:** [Authority borrowing](../../../concepts/heuristics/authority-borrowing.md) · [Data-driven insight](../../../concepts/heuristics/data-driven-insight.md) · [Authority bias](../../../concepts/heuristics/authority-bias.md) · [Specificity](../../../concepts/heuristics/specificity.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Authority borrowing](../../../concepts/heuristics/authority-borrowing.md) (halo effect) + [Data-driven insight](../../../concepts/heuristics/data-driven-insight.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "rational, persuasive, and calmly confident—ideal for performance-minded audiences who value proof over hype" |
| **Funnel** *(derived)* | Mid to bottom funnel (objection handling), and TOFU for analytical niches |
| **Best self** *(derived)* | [Ought self](../../../concepts/ought-self.md) (doing the responsible, evidence-based thing). [Actual self](../../../concepts/actual-self.md) for "I'm a research person" buyers |
| **Zone** *(derived)* | Low intensity. Zone 1 (calm confidence), or a mild Zone 3 when the stat exposes a problem |
| **Formats named in the prompt** | Minimalist stat-based carousel, "1 stat that changed how I market" short-form video, expert quote + real-world proof pairing |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 22–23). Only formatting is normalised.

```text
🎯 Objective:

Build high-conversion ad concepts that boost credibility and signal trust by leaning on borrowed authority (recognized experts, brands, or sources) and delivering a data-driven insight that reframes the audience’s thinking or strategy. These ads should feel like the *aha moment* people didn’t realize they were missing—anchored in hard proof, not hype.

Tone should feel *smart, elevated, and trustworthy*—designed for skeptical minds.

---

🧠 Psychology Behind This Prompt:

- Authority Borrowing taps into the halo effect—when we trust a brand, person, or source, we project that trust onto whatever is associated with them. Referencing known names, institutions, or expert voices gives instant legitimacy.
- Data-Driven Insight appeals to the analytical mind. People are more likely to believe and act when they see a stat, number, or correlation that surprises them—especially when it challenges their assumptions.

Together, these tactics allow your brand to *educate while persuading*—making your point feel objective, logical, and too well-supported to ignore.

---

🛠️ Instructions:

1. Start with a surprising stat, quote, or expert-backed claim. Bonus if it challenges a myth, assumption, or outdated behavior.
2. Tie it directly to a clear takeaway or reframed belief. Use the data to fuel insight—don’t just display it.
3. Position your brand as the *applier* of this insight. You’re not claiming the idea; you’re making it *actionable.*
4. Keep the tone sharp, minimal, and confident. Let the logic lead—don’t oversell.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  What’s the stat or claim? And what insight does it unlock?
- Narrative Angle or Hook
  How do we open the ad—what’s the statement or tension being introduced?
- Psychological Mechanism in Use
  How authority and data are layered to create credibility and clarity.
- Suggested Formats
  Ideal use cases (e.g., minimalist stat-based carousel, “1 stat that changed how I market” short-form video, expert quote + real-world proof pairing, etc.)

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Lead with a trusted stat, source, or expert POV
- Translate that data into a usable insight
- Tie the insight to your product, methodology, or positioning
- Include the concept summary, narrative hook, psychology note, and best format(s)

These concepts should feel rational, persuasive, and calmly confident—ideal for performance-minded audiences who value proof over hype.
```

### Fill-in block (append at the very bottom)
Per Sarah's tutorial, add the brand at the very bottom ([01:01]–[01:58]).

```text
Brand: {{brand_name}}
Product: {{product_name}} ({{one_line_description}})
Website / landing page: {{url_or_pasted_page_copy}}
```

Optional agent context *(wiki addition; strongly recommended)*:

```text
Verified stats / studies to use (with source + year; do not invent others):
{{stat_1 — source}}
{{stat_2 — source}}
Authorities we may cite (experts, institutions, press, certifications): {{authorities}}
Myth or outdated behaviour the data challenges: {{myth}}
Format needed: {{format}}
```

## Why the pairing works
- **Authority borrowing** "taps into the **halo effect**—when we trust a brand, person, or source, we project that trust onto whatever is associated with them. Referencing known names, institutions, or expert voices gives instant legitimacy." (Prompt #11)
- **Data-driven insight** "appeals to the **analytical mind**. People are more likely to believe and act when they see a stat, number, or correlation that surprises them—especially when it challenges their assumptions." (Prompt #11)
- "Together, these tactics allow your brand to *educate while persuading*—making your point feel objective, logical, and too well-supported to ignore."

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| You have real research, clinicals, certifications, press or expert partners | You'd need to invent or stretch a stat |
| Buyers are skeptical, high-consideration or B2B | Impulse/hedonic purchases where emotion leads ([#12](12-micro-story-and-suspense.md), [#8](08-contrast-and-aspirational-identity.md)) |
| A myth in the category can be corrected with data | The authority is a celebrity with no relevant expertise. The halo is weak and reads as paid |

## Expected output
3 concepts that each "lead with a trusted stat, source, or expert POV", "translate that data into a usable insight", "tie the insight to your product, methodology, or positioning", and include the concept summary, narrative hook, psychology note and best formats. The big idea answers "What's the stat or claim? And what insight does it unlock?" No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| "1 stat that changed how I…" | Wanting the smart, proven way | Data-driven insight, [authority](../../../concepts/heuristics/authority-bias.md) | Short-form talking head | "1 stat that changed how I market" (format named in prompt) | Prompt #11 formats |
| Myth-busting stat | Feeling misled by the old advice | Data-driven insight, [counterintuitive insight](../../../concepts/heuristics/counterintuitive-insight.md) | Minimalist stat carousel | — | Prompt #11 step 1 |
| Expert says → we apply | Trust by association | Authority borrowing (halo) | Expert quote + real-world proof pairing | "You're not claiming the idea; you're making it actionable." (principle) | Prompt #11 step 3 |

## UGC script skeleton *(derived guidance)*
1. **Hook:** the stat on screen in big type; the creator reacts or reads it. Cite the source on screen.
2. **Insight:** "Which means…" (one sentence).
3. **Authority:** who found it / who agrees (on-screen logo or name, only if permitted).
4. **Application:** how our product applies the insight (show the mechanism).
5. **CTA:** calm and confident. No hype.

## PDF vs Skool differences
None in wording. The PDF version is on pages 22–23. (The Welcome-tour screenshot of the Skool list titles it "Data-Driven Insights", plural. The page itself says "Insight".)

## Related
- Levers: [Authority borrowing](../../../concepts/heuristics/authority-borrowing.md) · [Data-driven insight](../../../concepts/heuristics/data-driven-insight.md) · [Authority bias](../../../concepts/heuristics/authority-bias.md)
- Similar prompts: [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md) · [#1 First Principles + Loss Aversion](01-first-principles-thinking-and-loss-aversion.md) · [#6 Pattern Disruption + Hidden Truth](06-pattern-disruption-and-hidden-truth.md)

## Sources
- Skool page: [11_Authority_Borrowing_+_Data_Driven_Insight….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/11_Authority_Borrowing_+_Data_Driven_Insight_The_Prompt.md>)
- PDF pages 22–23: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
