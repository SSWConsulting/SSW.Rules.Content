---
seoDescription: Customize AI applications using GPT API with system prompts that fit your application or company, ensuring consistent responses and tailored interactions.
type: rule
title: Do you use GPT API with system prompt?
uri: use-system-prompt
authors:
  - title: Jack Reimers
    url: https://www.ssw.com.au/people/alumni/jack-reimers/
created: 2023-09-28T12:00:00.000Z
guid: d98b6b99-28a2-4be3-8095-6f5c45094a98
---

When you're building a custom AI application using a GPT API you'll probably want the model to respond in a way that fits your application or company. You can achieve this using the system prompt.

<!--endintro-->

## What is the system prompt?

Requests to and from a GPT API generally have 3 types of messages, also known as roles or prompts:

### 1. User  

User messages are any messages that your application has sent to the model.

### 2. Assistant

Assistant messages are any messages that the model has sent back to your application.

### 3. System

The system prompt is sent with every request to the API and instructs the model how it should respond to each request.

When we don't set a system prompt the user can tell the model to act however they would like it to:

![Figure: GPT's responses without a system prompt](without-system-prompt.png)

![Figure: Responses with a system prompt](with-system-prompt.png)

::: info
**Note:** Depending on the model you're using, you may need to be more firm with your system prompt for the model to listen. Test your prompt using [OpenAI's Playground](https://platform.openai.com/playground) before deploying.
:::

For more information on system prompts, see [OpenAI's documentation](https://platform.openai.com/docs/guides/gpt-best-practices/strategy-write-clear-instructions), or use their [playground](https://platform.openai.com/playground) to start testing your own!
