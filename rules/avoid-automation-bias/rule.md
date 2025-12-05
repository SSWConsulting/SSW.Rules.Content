---
type: rule
tips: ""
title: Do you avoid Automation Bias? (aka AI Slop)
seoDescription: Did you know that AI has the potential to make your work worse? Learn the common pitfalls so that AI can help, not hinder.
  Learn the common pitfalls so that AI can help, not hinder.
uri: avoid-automation-bias
authors:
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz
related:
  - manage-security-risks-when-adopting-ai-solutions
  - manage-legal-implications-of-ai
  - mitigate-brand-risks-ai
  - use-ai-responsibly
  - checked-by-xxx
created: 2025-09-16T14:29:00.000Z
guid: 67B27A09-5546-4AD9-9DCC-732CE63D7183
---
AI has been championed as a huge productivity booster, which it is. However, people blindly trusting AI outputs, or preferring them over theirs, can lead to 'automation bias'.

Let's talk about what leads to creating AI slop:

<!--endintro-->

`youtube: https://www.youtube.com/embed/kDS5pwelhNM?si=_nqw5XQWgpib5b8z`
**Video: How AI is making you dumber (3 min)**

Automation bias is a type of cognitive bias.

Too many people use AI and pass on its answers, without taking 100% ownership of the content. If there's something you can't explain, then you're publishing **AI slop**.

## Errors from automation bias

There are two types of errors made due to automation bias:

* **Error of commission** - Doing the wrong thing because the system suggested it
  E.g. Accepting a flawed suggestion, getting ChatGPT to write your essay, etc.
* **Error of omission** - Failing to act because the system didn't flag a problem
  E.g. shipping flawed code, because Copilot review approved it

## Where AI slop (aka automation bias) shows up

* **Coding assistants (e.g. Copilot)** - They make you faster, not better. The more complex some generated code is, the more likely you'll be to click "Accept"
* **Google Search (especially 'AI Overview')** - These search engines are incentivised to return the most relevant content, rather than the most correct content

## What doesn't fix it (but seems like it should)

* **Human-in-the-loop** - This only covers legal accountability. Just because a human is in the loop, doesn't mean they're immune to automation bias
* **Higher model accuracy** - Using a highly accurate model breeds complacency
* **Training people that "software is often wrong"** - Makes people think they know more about the software than they do → false confidence

## Why do we fall for it?

### 1. Stress - Task complexity & time pressure

Under stress, cognition narrows and we rely more heavily on mental shortcuts. AI tools initially promise to "do less work," but this productivity gain often shifts expectations, leading to "do more work in the same time".

This creates a vicious cycle: Increased time pressure → more likely to accept AI outputs without scrutiny.

### 2. Lack of accountability

If there are two people within a company who don't know each other well, and review each other's code, they are less likely to care about what each other thinks, and they'll put less effort into a review.

### 3. Personality traits

More extroverted people want to move quickly → they accept AI outputs more readily.

People high in neuroticism may doubt their own outputs → they doubt AI's outputs too.

This isn't prescriptive, just a pattern to be aware of.

### 4. Cognitive Biases

Artificial Intelligence has been engineered to appear more human in recent years. End-users are more likely to place trust in systems they can engage with in human like interactions. As a side effect, we often afford more credence to AI models than warranted. This leads to AI generated outputs being less harshly scrutinized.

## How to avoid

### 1. Don't submit AI content that you don't fully understand

If AI helps you create work, that's great. But what if someone asks you a technical question about the work, that you can't answer?

It then becomes very obvious that this work is not your own - worse, it might even mean the solution is suboptimal.

Remember to always **own your work**.

### 2. Show error rates clearly (for devs)

When creating tools that are prone to mistakes, include exact error rates:

::: greybox
AI sometimes makes mistakes, ensure you check its output.
:::
::: bad
Bad example - Highly vague warning, most people will ignore it
:::

::: greybox
Studies have found that 25% of AI-generated code has security vulnerabilities. Ensure you review it.
:::
::: good
Good example - More specific warning, people are more likely to take it seriously
:::

::: good
![Figure: Our AI products always show precise error rates](dr-docenstein-message.png)
:::

### 3. Four Eyes Principle (with real relationships)

The Four Eyes Principle (aka Two-Person Rule) is a common internal control practice requiring that any activity involving a material risk be reviewed or double-checked by a second person.

This is similar to the ['Checked By' rule](/checked-by-xxx).

::: greybox
Random Person: *"Hey, can you review this code I wrote with Copilot?"*

Bob: *"I don't know you well, and I have better things to do... approved ✅"*
:::
::: bad
Bad example - Random pair reviews, people don't know each other well, so they won't feel accountable
:::

::: greybox
Alice: *"Hey Bob, can you review this code I wrote with Copilot?"*

Bob: *"Sure, I want to make sure I don't let Alice down, so I'll take a closer look 👀"*
:::
::: good
Good example - Pair reviews with people who know each other well, so they feel accountable
:::

### 4. Prompting - Provide information, not instructions

Ask AI to present information and sources before it asserts conclusions. Avoid instructive "Do this" prompts.

Assume you want top marks for your university assignment.

::: greybox
*"Write me an essay about diabetes treatments"*
:::
::: bad
Bad example - AI provides a summary, with not much context. People may take it at face value
:::

::: greybox
*"I am writing a university essay on treatments for diabetes.*

_The essay question is {{ XXX }},

_I have these sources {{ XXX }},

_My thoughts are {{ XXX }},

_and I want to make sure I cover {{ THESE POINTS }}.

*Can you help me draft an outline?"*
:::
::: good
Good example - AI has context, and is less likely to hallucinate. You can more easily take ownership of the work.
:::

### 5. Prompting - Are you sure you are ready to prompt?

Use these to decide if you know enough to prompt. If any answer is vague, pause and gather info first.

* **Who is this for?**  
* **What problem are we solving right now?**  
* **What information/context do you already have, and what’s missing?**  
* **What is the ([acceptance criteria](/acceptance-criteria/))?**  

- - -

## Summary - Why this matters now

Big Tech is heavily pushing **agents**. We love agents, however, without proper guardrails, we'll let text generators quietly make business decisions.

Recognise automation bias, design for it, and keep people accountable for their work.
