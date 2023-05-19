---
type: rule
title: Do you know the fundamentals of Prompt Engineering?
uri: fundamentals-of-prompt-engineering
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
related:
  - chatgpt-cheat-sheet
created: 2023-04-18T13:34:41.822Z
guid: 9731b1c3-5c21-4e85-8bb4-cb43e1823867
---
The best way to get up and running with ChatGPT is by using a cheat sheet. Check out our [ChatGPT Cheat Sheet](/chatgpt-cheat-sheet).

In ChatGPT prompt engineering, various elements play a critical role in shaping the user's prompt and obtaining the desired output. These elements are role, result, intent, context, and constraint.

<!--endintro-->

Let's define each of them and provide an example that illustrates their use.

* **[Role:](/give-chatgpt-a-role)**  The role defines the specific function or identity that the ChatGPT model is expected to assume during the conversation. It helps set the tone and expertise level expected from the model's responses.
* **Result:** The result refers to the desired outcome or specific information the user seeks to obtain from the interaction with ChatGPT. This guides the model in providing relevant and useful responses.
* **[Intent:](/define-intent-in-prompts)** Intent represents the user's goal or the purpose behind the interaction with the ChatGPT model. It helps the model understand the user's needs and respond accordingly.
* **[Context](https://www.ssw.com.au/rules/tell-chatgpt-to-ask-questions):** Context refers to any background information or situational details that are relevant to the conversation. Context helps the model understand the broader scenario and provide appropriate responses that fit the situation.
* **Constraint:** A constraint is a condition or limitation placed on the model's response. It ensures that the output adheres to specific requirements or avoids certain topics, styles, or content.

Suppose you want to ask ChatGPT for advice on how to improve your public speaking skills. Here's how each part can be framed:

::: greybox
"Give me some public speaking tips"
:::
::: bad
Figure: Bad example
:::

::: greybox
"As a career coach, I need your advice on improving my public speaking skills. I have an important presentation at my kid's school for the year 7 class, and I'm feeling nervous. Can you provide me with some practical and easy-to-implement tips that don't require professional coaching?"
:::
::: good
Figure: Good example
:::

Here’s how that breaks down:

* **Role:** Career coach
* **Result:** Advice on improving public speaking skills
* **Intent:** To receive practical and actionable tips to enhance public speaking abilities
* **Context:** The user is preparing for an important presentation for a young audience and needs help overcoming nervousness and delivering a compelling speech.
* **Constraint:** The advice should be easy to implement and not require extensive training or professional coaching.

By specifying the role, result, intent, context, and constraint in the prompt, you can guide ChatGPT to deliver a more relevant and targeted response, addressing your specific needs and expectations.

::: good
![Figure: Another good example](new-prompt-engineering-only-prompt.png)
:::

`youtube: https://www.youtube.com/embed/EYjG6i53-xk`
**Video: This Will Make You Better than 99% ChatGPT Users (6 min)**