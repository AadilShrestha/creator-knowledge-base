---
title: "Action Item - Generate + Submit Your Reports"
type: lesson
creator: evolve
course: start-here
section: 08-winners-and-scaling
order: 114
instructor: "unverified (action-item page; no video)"
sources:
  - knowledge-base/raw/evolve/start-here/_extracted/👣 Evolve (Start Here)/114. 💥 Action Item - Generate + Submit Your Reports_👣 Evolve (Start Here)_Evolve.html.md
tags: [action-item, breakthrough-report, claude-code, winning-ads, submit-data, clickup-form]
updated: 2026-11-02
---

# 114. Action Item - Generate + Submit Your Reports
> The assignment that follows lesson 113: generate a breakthrough report for your own best ad with the `analyze-breakthrough` Claude Code skill and submit it so your data improves the Evolve winning-ad definitions.

## 🤖 Agent use
- **Use when:** a human or agent must run the report-contribution workflow end to end, or needs a checklist to confirm nothing was skipped.
- **Inputs → outputs:** the account's Meta Ads Reporting CSV and the top-spending ad's name code → a breakthrough report in `breakthrough-reports/`, a shared Google Sheet and a ClickUp submission.
- **Rules:**
  - **DO** follow the six numbered repo steps in order; they are identical to the page text of [113](113-how-to-generate-submit-winning-ad-report.md).
  - **DO** open the Google Sheet to "anyone with the link" before submitting (page Step 4: "open for all to view").
  - **DO** use the video in [113](113-how-to-generate-submit-winning-ad-report.md) for the details this page omits: required report columns, USD and 7-day-click settings, date range, how to choose the ad, and what the ClickUp form asks for.
  - **DON'T** assume this page contains settings or screenshots: it has only the steps and links below. Everything else comes from the 113 video.
- **See also:** [113. How To Generate + Submit Winning Ad Report](113-how-to-generate-submit-winning-ad-report.md) · [112. Winning Ad Definitions ($0/mo-$1M/mo)](112-winning-ad-definitions-0-mo-1m-mo.md) · [109. How To Set Up Naming Templates](109-how-to-set-up-naming-templates.md)

## Key ideas
- Purpose stated on the page: "How to generate and submit your reports to contribute to the winning ad data definitions."
- The page repeats the lesson-113 instructions as a text checklist (the 113 page text has the same steps, with the heading missing).

## Steps / framework
1. **Download VS Code:** https://code.visualstudio.com/
2. **Create a "Claude Code" folder.**
3. **Download the repo and follow its steps:** https://github.com/zjamesblake/analyze-breakthrough
   1. Download ZIP from the repo.
   2. Unzip and place `analyze-breakthrough/` in your Claude Code workspace.
   3. Open Claude Code and say: "Go into analyze-breakthrough and install the requirements".
   4. Drop a CSV into `account-csvs/`.
   5. Run: `/analyze-breakthrough @File.csv "AD NAME" --brand "Brand"`
   6. The report lands in `breakthrough-reports/`.
4. **Upload the CSV into a Google Sheet and open it for all to view.**
5. **Submit via the ClickUp form:** https://forms.clickup.com/10505015/f/a0jtq-196694/56KSP3MSJJ3W6KDVEI

## Prompts / templates (verbatim)
```
Go into analyze-breakthrough and install the requirements
```
```
/analyze-breakthrough @File.csv "AD NAME" --brand "Brand"
```

## How to apply
- [ ] Watch [113](113-how-to-generate-submit-winning-ad-report.md) first; build the Meta Ads Reporting CSV with the required columns.
- [ ] Complete page steps 1-3 and generate one report per true breakthrough ad.
- [ ] Put each report in one Google Sheet (one tab per ad), set sharing to "anyone with the link" viewer.
- [ ] Submit the ClickUp form and grant view access as shown in 113.
- [ ] Record in your own notes which ads you submitted and their tier, so you can compare with [112](112-winning-ad-definitions-0-mo-1m-mo.md) after the dataset updates.

## Related
- Previous: [113. How To Generate + Submit Winning Ad Report](113-how-to-generate-submit-winning-ad-report.md) · Next: [115. How to Scale Facebook Ads (Up & Down)](115-how-to-scale-facebook-ads-up-down.md)
- [111. Winning Ads Definition - Part 2](111-winning-ads-definition-part-2.md)

## Sources and limitations
- Page text: [114 page](<../../../../../raw/evolve/start-here/_extracted/👣 Evolve (Start Here)/114. 💥 Action Item - Generate + Submit Your Reports_👣 Evolve (Start Here)_Evolve.html.md>). No video, transcript or attachment exists for this lesson.
- The repo contents and the ClickUp form behaviour beyond the video in 113 are not included in the course files. The steps name no deadline, minimum number of ads or reward.
