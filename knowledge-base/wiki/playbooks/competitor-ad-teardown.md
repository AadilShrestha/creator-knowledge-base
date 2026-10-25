---
title: "Playbook: Competitor Ad Teardown (video/UGC or static → YAML teardown card)"
type: playbook
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/frameworks/valence-intensity-diagnostic.md
  - knowledge-base/wiki/frameworks/three-selves-diagnostic.md
  - knowledge-base/wiki/frameworks/teep-journey.md
  - knowledge-base/wiki/frameworks/mindstate-emotion-mapping.md
  - knowledge-base/wiki/frameworks/story-frameworks-for-ads.md
  - knowledge-base/wiki/frameworks/visual-weight-hierarchy.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md
tags: [playbook, competitor-research, ad-teardown, ugc, statics, beat-map, heuristics, valence-intensity, three-selves, teep, mindstates, winner-signals, transferable-mechanism]
updated: 2026-10-20
---

# Playbook: Competitor Ad Teardown
> Turn one competitor ad (UGC/video or static) into a **YAML teardown card**: what it says beat by beat, which heuristics, zone, self, TEEP stage and emotion it uses, why it works, how sure we are that it *is* working, and the **transferable mechanism** stated so abstractly that it can't be copied. The card is the input to [angle remix](angle-remix.md) and the [landscape audit](competitor-landscape-audit.md).

## 🤖 Agent use
- **Use when:** a human or upstream agent hands you a competitor ad that seems to be "popping off" and asks what is working and why.
- **Inputs → outputs:** ad asset (video file or frames + transcript, or static image) + copy + landing page + ad-library data (first-seen date, days live, variant count, platforms) + comments sample → one `teardown_card` (template below), plus 0–3 hook rows proposed for [hooks library](../libraries/hooks.md).
- **Rules:**
  - DO analyse in Sarah's order: **emotion → intensity → self** [Jun11 0:37:08–0:38:09], and judge the ad top-down: **identity → emotion → tactics** [May7 0:06:14–0:09:40].
  - DO read the **first frame / image before the words**: it is processed first [R3 0:32:37].
  - DO record **why the zone fits the buyer** for a winner, not just the zone [valence-intensity diagnostic, Step 6, teardown row].
  - DON'T treat run time as proof. "Running for 195 days" isn't proof; big brands leave ads on [Jun11 0:22:19–0:26:35]. Score [winner signals](#step-10-winner-signals-how-sure-are-we-it-works) instead.
  - DON'T copy. Extract the mechanism; never carry their footage, script lines, characters, trademarks, claims or stats forward. "It is a hundred percent important that you don't copy your competitors" [Jun11 0:42:22].
  - DO mark every tag that is your inference as `inferred`, and every claim of theirs as `their_claim` (unverified, never reusable).
- **See also:** [Landscape audit](competitor-landscape-audit.md) · [Angle remix](angle-remix.md) · [Ad scorecard](../rubrics/ad-scorecard.md) · [Ad teardowns library](../libraries/ad-teardowns.md) · [Brands hub](../brands/README.md) · [Contradictions](../contradictions.md)

**Source key:** May7 = [Live May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · May21 = [Live May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jul9 = [Live Jul 9](../courses/tether-lab/05-live-recordings/2025-07-09-live-with-sarah.md) · Jul16 = [Live Jul 16](../courses/tether-lab/05-live-recordings/2025-07-16-live-with-sarah.md) · R1 = [Roast #1](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md) · Chase = [Chase Mohseni](../courses/tether-lab/05-live-recordings/2025-06-guest-session-02-chase-mohseni.md) · COS = [CreativeOS bonus](../courses/tether-lab/02-heuristics-101/08-bonus-creativeos.md). Steps marked **(pipeline design)** are our process, not Sarah's.

## Inputs
| Input | Required | How to get it / notes |
|---|---|---|
| Ad asset | yes | Video: file or 1 frame per cut + full audio. Static: full-resolution image. Keep it in an internal research folder. **Research use only; never a production asset.** |
| Transcript with timestamps | video: yes | Whisper-style, word or line timestamps. Include on-screen text separately from speech. |
| Copy | yes | Primary text, headline, description, CTA button. |
| Landing page | recommended | URL + desktop and mobile screenshots of the hero and buy box. |
| Ad-library data | recommended | First-seen date, days live, active variants/duplicates using the same asset or script, platforms (FB/IG/TikTok), other markets. |
| Comments | recommended | 20–50 comments, or the count plus a sample. |
| Our product truth sheet | for step 11 only | See [playbooks README](README.md#hand-off-artifacts). |

## Procedure

### Step 1: Capture (pipeline design)
1. Assign an ID: `TD-<competitor-slug>-<yyyymmdd>-<nn>`.
2. Fill the `source` block of the card: platform, URL/library ID, first-seen, days live, variant count, CTA button, landing URL.
3. Store the asset path and note `usage: research-only`.

### Step 2: Transcribe and beat-map
1. **Video:** list every cut with its start time and describe each: shot type (selfie / close-up / wide / b-roll / screen recording), who is on screen, on-screen text, spoken line.
2. Measure **cut pace** (average seconds per cut). Benchmark: 2–3 s is the standard, ~4 s the longest Sarah has seen; past 4 s attention drops "unless the story is strong" [May14 0:43:47; 0:47:13].
3. Map the beats. Not every ad has all six; record `absent`.

   | Beat | Window (typical) | Question to answer |
   |---|---|---|
   | Hook | 0–3 s / frame 1 | What stops the scroll: visual, spoken line, text overlay? Which heuristic? |
   | Problem / setup | after hook | Whose situation? How specific ("four levels deep" [R3 0:33:42])? |
   | Mechanism | middle | *Why* the product works (ingredient, design, process, insight). |
   | Proof | anywhere | Type: demo, review, number, authority, before/after, skeptic concession. |
   | Offer | late | Discount, bundle, trial, guarantee, drop. |
   | CTA | last 2–3 s | Exact words; definitive or browse-y ("Shop now")? [R1 0:26:52–0:29:09] |

4. Compute the **setup share** (problem + lived experience seconds ÷ total). Story ads that work spend ~2/3 on setup [May14 0:19:45].
5. **Message in frame 1?** Does the core message appear in the first frame/seconds, or only later? (Net Positive's video lost sales by showing it halfway [R3 0:19:30–0:21:32].)
6. **Static:** instead of beats, build a weight map: rank 1/2/3 elements and what the eye hits first ([visual weight hierarchy](../frameworks/visual-weight-hierarchy.md), Procedure step 2).
7. Name the **story framework** if one is visible (Pixar, Hero's Journey, In Medias Res, SCQA, Freytag, PAS…) by matching beats to the step tables in [story frameworks](../frameworks/story-frameworks-for-ads.md#framework-catalogue-steps--ugc-skeletons).

### Step 3: Tag heuristics
1. Use the two decision tables in the [heuristics hub](../concepts/heuristics.md#quick-teardown-decision-table) to label every shortcut; use slugs = file names in `concepts/heuristics/`.
2. Note **where** each sits (hook, body, badge, offer). In video, heuristics live "mostly in hooks" [Jul9 0:53:44].
3. Expect 2–3, with [processing fluency](../concepts/heuristics/processing-fluency.md) as the base ([heuristic stacking](../concepts/heuristic-stacking.md)). Flag the "less obvious" ones (affect, framing, goal gradient, Von Restorff…), which are the most reusable.
4. Note the **messenger**: who delivers the line (peer, skeptic, employee, expert, founder) → [messenger effect](../concepts/heuristics/messenger-effect.md), [in-group bias](../concepts/heuristics/in-group-bias.md).

### Step 4: Valence/intensity zone
Run [valence-intensity diagnostic](../frameworks/valence-intensity-diagnostic.md) Steps 1–5 in `teardown` mode: valence −2…+2, intensity 0…4 with evidence, zone Z1–Z4. Then write `why_zone_fits`: the buyer's state at exposure and why this zone moves them. Optional cross-check prompt (verbatim, on screen): **"Analyze this ad for valence + intensity. Which zone is this ad in?"** [Jun11 0:04:30].

### Step 5: Self
Score Actual / Ideal / Ought 0–10 with the [three-selves rubric](../frameworks/three-selves-diagnostic.md#scoring-rubric-apply-per-ad), copy **and** visuals. Classify by motivation frame, not tense ("your future self will thank you" = Ought). Quote the cue words.

### Step 6: TEEP stage
Tag T / E1 (exploration) / E2 (evaluation) / P using the cues in [TEEP](../frameworks/teep-journey.md#teardown-use-tagging-ads-by-stage): event call-out = T; entertaining/weird/brand intro = E1; comparison, ingredients, founder, "why not Amazon" = E2; discount/bundle/urgency = P. Record the cue that decided it.

### Step 7: Emotion (Leach mindstates)
1. Pick the dominant purchase emotion from the nine *Marketing to Mindstates* emotions ([mindstate mapping](../frameworks/mindstate-emotion-mapping.md); list is outside context, see that page).
2. Push it to a **specific** sub-emotion ("boardroom-level confidence", "disappointment", not "confidence", "fear") [Jun4 0:38:43] → [emotion specificity](../concepts/emotion-specificity.md).
3. Name the **emotional promise** (the payoff sold) → [emotional promise](../concepts/emotional-promise.md). Check there is **one** core emotion ([one core emotion per ad](../concepts/one-core-emotion-per-ad.md)).

### Step 8: Format and creative primitives
1. **Format:** UGC talking head · skeptic test · reluctant convert · fake podcast · founder story · demo · skit / mirror-effect · voiceover b-roll · motion static · comparison static · testimonial static · all-text / sticky note · advertorial-style ([native advertising](../concepts/native-advertising.md)).
2. **Primitives inventory** ([creative primitives](../concepts/creative-primitives.md)): copy line, product shot, background, colour, icon, badge, crop/angle, model/creator, setting, CTA.
3. **Visual psychology:** face/expression/posture ([model image psychology](../concepts/model-image-psychology.md)); ingredients shown? ([sight smell](../concepts/sight-smell.md)); props and context ([hero-image ↔ copy congruence](../concepts/hero-image-copy-congruence.md)); palette vs category ([colour psychology](../concepts/color-psychology.md)).
4. **Ability move** ([Fogg](../frameworks/fogg-behavior-model.md)): what does it do to answer "is this for me / will it fit / will it work"? Ability moves are easy to miss and often what makes it convert.
5. **Page congruence:** does the landing page repeat the ad's promise, tone and claims? (quick check; full audit with [landing-page scorecard](../rubrics/landing-page-scorecard.md)).

### Step 9: Why it works (one paragraph, max 3 sentences)
Template: *"For <buyer in state X>, the ad <activates self Y> by <identity cue>, sells <specific emotion / promise> at <zone> intensity, and removes <objection / ability crusher> with <proof type>; <heuristic A + B> make it fast to process."* Then list the **one element doing most of the work** (your hypothesis) and how you'd test it (a removal test [R1 0:22:01–0:23:01]).

### Step 10: Winner signals (how sure are we it works?)
Ad libraries don't show spend or sales: "we have no idea how much they're spending or how much they're making" [Jun11 0:41:18]. Score the evidence:

| Signal | Points (pipeline design) | Source / caveat |
|---|---|---|
| Live ≥ 90 days | +2 | CreativeOS "Evergreen" filter: presumed winner [COS 05:12] |
| Live ≥ 90 days **and** the brand is large | +1 only (instead of +2) | Big brands can afford to leave ads on; "running for 195 days" isn't proof [Jun11 0:22:19–0:26:35] |
| ≥3 active variants / duplicates of the same script or asset | +2 | Brands iterate what pays (pipeline inference) |
| Same concept on 2+ platforms or markets | +1 | pipeline inference |
| Comments: high volume **and** emotionally intense ("I will fight to the death to get this") | +2 | "The best ads… have thousands and thousands of comments… and run for a very, very long time" [May7 0:53:44–0:55:37] |
| Comments few or neutral ("love this") | 0 | [May7 0:54:40–0:55:04] |
| Unprompted organic content about it (stitches, remakes) | +1 | [May7 0:53:44–0:55:37] |
| Recently launched, one variant | 0 → `unproven` | |
| Real metrics known (member/own account, agency data) | override: use them | e.g. Net Positive CTR 6.5–7% [R3 0:04:08] |

**Confidence:** ≥6 = `high` · 3–5 = `medium` · ≤2 = `low`. `low` cards may still be torn down for ideas but are not used as the *only* source of an angle. The conflict between the 90-day rule and Jun 11 is logged in [contradictions](../contradictions.md) (row 9).

### Step 11: The transferable mechanism
1. Write the mechanism with **placeholders** only, no brand words: *"<Skeptic persona> voices the viewer's disbelief of <category claim>, runs <one harsh, fair, on-camera test>, and concedes reluctantly; <recurring catchphrase> builds fluency."*
2. List what is **kept** (structure, psychology, beat order, proof *type*) and what is **asset-specific and banned** (their footage, character, names, catchphrases, exact lines, trademarks, claims, numbers, distinctive visual signature).
3. Note **fit preconditions**: what must be true of *our* product for this mechanism to be honest (e.g. "requires a claim we can demonstrate in one shot").
4. Suggest 1–3 remix directions (another self, zone, framework or stage nobody in the niche uses) → handed to [angle remix](angle-remix.md).

## Output: teardown card
```yaml
teardown_card:
  id: TD-<competitor>-<yyyymmdd>-<nn>
  analyst: <agent id>
  date: <yyyy-mm-dd>
  source:
    brand: "<competitor>"
    niche: "<category>"
    platform: meta | tiktok | youtube | other
    url_or_library_id: "<…>"
    first_seen: <date | unknown>
    days_live: <n | unknown>
    active_variants: <n | unknown>
    platforms_seen: [<…>]
    cta_button: "<Shop now | Learn more | …>"
    landing_url: "<…>"
    asset_path: "<internal path>"
    usage: research-only            # never a production asset
  format: "<ugc talking head | skeptic test | fake podcast | founder | demo | comparison static | …>"
  length_s: <n>                      # video only
  cut_pace_s: <avg seconds per cut>
  messenger: "<peer | skeptic | employee | expert | founder | character | none>"
  beat_map:                          # video; statics use weight_map
    - beat: hook
      t: "0:00-0:03"
      visual: "<what is on screen>"
      on_screen_text: "<verbatim>"
      spoken: "<verbatim>"
      heuristics: [<slug>]
    - beat: problem
      t: "…"
      …
    - beat: mechanism
    - beat: proof
      proof_type: demo | review | number | authority | before_after | skeptic_concession | none
    - beat: offer
    - beat: cta
  weight_map:                        # statics
    rank_1: "<element>"
    rank_2: "<element>"
    rank_3: "<element>"
    skipped_ok: ["<…>"]
  setup_share: <0.0-1.0>
  message_in_frame_1: true | false
  story_framework: "<Pixar | Hero's Journey | In Medias Res | SCQA | Freytag | PAS | none>"
  heuristics:
    - slug: <file name in concepts/heuristics/>
      where: hook | body | badge | offer
      evidence: "<words/visual>"
  zone:
    valence: <-2..+2>
    valence_evidence: ["<…>"]
    intensity: <0..4>
    intensity_evidence: ["<…>"]
    zone: Z1 | Z2 | Z3 | Z4 | unmapped
    why_zone_fits: "<buyer state at exposure → why this zone moves them>"
    status: scored | inferred
  self:
    actual: <0-10>
    ideal: <0-10>
    ought: <0-10>
    dominant: actual | ideal | ought | mixed
    cues: ["<quoted copy / visual cue>"]
  teep_stage: T | E1 | E2 | P
  teep_cue: "<what decided it>"
  emotion:
    mindstate: "<achievement | autonomy | belonging | competence | empowerment | engagement | esteem | nurturance | security | other>"
    specific: "<sub-emotion>"
    promise: "<payoff sold>"
    one_core_emotion: true | false
  primitives:
    copy_line: "<…>"
    product_shot: "<…>"
    background: "<…>"
    colour: "<…>"
    badge: "<…>"
    crop_angle: "<…>"
    model_creator: "<expression, posture, casting>"
    setting_props: "<…>"
  ability_move: "<qualifier / demo / fit proof / none>"
  page_congruence: match | partial | mismatch | not_checked
  their_claims: ["<claim>"]          # unverified; NEVER reusable
  why_it_works: "<≤3 sentences>"
  key_element_hypothesis: "<the one element doing most of the work>"
  winner_signals:
    points: <n>
    evidence: ["<signal: value>"]
    confidence: high | medium | low
  transferable_mechanism:
    statement: "<placeholders only, no brand words>"
    keep: ["<structure / psychology / beat order / proof type>"]
    banned_assets: ["<their footage, character, lines, marks, claims, numbers>"]
    fit_preconditions: ["<what must be true of our product>"]
    remix_directions: ["<other self / zone / framework / stage>"]
  proposed_library_rows:
    hooks: ["<hook row for libraries/hooks.md>"]
```

## Worked example: Net Positive underwear (Roast My Ads #3)
Built from the real roast of Darian James's Net Positive ads [R3 0:02:05–0:21:32]; case file: [Net Positive](../brands/net-positive.md). It isn't a competitor of ours, but it is the best-documented "winning static → failing video" case in the course, with real metrics, so it shows every field. Tags marked `inferred` are the wiki's, not Sarah's.

```yaml
teardown_card:
  id: TD-net-positive-20250723-01
  date: 2026-10-20
  source:
    brand: "Net Positive"
    niche: "natural-fibre women's underwear (apparel)"
    platform: meta
    first_seen: unknown
    days_live: unknown
    active_variants: 3              # V1 static, V2 static + badges, V3 motion video
    cta_button: unknown
    usage: research-only
  format: "static (V1, V2) → short motion video of the static with lo-fi track (V3)"
  messenger: "model only, no speech"
  weight_map:                       # V2 static
    rank_1: "DITCH POLYESTER headline"
    rank_2: "redhead model, confident face, grey wall, brown set"
    rank_3: "badge 'ONLY 9 SETS LEFT in This Color' + footer 'You're 1 Click Away From Better Underwear'"
    skipped_ok: ["No Itch / No Irritation", "Naturally Breathable"]
  beat_map_v3:
    - beat: hook
      t: "0:00-0:03"
      visual: "model in underwear, no headline"
      on_screen_text: "Net Positive / No forever chemicals."
    - beat: message
      t: "~halfway"
      on_screen_text: "DITCH POLYESTER / No forever chemicals. No plastic. No compromises."
  message_in_frame_1: false          # V3; true for V1/V2
  heuristics:
    - {slug: framing-effect, where: hook, evidence: "'Ditch Polyester': a common enemy"}
    - {slug: scarcity-heuristic, where: badge, evidence: "'Only 9 sets left in this color'"}
    - {slug: social-proof, where: badge, evidence: "implied: 'people have purchased it enough' [0:16:50]"}
    - {slug: goal-gradient-effect, where: badge, evidence: "'1 Click Away' (inferred)"}
  zone:
    valence: +2
    intensity: 2
    zone: Z2
    why_zone_fits: "Millennial women leaving behind 'what doesn't serve us anymore'; confident, defiant energy [0:08:23-0:09:29]"
    status: inferred
  self: {actual: 5, ideal: 7, ought: 1, dominant: ideal, cues: ["ditch", "confident smirk, chest-out posture"]}
  teep_stage: E2                    # V1/V2 prospecting; V2 footer imported from P-stage ads (inferred)
  emotion:
    mindstate: empowerment           # inferred
    specific: "liberated confidence: 'I just don't care what people think about me' [0:06:55-0:08:23]"
    promise: "shed what irritates you; feel confident in your own body"
    one_core_emotion: true
  primitives:
    model_creator: "redhead; brows centred and pulled in, lowered lids, smirk not smile; normal un-airbrushed body; elbows on wall, chest out [0:05:14-0:12:36]"
    background: "plain grey wall"
    badge: "scarcity + colour ('in this color')"
  ability_move: "'in this color' clears the brain's 'reason not to buy' checklist [0:15:46-0:16:50]"
  page_congruence: mismatch          # badge message not on the landing page [0:15:00; 0:17:00]
  their_claims: ["Only 9 sets left (Darian: 'I just made that up' [0:15:00])"]
  why_it_works: >
    For millennial women tired of synthetic, itchy underwear, the static sells liberated
    confidence (Z2) through a two-word common-enemy line, and every visual signal (face,
    hair, posture, body) repeats that message. V3 failed because the message arrived
    after the scroll decision and skin without context reads as 'weird' [0:19:30-0:21:08].
  key_element_hypothesis: "the model's face + 'Ditch' headline in frame 1; other models underperformed [0:05:14]"
  winner_signals:
    points: override
    evidence: ["V1 CTR 6.5-7% (traffic campaign) [0:04:08]", "V2 beat V1", "V3: clicks, no early sales [0:18:56]"]
    confidence: high                 # for the static; low for the video
  transferable_mechanism:
    statement: >
      Name the material/ingredient/habit the buyer is ready to leave behind as a 1-2 word
      imperative ('Ditch <enemy>'), put it in frame 1, and cast one face whose expression,
      posture and body all say the same emotion; add one small, TRUE scarcity-or-popularity
      badge as a supporting character.
    keep: ["imperative common-enemy headline", "message-before-model order", "face = message casting", "badge as support"]
    banned_assets: ["'Ditch Polyester'", "their model/photos", "'1 Click Away From Better Underwear'", "invented stock count", "Net Positive marks"]
    fit_preconditions: ["our product genuinely replaces a disliked material/habit", "any stock badge uses real inventory"]
    remix_directions: ["Actual-self version: 'you already know what feels right'", "Z3 version: the itch moment", "skeptic UGC: wearing it through a hot day"]
```

## Quality gates (all must pass before hand-off)
- [ ] Every field is filled or explicitly `unknown`; nothing guessed silently.
- [ ] Each heuristic, zone and self tag quotes evidence from the ad.
- [ ] Zone was scored valence → intensity, and `why_zone_fits` names the buyer's state.
- [ ] Winner signals are scored and confidence is set; run time alone never makes `high`.
- [ ] `transferable_mechanism.statement` contains no competitor brand, product, character or line (search for their name and any 4+ word string from the transcript).
- [ ] `their_claims` lists every factual claim they make; none appear in `keep`.
- [ ] Optional: score the ad with the [ad scorecard](../rubrics/ad-scorecard.md) to see which criteria carry it.

## Common mistakes
- Tagging the copy and ignoring the image, which is read first [R3 0:32:37].
- Calling a long-running big-brand ad a winner from longevity alone [Jun11 0:24:32].
- Writing the mechanism as their headline with our product name swapped in (that's copying).
- Treating a new format as a new emotion (AG1's offer, comparison and product ads were all Z1) [Jun11 0:05:19–0:08:23].
- Missing the ability move; competitors show their prompts and motivation openly and their ability moves quietly ([Fogg](../frameworks/fogg-behavior-model.md)).

## Related
[Playbooks hub](README.md) · [Landscape audit](competitor-landscape-audit.md) · [Angle remix](angle-remix.md) · [Valence-intensity diagnostic](../frameworks/valence-intensity-diagnostic.md) · [Three-selves diagnostic](../frameworks/three-selves-diagnostic.md) · [TEEP](../frameworks/teep-journey.md) · [Mindstate mapping](../frameworks/mindstate-emotion-mapping.md) · [Story frameworks](../frameworks/story-frameworks-for-ads.md) · [Skeptic format](../frameworks/skeptic-format.md) · [Visual weight hierarchy](../frameworks/visual-weight-hierarchy.md) · [Psychology application ladder](../frameworks/psychology-application-ladder.md) · [Emotional stagnation](../concepts/emotional-stagnation.md) · [ChatGPT](../tools/chatgpt.md) · [Ad teardowns library](../libraries/ad-teardowns.md)
