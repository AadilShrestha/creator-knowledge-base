---
title: "Prompts library: every AI prompt in Evolve Start Here (verbatim, grouped by pipeline step)"
type: library
creator: evolve
course: start-here
instructor: "Spencer Pawliw (Evolve); Chef Karlo (L130, guest); Shaun Eng (L172)"
sources:
  - knowledge-base/wiki/courses/evolve/start-here/lessons/005-100-hook-templates-from-ads-doc.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/006-13-winning-static-ad-templates.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/007-evolve-master-prompt-doc.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/011-understanding-unaware-awareness-levels.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/058-understanding-your-product-part-2.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/059-understanding-your-product-part-3.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/063-how-to-find-desires-part-3.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/064-action-item-start-your-desire-hunt.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/065-understanding-market-sophistication-part-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/066-how-to-find-apply-new-mechanisms-part-2.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/067-action-item-find-new-mechanisms.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/068-how-to-find-apply-new-information-part-3.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/069-action-item-find-new-information.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/074-how-to-build-core-avatars.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/076-how-to-build-sub-avatars.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/079-how-to-come-up-with-ad-angles.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/088-the-execution-problem.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/090-how-to-get-a-players-editors-content.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/110-winning-ads-definition-part-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/113-how-to-generate-submit-winning-ad-report.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/114-action-item-generate-submit-your-reports.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/123-how-to-do-learnings-part-2-winning-ads.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/125-how-to-do-learnings-part-4-winning-ads.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/130-how-to-rewrite-losing-ads-into-winners.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/136-how-to-get-viral-ugc-inspo-for-creators-ads.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/143-how-to-create-an-insense-campaign.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/171-how-to-make-any-product-work-brand-building-pt-1.md
  - knowledge-base/wiki/courses/evolve/start-here/lessons/172-live-product-research-w-kalodata-pt-2.md
  - knowledge-base/raw/evolve/start-here/_extracted/👣 Evolve (Start Here)/79. How To Come Up With Ad Angles.docx.md
tags: [library, prompts, claude, chatgpt, claude-code, ai, research, desires, new-mechanism, new-information, avatars, angles, scripts, learnings, product-research]
updated: 2026-11-02
---

# Prompts library (Evolve Start Here)
> Every AI prompt in the 175 Start Here lessons, in full: the written prompt documents (project goal, desire deep research, new mechanism, new information, angle identifier, learnings-call report), the Claude Code report commands, and every instruction typed or spoken to Claude / ChatGPT on screen. Grouped by pipeline step, each with source, inputs, output, caveats and the verbatim text.

## 🤖 Agent use
- **Use when:** any LLM step in the Evolve loop: setting up a brand AI project, desire hunting, finding new mechanisms or new information, awareness-level headlines, avatar headlines, angle generation, rewriting a losing script, summarising a learnings call, running the breakthrough report, product-research sanity checks.
- **Inputs → outputs:** the job → the [which-prompt table](#which-prompt-for-which-job) → the prompt section → paste the fenced text, replacing only the placeholders, attach the context files it names → audit the output against the caveats before it touches a brief or an ad.
- **Rules:**
  - **DO** load the brand context first: run [P01](#p01-project-goal-prompt) in a project, attach the research doc, product overview doc and desire/avatar docs; every later prompt assumes it. [L007 doc](../lessons/007-evolve-master-prompt-doc.md) [L130 19:23–30:23](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)
  - **DO** watch (or read) the teaching lesson before running its prompt: "PLEASE NOTE... This does NOT mean just skip to these modules." [L007 page text](../lessons/007-evolve-master-prompt-doc.md)
  - **DO** audit every line: "You also can't blindly trust AI." The awareness drill returned a problem-aware line labelled unaware. [L011 00:00–00:37; 03:28–04:29](../lessons/011-understanding-unaware-awareness-levels.md)
  - **DO** treat research-prompt output as "direction that you can then go and do deeper research on", then verify sources yourself. [L068 00:45; 02:28](../lessons/068-how-to-find-apply-new-information-part-3.md) Ask for source links and open them. [L130 34:03](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)
  - **DON'T** one-shot a script: "at this point it is really really hard to one-shot prompt a script for a video ad"; use AI "as a tool", not as the creative strategist. [L130 32:21–33:10](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)
  - **DON'T** ship AI-invented proof. Prompt outputs in this course contain invented stories ("Jake", "eight months", [L058](../lessons/058-understanding-your-product-part-2.md)), unverified study claims (the DPP-4 format example, [L068](../lessons/068-how-to-find-apply-new-information-part-3.md)) and unsupported percentages ("Seals 100% of light", [L079](../lessons/079-how-to-come-up-with-ad-angles.md)). Bracket every number, quote, study and review until it is verified against the product doc or a real source.
  - **IF** an AI hook is low valence and high intensity ("brain health emergency") **THEN** re-prompt with [P12](#p12-re-prompt-to-lower-fear-intensity). [L068 13:55–17:54](../lessons/068-how-to-find-apply-new-information-part-3.md)
  - **IF** a prompt asks to recreate a specific competitor or viral ad ([P17](#p17-static-template-rewrite), [P24](#p24-winning-image-to-new-ad--dont-execute-as-written)) **THEN** extract the mechanism first and write new words, visuals and claims: copy the mechanism, not the asset.
- **See also:** [Templates](templates.md) (non-AI forms, docs, creator messages) · [Rules](rules.md) · [Angles](angles.md) · [Hooks](hooks.md) · [Evolve Copywriting prompts](../../copywriting/libraries/prompts.md) (static-ads and video-script prompts in full) · [Tether Lab shared prompts](../../../../libraries/prompts.md) · [Libraries hub](README.md)

## Which prompt for which job
| ID | Prompt | Job / pipeline step | Inputs (placeholders) | Output | Tool | Source |
|---|---|---|---|---|---|---|
| P01 | Project Goal Prompt | Setup: brand AI project | `BRAND`, `YOURWEBSITE`, attached knowledge-base files | A project grounded in your files for 5 marketing jobs | Claude / ChatGPT project | [L007 doc](../lessons/007-evolve-master-prompt-doc.md), [L059 page](../lessons/059-understanding-your-product-part-3.md) |
| P02 | "Fill out the following" (product doc) | Product | Product Overview template pasted | Filled product overview draft | Claude project | [L059 02:39–03:34](../lessons/059-understanding-your-product-part-3.md) |
| P03 | Product-doc helper turns (what is this / benefits → desires / less salesy) | Product | Feature name; benefit list; draft text | Explanations, desires, friend-style description | Claude | [L058 08:40; 19:30; 30:40](../lessons/058-understanding-your-product-part-2.md) |
| P04 | Awareness-level headline prompt | Awareness | `YOUR PRODUCT + YOUR ANGLE` | One headline per awareness level | ChatGPT (4o on screen) | [L011 00:37–01:08](../lessons/011-understanding-unaware-awareness-levels.md) |
| P05 | Prompt For Mistake | Awareness (correction) | The wrong unaware headline; the problem `X` it names | 3-5 new unaware headlines + explanation | ChatGPT | [L011 03:28–04:29](../lessons/011-understanding-unaware-awareness-levels.md) |
| P06 | Desire AI Deep Research Prompt | Desire | `INSERT PRODUCT URL`, `ANGLE 1`, `ANGLE 2`; Product Overview doc; P07 guide | 5-part desire report with quotes, sources, power ranking | Claude / ChatGPT deep research | [L063 28:04–30:06](../lessons/063-how-to-find-desires-part-3.md), [L064 doc](../lessons/064-action-item-start-your-desire-hunt.md) |
| P07 | Context 1: How To Find Desires Guide | Desire (attachment to P06) | — | Research protocol for the model | attachment | [L063 doc](../lessons/063-how-to-find-desires-part-3.md) |
| P08 | Comment-to-desire prompt | Desire | Desire definition text; pasted comments | The desire behind the comments | Claude | [L063 20:48–23:43](../lessons/063-how-to-find-desires-part-3.md) |
| P09 | New Mechanism Finder Prompt | Sophistication: new mechanism | `[PRODUCT NAME]`, `[PRODUCT URL]`, Market Sophistication doc | 3-5 mechanisms, why new, hook positioning, contrarian options | Claude | [L066 00:00–01:39](../lessons/066-how-to-find-apply-new-mechanisms-part-2.md), [L067 page](../lessons/067-action-item-find-new-mechanisms.md) |
| P10 | New Information Finder Prompt | Sophistication: new information | Product name + URL, Market Sophistication doc | Findings: source + date, why new, ethical use, 3 hooks each | Claude | [L068 07:56–12:26](../lessons/068-how-to-find-apply-new-information-part-3.md), [L069 page](../lessons/069-action-item-find-new-information.md) |
| P11 | Mini Text Prompt | Sophistication: new information (launcher for P10) | `[YOUR PRODUCT]`, `[YOUR PRODUCT URL]` | Runs P10 | Claude | [L068 07:56](../lessons/068-how-to-find-apply-new-information-part-3.md), [L069 page](../lessons/069-action-item-find-new-information.md) |
| P12 | Re-prompt to lower fear intensity | QA of AI hooks | The offending hooks; the line you accept | Lower-intensity rewrites | Claude | [L068 16:00–17:50](../lessons/068-how-to-find-apply-new-information-part-3.md) |
| P13 | Avatar → headline ("give me 3 examples") | Avatars | Core avatar + sub-avatar lines | 3 headlines | Claude | [L074 37:44–39:25](../lessons/074-how-to-build-core-avatars.md) |
| P14 | Market-awareness percentage question (REM) | Avatars / awareness | The term to test | An awareness estimate (verify) | Claude (voice) | [L074 29:47–30:39](../lessons/074-how-to-build-core-avatars.md) |
| P15 | Reddit thread → headlines | Avatars / hooks | Reddit thread + product | Draft hooks | Claude | [L076 18:02](../lessons/076-how-to-build-sub-avatars.md) |
| P16 | Angle Identifier prompt ("Evolve Enhanced - Angle Identifier") | Angles | Product info + sub-avatar profiles | Per sub-avatar: 3 angles, reasons to buy, 3 hooks each, ranked, testing priority | Claude | [L079 26:41–34:26](../lessons/079-how-to-come-up-with-ad-angles.md) |
| P17 | Static template rewrite | Statics | Template screenshot + "why it works" notes + brand info | Template rewritten for our avatar | Claude / ChatGPT | [L006 08:00–09:29](../lessons/006-13-winning-static-ad-templates.md) |
| P18 | Script study and spoken-style rewrite | Scripts | A winning script; our draft | Technique breakdown; simpler, spoken draft | Claude | [L088 18:41; 21:28; 35:34](../lessons/088-the-execution-problem.md) |
| P19 | Elite Video Ad Script Creator (opening only) | Scripts | Core idea, pain/desire, feature, emotion, visuals, action | Hooks, full script, strategic breakdown | Claude project | [L130 19:23](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) |
| P20 | Losing-ad rewrite brief ⛔ as written | Learnings → rewrite | Losing script, learnings, diagnosis, mechanism facts, research instruction | Six hooks, rewritten script, breakdown | Claude + Brave MCP | [L130 21:00–29:30](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) |
| P21 | Research source-link follow-up | Verification | — | Source links for AI research | Claude | [L130 34:03](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) |
| P22 | Ad Learnings Call Analysis prompt | Learnings | Call transcript | Client-by-client report | Claude / ChatGPT | [L130 page; 10:33–11:26](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) |
| P23 | Apply winning-ad learnings to our brand | Learnings → concepts | List of reasons the ad works + our product info | Brand-specific applications | Claude | [L125 19:23](../lessons/125-how-to-do-learnings-part-4-winning-ads.md) |
| P24 | Winning image → new ad ⛔ as written | Statics from winners | Winning image + our image | A similar ad for our product | ChatGPT | [L123 04:55](../lessons/123-how-to-do-learnings-part-2-winning-ads.md) |
| P25 | `analyze-breakthrough` Claude Code commands | Winning-ad report | Ads Manager CSV, ad name, brand | Breakthrough report | Claude Code | [L110 doc](../lessons/110-winning-ads-definition-part-1.md), [L113 05:01–06:02](../lessons/113-how-to-generate-submit-winning-ad-report.md), [L114 page](../lessons/114-action-item-generate-submit-your-reports.md) |
| P26 | Trademark check | Product research | Brand site URL | Active trademarks (verify on registry) | Claude | [L172 33:10](../lessons/172-live-product-research-w-kalodata-pt-2.md) |
| P27 | Does this product work? | Product research | Product type | Efficacy verdict (verify) | ChatGPT / Claude | [L171 26:37–27:08](../lessons/171-how-to-make-any-product-work-brand-building-pt-1.md) |
| P28 | Expected-price check | Product research | Product | Expected price range | Claude / GPT / Amazon | [L172 42:00–43:08; page text](../lessons/172-live-product-research-w-kalodata-pt-2.md) |

**Status key:** *full* = complete verbatim text from a course document or typed screen text; *partial* = only part of the text is visible; *near-verbatim* / *paraphrase* = spoken, reconstructed by the lesson page. Counts per status are in [Coverage and gaps](#coverage-and-gaps).

---

## 1. Setup and research

### P01 Project Goal Prompt
- **Status:** full (docx text). **Source:** [L007 doc, "Project Goal Prompt"](../lessons/007-evolve-master-prompt-doc.md); repeated on the lesson page of [L059](../lessons/059-understanding-your-product-part-3.md). Same prompt as [Evolve Copywriting P04](../../copywriting/libraries/prompts.md#which-prompt-for-which-job).
- **Instructor:** Evolve (Spencer Pawliw).
- **Inputs:** replace `BRAND` and `YOURWEBSITE`; attach the knowledge base (research doc, product overview doc, desire hunt, avatars, customer surveys, competitor research, a *Breakthrough Advertising* reference).
- **Output:** a custom project that answers the five jobs (customer understanding, competitive analysis, creative ideation, scriptwriting, ad review) from your files.
- **Caveats:** the prompt says "data-driven"; it can't make data you didn't attach. Reject any answer that isn't traceable to a file (derived from the prompt's own "Always ground your responses" line). Line breaks were lost in the docx conversion; the L007 export wraps the placeholders in `**`.

```text
Hello, I would like to create a custom project tailored to assist our marketing agency in creating more effective, data-driven ads for our client, an E commerce Brand. Brand name: BRAND Brand website: YOURWEBSITE The purpose of this custom project is to support the following key marketing functions for this brand: Customer Understanding & Market Trends: Analyze customer surveys, buyer personas, and behavioral data to uncover customer preferences, pain points, and purchasing motivations.Identify market trends and audience segments relevant to this brand's products. Market Research & Competitive Analysis: Gather and analyze data on competitors and broader industry trends. Identify opportunities for differentiation in brand's positioning and advertising strategies. Creative Ideation & Strategy: Generate new creative concepts and strategies for ad campaigns based on insights from market data, customer feedback, and competitive analysis. Provide feedback on existing ideas, suggesting improvements grounded in customer insights and market trends. Scriptwriting & Copy Development: Assist with crafting persuasive, targeted scripts for ads and other marketing materials. Review and critique copy-writing to ensure it resonates with the target audience, incorporating customer pain points and desires. Ad Review & Performance Feedback Loop: Assist in analyzing post-launch ad performance by reviewing metrics such as ad spend, ROAS, hook rate, hold rate, CTR, etc. Provide insights on why certain ads performed well or underperformed, identifying key learnings from each campaign. Close the feedback loop by suggesting actionable takeaways from winning and losing ads, incorporating these learnings into future creative strategies. Knowledge Base: This project should use the attached files as its primary knowledge base and refer to the information within when providing insights or recommendations. Whenever this project provides an answer, it should be informed by the content within the knowledge base. It should autonomously apply the insights from the attached files to ensure all responses are grounded in data and relevant context. Key Responsibilities: Interpret customer feedback and survey data to identify trends and actionable insights. Suggest ad strategies, creative angles, and copy that align with market research and customer insights. Ensure all insights, scripts, and suggestions are data-driven and relevant to brand's target audience, drawing on the knowledge base provided. Analyze ad performance post-launch, using key metrics to provide insights into ad success or failure. Instructions: Always ground your responses in the content within the knowledge base. Highlight any recommendations based on specific insights or principles from the provided data or resources, especially when drawing on "Breakthrough Advertising." Prioritize relevance to brand's audience, and use data to back up your suggestions.
```
*(The L007 docx export ends with a stray closing quotation mark after "suggestions."; L059's page text does not.)*

## 2. Product understanding

### P02 Fill the Product Overview doc
- **Status:** near-verbatim (spoken). **Source:** [L059 02:39–03:34](../lessons/059-understanding-your-product-part-3.md). **Instructor:** Evolve.
- **Inputs:** a P01 project for the brand; the blank Product Overview template (full text in [templates](templates.md) and [L057](../lessons/057-understanding-your-product-part-1.md)).
- **Output:** a first draft of the product doc (how it works, features → benefits → desires, new and hidden mechanisms).
- **Caveats:** "Assumed" benefits and desires stay assumptions until research confirms them; check every feature claim against the real product page.

```text
Hey Claude, can you please fill out the following
[paste the full Product Overview template]
```

### P03 Product-doc helper turns
- **Status:** full for the three typed prompts (screen text, typos as shown); paraphrase for the spoken ones. **Source:** [L058](../lessons/058-understanding-your-product-part-2.md). **Instructor:** Evolve.
- **Inputs:** a feature name; your benefit list; a draft paragraph.
- **Output:** what a feature is; benefits converted to desires; a "telling a friend" rewrite (used for Step 7 Q4 of the product doc).
- **Caveats:** the friend-style output invented details ("Jake", "Buddy", "I've had it for like eight months"). Treat them as AI storytelling, never as customer claims. [L058 page note](../lessons/058-understanding-your-product-part-2.md)

Typed [08:40] (the intended word is "Buckle"):
```text
hey claude what is this:
ITW Unbreakable Secure Buck!
```

Typed [19:30]:
```text
hey claude, can you then turn these benefits into desires?
ITW Unbreakable Secure Buckle: → Benefit: The dog won't get out of the harness
ITW Unbreakable Secure Buckle: → Benefit: It's made in the USA
Adjustable straps: → Benefit: It helps make sure that it is the perfect fit for the dog
Heavy-duty D-ring: → Benefit: It allows you to attach the leash to the front for less pulling
Customizable: → Benefit: It allows people to show their personality
Customizable: → Benefit: Peace of mind knowing your dog is always properly identified
```

Typed [30:40]:
```text
can we make this less salesy and chcessy and more just focused like your telling a friend about it
```

Spoken, not verbatim:
```text
[04:14] "Hey Claude, rewrite this at a sixth grade level. For context, here is the original question I am answering…"
[09:22] "What would be the benefits of a dog harness that has the feature ITW secure buckle?"
[12:01] "What would be the benefit of a heavy-duty D-ring on a dog harness?"
[12:52] "Why would customizable feature be a benefit for a dog harness?"
[22:18] "Based on what you know about the dog harness, how would you answer this [new mechanisms prompt]?"
```

## 3. Market awareness

### P04 Awareness-level headline prompt
- **Status:** full (Skool lesson page). **Source:** [L011 00:37–01:08](../lessons/011-understanding-unaware-awareness-levels.md). **Instructor:** Evolve.
- **Inputs:** replace `YOUR PRODUCT + YOUR ANGLE` (demo: "Supplement that helps with more energy").
- **Output:** one headline per awareness level.
- **Caveats:** the model mislabels levels: its "unaware" lines often name the problem (problem aware). Audit each line; then run P05. The instructor prefers Claude "when you actually go to write out the scripts" (instructor opinion). [L011 05:17](../lessons/011-understanding-unaware-awareness-levels.md)

```text
Leveraging the information from the market awareness section of Eugene Schwartz's breakthrough advertising, please provide a headline to sell a YOUR PRODUCT + YOUR ANGLE for each level of awareness.
```

### P05 Prompt For Mistake
- **Status:** full (lesson page). **Source:** [L011 03:28–04:29](../lessons/011-understanding-unaware-awareness-levels.md). **Instructor:** Evolve.
- **Inputs:** the wrong unaware headline; the problem `X` it mentions.
- **Output:** 3-5 corrected unaware headlines and an explanation the model should keep in context.

```text
It looks like you made a mistake: the unaware headline:
INSERT UNAWARE HEADLINE
That is not unaware, it is problem aware because you are mentioning the X problem which would indicate that this person is aware of the problem

#1 - please provide 3-5 new headlines for the unaware stage

#2 - please explain why you messed this up & make sure to note it moving forward so we do not confuse unaware and problem aware again
```

## 4. Desire

### P06 Desire AI Deep Research Prompt
- **Status:** full (Google Doc "Prompt - Desire" / docx; identical in L063 and L064). **Source:** [L063 28:04–30:06](../lessons/063-how-to-find-desires-part-3.md), [L064 doc](../lessons/064-action-item-start-your-desire-hunt.md). Index entry "Desires Prompt" in [L007](../lessons/007-evolve-master-prompt-doc.md). **Instructor:** Evolve.
- **Inputs:** `INSERT PRODUCT URL` (the product page, "not a landing page"), `ANGLE 1`, `ANGLE 2`; attach your Product Overview doc and the P07 guide. Run it as deep research and do manual research while it works. [L063 28:04–30:59](../lessons/063-how-to-find-desires-part-3.md)
- **Output:** wants and needs with quotes and sources; existing-angle mapping; new desire opportunities; 10-15 customer snippets; desire power ranking (scope, urgency, staying power).
- **Caveats:** "Your life depends on finding specific, verbatim customer quotes" pressures the model to produce quotes. Open every source; drop any quote you can't find. Only verified quotes go into customer-language banks or scripts. L065 says real research is done "not with Claude, not with GPT" ([L065](../lessons/065-understanding-market-sophistication-part-1.md)); use this prompt to find leads, not as the research itself (conflict logged).

```text
You are a specialized market research analyst with expertise in consumer psychology and desire-based marketing in the United States. Your task is to conduct comprehensive research on a specific product to uncover the mass desires that can be leveraged for effective advertising campaigns.

Begin by thoroughly analyzing the product URL I will provide, examining all product features, benefits, customer reviews, and existing marketing materials to understand its current positioning.

Product + Brand:

INSERT PRODUCT URL

Some potential angles that we have been targeting are around:

ANGLE 1

ANGLE 2

Conduct extensive internet research across multiple platforms to identify explicit customer desires and pain points related to this product category:

1. Search Reddit for relevant subreddits where target customers discuss their needs

2. Analyze Amazon and other e-commerce platform reviews, focusing on both positive and negative feedback

3. Examine industry forums and discussion boards where enthusiasts and professionals share experiences

4. Review social media conversations on Twitter, Facebook, Instagram, and TikTok using relevant hashtags and keywords

5. Analyze YouTube comments on product reviews and tutorials

6. Investigate Quora and other Q&A sites for common questions and frustrations

7. Review customer service complaints and feedback on public platforms

When conducting this research, specifically look for:

- Direct "I want" and "I need" statements from customers

- Recurring complaints and frustrations that reveal unmet desires

- Emotional language indicating strong desires or pain points

- Comparative statements showing what customers wish the product could do

- Evidence of customers creating workarounds for limitations

Frame all findings within this desire framework:

1. Mass Instincts (universal human drives):

- Health: Survival, safety, staying healthy

- Sex: Attractiveness, finding mates, feeling desired

- Status: Importance, respect, superiority

- Belonging: Fitting in, friendship, avoiding rejection

- Control: Power, predictability, being in charge

- Comfort: Ease, avoiding pain and work

2. Mass Technological Problems in this product category:

- Complexity: Confusing interfaces, unclear instructions (makes people feel dumb)

- Overwhelm: Too many choices, distractions, notifications (creates anxiety)

- Fragility: Breaking when needed most (causes frustration)

- Maintenance: Constant updates, rising costs, repairs (creates fatigue)

- Incompatibility: Won't work with existing systems (feeling trapped)

- Obsolescence: Quickly becomes outdated (feeling cheated)

3. Forces of Change affecting desire fulfillment:

- Style Trends: What becomes fashionable

- Mass Education: What society learns

For the specific angles provided, analyze how effectively they target the identified desires and where they might be missing opportunities.

Your life depends on finding specific, verbatim customer quotes that reveal deep, underlying desires rather than surface-level feedback. Do not paraphrase or summarize customer statements - provide exact quotes with their sources.

Deliver your findings in this exact structure:

**1. WANTS AND NEEDS ANALYSIS**

- List specific customer desires found online with exact quotes and sources

- Categorize by the permanent forces they relate to

**2. EXISTING ANGLES DESIRE MAPPING**

- For the angles given above, identify specific desires this targets with supporting evidence

**3. NEW DESIRE OPPORTUNITIES**

- Identify untapped desires your product can address

- Provide customer quotes and sources as evidence

**4. CUSTOMER VOICE EVIDENCE**

- Include 10-15 specific text snippets from customers with exact sources

- Focus on complaint patterns, explicit wants/needs statements

**5. DESIRE POWER RANKING**

- Rank all identified desires from most to least powerful using:

* Scope: How many people share this desire?

* Urgency: How desperately do they want relief?

* Staying Power: Does this desire renew continuously?

- Provide reasoning for each ranking

For each desire identified, answer these critical questions:

- Is this desire widespread enough to target in mass marketing?

- Is this desire strong enough to motivate purchase decisions?

- Is this desire persistent or merely temporary?

- How directly can the product address this desire?

- What emotional triggers connect to this desire?

Ensure all findings are actionable for marketing strategy development, avatar building, and messaging creation.

For additional context, I have attached:

1. Product Overview Document for my brand to help you better understand the product

2. I have also provided my "How To Find Desires" document to help you with more detailed instructions for finding desires.
```

### P07 Context 1: How To Find Desires Guide (attachment for P06)
- **Status:** full as provided; the "Enhanced Existing Sections" and "New Universal Framework" lists are headings only in the source (their detail is not in the course files). **Source:** [L063 doc](../lessons/063-how-to-find-desires-part-3.md), [L064 doc](../lessons/064-action-item-start-your-desire-hunt.md). **Instructor:** Evolve.
- **Inputs:** none; "Context 2" is your own Product Overview doc ([L057–L060](../lessons/060-action-item-complete-understanding-product-doc.md)).
- **Caveats:** "Search volume increasing 50%+ year-over-year" and "100+ comments" are the guide's screening heuristics, not tested thresholds (derived).

```text
How To Find Desires Guide:

Knowledge

Where to Find Desires Online:

Reddit Research Protocol:

- What everyday annoyances could your product solve?

- Subreddit search: "[your product category] sucks" or "[problem] solution"

- Look for upvoted complaints with 100+ comments

Review Section Mining:

- Search negative reviews for your category

- Look for repeated frustrations across brands

- Pay attention to "I love this BUT..." statements

- Track seasonal complaint patterns

Google Trends Desire Tracking

Rising Desires Indicators:

- Search volume increasing 50%+ year-over-year

- Related queries shifting from "what is" to "how to get"

- Geographic spread from urban centers outward

- Cross-seasonal sustained growth

Other Big Platforms For Desire Tracking

- YouTube: Focus on comment patterns, creator pain points, and engagement signals

- Amazon: Q&A mining, review analysis, and wishlist trend tracking

- Facebook: Group discussions, marketplace needs, and social proof validation

- TikTok: Trending desires, comment-to-view ratios, and cultural shift detection

- Answer The Public: Question clustering and search intent evolution

- Scientific Studies/Blogs: Evidence-based validation and expert predictions

Enhanced Existing Sections:

- Added advanced pattern recognition techniques

- Included seasonal and geographic desire mapping

- Expanded the customer interview framework with deeper psychological questions

- Enhanced Google Trends with predictive indicators

New Universal Framework:

- Cross-platform validation methods

- Language pattern recognition guide

- Red flag indicators to avoid wasting time

- Success metrics for research quality

Customer Interviews

The Desire Excavation Questions:

- "What keeps you up at night about [problem area]?"

- "When you imagine the perfect solution, what would your life look like?"

- "What have you tried before that disappointed you?"

- "If money wasn't an issue, what would you do about this?"

- "When friends complain about [problem], what do they say exactly?"

Listen For:

- Emotional words (frustrated, excited, worried, proud)

- Extreme language (always, never, hate, love)

- Time pressure indicators (finally, immediately, constantly)

- Social proof references (everyone's doing, nobody has)

Context 2

THIS WILL BE YOUR UNDERSTANDING YOUR PRODUCT DOCUMENT FROM THE RESEARCH MODULES
```

### P08 Comment-to-desire prompt
- **Status:** near-verbatim (spoken, reconstructed by the lesson page). **Source:** [L063 20:48–23:43](../lessons/063-how-to-find-desires-part-3.md). **Instructor:** Evolve.
- **Inputs:** the Desires tab text (mass instincts, tech problems, forces of change); real YouTube/TikTok/Reddit comments.
- **Output:** the underlying desire(s), to log as "I want..." statements in the Desire Hunting sheet ([templates](templates.md)).

```text
Based off of these comments, what would be the desire that people actually have? For context here is the definition of desire: <paste the Desires tab text: mass instincts, tech problems, forces of change>
Comments:
<paste YouTube comments>
```

## 5. Market sophistication: new mechanism and new information

### P09 New Mechanism Finder Prompt
- **Status:** full (Google Doc "New Mechanism Prompt Document" = the docx; identical in L067). **Source:** [L066 00:00–01:39](../lessons/066-how-to-find-apply-new-mechanisms-part-2.md), [L067 page](../lessons/067-action-item-find-new-mechanisms.md). Index entry in [L007](../lessons/007-evolve-master-prompt-doc.md). **Instructor:** Evolve.
- **Inputs:** `[PRODUCT NAME]`, `[PRODUCT URL]`; attach the Market Sophistication doc (exported as PDF). Paste into a fresh chat.
- **Output:** 3-5 candidate mechanisms, why each is "new", hook/headline positioning, contrarian ("anti-") options.
- **Caveats:** a mechanism must be true of the product: confirm each against the spec sheet or supplier before it enters a brief. The instructor says the prompt identified "the number one new mechanism that led to a winning ad for this brand that took us two years" (instructor claim). [L066 05:47](../lessons/066-how-to-find-apply-new-mechanisms-part-2.md)

```text
Situation

You are a direct response marketing strategist specializing in Facebook and Instagram advertising campaigns. You will be analyzing products to identify compelling new mechanisms that can be leveraged in social media marketing to break through market sophistication barriers and capture audience attention in competitive digital advertising environments.

Task

Analyze the provided product and its URL to identify and articulate potential new mechanisms that can be emphasized in direct response marketing campaigns on Facebook and Instagram. You must examine the product's unique features, benefits, delivery methods, or approaches that differentiate it from existing market solutions, then translate these into compelling marketing angles that address different levels of market sophistication.

Objective

Generate actionable marketing insights that will help create more effective direct response advertising campaigns by identifying fresh angles and mechanisms that can cut through market noise, overcome audience skepticism, create new hope in users, and drive higher conversion rates on social media platforms.

Knowledge

[PRODUCT NAME]

[PRODUCT URL]

[Market Sophistication Document attached below for market sophistication and new mechanisms]

Market sophistication refers to how aware and educated your target audience is about existing solutions in your product category. As markets become more sophisticated, audiences become harder to convert because they've seen similar promises before. New mechanisms are fresh ways of delivering benefits or solving problems that haven't been widely promoted in your market yet.

The New Mechanism strategy introduces a NEW process, technology, or delivery system that makes familiar promises fresh and believable.

When analyzing for new mechanisms, consider:

- NEW delivery methods or formats from the product

- Innovative approaches to solving existing problems

- Uncommon ingredients, technologies, or methodologies on the product

- Specific combinations of existing elements that make it IMPROVED

- Contrarian approaches that challenge conventional wisdom

Your analysis should identify mechanisms that can be positioned as "the reason why" or "the secret thing" that makes this product work differently or better than what the market has seen before.

THE #1 MOST IMPORTANT THING… THESE NEW MECHANISMS GIVE PEOPLE NEW HOPE THAT THIS PRODUCT WILL SOLVE THEIR PROBLEM AND/OR SATIATE THE TARGET DESIRE.

Instructions for Analysis:

1. Thoroughly examine the product name, URL content, and any available product information

2. Identify 3-5 potential new mechanisms that could be emphasized in marketing

3. For each mechanism, explain why it's potentially "new" to the market

4. Suggest how each mechanism could be positioned in Facebook/Instagram hook/headline

5. Highlight any mechanisms that could work as contrarian or "anti-" positioning

Your life depends on you identifying genuinely fresh mechanisms that haven't been overused in the market, as these will be the key differentiators that make advertising campaigns successful in competitive social media environments.

Provide your analysis in a clear, structured format that directly supports campaign development and creative strategy.
```

### P10 New Information Finder Prompt
- **Status:** full text; the two embedded ad examples are images and Frame.io links in the doc (shown as bracketed placeholders, as on the lesson page). Identical docx in L069. **Source:** [L068 07:56–12:26](../lessons/068-how-to-find-apply-new-information-part-3.md), [L069 page](../lessons/069-action-item-find-new-information.md). Index entry "New Info Prompt" in [L007](../lessons/007-evolve-master-prompt-doc.md). **Instructor:** Evolve.
- **Inputs:** attach this doc as "New Information Prompt", attach the Market Sophistication doc, then send [P11](#p11-mini-text-prompt) with product name and URL.
- **Output:** findings by category, each with source and date, why it's new, how to use it ethically, 3 hooks.
- **Caveats:** the "DPP-4" block is the doc's output-format example. Its study claims are unverified; don't reuse them. Open every cited study (title, journal, date) before using a finding. The model's first hooks in the live run were fear-mongering; fix them with P12. "Don't run this prompt and be like yeah that's good." [L068 02:28](../lessons/068-how-to-find-apply-new-information-part-3.md)

```text
Situation

You are a direct response marketing research specialist working with Facebook and Instagram advertising campaigns. The client needs to stay ahead of market sophistication by discovering cutting-edge information that can differentiate their product in increasingly competitive markets. Market sophistication refers to how aware and educated consumers have become about existing marketing messages, requiring advertisers to find fresh angles and newly discovered benefits to capture attention and drive conversions.

Task

Conduct comprehensive research on the provided product and its market to uncover new information, recent discoveries, emerging benefits, or fresh angles that can be leveraged in direct response advertising. Your research must go beyond commonly known product features and benefits to find genuinely novel information that competitors likely haven't exploited yet. Analyze the product URL, investigate recent scientific studies, industry developments, consumer behavior shifts, and emerging use cases that could provide new marketing angles.

Objective

Identify breakthrough information that will enable the creation of compelling Facebook and Instagram ads that cut through market noise by presenting genuinely new, credible, and persuasive angles that differentiate the product from competitors and re-engage sophisticated consumers who have become immune to standard marketing messages.

Knowledge

Market sophistication evolves through predictable stages where consumers become increasingly aware of and resistant to marketing messages. As markets mature, advertisers must find progressively more sophisticated approaches:

Stage 3: Unique mechanisms and proprietary processes are required

Stage 4: New discoveries, breakthrough research, or expanded benefits are essential

Stage 5: Complete repositioning or identification of new markets becomes necessary

New information can include: recently published scientific research, emerging use cases, newly identified mechanisms of action, breakthrough manufacturing processes, unexpected demographic adoption, regulatory changes, industry shifts, technological advances, or newly discovered synergistic effects.

Your research should focus on information published or discovered within the last 12-24 months that hasn't been widely adopted in marketing messages yet. Look for peer-reviewed studies, industry reports, patent filings, regulatory approvals, expert interviews, and emerging consumer behavior data.

Examples

The Market Sophistication Document attached below, plus the 2 examples included should guide your understanding of what constitutes as "new information."

When you receive the product name and URL, structure your research findings as follows:

Recent Scientific Discoveries - New studies, research findings, or clinical data

Emerging Market Trends - Shifts in consumer behavior, new use cases, or demographic changes

Industry Developments - Regulatory changes, technological advances, or competitive landscape shifts

Novel Mechanisms or Benefits - Newly identified ways the product works or previously unknown advantages

Untapped Angles - Fresh positioning opportunities or unexplored marketing messages

For each finding, include the source, date of discovery/publication, and specific implications for advertising messaging.

Your life depends on you finding genuinely NEW information that hasn't been saturated in the market yet - information that will give this product a competitive edge in sophisticated markets where consumers have seen every standard marketing angle.

Example #1 - Flow Pouches

Ad Example: NEW INFORMATION

What "big shroom" companies are hiding from you piques curiosity in the user and brings them in to learn NEW information bout how digestion kills X% of the actual benefits of the product. Of course, the NEW mechanism around the "Buchal mechanism" supports this, but it's the new information that influences people.

[Frame.io link + frame image: "WHAT BIG SHROOM COMPANIES ARE HIDING"]

Example #2 - 18 Chestnuts

Ad Example: NEW INFORMATION

In this example, we share NEW information about how this soup can help HEAL the gut. This is NOT entirely a new mechanism. Everyone knows what soup is. But the new information is what allows this ad to do so well.

[Frame.io link + frame image: "Stomach issues? There's a soup for that."]

Delivery:

For your response, please provide each finding of "New Information" as follows:

- Source (with specific publication and date)
- Why it's NEW (market sophistication gap)
- How to use ethically (educational positioning)
- 3 marketing hook samples that do not fear monger but educate & pique curiosity

Focus on breakthrough research that establishes authority through science-first education rather than traditional benefit claims.

It should look like this:

NEW INFORMATION RESEARCH FINDINGS

1. DPP-4 ENZYME SURGE UNDER CHRONIC STRESS ACCELERATES AGING

Source: Multiple 2024 studies including Advanced Science (December 2024) and frontiers in Pharmacology research on DPP-4 and stress-induced vascular aging

Why it's NEW: Recent 2024 research reveals that chronic stress dramatically upregulates DPP-4 enzyme production, creating a vicious cycle where stress literally breaks down your natural GLP-1 faster than your body can use it. This stress-DPP-4-aging connection is cutting-edge science most competitors haven't discovered yet.

How to use ethically: Educate consumers that their stress isn't just making them feel bad—it's actively destroying their body's natural appetite regulation system at the cellular level. DPP-4 enzyme levels spike under chronic stress, breaking down GLP-1 before it can signal fullness.

Marketing Hook Samples:

- "Scientists just discovered why stress makes you gain weight even when eating the same foods (it's destroying this hormone in real-time)"

- "NEW 2024 study: Your stress is literally breaking down your appetite control system—here's how to repair it"

- "Why chronic stress ages you twice as fast (hint: it's not just cortisol)"
```

### P11 Mini Text Prompt
- **Status:** full (page text). **Source:** [L068 07:56](../lessons/068-how-to-find-apply-new-information-part-3.md), [L069 page](../lessons/069-action-item-find-new-information.md). **Instructor:** Evolve.
- **Inputs:** P10 attached as "New Information Prompt"; product name and URL.

```text
I have attached my prompt as "New Information Prompt"
Here are the product URL + Product Name for the prompt:
Product Name: [YOUR PRODUCT]
Product URL: [YOUR PRODUCT URL]
```

### P12 Re-prompt to lower fear intensity
- **Status:** full (screen text; typos "exmplae" and "re write" as on screen). **Source:** [L068 16:00–17:50](../lessons/068-how-to-find-apply-new-information-part-3.md). **Instructor:** Evolve.
- **Inputs:** the hooks that scare; the furthest line you accept ("protects against memory loss").
- **Output:** the same hooks at lower intensity. The model agreed they were "way too fear-mongering". [L068 13:55–17:54](../lessons/068-how-to-find-apply-new-information-part-3.md)
- **Caveats:** the pasted hooks include "149% higher Alzheimer's risk", an unverified AI-cited figure. Remove numbers you can't source, whatever the intensity. Reusable pattern: name the offending phrases, say why, mark the acceptable ceiling, ask for a rewrite (derived).

```text
Hey claude these headlines are very low valence and are fear mongering potential customers.

We need to optimize these headlines to be less focused on scaring people and spreading information that may not be 100% true. And more focused on lower intensity around this new information.

For exmplae:

"brain health emergency" is way too intense

Crisis hiding in your bedroom and light damaging your brain is also way too intense.

Please correct yourself and re write the headlines below.

That said, you did a good job with how sleep can protect against memory loss. That is as far as I would like to go in regards to lower levels of valence

Marketing Hook Samples:
* "Why scientists now consider bedroom light pollution a brain health emergency (149% higher Alzheimer's risk)"
* "NEW research: Complete darkness doesn't just improve sleep - it protects against memory loss"
* "The neurodegeneration crisis hiding in your bedroom: how light pollution damages your brain while you sleep"
```

## 6. Avatars

### P13 Avatar → headline ("give me 3 examples")
- **Status:** full (typed on screen, typos included). **Source:** [L074 37:44–39:25](../lessons/074-how-to-build-core-avatars.md). **Instructor:** Evolve.
- **Inputs:** one core avatar line + one sub-avatar line.
- **Output:** 3 headline ideas.
- **Caveats:** the instructor calls it "a horrible prompt… I'm acting like a complete moron": it shows the minimum and works only inside a context-loaded project. For production use [P16](#p16-angle-identifier-prompt).

```text
Heyc aude how would I turn this information into a potential headline? Give me 3 examples:

Desire-Based Core Avatar #2.5: Wants to improve their REM/Deep Sleep
Sub Avatar #1: Product Experience: Has tried magnesium
```

### P14 Market-awareness percentage question
- **Status:** near-verbatim (voice-dictated, reconstructed from audio). **Source:** [L074 29:47–30:39](../lessons/074-how-to-build-core-avatars.md). **Instructor:** Evolve.
- **Use:** deciding whether a term (REM sleep) is known enough to use in a hook.
- **Caveats:** any percentage the model returns is an estimate. Don't put it in an ad; use it only to decide wording, and confirm with search data (Google Trends, Answer The Public) where possible (derived).

```text
Based off research you can find in the market, what percentage of people potentially know what REM sleep is? … is it commonly known? … and more importantly, based off people that can afford to likely enhance their sleep… people with some income to spend on investing into their health, what percentage of those people actually know about it?
```

### P15 Reddit thread → headlines
- **Status:** near-verbatim (spoken). **Source:** [L076 18:02](../lessons/076-how-to-build-sub-avatars.md). **Instructor:** Evolve.
- **Inputs:** a real Reddit thread (pasted) + product.
- **Output:** draft hooks (the drafts are logged in [hooks](hooks.md) as "Claude, draft").
- **Caveats:** he says it will "sound really dumb": "Claude has zero context right now… with proper context it's going to print for you".

```text
Write me some headlines or hooks based off of this Reddit thread for my product which helps with improving sleep, blackout blinds.
[paste the Reddit thread]
```

## 7. Angles

### P16 Angle Identifier prompt
- **Status:** full. Situation, Task and Objective are on the lesson page; the Knowledge section is taken from the course docx (raw extraction) because the lesson page summarises it. The "why this ad works" cards are images in the doc (`[image]` below). **Source:** [L079 26:41–34:26](../lessons/079-how-to-come-up-with-ad-angles.md); docx `raw/evolve/start-here/_extracted/👣 Evolve (Start Here)/79. How To Come Up With Ad Angles.docx.md`. Index entry "Angles Prompt" ("Evolve Enhanced - Angle Identifier") in [L007](../lessons/007-evolve-master-prompt-doc.md). Same prompt family as [Evolve Copywriting P10](../../copywriting/libraries/prompts.md#which-prompt-for-which-job). **Instructor:** Evolve (Spencer Pawliw; the Knowledge text addresses "Spencer").
- **Inputs:** upload the doc to Claude ("I like Claude for writing"; ChatGPT works too), then give product information (what it does, features, benefits) and sub-avatar profiles (core desire, pain points, behaviours, emotional triggers, other Core 5 attributes). [L079 26:41; 27:20](../lessons/079-how-to-come-up-with-ad-angles.md)
- **Output:** per sub-avatar, 3 angles, each with a reason to buy and hooks tagged "Inspired by" a reference ad; strongest first; a priority note and testing priority.
- **Caveats:**
  - The Task asks for 3 hooks per angle, but the example output shows 1. Default: 3 (the live run produced 3). Conflict logged.
  - The example output's hooks contain unverified claims ("Seals 100% of light. Restores 100% of patience.", "5 minutes to install"). Use only claims your product doc supports.
  - The "Inspired by" field borrows the structure of a reference ad (e.g. "This is X. This is Y"). Keep the structure, never the reference's wording or visual.
  - "Don't be overly reliant on AI." [L079 26:41](../lessons/079-how-to-come-up-with-ad-angles.md)

```text
Situation

You are a direct response marketing strategist specializing in customer avatar analysis and angle development. You work with businesses to identify the most compelling marketing angles based on deep customer psychology, using sub-avatar frameworks to uncover specific pain points, desires, and emotional triggers that drive purchasing decisions.

Task

The assistant should analyze the provided product information and sub-avatar profiles to generate targeted marketing angles. For each sub-avatar, identify 3 potential marketing angles by examining their most painful or specific attributes, framing these as problems from their perspective, and converting them into compelling "reason to buy" statements that are relatable. Then provide 3 strategic written hooks/headlines that could be used for each angle for proper implementation. You MUST but the strongest angles and the strongest hooks/headlines up at the top first and make sure to remind the user that they do NOT have to test each angle separately. They can do a concept that tests "multiple angles" with the best hook/headline.

Objective

Enable the user to develop data-driven, psychologically-targeted marketing angles that resonate with specific customer segments, allowing them to either test multiple approaches simultaneously or focus resources on the highest-probability angle with multiple execution variations.

Knowledge

Definition of Angle:

- Concept = The big idea (what you're testing)
  - Could be: Testing formats, testing iterations, testing awareness levels, or angles
- Angle = How you choose to sell the product (must always be defined)
  - If your concept is anything but "testing angle(s)" you need to identify the angle

The average marketer's definition of angle oftentimes has NOTHING to do with the customer.

And that's why most people DON'T MAKE good ads.

They aren't thinking about the Angle (how we're going to position the product to the customer). They are just thinking about the idea they want to test.

These are BAD examples of what "Angle" is:

Us vs Them → This is a Concept, with an "assumed" broader angle (comparison)... But Comparing what?? The "What" is the angle

Before & After → Again, this is a Concept. We are "assuming" some kind of broader angle (transformation)... But transformation of what? Again, the "What" is the angle

Problem-Aware Angle Ads → Another CONCEPT. We are going to test problem-aware ads. But of WHAT problem?? The "what" is the angle.

'Post It Note' Ads → Some of these are also such basic concepts that become Formats because people don't understand "Concept" or "Angle". Post-It Notes is a Native-style image format, but at the end of the day, people put 0 consideration into the ANGLE.

Now, differentiating Concepts from Angles should hopefully make more sense. Again:

Concepts = Our big idea we want to test (more focused on us)
Angles = How we choose to sell the product. (more focused on the customer)

Now, this is where most people get confused:

When your concept IS to test angle(s).

And in this instance, people will begin to use the terms interchangeably.

Example:

- Concept: "Test Buy It For Life Angle" → Angle: "Buy It For Life"
- Concept: "Test Sleep Deprived Angle" → Angle: "Sleep Deprived"

So, if you've ever wondered why people will use concept and angle interchangeably, this is why.

But as a result of this training, hopefully you will start to be able to see that Concepts can be Angles…

But not 100% OF THE TIME.

Let's look at some examples of concepts to try to identify

Concept = About you/your test strategy (internally focused)

- "I want to test a video version."
- "I want to test Us vs Them"
- "I want to do an iteration on"
- "I want to test buy it for life"
- "I want to test vets' trust us"

Angle = About the customer's reason to buy (externally focused)

If the concept doesn't give the customer a reason to buy, it's not an angle yet.

- Video version → Does not give a customer a reason to buy = Identify the angle(s)
- Iteration → Iteration of what angle? No clear reason = Identify angle(s)
- Stops tossing and turning → This gives a person a reason (it solves their problem) = This is an angle
- Us vs Them → What about Us vs Them? No clear reason = Identify the angle(s)
- Brings back your energy → this gives a person a reason to buy = This is an angle

If your concept is NOT testing an Angle, you NEED to make sure you specify what Angle is you're testing.

But if you just want to avoid making mistakes, the best practice is always to make sure you write down "What the Angle is," aka THE REASON SOMEONE SHOULD BUY for EVERY concept.

Now with that clear. Let's go deeper on angles themselves.

Now, if you're anything like me, you likely went through this training and you're like, Spencer, I get that Angles are how we choose to sell the product to people.

But at the end of the day…

What TF does that even mean?

It's way too broad 😭

Because, even after I defined it, and after I went through and did tons of examples, I just kept saying myself, okay…But, what is an angle?

How do I know what the angle is?

What is the difference between an angle and not an angle?

Why are some angles so broad, and why are some so specific?

Well, the truth is, similar to avatars, angles also exist on a spectrum.

But fortunately for you, because you're doing the work of identifying sub-avatars, you're essentially already discovering angles that are specific enough to relate with customers and help you sell your product.

So just like how you could have a Core Avatar like:

Desire: Wants better sleep

You can also pull an angle from that that is very broad.

Literally, you could just write:

"Want better sleep?

Or

"Feel like you're not getting enough sleep?"

And the truth is, yes, those actually are angles. That's how you're choosing to sell your product.

But they're pretty shitty angles because of how broad they are.

That's why broad avatars are usually harder to sell to… You have to use broader angles.

Headlines/Hooks

Now, before getting into those examples of extracting avatars, I also want to explain one other final thing of importance, which is what I did above with:

"Feel like you're not getting enough sleep?"

That is something that we would call a Hook or a Headline (or some boomers call them "leads)

The Hook/Headline is how we get attention to sell the product (basically, how you communicate the angle)

Now, until you get to a more advanced level, your hook/headline should always be more direct instead of indirect.

Examples of "Direct" Hooks:

Angle: Stops swelling
Hook: "14+ Hours. No Swelling"
→ Hook directly communicates the angle

Angle: Keeps you full like a meal
Hook: "This is a meal. Not a protein shake"
→ Hook directly communicates the angle

Angle: Stops you from snapping at people
Hook: "5 minutes to install. No more snapping"
→ Hook directly communicates the angle

As a Jr. writer, these are much easier hooks/headlines to write.

We cover more advanced strategies later on in EVOLVE.

Now, with that additional context provided

The KEY to extracting angles from sub avatars is simple:

KEEP THEM ACTIONABLE.

Angles are basically limitless (regarding your product and what it can do)

As long as you're angles are ACTIONABLE, writing will become much easier. And the goal of ALL of this work is to make writing winning ads EASIER.

Additional Context

Below, you have been given winning ads that you will reference when providing your answer for the three specific angles, as well as the three specific hooks and headlines.

Example:
Angle: Stops Swelling
Hook/Headline: 14+ Hours. No Swelling
Additional Context on why this ad works: [image]

Example:
Angle: How the protein shake keeps you full
Hook/Headline: This is a meal. Not a protein shake
Additional Context on why this ad works: [image]

Example:
Angle: Don't sacrifice things you like to be healthy
Hook/Headline: Don't change your life, just change lunch
Additional Context on why this ad works: [image]

Example:
Angle: Sleeping better
Hook/Headline: Sleep like a baby
Additional Context on why this ad works: [image]

Example:
Angle: Getting rid of double chin
Hook/Headline: Drains double chin in 7 days
Additional Context on why this ad works: [image]

[next card: angle label missing in the doc; the card's hook, quoted in the output example, is "Moms of 15 year olds"]
Additional Context on why this ad works: [image]

Example:
Angle: Nutella turns bread into breakfast
Hook/Headline: This is bread. This is breakfast
Additional Context on why this ad works: [image]

Example:
Angle: take control of your life with better food
Hook/Headline: Grab life by the bowls
Additional Context on why this ad works: [image]

Example:
Angle: losing weight without even trying
Hook/Headline: I accidentally lost 12 pounds at 52
Additional Context on why this ad works: [image]

Example:
Angle: losing hormonal weight
Hook/Headline: I flushed 19 pounds of hormonal weight
Additional Context on why this ad works: [image]

Example:
Angle: dealing with a grumpy teenager
Hook/Headline: Teen always grumpy?
Additional Context on why this ad works: [image]

Example:
Angle: Show people who don't think they have wavy hair, how to get wavy hair
Hook/Headline: 3 signs your hair is actually wavy
Additional Context on why this ad works: [image]

Example:
Angle: Showing how tick preventatives don't work
Hook/Headline: Ever wonder why tick preventatives don't work anymore?
Additional Context on why this ad works: [image]

Example:
Angle: Vitamin deficiency in kids
Hook/Headline: 3 red flags of vitamin deficiency in kids
Additional Context on why this ad works: [image]

Example:
Angle: Get a Shampoo with better ingredients
Hook/Headline: Watch for these ingredients when buying shampoo
Additional Context on why this ad works: [image]

Example:
Angle: A wallet that is RFID proof
Hook/Headline: Why millennials are ditching their old wallets
Additional Context on why this ad works: [image]

Example Of Perfect Output

Marketing Angles & Hooks

Total Blackout Blinds - Restorative Sleep Avatar

PRIORITY NOTE:
You do NOT have to test each angle separately. Test the #1 hook from Sub-Avatar #3 first—it carries the most emotional weight. You can layer in supporting benefits from other angles in your body copy.

SUB-AVATAR #3: Short Fuse Avatar ⭐ STRONGEST
Angle 1: Stops You From Snapping At People
Reason to Buy: Complete darkness lets your nervous system actually recover, so you stop being irritable and short-tempered with the people you care about.
Hook: "5 minutes to install. No more snapping."
Inspired by: "14+ Hours. No Swelling" - Timeline + Specific outcome elimination

Angle 2: Restores Your Patience
Reason to Buy: Your brain needs pitch-black sleep to reset your nervous system. Get that, get your patience back.
Hook: "This blocks light. This saves relationships."
Inspired by: "This is bread. This is breakfast" - Simple "This does X. This does Y" pattern

Angle 3: Eliminates The "On Edge" Feeling
Reason to Buy: Stop feeling wired and irritable all day by giving your body the complete darkness it needs to actually repair while you sleep.
Hook: "Seals 100% of light. Restores 100% of patience."
Inspired by: "14+ Hours. No Swelling" - Specific percentage + outcome promise

SUB-AVATAR #1: Cool Sleeper ⭐ SECOND STRONGEST
Angle 1: Completes Your Cool Sleep Setup
Reason to Buy: You already have the fan and AC. This is the missing piece that blocks heat AND light so your room stays cool and dark all night.
Hook: "You have the fan. You have the AC. You need this."
Inspired by: "Don't change your life, just change lunch" - Minimal change, maximum impact framing

Angle 2: Keeps Room Cooler Than AC Alone
Reason to Buy: These block heat transfer from the sun, so your room stays cooler without cranking the AC. Better sleep, lower energy bills.
Hook: "This is a curtain. This is a cooling system."
Inspired by: "This is a meal. Not a protein shake" - Product redefinition pattern

Angle 3: The Final Sleep Optimization Step
Reason to Buy: You've optimized temperature. Now optimize light. This is what serious sleep optimizers add after mastering cooling.
Hook: "Cool room in 5 minutes. Deep sleep in 8 hours."
Inspired by: "Drains double chin in 7 days" - Dual timeline showing speed + result

SUB-AVATAR #2: Night Faster ⭐ THIRD PRIORITY
Angle 1: Matches Your Sleep Discipline
Reason to Buy: You're disciplined enough to fast before bed. Now use equipment that's equally serious about blocking 100% of light.
Hook: "Serious about fasting? Serious about darkness."
Inspired by: "Moms of 15 year olds" - Direct avatar call-out with identity match

Angle 2: Protects Your Melatonin Production
Reason to Buy: Your fasting discipline is wasted if light is destroying your melatonin production every morning. Protect both.
Hook: "0% light. 100% melatonin production."
Inspired by: "14+ Hours. No Swelling" - Percentage-based outcome promise

Angle 3: Professional Tools For Serious Sleepers
Reason to Buy: People who fast before bed aren't casual about sleep. Stop using casual blackout curtains.
Hook: "This is a blackout curtain. This is a sleep protocol."
Inspired by: "This is bread. This is breakfast" - Elevation from commodity to system

TESTING PRIORITY:
Start with Sub-Avatar #3, Angle 1. Test that hook first. If it hits, run variations. If not, move to Sub-Avatar #1, Angle 1.
```

Input block to send after uploading the doc (derived from Claude's request on screen, [L079 27:20](../lessons/079-how-to-come-up-with-ad-angles.md)):
```text
Product information: <what it does, key features, benefits>
Sub-avatar profile(s): <core desire; specific pain points/problems; behaviors; emotional triggers; any other Core 5 category attributes>
```

## 8. Scripts and statics

### P17 Static template rewrite
- **Status:** near-verbatim (spoken, not a document). **Source:** [L006 08:00–09:29](../lessons/006-13-winning-static-ad-templates.md). The full Evolve static-ads prompt ("$100k Static Ads - Full EVOLVE Prompts") is not in the Start Here files; it is reproduced in Evolve Copywriting ([Copywriting P09](../../copywriting/libraries/prompts.md#which-prompt-for-which-job)). **Instructor:** Evolve.
- **Inputs:** a screenshot of the whole template (ad + "why it works" notes) and your brand information.
- **Output:** the template rewritten for our brand and avatar.
- **Caveats:** "AI is not going to be able to save you if you don't know what a good headline is." [L006 08:00–09:29](../lessons/006-13-winning-static-ad-templates.md) Compliant use: add to the prompt "keep the structure and the 'why it works' mechanism; use only our product facts and real customer language; don't reuse the reference ad's wording, numbers, characters or visuals" (derived).

```text
Here is this ad. Here is my brand. Can you rewrite this for me specifically and for my avatar specifically based on the context of my brand?
```

### P18 Script study and spoken-style rewrite
- **Status:** paraphrase (spoken; "not an official prompt"). **Source:** [L088 18:41; 21:28; 35:34](../lessons/088-the-execution-problem.md). **Instructor:** Evolve.
- **Inputs:** a winning script (to study); our draft (to simplify).
- **Output:** the techniques the winning script uses; a draft that reads as spoken at grade 5-6.
- **Caveats:** study the techniques, then test them in our own words; never lift lines.

```text
[35:34] "Claude, what are these people doing? How are they writing this script?"
[18:41; 21:28] Ask AI to rewrite a script "so it sounds more spoken" and to dumb it down to grade five or six.
```

### P19 Elite Video Ad Script Creator - Enhanced Psychology Edition (opening only)
- **Status:** partial: only the visible opening on screen. The doc is "27 pages long" and is not in the course files. **Source:** [L130 19:23](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) ("EAM // Creative Strategy Prompts" doc). The L007 index names a separate "Evolve - Video Script Prompt"; the Copywriting course reproduces "EVOLVE OPTIMIZED VIDEO AD SCRIPT - FINAL EDITION" in full ([Copywriting P19](../../copywriting/libraries/prompts.md#which-prompt-for-which-job)). Whether these are the same prompt is not shown. **Instructor:** Chef Karlo (guest).
- **Use:** paste it into a brand project and write "run this prompt"; Claude's first reply is always the core-idea question; answer with the learnings, your diagnosis and the instruction (P20). Output: six hook ideas, the whole script and a strategic breakdown. [L130 19:23–33:10](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)

```text
Elite Video Ad Script Creator - Enhanced Psychology Edition

YOUR IMMEDIATE FIRST RESPONSE
When a user shares this prompt, your VERY FIRST response must always be: "What's the core idea behind this video ad concept? Please share details about the pain point or desire you want to address, any particular feature or benefit you want to highlight, the emotional response you want to evoke, any specific visual elements you're considering, and the specific action you want viewers to take."

MANDATORY KNOWLEDGE BASE INTEGRATION
Before writing a single word, you MUST conduct a deep archaeological dig through ALL information in the project's knowledge base. ...
```

### P20 Losing-ad rewrite brief (Zend / MetaGlow postpartum) ⛔ don't execute as written
- **Status:** partial (transcribed from screen frames; the pasted learnings block and the first transcript lines are not fully visible). **Source:** [L130 21:00–29:30](../lessons/130-how-to-rewrite-losing-ads-into-winners.md). **Instructor:** Chef Karlo (guest).
- **Inputs:** the losing script, the learnings from the call, your diagnosis, the mechanism facts, a research instruction (Brave MCP → Reddit), the target format.
- **Output:** six hooks, a rewritten script, a strategic breakdown. Karlo then edits it line by line outside Claude. [L130 33:10](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)
- **Why ⛔:** it tells the model to "make women believe that they're struggling with weight loss due to prolactin" and to build the narrative that hormones are "the main source of this problem". That is persuasion toward an unproven health cause, and the scripts it produced carry claims (GLP-1 boost percentages, "Thousands of moms") that need substantiation.
- **Compliant rewrite (derived):** keep the structure, which is the useful mechanism: what happened → our diagnosis → mechanism facts → research step → write instruction → format. Replace the belief instruction with: "Explain [mechanism] only as far as [cited study / product doc] supports it; mark every health or results claim with [VERIFY]; use no customer counts, percentages or testimonials that aren't in the attached files; add the required disclaimer to every starred claim."

```text
We made an ad that had pretty decent initial performance but then died out after a week. It was a video ad targeting postpartum women, it was executed as a video ad with voiceover

This is the transcript: <script of the losing ad>

<the learnings block copied from the call summary>

So basically, we think this ad got a lot of attention due to mentioning "fat storing hormone", and we position that hormone as a "villain" and the reason why they're retaining fat, so we make them believe the problem is not THEM, but this hormone.

However, the biggest issue I see with this is we introduce the product too quickly and the viewers are not really convinced this is what's really happening.

So we need to be much more persuasive when writing about this hormone. We need to make it believable, but also super easy to understand, the script should talk in our customer's language, not be too complicated. Before mentioning the product, we should introduce the mechanism.

And in this case, we believe we should've mentioned Dyglomera earlier in the ad and use that as a "new mechanism", and Metaglow is the only marine collagen that has Dyglomera, so we should definitely leverage that information to build authority.

Dyglomera basically naturally boosts GLP-1 and that helps your body burn stored fat easier.

What I want you to do now is use Brave MCP to go to Reddit, do some research around what are these women (postpartum moms) saying about their weight-loss journey, what problems are they facing, what are they talking about, how are they feeling, etc, so you get a better understanding of the target audience we're making this ads for.

Then based on that research you did and all of the information I just gave you, I want you to write a better script that will have a similar structure to the previous one since it showed potential, but make it much more persuasive, build "narrative" in the ad, and make women believe that they're struggling with weight loss due to prolactin, position Dyglomera as the solution and a new mechanism that boosts the other hormone (GLP-1), and then mention how Metaglow is the only marine collagen that contains Dyglomera, and gradually funnel towards the product.

So the entire idea of this ad will be to build narrative around how HORMONES are the main source of this problem these women are facing, and our product is the solution.

I want you to execute this new script as an organic text on screen concept.
```

### P21 Research source-link follow-up
- **Status:** full (typed). **Source:** [L130 34:03](../lessons/130-how-to-rewrite-losing-ads-into-winners.md). **Instructor:** Chef Karlo (guest).
- **Use:** after any AI research step. Open the threads (his example: an r/beyondthebump thread) and read them yourself. Run it after P06, P10, P20 and any deep-research prompt.

```text
can you provide me with source links for the Reddit research you did, so I can take a look and do more research myself.
```

## 9. Learnings and iteration

### P22 Ad Learnings Call Analysis prompt
- **Status:** full (lesson page "Prompt" link = attached docx; bullet nesting restored by the lesson page). **Source:** [L130 page; 10:33–11:26](../lessons/130-how-to-rewrite-losing-ads-into-winners.md). Index entry "Ads Call Analysis Prompt" ("Ad Learnings Call Analysis Prompt") in [L007](../lessons/007-evolve-master-prompt-doc.md). **Instructor:** Chef Karlo (guest).
- **Inputs:** the full transcript of the weekly learnings call (a note-taker records it).
- **Output:** a client-by-client report: executive summary, performance overview, per-ad analysis, learnings, next steps.
- **Caveats:** the prompt's labels ("loser", "winner", "super winner") and "run them for 4-7 days" are the agency's; Start Here's label set is breakthrough / spend winner / KPI winner / loser ([L112](../lessons/112-winning-ad-definitions-0-mo-1m-mo.md)). Swap the labels in before you run it (derived). Its Warnings section (don't guess, note unclear status, extract facts only) is the part to keep in any summarising prompt.

```text
**Goal**

Your task is to extract and organize key insights from our weekly ad learnings call transcription and format it as a straightforward client report summarizing what we found, learned, and decided during our analysis of the ads we're running for them.

**Return Format**

You will provide a client-by-client summary with the following structure for each client:

**Client Name**

- Executive Summary (3-5 sentences summarizing what we discovered this week for this specific client, key insights we identified, and major strategic decisions we made)
- Performance Overview (high-level metrics and trends we observed for this client)
- Individual Ad Analysis (detailed breakdown of each ad we reviewed for this client)
- Key Learnings & Insights (patterns and insights we identified for this client)
- Next Steps & Recommendations (actions we're taking for this client based on our analysis)

**Context/Data**

You will analyze the complete call transcription from our weekly ad learnings meeting. As a performance marketing agency, we run and analyze social media ads (primarily on Meta platforms) for our clients. Here's our workflow context:

- We first have strategy calls with clients where we develop creative concepts
- We create ads based on these concepts and run them for 4-7 days
- Each ad is then reviewed in our weekly "ad learnings call" to determine if it's a "loser," "winner," or "super winner"
- We track all ads in ClickUp, and only review ads in the "learnings" phase during this call
- We organize our discussion client by client, reviewing each ad's performance
- We use CBO (Campaign Budget Optimization) in Meta ad accounts, so an important initial indicator is whether an ad received significant spend
- Key metrics we typically discuss include: profitability (ROAS), hook rate (3-second views), hold rate (watch time), CTR (Click-Through Rate), and other relevant engagement metrics

**Instructions**

Please analyze the following ad learnings call transcription and:

- Identify all clients discussed in the meeting
- For each client, provide a separate section written in first-person plural ("we") as if reporting to that specific client:
  - Client name as header
  - Executive summary paragraph (3-5 sentences) written as: "This week, we reviewed [X] ads and found that..." Focus on what we learned and decided for this specific client
  - Performance overview written as: "Here's what we saw in the account..."
    - Total number of ads we reviewed for this client
    - Distribution of winners/losers/super winners we identified for this client

For each ad we discussed under each client:

- Ad name/identifier (if mentioned)
- Performance metrics we analyzed (spend, profitability, key metrics)
- Our classification as winner/loser/super winner
- Key insights we discovered about success/failure reasons
- Specific creative elements we highlighted (hooks, visuals, etc.)

- Extract patterns and insights for each client in simple, direct language:
  - Write as "We noticed that..." or "We found that..."
  - Creative elements we found consistently perform well/poorly for this client
  - Trends we identified in this client's data
  - Testing ideas and optimizations we're recommending for this client

Document our action items and next steps for each client:

- Write as "We're going to..." or "We'll..."
- Specific tasks we're assigning to team members for this client
- New creative concepts we're developing for this client
- Optimization strategies we're planning for this client
- Highlight exceptional performances or critical issues for each client that need attention

**Tone & Style Guidelines**

- Write from the agency's perspective using "we," "our team"
- Use simple, straightforward language - avoid overly formal or complex phrases
- Focus on insights and learnings rather than just raw data
- Present findings as discoveries and decisions we made
- Avoid jargon - explain technical terms simply when necessary
- Remember: WE create and run the ads, not the client
- Keep the tone conversational
- Maintain the client-by-client structure throughout the entire report

**Warnings**

If an ad's status is unclear from the transcript, note this rather than guessing

If specific metrics are mentioned but not clearly attributed to a particular ad, note this in that client's summary

Focus on extracting factual information rather than making recommendations not present in the transcript

Our discussions may contain jargon and casual conversation - translate this into simple client-facing language

Team members may disagree about an ad's classification - present the final decision we reached

Keep each client's section completely separate and focused only on their ads and performance

Always remember that WE are the ones creating, running, and analyzing the ads - not the client
```
Karlo's spoken variant of the context line: "we're a marketing agency… we mostly run CBO… the main purpose of this call is to look at ads that we ran and try to figure out why are they good, why are they not good". [L130 10:33–11:26](../lessons/130-how-to-rewrite-losing-ads-into-winners.md)

### P23 Apply winning-ad learnings to our brand
- **Status:** paraphrase (spoken). **Source:** [L125 19:23](../lessons/125-how-to-do-learnings-part-4-winning-ads.md). **Instructor:** Evolve.
- **Inputs:** your written list of why the winning ad works (hook, bridge, close; studied as a customer first), plus our product info.
- **Output:** brand-specific ways to apply those mechanisms.
- **Caveats:** give it mechanisms, not the ad's lines; ask for new wording. "Never reuse lines." [L125 page checklist](../lessons/125-how-to-do-learnings-part-4-winning-ads.md)

```text
Here's every reason why this is working. Can you apply this to my brand? How could we apply this to my brand specifically?
```

### P24 Winning image to new ad (⛔ don't execute as written)
- **Status:** paraphrase (spoken; the full ChatGPT prompt from the instructor's AI program is not shown). **Source:** [L123 04:55](../lessons/123-how-to-do-learnings-part-2-winning-ads.md). **Instructor:** Evolve.
- **Inputs:** a saved winning image ad + your own product image.
- **Why ⛔:** asking for an ad "similar to that" from someone else's winning creative invites a near-copy of the asset (layout, wording, visual).
- **Compliant rewrite (derived):** "Here is a winning ad. First list its mechanisms (hook type, angle, proof type, layout logic, emotion). Then create a new static for [our product] that uses those mechanisms with our own headline, our own photo and only claims from the attached product doc. Do not reuse any words, characters, numbers or visual composition from the reference."

```text
take the learnings from this and... process and identify this and create an ad for this product and this brand in particular that is similar to that
```

### P25 `analyze-breakthrough` Claude Code commands
- **Status:** full (page/doc text). **Source:** [L110 doc ("📊 Generating Reports")](../lessons/110-winning-ads-definition-part-1.md), [L113 05:01–06:02](../lessons/113-how-to-generate-submit-winning-ad-report.md), [L114 page](../lessons/114-action-item-generate-submit-your-reports.md). **Instructor:** Evolve.
- **Inputs:** an Ads Manager CSV with campaign name, ad name, day breakdown, amount spent, purchases, cost per purchase, purchase conversion value, ROAS ([L113](../lessons/113-how-to-generate-submit-winning-ad-report.md)); the ad name; the brand.
- **Output:** a breakthrough report in `breakthrough-reports/`.
- **Caveats:** the repo is third-party (`github.com/zjamesblake/analyze-breakthrough`). Review it before letting Claude Code install its requirements. Submitting the report shares account data with Evolve via a ClickUp form and a Leadsie link; get the account owner's approval first (derived).

```text
Go into analyze-breakthrough and install the requirements
```
```text
/analyze-breakthrough @File.csv "AD NAME" --brand "Brand"
```

## 10. Product research (brand-building lessons)

### P26 Trademark check
- **Status:** full as typed on screen. **Source:** [L172 33:10](../lessons/172-live-product-research-w-kalodata-pt-2.md). **Instructor:** Shaun Eng.
- **Output:** a lead on active trademarks. Confirm on the official registry (US: USPTO, free). [L172 04:41–07:50](../lessons/172-live-product-research-w-kalodata-pt-2.md)
- **Note:** L172 also teaches reusing other sellers' TikTok Shop videos. That tactic is **don't execute** (see [rules](rules.md)); the trademark check itself is fine to run.

```text
Does [brand site URL] have any trademarks active
```

### P27 Does this product work?
- **Status:** paraphrase (spoken). **Source:** [L171 26:37–27:08](../lessons/171-how-to-make-any-product-work-brand-building-pt-1.md). **Instructor:** Evolve (speaker not verified on the lesson page).
- **Use:** a conviction screen before picking a product. His examples: the AI called chin slimmers "largely ineffective" ("probably wouldn't sell it then"); body shapers "do actually work".
- **Caveats:** an LLM verdict is a first filter. Check reviews, return reasons and evidence before deciding, and never quote the AI's verdict as proof in an ad.

```text
Ask ChatGPT/Claude whether [product type] actually works.
```

### P28 Expected-price check
- **Status:** paraphrase (page text). **Source:** [L172 42:00–43:08; page text](../lessons/172-live-product-research-w-kalodata-pt-2.md). **Instructor:** Shaun Eng.
- **Use:** check that 3x (COGS + shipping) still falls inside the price range buyers expect. Example: $20 total cost, $60 price, $40-60 expected range.

```text
Use Claude, GPT or Amazon to check the average price for [product], so the selling price (about 3x COGS + shipping) stays within the expected range.
```

---

## Named but unavailable
| Prompt / tool | Named in | What we know | Where to go instead |
|---|---|---|---|
| Static Ads Prompt ("$100k Static Ads - Full EVOLVE Prompts") | [L007 index](../lessons/007-evolve-master-prompt-doc.md) | Separate Google Doc, not exported in Start Here | Full text in Evolve Copywriting: [Copywriting P09](../../copywriting/libraries/prompts.md#which-prompt-for-which-job) |
| Video Ads Prompt ("Evolve - Video Script Prompt") | [L007 index](../lessons/007-evolve-master-prompt-doc.md) | Separate Google Doc ("Older Video") | Full text in Evolve Copywriting: [Copywriting P19](../../copywriting/libraries/prompts.md#which-prompt-for-which-job) |
| Elite Video Ad Script Creator, pages after the opening | [L130 19:23](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) | "27 pages long"; opening in [P19](#p19-elite-video-ad-script-creator---enhanced-psychology-edition-opening-only) | Copywriting P19 |
| "EAM // Creative Strategy Prompts" tabs: Market Research, Custom Project, Comment Miner, Target Avatar (+ example), Desires, Ideas From Reviews, Hook/Headline Ideas, Static Ads, Video Ads, NEW Video Ads | [L007 doc screenshot](../lessons/007-evolve-master-prompt-doc.md), [L130](../lessons/130-how-to-rewrite-losing-ads-into-winners.md) | Tab names only | P01 (custom project), P06 (desires), P08 (comment mining) |
| Alex Cooper's Prompts | [L007 index](../lessons/007-evolve-master-prompt-doc.md) | Call recording + Notion; "EVOLVE ACCESS ONLY" | — |
| Evolve AI - Prompts (Karlo's program) | [L007 index](../lessons/007-evolve-master-prompt-doc.md) | "The remaining AI Prompts & other AI tools we use are found in the Evolve AI program" | — |
| ecomtalent AI custom Gemini projects | [L090 page text](../lessons/090-how-to-get-a-players-editors-content.md) | Image/video generation and "custom Gemini Projects for building prompts" | — |
| "Ask the Ad AI" project / ad-killing Claude Skill | [L110 doc; 19:15–20:09](../lessons/110-winning-ads-definition-part-1.md) | "Coming as a Claude Skill"; promised, not shipped in the files | [P25](#p25-analyze-breakthrough-claude-code-commands) |
| Viral-script "rewriter" prompt | [L136 02:06](../lessons/136-how-to-get-viral-ugc-inspo-for-creators-ads.md) | Instructor sends a viral transcript to "my rewriter for my specific brand inside of Claude" | Use [P23](#p23-apply-winning-ad-learnings-to-our-brand) on extracted mechanisms; don't rewrite a viral transcript line for line |
| Hook-replication prompt for the 100 hook templates | [L005 page text](../lessons/005-100-hook-templates-from-ads-doc.md) | "if you want to have Claude replicate some of these hooks": feed template + brand, avatar, facts; no text supplied | [Hooks library](hooks.md), P16 |
| Insense campaign copy via ChatGPT | [L143 00:00](../lessons/143-how-to-create-an-insense-campaign.md) | "Usually I use ChatGPT to help me put the copy together for this"; no prompt shown | Insense hint-box checklists in [templates](templates.md) |
| Full winning-image ChatGPT prompt | [L123 04:55](../lessons/123-how-to-do-learnings-part-2-winning-ads.md) | Spoken paraphrase only ([P24](#p24-winning-image-to-new-ad--dont-execute-as-written)) | P24 compliant rewrite |
| P07 detail sections ("Enhanced Existing Sections", "New Universal Framework") | [L063](../lessons/063-how-to-find-desires-part-3.md) | Headings only | — |

## Coverage and gaps
- **Scope:** all 175 lesson pages were checked: their "Prompts / templates (verbatim)" sections (103 lessons have one) and a full-text search for Claude / ChatGPT / GPT / Gemini / prompt. Non-AI material in those sections (research-doc and product-doc forms, desire-hunting sheet, creator messages, frameworks, naming legends, checklists) is in [templates](templates.md), not here.
- **Counts:** 28 prompt entries. 14 have full verbatim text: P01, P03 (typed turns), P04, P05, P06, P07, P09, P10, P11, P12, P13, P16, P22, P25. 2 are partial written text: P19 (opening only) and P20 (screen-transcribed brief, middle not visible). 12 are near-verbatim or paraphrase: P02, P08, P14, P15, P17, P18, P21 (full, one line), P23, P24, P26 (typed, one line), P27, P28. 13 named prompts or tools are unavailable.
- **Duplicates merged:** P01 appears in L007 and L059 (identical apart from the `**` placeholder formatting); P06 and P07 in L063 and L064 (verified identical); P09 in L066 and L067; P10 and P11 in L068 and L069; P25 in L110, L113 and L114.
- **⛔ marked:** P20 (belief-forcing health narrative), P24 (recreate a winning competitor image). P17 and P16 carry copy-the-mechanism instructions.
- **Conflicts logged** to the contradictions notes: P16's 3 hooks per angle vs its 1-hook example output; L063's AI deep-research prompt vs L065's "not with Claude, not with GPT" research standard.
- **Evidence limits:** outcome claims about prompts ("found the #1 mechanism... took us two years", L066) are instructor claims. No prompt output in the course was shown with its test result.

## In other courses
- RMBC II: [RMBC II prompt library: every prompt and Claude Project instruction, by pipeline stage](../../../stefan-georgi/rmbc-ii/libraries/prompts.md): RMBC prompts
- RMBC II: [The Claude Project recipe](../../../stefan-georgi/rmbc-ii/concepts/claude-project-recipe.md): Claude Project recipe

Which page owns the topic: [topic map](../../../../topic-map.md).
