---
seoDescription: Embedding react server components into AI chat with Vercel AI SDK
type: rule
title: Do you know how to embed UI into an AI chat?
uri: embed-ui-into-an-ai-chat
authors:
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
created: 2024-06-13T17:00:00.000Z
guid: C3402A62-C2F0-4A1C-9922-87B52446915D
---

Embedding a user interface (UI) into an AI chat can significantly enhance user interaction, making the chat experience more dynamic and user-friendly. By incorporating UI elements like buttons, forms, and multimedia, you can streamline the conversation flow and improve user engagement.

<!--endintro-->

### Benefits of Embedding UI into AI Chat

Embedding UI elements in AI chats can:

* Simplify complex interactions by providing users with intuitive options.
* Enhance data collection through structured forms and inputs.
* Improve user experience with multimedia elements like images, videos, and interactive charts.
* Streamline navigation with quick-reply buttons and menus.

### Implementing UI Elements in AI Chats

One library that can help you embed UI elements in AI chats is [Vercel AI SDK](https://sdk.vercel.ai/docs/introduction)

This SDK allows you to integrate AI into your chat applications through the use of React Server Components. Your LLM can stream UI directly to clients without the need for heavy JavaScript.

See here for a demo of the Vercel AI SDK in action: [Vercel AI SDK Demo](https://chat.vercel.ai/).

### Examples

::: ok
![Figure: OK example - using only text-based responses can make the conversation less engaging and efficient](./text-based-chat.png)
:::

::: good
![Figure: Good example - embedding visual UI elements like images can make the conversation much more engaging](./ui-based-chat.png)
:::

### Use Cases

Embedding UI elements in AI chats is beneficial for various use cases, including:

* Customer support: Providing quick-reply buttons for common queries.
* E-commerce: Embedding product images and links for easy browsing.
* Surveys and feedback: Using structured forms to collect user responses.
* Booking and reservations: Streamlining the booking process with date pickers and dropdowns.
* Data visualization: Displaying interactive charts and graphs for data analysis.
