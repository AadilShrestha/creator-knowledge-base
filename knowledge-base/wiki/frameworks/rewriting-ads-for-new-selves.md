---
title: "Rewriting Winning Ads for New Selves (self-shift remix)"
type: framework
course: tether-lab
module: 04-self-targeting-system
sources:
  - raw/tether-lab/_transcripts/4. The Self Targeting System/7. How to Rewrite Winning Ads For New Selves .txt
  - raw/tether-lab/_transcripts/4. The Self Targeting System/4. The 3 Selves That Drive Every Buying Decision.txt
  - raw/tether-lab/_extracted/4. The Self Targeting System/11. 3-Selves Course - Prompts.md
  - raw/tether-lab/_extracted/4. The Self Targeting System/10. eBook Which ‘You’ Are You Selling To (2).md
tags: [framework, rewriting, remix, angles, three-selves, ugc, competitor-research, iteration]
updated: 2026-10-20
---

# Rewriting Winning Ads for New Selves
> Take an ad that's already working (ours, or a competitor's proven mechanism) and **re-target it to the self it doesn't speak to**. Keep the offer, product truth and visual frame, and change the promise, proof and wording. One winner becomes three angle variants.

## 🤖 Agent use
- **Use when:** you've found a winning ad (competitor library or our account) and need *new* angle variants for our product: the "take what's working and make it our own" step. Runs after the [Three selves diagnostic](three-selves-diagnostic.md) and before [Testing ads by self type](testing-ads-by-self-type.md).
- **Inputs → outputs:** one winning ad (copy + visual description or transcript) + its self scores + our product facts and verified proof → two (or three) self-shifted variants as static copy blocks (headline, subhead, social proof, bullets/badge) **or** UGC scripts + creator brief notes, each labelled with its self.
- **Rules:**
  - DO start from a proven winner, never a blank page [L7 00:18].
  - DO keep the **offer, CTA, landing page, price and bundle/discount identical** across variants [L7 00:38].
  - DO keep the **visual frame / layout** as close as possible. Only the self-messaging should differ ([L8 01:35](../courses/tether-lab/04-self-targeting-system/08-how-to-test-your-ads-by-self-type.md)).
  - DO change: the **promise** (what life looks like), the **verb** (become / already / should), the **proof type**, and the **identity callout**.
  - DO let the core message shift per self, UNLESS it's a long-proven brand line. Then keep it verbatim and re-self only the supporting copy [L7 02:41–03:06].
  - DO use only our own **verified** claims and proof. DON'T copy the competitor's claims, press logos, reviews or visuals. Remix the mechanism.
  - DON'T ship LLM-invented proof (e.g. "Featured in Outside and Men's Health" in the L7 output). Replace it with real proof.
  - DO lightly fix Ought copy: pressure must resolve into relief and reassurance [L4 05:36].
- **See also:** [Prompt 3 (verbatim)](../resources/three-selves-prompts.md#prompt-3-rewrite-one-ad-for-all-three-selves) · [3 selves](../concepts/three-selves.md) · [Testing ads by self type](testing-ads-by-self-type.md)

## Inputs
| Input | Notes |
|---|---|
| Winning ad | Copy (headline, subhead, primary text, CTA), visual description, or video transcript |
| Its self scores | From the [diagnostic](three-selves-diagnostic.md). Identify the **primary self** |
| Our product facts | Features, outcomes, the offer (unchanged across variants) |
| Our verified proof | Review count and rating, press, expert endorsements, certifications, UGC quotes |
| Is the core message a proven brand line? | If yes, keep it fixed [L7 02:43] |
| Output type | Static concept (default) or ad/UGC script. For scripts, change the prompt output to "generate an ad script" [L7 02:18] |

## Procedure
1. **Identify the primary self** of the winner (diagnostic or Prompt 3 step 2).
2. **Extract the transferable mechanism** *(agent step for competitor ads)*: hook structure (e.g. contrast pun, "for X only", warning label), format (static/UGC/comparison), proof type, visual frame. Discard brand-specific assets and claims.
3. **Pick the two missing selves** as targets (or all three when remixing a competitor ad for our product).
4. **Apply the shift table** below for each target self.
5. **Write each variant** in the output structure: **Headline** 4–7 words, punchy and emotionally clear · **Subhead** 1–2 lines expanding the benefit and the self motivation · **Social proof** (optional) matched to the self · **Bullets or badge** (choose one) highlighting key features or benefits. *(Prompt 3 and e-book ch. 4.)*
6. **Keep constant**: offer, CTA, landing page, price, product shot or visual layout.
7. **Check**: core message rule, verified proof only, Ought copy resolves into relief.
8. **Hand off** the three labelled variants to the [testing framework](testing-ads-by-self-type.md) (one ad set).

## Shift table: what changes when you move to each self
| Element | → Actual Self | → Ideal Self | → Ought Self |
|---|---|---|---|
| Promise | "This fits who you already are" | "This is who you could become" | "This is how you meet the standard / avoid the risk" |
| Core verb / frame | already, know, for [identity] who…, made for you | become, unlock, step into, finally | should, don't risk, real [role]s…, don't let… |
| Identity callout | In-group, present ("For Wine Lovers Who Know") | Aspirational status ("For campfire legends only") | Role responsibility ("Real Adults Bring a Flask", parent, host) |
| Emotion | Comfort, pride | Hope, inspiration, thrill | Guilt/pressure → relief |
| Proof type | Peer reviews from people like them ("900+ 5-Star Reviews from real wine lovers") | Transformation, status, elevated product hero | Authority/press ("As seen in Vogue…"), expert approval ("Dermatologist-approved"), safety features |
| Bullets lean | Ease, fit, no compromise ("Designed for wine drinkers, not hikers") | Upgrade, elevation, future scene | Protection, security, preparedness ("Shatterproof & secure", "Makes you look like the prepared one") |
| Funnel fit (e-book) | Consideration / Conversion | Awareness / Consideration | Awareness / Conversion |
| Expected test signature (L8) | Lower CTR, higher AOV | High CTR, low AOV | Slow start, high LTV |

## Worked examples (course)

**Rewrites (before → after)**
| Before | After | What changed (verb / visual / promise / self / intensity) | Source |
|---|---|---|---|
| Ideal: "Spill The Tea, Not Your Wine." / "Elevated. Easy. Enjoy Wine Anywhere." | Ought: "Don't Risk the Bottle" / "Keep your wine safe, sealed, and temperature-controlled — like a responsible adult." / Bullets: Shatterproof & secure · Protects your wine from heat + light · Makes you look like the prepared one | Self → Ought. Verb "don't risk" (prevention). Promise = responsible adult. Proof → authority | [L7 02:02] |
| Same | Ought final design: "Don't Risk the Bottle… / Real Adults Bring a Flask" + "As seen in Vogue · Men's Journal · goop · Business Insider" | Same visual. Social-standard headline. Press bar | [L7 02:30] |
| Same | Actual: "For Wine Lovers Who Know" / "You already bring the good stuff — now bring the gear to match." / ★★★★★ 900+ 5-Star Reviews from real wine lovers / No spills. No glass. No compromise. · Keeps flavor intact — wherever you are · Designed for wine drinkers, not hikers | Self → Actual. Verb "already". In-group identity. Peer proof | [L7 02:02] |
| Ideal: "The skincare routine your future self deserves." | Actual: "Skin that feels like you again." / "A routine that fits your life, not the other way around" | Future-self promise → return to the true current self. Fit, not change | e-book p. 7 |
| Ideal: "The skincare routine your future self deserves." | Ought: "You know you should be doing this." / "Dermatologist-approved, zero guilt, full coverage." | "Should" frame. Expert authority. Guilt relieved ("zero guilt") | e-book p. 7 |
| (Cookware) | Ideal: "Cook Like the Future You" / "Cleaner cookware for the version of you who doesn't cut corners." / ★★★★★ 40,000+ happy kitchens / Non-toxic ceramic coating · Oprah-approved design · Calmer cooking, sleeker kitchen | Example output format for an Ideal version | Prompt 3 example |

![Three designed variants of the same flask ad: Ideal, Ought, Actual](../assets/tether-lab/04-self-targeting-system/07-three-versions-0230.jpg)
*The finished set: same visual and offer, three selves. The Ought version adds a press bar. The Actual version adds a peer-review strip.*

## Competitor-remix playbook (the "make it our own" workflow)
1. **Find** a competitor winner (long-running or heavily duplicated in the ad library).
2. **Diagnose** its self with the [rubric](three-selves-diagnostic.md#scoring-rubric-apply-per-ad). Typically Ideal.
3. **Extract the mechanism** (hook pattern, format, proof type, visual frame). Example: the "Spill The Tea, Not Your Wine" mechanism is a *contrast pun* + product hero + wine splash.
4. **Keep the mechanism, change the self.** Build our version in the competitor's *uncontested* selves (e.g. Actual and Ought), using our product facts and verified proof.
5. **Optionally build our own Ideal version** too, so all three selves get tested on our offer.
6. **Brief and test** in one ad set ([testing](testing-ads-by-self-type.md)).

> (Agent adaptation, not verbatim from course:) The course demonstrates steps 2, 4 and 6 on the brand's *own* winner. Applying them to a competitor's mechanism is the same procedure with a step 3 extraction added. Always use our own claims and visuals.

## UGC script skeletons per self *(agent adaptation built from course language; the course shows statics only)*
| Beat | Actual | Ideal | Ought |
|---|---|---|---|
| Hook (0–3 s) | Creator names the identity they already hold: "If you're the one who always brings the [X]…" | Creator voices the aspiration: "I wanted to be the kind of person who…" / "For [legends] only." | Creator voices the should: "I knew I should've been [doing X]…" / "Real adults don't risk [Y]." |
| Body | Product fits the current routine with no change; "exactly what I needed" | Before → after, the future scene, the elevated product | The standard, the risk, how the product meets it; protection features |
| Proof | "900+ reviews from people like me" | Status or transformation proof | Authority, press, expert, safety |
| Close | "It just fits. You already…" | "Step into…" | Relief: "Now I don't have to worry about…" |
| Offer / CTA | **Identical across all three** | **Identical** | **Identical** |

## Output format
```markdown
### Self-shift variants: <source ad> → <our product>
**Source primary self:** Ideal (scores A/I/O = 2/8/1)
**Mechanism kept:** <hook pattern, format, visual frame>
**Constant across variants:** offer <…>, CTA <…>, LP <…>, price <…>

#### Variant A: Actual Self
- Headline (4–7 words):
- Subhead (1–2 lines):
- Social proof (verified):
- Bullets OR badge:
- [UGC script beats if requested]

#### Variant B: Ought Self
…
#### Variant C: Ideal Self (our version, optional)
…
**Expected signatures:** A = lower CTR / higher AOV · B = slow start / high LTV · C = high CTR / low AOV
```

## Common mistakes
- Changing the CTA, discount or bundle along with the self [L7 00:45].
- Re-selfing a proven core brand message [L7 02:43].
- Designing the variants differently, which confounds the test [L8 01:35].
- Keeping model-invented proof.
- Ought copy that only guilts. Add relief.

## Where it's taught
- [L7 How to Rewrite Winning Ads for New Selves](../courses/tether-lab/04-self-targeting-system/07-how-to-rewrite-winning-ads-for-new-selves.md) [00:00–04:15]
- [L6](../courses/tether-lab/04-self-targeting-system/06-how-to-use-the-prompts-for-instant-insights.md) [02:35] (Prompt 3 intro) · [L4](../courses/tether-lab/04-self-targeting-system/04-the-3-selves-that-drive-every-buying-decision.md) [07:05] ("reposition the message")
- E-book chapters 4–5: [Which 'You' Are You Selling To?](../resources/which-you-are-you-selling-to-ebook.md)

## Related
[Three selves diagnostic](three-selves-diagnostic.md) · [Testing ads by self type](testing-ads-by-self-type.md) · [Three selves prompts](../resources/three-selves-prompts.md) · [3 selves](../concepts/three-selves.md) · [Valence–intensity diagnostic](valence-intensity-diagnostic.md) (dial the emotion of each variant) · [CreativeOS](../tools/creativeos.md) (static templates for fast production)
