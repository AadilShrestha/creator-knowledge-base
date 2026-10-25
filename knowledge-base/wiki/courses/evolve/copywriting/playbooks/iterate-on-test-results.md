---
title: "Playbook: iterate on test results (label → learn → diagnose → choose iterations → brief → track)"
type: playbook
creator: evolve
course: copywriting
instructor: "Spencer Pawliw"
sources:
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/45-overview-of-iteration-section.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/46-the-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/47-claude-code-10-step-iteration-process.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/48-how-to-iterate-on-losing-ads.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/49-how-to-iterate-on-kpi-winners.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/50-how-to-iterate-on-spend-winners.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/51-how-to-iterate-on-breakthroughs.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/52-the-iteration-playbook-script.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/53-the-iteration-playbook-formats-styles.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/54-iteration-examples-breakdowns-walkthrough.md
  - knowledge-base/wiki/courses/evolve/copywriting/lessons/70-how-to-write-video-ads-part-1.md
tags: [playbook, iteration, testing, outcome-labels, learnings, issue-codes, breakthroughs, spend-winners, losers, kpi-winners, naming, quality-gate]
updated: 2026-10-21
---

# Playbook: iterate on test results
> After a test window: label each ad (loser / KPI winner / spend winner / breakthrough) with spend numbers, run the ten-step learnings and the nine-component audit, diagnose with issue codes, pick iterations from the outcome's list (fix losers with evidence, fix spend winners' conversion gaps first, multiply breakthroughs), brief them through the script or static playbook, and name every iteration `ITER#N_BATCH#ORIG#` so the count and the learnings accumulate.

## 🤖 Agent use
- **Use when:** results are in for a batch; a breakthrough appears or starts dropping; a spend winner won't scale; someone asks "what do we make next?"
- **Inputs → outputs:** per ad: name (batch), screenshots per hook variation, ad spend and campaign spend over the same window, KPI target and actual, CTR/CPC/CVR/AOV, hook and hold rate (if spend is meaningful), the tracker row, comments, landing page → `learning_record` per ad + `iteration_plan` + updated Roadmap rows → briefs via [write a video ad script](write-a-video-ad-script.md) / [write static image ads](write-static-image-ads.md).
- **Rules:**
  - **DO** label the outcome before anything else; "the most crucial thing ... is you need to have a clear process on actually identifying what is the outcome of your ad." [L45 00:00–00:57](../lessons/45-overview-of-iteration-section.md)
  - **DO** wait 7 days, or start at 2–3 days only if the ad "starts scaling the entire account". [L46 02:05–03:31](../lessons/46-the-10-step-iteration-process.md)
  - **DON'T** iterate without learnings, and don't call the hypothesis a fact. [L48 04:59](../lessons/48-how-to-iterate-on-losing-ads.md); [L46 14:17–15:40](../lessons/46-the-10-step-iteration-process.md)
  - **DON'T** turn a breakthrough off after a few bad days ("your ads earn respect"). [L51 03:25–05:36](../lessons/51-how-to-iterate-on-breakthroughs.md)
  - **DON'T** change the format of a spend winner before fixing belief, urgency, stakes and funnel. [L50 17:18](../lessons/50-how-to-iterate-on-spend-winners.md)
  - **DO** judge by scale, not "some purchases" (a profitable ad with under 10% of spend was logged as Losing). [L70 00:53–01:47](../lessons/70-how-to-write-video-ads-part-1.md)
  - **DO** name and count every iteration; 30 iterations without another winner means "the iterations ... are not in depth and they're not with intent". [L46 18:54–21:22](../lessons/46-the-10-step-iteration-process.md)
  - **DO** keep every iteration truthful: new authority, facts, urgency or stakes must come from the product truth sheet. [L52 02:19](../lessons/52-the-iteration-playbook-script.md)
- **See also:** [Ten-step learnings](../frameworks/ten-step-iteration-learnings.md) · [Nine-component audit](../frameworks/nine-component-audit.md) · [Iteration issue codes](../frameworks/iteration-issue-codes.md) · [Iteration playbook](../frameworks/iteration-playbook.md) · [Iteration outcomes](../concepts/iteration-outcomes.md) · [Copy checklist scorecard](../rubrics/copy-checklist-scorecard.md)

## Steps
| # | Step | Do | Output | Consult |
|---|---|---|---|---|
| 1 | Collect | Per ad: batch, screenshots per hook variation, ad spend + campaign spend (same window), KPI, CTR/CPC/CVR/AOV, hook/hold rate, frequency, comments, LP | raw data | [L46 01:14–04:14](../lessons/46-the-10-step-iteration-process.md); [L47 00:58–05:12](../lessons/47-claude-code-10-step-iteration-process.md) |
| 2 | Label | Loser / KPI winner / spend winner / breakthrough; record the majority-of-spend threshold you assumed (10% for big accounts up to 60–70% for small) | `outcome` | [L45 01:29–02:24](../lessons/45-overview-of-iteration-section.md) |
| 3 | Learnings (steps 3–8) | Ad type; hooks verbatim (text + VO); rates only if ~$1k spend after 7 days; [nine-component audit](../frameworks/nine-component-audit.md) planned vs executed; hypothesis + 3 ideas; links; board card | `learning_record` | [ten-step learnings](../frameworks/ten-step-iteration-learnings.md) |
| 4 | Decide whether to iterate | Use the ad-type × outcome table | iterate / move on / leave running | [ten-step: ad-type table](../frameworks/ten-step-iteration-learnings.md#why-step-3-matters-ad-type-changes-the-decision) |
| 5 | Diagnose | Pick 1–3 [issue codes](../frameworks/iteration-issue-codes.md) with evidence using the triage table (hook rate < 30% → #1/#4; decent hook, no conversion → #5–#8; spend winner with fine CTR → #7, #9–#12; breakthrough dropping → lifespan risks) | `diagnosis` | [issue codes: triage](../frameworks/iteration-issue-codes.md#triage-decision-table-metric-pattern--codes-to-check-in-order) |
| 6 | Choose iterations | Losers/KPI winners: one fix per code. Spend winners: fix conversion in the same format first. Breakthroughs: components rewrite first, then script and format iterations, then cross-format statics | `iteration_plan` | [iteration playbook](../frameworks/iteration-playbook.md) |
| 7 | Write before → after | For each iteration, the exact changed line(s) with a "Changes Made" label (code + component) | change list | [L54 08:49](../lessons/54-iteration-examples-breakdowns-walkthrough.md); [rewrites library](../libraries/rewrites.md) |
| 8 | Brief | Send each iteration through the script or static playbook (they carry the truth QA and gates) | briefs | [write a video ad script](write-a-video-ad-script.md); [write static image ads](write-static-image-ads.md) |
| 9 | Off-ad fixes | Offer (#8) and funnel/landing page (#11) go to the offer/CRO owner, logged in the Page Roadmap / CRO tab | page tasks | [L48 18:22–19:00](../lessons/48-how-to-iterate-on-losing-ads.md); [L50 12:15–14:43](../lessons/50-how-to-iterate-on-spend-winners.md); [memo framework](../frameworks/mini-breakthrough-memo-and-growth-guide.md) |
| 10 | Name + track | `ITER#[N]_BATCH#[ORIG#]` at file, ad, ad-set level; update the Roadmap (RESULTS, LEARNINGS, Ad Variable, Test Result); append to the patterns log | named launch | [L46 18:54–21:22](../lessons/46-the-10-step-iteration-process.md) |
| 11 | Re-read the next window | When an iteration pops, promote the hypothesis to a learning; if it stays a spend winner, diagnose again | learning promoted | [L46 14:17–15:40](../lessons/46-the-10-step-iteration-process.md); [L50 05:23](../lessons/50-how-to-iterate-on-spend-winners.md) |

### Outcome decision table (what to do with each label)
| Outcome | First action | Iteration source | Don't | Source |
|---|---|---|---|---|
| Loser (ideation) | Learnings; up to 2–3 retries, each with new evidence | Codes #1–#8 | retry without new evidence | [L48 02:18–03:11](../lessons/48-how-to-iterate-on-losing-ads.md) |
| Loser (iteration of a winner) | Compare with the winning original | Codes; "you made the ad worse, or you didn't make it different enough" | stop after one failed iteration | [L48 03:11–04:00] |
| Loser (imitation) | Usually move on | — | iterate visual imitations by habit | [L48 04:00–04:59] |
| KPI winner at ~1% spend | Treat as a lucky loser | Codes #1–#8 | count it as a hit | [L49 00:00–00:39](../lessons/49-how-to-iterate-on-kpi-winners.md) |
| KPI winner, deliberate BOF/offer ad | Leave it running; maybe test formats | — | expect it to scale | [L49 00:39–03:56] |
| Spend winner, ROAS 0.2–0.3x | Check misleading (#12); likely turn off | — | wait for Meta to pull spend | [L50 00:35; 14:43](../lessons/50-how-to-iterate-on-spend-winners.md) |
| Spend winner near target | Fix #7 belief, #9 urgency, #10 stakes, #11 funnel in the same format | then script iterations | hold/format iteration mode | [L50 02:02–17:18] |
| Breakthrough | Keep it on through bad days; dissect; plan the next one | Components rewrite → script #2–#9 → formats → cross-format | spam hook/format iterations without dissection | [L51](../lessons/51-how-to-iterate-on-breakthroughs.md); [L52 19:07](../lessons/52-the-iteration-playbook-script.md) |

## Output: iteration round
```yaml
iteration_round:
  id: ITR-<yyyymmdd>-<batch>
  window: {start: YYYY-MM-DD, days: <n>}
  account_majority_threshold_assumed: "<%>"
  ads:
    - name: "<...>"
      outcome: loser | kpi_winner | spend_winner | breakthrough
      ad_type: ideation | imitation | iteration
      spend: {ad: <$>, campaign: <$>, share: "<%>"}
      metrics: {ctr: , cpc: , cvr: , aov: , roas: , hook_rate: , hold_rate: , trusted: <bool>}
      learning_record: "<link>"
      decision: iterate | move_on | leave_running | turn_off
      diagnosis: [{code: "#9 Urgency", evidence: "<quote>"}]
      iterations:
        - name: "ITER#<n>_BATCH#<orig>"
          type: "<e.g. L52 #3 Bridge remake | L53 #12 Founder delivery | DOCX #19 Static extraction>"
          changes_made: "<code + component>"
          before: "<line>"
          after: "<line>"
          keep_constant: ["<...>"]
          truth_refs: ["<...>"]
          brief_via: write-a-video-ad-script | write-static-image-ads | cro
  breakthrough_watch: [{ad: "<...>", weeks_at_scale: <n>, bad_days: <n>, lifespan_risks: ["easy_to_copy", "seasonal"], keep_on: true}]
  iteration_count_by_concept: {"<concept>": <n>}
  learnings_promoted: ["<hypothesis that popped>"]
```

## Quality gates
1. Every ad has an outcome label with spend numbers and the assumed threshold.
2. Every iteration traces to a learning record and names its issue code or iteration type.
3. Every changed line passes ⛔ G1–G6 of the [copy checklist scorecard](../rubrics/copy-checklist-scorecard.md) (the briefs then pass their own gates).
4. No breakthrough is paused on fewer than ~a week of bad performance after weeks at scale without a written reason [L51 04:52–05:36](../lessons/51-how-to-iterate-on-breakthroughs.md).
5. Iteration names carry `ITER#N_BATCH#ORIG#`.

## Combine with Tether Lab
| Shared page | Use it for | Evolve contributes | Tether contributes |
|---|---|---|---|
| [Test and iterate](../../../../playbooks/test-and-iterate.md) | Launch plan and read-outs | Outcome taxonomy (loser/KPI/spend/breakthrough), ad-type rules, issue codes, 9 script + 15 format + 22 DOCX iterations, naming/count tracking | One learning goal per campaign, batch sizes, read-outs by self/zone/TEEP, metric-pattern table, scaling increments |
| [Competitor ad teardown](../../../../playbooks/competitor-ad-teardown.md) | Breakdown of a competitor's "version 2" | Issue-code labels on what changed | Winner signals, transferable mechanism |
| [Angle remix](../../../../playbooks/angle-remix.md) | When iterations exhaust an angle | Memo for the new idea | Self/zone shifts the account lacks |
| [UGC script writing](../../../../playbooks/ugc-script-writing.md) · [Static ad creation](../../../../playbooks/static-ad-creation.md) | Executing iterations | Hook/bridge/hold modules; truth QA | Frameworks, layout, format ladder |
| [Creator brief](../../../../playbooks/creator-brief.md) | Creator iterations (DOCX #16, L53 #2) | 3-video creator brief | Casting, seed asset |
| [Ad scorecard](../../../../rubrics/ad-scorecard.md) · [UGC script checklist](../../../../rubrics/ugc-script-checklist.md) | Gate on each iteration | ⛔ truth gates | Psychology scoring |

**In one line:** Evolve = the iteration system (labels, learnings, codes, named iterations, counting); Tether = the psychology lenses for which emotional variable to move and the testing structure.

**Disagreements and agent defaults (logged in the contradiction notes):**
| Topic | Evolve | Tether | Default |
|---|---|---|---|
| Variables per iteration | Example pairs change several things at once (visual + hook + valence) and label them [L48](../lessons/48-how-to-iterate-on-losing-ads.md); [L54 08:49](../lessons/54-iteration-examples-breakdowns-walkthrough.md) | One variable at a time on winners | Winners (spend winner, breakthrough): one primary change per iteration, labelled. Losers being "fixed": several labelled changes allowed, since the goal is a new working version, not a clean read |
| Scaling a breakthrough | Budget jumps (illustration 2K → 5K/day), scale back if it dies; keep it on through bad days | +10% every other day, up to 10–15%/day while CPA holds | Tether's increments for budget; Evolve's keep-on rule for creative decisions |
| Hook-rate threshold | < 30% = hook problem [L48](../lessons/48-how-to-iterate-on-losing-ads.md); prompt says < 25% is "low" [L70](../lessons/70-how-to-write-video-ads-part-1.md) | — | < 25% definite hook issue; 25–30% probable; above, look past the hook |
| Fatigue | Breakthroughs die faster than before; check seasonality, copying, offer-only | Frequency ~2 is not fatigue | Don't call fatigue on frequency alone; check Evolve's lifespan risks first |

## Related
[Course playbooks hub](README.md) · [Ten-step learnings](../frameworks/ten-step-iteration-learnings.md) · [Iteration issue codes](../frameworks/iteration-issue-codes.md) · [Iteration playbook](../frameworks/iteration-playbook.md) · [Ad idea to brief](ad-idea-to-brief.md)

## Sources and limitations
- Thresholds (7 days, $1k, 30 iterations, 30%/25%) are instructor numbers without data; exact spend-share definitions are not in the course files. Step order, YAML and gates are pipeline design.
