---
title: "Advertorial Build (RMBC II)"
type: framework
creator: stefan-georgi
course: rmbc-ii
instructor: "Stefan Georgi"
sources:
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-01-advertorials-overview-and-examples.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/09-02-claude-project-for-advertorials.md
  - knowledge-base/wiki/courses/stefan-georgi/rmbc-ii/lessons/12-02-native-ads.md
tags: [advertorial, pre-sell, claude-project, prompt-sequence, native-ads, meta-ads, congruence, swipe, compliance, framework]
updated: 2026-11-02
---

# Advertorial Build (RMBC II)
> Pick the journey from what the ad already revealed, then run a Claude Project loaded with varied real advertorials through hooks → outline → draft → shorter variant → claim audit, and ship one labelled pre-sell page per ad pain point.

## 🤖 Agent use
- **Use when:** a cold ad (Meta static/video, native) needs a pre-sell page before a PDP, VSL, checkout hybrid or lead form; you must write, swipe the structure of, shorten or audit an advertorial; you are setting up the advertorial Claude Project.
- **Inputs → outputs:** traffic source + the ad (or what it reveals) + destination page + price + offer source (brief, landing page, PDF, VSL script) + best-performing ad caption + real proof → journey decision and length band → 10 hooks → approved outline → full draft → ~50% shorter test variant → audited, labelled copy (optionally a deployed page).
- **Rules:**
  - **DO** decide length from what the ad already did. Teasing static → long story advertorial; a 1–2 min video that showed problem, product and mechanism → shorter, graphics-heavy page that names the product early. [09-01 36:42–38:00](../lessons/09-01-advertorials-overview-and-examples.md) [09-01 44:14–45:09](../lessons/09-01-advertorials-overview-and-examples.md)
  - **DO** build every advertorial from three ingredients: educational (UM and/or product), personal/emotional, curiosity. [09-01 11:01–11:35](../lessons/09-01-advertorials-overview-and-examples.md)
  - **DON'T** send a cold curiosity ad straight to a short PDP when the product needs belief: "Your CPA is going to be way too high. Your AOV is going to be way too low" (instructor claim). [09-01 07:45](../lessons/09-01-advertorials-overview-and-examples.md)
  - **DO** load the Project with real advertorials of mixed length (short, medium, long) and mixed niches; **DON'T** stack your own niche ("make it work harder"). [09-02 03:00–05:52](../lessons/09-02-claude-project-for-advertorials.md) [09-02 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** run Prompt 1 (10 hooks) → Prompt 2 (outline at a stated length) → Prompt 3 (write). Outline first, to catch a structure that "zigs and zags". [09-02 16:23–17:54](../lessons/09-02-claude-project-for-advertorials.md) [09-02 27:01–27:45](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** pick the hook that matches the angle already winning in the brand's ads and paste that ad caption into Prompt 2 for congruence. [09-02 22:27–27:01](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** check every number, guarantee length and offer term against the source page; Stefan caught a 90-day guarantee that should be 60. [09-02 30:24–30:55](../lessons/09-02-claude-project-for-advertorials.md) [09-02 49:05–49:51](../lessons/09-02-claude-project-for-advertorials.md)
  - **DO** read the draft as a third party ("dissociative state") and add the missing motive wherever a reader would ask "why would he do that?". [09-02 51:22–52:41](../lessons/09-02-claude-project-for-advertorials.md)
  - **DON'T** publish model-written testimonials, doctors, studies, stats or scarcity. Stefan calls them placeholders: "to be compliant, you would obviously want to put real testimonials". [09-02 38:01](../lessons/09-02-claude-project-for-advertorials.md)
  - **IF** the destination is a VSL **THEN** keep the advertorial short and image-led; **IF** it is a PDP **THEN** go longer and educate. [09-01 v2 31:23–33:26](../lessons/09-01-advertorials-overview-and-examples.md)
  - **IF** the ad is about one pain point and the product solves many **THEN** write one advertorial per pain point that ends on "it cleans other stuff too". [09-01 v2 26:07–27:24](../lessons/09-01-advertorials-overview-and-examples.md)
  - **DO** label the page "Advertorial"/"Advertisement". [09-01 27:15](../lessons/09-01-advertorials-overview-and-examples.md) [09-01 47:58](../lessons/09-01-advertorials-overview-and-examples.md)
- **See also:** [prompts library](../libraries/prompts.md) · [templates library](../libraries/templates.md) · [ad-to-page journey](../concepts/ad-to-page-journey.md) · [congruence](../concepts/congruence.md) · [composite vs swipe](../concepts/composite-vs-swipe.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [paid traffic by platform](paid-traffic-by-platform.md)

## What it is
An advertorial is the "interstitial" page between ad and offer. Stefan gives it four jobs: "do the legwork of selling a product or service", "sell the click" (to a VSL, PDP etc.), compliance (an in-between page), and ad-to-page congruence. [09-01 v2 00:00–00:33](../lessons/09-01-advertorials-overview-and-examples.md) The build has two halves:
1. **Journey and length decision** (09-01): what page, how long, which pain point, which destination.
2. **Generation loop** (09-02): a Claude Project whose knowledge base is varied real advertorials, driven by three short prompts plus "boss" edits. Stefan: "with AI, you're still the boss for now." [09-02 44:02](../lessons/09-02-claude-project-for-advertorials.md)

A quick alternative (09-01): paste one live advertorial, have Claude outline its structure, then write ours "that follows the same structure". [09-01 27:50–30:35](../lessons/09-01-advertorials-overview-and-examples.md)

## Inputs checklist
- [ ] Traffic source: Meta static, Meta video, native (Taboola/Outbrain-type news widgets).
- [ ] The ad itself, plus a note of what it already reveals: problem / product / mechanism / proof / price. [09-01 44:14–45:09](../lessons/09-01-advertorials-overview-and-examples.md)
- [ ] Destination: short PDP, PDP-checkout hybrid, VSL lander, lead form.
- [ ] Price point and bundle structure (AOV levers). [09-01 05:08–06:46](../lessons/09-01-advertorials-overview-and-examples.md)
- [ ] Offer source document: brief ([Brief 2.0](../concepts/brief-2-0.md) preferred), landing page copy, product PDF or VSL script. [09-02 16:23–17:28](../lessons/09-02-claude-project-for-advertorials.md)
- [ ] Best-performing ad caption/story from the brand. [09-02 26:24](../lessons/09-02-claude-project-for-advertorials.md)
- [ ] Mechanism (UMP/UMS) from the [unique mechanism](../concepts/unique-mechanism.md) work and research from the [unified research document](../concepts/unified-research-document.md).
- [ ] Real proof only: permissioned reviews and photos, verified review counts, substantiated claims, real guarantee terms, real stock/offer dates. Missing items get listed as `[VERIFY: …]`, not invented.
- [ ] 12–20 saved real advertorials (short/medium/long, mixed niches) for the Project knowledge base. [09-02 Steps](../lessons/09-02-claude-project-for-advertorials.md)

## Steps

### Step 1 — Choose the journey and length band
- **Input:** traffic source, the ad, destination, price.
- **Output:** one row from the [Decision points](#decision-points) table: advertorial yes/no, type (long story / short product-forward / interstitial offer / short VSL bridge / listicle), target length band.
- **Prompt:** none (decision step).
- **Tool/model:** none.
- **Length bands (course doc):** short 200–500 words, medium 500–1,000, long 1,000–2,000. Treat as guides: "These are guidelines, not like golden rules. Something could be 150 words, something could be 2,500." [09-01 19:00–19:33](../lessons/09-01-advertorials-overview-and-examples.md) The Clarifion long page that runs is about 2,900 words (derived count). [09-01 doc](../lessons/09-01-advertorials-overview-and-examples.md)
- **Check before moving on:** you can state in one line what the ad revealed and why this page length follows from it.

### Step 2 — Build (once) the advertorial Claude Project
- **Input:** 12–20 real advertorials saved as PDF/Google Doc with the original link (live pages get taken down). [09-02 03:32–04:35](../lessons/09-02-claude-project-for-advertorials.md)
- **Output:** a Project ("Advertorial Generation") with description = instructions, knowledge = varied advertorials. Stefan's has 14 PDFs: 6 short, 4 medium, 4 long, across ED, bladder, weight loss, eye bags, crepey skin, hearing aid, tinnitus, neck pillow, lash serum, anti-aging cream, home-shower lead gen. Nothing else is uploaded: no brief, no style guide. [09-02 Structured units](../lessons/09-02-claude-project-for-advertorials.md)
- **Prompt (Project description AND instructions, verbatim):**
```text
I will be giving you different sales pages, landing pages, product details, or relevant data points, and you will then be writing new advertorials based off the numerous examples that are in your knowledge base. What you'll want to do is analyze the structure of the various advertorial examples, and then synthesize that knowledge and use that same knowledge, along with your judgement, to produce new advertorials.
```
[09-02 01:33–02:29](../lessons/09-02-claude-project-for-advertorials.md) · also in [prompts library](../libraries/prompts.md)
- **Sourcing the swipe file:** open local-news sites in random cities, scroll to "From around the web" widgets, click through; use incognito or another browser because targeting follows your clicks; save with copy-paste or a full-page screenshot (Markup Hero). [09-02 12:46–15:51](../lessons/09-02-claude-project-for-advertorials.md) Native spy tools (Anstrex) are covered by the 12-02 guest (guest claim). [12-02 v3 00:41–03:43](../lessons/12-02-native-ads.md)
- **Tool/model:** Claude Projects; Claude Sonnet 4 on screen. [09-02 Key ideas](../lessons/09-02-claude-project-for-advertorials.md)
- **Why varied niches:** "the content is not as important as the structure or like the syntax." Abstract the skeleton (headline → stat → pain dimensionalised → simple solution found → watch-video CTA) and reuse it in any category. [09-02 05:52–11:15](../lessons/09-02-claude-project-for-advertorials.md)
- **Check before moving on:** at least 3 files per length band; no single niche is more than about a third of files (derived); saved copies, not bare links.

### Step 3 — Generate 10 hooks from the offer source
- **Input:** offer source attached (PDF of landing page, brief, VSL script).
- **Output:** 10 named advertorial hooks with headlines and rationale.
- **Prompt (template, verbatim; blanks are placeholders):**
```text
Here is a __Document Type____ for a ___Product Type____. Please analyze it, and then I want you to give me 10 potential hooks for advertorials we could write.
```
As typed in the demo (Norse landing page PDF attached):
```text
Here is landing page copy for a acne removing product. Please analyze it, and then I want you to give me 10 potential hooks for advertorials we could write.
```
[09-02 16:23–17:28](../lessons/09-02-claude-project-for-advertorials.md) [09-02 21:50–23:18](../lessons/09-02-claude-project-for-advertorials.md)
- **Tool/model:** the Step 2 Project.
- **Check before moving on:** (1) at least one hook matches the angle already winning in the brand's ads; (2) flag every hook whose headline carries an invented number or disease claim (the demo's "90% Clear in Just One Week" and "3X Faster Than Prescriptions" are model-invented and not on the source page) [09-02 Example B](../lessons/09-02-claude-project-for-advertorials.md).

### Step 4 — Outline at a stated length, with the winning-ad caption
- **Input:** chosen hook number, length band from Step 1, the brand's best ad caption.
- **Output:** a section-by-section outline with word targets.
- **Prompt (template, verbatim; the price sentence is optional):**
```text
Okay nice, let's go ahead and do #___ first. Can you write out an outline for a ____ length advertorial with that angle? One note is that I don't want to reveal the price, but rather say that readers can save XX%.
```
Congruence paragraph Stefan added before sending (verbatim, screen):
```text
One thing to bring up is that this type of story has worked really well in the brand's ads. I will copy and paste the ad caption here, so you can make the advertorial congruent with this story.

[PASTE THE BRAND'S WINNING AD CAPTION / STORY HERE]
```
[09-02 17:28](../lessons/09-02-claude-project-for-advertorials.md) [09-02 25:51–28:06](../lessons/09-02-claude-project-for-advertorials.md)
- **Agent addendum (derived, not a course asset; append for our brands):**
```text
Use only the facts, proof and claims in the attached source. Where a section needs a testimonial, statistic, expert, study or stock level that the source does not contain, write [VERIFY: what is needed] instead of inventing it. Do not name or imitate real people.
```
- **Check before moving on:** point-by-point flow, not "zigs and zags" ("It's almost always fine"); every number traced to the source page (Stefan: "Is there 95 anywhere on this? Yeah… it's taking it from their claims on their page"). [09-02 27:01–30:55](../lessons/09-02-claude-project-for-advertorials.md)

### Step 5 — Write the full draft
- **Input:** approved outline.
- **Output:** full advertorial.
- **Prompt (verbatim, process doc):**
```text
perfect, let's go ahead and write this advertorial now. If you run out of space in a single output and need to do it over multiple outputs that's fine, just let me know and I'll prompt you to continue.
```
Short form as typed: `perfect, let's go ahead and write this advertorial now`. Stefan says Prompt 3 is "to be honest with you, not needed" because Claude continues when told. [09-02 17:54](../lessons/09-02-claude-project-for-advertorials.md) [09-02 30:55](../lessons/09-02-claude-project-for-advertorials.md)
- **Tool/model:** same chat.
- **Check before moving on:** run Step 7's audit list on the draft before asking for variants, so errors do not propagate.

### Step 6 — Produce the shorter test variant and further angles
- **Input:** the approved draft.
- **Output:** a ~50% shorter version with the same headline and beats; optionally a draft for a second hook.
- **Prompt (verbatim, spoken and confirmed on screen):**
```text
this is great, really nice job. Can you now do another version of this advertorial that retains the main structure and elements, but that's about 50% shorter so I can have a less lengthy version to also test.
```
Second-angle request (spoken; Whisper text cleaned for punctuation):
```text
Great job. Now let's do hook number six, the arctic discovery. For this let's keep it shorter, the short version of the advertorial you just did. Still have the target audience be parents of kids. Frustrated parents of kids with acne, but incorporate this discovery.
```
[09-02 40:48–41:19](../lessons/09-02-claude-project-for-advertorials.md) [09-02 44:37–45:53](../lessons/09-02-claude-project-for-advertorials.md)
- **Why:** "sometimes… for sure, one's going to be better. We just want to test options." [09-02 41:19–41:54](../lessons/09-02-claude-project-for-advertorials.md)
- **Check before moving on:** the short version keeps scene, failed-alternatives, mechanism line, timeline, guarantee and CTA (Stefan's short version kept these). [09-02 41:54–44:02](../lessons/09-02-claude-project-for-advertorials.md)

### Step 7 — Boss edit and claim audit
- **Input:** each draft.
- **Output:** a numbered feedback message to the model, then a clean, audited draft.
- **Prompt (reconstructed from audio; the typed text may differ):**
```text
Great job. A few things.
1. Instead of speaking specifically about Big Pharma, let's talk about big skin care companies instead. We can still also reference prescriptions, but I don't want the whole [piece] focused on anti Big Pharma.
2. Next, let's make this about 20% shorter.
3. Third, it's a 60 day guarantee. [fix the guarantee length]
4. Fourth, I want a little more congruency between discovering these plants and the decision to test them against acne bacteria.
```
Congruence note as typed (verbatim, screen):
```text
I think what's missing is something like, when Dr. Johansson saw the incredible antimicrobial power of these plants, he immediately thought about acne. Perhaps even say that's because his own teenage sons both suffered from severe acne and nothing they'd tried worked.
```
[09-02 49:05–54:55](../lessons/09-02-claude-project-for-advertorials.md) — the doctor and sons are model-invented; for our brands use a real, documented origin or drop the persona.
- **Audit list (what Stefan checked, plus repo rules):**
  1. Every statistic and quote traced to the source; else cut or `[VERIFY: …]`. [09-02 30:24–30:55](../lessons/09-02-claude-project-for-advertorials.md)
  2. Guarantee, discount, kit contents, supply claims match the live offer ("attention to detail"). [09-02 49:05–49:51](../lessons/09-02-claude-project-for-advertorials.md)
  3. Enemy matches the product category (skincare companies, not "Big Pharma"). [09-02 49:51–50:27](../lessons/09-02-claude-project-for-advertorials.md)
  4. Story logic: for each step ask "why would he/she do that?"; add the motive. [09-02 51:22–52:41](../lessons/09-02-claude-project-for-advertorials.md)
  5. Length: ask for "about N% shorter" rather than hand-trimming; "about" lets it land at 24–26%. [09-02 50:27](../lessons/09-02-claude-project-for-advertorials.md)
  6. Testimonials: replace with real screenshots/photos with permission; this also shortens the page. [09-02 37:37–38:01](../lessons/09-02-claude-project-for-advertorials.md)
  7. Run the full [LLM output claim audit](../rubrics/llm-output-claim-audit.md) and [compliance red flags](../concepts/compliance-red-flags.md).
- **Check before moving on:** zero unbracketed invented proof; offer terms match; "Advertorial" label planned.

### Step 8 — Package as a page and test
- **Input:** audited copy, a full-page screenshot of a design to imitate, our own images and policy URLs.
- **Output:** a live page (Stefan uses Magic Patterns; any page builder works), title/favicon/social image set, pixels installed.
- **Prompt (Magic Patterns, spoken near-verbatim):**
```text
We're going to create a new advertorial. You can model off the design and the screenshot attached. Please do not include the screenshot image in the new advertorial. It's being provided as a design reference only. Here's the copy.

[PASTE ADVERTORIAL COPY HERE]
```
Follow-ups go one change at a time (urgency box, masthead name, breadcrumb, hero image "about half the current size", green CTA link, footer with privacy/terms/guarantee links). [09-02 v2 03:21–19:23](../lessons/09-02-claude-project-for-advertorials.md) Full follow-up texts: [09-02 Prompts §6](../lessons/09-02-claude-project-for-advertorials.md).
- **Tool/model:** Magic Patterns (Stefan names Lovable and Replit as alternatives). Pixels: the tool could not add a Meta pixel; a developer added Facebook and Hyros snippets in a `useEffect`. Each change needs Deploy → "Publish new version". [09-02 v2 33:10–36:27](../lessons/09-02-claude-project-for-advertorials.md)
- **Test design:** hold one basic PDP constant and put many ads and advertorials in front of it: "it's easier to just put up tons of advertorials that go to this page" (instructor claim). [09-01 32:32–33:42](../lessons/09-01-advertorials-overview-and-examples.md) Native guest target: about 25–30% landing-page CTR on mid/long advertorials, 40–50% on short jump pages (guest claim). [12-02 v3 13:05; v3 21:05; v3 32:13](../lessons/12-02-native-ads.md)
- **Check before moving on:** "Advertorial"/"Advertisement" label visible above the fold; our own images and policy links (Stefan's demo reused another brand's images and links); pixel firing; one variable changed per test.

### Alternate Step 3–5 — Single-page structure swipe (quick path)
Use when one proven advertorial fits our traffic and product class exactly.
- **Prompt 1 (verbatim):**
```text
Here's an advertorial I just read. Can you please go through it and then create a detailed outline of the structure:

[paste full advertorial text]
```
- **Prompt 2 (verbatim; brand and product are the course's, replace them):**
```text
Perfect, thanks this was great. Let's write an advertorial for opal beauty that follows the same structure. Specifically for our Unity Eye Serum:

[product page URL]
```
[09-01 27:50–30:35](../lessons/09-01-advertorials-overview-and-examples.md)
- **Output seen:** Claude labelled the Clarifion structure "Problem → Agitation → Solution → Proof → Urgency → Action" and also listed "red flags" (fictitious testimonials disclaimer, unproven health claims, false scarcity). Its eye-serum version invented "Sarah M., 52" and clinical percentages. [09-01 28:31–30:35](../lessons/09-01-advertorials-overview-and-examples.md)
- **Agent rule (derived):** give the brief, mechanism and real proof, not just a URL; keep section order and beats only; never the protagonist, anecdote, claims or numbers. Prefer the composite Project (Steps 2–5) — see [composite vs swipe](../concepts/composite-vs-swipe.md).

## Advertorial structures
| Type | Typical length | Section order (as taught) | Use for | Source |
|---|---|---|---|---|
| Long story advertorial (Clarifion #1) | ~2,900 words (derived) | Headline + dateline → named protagonist matching avatar → normal life → crisis scene → expert names a cause → problem education (UMP of the problem) → failed solutions → friend/guide discovery → transformation + multi-unit cue → product explanation → future pacing → scarcity + social proof → "I tested it myself" diary → price justification → dated update box + soft CTA | Meta static/curiosity ad → short PDP | [09-01 10:30–27:50](../lessons/09-01-advertorials-overview-and-examples.md) |
| Short product-forward (Clarifion #2) | short, graphics-heavy | Hook paragraph → pain amplification → root cause → solution reveal (product named at once) → features/studies → peer proof + bundle push → close (guarantee, check availability) + sticky bar/sidebar | Meta 1–2 min video ad that already revealed product | [09-01 36:42–45:09](../lessons/09-01-advertorials-overview-and-examples.md) |
| Brand pre-sell page (Comfort Orthowear) | short | Problem → why traditional fixes fail → why our product → social proof → "why is this for you" spokesperson → three reasons → get it here → reviews → sale → guarantee → FAQ | Video ad → plain Shopify PDP | [09-01 45:09–49:32](../lessons/09-01-advertorials-overview-and-examples.md) |
| Interstitial offer page (Earth Breeze) | very short | Segment-specific offer framing ("Dear Valued Senior…") → reasons → button to PDP | Aware ad + segment discount | [09-01 49:32–52:55](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native mini sales letter (hearing spray) | long | Expert claim → problem ruining life → personal discovery → "real cause" → solution → ingredients → social proof → future pacing → scarcity → experts → save more → guarantee → emotional close → final proof | Native → PDP | [09-01 v2 12:22–16:42](../lessons/09-01-advertorials-overview-and-examples.md) |
| Listicle (grounding bedsheet) | medium | Pain question → "What if…" → product → N benefits → how it works / the science | Native, educational readers, $99+ | [09-01 v2 16:42–20:32](../lessons/09-01-advertorials-overview-and-examples.md) |
| Pain-point advertorial (oven cleaner) | medium | Personal story → what it is → how it works → "cleans other stuff too" | One product, many pain points, general PDP | [09-01 v2 23:44–27:24](../lessons/09-01-advertorials-overview-and-examples.md) |
| Short VSL bridge (lung) | ~1 screen | Lead question → discovery paragraph → tease → "Click here to watch" → Watch Now | Native → VSL | [09-01 v2 31:23–33:26](../lessons/09-01-advertorials-overview-and-examples.md) |
| Short lead-in skeleton (Project KB) | 200–575 words | Curiosity headline → stat about sufferers → pain dimensionalised → experts found a simple solution → CTA to video and why you haven't heard of it | Any, to a video | [09-02 06:23–07:30](../lessons/09-02-claude-project-for-advertorials.md) |
| Top-5 comparison | "pretty short" | Named only; not shown | "people don't run as much, but they kind of should" | [09-01 52:55–53:27](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native mid-form (guest) | mid | Relatable story → price mention → "horror scenario" → quick progress → CTA → testimonials → final offer | Native ecom gadget → PDP (guest claim) | [12-02 v3 17:12–19:00](../lessons/12-02-native-ads.md) |

Full outlines: [templates library](../libraries/templates.md).

## Decision points
| IF | THEN | Source |
|---|---|---|
| Meta static or curiosity ad ("…but did you know") → short PDP/checkout hybrid | Insert a LONG story advertorial; add multi-unit cues ("one in every room") | [09-01 07:45; 30:35–33:42](../lessons/09-01-advertorials-overview-and-examples.md) |
| Meta 1–2 min video already showed problem, product, mechanism | Short, graphics-heavy page; name the product immediately; don't reuse the long story page | [09-01 36:42–38:00; 44:14–45:09](../lessons/09-01-advertorials-overview-and-examples.md) |
| Short aware ad that shows the product and says "shop now" | Can go straight to PDP; test a segment interstitial in front | [09-01 49:32–52:55](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native traffic, any destination | Use an article-format advertorial; the problems are "compliance and congruence" | [09-01 v2 10:37–13:40](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native → VSL | Short image-led bridge; let the VSL educate | [09-01 v2 31:23–33:26](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native → PDP, or price ≥ ~$99 | Long educational advertorial or listicle | [09-01 v2 12:22–16:42; 19:19–20:32; 28:44](../lessons/09-01-advertorials-overview-and-examples.md) |
| Native and the product is commoditised, buyer already knows the solution | Exception to "advertorial for 99% of offers" (guest claim) | [12-02 v2 03:01–03:31](../lessons/12-02-native-ads.md) |
| Ad is about one pain point; product solves many | One advertorial per pain point, ending with the product's breadth | [09-01 v2 26:07–27:24](../lessons/09-01-advertorials-overview-and-examples.md) |
| Product is a one-unit ~$45 item | Raise AOV inside the story (more rooms, gifts, bundles) | [09-01 18:33; 21:08](../lessons/09-01-advertorials-overview-and-examples.md) |
| Brand has an ad story already winning | Pick the matching hook; paste the caption into Prompt 2 | [09-02 22:27–27:01](../lessons/09-02-claude-project-for-advertorials.md) |
| You want the price hidden | Keep the "save XX%" sentence in Prompt 2; else delete it | [09-02 17:28](../lessons/09-02-claude-project-for-advertorials.md) |
| Unsure of length | Produce two lengths (full + ~50% shorter) and test | [09-01 v2 23:14–23:44](../lessons/09-01-advertorials-overview-and-examples.md); [09-02 41:19](../lessons/09-02-claude-project-for-advertorials.md) |
| The design looks like a sales letter, not an article (native) | Rebuild in native article format; format matters, not only copy | [09-01 v2 21:23–22:46](../lessons/09-01-advertorials-overview-and-examples.md) |
| Model output is cut off | Say "continue" | [09-02 17:54](../lessons/09-02-claude-project-for-advertorials.md) |
| Long native page | Delay the CTA button so traffic is pre-qualified (guest claim) | [12-02 v3 21:05](../lessons/12-02-native-ads.md) |

## Failure modes and fixes
| Failure | Symptom | Fix | Source |
|---|---|---|---|
| No pre-sell on a belief-heavy product | High CPA, low AOV; "you may need to spend $400, $500 on Meta" per sale (instructor illustration) | Insert a long advertorial before the PDP | [09-01 05:08–09:41](../lessons/09-01-advertorials-overview-and-examples.md) |
| Topic mismatch (ad ≠ page) | "I feel bait-and-switched" | Pain-point advertorial that bridges to the general PDP | [09-01 v2 doc *4. Native Ads*](../lessons/09-01-advertorials-overview-and-examples.md) |
| Experience mismatch (article → shop page) | "I wanted to consume content, not shop" | Put an article-format page between them | [09-01 v2 29:20–29:52](../lessons/09-01-advertorials-overview-and-examples.md) |
| Repeating what the video already said | Long grandma story after a 1–2 min video | Shorter product-forward page | [09-01 36:42](../lessons/09-01-advertorials-overview-and-examples.md) |
| Model invents numbers, guarantee terms | "90 day" guarantee vs real 60; "96% within 30 days" not on source | Trace each claim to source; correct or `[VERIFY]` | [09-02 49:05–49:51](../lessons/09-02-claude-project-for-advertorials.md); [09-02 Example B](../lessons/09-02-claude-project-for-advertorials.md) |
| Wrong enemy | Whole piece turns "anti Big Pharma" | Re-aim at the category ("big skin care companies") | [09-02 49:51–50:27](../lessons/09-02-claude-project-for-advertorials.md) |
| Story logic gap | Reader asks "why would he test that?" | Add a motive; reread as a third party | [09-02 51:22–54:55](../lessons/09-02-claude-project-for-advertorials.md) |
| Internal contradiction | "almost kill her" vs "luckily not serious" | Read for consistency; Stefan notes it still ran, so judge by data, but fix it in ours | [09-01 20:03](../lessons/09-01-advertorials-overview-and-examples.md) |
| Too long | "it's good, but it's too long" | "about N% shorter" request; testimonial screenshots in place of written ones | [09-02 37:37–38:01; 44:02; 50:27](../lessons/09-02-claude-project-for-advertorials.md) |
| Overdramatic close | Melodramatic line | Tone it down in the edit pass | [09-02 40:22](../lessons/09-02-claude-project-for-advertorials.md) |
| Knowledge base all one niche | Model copies topic, not structure | Mix niches and product types | [09-02 12:14–12:46](../lessons/09-02-claude-project-for-advertorials.md) |
| Swipe link dies | Reference advertorial gone | Save PDF/screenshot copies | [09-02 03:32–04:35](../lessons/09-02-claude-project-for-advertorials.md) |
| Claude upload error on huge image PDF | File too large | Convert to text or "do something else" (Stefan's words) | [09-02 20:54–21:50](../lessons/09-02-claude-project-for-advertorials.md) |
| Untrustworthy page shell | Default tab title, globe favicon | Set title, description, 1200×630 social image, 32×32 favicon; redeploy | [09-02 v2 23:39–29:41](../lessons/09-02-claude-project-for-advertorials.md) |
| Page edits not live | Old version served | Deploy → "Publish new version" | [09-02 v2 33:10](../lessons/09-02-claude-project-for-advertorials.md) |
| Unverifiable proof on page | Review count claimed vs far fewer findable (15,000 claimed; Stefan found 356 on Trustpilot) | State only counts we can show | [09-01 40:34–41:09](../lessons/09-01-advertorials-overview-and-examples.md) |

## Output contract
Deliver, per advertorial:
1. **Journey line:** `ad (type, what it revealed) → advertorial (type, length band) → destination (price)`.
2. **Hook chosen** + why (link to winning ad angle).
3. **Outline** (section list with word targets).
4. **Full draft** and **~50% shorter variant**, each with headline, subhead, "Advertorial"/"Advertisement" label, byline/date only if real, body, soft CTA ("check availability", "watch now"), disclaimers.
5. **Claim table:** every factual claim → source (brief, PDP, study) or `[VERIFY: …]`.
6. **Missing-inputs list:** proof, photos, reviews, guarantee terms we still need.
7. **Test note:** what is held constant (PDP), what varies (advertorial length/hook).

## Compliance
- **Course content, structure only; claims not reusable.** The examples include invented protagonists ("Carol F., 76"), reviews the page itself calls fictitious, "reviewed by a nurse, allegedly", "64,317 new customers", "15,000 five-star reviews", "sold out twice", dated "inventory is dwindling" boxes, "Harvard scientists" / "Nobel-Prize-winning research", "reverse hearing loss", "91% are affected", "cancer-causing chemicals", and a deepfake of a real doctor. [09-01 Compliance flags](../lessons/09-01-advertorials-overview-and-examples.md)
- **Model-invented proof in the demo:** "Dr. Erik Johansson", his sons, "3X faster", "87%", "92%", "Zero reported side effects", "Michelle from Arizona", "David from Texas" — none on the source page. [09-02 Example B](../lessons/09-02-claude-project-for-advertorials.md)
- **HARD STOP (repo rule).** Stefan on the made-up researcher story: "You can figure out ways when you're doing these to ensure anything that you have is congruent, truthful... or, you know, it's an editorial, so you can kind of not, but you'd have to say, hey, this is like a sort of made-up story or composite story". [09-02 53:09](../lessons/09-02-claude-project-for-advertorials.md) Under [AGENTS.md](../../../../../../AGENTS.md) "never invent proof": do not write invented experts, quotes, studies, results or customers as fact, editorial format or not. A dramatisation is allowed only if it contains no fabricated proof, is clearly labelled, and makes no claim beyond substantiated ones.
- **Black-hat refusal recorded:** Stefan himself refused to teach from the deepfake pink-salt page ("I don't want to teach off of super black hat stuff"). Never use a real person's name, likeness or invented quotes. [09-01 v2 06:41–09:06](../lessons/09-01-advertorials-overview-and-examples.md)
- **Disclosure:** label "Advertorial"/"Advertisement"; Stefan flags the unlabelled Comfort Orthowear page ("They should, for compliance"). [09-01 47:58](../lessons/09-01-advertorials-overview-and-examples.md) Native standards are "lower", not none; claims on native pages are "too aggressive". [09-01 v2 16:11–16:42](../lessons/09-01-advertorials-overview-and-examples.md)
- **Scarcity:** no same-day timers or invented stock; bigger native networks disallow current-date timers (guest claim). Use a real offer end date or none. [12-02 v3 19:00](../lessons/12-02-native-ads.md)
- **Supplements/skincare:** structure/function wording only; no disease, cure or "faster than prescriptions" claims without substantiation.
- **Compliant placeholders:** `[VERIFY: review count from Trustpilot/Shopify]`, `[VERIFY: permissioned customer story + photo]`, `[VERIFY: study citation supporting X]`, `[VERIFY: guarantee length]`, `[VERIFY: real stock/offer end date]`.
- Use our own images, domain and policy pages (the 09-02 v2 demo used another brand's images and policy links for demonstration). [09-02 v2 03:21–33:44](../lessons/09-02-claude-project-for-advertorials.md)

## Worked examples
- **Clarifion ODRx, two advertorials for two ad types** (structure only; claims not reusable): long grandma story behind static ads; short product-forward page behind a 1:13 video ad. [09-01 10:30–45:09](../lessons/09-01-advertorials-overview-and-examples.md)
- **Norse Organics acne, full Project loop** (structure only; claims not reusable): landing-page PDF → 10 hooks → #5 "Mom Shocked" medium outline with the brand's winning caption → draft → ~50% shorter → #6 "Arctic Discovery" short → 4-point boss edit (enemy, −20%, 60-day guarantee, motive) → hand edit of the transition → Magic Patterns page → deploy. [09-02 17:54–1:00:03; v2 00:00–36:55](../lessons/09-02-claude-project-for-advertorials.md)
- **Oven cleaner pain-point page** in front of an all-purpose cleaner PDP. [09-01 v2 23:44–27:24](../lessons/09-01-advertorials-overview-and-examples.md)
- **Florist abstraction:** the short ED skeleton reapplied to an on-demand bouquet service, to show structure transfers across categories. [09-02 08:01–10:16](../lessons/09-02-claude-project-for-advertorials.md)
- **Unity Eye Serum swipe** of the Clarifion structure (quick path). [09-01 29:09–30:35](../lessons/09-01-advertorials-overview-and-examples.md)

## Where it's taught
- [09-01 Advertorials Overview and Examples](../lessons/09-01-advertorials-overview-and-examples.md): purposes, elements, lengths [00:00–19:33]; Clarifion #1 [10:30–27:50]; Claude swipe [27:50–30:35]; static → long → short PDP [30:35–33:42]; Clarifion #2 [34:53–45:09]; Comfort Orthowear [45:09–49:32]; Earth Breeze [49:32–52:55]; native problems [v2 10:37–13:40]; native examples [v2 03:54–33:26].
- [09-02 Claude Project for Advertorials](../lessons/09-02-claude-project-for-advertorials.md): Project setup [00:00–05:52]; structure over topic [05:52–11:45]; swipe file [12:46–16:23]; three prompts [16:23–17:54]; live demo [17:54–1:00:03]; Magic Patterns build and deploy [v2 00:00–36:55].
- [12-02 Native Ads](../lessons/12-02-native-ads.md) (guest: Dynh Nguyen): advertorial for "99% of offers", mid/long advertorial structures, landing-page CTR targets, timers [v2 03:01–03:31; v3 13:05–32:13].

## Cross-course notes
- **Shared Tether concept:** [Native advertising](../../../../concepts/native-advertising.md). RMBC adds the length-by-what-the-ad-revealed rule and the Claude Project loop.
- **Evolve Start Here — page selection.** Evolve picks the page by awareness level and split-tests at least two pages against a control LP ([market awareness levels](../../../evolve/start-here/concepts/market-awareness-levels.md); [L95 test landing pages 3-2-2-2](../../../evolve/start-here/lessons/095-how-to-test-landing-pages-3-2-2-2.md); [L121](../../../evolve/start-here/lessons/121-how-to-deal-with-roller-coaster-performance.md)). Stefan picks by unit economics and by what the ad revealed, and holds one PDP constant while mass-testing advertorials. [09-01 32:32–33:42](../lessons/09-01-advertorials-overview-and-examples.md) **Agent default:** use Stefan's rule to decide whether and how long; use Evolve's 3-2-2-2 to structure the page test.
- **Evolve Copywriting — bridges.** Evolve writes a [bridge](../../../evolve/copywriting/concepts/bridges.md) between hook and pitch; in Stefan's examples the advertorial's first screen is that bridge (derived).
- **Evolve Copywriting — AI.** Same "you are the editor" stance as [AI in copywriting](../../../evolve/copywriting/concepts/ai-in-copywriting.md).
- **Tether shared:** [Hero image and copy congruence](../../../../concepts/hero-image-copy-congruence.md) and [landing page psychology audit](../../../../frameworks/landing-page-psychology-audit.md) for the page review after Step 8.

## Related
- [Ad-to-page journey](../concepts/ad-to-page-journey.md) · [Congruence](../concepts/congruence.md) · [Sell the click](../concepts/sell-the-click.md) · [Composite vs swipe](../concepts/composite-vs-swipe.md) · [Claude Project recipe](../concepts/claude-project-recipe.md) · [LLM copy-chief editing](../concepts/llm-copy-chief-editing.md) · [Compliance red flags](../concepts/compliance-red-flags.md) · [Unique mechanism](../concepts/unique-mechanism.md) · [Funnel economics](../concepts/funnel-economics.md)
- [Paid traffic by platform](paid-traffic-by-platform.md) · [PDP build](pdp-build.md) · [Brief generator](brief-generator.md) · [Hook generation system](hook-generation-system.md) · [CRO testing](cro-testing.md)
- [Playbook: offer to funnel end to end](../playbooks/offer-to-funnel-end-to-end.md) · [Playbook: launch a cold traffic funnel](../playbooks/launch-a-cold-traffic-funnel.md)
- [Prompts library](../libraries/prompts.md) · [Templates library](../libraries/templates.md) · [Benchmarks](../libraries/benchmarks.md) · [LLM output claim audit](../rubrics/llm-output-claim-audit.md) · [Funnel audit](../rubrics/funnel-audit.md)
