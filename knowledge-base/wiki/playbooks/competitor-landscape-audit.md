---
title: "Playbook: Competitor Landscape Audit (find emotional stagnation and white space)"
type: playbook
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md
  - knowledge-base/wiki/concepts/emotional-stagnation.md
  - knowledge-base/wiki/concepts/heuristics/von-restorff-effect.md
  - knowledge-base/wiki/frameworks/teep-journey.md
  - knowledge-base/wiki/frameworks/three-selves-diagnostic.md
  - knowledge-base/wiki/frameworks/customer-research-stack.md
tags: [playbook, competitor-research, landscape, emotional-stagnation, white-space, differentiation, von-restorff, zone-tally, self-tally, opportunity-list]
updated: 2026-10-20
---

# Playbook: Competitor Landscape Audit
> Tear down 10–30 competitor ads, tally their zones, selves, TEEP stages, heuristics, emotions, formats and looks, and find where the whole category is stuck (**emotional stagnation**) and what nobody is doing (**white space**). Then go the opposite way. Output: a **landscape matrix** and a scored **opportunity list** for [angle remix](angle-remix.md).

## 🤖 Agent use
- **Use when:** entering a new niche, before a new creative batch, or when our ads look like everyone else's.
- **Inputs → outputs:** 3–8 competitors × 3–10 ads each (10–30 total) as [teardown cards](competitor-ad-teardown.md) (full or "lite") → `landscape_matrix` (markdown tables) + `opportunity_list` (YAML).
- **Rules:**
  - DO tag every ad by zone; "every single one is like the same exact zone" was Sarah's AG1 finding across 15–20 ads [Jun11 0:07:22–0:08:23].
  - DO treat zones as attributes of **people**: a single-zone category leaves whole customer types unserved ("I have tried every supplement on the planet and all of them upset my stomach" = Zone 3) [Jun11 0:17:00–0:18:05].
  - DON'T copy what dominates. Find their core message, colour and tone, then go opposite: "If they go big you go small, if they're green you go red, if they're stupid wild and loud you go very soft and subtle" [Jun11 0:42:22–0:44:31] ([Von Restorff effect](../concepts/heuristics/von-restorff-effect.md)).
  - DO go negative only about the **industry**, positive about the viewer ("you're smart for noticing") [Jun11 0:20:12–0:21:13].
  - DON'T read "everyone does X" as "X works". You can't see their spend or profit [Jun11 0:41:18].
  - DO note the TEEP stages each brand ignores: "some of these brands are only running one specific level of the model" [Jun4 0:39:49].
- **See also:** [Competitor ad teardown](competitor-ad-teardown.md) · [Emotional stagnation](../concepts/emotional-stagnation.md) · [Angle rut](../concepts/angle-rut.md) · [Customer research stack](../frameworks/customer-research-stack.md) (step 8, competitor pass) · [Brands hub](../brands/README.md) · [Colour psychology](../concepts/color-psychology.md)

**Source key:** Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jun18 = [Live Jun 18](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md). **(pipeline design)** = our process.

## Procedure

### Step 1: Define the set (pipeline design)
- Category keyword + 3–8 competitors: the category leader, 2–3 fast-growing DTC challengers, 1–2 adjacent-category brands our buyer also sees.
- Per competitor, sample 3–10 ads. Priority: (a) high winner-signal ads, (b) most variants, (c) newest launches (their current bet). Include videos (transcribe them) — Sarah's AG1 sample included videos [Jun11 0:07:22].

### Step 2: Lite teardown each ad
Full [teardown cards](competitor-ad-teardown.md) for the top 3–5 ads; for the rest, a **lite card** with only the tally fields:

```yaml
lite_card: {id: TD-<brand>-<nn>, brand: "", format: "", hook: "<first line / headline>", core_message: "<their repeated word/idea>",
  zone: Z1|Z2|Z3|Z4, self: actual|ideal|ought|mixed, teep: T|E1|E2|P, mindstate: "", specific_emotion: "",
  heuristics: [<slugs>], messenger: "", palette: "<dominant colours>", tone: loud|neutral|soft, scale: big|small,
  proof_type: "", offer: "", winner_confidence: high|medium|low}
```
Competitor-library prompt (as said by Sarah): *"Tell me which emotions are in here, how intense they are, which selves they're currently targeting, and… what the core message is."* [Jun11 0:41:18–0:42:22]. Attach the ads; ask for a table; verify each row yourself.

### Step 3: Build the landscape matrix
Fill these tables (counts; use high-confidence ads ×2 weight if you want a weighted view — pipeline design).

**A. Zone × self grid** (the core white-space map)
| | Actual | Ideal | Ought |
|---|---|---|---|
| Z1 feel-good | n | n | n |
| Z2 hype | n | n | n |
| Z3 pain whisper | n | n | n |
| Z4 danger | n | n | n |

**B. TEEP coverage per brand**
| Brand | T | E1 | E2 | P | Missing |
|---|---|---|---|---|---|

**C. Heuristic frequency** (across all ads; flag the "very expected in DTC" trio: scarcity, social proof, authority — [heuristics hub](../concepts/heuristics.md))
| Heuristic | Count | Brands using it |
|---|---|---|

**D. Emotion map**: mindstate → specific sub-emotion → count. Generic labels ("confidence") count as a gap in specificity ([emotion specificity](../concepts/emotion-specificity.md)).

**E. Format and messenger**: format × count; messenger (peer, expert, founder, skeptic, character, none) × count.

**F. Look and language**: dominant palette, tone (loud/soft), scale claims (big/vague vs small/specific), repeated core words (AG1: "activate") [Jun11 0:42:22].

### Step 4: Detect stagnation and ruts
| Pattern | Threshold (agent heuristic) | Reading |
|---|---|---|
| One zone holds ≥80% of a brand's ads | ≥80% ([Jun 11 page](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md#rules-of-thumb) wiki threshold; Sarah said "every single one") | That brand is emotionally stagnant |
| One zone holds ≥60% of the **category** | ≥60% (pipeline design) | Category-level stagnation: empty zones are open |
| One self scores highest in ≥70% of ads | ≥70% ([three-selves decision table](../frameworks/three-selves-diagnostic.md#decision-table-what-to-do-with-the-result)) | Angle rut; the other selves are uncontested |
| A TEEP stage has 0–1 ads category-wide | — | Stage gap (often E1 exploration or E2 evaluation; most brands run only T and P [May 21 via TEEP page]) |
| Same 2–3 heuristics everywhere | — | Use the less obvious ones (affect, framing, goal gradient, Von Restorff, IKEA…) |
| Everyone's palette/tone is alike | — | A colour/tone flip is a cheap salience win |

### Step 5: Write the "opposite" column
For each dominant pattern, write its opposite (Sarah's examples [Jun11 0:43:27–0:44:31]):

| They do | Opposite to test | Example from the course |
|---|---|---|
| Big, vague promise | Small, specific, "medicalized" | "activate your health" → "boost your mitochondria" |
| Pinks, pastels, greys | Black and green / saturated | — |
| Loud and wild | Soft and subtle | — |
| All Zone 1 calm | Z2 / Z3 / Z4 (handled with care) | AG1 all Z1 → "tried every supplement, all upset my stomach" |
| Plastic-bottle sameness | Look like nothing else in the category | Liquid Death skulls and crossbones [Jun11 0:45:32] |
| Only video | Statics, GIFs (cheaper CPMs in Faraz's account: ~$30–40 vs ~$160) | [Jun11 0:52:52–0:54:59] |

### Step 6: Filter by truth and ethics
Drop any opportunity that (a) needs a claim our [product truth sheet](README.md#hand-off-artifacts) can't support, (b) would shame the viewer's self (Z3/Z4 must target situations or industry beliefs, and end with hope [Jun4 0:28:12–0:30:17]), (c) is just a competitor's distinctive asset in reverse.

### Step 7: Score the opportunities (pipeline design)
| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Gap size | crowded | some use | rare | nobody |
| Customer evidence (reviews, Reddit, CIM) | none | anecdotal | several quotes | repeated + intense |
| Product fit / proof available | none | weak | adequate | strong, demonstrable |
| Distinctiveness (Von Restorff) | looks like the category | slightly | clearly | the "one thing that differs" |
| Cost to test | needs pro video | UGC | static batch | headline swap |

Score = sum (0–15). Hand ≥10 to [angle remix](angle-remix.md); 7–9 = backlog; ≤6 = drop.

## Output
```markdown
### Landscape audit: <category> (<date>)
Sample: <n> ads from <brands>; high-confidence ads: <n>
**A. Zone × self grid** (table) · **B. TEEP coverage** (table) · **C. Heuristics** (table) · **D. Emotions** · **E. Formats/messengers** · **F. Look & language**
**Stagnation findings:** <brand>: <n>/<N> ads in Z1 → stagnant · category: <zone> <pct>% · self rut: <self> <pct>%
**Uncontested:** zones <…> · selves <…> · stages <…> · heuristics <…> · formats <…> · palette/tone <…>
```
```yaml
opportunity_list:
  - id: OPP-<nn>
    gap: "<e.g. Z3 × Actual: nobody shows the stomach-upset history>"
    opposite_of: "<dominant pattern>"
    evidence: ["<review/Reddit quote or tally>"]
    fit: "<which true product fact makes it honest>"
    proof_available: "<demo | reviews | test results | none>"
    suggested_teep: T | E1 | E2 | P
    suggested_zone: Z1 | Z2 | Z3 | Z4
    suggested_self: actual | ideal | ought
    source_mechanisms: [TD-<…>]     # teardown cards whose mechanism could carry it
    score: {gap: 0-3, evidence: 0-3, fit: 0-3, distinct: 0-3, cost: 0-3, total: 0-15}
    next: angle-remix | backlog | drop
```

## Worked mini-example: greens powder category (from Jun 11)
- Sample: 15–20 AG1 ads incl. videos (Sarah) [Jun11 0:07:22]. Three shown: "The best just got BETTER." (self before/after), "Get your $76 Free Welcome Kit Now" (UGC-style offer), "AG1 is #1 for a Reason" (comparison chart). All **Z1** (high valence, low intensity) per her GPT [0:04:30–0:07:56]. Case file: [AG1](../brands/ag1.md).
- Stagnation: 100% Z1 → stagnant; new formats didn't create new emotions [Jun11 0:05:19–0:08:23].
- Opportunities Sarah named: Z3 "tried every supplement… they all upset my stomach" [0:18:05]; industry call-out + "you're a smart shopper for noticing" [0:20:12]; honest taste admission ("it dissipates quicker than everybody else") [0:25:35]; small, medical language vs "activate" [0:43:27]. The chart's own objection list ("hidden ingredients", "poor absorption") becomes negative-zone hooks (wiki fix on the session page).

## Quality gates
- [ ] ≥10 ads, ≥3 brands, videos transcribed.
- [ ] Every count traces back to a card ID.
- [ ] Each opportunity has customer evidence or is marked `evidence: none` (and then scores 0 there).
- [ ] No opportunity relies on a competitor's claim, character or look.
- [ ] Z3/Z4 opportunities target a situation or industry belief, never the viewer's self-worth.

## Related
[Playbooks hub](README.md) · [Competitor ad teardown](competitor-ad-teardown.md) · [Angle remix](angle-remix.md) · [Customer research → angles](customer-research-to-angles.md) · [Emotional zones](../concepts/emotional-zones.md) · [Emotional stagnation](../concepts/emotional-stagnation.md) · [Brand enemy](../concepts/brand-enemy.md) · [Category perception](../concepts/category-perception.md) · [TEEP](../frameworks/teep-journey.md) · [Angles library](../libraries/angles.md)
