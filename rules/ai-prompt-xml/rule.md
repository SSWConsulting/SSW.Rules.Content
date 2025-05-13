---
type: rule
archivedreason:
title: Do you use XML tags to structure your AI prompts?
seoDescription: The industry standard method used for digesting and analysing form results, Microsoft Forms, Google Forms, SurveyMonkey
guid: 4d8e03c3-e842-4b1d-a049-8eff21b1209f
uri: ai-prompt-xml
created: 2025-05-13T16:42:19.624Z
authors:
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz
related:
---

The bigger your prompts get, the more challenging they become for the AI to understand. 
Using XML tags will help an LLM parse your prompts more accurately, leading to higher-quality outputs.

The best part is that it doesn't need to follow any specific syntax. It just helps both humans and AI to have structured prompts.
            
<!--endintro-->

## Why use XML tags?
- **Clarity:** Ensure your prompt is well structured by having clear separation of different parts.
- **Accuracy:** Reduce the 'needle-in-a-haystack' problem by being more explicit.
- **Flexibility:** Easily re-arrange, add, remove, and locate different parts of your prompt by having everything atomic.


You can even ask the LLM to give outputs in XML, which makes things easier to read for humans too!

::: bad
```
You're a sales manager at Northwind. Analyze our Q2 sales performance across all regions. Include sections on Top Products, Regional Performance, and Customer Satisfaction, referencing last quarter's report: {{Q1_SALES_REPORT}}. Use the latest sales metrics from: {{SALES_DASHBOARD}}. The analysis should be data-driven, actionable, and highlight key wins and opportunities. Focus on identifying emerging market trends and providing strategic recommendations for Q3.
```
:::
**Bad example: If it's hard for humans to read 'at-a-glance', the AI will struggle too.**

::: good
```xml
<context>
    You are a sales manager at Northwind
    Northwind is a B2B offshore wind infrastructure management SaaS company.
    Our investors value transparency and actionable insights
</context>

Use this data for the report
<data>
    {{REPORT_DATA_CSV}}
</data>

<instructions>
1. Include sections: Revenue Growth, Profit Margins, Cash Flow.
2. Highlight stregnths and areas for improvement.
</instructions>

<tone>
Make sure your tone is concise and professional.
</tone>
```
:::
**Good Example: XML in your prompts makes it easier for humans and LLMs to both read, leading to higher quality and more desirable outputs.**






