---
type: rule
tips: ""
title: Do you avoid Automation Bias? (aka AI Slop)
seoDescription: Did you know that AI has the potential to make your work worse? Learn the common pitfalls so that AI can help, not hinder.
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

```
youtube: https://www.youtube.com/embed/kDS5pwelhNM?si=_nqw5XQWgpib5b8z
```

***\*Video: How AI is making you dumber (3 min)\****



Automation bias is a type of cognitive bias. A thinking shortcut, where we overly rely on machine-generated decisions and forego critical thinking. It’s a brain problem, not a model problem.



## Errors from automation bias

There are two types of errors made due to automation bias:

* **Error of commission** - Doing the wrong thing because the system suggested it (e.g. accepting a flawed suggestion, getting ChatGPT to write your essay, etc.)
* **Error of omission** - Failing to act because the system didn't flag a problem (e.g. shipping flawed code, because Copilot review approved it)

### Where automation bias shows up

* **Coding assistants (e.g. Copilot)** - They make you faster, not necessarily better. The more complex some generated code is, the more likely you'll be to click "Accept"

* **Google Search (especially 'AI Overview')** - These search engines are incentivised to return the most relevant content, rather than the most correct content

* **GPS Navigation** - Countless cases of people driving their car into water 'because the app told them to' (it's happened dozens of times!)

  

### Why do we fall for it?

#### Task complexity + time pressure

Under stress, cognition narrows and we rely more heavily on mental shortcuts. AI tools initially promise to "do less work," but this productivity gain often shifts expectations, leading to "do more work in the same time".

This creates a vicious cycle where increased time pressure makes us even more likely to accept AI outputs without proper scrutiny, amplifying our over-reliance on automation.

#### Social aspects & accountability

If there are two people within a company who don't know each other well, and review each other's code, they are less likely to care about what each other thinks, and they'll put less effort into a review.

#### Personality traits

More extroverted people may move quickly and accept outputs more readily.

People high in neuroticism may doubt their own outputs, and thus doubt AI's outputs too.

This isn't prescriptive, just a pattern to be aware of.

### What doesn't fix it (but seems like it should)

* **Human-in-the-loop** - This only covers legal accountability. Just because a human is in the loop, doesn't mean they are critically evaluating the output
* **Higher model accuracy** - Even a 99.9% accurate model can still be wrong, furthermore - a more accurate model can lead to more complacency
* **Training people that "software is often wrong"** - Makes people think they know more about the software than they do, leading to overconfidence

### What actually helps

#### Don't submit AI content that you don't fully understand

If AI helps you create work, that's great. 

But what if someone asks you a technical question about the work, that you can't answer? 

It then becomes very obvious that this work is not your own - worse, it might even mean the solution is suboptimal.

Remember: own your work.

#### Show error rates clearly

AI and automation tools that are prone to mistakes should include exact error rates:

::: greybox
AI sometimes makes mistakes, ensure you check its output.
:::
::: bad
Highly vague warning, most people will ignore it
:::

::: greybox
Studies have found that 25% of AI-generated code has security vulnerabilities. Ensure you review it.
:::
::: good
More specific warning, people are more likely to take it seriously
:::

#### Four Eyes Principle (with real relationships)

::: greybox
"Random Person: Hey, can you review this code I wrote with Copilot?"

Bob: I don't know you well, and I have better things to do... approved.
:::
::: bad
Random pair reviews, people don't know each other well, so they won't feel accountable
:::

::: greybox
Alice: Hey Bob, can you review this code I wrote with Copilot?

Bob: Sure, I want to make sure I don't let Alice down, so I'll take a closer look.
:::
::: good
Pair reviews with people who know each other well, so they feel accountable
:::

#### Information, not recommendation

Ask AI to present information and sources before it asserts conclusions. Avoid instructive "do this" prompts.

::: greybox
"Write a summary of diabetes treatments"
:::
::: bad
AI provides a summary, with not much context. People may take it at face value
:::

::: greybox
I am writing a university essay on treatments for diabetes. The essay question is {xyz}, I have these sources {abc}, my thoughts are {123}, and I want to make sure I cover {these points}. Can you help me draft an outline?
:::
::: good
AI has context, and is less likely to make stuff up. People are more likely to critically evaluate the output
:::

##### Four directing questions (readiness gate before prompting)

Use these to decide if you know enough to prompt. If any answer is vague, pause and gather info first.

* **Who is this for?**  
* **What problem are we solving right now?**  
* **What does success look like ([acceptance criteria](/acceptance-criteria/))?**  
* **What information/context do you already have, and what’s missing?**  

## Why this matters now

Big Tech is heavily pushing **agents**. We love agents, however, without proper guardrails, we'll let text generators quietly make business decisions. Recognise automation bias, design for it, and keep humans accountable for their work.
