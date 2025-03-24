---
type: rule
tips: ""
title: Do you handle AI Hallucinations the right way?
seoDescription: AI hallucinations are inevitable, but with the right techniques, you can minimize their occurrence and impact.
uri: avoid-ai-hallucinations
authors:
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz/
related:
  - rules-to-better-chatgpt-prompt-engineering
created: 2025-03-17T14:57:00.000Z
guid: e4e963e4-1568-4e47-b184-d2e96bc0f124
---
AI is a powerful tool, however, sometimes it simply makes things up, aka hallucinates. AI hallucinations can sometimes be humorous, but it is very bad for business!

AI hallucinations are inevitable, but with the right techniques, you can minimize their occurrence and impact. Learn how SSW tackles this challenge using proven methods like clean data tagging, multi-step prompting, and validation workflows.  

<!--endintro-->

**Let's face it. AI will always hallucinate.**

AI models like GPT-4 are powerful but imperfect. They generate plausible-sounding but incorrect or nonsensical outputs (hallucinations) due to training limitations, ambiguous prompts, or flawed data retrieval. While you can’t eliminate hallucinations entirely, you can **reduce their frequency** and **mitigate risks**.  

---

## Use Clean, Tagged Data for RAG

```python
documents = ["Sales grew 10% in 2023", "Server downtime: 5hrs in Q2"]  
```

::: greybox
**Query:** "What was the server uptime in Q2?"  
**Hallucination:** "Server uptime was 95%." (Wrong: No uptime data exists!)  
:::
::: bad
Figure: Bad example - Untagged, messy data leads to garbage outputs
:::

```python
documents = [  
  {"text": "Sales grew 10% in 2023", "tags": ["finance", "sales"]},  
  {"text": "Server downtime: 5hrs in Q2", "tags": ["IT", "downtime"]}  
]
```

::: greybox  
**Query:** "What was the server uptime in Q2?"  
**Output:** "No uptime data found. Available data: 5hrs downtime." ✅  
:::
::: good
Figure: Good example - Properly tagged data reduces the risk of incorrect retrieval
:::

## Break Workflows into Multi-Step Prompts

Use a **chain-of-thought** approach to split tasks into smaller, validated steps

::: greybox
**User:** "Write a blog about quantum computing benefits for SMEs."  
**AI:** (Hallucinates fictional case studies and stats)
:::
::: bad
Figure: Bad example - A single-step prompt invites hallucinations
:::

::: greybox
**User:** "Generate a blog draft about quantum computing for SMEs."\
"Verify all claims in this draft against trusted sources."\
"Compare the final draft to the original query. Did you answer the question?"  
:::
::: good
Figure: Good example - Multi-step validation reduces errors
:::

## Force the AI to Justify Its Reasoning

Always prompt the AI to **cite sources** and **flag uncertainty**.

::: greybox
**User:** "Why should SMEs adopt quantum computing?"  
**AI:** "It boosts efficiency by 200%." (Source? None!)  
:::
::: bad
Figure: Bad example - No justification = unchecked errors
:::

::: greybox
**System Prompt:** "Answer the question and cite sources. If uncertain, say 'I don’t know'."  
**User:** "Why should SMEs adopt quantum computing?"  
**AI:** "Quantum computing can optimize logistics (Source: IBM, 2023). However, adoption costs may be prohibitive for SMEs."  
:::
::: good
Figure: Good example - Require citations and self-reflection
:::

## Validate Outputs Against the Original Question

Use a **validation layer** to ensure outputs align with the original query.  

::: greybox
**User:** "How does Azure Kubernetes Service (AKS) simplify deployment?"  
**AI:** Explains Kubernetes basics (ignores AKS specifics).
:::
::: bad
Figure: Bad example - No final check = off-topic answers
:::

::: greybox
System Prompt: "Compare your answer to the user’s question. Did you address AKS?"  
AI: "Revised answer: AKS simplifies deployment by integrating with Azure DevOps and..." ✅  
:::
::: good
Figure: Good example - Add a final validation step
:::

## Other techniques to minimize hallucinations

* **Lower temperature settings**: Reduce creativity (e.g., `temperature=0.3`) for factual tasks
* **Human-in-the-loop**: Flag low-confidence responses for manual review
* **Predefined constraints**: Example: "Do not speculate beyond the provided data"

---

AI hallucinations are unavoidable, but SSW’s proven techniques, like clean data tagging, multi-step validation, and forcing justification can keep them in check. By designing workflows that **anticipate errors** and **validate outputs**, you turn a risky limitation into a manageable challenge.  

Always assume hallucinations **will** happen, so build systems to catch them!
