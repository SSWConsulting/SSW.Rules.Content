---
type: rule
title: ChatGPT - Do you use Reflexion to iterate on outputs?
uri: reflexion
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair/
created: 2023-09-20T07:43:12.917Z
guid: 41304829-c730-411c-b725-016882082231
---

Have you ever received an output from ChatGPT and wondered if it could be improved, but you don't have specific complaints? Reflexion (spelled with an 'x', not a 'ct') is way to improve the output from ChatGPT by having ChatGPT critique itself.

<!--endintro-->

## What is Reflexion?

Think of Reflexion like a self-check for your computer's "brain" (the Large Language Model or LLM). Just like you might double-check your work before submitting it, Reflexion lets the computer double-check its own answers. This helps make those answers better each time.

::: greybox
Just like self-reflection is used as a coding technique, the technique of getting an LLM to reflect on its answers is called 'Reflexion'
:::
**Figure: Why 'Reflexion' is a proper noun as per the [MIT, Princeton, and Northeastern research](https://arxiv.org/pdf/2303.11366.pdf)**

Imagine you're baking a cake. The first time you try, it might not be perfect. Maybe it's too dry or lacks flavor. You taste it, figure out what went wrong, and try again. That's what Reflexion does for computer-generated answers. It helps the computer "taste-test" its own work, so the next cake/answer is even better.

## Why is Reflexion important?

Reflexion takes an LLM into a more nuanced and iterative approach to problem-solving, which closely mirrors the human cognitive processes. It asks the LLM to evaluate its output, which optimizes the results for accuracy.

## How to do it

1. **Initial prompt**: Start by asking the LLM to complete a task.
2. **Reflexion prompt**: Ask the LLM to rate its own output and provide recommendations for improvement to your prompt.
3. **Iterate**: Make adjustments to your next prompt based on the LLM's feedback and repeat the process.
4. **Contextual Testing (optional)**: Once satisfied, test the improved prompt in a new chat to remove any lingering biases.

::: greybox
Write me a recipe for healthy cookies.
:::

::: bad 
Figure: Bad Example - This prompt doesn't engage the LLM in a Reflexion loop and misses the opportunity for iterative improvement
:::

::: greybox

**Prompt #1:** "Write me a recipe for healthy cookies."

**Prompt #2:** "Rate the recipe /10 for healthiness and tastiness. Also provide recommendations for improvement and provide an updated recipe."

**Prompt #3:** "Implement recommendations 1 and 3 then repeat."

:::

::: good 
Figure: Good Example - This prompt initiates a Reflexion loop by asking the LLM to evaluate and critique its output
:::

### Iteration - Manual Edits vs Automatic Edits
ChatGPT is great at giving recommendations for improvement, but sometimes it doesn't apply them very well. You can always apply some of the recommendations manually and feed your new version back in.

In the good example above, after Prompt #2, you could update the recipe yourself and change Prompt #3 to say to evaluate the new version.

If the recommendation is something logical and systematic like changing "raisins" to "dates" then ChatGPT will probably do a good job.
On the other hand, if it is something more abstract, then it may not do the best job.

## Bonus - Comparative evaluation

You can also use Reflexion to help make decisions by asking the LLM for multiple options and then using Reflexion to assign scores and critical evaluations to each option. These scores will make it easier to decide on the best approach. See the pros and cons rule - https://ssw.com.au/rules/pros-and-cons-and-ratings/

![Figure: GPT-4 was found to be 30% more accurate on coding tests when asked to critique itself in self-reflective loops](reflexion-figure.png)
[See more at - https://newatlas.com/technology/gpt-4-reflexion/](https://newatlas.com/technology/gpt-4-reflexion/)
