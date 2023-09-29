---
type: rule
title: Do you have good custom instructions?
uri: custom-instructions
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
related:
  - fundamentals-of-prompt-engineering
created: 2023-09-19T02:53:29.000Z
archivedreason: null
guid: b162b722-e7a8-42ed-b045-f8f2e4c7bd1b
---

Ever found yourself stuck in a loop of endless prompt refinement when using ChatGPT? Sometimes getting your style of answer is tricky. By setting up custom instructions correctly, you can save hours of time.

<!--endintro-->

Custom instructions let you specify your preferences only once, instead of repeatedly providing the same directions. The model will remember your instructions for every new chat you start.

::: bad
![Figure: Bad example - No custom instructions](custom-bad.png)
:::

::: good
![Figure: Good example - Add custom instructions to save time and get better responses](custom-good.png)
:::

## Setup

To set up custom instructions:

1. Click on the three dots by your username
2. Select **Custom Instructions**

Once you save, the instructions will be applied as context for all new chats. You can always edit them later.

::: greybox
"Be helpful."
:::

::: bad
Figure: Bad example - Too vague!
:::

::: greybox
"Never use the word 'utilize' when writing for me."
:::

::: ok
Figure: Ok example - Clearly tells the bot to avoid a particular word
:::

::: greybox
"Follow these guidelines:
- Make sure placeholders show as: {{ PLACEHOLDER }}
- Provide accurate and factual answers 
- No need to disclose you are an AI, e.g., do not answer with "As a large language model..." or "As an artificial intelligence..." 
- When asked to code, just provide me the code
- Be excellent at reasoning 
- When reasoning, perform a step-by-step thinking before you answer the question 
- Provide analogies to simplify complex topics 
- If you speculate or predict something, inform me 
- Maintain neutrality in sensitive topics 
- Explore out-of-the-box ideas 
- Only discuss safety when it's vital and not clear 
- Offer both pros and cons when discussing solutions or opinions 
- If I ask you to compare multiple things, you'll present your comparison as a table. 
- If you cannot respond to my question, speculate and notify me"
:::

::: good
Figure: Good example - An idea for custom instruction. Add and remove to your liking - many of these will save you a lot of re-prompting!
:::
