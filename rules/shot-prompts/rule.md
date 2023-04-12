---
type: rule
title: Do you know when to use 0-shot, 1-shot, or multi-shot prompts (e.g. give
  it 1 or more examples)?
uri: shot-prompts
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2023-04-12T13:55:36.349Z
guid: 5d53a8ed-35c1-43cd-8a1e-efc8fad352f6
---
You can give ChatGPT examples of the type of output you want, including the format. Each example you feed it is known as a “shot”.
 
Understanding when to use 0-shot, 1-shot, or multi-shot prompts can help you get the most out of ChatGPT. These approaches allow the model to learn from different contexts, making it more likely to generate the desired output.
            
<!--endintro-->

Here are some guidelines for using 0-shot, 1-shot, and multi-shot prompts:

### 0-shot prompts

Used when you want the model to generate a response without any examples. These prompts can be helpful for general questions or tasks where providing examples is unnecessary or could add confusion. 

Use 0-shot prompts when you trust the model's general knowledge to provide a sufficient answer.

### 1-shot prompts

Provide a single example of the desired output, helping to guide the model's response. This approach can be useful when you need a specific format or style or when the task requires some level of guidance. 

Use 1-shot prompts when you want to nudge the model in the right direction without overwhelming it with multiple examples.
 
Example 1-shot prompt: 

:::greybox
"Translate the following English sentences into French. Here's an example:  
'I love playing soccer.' -> 'J'aime jouer au football.'

Now translate: 'She enjoys reading books.'"
:::
**Figure: 1-shot example - providing a single example of translation**
 
### Multi-shot prompts 

Offer multiple examples, allowing the model to learn from various instances. These prompts can be beneficial when dealing with complex tasks, where providing a range of examples helps the model better understand the desired outcome. 

Use multi-shot prompts when a single example might not be sufficient for guiding the model or when you want to demonstrate a pattern or trend.
 
Example multi-shot prompt: 

::: greybox
"Translate the following English sentences into French. Here are some examples:
- 'I love playing soccer.' -> 'J'aime jouer au football.'
- 'The weather is nice today.' -> 'Le temps est agréable aujourd'hui.' 

Now translate: 'They are going to the park.'"
:::
**Figure: Multi-shot example - providing multiple examples of translations**
 
By knowing when to use 0-shot, 1-shot, or multi-shot prompts, you can optimize your interactions with ChatGPT and receive more accurate and tailored responses.