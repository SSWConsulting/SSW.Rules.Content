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

Suppose you're seeking advice on improving coding practices, specifically focusing on C#. Here's how each part can be framed:

::: greybox
"Give me some C# coding tips"
:::
::: bad
Figure: Bad example - prompt is vague and lacking context
:::

::: greybox
"As a senior software engineer, I need your guidance to improve my C# coding practices. I am working on a large-scale data processing project where readability and efficiency are critical. Can you provide me with some specific, actionable tips to enhance my code's performance while ensuring it remains clean and easy for others to understand?"
:::
::: good
Figure: Good example - prompt contains context, goal, and constraint
:::

Here’s how that breaks down:

* **Role:** Senior software engineer
* **Result:** Guidance to improve Python coding practices
* **Intent:** To receive specific and actionable tips to enhance Python code efficiency and readability
* **Context:** The user is working on a large-scale data processing project
* **Constraint:** The advice should contribute to both the performance and cleanliness of the code, catering to the requirements of readability and efficiency in a large-scale project setting.

By specifying the role, result, intent, context, and constraint in the prompt, you can guide ChatGPT to deliver a more relevant and targeted response, addressing your specific needs and expectations.

::: good
![Figure: Another good example](new-prompt-engineering-only-prompt.png)
:::

`youtube: https://www.youtube.com/embed/EYjG6i53-xk`
**Video: This Will Make You Better than 99% ChatGPT Users (6 min)**