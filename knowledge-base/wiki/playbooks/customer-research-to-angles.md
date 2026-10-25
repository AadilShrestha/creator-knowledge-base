---
title: "Playbook: Customer Research → Angles (reviews, Reddit, search, surveys → mindstates → hidden motivators → angles)"
type: playbook
creator: sarah-levinger
course: tether-lab
sources:
  - knowledge-base/wiki/frameworks/customer-research-stack.md
  - knowledge-base/wiki/frameworks/mindstate-emotion-mapping.md
  - knowledge-base/wiki/frameworks/core-identity-map-surveys.md
  - knowledge-base/wiki/frameworks/three-selves-diagnostic.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md
  - knowledge-base/wiki/courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md
tags: [playbook, customer-research, review-mining, reddit, answerthepublic, tiktok-creator-search-insights, core-identity-map, mindstates, hidden-motivators, outliers, angles, hooks]
updated: 2026-10-20
---

# Playbook: Customer Research → Angles
> Run Sarah's four research layers — **market → consumer (reviews) → behaviour/emotion (CIM surveys) → social trends** — then map what customers feel to the nine **mindstate** emotions, push each to a specific sub-emotion, find the **hidden motivators** and **outliers**, tag them by self and zone, and turn them into angle seeds and hook lines in the customer's own words. Output: a `research_brief` + `angle_seeds` for [angle remix](angle-remix.md).

## 🤖 Agent use
- **Use when:** before any new batch for a product; when the account keeps fatiguing; before a landscape audit (so you know what "opposite" means); whenever you need hooks in customer language.
- **Inputs → outputs:** category keyword + reviews (≥50, ideally ~80 paragraph-length) + Reddit threads + search data (Google Trends, AnswerThePublic, Keyword Planner, TikTok Creator Search Insights) + surveys/quiz/comments if any → `research_brief` ([template](../frameworks/customer-research-stack.md#output-template-research-brief)) + `angle_seeds` (YAML below) + hook candidates.
- **Rules:**
  - DO run the layers in order and refresh: market monthly, the rest ~weekly; **update, don't accumulate** [Jun4 0:25:00–0:28:12; May7 0:10:15–0:10:51].
  - DON'T build acquisition ads from reviews alone: "you are going to be pulling in the exact same person who already purchased from you." Use reviews for **outliers** and language [Jun4 0:23:59–0:27:07] ([contradictions](../contradictions.md) row 14).
  - DO tell the LLM to **read between the lines** and find the **hidden motivators**; it reads literally by default [R1 0:46:04–0:47:07; Jun11 0:27:40–0:28:44].
  - DON'T let ChatGPT invent customer types or ICPs; it may list candidates, then **verify each on Reddit (thread count) and TikTok** [May7 0:30:31–0:31:34; May14 0:29:57] ([contradictions](../contradictions.md) row 15).
  - DO name the **specific** emotion: "The only reason ads are expensive is because we're using a generalized term" [Jun4 0:38:43].
  - DO check founder bias if you are the target customer [Jun11 0:28:44–0:29:47].
  - DON'T invent quotes, stats or "real user" labels. Quote reviews verbatim with an ID.
- **See also:** [Customer research stack](../frameworks/customer-research-stack.md) · [Mindstate mapping](../frameworks/mindstate-emotion-mapping.md) · [Core Identity Map surveys](../frameworks/core-identity-map-surveys.md) · [Emotion specificity](../concepts/emotion-specificity.md) · [Triggering events](../concepts/triggering-events.md) · [AnswerThePublic](../tools/answerthepublic.md) · [TikTok Creator Search Insights](../tools/tiktok-creator-search-insights.md) · [ChatGPT](../tools/chatgpt.md) · [Angles library](../libraries/angles.md)

**Source key:** May7 = [Live May 7](../courses/tether-lab/05-live-recordings/2025-05-07-live-with-sarah.md) · May14 = [Live May 14](../courses/tether-lab/05-live-recordings/2025-05-14-live-with-sarah.md) · May21 = [Live May 21](../courses/tether-lab/05-live-recordings/2025-05-21-live-with-sarah.md) · J = [Joanna Wallace](../courses/tether-lab/05-live-recordings/2025-05-23-guest-session-01-joanna-wallace.md) · R1 = [Roast #1](../courses/tether-lab/05-live-recordings/2025-05-28-roast-my-ads-1.md) · Jun4 = [Live Jun 4](../courses/tether-lab/05-live-recordings/2025-06-04-live-with-sarah.md) · Jun11 = [Live Jun 11](../courses/tether-lab/05-live-recordings/2025-06-11-live-with-sarah.md) · Jun18 = [Live Jun 18](../courses/tether-lab/05-live-recordings/2025-06-18-live-with-sarah.md) · R3 = [Roast #3](../courses/tether-lab/05-live-recordings/2025-07-23-roast-my-ads-3.md). **(pipeline design)** = our process.

## Procedure

### Step 1: Market layer (monthly)
1. Google Trends, category keyword, 5-year view → rising / flat / declining; a flat line explains a hard year before you blame creative [Jun4 0:25:00–0:26:05].
2. AnswerThePublic: read all the questions and classify buyer **education** [Jun4 0:52:34–0:54:36]:

   | Questions you see | Education | Lead with |
   |---|---|---|
   | "What is it / how does it work / what does it taste like" | low | trigger + exploration ads, heavy education |
   | Questions about a specific ingredient/feature | mid ("evaluatory stage") | evaluation: comparisons and proof |
   | Highly specific variants | high ("college-level") | purchase: "be the best at offers" |

3. Pinterest Trends / Reddit for raw emotion. Rate Reddit's emotional intensity 1–10; r/FemaleHairLoss was "an 11, a 10" while surveys were "very simple, nice, easy" [Jun4 0:28:12].

### Step 2: Collect consumer text
- ~80 reviews of at least a paragraph (50 good ones can work; 15 is too few) [R1 0:47:07–0:48:07]. Add surveys, quiz answers, ad comments, emails, call notes [Jun11 0:27:40; J 0:07:12].
- Optional: competitor reviews from ~20 brands to separate industry-wide emotions from our outlier [Jun4 0:14:34].
- Give every item an ID (`REV-<nn>`, `RED-<nn>`, `SRV-<nn>`) so quotes stay traceable.

### Step 3: Review NLP (hidden motivators + mindstates)
Run the combined prompt (assembled from Sarah's spoken prompts; [research stack](../frameworks/customer-research-stack.md#prompts-verbatim-or-near-verbatim-as-spoken)):
```text
Below are <N> customer reviews for <product>, each with an ID. Read between the lines: look for the
context behind what people say, not only the literal words.
1. What are the hidden motivators inside all of these reviews? Quote 2-3 review IDs as evidence for each.
2. Map the reviews to these nine emotions: achievement, autonomy, belonging, competence, empowerment,
   engagement, esteem, nurturance, security. Return the top three with share of reviews, then three more
   specific sub-emotions for each.
3. List outliers: behaviors, situations or phrases that appear in only a few reviews but are vivid or unexpected.
4. List exact phrases customers use for the product and the problem.
5. Which jokes or kinds of humor do these customers already make?
Do not invent quotes or statistics. Use only the review text.
```
Verify every quote against the source ID. (The nine-emotion list is outside context; Sarah named security, belonging, achievement and esteem — see [mindstate mapping](../frameworks/mindstate-emotion-mapping.md#definition).) Listen for keywords the way Sarah does: "I wasn't allowed to as a kid" = deprivation; "I just got to be free for a minute" = freedom [R1 0:46:04].

### Step 4: Push to specific emotions
For each top emotion, write 3 nuances and a situation: esteem → confidence / control / appeal; "boss babe" vs "cheeky" confidence [Jun4 0:36:36–0:37:39]. Ask: "is it actually esteem that they want, or do they want to be more appealing? Is it belonging, or do they just want to feel noticed?" [Jun4 0:37:39–0:38:43]. Score each with valence/intensity → the zone the customer is *in* ([valence-intensity diagnostic](../frameworks/valence-intensity-diagnostic.md)).

### Step 5: Validate customer types (Reddit + TikTok)
If you lack customer access: ask an LLM for every type of person who could use the product, then keep only the types with real Reddit threads, double-check on TikTok, and look for small viable subgroups (70–80-year-olds keeping muscle mass vs bodybuilders) [May7 0:29:20–0:32:06]. Record thread counts. Drop types with no threads [May7 0:31:08–0:31:34].

### Step 6: Social trends
TikTok Creator Search Insights: list searched terms with too little content → video topics and hook seeds [Jun4 0:27:07–0:28:12].

### Step 7: Behaviour and identity (surveys)
If you can survey customers, use [CIM rules](../frameworks/core-identity-map-surveys.md): ~4 pictures per question, metaphors, "how do you **feel**" (never "think"), open with NPS + "What would get you up to a ten?", don't lead, don't name the feeling, ask about behaviour (where it's stored, how often used) [Jun4 0:55:41–0:57:44; May7 0:18:40–0:19:22]. The "40 bottles on the counter" outlier came from this layer [May7 0:17:51–0:20:05].

### Step 8: Motivators → self, trigger and stage (pipeline design on course cues)
For each hidden motivator:
- **Self**, using customer-language cues: "This is so me / exactly what I needed" = Actual; "One day I'll… / finally becoming" = Ideal; "I should really… / it's about time I…" = Ought ([self-spotting](../frameworks/three-selves-diagnostic.md#self-spotting-in-customer-language-for-research-and-reviews)).
- **Trigger event vs motivator**: stable life event ("I just bought a puppy") vs passing mood ("didn't drink enough coffee") — write trigger ads to events [May21 0:39:40–0:40:44] ([triggering events](../concepts/triggering-events.md)).
- **Belief**: the belief under the behaviour; note when the trigger is negative but the behaviour is optimistic ("I can slow it down") and test both [Jun11 0:29:47–0:31:50].
- **Routing**: majority patterns → retention/retargeting; outliers → acquisition [Jun4 0:23:59–0:25:00] (routing derived).

### Step 9: Angle seeds and hooks
Turn each motivator into an angle seed (template below) and lift 2–3 hook candidates from real phrases. Examples of the move in the course:

| Research finding | Angle / line | Source |
|---|---|---|
| Survey outlier: "40 bottles on my counter" | "This is the last time you're ever going to switch." → "The last skincare switch you'll ever make" (ran 8 months) | [May7 0:17:51–0:20:05]; [Jun4 0:47:21] |
| Review: "He put up the tent…" | "He put up the tent, but you brought the flask." | [Heuristics 101 L3](../courses/tether-lab/02-heuristics-101/03-emotion-clarity-urgency.md) [01:27] |
| Comments: grinder is "a tank… a weapon" | "Can be used as a weapon. Also the best pepper grinder I've ever used." (real user quote) | [J 0:07:12–0:08:17] |
| Reviews: back pain on waking | "Wake up better" instead of "get better sleep" | [May21 0:30:50–0:33:51] |
| Reviews across use cases: "I know I can go back to this" | "a reliable piece of calm" | [May7 0:41:36–0:43:43] |
| Pet owners "defeated by failed solutions" | "Every bowl that we gave him, he destroyed." | [R3 0:31:35–0:34:44] |

## Output
Fill the [research brief template](../frameworks/customer-research-stack.md#output-template-research-brief), then:
```yaml
angle_seeds:
  - id: SEED-<nn>
    motivator: "<hidden motivator in one line>"
    evidence: ["REV-12: '<verbatim>'", "RED-03: '<verbatim>'"]
    frequency: majority | outlier
    route: acquisition | retargeting | retention
    mindstate: "<…>"
    specific_emotion: "<sub-emotion + situation>"
    customer_zone_now: Z1 | Z2 | Z3 | Z4      # the feeling they are in
    target_zone: Z1 | Z2 | Z3 | Z4            # the feeling the ad should create
    self: actual | ideal | ought
    trigger_event: "<event | none>"
    belief: "<belief under the behaviour>"
    education_level: low | mid | high
    suggested_teep: T | E1 | E2 | P
    customer_phrases: ["<verbatim>"]
    hook_candidates: ["<line using customer words>"]
    validated_on: {reddit_threads: <n>, tiktok: yes | no}
    expires: <date + 30 days>
```

## Quality gates
- [ ] ≥50 paragraph-length reviews (or the gap is stated); every quote carries an ID and matches the source.
- [ ] Each top emotion has 3 specific nuances; no umbrella emotions left.
- [ ] Every customer type has outside evidence (Reddit/TikTok/survey); none comes only from an LLM.
- [ ] Outliers are separated from majority patterns, and acquisition seeds aren't majority-only.
- [ ] Brief has an expiry date; stale seasonal findings removed.

## Related
[Playbooks hub](README.md) · [Angle remix](angle-remix.md) · [Landscape audit](competitor-landscape-audit.md) · [Blended emotions](../concepts/blended-emotions.md) · [Core brand emotion](../concepts/core-brand-emotion.md) · [Perception management](../concepts/perception-management.md) · [Identity stacking](../concepts/identity-stacking.md) · [Will Leach](../people/will-leach.md) · [Humor in ads](../concepts/humor-in-ads.md)
