---
title: "VSL review rubric (structure checks + 16-05 live-data benchmarks)"
type: rubric
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi (structure, modules 4-7); Patrick Stiles of Vidalytics (benchmarks, 16-05, guest)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-02-vsl-fundamentals-classic-structure.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-03-vsl-leads-after-the-opening-hook.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-04-vsl-background-stories-and-unique-mechanisms.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-05-vsl-product-buildup-and-reveal.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-06-vsl-closes.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/06-01-claude-vsl-projects-setup-overview.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-01-long-form-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-02-medium-length-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-03-3-7-minute-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/07-04-short-vsl.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md
tags: [rubric, vsl, script-review, structure, lead, mechanism, close, benchmarks, vidalytics, engagement, conversion-rate, unmute, cta-timing]
updated: 2026-11-02
---

# VSL review rubric
> Two-part review for any video sales letter: Part 1 scores the script against Stefan Georgi's classic structure and his LLM-draft checks before it is recorded; Part 2 diagnoses a live VSL against Patrick Stiles' Vidalytics benchmarks (16-05) in the order he gives, and names the fix for each miss.

## 🤖 Agent use
- **Use when:** (Part 1) an outline or script from a Claude VSL Generator project, a human writer, or a swipe needs a go/no-go before recording; (Part 2) a VSL is live and you have player analytics.
- **Inputs → outputs:** (Part 1) script + brief + placement (in-feed or on-page) + target length + CTA type + the [claim audit](llm-output-claim-audit.md) result → per-check pass/fail with quoted evidence, a score, a band and an ordered fix list. (Part 2) conversion rate, engagement at 2 min / CTA drop / end, unmute rate and time, conversion by watch point, length, CTA-drop %, device split, returning-visitor share, funnel type → benchmark gaps and the ordered fixes.
- **Rules:**
  - **DO** run the [LLM output claim audit](llm-output-claim-audit.md) first. A VSL with any ⛔ claim fail is BLOCKED regardless of structure score.
  - **DO** decide placement before scoring: in-feed and on-page VSLs use different spines; "especially the lead really needs to be different" ([04-11 11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)).
  - **DO** score structure beat by beat: "The more closely you can generally follow this beat by beat structure, the better." ([04-02 34:31–36:57](../lessons/04-02-vsl-fundamentals-classic-structure.md))
  - **DO** check length by word count, not the model's estimate: Claude estimated about 8,500 words; actual was 5,707 ([07-01 v3 01:13](../lessons/07-01-long-form-vsl.md)). Derived rate: about 150 spoken words per minute ([07-02](../lessons/07-02-medium-length-vsl.md)).
  - **DO** fix the lead first when a live VSL underperforms: "the highest impact split test is always going to be split testing the lead of the video" (guest claim, [16-05 20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)); Stefan agrees: more people reaching the pitch enlarges every later optimisation ([04-05 30:58–35:38](../lessons/04-05-vsl-product-buildup-and-reveal.md)).
  - **DON'T** treat 16-05 player correlations as split-test proof: "these aren't split tests" ([16-05 11:23–11:52](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)). Benchmarks are vendor data, health-heavy, mostly paid traffic.
  - **IF** a retention curve drops steeply at one mid-video point **THEN** fix that section, not the lead ([04-05 38:13–39:52](../lessons/04-05-vsl-product-buildup-and-reveal.md)).
- **See also:** [Classic VSL structure](../concepts/classic-vsl-structure.md) · [VSL length bands](../concepts/vsl-length-bands.md) · [VSL build with Claude](../frameworks/vsl-build-with-claude.md) · [Write a VSL with Claude (playbook)](../playbooks/write-a-vsl-with-claude.md) · [Benchmarks library](../libraries/benchmarks.md) · [Funnel audit](funnel-audit.md) · Evolve: [copy checklist scorecard](../../../evolve/copywriting/rubrics/copy-checklist-scorecard.md) · Tether: [ad scorecard](../../../../rubrics/ad-scorecard.md)

---

## Part 1: script review (before recording)

### Step 0: context (fill before scoring)
```text
Asset: ____  Placement: in-feed ad | on-page VSL | both   Funnel: straight sale | book-a-call | upsell | tease-to-longer-VSL
Target length: __ min  Measured words: __ (÷150 = __ min, derived)   Awareness target: problem | solution | product
Narrator: founder | expert | customer | host+expert   CTA: buy | book call | watch longer video
Claim audit verdict: PASS | FIX | BLOCK  (BLOCK = stop here)
```

### Length band check
| Band (project) | Range (instruction docs) | Typical use | Source |
|---|---|---|---|
| Long Form VSL Generator | 25-60 min | ClickBank-type traffic; on Meta Stefan "would probably shoot for a shorter video ad" | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md); [07-01 v2 34:11–35:17](../lessons/07-01-long-form-vsl.md) |
| Medium Length VSL Generator | 6-16 min (he asks for ~18 because Claude "estimates a little low") | In-feed or on-page | [06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md); [05-02 23:00](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) |
| 3-7 Minute VSL Generator | 3-7 min | "Almost always" in-feed Meta ads that tease and send to a video/report | [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Short Length VSL Generator | 1-4 min (spoken "almost all one to two minutes") | Short ads | [06-01 00:30](../lessons/06-01-claude-vsl-projects-setup-overview.md) |
| Live-data sweet spot (guest) | 15-35 min convert highest; straight sale best 20 / worst 45; book-a-call best 25 / worst 60; upsell best 20 / worst 40; "about an hour… drop off a cliff" | Use to choose a long-form target | [16-05 35:17–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) |

**Conflict and default:** the long-form project allows up to 60 minutes; the 16-05 data puts 45+ minutes at the worst-converting end for straight sale (guest claim). Agent default: target 20-35 minutes for a straight-sale long form unless the niche average is longer (finance 59, health 40 min averages, [16-05 34:54](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) and you can test.

### Structure checks
Score each 2 = fully present and correct, 1 = present with a defect, 0 = missing or wrong. n.a. needs a reason (e.g. a 90-second tease ad has no close).

| # | Check | PASS (2) if | Why (cited) | Fix |
|---|---|---|---|---|
| S1 | **Spine order** | Beats run hook/micro-lead → lead → background → discovery → UMP → UMS → product build-up and reveal → close → FAQ (on-page); in-feed: hooks → education → pain + promise → quick background → UMP → UMS → build-up/reveal → close | "For any kind of consumer physical product, you're basically always following the structure" ([04-02 00:56–01:50; 15:01](../lessons/04-02-vsl-fundamentals-classic-structure.md)); in-feed spine from the doc ([04-11 04:02–05:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)) | Re-order; attach the classic outline to the project and ask for a revised outline ([07-01 C4](../lessons/07-01-long-form-vsl.md)) |
| S2 | **No zig-zag** | No new topic block (e.g. "five myths") inserted after the build-up starts; sections only subtracted, not added | Adding creates "a zigzag sales letter structure" ([04-05 15:47–17:40](../lessons/04-05-vsl-product-buildup-and-reveal.md)) | Cut or move the block into its native section |
| S3 | **Micro-lead / hook** | First 10-30 s relates fast to the pain and to the promise; 2-3 alternate micro-leads exist over the same body | [04-02 03:05–06:36](../lessons/04-02-vsl-fundamentals-classic-structure.md); [04-03 10:58; 46:22](../lessons/04-03-vsl-leads-after-the-opening-hook.md) | Generate leads in the hook project and paste 3-4 options on top ([07-01 v4](../lessons/07-01-long-form-vsl.md)) |
| S4 | **Lead does its job** | Calls out problem, promises solution, teases discovery story, teases the mechanism and its contrarian nature, fascinations, brief credibility, qualifiers, addresses skepticism; ends with a small promise and future pace | Lead checklist ([04-03 14:20–15:20](../lessons/04-03-vsl-leads-after-the-opening-hook.md)); "one thing I might like to see at the end of the micro lead is a little promise" ([07-02 v1 26:26–27:02](../lessons/07-02-medium-length-vsl.md)) | Ask the model to add the missing items; keep mid-length leads short ([04-02 09:55](../lessons/04-02-vsl-fundamentals-classic-structure.md)) |
| S5 | **Lead teases, doesn't teach** | Mechanism is teased, not explained; product, product type and brand not named in the lead | "Don't teach or explain the mechanism inside the lead" ([04-03 17:14; 26:19](../lessons/04-03-vsl-leads-after-the-opening-hook.md)); "applying this every morning" became "using this breakthrough" ([07-01 v1 47:26–48:29](../lessons/07-01-long-form-vsl.md)) | Replace product-type words with "this breakthrough"/"this discovery" |
| S6 | **No assumed viewer state** | Lead and body guess and soften ("maybe you've…") rather than assert the viewer's life | "you're probably living it too" puts the viewer on the defensive ([07-01 v1 48:29–49:33](../lessons/07-01-long-form-vsl.md)) | Rewrite as a qualifier or a "some people notice…" line |
| S7 | **One big idea, concrete metaphor** | Lead carries one fascinating idea and a repeated "one thing" phrase; metaphor maps to the viewer's own problem | "five tasty superfoods" repetition ([04-03 23:48](../lessons/04-03-vsl-leads-after-the-opening-hook.md)); "riot" too abstract, "silent war" fixed ([04-03 44:55–45:52](../lessons/04-03-vsl-leads-after-the-opening-hook.md)) | Pick one idea; swap abstract metaphors for physical ones |
| S8 | **Background in five beats, moving** | Who I am + credibility; just like you + emotional story; traditional solutions failed; trigger event; search for truth; with check-ins to the viewer | [04-04 07:59–08:57; 49:26; 49:56–51:25](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md) | Trim the pain story; add "Have you ever…?" check-ins |
| S9 | **UMP explainable in one sentence** | Real cause, surprising, simple metaphor, recap sentence; (health) how it should work → why it doesn't → culprit | "it's a pretty good mechanism because it's pretty easy to understand" ([04-02 13:04](../lessons/04-02-vsl-fundamentals-classic-structure.md)); repeatable after "one or two times" ([04-04 51:54–53:44](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md)) | Cut jargon ("move away from the DEJ" [05-02 07:58](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md)) |
| S10 | **UMS logically tied, macro then micro** | Macro solution first, then the specific device/ingredients with real citations; supplement ingredients revealed in the UMS, not first at the reveal | [04-04 09:26; 43:09–45:29](../lessons/04-04-vsl-background-stories-and-unique-mechanisms.md); [04-02 39:48–41:48](../lessons/04-02-vsl-fundamentals-classic-structure.md) | Use the supplement UMS template ([04-02](../lessons/04-02-vsl-fundamentals-classic-structure.md)) with truth-sheet facts only |
| S11 | **"Why can't I just buy it?" answered** | Before the reveal, says why the off-the-shelf version fails, with a real reason | "if the solution was Ashwagandha, go buy it on Amazon, you won't have a product to sell" ([04-02 16:57–17:55](../lessons/04-02-vsl-fundamentals-classic-structure.md)); [04-05 00:00–00:55](../lessons/04-05-vsl-product-buildup-and-reveal.md) | Add a real differentiator (form, dose, combination, sourcing) `[VERIFY]` |
| S12 | **Build-up is real** | Trial-and-error section present and true (real sourcing, testing, formulation) | "when you really play this up, it just converts better" ([04-02 19:50–22:40](../lessons/04-02-vsl-fundamentals-classic-structure.md)); Stefan calls the Nooro prototype story made up ([04-02 21:45](../lessons/04-02-vsl-fundamentals-classic-structure.md)) → claim-audit C11 | Use real development facts or shorten the section |
| S13 | **Brand held to the reveal** | Brand/product name first appears at the end of build-up and reveal | [07-01 v1 31:13–32:48](../lessons/07-01-long-form-vsl.md); [05-02 26:59](../lessons/05-02-the-brief-generator-with-claude-project-unity-eye-serum-exam.md) | Remove earlier mentions |
| S14 | **Close is the longest section and complete** | Close ≈ 25-35% of a full VSL; product details, dismiss alternatives, value, testimonials (real), how to use (numbered), price justification + anchor (real), personal mission, offer, "smart people buy more", first CTA, what happens next, guarantee with contact details, second CTA, two choices, third CTA, FAQ + CTA | [04-05 20:08–20:37](../lessons/04-05-vsl-product-buildup-and-reveal.md); close outline ([04-06](../lessons/04-06-vsl-closes.md)); guarantee contact details "alleviates a lot of concern" ([04-06 30:31](../lessons/04-06-vsl-closes.md)) | Ask the model to add the missing close beats in order |
| S15 | **First CTA not buried** | First CTA comes right after price reveal + "smart people buy more", with only a couple of sentences on the biggest package; single-unit buyers not shamed | [04-06 12:12–14:38; 28:40–29:09](../lessons/04-06-vsl-closes.md) | Move the button up; add "even if you only get one…" style line |
| S16 | **Enough CTAs, each with a reason why** | Multiple CTAs; every price, bundle, guarantee and urgency line has a reason | "you can't really go wrong with too many call to actions"; "It's all reason why copy." ([04-06 08:47; 38:42](../lessons/04-06-vsl-closes.md)) | Add CTAs after guarantee, two-choices, FAQ |
| S17 | **Post-CTA clincher** | After the first CTA, copy speaks to the deciding buyer ("If you're ready to buy, then do it." "I am not going over anything new here.") | 47% of conversions come from the 3% who reach the end (guest claim, [16-05 30:44–31:14; 33:53](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) | Write a clincher block; plan a countdown redirect end screen |
| S18 | **Every opened loop paid off** | Each tease/fascination in the lead resolves later | Morocco tease "wasn't paid off right" ([07-02 v1 29:53; 30:08–30:37](../lessons/07-02-medium-length-vsl.md)) | Ask for a fascination "that does get paid off later in the VSL" |
| S19 | **Transitions and objections** | Bridge lines before topic shifts and before objection handling; natural objections answered inside the UMP and again in close/FAQ | "we need a better transition" ([07-02 v2 13:05–14:18](../lessons/07-02-medium-length-vsl.md)); [04-02 36:57–39:48](../lessons/04-02-vsl-fundamentals-classic-structure.md); "not turmeric" said at first mention ([07-03 v2 07:06](../lessons/07-03-3-7-minute-vsl.md)) | Prompt for bridge lines (07-01 C12 pattern) |
| S20 | **No AI phrasing** | No stock AI phrases ("reclaim their vitality") | [07-02 v1 12:36](../lessons/07-02-medium-length-vsl.md) | Read aloud; replace with customer language |
| S21 | **Placement fit** | In-feed: education/entertainment-led, curiosity-heavy, often multi-hook, CTA "watch the video", no brand/product ([07-03 v1 01:47–02:09](../lessons/07-03-3-7-minute-vsl.md)); on-page: classic lead | An in-feed winner dropped engagement on a page because "there was no classic lead" ([04-11 09:59–11:01](../lessons/04-11-vsls-on-landing-pages-vs-vsls-as-in-feed-ads.md)) | Write a placement-specific lead over the same body |
| S22 | **Length measured** | Word count within the target band (÷150 wpm, derived) | [07-01 v3 01:13](../lessons/07-01-long-form-vsl.md); 3-minute scripts ran 790-850 words, i.e. 5+ min ([07-03](../lessons/07-03-3-7-minute-vsl.md)) | Cut or extend; for cut-downs keep the opening options ([07-02 v2 00:28–01:01](../lessons/07-02-medium-length-vsl.md)) |
| S23 | **First 7 seconds work muted** | Opening is visually and textually strong without sound; captions planned | Average unmute at ~7 s; make the first 7 s "super juicy" (guest claim, [16-05 24:04–24:30](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) | Add on-screen text, real footage, captions |

**Scoring (pipeline design, not the course's):** sum applicable checks ÷ (2 × applicable) = %. ≥ 85% = record; 70-84% = fix listed defects then record; < 70% = re-outline. S1, S5, S12, S14 (full VSLs) at 0 = re-outline regardless of %.

### Review output format
```text
VSL REVIEW: <asset>  | claim audit: PASS/FIX/BLOCK | measured: __ words ≈ __ min (band __)
Scores: S1 _ S2 _ S3 _ S4 _ S5 _ S6 _ S7 _ S8 _ S9 _ S10 _ S11 _ S12 _ S13 _ S14 _ S15 _ S16 _ S17 _ S18 _ S19 _ S20 _ S21 _ S22 _ S23 _
Score: __% → record | fix | re-outline
Top fixes (lead first, then the earliest structural defect, then polish):
1. [check] "quoted line" → fix
2. …
Lead variants to test over the same body: __
```

---

## Part 2: live VSL diagnosis (16-05 benchmarks)
All figures are Patrick Stiles' Vidalytics platform data (guest claim): correlation, not split tests; mostly health advertisers and paid traffic ([16-05 04:39; 07:33–08:03; 11:23–11:52](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)). Work top to bottom: the deck runs "from the easy wins… to the stuff that's going to be a heavier lift" ([16-05 01:28](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)).

| # | Metric | Benchmark (guest claim) | Cite | FAIL if | Fix (in order) |
|---|---|---|---|---|---|
| B1 | Conversion rate | 1.78% all videos; ~8% (8.24%) book-a-call. Niche: Biz Op 2%, Dating 0.73%, Finance 3.45%, Golf 0.54%, Health 1.61%. Source: Meta 1.87%, Google paid 1.55%, YouTube 0.75%, TikTok 0.50% | [16-05 04:14; 06:08–07:33; slides 12-15](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Below the niche and source figure for your funnel type | Segment by device and source first; then cheap player fixes (B2); then lead tests (B3) |
| B2 | Player setup | Controls on; video can run 1080p but starts at medium or lower resolution; smart autoplay, smart pause, focused full screen; thumbnail/first frame set | [16-05 11:01–19:36; 28:22–30:16](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Any missing; autoplay fails ~6.4-6.5% of the time, "over 1/20th of your traffic" | Turn on; always set a thumbnail |
| B3 | Engagement at 2 min | 33% | [16-05 19:36; slide 31](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | < 33% | Rework and split-test the lead (deck: "replace the first 2 minutes"); fire a tracking event at 2:00 to price "getting somebody to two minutes" ([20:35–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B4 | Engagement at CTA drop | ~28% (29% in Q&A) | [16-05 slide 31; 57:54](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | < 28%, or a big gap from B3 | Work the lead-to-CTA stretch: "I'd really focus on the message between those two… the biggest leverage point" ([58:54–1:00:44](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)); re-score S8-S13 |
| B5 | Engagement at end | 3% | [16-05 slide 31](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | < 3% | Work the close (CTA to end): S14-S17 |
| B6 | Average engagement | 19% (niche 12-24%; health 12%, finance 24%) | [16-05 15:29; slide 27](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Context only | Don't chase engagement alone: correlation with conversion 28% and weakening ([14:33–16:27](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B7 | Unmute rate | Avg 40%; top 10% 75% | [16-05 24:30–25:29](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Far below 40% (example: 18% was a presell/headline problem) | Fix headline/presell and the first 6-7 s; add captions; customise the autoplay message ("Front and Center" 32% vs no message 7%, slide 40); looping video thumbnail ([21:55–27:39](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B8 | Unmute time | Avg 7 s (best 0, worst 63) | [16-05 24:04](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | > 7 s | Strengthen the opening visuals: real footage "not B-roll, not text on screen" ([25:29–27:39](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B9 | Conversions at end of video | 47% of conversions come from the 3% at the end (35% earlier) | [16-05 30:44–31:14](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | No post-CTA clincher; no end screen | Clincher copy (S17); countdown-timer redirect; CRM tags and micro-conversion retargeting for deep viewers ([31:14–33:53](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B10 | Length | Avg 36 min (2025); sweet spot 15-35; straight sale best 20 / worst 45 | [16-05 34:24–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Straight sale ≥ 45 min, or ~60 min any type | Test a cut-down (07-02 Pipeline B) |
| B11 | CTA drop point | Best converters drop at 30% of the video; worst at 79% | [16-05 36:12–36:42; slide 55](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | CTA drop late (≥ ~75%) and conversion below B1 | Test an earlier offer/button drop (reveal need not coincide with the CTA, slide 56); track AOV and LTV: "what is their AOV and their lifetime customer value" ([42:05–42:35](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B12 | Upsell VSLs | Engagement 15% vs 21% front end; seeking bar 24% (+60%); take rate "can be 20%"; avg upsell length 24 min (36 in 2022); best 20 / worst 40 | [16-05 42:44–43:33](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | No seeking bar; > 20 min | "put seeking bars on all of your upsells"; shorten |
| B13 | Devices | Mobile 72% of traffic; straight sale converts best on desktop, book-a-call on mobile; tablets 27% lower conversion | [16-05 43:33–44:57](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | One cut for all devices | Vertical cut for mobile, landscape for desktop ([44:57–45:25](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B14 | Returning visitors | 12% of traffic; convert 62% higher (slide; 65% spoken) | [16-05 45:25–47:58](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Returning viewers see the full video again | Shorter returning-visitor video with a real seeking bar, earlier CTA and clincher ([47:58–48:28](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) |
| B15 | Geo | US ~4x Africa; EU ~30% above North America; Brazil/Singapore low engagement but not worst conversion | [16-05 08:03–11:01](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md) | Judging a mixed-geo VSL on blended numbers | Segment by geo; weigh engagement less for Brazil/Singapore |

### Diagnosis worksheet (from the 16-05 lesson page, derived)
```text
Funnel type: [straight sale | book-a-call | upsell]  Traffic: [paid | email | affiliate | organic]  Device mix: __
Conversion __% vs 1.78% (book-a-call ~8%)
Engagement at 2 min __% (33%) | at CTA __% (28%) | at end __% (3%)
Unmute rate __% (40%) | avg unmute time __ s (7)
Autoplay thumbnail set? Y/N
Conversions at end of video __% (47%)
VSL length __ min | CTA drop at __% of video (best 30%)
Returning visitors __% | separate returning-visitor video? Y/N
Upsell seeking bar? Y/N
→ First failing row: __  → Fix: __  → Test: lead variant | CTA timing | cut-down | player change
```

### Conflicts to hold in mind
| Topic | Position A | Position B | Agent default |
|---|---|---|---|
| Where the first CTA goes | Classic close: build value, then first CTA after price reveal deep in the close; close is 25-35% of the VSL ([04-06](../lessons/04-06-vsl-closes.md); [04-05 20:08–20:37](../lessons/04-05-vsl-product-buildup-and-reveal.md)) | Best-converting VSLs drop the CTA at 30% of the video; a nine-figure brand drops it at 30 s (guest claim, [16-05 36:12–42:35](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)); Patrick: "I don't know how to balance those" ([57:27–57:54](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) | Write the classic structure; test an earlier button drop below the video as a page-level variant; judge on revenue per visitor and LTV, not conversion alone |
| Long-form length | Long Form generator: 25-60 min ([06-01](../lessons/06-01-claude-vsl-projects-setup-overview.md)) | Straight sale worst at 45 min; ~1 hour "drop off a cliff" ([16-05 35:17–36:42](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) | 20-35 min target for straight sale; longer only where the niche average is longer and a test is planned |
| What to do below 33% at 2 min | Deck: "replace the first 2 minutes" (slides 32-34) | Spoken: split-test leads, but "I wouldn't necessarily focus on your lead" about a 45% performer ([16-05 20:07–21:00](../lessons/16-05-vsl-benchmarks-data-and-best-practices-with-patrick-stiles.md)) | Below 33%: test new leads over the same body; above 33%: leave the lead and work the B4/B5 stretches |

## Related
- [LLM output claim audit](llm-output-claim-audit.md) · [Funnel audit](funnel-audit.md) · [Classic VSL structure](../concepts/classic-vsl-structure.md) · [Modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md) · [Hook generation system](../frameworks/hook-generation-system.md) · [Benchmarks library](../libraries/benchmarks.md)
