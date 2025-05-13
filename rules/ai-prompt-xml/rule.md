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
You're a software architect at Northwind. Review our codebase architecture and suggest improvements to our microservices. Include sections on API Design, Service Communication, and Database Optimization, referencing our current architecture document: {{ARCHITECTURE_DOC}}. Use the latest performance metrics from: {{PERFORMANCE_DASHBOARD}}. The review should be technical, actionable, and highlight key issues and opportunities. Focus on identifying scalability bottlenecks and providing strategic recommendations for the next sprint.
```
:::
**Bad example: If it's hard for humans to read 'at-a-glance', the AI will struggle too.**

::: good
```xml
<context>
    You are a software architect at Northwind
    Northwind is a B2B supply chain management SaaS company
    Our development team values clean architecture and maintainable code
</context>

Use this data for the review
<data>
    {{CODEBASE_ANALYSIS_JSON}}
</data>

<instructions>
1. Include sections: API Design, Service Communication, Database Optimization
2. Highlight strengths and areas for improvement
</instructions>

<tone>
Make sure your tone is technical and solution-oriented
</tone>

Follow this structure:
<formatting-example>
    {{PREVIOUS_ARCH_REVIEW_MD}}
</formatting-example>
```
:::
**Good Example: XML in your prompts makes it easier for humans and LLMs to both read, leading to higher quality and more desirable outputs.**






