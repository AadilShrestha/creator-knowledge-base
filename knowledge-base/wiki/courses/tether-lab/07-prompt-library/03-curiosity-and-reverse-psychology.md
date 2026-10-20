---
title: "3. Curiosity + Reverse Psychology"
type: prompt
course: tether-lab
module: 07-prompt-library
order: 3
sources:
  - raw/tether-lab/7. The Prompt Library/3_Curiosity_+_Reverse_Psychology_The_Prompt_Library_·_T.html
  - raw/tether-lab/_extracted/7. The Prompt Library/3_Curiosity_+_Reverse_Psychology_The_Prompt_Library_·_T.md
  - raw/tether-lab/_extracted/6. The Ad Lab Toolkit/4. Prompt Library - Tether Lab.md
  - raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt
tags: [prompt, prompt-library, curiosity, reverse-psychology, hooks, tofu, sarcasm, ad-concepts]
updated: 2026-10-20
---

# 3. Curiosity + Reverse Psychology
> Generates 3 ad concepts that open on a "Wait, what?" contradiction, tell the viewer to keep doing the wrong thing ("Go ahead, keep doing what you're doing…"), then land a smarter insight. It's the prompt Sarah demos in the [tutorial video](README.md#video-tutorial-how-to-use-the-prompt-library), so it's the only one with real example output.

## 🤖 Agent use
- **Use when:** you need scroll-stopping, slightly provocative TOFU hooks that also **qualify** the viewer, or a competitor winner uses sarcasm / "don't buy this" / "keep doing X if you want Y" copy and you want to remix that mechanism.
- **Inputs → outputs:** brand + product + URL (+ the habit or belief the audience holds) → 3 concepts (big idea, narrative hook, psychology note, suggested formats), ready to turn into UGC scripts, carousels or statics.
- **Rules:**
  - DO paste the whole prompt, then add the brand at the very bottom. The prompt has no brand line of its own ([01:01]–[01:58]).
  - DO check the "Psychological Mechanism in Use" line in each concept. It's there so you can confirm the model really used *both* levers ([02:02]–[02:36]).
  - DO aim the sarcasm at the *habit*, never at the viewer's body or identity. The joke is "keep skipping breakfast", not "you look old".
  - DO follow up in the same chat: "second round", "Let's do headlines" ([04:04]).
  - DON'T use it where the "wrong" behaviour is dangerous or the claim can't be backed (health outcomes, guaranteed results). Reverse psychology implies a consequence, and that consequence is a claim.
  - DON'T resolve the tension in the hook. The contradiction has to hang for a beat before the insight.
- **See also:** [Curiosity gap](../../../concepts/heuristics/curiosity-gap.md) · [Reverse psychology](../../../concepts/heuristics/reverse-psychology.md) · [#6 Pattern Disruption + Hidden Truth](06-pattern-disruption-and-hidden-truth.md) · [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md) · [Prompt Library hub](README.md)

## At a glance

| | |
|---|---|
| **Levers** | [Curiosity gap](../../../concepts/heuristics/curiosity-gap.md) + [Reverse psychology](../../../concepts/heuristics/reverse-psychology.md) |
| **Output** | 3 ad concepts: Big Idea / Premise, Narrative Angle or Hook, Psychological Mechanism in Use, Suggested Formats |
| **Tone (per prompt)** | "bold, slightly provocative, and intellectually fun to interact with" |
| **Funnel** | Top of funnel. Sarah: reverse psychology "really does qualify the customer at the top of the funnel" [03:03] |
| **Best self** *(derived)* | [Ought self](../../../concepts/ought-self.md) ("you know you should…") and [Actual self](../../../concepts/actual-self.md) ("I feel attacked… this is so me" [03:03]) |
| **Zone** *(derived)* | Opens in Zone 4 / Zone 3 (low valence: the cost of the bad habit), resolves toward Zone 1/2. See [emotional zones](../../../concepts/emotional-zones.md) |
| **Formats Sarah's output suggested** | Quick-cut video, static carousel, UGC, story ads with sarcasm [02:36]–[03:30] |

## The prompt (verbatim)
Copied from the Skool lesson page. Wording is identical in the PDF (file pages 6–7). Only formatting is normalised (bold markers removed, line breaks kept).

```text
🎯 Objective:

Create high-converting ad concepts that pull people in through an irresistible sense of *“Wait, what?”* curiosity—then flip expectations using Reverse Psychology to challenge the viewer’s instincts, behaviors, or assumptions.

These ads should feel like a contradiction that *has to be resolved*. They trigger a reader’s need to know *why the opposite of what they believe might be true*—then hit them with a smarter (and often more subversive) insight.

---

🧠 Psychology Behind This Prompt:

- Curiosity is triggered when there's an *information gap*—something we *almost* understand but need closure to resolve. This creates a cognitive itch that must be scratched.
- Reverse Psychology works by encouraging someone to do (or believe) the opposite of what you actually want them to do—creating mental resistance, which paradoxically draws them closer to your point.

When paired together, these tactics create ad concepts that challenge people’s certainty, spark debate, and invite clicks through mental friction.

---

🛠️ Instructions:

1. Start with a statement or visual that contradicts what the audience believes.
 Think: bold, confusing, or intentionally “wrong-sounding” statements that prompt, *“That can’t be right…”*
2. Use Reverse Psychology to push against what they think they want.
 Frame your message as, *“Go ahead, keep doing what you’re doing…”*—then reveal why that path is broken.
3. Leave a moment of confusion or a gap in logic.
 Your goal is to have the viewer internally protest the idea, which builds tension that can only be resolved by engaging deeper.
4. Finally, land on an insight that reorients their thinking.
 Offer a solution that feels clever, contrarian, or surprisingly logical.

---

✍️ Format for Each Concept:

Each ad concept should include:

- Big Idea / Premise
  A 1–2 sentence summary of the central message.
- Narrative Angle or Hook
  What moment, contradiction, or social behavior are you spotlighting?
- Psychological Mechanism in Use
  How Curiosity + Reverse Psychology are applied.
- Suggested Formats
  Types of ads or platforms where this idea could work best (Reels, carousel, UGC, etc.).

---

✅ Output Instructions:

Generate 3 ad concepts using this framework. Each concept should:

- Start with a hook or situation that triggers curiosity
- Use reverse psychology to challenge beliefs or behavior
- End with a surprising or counterintuitive insight
- Include idea, narrative angle, psychology notes, and ideal format

These concepts should feel bold, slightly provocative, and intellectually fun to interact with.
```

### Fill-in block (append at the very bottom)
Sarah: "Just make sure that you put your brand at the bottom of here. You can put your brand, my website, my landing page, my product, whatever you'd like… at the very, very bottom. So it knows what it's supposed to be generating for." [01:01]–[01:58]

```text
Brand: {{brand_name}}
Product: {{product_name}} ({{one_line_description}})
Website / landing page: {{url_or_pasted_page_copy}}
```

Optional agent context *(wiki addition, not part of Sarah's prompt)*:

```text
Audience: {{audience_description}}
The habit or belief they hold that our product contradicts: {{current_habit_or_belief}}
Target self: {{actual|ideal|ought}} · Target zone: {{zone}}
Format needed: {{ugc_video_30s|static|carousel}}
Claims we can make (do not invent others): {{approved_claims}}
Competitor mechanism to remix (mechanism only, not the asset): {{competitor_teardown_summary}}
```

## Why the pairing works
- **Curiosity** = an *information gap*, "something we *almost* understand but need closure to resolve… a cognitive itch that must be scratched." (Prompt #3)
- **Reverse psychology** = "encouraging someone to do (or believe) the opposite of what you actually want them to do—creating mental resistance, which paradoxically draws them closer to your point." (Prompt #3)
- Together: the hook says something "wrong-sounding" ("That can't be right…"). The viewer "internally protest[s]", and that tension "can only be resolved by engaging deeper". The payoff is an insight that "reorients their thinking."
- Sarah's own reaction to her demo output shows the mechanism working: "I might have to go buy some collagen now. I feel attacked… This is so me… I don't want to look older faster." [03:03]

## When to use / when not to

| Use it when | Avoid it when |
|---|---|
| The audience has a **default habit** your product replaces (skipping breakfast, ignoring collagen, using the old tool) | The "wrong" behaviour is genuinely harmful. Sarcasm about medical, safety or financial harm reads as mockery |
| You want TOFU hooks that **filter in** committed buyers ("calls in that type of person that's ready to make a long-term commitment" [03:30]–[04:04]) | The brand voice is elevated or luxury. Sarcasm clashes with it |
| Competitor ads all say "you need X". Saying "go ahead, skip X" is a [pattern break](../../../concepts/heuristics/pattern-disruption.md) | You can't back the implied consequence ("brittle hair, slow metabolism") with approved claims |
| You need to pre-empt an objection ("supplements don't work overnight") by daring the viewer | The audience is already anxious (Zone 4 fatigue). Use [#5 Tribal Belonging + Vulnerability](05-tribal-belonging-and-vulnerability.md) or [#15](15-hindsight-bias-and-bounded-rationality.md) instead |

## Expected output
Per the tutorial [02:02]: a header like "Three bold curiosity-triggering ad concepts… 'Wait, what?'… plus reverse psychology framework" that names the framework (it "should match the exact prompt that you pulled out of the classroom"), then 3 concepts customised to the brand, each with **Big idea / premise → narrative angle or hook → psychological mechanism → resolution → suggested formats** (sometimes with sample carousel or UGC lines). The model then offers next steps ("Do you want a second round? Do you want to do headlines?") [04:04].

## Example outputs from the course (tutorial demo, supplement/collagen brand)
The brand Sarah typed is transcribed as "Avi" (Whisper; spelling uncertain). The outputs below are her ChatGPT 4o results read aloud. They're near-verbatim.

| Hook (verbatim or near) | Heuristic(s) | Emotion / zone | Self targeted | Why it works | Source |
|---|---|---|---|---|---|
| "Go ahead, keep skipping breakfast." | Reverse psychology + curiosity | Sarcastic warning, Zone 4→2 | Ought ("I know I should eat") | Dares the viewer to continue a habit they already feel guilty about. The premise lists the hidden cost: "Keep doing that if you want low energy, brittle hair, slow metabolism." | [02:02]–[02:36] |
| "Go ahead, skip breakfast, let your metabolism crawl, your glow could wait… Or fuel up in 30 seconds with this." | Reverse psychology → [transformation shortcut](../../../concepts/heuristics/transformation-shortcut.md) | Zone 4 → Zone 2 | Ought → Ideal | Static carousel: sarcastic setup, then an effortless fix ("faster… effortless") | [02:36]–[03:03] |
| "If you really want to age faster, do this." | Reverse psychology + curiosity | Mock advice, Zone 4 | Ideal (fear of losing youth) | Big idea: "your goal is to look older sooner. By all means, ignore collagen." Sarah: "I feel attacked… This is so me." | [03:03] |
| "Top three ways to look older: skip collagen, skip hydration, keep doing what you're doing." | Reverse psychology (list format) | Sarcasm, Zone 4 | Ought | Story ad "with sarcasm", a "great way to draw people in at the top of the funnel" | [03:03]–[03:30] |
| UGC line: "I stopped taking collagen because I missed dry hair, skin fall, and feeling 47…" (transcript garbled) | Reverse psychology, first-person UGC | Sarcastic testimonial | Actual | Creator "regrets" stopping, which implies the product works without claiming it outright | [03:03]–[03:30] |
| "The longer you wait, the more it won't work." | Reverse psychology + [loss aversion](../../../concepts/heuristics/loss-aversion.md) | Urgency, Zone 4 | Ought (commitment) | Calls out "supplements don't work overnight", so it qualifies buyers "ready to make a long-term commitment" | [03:30]–[04:04] |

## Angle template

| Angle | Core desire / pain | Heuristic(s) | Best format | Example line | Source |
|---|---|---|---|---|---|
| "Go ahead, keep doing X" (sarcastic dare) | Pain: the hidden cost of a habit they defend | Reverse psychology, curiosity gap | UGC talking head, sarcastic story ad, list carousel | "Go ahead, keep doing what you're doing…" | Prompt #3 instructions; demo [02:02] |
| "If you want [bad outcome], do this" | Fear of the bad outcome, framed as advice | Reverse psychology, loss aversion | Carousel ("Top 3 ways to…"), UGC | "If you really want to age faster, do this." | [03:03] |
| Dare the impatient buyer | Wanting instant results vs. a product that needs consistency | Reverse psychology, qualification | UGC confessional, static | "The longer you wait, the more it won't work." | [03:30] |

## UGC script skeleton *(derived guidance, not from the course)*
1. **Hook (0–3s):** creator deadpans the dare to camera. On-screen text repeats it. *("Go ahead. Keep skipping breakfast.")*
2. **Twist (3–8s):** list the consequences sarcastically, with quick cuts (yawning, dull hair, 3pm crash).
3. **Gap (8–12s):** "Or… you could do the thing nobody tells you about." Hold the reveal for a beat.
4. **Insight + product (12–25s):** the "surprisingly logical" fix, shown in use ("30 seconds").
5. **CTA:** keep the dare voice. *("Or keep skipping it. Your call.")*

## PDF vs Skool differences
None in wording. The PDF version is on file pages 6–7 (printed 5–6) and carries no prompt number (only page numbers). Its Psychology text was accidentally re-used on the Shock Factor page; see [#4](04-shock-factor-and-transformation-shortcut.md#pdf-vs-skool-differences).

## Related
- Levers: [Curiosity gap](../../../concepts/heuristics/curiosity-gap.md) · [Reverse psychology](../../../concepts/heuristics/reverse-psychology.md) · [Loss aversion](../../../concepts/heuristics/loss-aversion.md)
- Similar prompts: [#2 Status Signaling + Open Loop](02-status-signaling-and-open-loop.md) · [#6 Pattern Disruption + Hidden Truth](06-pattern-disruption-and-hidden-truth.md) · [#13 Counterintuitive Insight + Specificity](13-counterintuitive-insight-and-specificity.md)
- Tone check after generating: [Valence + Intensity prompts](../../../resources/valence-intensity-prompts.md) · Self check: [Three selves prompts](../../../resources/three-selves-prompts.md)

## Sources
- Skool page: [3_Curiosity_+_Reverse_Psychology….md](<../../../../raw/tether-lab/_extracted/7. The Prompt Library/3_Curiosity_+_Reverse_Psychology_The_Prompt_Library_·_T.md>)
- PDF pages 6–7: [Prompt Library PDF notes](../../../resources/prompt-library-pdf.md)
- Tutorial transcript: [4. The Prompt Library.txt](<../../../../raw/tether-lab/_transcripts/6. The Ad Lab Toolkit/4. The Prompt Library.txt>)
