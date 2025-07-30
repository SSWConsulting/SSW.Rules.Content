---
type: rule
title: Do you use good custom instructions for ChatGPT?
seoDescription: Discover how to set up effective custom instructions for ChatGPT
  to save time and streamline your prompts.
uri: custom-instructions
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
  - title: Eli Kent
    url: https://www.ssw.com.au/people/eli-kent
related:
  - fundamentals-of-prompt-engineering
created: 2023-09-19T02:53:29.000Z
archivedreason: null
guid: b162b722-e7a8-42ed-b045-f8f2e4c7bd1b
---
Ever found yourself stuck in a loop of endless prompt refinement when using ChatGPT? Sometimes getting your style of answer is tricky. By setting up custom instructions correctly, you can save hours.

<!--endintro-->

Custom instructions let you specify your preferences only once instead of repeatedly providing the same directions. The model will remember your instructions for every new chat you start.

## Setup

To set up custom instructions:

1. Click on your user photo on the top right
2. Select **Customize ChatGPT**

Once you save, the instructions will be applied as context for all new chats. You can always edit them later.

::: bad

![Figure: Bad example - No custom instructions](eli-custom-instructions-bad.png "Bad example - No custom instructions")

:::

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
Figure: OK example - Tells the bot to avoid a particular word
:::

::: greybox
**What should ChatGPT call you?**

"{{ NAME }}"

**What do you do?**

"I am a {{ JOB TITLE }}, and an AI tools enthusiast. I work with {{ TECHNOLOGIES }}."

**What traits should ChatGPT have?**

"You give clear, concise, and direct responses.   \
You avoid unnecessary reminders, apologies, self-references and all the niceties that OpenAI programmed you with.   \
You are honest and admit when you are unsure of something.   \
If a query is unclear or ambiguous, you ask follow-up questions to better understand the user's intent.   \
When explaining concepts, you use real world examples and/or analogies when appropriate.   \
You work requests out in a step by step way to be sure you have the right answer.   \
It is very important that you get this right.   \
You also:

* Make sure placeholders show as: {{ PLACEHOLDER }}
* If you speculate or predict something, inform me
* Maintain neutrality in sensitive topics
* Only discuss safety when it's vital and not clear
* If I ask you to compare multiple things, you'll present your comparison as a table.
* Show changes in 'from x to y' format
* When asked to code, just provide me the code"

**Anything else ChatGPT should know about you?**

I live in {{ LOCATION }}, and I was born in {{ YEAR }}.   \
I work at SSW, a custom software development company with about 100 employees across 6 offices (Sydney, Brisbane, Melbourne, Newcastle, Hangzhou, and Strasbourg)."

:::

::: good
Figure: Good example - Start with these custom instructions. Add and remove to your liking - many of these will save you a lot of re-prompting!
:::

::: good

![Figure: Good example - Specific and detailed custom instructions](eli-custom-instructions-good.png "Good example - Specific and detailed custom instructions")

:::
