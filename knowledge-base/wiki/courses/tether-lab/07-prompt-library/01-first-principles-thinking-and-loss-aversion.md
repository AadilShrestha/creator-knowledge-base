---
title: "1. First Principles Thinking + Loss Aversion"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 1
sources:
  - raw/tether-lab/7. The Prompt Library/1_First_Principles_Thinking_+_Loss_Aversion_The_Prompt_.html
  - raw/tether-lab/_extracted/7. The Prompt Library/1_First_Principles_Thinking_+_Loss_Aversion_The_Prompt_.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, first-principles, loss-aversion, category-reframe, mofu, ad-concepts]
updated: 2026-10-20
---

# 1. First Principles Thinking + Loss Aversion
> Generates 3 ad concepts that take apart a "best practice" the audience follows, rebuild the logic from the ground up, and show what clinging to the old way is **costing them right now**. The intended feeling is "bold, clarifying, and slightly uncomfortable—like the truth just clicked, and action is now urgent."

## 🤖 Agent use
- **Use when:** the category has an entrenched routine or "the way everyone does it" that our product replaces, and you need a switching argument. Also use it when a competitor's winner is a "you've been doing X wrong" ad and you want the mechanism, not the copy.
- **Inputs → outputs:** brand + product + URL + the conventional belief/process to attack (+ what it costs: money, time, results) → 3 concepts (big idea, narrative/metaphor, psychology note, formats). Each concept works across video, carousel, static and long-form copy.
- **Rules:**
  - DO name the specific conventional belief in the fill-in block. The prompt asks the model to choose one, and its default pick is often generic.
  - DO make the loss concrete and true (minutes, dollars, results). Loss aversion "is more powerful than gain-seeking", so it needs no exaggeration.
  - DO end on the reframed solution ("Of course—why didn't I see this before?"), not on the loss. A loss with no exit is just Zone 4 anxiety.
  - DON'T attack the customer for following the old way. Attack the *logic*. If you need to soften blame, pair with [#15](15-hindsight-bias-and-bounded-rationality.md) ("You weren't doing it wrong…").
  - DON'T claim competitor products "don't work" unless you can prove it.
- **See also:** [First principles thinking](../../../concepts/heuristics/first-principles-thinking.md) · [Loss aversion](../../../concepts/heuristics/loss-aversion.md) · [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md) · [Framing effect](../../../concepts/heuristics/framing-effect.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [First principles thinking](../../../concepts/heuristics/first-principles-thinking.md) + [Loss aversion](../../../concepts/heuristics/loss-aversion.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "fresh, friction-breaking, and urgent" |
| **Funnel** *(derived)* | Mid funnel: problem-aware people who already use the old way |
| **Best self** *(derived)* | [Ought self](../../../concepts/ought-self.md) (doing it *right*, not wasting money) and [Actual self](../../../concepts/actual-self.md) (rational, "makes sense to me") |
| **Zone** *(derived)* | Zone 4 (loss, urgency) resolving to Zone 1 (clarity, relief). See [emotional zones](../../../concepts/emotional-zones.md) |
| **Formats named in the prompt** | Video, carousel, static, long-form copy |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (pages 2–3). Only formatting is normalised (bold markers removed, line breaks kept).

```text
🎯 Objective:

Develop full ad concepts that challenge conventional wisdom using First Principles Thinking, while tapping into Loss Aversion to show what the audience is missing or wasting by sticking with the old way. These ads should feel *bold, clarifying, and slightly uncomfortable*—like the truth just clicked, and action is now urgent.

Each concept should include a compelling idea or narrative that can be applied across multiple ad types (video, carousel, static, long-form copy, etc.).

---

🧠 Psychology Behind This Prompt:

- First Principles Thinking strips away assumptions and rebuilds logic from the ground up. It’s about questioning “Why do we do this?” and reconstructing a better, truer answer.
- Loss Aversion triggers when people fear they’re wasting time, losing money, or falling behind. It’s more powerful than gain-seeking—and drives immediate decision-making.

Used together, this combo helps audiences realize they’ve been *operating on faulty logic*—and that it’s *costing them* something valuable right now.

---

🛠️ Instructions:

1. Choose a conventional belief, process, or “best practice” your audience follows today.
2. Deconstruct that belief using First Principles. Ask questions like:

   - “What is the actual goal behind this?”
   - “Is there proof this method even works?”
   - “What’s the simplest, truest way to get the result?”
3. Reveal what they’re losing by clinging to outdated thinking:

   - Money, time, growth, peace of mind, momentum, relevance, trust, etc.
4. Reframe the solution as clear, logical, and urgent. Make it feel like “Of course—why didn’t I see this before?”

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  A 1–2 sentence summary of the main message.
- Narrative Angle or Hook
  What’s the story, metaphor, or situation used to bring the message to life?
- Psychological Mechanism in Use
  A short note on how First Principles + Loss Aversion show up.
- Suggested Formats
  How this idea could play across video, static, carousel, etc.

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each concept should:

- Challenge a conventional assumption (First Principles)
- Emphasize what the audience is losing (Loss Aversion)
- Deliver a reframed, clarity-driven solution
- Include idea, narrative angle, psychology used, and format suggestions

Make it feel fresh, friction-breaking, and urgent.
```

### Fill-in block (append at the very bottom)
Sarah's instruction for every prompt: put "your brand, my website, my landing page, my product" at the very bottom so the model "knows what it's supposed to be generating for" ([tutorial](README.md#video-tutorial-how-to-use-the-prompt-library) [01:01]–[01:58]).

```text
Brand: {{brand_name}}
Product: {{product_name}} ({{one_line_description}})
Website / landing page: {{url_or_pasted_page_copy}}
```

Optional agent context *(wiki addition, not part of Sarah's prompt)*:

```text
Conventional belief / "best practice" to deconstruct: {{conventional_belief}}
What it costs them (true, specific): {{cost_in_time_money_results}}
Audience: {{audience_description}} · Target self: {{actual|ideal|ought}}
Format needed: {{ugc_video_30s|static|carousel|long_form}}
Claims we can make (do not invent others): {{approved_claims}}
```

## Why the pairing works
- **First principles thinking** "strips away assumptions and rebuilds logic from the ground up… questioning 'Why do we do this?' and reconstructing a better, truer answer." (Prompt #1)
- **Loss aversion** "triggers when people fear they're wasting time, losing money, or falling behind. It's more powerful than gain-seeking—and drives immediate decision-making." (Prompt #1)
- Together they make the audience "realize they've been *operating on faulty logic*—and that it's *costing them* something valuable right now." First principles supplies the *why* (a credible argument); loss aversion supplies the *now* (urgency).
- The three deconstruction questions in the prompt work as a research checklist: "What is the actual goal behind this?" · "Is there proof this method even works?" · "What's the simplest, truest way to get the result?"

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| A habitual routine or incumbent product dominates the category (multi-step routines, legacy tools, "everyone does it this way") | The product *is* the convention. You'd be arguing against yourself |
| The audience is rational and research-minded (supplements, skincare actives, B2B, home tools) | The purchase is impulsive or hedonic (fashion, treats). Logic is the wrong door; try [#8](08-contrast-and-aspirational-identity.md) or [#12](12-micro-story-and-suspense.md) |
| You can quantify the waste (time per day, cost per year, % that doesn't absorb…) | You can't prove the "old way" is worse. That turns it into an unprovable claim |

## Expected output
3 concepts, each with: a 1–2 sentence **big idea**, a **narrative angle** (story, metaphor or situation), a **psychology note** naming both levers, and **format suggestions** across video, static and carousel. The output instructions require each concept to challenge an assumption, emphasise the loss and deliver "a reframed, clarity-driven solution."

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| "Why do we even do it this way?" | Pain: wasting money/time on a routine that doesn't serve the goal | First principles, loss aversion | UGC talking head ("I asked one question…"), myth-vs-truth carousel | "What is the actual goal behind this?" | Prompt #1 instructions |
| Cost of the old way | Loss: money, time, growth, peace of mind, momentum, relevance, trust | Loss aversion, [framing](../../../concepts/heuristics/framing-effect.md) (cost per year/day) | Static with a big number, calculator-style carousel | *Illustrative, not from course:* "Your 7-step routine costs you 21 minutes a day. Here's the 1 step that does the job." | Prompt #1 step 3 |
| "Of course—why didn't I see this before?" | Relief: a simpler, truer path | First principles → [processing fluency](../../../concepts/heuristics/processing-fluency.md) | Before/after demo video | "Of course—why didn't I see this before?" | Prompt #1 step 4 |

No example outputs for this prompt appear in the course.

## UGC script skeleton *(derived guidance, not from the course)*
1. **Hook:** the creator questions the ritual on camera, holding the old product. ("Why do we all do [X]?")
2. **Deconstruct:** "The actual goal is [Y]. [X] doesn't even do that, because [reason]."
3. **Loss:** one specific, true cost (on-screen number).
4. **Rebuild:** our product as the simplest path to the real goal, demonstrated.
5. **CTA:** urgency through loss ("every week you wait is another [cost]").

## PDF vs Skool differences
None in wording. The PDF version is on pages 2–3 and is untitled except for the lever pair (no "1."). See [PDF notes](../../../resources/prompt-library-pdf.md).

## Related
- Levers: [First principles thinking](../../../concepts/heuristics/first-principles-thinking.md) · [Loss aversion](../../../concepts/heuristics/loss-aversion.md)
- Similar prompts: [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md) · [#7 What If Scenario + Pain Point Amplification](07-what-if-scenario-and-pain-point-amplification.md) · [#15 Hindsight Bias + Bounded Rationality](15-hindsight-bias-and-bounded-rationality.md)
- Tone check: [Valence + Intensity prompts](../../../resources/valence-intensity-prompts.md) (soften with the Zone 1 prompt if the result is too harsh)

## Sources
- Skool page: [1_First_Principles_Thinking_+_Loss_Aversion….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/1_First_Principles_Thinking_+_Loss_Aversion_The_Prompt_.md>)
- PDF pages 2–3: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Usage instructions: [tutorial transcript](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
