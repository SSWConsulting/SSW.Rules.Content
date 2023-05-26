---
type: rule
archivedreason:
title: Do you know how GPT tokens work?
guid: 2f765699-a933-45a7-94b5-b03eb5c01a5a
uri: gpt-tokens
created: 26/05/2023
authors:
- title: Seth Daily
  url: https://www.ssw.com.au/people/seth-daily
related:

---

GPT models utilize "tokens" as their smallest units of text. These tokens can be as small as a single character, like "a," or as large as a word, such as "apple." Interestingly, tokens can also represent parts of a word.
For instance, in GPT's perspective, the word "unhappiness" could be tokenized into three parts: "un," "happi," and "ness." Each of these parts is considered a separate token. This flexible understanding of tokens is what allows GPT models to efficiently break down text data for analysis.

<!--endintro-->

**How GPT Models Utilize Tokens**

These models are trained on vast amounts of text data, wherein the data is divided into tokens. Through this process, the model comprehends the statistical relationships between tokens, enabling it to generate new text that mirrors the style and content it was trained on.

**The Influence of Tokens on ChatGPT's Performance**

ChatGPT breaks down an input message into tokens and uses these to generate a sequence of output tokens. This reflects what it has learned during training. The model can process only a specific number of tokens in a single instance, counted as the token limit. This limit is around 4000 for GPT-3.5 and about 8000 for GPT-4.

For example, if you send a message of 10 tokens to ChatGPT and it responds with a message of 20 tokens, that would count as 30 tokens used. This count includes both input and output tokens.

**How Token Allocation Impacts Response Quality**

ChatGPT “remembers” elements of a conversation until it reaches its token limit. Having longer conversations helps it to retain context as you refine the responses, which can be useful (See SSW.Rules | Do you use chained prompting?). However, it is important to be mindful that although longer conversations give more context, at a certain point (its token limit), ChatGPT will start to “forget” earlier parts of a conversation. This results in truncated responses or loss of context.

**Tips for Managing Tokens**

1.	Limit prompt length: Since the number of input tokens affects the total token count, keep your prompts concise if you need a long answer. This leaves more room for ChatGPT's responses.

2.	Control the length of responses: You can set a maximum token limit for ChatGPT's responses. This can prevent the model from generating overly long responses that consume too many tokens. ChatGPT is not great at counting words but adheres well to token limits.
 
 Examples: 
    List the differences between Python and Java using 70 tokens.
    Explain the principles of RESTful API design using 100 tokens.

3.	Clear prompting: Direct prompts can lead to more efficient token usage. Try to be specific and clear in your prompts to get a better response that uses fewer tokens and doesn’t give you background info you’re not interested in.

Tip: Refining prompts can help optimize token usage and improve your ChatGPT efficiency. See SSW.Rules | Do you create ChatGPT prompt templates for repeatable tasks?

4.	Balancing complex queries: There are scenarios where complex queries or detailed explanations may require a large number of tokens. In such cases, it's essential to find a balance between providing enough context and keeping the token count manageable. You can use techniques like summarization or abstraction to reduce the token count while keeping the important information. See SSW.Rules | Do you summarize long conversations for better context retention?
  
  Examples:
    Summarization: “Summarize your last reply while keeping all the important points”
    Abstraction: “Abstract the main arguments in your last response”
