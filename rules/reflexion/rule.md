---
type: rule
title: ChatGPT - Do you use Reflexion to iterate on outputs?
uri: reflexion
authors:
  - title: Piers
    url: https://www.ssw.com.au/people/piers-sinclair/
created: 2023-09-20T07:43:12.917Z
guid: 41304829-c730-411c-b725-016882082231
---

Have you ever received an output from ChatGPT or another large language model and wondered if it could be improved? Reflexion (spelled with an 'x', not a 'ct') is an iterative approach that allows you to fine-tune outputs by involving the model in the evaluation process.

<!--endintro-->

![Figure: [Reflexion delivers better results](https://www.promptengineering.org/reflexion-an-iterative-approach-to-llm-problem-solving/)](reflexionresults.png)

## Why is Reflexion important?

Reflexion takes an LLM into a more nuanced and iterative approach to problem-solving, which closely mirrors the human cognitive processes. It asks the LLM to evaluate its output, which optimizes the results for accuracy.

## How to do it

1. **Initial prompt**: Start by asking the LLM to complete a task.
2. **Reflexion prompt**: Ask the LLM to rate its own output and provide recommendations for improvement to your prompt.
3. **Iterate**: Make adjustments to your prompt based on the LLM's feedback and repeat the process.
4. **Contextual Testing**: Once satisfied, test the improved prompt in a new chat to remove any lingering biases.

::: greybox
"Write me a recipe for healthy cookies"
:::

::: bad 
Figure: Bad Example - This prompt doesn't engage the LLM in a Reflexion loop and misses the opportunity for iterative improvement>
:::

::: greybox
"Write me a recipe for healthy cookies. Rate the recipe /10 for healthiness and tastiness. Also provide recommendations for improvement."
:::

::: good 
Figure: Good Example - This prompt initiates a Reflexion loop by asking the LLM to evaluate and critique its output>
:::

## Extra - Comparative evaluation

You can also use Reflexion to help make decisions by asking the LLM for multiple options and then using Reflexion to assign scores and critical evaluations to each option. These scores will make it easier to decide on the best approach.
