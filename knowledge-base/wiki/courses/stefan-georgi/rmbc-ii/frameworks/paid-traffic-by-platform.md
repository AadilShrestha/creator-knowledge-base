---
title: "Paid Traffic by Platform (Meta, native, Google, TikTok)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi (Meta); guests Dynh Nguyen (native), David O'Connell (Google), Max Finn (TikTok)"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-01-meta-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-02-native-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-03-google-ads.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-04-tiktok-ads.md
tags: [paid-traffic, meta-ads, native-ads, google-ads, tiktok-ads, channel-selection, ad-library-research, creative-testing, awareness]
updated: 2026-11-02
---

# Paid Traffic by Platform
> Run the same pre-writing diagnosis on every channel (objective, awareness, destination, format, winner commonalities), then apply the channel's own mechanics: Meta sells the click and tests creative against a fixed caption; native buys intent from a 55+ reader and needs a pre-sell page; Google maps campaign type to awareness; TikTok runs a weekly 4+ creative batch built from modular scenes.

## 🤖 Agent use
- **Use when:** choosing a paid channel for an offer; writing or briefing ads for Meta, native (Taboola/Outbrain/MGID), Google (Search, Shopping, Demand Gen, PMax) or TikTok; planning channel-specific research and tests.
- **Inputs → outputs:** offer, price, product type (physical / info / service / lead gen), audience age, awareness stage, existing pages (advertorial, VSL, PDP, registration), real customer language → channel choice + per-channel ad brief + destination page + test plan.
- **Rules:**
  - **DO** fix assets and journey before the ad: "an ad will never exist in a vacuum"; "You can't talk about ads without assets." [12-01 01:02](../lessons/12-01-meta-ads.md)
  - **DO** expect testing to decide: "You can't get around testing"; "You could sell the same product or service using five different funnel formats." [12-01 52:19](../lessons/12-01-meta-ads.md)
  - **DO** match destination to what the ad revealed: product shown → product page; product hidden → advertorial/VSL. "A blind VSL is basically never going to talk to product aware or most aware." [12-01 39:15–39:43](../lessons/12-01-meta-ads.md)
  - **DO** copy customer words from winning ads, so it reads as "a user talking to a user" (guest claim, Dynh Nguyen). [12-02 v3 03:13–03:43](../lessons/12-02-native-ads.md)
  - **DON'T** clone a spy-tool #1 or competitor ad one-to-one; filter for real paid winners and copy structure only (guest claims, Max Finn, Dynh Nguyen). [12-04 v3 02:21–04:42](../lessons/12-04-tiktok-ads.md), [12-02 v3 00:00](../lessons/12-02-native-ads.md)
  - **DON'T** present AI avatars as real customers with personal results (derived; repo rule 2). [12-04 v4 06:41–07:10](../lessons/12-04-tiktok-ads.md)
  - **DON'T** reuse any course example claim (health, income, sales counts, "doctors shocked", same-day timers). See [compliance red flags](../concepts/compliance-red-flags.md).
  - **IF** Meta account structure, budgets or kill rules are needed **THEN** use Evolve Start Here [campaign structure 3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md) and [scaling rules](../../../evolve/start-here/frameworks/scaling-rules.md); RMBC gives none (Stefan's own note: [12-01 Related](../lessons/12-01-meta-ads.md)).
- **See also:** [sell the click](../concepts/sell-the-click.md) · [ad-to-page journey](../concepts/ad-to-page-journey.md) · [product-market awareness](../concepts/product-market-awareness.md) · [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md) · [hook generation system](hook-generation-system.md) · [advertorial build](advertorial-build.md) · [pdp-build](pdp-build.md) · [prompts library](../libraries/prompts.md) · [benchmarks](../libraries/benchmarks.md) · shared [native advertising](../../../../concepts/native-advertising.md) · [creative testing system](../../../../frameworks/creative-testing-system.md) · [competitor ad teardown playbook](../../../../playbooks/competitor-ad-teardown.md)

## Step 0. Universal pre-writing diagnosis (all platforms)
- **Input:** the ad (ours or a competitor's) or the offer.
- **Output:** five filled answers. Stefan's doc checklist [12-01 03:22–56:19](../lessons/12-01-meta-ads.md):
```text
Meta ad analysis
Overarching: You can't talk about ads without assets. You can't get around testing.
1. What is the Objective? Acquire new customers / Generate new leads / Sell the solution / Sell the click / Increase brand and product awareness
2. What is the Product/Market Awareness Level? Unaware / Problem aware / Solution aware / Product aware / Most aware
3. Where do we send people? Advertorial / VSL / long PDP / short PDP / Brand building and awareness / Registration-signup page
4. What is the Format? Ultra short video / Short video / Medium video / Long video / Static
5. Commonalities? Curiosity / Visuals / Education / Emotional / Social proof (UGC, testimonials, etc.) / ???
```
- "Understanding the purpose is more important, I think, in a way than the copy." [12-01 56:19](../lessons/12-01-meta-ads.md)
- **IF** the destination page does the selling (advertorial, long PDP) **THEN** the ad only sells the click: "it's a lot easier to sell the click than it is to sell the prospect." [12-01 03:22](../lessons/12-01-meta-ads.md) **IF** the page is short **THEN** the video must do the selling [12-01 23:32](../lessons/12-01-meta-ads.md).

## Platform comparison

| Dimension | Meta (Stefan) | Native (Dynh Nguyen, guest) | Google (David O'Connell, guest) | TikTok (Max Finn, guest) |
|---|---|---|---|---|
| User state | Fast scrolling, interrupted | "Arrive with a certain intent and time"; reading editorial [12-02 v2 00:31–01:31](../lessons/12-02-native-ads.md) | Search: declared intent; Demand Gen: interrupted [12-03 v2 00:31, v3 09:46](../lessons/12-03-google-ads.md) | Fast scrolling; first 3 s decide [12-04 v7 03:19](../lessons/12-04-tiktok-ads.md) |
| Targeting | Platform audiences (structure from Evolve) | "No targeting, Ads will have to do the job" [12-02 doc](../lessons/12-02-native-ads.md) | Keywords (Search), feed (Shopping), audiences (Demand Gen), AI signals (PMax) | Broad winning audience as control [12-04 v5 04:14](../lessons/12-04-tiktok-ads.md) |
| Audience | Broad | ~55+, homeowners [12-02 v2 02:28](../lessons/12-02-native-ads.md) | ">90% of internet users" (guest claim) [12-03 v1 00:55](../lessons/12-03-google-ads.md) | Mobile short-video users |
| Default destination | Depends on reveal: advertorial / VSL / PDP / registration | Advertorial or jump page "for 99% of offers" [12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md) | Page matching keyword tier; Shopping needs approved product page [12-03 v4 02:30](../lessons/12-03-google-ads.md) | TikTok Shop / PDP / lead form; soft pitch [12-04 v7 10:00](../lessons/12-04-tiktok-ads.md) |
| Main creative lever | Image, video hook (3–10 s), thumbnail with caption fixed [12-01 06:36, 12:30](../lessons/12-01-meta-ads.md) | Odd "organic" image + customer keyword [12-02 v3 05:54, 15:40](../lessons/12-02-native-ads.md) | Query match (Search); thumbnail/big text (Demand Gen); feed title/image (Shopping) | Hook stack + modular scenes [12-04 v6, v7](../lessons/12-04-tiktok-ads.md) |
| Copy weight | Captions "important, but… not crazy" [12-01 v2 00:32](../lessons/12-01-meta-ads.md) | Page copy carries the sale; readers "will read the whole page" [12-02 v3 23:38](../lessons/12-02-native-ads.md) | 30-char headlines / 90-char descriptions; one message per tier | Spoken script + overlays |
| Research tool | Meta Ad Library (repetition, "N ads use this creative") [12-01 21:50, 31:24](../lessons/12-01-meta-ads.md) | Anstrex (gravity / ad strength), AdPlexity, tracker params [12-02 v3 00:41–02:43](../lessons/12-02-native-ads.md) | Live SERP, YouTube feed, Adbeat [12-03 v2 09:42, v3 27:36](../lessons/12-03-google-ads.md) | Kalodata, The Daily Virals, FastMoss, Foreplay [12-04 v3](../lessons/12-04-tiktok-ads.md) |
| Key metric named | Not given (use Evolve KPIs) | High CPM from high CTR + low CPC; landing-page CTR [12-02 v2 09:02](../lessons/12-02-native-ads.md) | CTR → position and CPC; ROAS vs volume by type [12-03 v1 06:08, v2 10:40](../lessons/12-03-google-ads.md) | Cost per result vs baseline; hit rate 1 in 4 [12-04 v5 03:19–06:38](../lessons/12-04-tiktok-ads.md) |
| Test unit | One variable vs fixed caption | 50/50 split per publisher via tracker [12-02 v2 06:37](../lessons/12-02-native-ads.md) | Per keyword group / asset | Weekly batch, one ad group per batch [12-04 v5 04:14](../lessons/12-04-tiktok-ads.md) |
| Best fit (derived) | Most DTC offers; statics for aware buyers | Older-audience health, gadgets, lead gen | Aware buyers (Search/Shopping); cold volume (Demand Gen) | Volume UGC-style creative, TikTok Shop products |

All guest figures are guest claims with no data shown in the files.

## A. Meta (Stefan Georgi)

### A1. Research the Ad Library
- **Input:** competitor brand names. **Output:** grouped ads + five-question sheet per ad.
1. Ad Library, US, All ads, Active; search the brand [12-01 Steps A](../lessons/12-01-meta-ads.md).
2. Group by shared caption and shared creative; note what is constant and what varies (image, hook, thumbnail, video length, caption length).
3. Read caption, watch one video, click through; record page type and length.
4. Fill Step 0.
5. Save captions to a swipe file [12-01 21:09, 49:05](../lessons/12-01-meta-ads.md).
- Winner signal (instructor inference): same hook repeated over weeks [12-01 21:50](../lessons/12-01-meta-ads.md); "N ads use this creative and text" label [12-01 31:24](../lessons/12-01-meta-ads.md). Treat as a hint, not proof; Evolve defines winners from own-account data ([winning-ad labels](../../../evolve/start-here/concepts/winning-ad-labels.md)).

### A2. Map ad to destination
| IF the ad is | THEN objective | Destination | Source |
|---|---|---|---|
| Static, short/no caption | Sell the click | Long advertorial | [12-01 03:22–07:11](../lessons/12-01-meta-ads.md) |
| Short video, product revealed | Sell solution + click | Product-aware advertorial or PDP | [12-01 10:23](../lessons/12-01-meta-ads.md) |
| 12–15 min in-feed VSL | Sell the solution | Short/medium PDP (maybe via quiz) | [12-01 23:32](../lessons/12-01-meta-ads.md) |
| Static results story, aware buyer | Sell + brand | Long PDP / bundle page | [12-01 25:48–27:34](../lessons/12-01-meta-ads.md) |
| Curiosity video, product hidden | Sell the click | VSL | [12-01 38:37–40:17](../lessons/12-01-meta-ads.md) |
| Educational reel (lead gen) | Leads | Short registration page | [12-01 40:59–48:20](../lessons/12-01-meta-ads.md) |
| High-volume UGC | Sell + frequency-built awareness | Basic PDP | [12-01 53:15–55:48](../lessons/12-01-meta-ads.md) |

### A3. Write captions (Claude Project)
- **Input:** 8–10 real swipe captions from our niche + our hooks. **Output:** caption set.
- Project instruction (verbatim, doc "Claude Captions Generator Setup") [12-01 v2 00:00](../lessons/12-01-meta-ads.md):
```text
I'm going to give you several examples of meta ad captions in your knowledge base. You'll use these and other knowledge you have about meta ad captions to generate new ad captions based on instructions I put in your chat interface.
```
- Chat prompts (reconstructed from speech) [12-01 v2 00:32–02:04](../lessons/12-01-meta-ads.md):
```text
Can you do some ad captions for [eye serum product]? Benefits plus a CTA to save 57% off. And then I can run my link.

Great, thank you. Now can you do some really short ones that are just a few lines and sell the click.
```
- **IF** no hooks exist yet **THEN** run [hook generation system](hook-generation-system.md) first and add hooks to the project [12-01 v2 01:12, 04:00](../lessons/12-01-meta-ads.md).
- Stefan's own stance: "I don't use this personally"; any LLM writes acceptable captions [12-01 v2 00:32](../lessons/12-01-meta-ads.md). Put effort into creative variants instead.

### A4. Test creative against a fixed caption
- Hold caption, vary one element: image ("same copy, different images will often have very different results") [12-01 06:36](../lessons/12-01-meta-ads.md); video hook (first 3–10 s) and thumbnail [12-01 12:30](../lessons/12-01-meta-ads.md); video length (Nooro ran 2/4/15/16 min, ~15 min "sweet spot", observed) [12-01 30:37](../lessons/12-01-meta-ads.md); caption length (Calvin Tran) [12-01 45:33–48:20](../lessons/12-01-meta-ads.md).
- Keep the CTA on screen after the video ends [12-01 34:38](../lessons/12-01-meta-ads.md).
- Mechanics: [modular creative and hook swaps](../concepts/modular-creative-and-hook-swaps.md).

### A5. Account structure, budgets, kill rules: use Evolve
RMBC gives no Meta campaign structure, budget or kill rule. Use:
- [Campaign structure 3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md): one broad Sales CBO; each concept = one ad set of 3 ads × 2 primary texts × 2 headlines; support campaigns (page tests, zombie, ABO, raw content, promo) by spend.
- [Scaling rules](../../../evolve/start-here/frameworks/scaling-rules.md): +20% after 48–72 h at target with >60% click-based purchases; −20% below breakeven; ad-set-level kill table.
- [KPIs and columns](../../../evolve/start-here/frameworks/kpis-and-columns.md) and [KPI thresholds](../../../evolve/start-here/libraries/kpi-thresholds.md).
- Fit: Evolve's 3:2:2 holds the same two primary texts across a concept's three ads, which matches Stefan's "same caption, varied creative" pattern [12-01 Related](../lessons/12-01-meta-ads.md).

### A6. Meta failure modes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| High CTR, low CVR | Blind VSL after product reveal; awareness mismatch | Send product-reveal ads to PDP | [12-01 39:15](../lessons/12-01-meta-ads.md) |
| Can't tell what worked | Caption and creative changed together | One variable per test | [12-01 06:36](../lessons/12-01-meta-ads.md) |
| Cold CPA poor on aware-style static | Static results story on cold traffic | Use for retargeting / aware; cold → pre-sell | [12-01 27:02–27:34](../lessons/12-01-meta-ads.md) |
| Biz-op ads flagged | Social proof / income claims | Limit social proof "for FTC reasons" (Stefan; verify with counsel) | [12-01 43:19](../lessons/12-01-meta-ads.md) |

## B. Native (Dynh Nguyen, guest)

### B1. Offer-fit gate
- **Input:** offer, audience age. **Output:** go / no-go.
- **IF** the offer does not resonate with ~55+ readers **THEN** no-go: a 30-day handstand course "won't work"; a blood-sugar VSL "would work very, very well" (guest claim) [12-02 v2 02:28, 04:32–05:33](../lessons/12-02-native-ads.md).
- Strong categories: diabetes/blood sugar, vision, weight loss, prostate, toenail fungus (health VSL); insoles, knee sleeves, acupressure clips (gadgets); solar, Medicare, bathroom remodel (lead gen) [12-02 v3 04:14, 14:10, 23:38](../lessons/12-02-native-ads.md). Health verticals carry the highest claim risk: structure/function wording, no disease claims.

### B2. Pick the funnel and CTR target

| Vertical | Ad | Page 1 | Page 2 | Landing-page CTR target (guest) | Source |
|---|---|---|---|---|---|
| Health VSL | Odd organic image + curiosity headline | Jump page: play image + 3–5 paragraphs | ~40-min VSL, add-to-cart ~30:00 | 40–50% | [12-02 v3 04:14–07:21, 13:05](../lessons/12-02-native-ads.md) |
| Ecom gadget | Product or odd-trick image + customer keyword | Mid/long story advertorial, late CTA | PDP / checkout | ~25–30% (said 25% and 30%) | [12-02 v3 14:10–23:38, 32:13](../lessons/12-02-native-ads.md) |
| Lead gen | Offer/benefit image | Short advertorial ~5 paragraphs + state/zip selector | Form | ~30%; CTA can sit early | [12-02 v3 24:07–25:59](../lessons/12-02-native-ads.md) |

- **IF** commoditised product whose buyers already know the solution (guest example: Ozempic) **THEN** direct to product page is the exception [12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md).
- Page build: [advertorial build](advertorial-build.md). Saved swipe pages (socks long/mid-form, solar, diabetes VSL jump pages) are structure only; their proof is invented [12-02 Examples](../lessons/12-02-native-ads.md).

### B3. Spy twice a week
1. Anstrex first, plus one more tool ("tools won't cover every single ad") [12-02 v3 00:41–01:11](../lessons/12-02-native-ads.md).
2. Sort by **gravity** for what runs now; **ad strength** for last year's winners [12-02 v3 01:40–02:43](../lessons/12-02-native-ads.md).
3. Search by problem and by tracker parameter to find affiliate funnels: `hop=`, `voluumdata=`, `rdt=`, `sub1=`, `rtcd=`, `campaign_id=` [12-02 doc, v3 27:00–28:07](../lessons/12-02-native-ads.md).
4. Log customer words ("bionic", "bone-to-bone", "itchy"), image type, page length, CTA position [12-02 v3 03:13, 15:40, 28:36](../lessons/12-02-native-ads.md).
5. Write the mechanism, not a copy.

### B4. Launch and buy
- Link tracker (RedTrack, Voluum, ClickMagick) for redirects and 50/50 per-publisher splits [12-02 v2 05:33–07:04](../lessons/12-02-native-ads.md). **DON'T** import tracker redirects to Meta/Google/TikTok without a policy check (guest says redirects there risk bans) [12-02 v2 05:33](../lessons/12-02-native-ads.md).
- Ask the rep for category benchmarks (CPM, CTR, CPC, CPA by device) and a 100–150 publisher start list [12-02 v3 30:35–32:43](../lessons/12-02-native-ads.md).
- **IF** US on Taboola **THEN** pause mail placements (Yahoo/AT&T Mail), block push and gaming, start with below-article format [12-02 v3 29:04–30:06](../lessons/12-02-native-ads.md).
- Optimise for "high CPMs with high CTRs and low CPCs" ("the golden formula") [12-02 v2 09:02–10:00](../lessons/12-02-native-ads.md); raise bids per publisher from tracker data [12-02 v2 10:00](../lessons/12-02-native-ads.md).
- **Use native as a lab:** test angle + page on native, then port to another source with CTR and CVR data in hand [12-02 v2 07:04–07:37](../lessons/12-02-native-ads.md).

### B5. Native failure modes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Ads rejected | Same-day countdown timers | Real end date or none ("bigger native traffic sources don't allow that anymore") | [12-02 v3 19:00](../lessons/12-02-native-ads.md) |
| Low spend / volume | Low CTR → low CPM | Clickier organic image; customer words | [12-02 v2 09:02](../lessons/12-02-native-ads.md) |
| Junk traffic | Mail, push, gaming placements | Block at launch | [12-02 v3 29:04](../lessons/12-02-native-ads.md) |
| Low LP CTR on long page | CTA too early (unqualified clicks) or weak story | CTA late on mid/long pages | [12-02 v3 21:05](../lessons/12-02-native-ads.md) |
| Budget won't spend | Limited inventory | Expect it; "quite rare that you would spend that 100k" a day | [12-02 v2 07:37–08:35](../lessons/12-02-native-ads.md) |

## C. Google (David O'Connell, guest)

### C1. Pick campaign type by awareness
| Awareness | Campaign types | Trade-off | Source |
|---|---|---|---|
| Most aware, product aware | Search, Shopping, PMax | High ROAS, limited volume | [12-03 v1 06:08](../lessons/12-03-google-ads.md) |
| Solution, problem, unaware | Demand Gen, PMax | Very high volume | [12-03 v1 07:01](../lessons/12-03-google-ads.md) |

- Spend share across the guest's accounts since April 2025: Demand Gen 58%, PMax 27%, Search 11%, Shopping 4% (guest claim) [12-03 v1 07:54](../lessons/12-03-google-ads.md).
- **IF** info product or service **THEN** no Shopping (physical products only; page must be approved; a VSL-only page is not) [12-03 v4 02:30–03:27](../lessons/12-03-google-ads.md).
- **Order:** run Search / Shopping / Demand Gen, find winners, then build PMax from them; "don't start with performance max ads as your first ad type" [12-03 v5 05:52–06:51](../lessons/12-03-google-ads.md).

### C2. Search ads
1. List keyword groups by tier: brand / product-aware / solution-aware / problem-aware [12-03 v2 04:21](../lessons/12-03-google-ads.md).
2. Type one sample query per group into google.com; read every sponsored result [12-03 v2 09:42, 11:42](../lessons/12-03-google-ads.md).
3. Log each competitor's offer (price, speed, authority, risk reversal, free trial).
4. Write 30-char headlines / 90-char descriptions that answer exactly that query plus one differentiator the SERP lacks: "if they came to you and they're looking for bananas, give them bananas." [12-03 v2 09:42](../lessons/12-03-google-ads.md)
5. Strong CTA + extensions (higher CTR = higher position, lower CPC) [12-03 v2 10:40](../lessons/12-03-google-ads.md).
6. Dynamic keyword insertion only where the product fits the query [12-03 v2 09:42](../lessons/12-03-google-ads.md).
- Tier strategies (slide): brand = official + price/offer; product-aware = proof, fit, testimonials, guarantee; solution-aware = educate + introduce as superior; problem-aware = empathise, agitate, introduce [12-03 v2 04:21–08:45](../lessons/12-03-google-ads.md).
- Worked differentiation (guitar lessons): competitors offered "at home", "$20/hr", "free first lesson"; guest's ad stacks speed + free first lesson + named authority + "learn in 30 days or you won't pay" [12-03 v2 13:12–14:59](../lessons/12-03-google-ads.md). Only claim what we can deliver.

### C3. Demand Gen ads
1. One audience (in-market, custom segment, lookalike, placement) and its stage [12-03 v3 02:23–04:49](../lessons/12-03-google-ads.md).
2. Lead with image OR video, whichever we are stronger at; add the other later [12-03 v3 08:52–09:46](../lessons/12-03-google-ads.md).
3. "You must interrupt!": thumbnail/image with big bright text, a face, intrigue (in-feed often doesn't autoplay) [12-03 v3 09:46–12:38](../lessons/12-03-google-ads.md).
4. Make no-text variants for placements that reject text [12-03 v3 12:38](../lessons/12-03-google-ads.md).
5. Upload square, wide and tall sizes; fill all 5 headlines (40 c) and 5 descriptions (90 c) with curiosity/specificity ("Stop yo-yo dieting for good" vs "Try our plan") [12-03 v3 13:35](../lessons/12-03-google-ads.md).
6. Check the ad against the organic thumbnails beside it in the feed [12-03 v3 19:03–20:57](../lessons/12-03-google-ads.md).
7. Iterate the winner; "the volume can really explode" (guest claim) [12-03 v3 13:35–14:30](../lessons/12-03-google-ads.md).
- **DON'T** load weak headlines; low performers "will get some traffic" and lower results [12-03 v3 05:48–06:19](../lessons/12-03-google-ads.md).

### C4. Shopping and PMax
- Merchant Center; keyword-relevant titles; test title styles ("Ray-Ban Aviators" / "Polarized Ray-Ban Aviators" / "Best Aviators of 2025") and image backgrounds (white vs bright colour) [12-03 v4 06:12–10:38](../lessons/12-03-google-ads.md). Verify the keyword-stuffing tip against Merchant Center policy (lesson flag).
- Physical products: add the feed to PMax as well ("you will always see a big boost", guest claim) [12-03 v5 01:30–02:27](../lessons/12-03-google-ads.md).
- Guest says before/after is allowed on Google where Meta blocks it; no policy citation given; check policy [12-03 v3 31:26](../lessons/12-03-google-ads.md).

### C5. Google failure modes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Shopping disapproved | Info product or VSL page | Physical product page with price + buy front and centre | [12-03 v4 02:30](../lessons/12-03-google-ads.md) |
| Demand Gen ad shows blank background / odd label | Text-only assets; unedited name field | Upload images in all sizes; check every field | [12-03 v3 18:07–19:03, 22:51](../lessons/12-03-google-ads.md) |
| PMax underperforms | Started cold with unproven assets | Port proven winners only | [12-03 v5 05:52](../lessons/12-03-google-ads.md) |
| Search CTR low | Generic copy vs SERP | Differentiator the SERP lacks | [12-03 v2 13:12–14:59](../lessons/12-03-google-ads.md) |

## D. TikTok (Max Finn, guest; "fundamental principles" for any short-video channel)

### D1. Avatar deep research (once per brand)
- **Input:** brand URL. **Output:** research outputs from 3–4 models in one brand project.
- Run the "Ultimate Universal Target Avatar Deep Research Prompt" (83 questions + 5 business-specific) in Claude Deep Research, Gemini Deep Research, Grok and Perplexity; keep all outputs; score pains and core wounds by hand [12-04 v2 00:56–07:51](../lessons/12-04-tiktok-ads.md). Opening (verbatim; full text in [12-04 Prompts](../lessons/12-04-tiktok-ads.md) and [prompts library](../libraries/prompts.md)):
```text
Ultimate Universal Target Avatar Deep Research Prompt

CONTEXT: I need you to analyze [WEBSITE URL] and conduct comprehensive target avatar research for this business. First, visit their website and understand their product/service, value proposition, target market, pricing, and unique positioning. Then provide detailed answers about their ideal target avatar so I can create the most profitable ads possible.

YOUR MISSION: After analyzing the business website, answer ALL of the following questions with specific, actionable insights about their ideal customer avatar:
```
- RMBC's own research stage is broader: [deep research workflow](deep-research-workflow.md) and [unified research document](../concepts/unified-research-document.md). **Agent default (derived):** if a unified research doc exists, use it; run the avatar prompt only to fill gaps, and treat LLM "insights" as hypotheses until matched to real reviews/comments.

### D2. Creative research with filters
1. Kalodata Video & Ad section; check the 30-day revenue trend (reject one-day spikes) [12-04 v3 02:21–03:19](../lessons/12-04-tiktok-ads.md).
2. Set a minimum Ad View Ratio; require at least half the views paid [12-04 v3 03:19–04:14](../lessons/12-04-tiktok-ads.md).
3. Cap creators at <50k followers [12-04 v3 03:47](../lessons/12-04-tiktok-ads.md).
4. Category granular but not ~10 videos [12-04 v3 04:42–05:11](../lessons/12-04-tiktok-ads.md).
5. Per video log: opening words, visual, overlays, POV vs third person, people, length, tone, speed, raw vs polished, humor vs serious; then metrics [12-04 v3 05:11–06:05](../lessons/12-04-tiktok-ads.md).
- Failure mode: grabbing the unfiltered #1 video, copying it, and it bombs: "That's why." [12-04 v3 04:14–04:42](../lessons/12-04-tiktok-ads.md)

### D3. Build modular scenes

| Scene | Content | Swap ideas |
|---|---|---|
| 1 Hook | Text + visual + audio hook stack ("three shots instead of one") | Overlay, visual, line |
| 2 Problem | Show the problem | Different framing |
| 3 Alternative solution | What people try that fails | Different alternative |
| 4 Our solution | Why ours | Different features/benefits |
| 5 Social proof | Real customers, real authority | Different proof |
| 6 Offer | Channel deal | Free shipping vs discount vs bonus stack |

Source: [12-04 v6 01:27–04:21, v7 03:49–04:45](../lessons/12-04-tiktok-ads.md). "Just one type of framework" [v6 03:23].
- Breakdown principles: third-party framing ("I saw all these five-star reviews") beats brand bragging; visual change; belief-flip open loop; re-hook mid-video; unexpected visuals; soft pitch; congruent setting; emotional first, logic block after first CTA [12-04 v7 05:14–11:29, BD4 05:00–06:01](../lessons/12-04-tiktok-ads.md).
- Length: "can you get the mission done in that timeframe?"; many top ads 30–90 s; 15–20 s for a $20 gadget; 2.5–3.5 min for high-ticket (observed) [12-04 v7 01:52–03:19](../lessons/12-04-tiktok-ads.md).

### D4. (Optional) AI concept tests
- Veo 3 / Creatify to test hooks, angles, looks before paying a creator; then brief the winner to a real creator [12-04 v4 06:12–07:10, 11:04–12:23](../lessons/12-04-tiktok-ads.md).
- **Hard stop:** no AI person presented as a customer, patient or reviewer with a personal result in a published ad (derived; repo rule 2). The course's Vlog generator asks for "genuine discoveries or recommendations" from a fictitious vlogger [12-04 Prompts §2](../lessons/12-04-tiktok-ads.md): concept test only.

### D5. Weekly test loop
```text
Every week (fixed day, e.g. every Monday):
[ ] 4+ new creatives launched                                   [v5 03:19-03:48]
[ ] New ad group per batch, on the winning audience             [v5 04:14-04:41]
[ ] 1 creative per ad group, or near-identical variants only    [v5 04:41-06:09]
[ ] Early stage ~75-80% net-new angles; later ~50/50 with iterations   [v6 07:39-08:38]
[ ] Winner: raise budget in place AND add to the Smart+ campaign       [v5 06:38-07:36]
[ ] Iterate the winner by swapping ONE scene (hook / problem / alternative solution / proof / offer)   [v6 04:21-04:49]
[ ] Feed what iterations taught (formats, people, styles) into the next net-new batch   [v6 08:38-09:34]
```
(verbatim from [12-04 Prompts §4](../lessons/12-04-tiktok-ads.md))
- Hit-rate target: 1 winner per 4 (25–33%); starting out 1 in 8–10 (guest claim) [12-04 v5 03:19–04:14](../lessons/12-04-tiktok-ads.md).
- Winner = outlier vs own baseline cost per result (his baseline "in the teens" per lead; outlier "$2, $3") [12-04 v5 06:09–06:38](../lessons/12-04-tiktok-ads.md).
- **DON'T** turn a winner off or leave it untouched in testing [12-04 v5 06:38–07:36](../lessons/12-04-tiktok-ads.md).

### D6. TikTok failure modes
| Symptom | Cause | Fix | Source |
|---|---|---|---|
| Copied "winner" bombs | Viral fluke or mega-creator | D2 filters | [12-04 v3 04:14](../lessons/12-04-tiktok-ads.md) |
| Concepts under-spent in test | Different angles in one ad group | One creative per ad group | [12-04 v5 04:41–06:09](../lessons/12-04-tiktok-ads.md) |
| Winner fatigues, no follow-up | Monolithic creative | Modular scene swaps | [12-04 v6 00:00–01:27](../lessons/12-04-tiktok-ads.md) |
| Viewers distrust | Brand bragging, hard sell | Third-party framing; soft pitch | [12-04 v7 05:14, 10:00](../lessons/12-04-tiktok-ads.md) |
| Boring category, low hold | Talking head only | Props, POV, cuts | [12-04 v7 05:43, BD4 00:00–02:20](../lessons/12-04-tiktok-ads.md) |

## Decision: which channel first (derived)
- **IF** physical product, aware demand exists (people search the category) **THEN** Google Search + Shopping first for ROAS, then Demand Gen/PMax for volume.
- **IF** older-skewing health, gadget or lead-gen offer with a pre-sell page **THEN** native, and use it as a page/angle lab.
- **IF** volume UGC-style creative is cheap to produce and the product demos well **THEN** TikTok (and Meta Reels) with the weekly batch loop.
- **IF** general DTC with advertorial/PDP assets **THEN** Meta with Evolve 3:2:2 structure.
- Channel choice must also pass [funnel selection matrix](../concepts/funnel-selection-matrix.md) and [funnel economics](../concepts/funnel-economics.md).

## Where it's taught
- [12-01 Meta Ads](../lessons/12-01-meta-ads.md): rules [00:00–06:36]; five questions [03:22–56:19]; Odorless Cat [02:15–15:28]; Miami MD [16:19–24:07]; Happy Mammoth [24:34–30:00]; Nooro [29:59–31:24]; BugMD [31:24–36:49]; AKKA/Emma [36:49–40:17]; biz-op lead gen [40:17–52:19]; David Protein [52:19–56:19]; caption project [v2 00:00–04:00].
- [12-02 Native Ads](../lessons/12-02-native-ads.md): why native [v2 00:31–03:01]; offer fit [v2 03:01–05:33]; trackers [v2 05:33–07:37]; CPM logic [v2 07:37–10:54]; Anstrex [v3 00:00–03:43]; health VSL [v3 04:14–14:10]; ecom gadget [v3 14:10–23:38]; lead gen [v3 23:38–26:00]; hygiene and benchmarks [v3 29:04–32:43].
- [12-03 Google Ads](../lessons/12-03-google-ads.md): types and 2025 change [v1]; Search [v2]; Demand Gen [v3]; Shopping [v4]; PMax [v5].
- [12-04 TikTok Ads](../lessons/12-04-tiktok-ads.md): research [v2–v3]; AIGC [v4]; testing [v5]; modular iteration [v6]; breakdowns [v7–v13, BD4].

## Cross-course notes
- **Meta structure:** RMBC silent; Evolve [3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md) + [scaling rules](../../../evolve/start-here/frameworks/scaling-rules.md) are the default.
- **Test structure conflict:** TikTok guest runs one ad group per weekly batch, one creative per ad group (or near-identical hook variants), winners ascended to Smart+ [12-04 v5 04:14–07:36](../lessons/12-04-tiktok-ads.md); Evolve tests each concept as one ad set of 3 ads × 2 texts × 2 headlines inside one broad CBO ([3:2:2](../../../evolve/start-here/frameworks/campaign-structure-322.md)). **Agent default:** Evolve 3:2:2 on Meta; the guest's batch structure on TikTok; on both, one concept per test unit and only near-identical variants grouped.
- **Winner definition:** Stefan reads Ad Library repetition as a winner hint; Evolve defines winners from own-account data ([winning-ad labels](../../../evolve/start-here/concepts/winning-ad-labels.md)). **Default:** library signals pick what to study; only our own data declares a winner.
- **Hooks:** Evolve [hooks](../../../evolve/copywriting/concepts/hooks.md) and the KB [creative testing system](../../../../frameworks/creative-testing-system.md) agree with Stefan and Max Finn on testing hooks against a fixed body.
- **Native:** the shared [native advertising](../../../../concepts/native-advertising.md) concept had no buyer-side material; 12-02 adds it.

## Related
[ad-to-page journey](../concepts/ad-to-page-journey.md) · [congruence](../concepts/congruence.md) · [hook generation system](hook-generation-system.md) · [cro-testing](cro-testing.md) · [hooks library](../libraries/hooks.md) · [ad teardowns library](../libraries/ad-teardowns.md) · [angles library](../libraries/angles.md)
