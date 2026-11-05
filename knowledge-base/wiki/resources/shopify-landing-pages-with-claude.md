---
title: "Shopify landing pages with Claude (listicles, advertorials, PDPs): options and recommended stack"
type: resource
creator: synthesis
course: none
sources:
  - https://shopify.dev/docs/apps/build/ai-toolkit
  - https://github.com/Shopify/dev-mcp
  - https://shopify.dev/docs/api/shopify-cli/theme/theme-push
  - https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
  - https://shopify.dev/docs/api/admin-graphql/latest/mutations/pageCreate
  - https://docs.replo.app/mcp/get-started
  - https://help.pagefly.io/integrations/ai-assistant-connector/connect-pagefly-to-claude-chatgpt-or-another-ai-assistant
  - https://instant.so/changelog/instant-mcp
  - https://feedback.gempages.net/changelog
  - https://www.getlandra.com/blog/listicle-landing-page-examples-that-convert
  - https://www.getlandra.com/blog/advertorial-examples-that-convert
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://fal.ai/pricing
  - https://www.shoplift.ai/pricing
  - https://www.intelligems.io/pricing
tags: [shopify, landing-pages, listicle, advertorial, pdp, claude-code, mcp, page-builders, image-generation, ab-testing, research]
updated: 2026-10-30
---

# Shopify landing pages with Claude
> Web research (30 Oct 2026) for building ad landing pages (listicles, advertorials, PDPs) on Shopify with Claude Code, plus AI image tools and A/B testing. **Not course knowledge:** these are vendor docs and pricing pages that change often, so re-check prices before buying.

## 🤖 Agent use
- **Use when:** asked to build or plan a Shopify landing page, listicle, advertorial or PDP with Claude, or to pick an image or A/B tool.
- **Inputs → outputs:** store access + winning ad angle + product facts → section-based Shopify page template on an unpublished theme → QA → A/B test.
- **Rules:**
  - DO build on an unpublished/development theme (`shopify theme push --unpublished`); never `--allow-live`.
  - DO keep content in section settings and blocks so non-coders can edit it in the theme editor.
  - DO label advertorials "Advertisement"; never invent a publication, expert byline, press logo or result (see [proof rules](../../../.claude/skills/write-ugc-script/references/proof-and-claims.md)).
  - DO compare Meta Events Manager counts with Shopify orders after launch; don't double-fire pixels.
  - DON'T go off-Shopify (Next.js, Funnelish) unless a test shows it's worth the tracking risk.
- **See also:** [landing-page scorecard](../rubrics/landing-page-scorecard.md) · [landing page psychology audit](../frameworks/landing-page-psychology-audit.md) · [native advertising](../concepts/native-advertising.md)

## Ways to build
| Route | How Claude does it | Cost | Best for |
|---|---|---|---|
| **Native theme (recommended start)** | Shopify **AI Toolkit** plugin for Claude Code (`claude plugin install shopify-ai-toolkit@claude-plugins-official`): Shopify docs search, Liquid/GraphQL validation, CLI tasks. Dev MCP: `npx -y @shopify/dev-mcp@latest` (sends usage telemetry). One JSON template per angle (`page.listicle-<angle>.json`) built from reusable sections; push to an unpublished theme for a preview URL. Limits: 25 sections per template, 50 blocks per section | Free | Fast, owned, no app bloat |
| Admin API `pageCreate` | Bulk-create pages that use a template (`templateSuffix`). Needs `write_content` / `write_online_store_pages` scope | Free | Many pages from one template |
| **Page builders with MCP** | **Replo** (hosted MCP, can publish and read analytics; pages are Next.js repos) · **PageFly** (MCP, builds section by section, previews in your theme, publishes only when asked) · **Instant** (MCP) · **GemPages** (MCP beta; converts HTML into editable elements, slowly) | About $24–$300/month (from PageFly's comparison page, verify) | Owner wants to edit visually |
| Shopify Sidekick | Theme settings, generated theme blocks (not on Starter plan), photo edits. Shopify warns generated code "may not always be perfect" | Included | Small edits only |
| Off-Shopify (Next.js/Vercel, Funnelish, Checkout Champ) | Full control | Varies | Only after testing: Shopify Web Pixels don't fire there, and click IDs/UTMs can be lost before checkout |

## Page structures (from teardown sources; commercial, verify claims)
- **Listicle ("5 reasons…"):** the headline names the audience or a big real proof number. Reason 1 answers the category's #1 objection, and every reason is a felt outcome. Proof and guarantee sit inside the list; the first CTA comes after the strongest reason.
- **Advertorial:** problem → mechanism → proof → offer. It reads like an article for about 70% of the page, with a named narrator and an opening concession. Label it "Advertisement".
- **One product, many angles:** duplicate the page skeleton and change only the headline and reasons for each ad angle (Funnel of the Week, Primal Viking breakdown).
- **Swipe sources:** Landra examples (about 70 teardowns), Funnel of the Week (paid), and pages that long-running ads in the Meta Ad Library point to.

## AI images at volume (list prices, Oct 2026)
| Tool | Price per image | Use |
|---|---|---|
| Nano Banana 2 (Gemini 3.1 Flash Image) | about $0.067 | Ad variations (original Nano Banana about $0.039 shuts down 15 Mar 2027) |
| Nano Banana Pro | $0.134 (1K/2K) | Higher quality |
| GPT Image 2 | $0.006 / $0.053 / $0.211 (low/med/high), batch 50% off | Text-heavy images, edits |
| FLUX.1 Kontext pro (fal) | $0.04 | Keeping the product consistent across edits |
| Photoroom API | from about $0.02 | Background removal, catalog cleanup |
| Kie.ai (reseller) | about $0.03 | Cheap drafts; third-party reliability risk |

## A/B testing
Shoplift (from $99/month; template and URL-redirect tests) or Intelligems (from $79/month). Both test Shopify-hosted pages.

## Recommended stack and first steps
1. **Install the Shopify AI Toolkit in Claude Code and set up a git theme repo.** Build 5–6 reusable sections (hero, numbered reason, proof, comparison table, CTA) and one no-nav listicle template. Deploy to an unpublished theme.
2. **Build a listicle for the best-selling product** from the top ad angle, with reason 1 answering the top objection. Check on mobile, then check that Meta and Shopify events match.
3. **Weekly loop:** duplicate the template for a second angle, run a Shoplift or Intelligems test, and generate ad image variations with Nano Banana 2 / GPT Image 2.

## Limitations
- This is web research, not course knowledge, and prices change.
- Third-party skills (DTCskills Shopify Page Builder, robpalmer99 copywriting skills, maxwellt7 advertorial skill) were found but not reviewed. Read their SKILL.md before installing.
- No good public source was found for quiz funnels.
