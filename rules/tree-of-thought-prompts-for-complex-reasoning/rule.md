---
type: rule
title: Do you use "Tree of Thought" prompts for complex reasoning?
uri: tree-of-thought-prompts-for-complex-reasoning
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
  - do-you-know-tree-of-thought-prompts
  - do-you-know-prompts-for-complex-reasoning
created: 2023-11-26T23:10:50.651Z
archivedreason: null
guid: 0e84b5e3-cbe7-42cf-98b1-57fd0074b994
---
Imagine you're using ChatGPT and you find that the model's answers lack depth or reasoning. You're not alone. Many users experience this, especially when asking complex questions. Tree of Thought (ToT) prompting can be a game-changer in such scenarios.

**Note:** If you're on GPT Plus, you can use this custom GPT: [Tree of Thought Problem Solver](https://chat.openai.com/g/g-CIFNL94KS-tree-of-thoughts-problem-solver).

<!--endintro-->

### What is Tree of Thought Prompting?

Tree of Thought Prompting is a technique that enhances the reasoning abilities of Large Language Models like ChatGPT. It allows the model to explore multiple branches of reasoning and self-correct as it goes along.

Think of ToT prompting as a brainstorming session among experts. Each expert represents a branch of reasoning. They share their thoughts, evaluate each other's reasoning, and reach a consensus.

### Why is it Useful?

* **Enhanced Reasoning** - ToT prompting improves the model's ability to answer complex questions
* **Self-Correction** - The model can identify and rectify its errors autonomously
* **Single Prompt** - ToT can run from start to finish without any user interaction.

Use ToT prompting when you need more reasoned and nuanced answers from ChatGPT, especially for complex queries.

### How to Implement a Simple ToT Prompt

The basic structure of a ToT prompt involves asking the model to imagine multiple experts debating the question. Each expert shares one step of their reasoning before moving on to the next.

::: greybox
“Imagine 3-6 different experts are answering this question. {{ YOUR QUESTION }}

All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they're wrong at any point, then they leave.

Continue this process until we have a definitive answer.”
:::

::: good 
Figure: Good example - This structure allows the model to explore multiple reasoning paths and self-correct
:::

### Examples

::: greybox
"Should I vote 'yes' or 'no' on The Voice?"
:::

::: bad 
Figure: Bad example - This is a nuanced question and this simple prompt is unlikely to fully explore the options
:::

::: greybox
"Read https://voice.gov.au 

Imagine 3 different experts are answering this question: "Should we vote 'yes' or 'no' on The Voice?"

All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they're wrong at any point, then they leave.

Continue this process, until you have a definitive 'yes' or 'no' answer"
:::

::: good 
Figure: Good example - This is a complex question that benefits from ToT prompting
:::
