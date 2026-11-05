---
title: "Primer: how a dropshipping / DTC ecom business and Meta ads work (2026), and where a technical creative strategist fits"
type: resource
creator: synthesis
course: none
sources:
  - https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
  - https://www.jonloomer.com/meta-andromeda/
  - https://www.jonloomer.com/meta-ads-attribution-2026/
  - https://www.facebook.com/business/ads/ad-auction
  - https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness
  - https://developers.facebook.com/blog/post/2026/04/29/introducing-ads-cli/
  - https://help.shopify.com/en/manual/payments/shopify-payments/reserves
  - https://www.ftc.gov/legal-library/browse/rules/mail-internet-or-telephone-order-merchandise-rule
  - https://venon.io/blog/ecommerce-contribution-margin
  - https://theoptimizer.io/blog/how-to-test-ad-creatives-on-meta-after-the-andromeda-update-2026-playbook
  - https://27five-website.pages.dev/blog/meta-ads-benchmarks-ecommerce-2026
  - https://jetfuel.agency/creative-performance-metrics-for-dtc-video-ads-hold-rate-thumbstop-and-thruplay-benchmarks-2026/
  - https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026
tags: [primer, dropshipping, dtc, unit-economics, breakeven-roas, meta-ads, andromeda, advantage-plus, creative-testing, metrics, creative-strategist, onboarding]
updated: 2026-10-30
---

# Primer: ecom + Meta ads for a technical creative strategist
> Web research (30 Oct 2026), written to teach. Meta's engineering, policy and CLI pages, the FTC and Shopify are primary sources. Most numbers and "rules" come from agency or vendor blogs: treat them as rules of thumb, not facts. Verify policy against Meta's own pages.

## 1. The machine in one picture
**Find a product → make ads → spend a little to test → kill what loses → put more money behind what wins → make new ads before the winners get tired → repeat.**

Dropshippers run many small bets because they don't know in advance which product, angle or ad will work. The ad is the product's real test. Most bets lose. One winner pays for the losers, as long as the math (section 3) works.

## 2. Types of stores
| Type | What it is | Reality in 2026 |
|---|---|---|
| General store | Many unrelated products, no brand | Mostly dead: saturated, thin margins (sources say about 2–10%) |
| One-product / niche store | One hero product, one angle, lots of creative testing | Common way in; lives or dies on creative |
| Branded dropshipping / DTC | Own branding and packaging, $30–100 products, landing pages | More margin (vendor claims about 15–35% net), repeat buyers, fewer refunds; slower and costlier to start |

## 3. The money math (learn this first)
- **Contribution per order (before ads)** = what the customer pays − product cost − shipping − payment fees − refunds and discounts.
- **Breakeven CPA** = that contribution. Pay more than this per sale and you lose money.
- **Breakeven ROAS** = order value ÷ contribution, which is the same as 1 ÷ margin %.
- **MER** = total revenue ÷ total ad spend for the whole store. It's the honest number, because it ignores what Meta claims.
- **LTV** (lifetime value) lets brands pay more on the first order when people buy again.

**Worked example (made-up numbers):**

| | 1 unit | "Buy 2, save 15%" |
|---|---|---|
| Customer pays | $39.99 | $67.98 |
| Product cost | $9.00 | $18.00 |
| Shipping | $6.00 | $8.00 |
| Payment fees (~3%) | $1.20 | $2.04 |
| Refunds (~5%) | $2.00 | $3.40 |
| **Contribution = breakeven CPA** | **$21.79** | **$36.54** |
| **Breakeven ROAS** | **1.84** | **1.86** |

The bundle earns more per order, but it doesn't make profit easier, because the discount eats the margin. Calculate a separate breakeven for every offer.

## 4. Testing products and ads (rules of thumb, sources vary)
- **Find candidates:** TikTok Creative Center, Kalodata (TikTok Shop sales), ad spy tools (ads running for weeks are a rough profit signal), Amazon Movers & Shakers, then check supply on AliExpress or CJ.
- **Signs of a winner:** solves a visible problem, has a "wow" moment on video, sells at about 2.5–3× landed cost, isn't in local stores, light, low returns.
- **Test:** 3–5 genuinely different creatives per product. Spend about 2–5× target CPA per creative (or a ~$150 floor), over a few days to a week.
- **Decide:**
  - **Kill** a creative after about 2–3× breakeven CPA spent with no purchases and weak CTR.
  - **Fix the page or offer** if clicks and add-to-carts are healthy but purchases are thin.
  - **Scale** when CPA stays under breakeven for several days: raise the budget about 10–20% every 2–3 days, and duplicate into the scaling campaign.
  - **Kill the product** when several distinct concepts all fail. Usually the creative dies first.

## 5. How Meta ads work now
- **Auction:** Meta doesn't simply pick the highest bid. A rough model is bid × estimated chance of the action × ad quality. A more relevant ad can beat a bigger bid. Clickbait and withheld information lower quality.
- **Andromeda (2025–26):** the first-stage system that picks a few thousand candidate ads out of millions for each person.
  - Meta says the goal shifted "from niche targeting to creative diversification".
  - So **the creative is the targeting**: each ad's angle decides who it reaches.
  - Ten near-identical ads compete with each other. Ten different concepts reach ten different groups of people.
- **Advantage+ sales campaigns + broad targeting** are the default: Meta's AI picks the audience, and your creatives steer it.
- **Learning phase:** needs about 50 conversions a week. Big edits restart it, so make edits in batches, not constantly.
- **Tracking:** pixel (browser) + Conversions API (server), deduplicated with the same `event_id`. Aim for Event Match Quality of 7+.
- **Attribution in 2026:**
  - Default is 7-day click, 1-day engage, 1-day view, and only link clicks count as clicks.
  - View-through attribution inflates results, so always check Ads Manager against Shopify orders and MER.

## 6. Account setup for testing (one common pattern)
- A **testing campaign** with a fixed budget for each ad set (ABO):
  - one concept per ad set, broad targeting
  - about $20–50/day each
  - 8–12 distinct concepts per round
  - read after about 7 days or about $100–150 spend per creative, with an early stop-loss
- **Winners** move to a scaling campaign (CBO or Advantage+) with 15–25 active creatives.
- **New ads:** keep launching new concepts every week. Only about 5–10% of new creatives become winners, and fatigue shows as frequency rising while CTR falls.
- "3-3-3" usually means 3 creatives × 3 primary texts × 3 headlines. Ask what your team means by it.

## 7. Metrics and what to fix
| Metric | Meaning | Rough benchmark (directional) |
|---|---|---|
| Hook rate | 3-second views ÷ impressions | ~23% feed, ~30% Reels |
| Hold rate | ThruPlays ÷ 3-second views (definitions vary) | 18–50% |
| CPM | Cost per 1,000 impressions | ~$14 median (2025) |
| Link CTR | Link clicks ÷ impressions | ~1–2%+ |
| CVR | Purchases ÷ clicks | ~1.6% median |
| CPA / ROAS | Cost per purchase / revenue ÷ spend | Judge against **your** breakeven, not the median |

**Diagnosis:**
- **Low hook rate:** fix the first 3 seconds.
- **Good hook, low hold:** the middle drags, so get to the promise faster.
- **Good CTR, low CVR:** look at the landing page, offer, price, shipping, or a mismatch between ad and page.
- **Low CTR with a good hook:** the angle or CTA is weak.
- **High CPM:** creatives are too similar, the audience is saturated, it's the season, or creative quality is low.
- **Great ROAS in Ads Manager but flat Shopify revenue:** attribution inflation, so check MER.

Wait for at least 1,000 (ideally 3,000+) impressions before judging an ad.

## 8. Creative, and who does what
- **Media buyer:** account structure, budgets, killing and scaling.
- **Creative strategist:** research, angles, personas, briefs, scripts, reading the results, choosing the next tests.
- **Editors, designers, creators:** make the ads.
- **Test concepts first** (a different persona, desire, awareness level or angle). Then test variations of winners (new hooks, edits, copy).
- **Formats:** UGC, founder video, statics, carousels, advertorial-style, partnership (whitelisted) ads, AI UGC. The evidence on which is best is thin. Test.
- **A brief** = angle, persona, hook options, proof, offer, and the one metric to judge it by. See the [write-ugc-script skill](../../../.claude/skills/write-ugc-script/SKILL.md).

## 9. Ways to lose the business
- **Health and wellness (Meta):**
  - no "inferior appearance" statements
  - no promising specific results in a set time without qualifiers
  - no claims to cure incurable conditions
  - before/after only within the rules
  - weight-loss and cosmetic-procedure ads must target 18+
- **Personal attributes:** don't imply you know the viewer's health, age, money or traits ("Struggling with weight?").
- **Landing pages** are reviewed too.
- **AI-generated people:** get an AI label; photorealistic AI people face the strictest rules.
- **Account hygiene:** verify the business, use 2FA, keep payments clean, never open a new Business Manager to dodge a ban, and don't let automation hammer the API.
- **Shopify Payments reserves:** triggered by chargebacks, refunds, long delivery times and sudden spikes. Keep a backup payment processor.
- **FTC shipping rule (US):** you need a reasonable basis for the shipping time you advertise. Otherwise get the buyer's consent to the delay, or refund.
- **IP/trademark:** copying branded products or designs leads to takedowns. Never fake reviews, bylines, timers or doctors.

## 10. Where a technical person creates the most leverage
1. **Research engine:** weekly digest of competitor ads (Ad Library / spy tools + Gemini/Jev), TikTok Shop trends, new reviews.
2. **Review and comment mining:** customers' pains, words and objections, which become the inputs for high-intent copy.
3. **Copy at volume that is still high intent:** research → many *distinct* concepts (Andromeda wants diversity) → each with 3–6 hooks → checked by an honesty and quality checklist → human picks. See [write-ugc-script](../../../.claude/skills/write-ugc-script/SKILL.md) and `evals/`.
4. **Landing pages:** Shopify sections and templates built with Claude ([guide](shopify-landing-pages-with-claude.md)), one page per winning angle, A/B tested.
5. **Image and static production:** AI images (Nano Banana / GPT Image) composed into editable ads.
6. **Reporting:** a dashboard joining Shopify costs with Meta spend → contribution, breakeven ROAS and MER per product, plus a per-creative view of hook rate, hold rate and CPA. Meta's Ads CLI (Apr 2026) and the MCP server can read insights (start read-only; everything is created PAUSED).

## Daily Ads Manager check (creative strategist)
1. Spend and results per ad (24 h / 3 days / 7 days): which concepts get budget?
2. Hook and hold rate for new videos.
3. Link CTR, CPM, frequency (fatigue).
4. CPA and ROAS vs breakeven, judged only with enough data.
5. Ads Manager vs Shopify vs MER.
6. Rejections and Account Quality.
7. The pipeline: how many distinct concepts are live, and what replaces the tired ones?
8. Ad Library: competitors' newest ads become angles to test.

## Limitations
- Most benchmarks, budgets and kill rules come from agencies and vendors that sell tools. Meta's Help Center pages on auctions, attribution and personal attributes would not load during research, so check them directly.
- The 2026 changes (Advantage+ learning threshold, MCP details) are single-source claims.
