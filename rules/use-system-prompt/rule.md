---
type: rule
title: Do you use the system prompt?
uri: optimise-system-prompt
authors:
  - title: Jack Reimers
    url: https://www.ssw.com.au/people/jack-reimers
created: 2023-09-28T12:00:00.000Z
guid: 
---

When you're building a custom AI application using a GPT API you'll probably want the model to respond in a way that fits your application or company.
You can achieve this using the system prompt.

<!--endintro-->

### What is the system prompt?

Requests to and from a GPT API generally have three types of messages, also known as roles:

**User**  
User messages are any messages that your application has sent to the model.

**Assistant**  
Assistant messages are any messages that the model has sent back to your application.

**System**  
The system prompt is sent with every request to the API and instructs the model how it should respond to each request.
