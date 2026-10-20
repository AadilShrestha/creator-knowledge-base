---
title: "2. Status Signaling + Open Loop"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 2
sources:
  - raw/tether-lab/7. The Prompt Library/2_Status_Signaling_+_Open_Loop_The_Prompt_Library_·_Tet.html
  - raw/tether-lab/_extracted/7. The Prompt Library/2_Status_Signaling_+_Open_Loop_The_Prompt_Library_·_Tet.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, status-signaling, open-loop, exclusivity, insider, ideal-self, ad-concepts]
updated: 2026-10-20
---

# 2. Status Signaling + Open Loop
> Generates 3 ad concepts that feel like "an exclusive peek into a world only a select few understand… and the viewer is just one click away from joining them." Status sets the identity ("people like me are already doing this"). The open loop withholds the answer so the viewer has to click.

## 🤖 Agent use
- **Use when:** premium, trend-led or early-adopter products. Also use it when a competitor's winner uses insider language ("what top performers do", "the thing nobody's talking about yet"), or when you need curiosity-led TOFU hooks that sell an identity.
- **Inputs → outputs:** brand + product + URL (+ the aspirational tribe: high-performers, trendsetters, early adopters, insiders, rebels) → 3 concepts that tease, not tell.
- **Rules:**
  - DO name the status identity in the fill-in. The prompt lists "high-performers, trendsetters, early adopters, insiders, rebels". Pick one; don't let the model blend them.
  - DO "end with a tease, not a resolution". The landing page, PDP or next frame must then **close the loop**, or the click feels like bait.
  - DO use social cues (who's in the frame, setting, language) to signal the in-group. Don't just state it.
  - DON'T over-index on [Ideal self](../../../concepts/ideal-self.md). Module 4 warns that Ideal-self aspiration is the angle everyone over-uses ([angle rut](../../../concepts/angle-rut.md)). Rotate with Actual/Ought versions.
  - DON'T fake exclusivity ("only for the elite") if anyone can buy. Signal it through taste and knowledge instead.
- **See also:** [Status signaling](../../../concepts/heuristics/status-signaling.md) · [Open loop](../../../concepts/heuristics/open-loop.md) · [Aspirational identity](../../../concepts/heuristics/aspirational-identity.md) · [#8 Contrast + Aspirational Identity](08-contrast-and-aspirational-identity.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Status signaling](../../../concepts/heuristics/status-signaling.md) + [Open loop](../../../concepts/heuristics/open-loop.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "cool, aspirational, and incomplete in the best way possible" |
| **Funnel** *(derived)* | Top of funnel (curiosity click) into a page that closes the loop |
| **Best self** *(derived)* | [Ideal self](../../../concepts/ideal-self.md) (who I want to be seen as). Social-standard variants can hit the [Ought self](../../../concepts/ought-self.md) |
| **Zone** *(derived)* | Zone 2: high valence, high intensity (anticipation, pride) |
| **Formats named in the prompt** | Short-form video, story ad, native post, carousel |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 4–5). Only formatting is normalised.

```text
🎯 Objective:

Develop high-converting ad concepts that leverage the power of Status Signaling—people’s desire to be seen as successful, elite, informed, or “in the know”—and pair it with the magnetic force of an Open Loop—an unresolved idea or narrative that creates curiosity and drives engagement.

These ads should feel like an exclusive peek into a world only a select few understand… and the viewer is just one click away from joining them.

---

🧠 Psychology Behind This Prompt:

- Status Signaling is the act of broadcasting identity through behavior, language, aesthetics, or association. It’s how we subtly (or not so subtly) communicate where we belong in the social/aspirational hierarchy.
- Open Loops are incomplete thoughts or stories that provoke the brain’s need to resolve tension. Think cliffhangers, teaser lines, or insights that are *almost* fully revealed.

Together, these two tactics make the viewer think:

“People like me are already doing this… and I need to know what I’m missing.”

---

🛠️ Instructions:

1. Tap into a status-oriented identity your audience aspires to—e.g. high-performers, trendsetters, early adopters, insiders, rebels, etc.
2. Hint at something exclusive or transformational they could unlock—but don’t give the full answer right away. Keep them leaning forward.
3. Use visual, tonal, or social cues to make the ad feel like an invitation to a world that’s just out of reach.
4. End with a tease, not a resolution. The goal is to get the viewer to *click, watch, or scroll* to close the loop.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  A 1–2 sentence summary of the main message.
- Narrative Angle or Hook
  What story, device, or tension is being used to draw people in?
- Psychological Mechanism in Use
  How are you applying Status Signaling and Open Loop theory?
- Suggested Formats
  Where this idea thrives (e.g., short-form video, story ad, native post, carousel).

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each one should:

- Target an identity or tribe your audience aspires to
- Tease a transformation, benefit, or insight without fully revealing it
- Use social cues or language that make the ad feel exclusive
- Leave an unresolved curiosity gap that pulls the viewer deeper

Your concepts should feel cool, aspirational, and incomplete in the best way possible.
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
Status identity the audience aspires to: {{high_performers|trendsetters|early_adopters|insiders|rebels|other}}
What the "exclusive" thing really is (must be true): {{the_insight_or_benefit_being_teased}}
Where the loop gets closed: {{landing_page_section_or_video_payoff}}
Target self: {{ideal|ought|actual}} · Format needed: {{format}}
```

## Why the pairing works
- **Status signaling** "is the act of broadcasting identity through behavior, language, aesthetics, or association. It's how we subtly (or not so subtly) communicate where we belong in the social/aspirational hierarchy." (Prompt #2)
- **Open loops** "are incomplete thoughts or stories that provoke the brain's need to resolve tension. Think cliffhangers, teaser lines, or insights that are *almost* fully revealed." (Prompt #2)
- The intended thought: **"People like me are already doing this… and I need to know what I'm missing."** Status creates the *want* (belonging higher up). The open loop creates the *need to click* (unresolved tension).

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| The product carries identity value (premium, design-led, performance gear, "in-the-know" wellness) | The product is a commodity bought on price. Status claims ring hollow |
| You have a genuine insider insight or new method to tease | You have nothing behind the tease. An unclosed loop burns trust |
| The audience is social and comparison-driven | The brand is an Actual-self "comfort" brand. Use [#5](05-tribal-belonging-and-vulnerability.md) (tribe without hierarchy) |

## Expected output
3 concepts that each target an aspirational identity or tribe, tease a transformation or insight **without fully revealing it**, use exclusive-feeling social cues or language, and "leave an unresolved curiosity gap that pulls the viewer deeper." No example outputs appear in the course.

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| Insider peek | Desire to be "in the know" / ahead | Status signaling, open loop | Short-form video, native post | "People like me are already doing this… and I need to know what I'm missing." (target thought) | Prompt #2 |
| What the top tier does differently | Desire to rank higher in a hierarchy | Status signaling, [social proof](../../../concepts/heuristics/social-proof.md) (aspirational crowd) | Story ad, carousel that stops before the reveal | *Illustrative, not from course:* "Every runner who broke 3 hours this year changed one thing. (It's not their shoes.)" | Prompt #2 steps 1–2 |
| Invitation to a world just out of reach | Belonging upward | Status signaling, [tribal belonging](../../../concepts/heuristics/tribal-belonging.md) | Lifestyle UGC with insider vocabulary | — | Prompt #2 step 3 |

## UGC script skeleton *(derived guidance)*
1. **Hook:** the creator's setting and props signal the tribe. The line hints at a secret ("The thing every [tribe] I know switched to…").
2. **Status cues:** two or three quick, specific details only insiders would recognise.
3. **Loop:** "I'll show you what it is, but first…", then build anticipation without the answer.
4. **CTA:** "See what it is →". The landing page opens with the reveal.

## PDF vs Skool differences
None in wording. The PDF version is on pages 4–5 (the word "high-performers" is hyphen-wrapped across a line break in the PDF).

## Related
- Levers: [Status signaling](../../../concepts/heuristics/status-signaling.md) · [Open loop](../../../concepts/heuristics/open-loop.md) · related: [Curiosity gap](../../../concepts/heuristics/curiosity-gap.md), [Suspense](../../../concepts/heuristics/suspense.md)
- Similar prompts: [#8 Contrast + Aspirational Identity](08-contrast-and-aspirational-identity.md) · [#12 Micro-Story + Suspense](12-micro-story-and-suspense.md) · [#3 Curiosity + Reverse Psychology](03-curiosity-and-reverse-psychology.md)
- Self check: [Three selves diagnostic](../../../frameworks/three-selves-diagnostic.md)

## Sources
- Skool page: [2_Status_Signaling_+_Open_Loop….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/2_Status_Signaling_+_Open_Loop_The_Prompt_Library_·_Tet.md>)
- PDF pages 4–5: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
