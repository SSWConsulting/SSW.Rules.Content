---
type: rule
title: Do you summarize long conversations for better context retention?
uri: summarize-long-conversations
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
  - title: Jernej Kavka (JK)
    url: https://www.ssw.com.au/people/jk
    img: https://github.com/SSWConsulting/SSW.People.Profiles/raw/main/Jernej-Kavka/Images/Jernej-Kavka-Profile.jpg
created: 2023-05-04T00:24:29.829Z
guid: 17c33700-ec9b-41ea-b7ba-f96bc1877670
---
For very long conversations, it's important to know that you only have a certain number tokens to play with, and if your inputs or outputs have been very long, in a long conversation GPT will start to forget some of the earlier context. To avoid this, you can ask ChatGPT to summarize the conversation and then use that summary as a prompt to refresh the context during future interactions.

<!--endintro-->

Here's how to implement this approach:

1. Copy the essential parts of the conversation
2. Ask ChatGPT to *"Summarize this conversation without losing important information."*
3. Convert the summary into a prompt that can be used in subsequent chats to maintain context

Use the summary prompt on every chat or after several prompts, depending on the size and complexity of the conversation.

::: greybox
“Summarise this conversation without losing important information. Then convert it into a prompt I can use on every chat to refresh the context of the conversation. Then remove any obvious context to shorten the prompt.”
:::
::: good
Figure: Good example prompt - asking ChatGPT to summarize a conversation
:::

By summarizing long conversations and using the summaries as prompts, you can maintain context and ensure that crucial details are not lost, leading to more coherent and informed responses from ChatGPT.