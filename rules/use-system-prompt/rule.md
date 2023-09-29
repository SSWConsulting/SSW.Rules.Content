---
type: rule
title: GPT - Do you use the system prompt?
uri: use-system-prompt
authors:
  - title: Jack Reimers
    url: https://www.ssw.com.au/people/jack-reimers
created: 2023-09-28T12:00:00.000Z
guid: d98b6b99-28a2-4be3-8095-6f5c45094a98
---

When you're building a custom AI application using a GPT API you'll probably want the model to respond in a way that fits your application or company.
You can achieve this using the system prompt.

<!--endintro-->

### What is the system prompt?

Requests to and from a GPT API generally have three types of messages, also known as roles or prompts.

**User**  
User messages are any messages that your application has sent to the model.

**Assistant**  
Assistant messages are any messages that the model has sent back to your application.

**System**  
The system prompt is sent with every request to the API and instructs the model how it should respond to each request.

![Figure: The default helpful assistant prompt](helpful-assistant.png)

![Figure: We can use the system prompt to make GPT unhelpful](unhelpful-assistant.png)

For more information on system prompts, see [OpenAI's documentation](https://platform.openai.com/docs/guides/gpt-best-practices/strategy-write-clear-instructions), or use their [playground](https://platform.openai.com/playground) to start testing your own!
