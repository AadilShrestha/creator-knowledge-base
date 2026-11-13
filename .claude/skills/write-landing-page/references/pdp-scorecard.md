# PDP scorecard (100 points)

Combined reviewer rubric for product pages and landing pages. It merges:
- Tether Lab [landing-page scorecard](../../../../knowledge-base/wiki/rubrics/landing-page-scorecard.md) and [psychology audit](../../../../knowledge-base/wiki/frameworks/landing-page-psychology-audit.md) (congruence, cognitive load, message, CTA, ability, buy box)
- RMBC II [PDP build](../../../../knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/frameworks/pdp-build.md), [unique mechanism](../../../../knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/concepts/unique-mechanism.md), [claim audit](../../../../knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/rubrics/llm-output-claim-audit.md), [compliance red flags](../../../../knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/concepts/compliance-red-flags.md)
- Evolve Copywriting [copy checklist scorecard](../../../../knowledge-base/wiki/courses/evolve/copywriting/rubrics/copy-checklist-scorecard.md) (three checks, show don't tell, objections, Big 4, gates G1–G6)
- Evolve Start Here [awareness levels](../../../../knowledge-base/wiki/courses/evolve/start-here/concepts/market-awareness-levels.md) and [sophistication levers](../../../../knowledge-base/wiki/courses/evolve/start-here/concepts/market-sophistication-levers.md)

Weights and bands are pipeline design, not course numbers. Quote the line behind every score.

## Auto-fails (check first; any one caps the total at 59)
| # | Fails if the page… | Basis |
|---|---|---|
| AF1 | States any review, rating, count, percentage, survey, testimonial, expert, endorsement, press logo or result that is not in the truth sheet. `[REAL: …]` slots with **no example value** pass. | Tether LP2, Evolve G3, RMBC claim audit |
| AF2 | Makes a disease, cure, treat, diagnose or drug-replacement claim, or says it is safe with medication / with everything, or omits the FDA disclaimer on a supplement | RMBC compliance red flags, Tether LP4 |
| AF3 | Gives unsafe advice (push through reactions, ignore symptoms, dose beyond label) | Evolve G4 |
| AF4 | Uses fake scarcity or deadlines (sold-out batches, stock bars, timers not tied to real stock) | Tether LP3, Evolve G4 |
| AF5 | Contradicts the label or the policies (doses, ingredients, guarantee terms, shipping time, support email) | Tether LP1, Evolve G1 |
| AF6 | Overstates a study (cause from correlation, hides size/design, claims a result the study did not find) | Evolve G1–G2, RMBC claim audit |

## Sections (score 0–3; points = weight × score ÷ 3)

| # | Section | Wt | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|
| S1 | Job + awareness fit | 8 | Length/job ignore the traffic | Right length, wrong level (e.g. pitches product to someone who doesn't believe the cause yet) | Level matched; minor jumps | Page does exactly the remaining selling for its traffic and level; new-mechanism play for a saturated market (Start Here sophistication) |
| S2 | Hero | 15 | Generic or brand-centred; mechanism absent | One message but generic; mechanism buried | Specific "you" message + mechanism visible; one weak element (bullets, proof strip, CTA) | A skimmer gets who it's for, the mechanism and the reason to believe in 5 seconds on mobile; 3–5 bullets ≤2 lines; true proof strip; CTA echoes the offer; would stop a parent who has seen 20 rival pages |
| S3 | Mechanism (UMP → UMS) | 14 | None, or category language ("natural focus support") | Named not explained | Explains why past fixes failed and how this works; tied to label | Ownable (renamed, nobody else can say it), true to the label doses, checkable by the reader, believable to a skeptic who researches |
| S4 | Scenes + customer language | 10 | Benefit lists | Some concrete lines | Key pains shown as specific moments | Scenes a parent recognises instantly, in their words; emotion specific (guilt, dread, relief); future pacing describes days, not promised results |
| S5 | Copy craft | 10 | Written-sounding, fluffy, repetitive | Mixed | Mostly spoken, grade ≤7, few cuttable lines | Passes visual / falsifiable / nobody-else checks on key lines; grade ≤6 body; nothing to cut; no section repeats another; hedges used once, not everywhere |
| S6 | Objections + ability | 10 | Not addressed | Generic FAQ | Main objections answered with a "because" | The top crusher for this market ("I've tried everything", "is it safe for my kid", "will they take it", "with meds?") is answered where the doubt appears, in 4–5 words or visually, then in the FAQ |
| S7 | Proof architecture | 10 | Proof is absent, or depends on slots | Some true proof | True-today proof leads; slots placed and worded | Page is persuasive with every slot empty: label transparency, doses, COA/certificate slots, honest research with limits, guarantee, founder slot; slots sit where proof is needed and are worded so a real value drops in |
| S8 | Offer + buy box | 13 | Price only, hard maths, no tiers | Some rules met | Tiers + $ savings + guarantee | Per-day / per-dose price vs what they spend now (RMBC price justification); easy-math tiers; true best-seller frame slot; guarantee in policy words as risk reversal; a true reason to act today (not fake urgency) |
| S9 | CTA + flow + load | 10 | "Shop"/"Add to cart", one button at the bottom, wall of text | Action verbs, late buy points | Buy points after conviction; mostly scannable | Offer-echo button labels, buy point after each conviction section, sticky mobile bar, short paragraphs, icons/numbers, logical order (problem → cause → mechanism → proof → offer → objections) |

**Total = sum of points.** Bands: **≥ 90 ship** · 80–89 fix the lowest two sections · < 80 rewrite weakest half · any auto-fail = block.

## Reviewer output (YAML)
```yaml
pdp_review:
  draft: X
  auto_fail: {checked: [AF1, AF2, AF3, AF4, AF5, AF6], triggered: [], evidence: []}
  sections:
    - {id: S1, wt: 8,  score: , points: , evidence: "<quote>"}
    - {id: S2, wt: 15, score: , points: , evidence: }
    - {id: S3, wt: 14, score: , points: , evidence: }
    - {id: S4, wt: 10, score: , points: , evidence: }
    - {id: S5, wt: 10, score: , points: , evidence: }
    - {id: S6, wt: 10, score: , points: , evidence: }
    - {id: S7, wt: 10, score: , points: , evidence: }
    - {id: S8, wt: 13, score: , points: , evidence: }
    - {id: S9, wt: 10, score: , points: , evidence: }
  total: 
  band: ship | fix | rewrite | block
  fixes: ["<section: exact change, with the line to replace>", "..."]
  steal_from_others: ["<draft: line or section worth folding in>"]
```

## Reviewer rules
- Score what is on the page, not what the notes promise.
- A 3 means "I could not improve this section much"; don't give 3s by default.
- Evidence for every score is a quote or a named section.
- List fixes as exact edits (line to replace → replacement), most points first.
