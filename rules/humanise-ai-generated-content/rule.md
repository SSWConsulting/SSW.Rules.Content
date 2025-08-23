---
type: rule
tips: ""
title: Do you make ChatGPT produce human-sounding content?
seoDescription: Enhance the human-like quality of your AI-generated content with techniques such as using personas, incorporating personal experiences, varying sentence lengths, and more to make GPT's content engaging, relatable, and valuable to readers.
uri: humanise-ai-generated-content
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren/
related:
  - train-ai-to-write-in-your-style
created: 2024-06-04T00:04:05.234Z
guid: 6a85e236-0988-4c02-9003-4d924f9092f0
---
Creating content that sounds human is essential for engaging readers and meeting quality standards. AI-generated content can sometimes feel robotic, lacking the natural flow and personal touch that human writing possesses.

We can use specific techniques to make ChatGPT's content more human-like, improving its readability and relatability.

<!--endintro-->

## 1. Use personas

Assign ChatGPT a specific role, such as a friendly advisor or an expert in a particular field, to guide the tone and style.

**Prompt example:** _"As a seasoned travel blogger, describe the best destinations for solo travelers."_

## 2. Incorporate personal experiences

Share personal anecdotes or opinions to add authenticity.

**Prompt example:** _"Include this story about my favorite childhood memory related to the topic: {{ ADD STORY }}"_

## 3. Fact insertion

Add relevant and recent facts to make the content more informative and credible… Things that the AI’s cut off date mean it couldn’t know.

**Prompt example:** _"Include these statistics on the current market trends for this industry: {{ ADD FACTS }}"_

## 4. Perplexity

Avoid common AI phrases and terms that make the text sound unnatural. Perplexity measures the complexity and unpredictability of text. To make AI-generated content sound more human, avoid overused and predictable phrases. This enhances the natural flow and makes the content more engaging.

**Prompt example:** _"Don’t always use the most natural words. Use the following words fewer than three times on this page: unique, ensure, utmost, meticulous, meticulously, navigate, navigation, digital era, art of, secrets of, ever-evolving, unlock, bespoke, realm of, utilize, synthesize, conceptualize, paradigm, leverage, pivot, robust, synergy, optimize, utilize, orchestrate, cultivate.”_
     
## 5. Burstiness

Vary sentence and paragraph lengths to create a dynamic flow.

**Prompt example:** **"Mix short and long sentences to enhance readability."**

## 6. **Unfluffing:**

Ensure every sentence provides value and is actionable, removing unnecessary filler content.

**Prompt example:** _"Eliminate vague statements and focus on specific, useful information."_

## 7. Adding flavor

Make the content more engaging and conversational by adding humor, anecdotes, and a conversational tone.

**Prompt example:** "Engagement is the highest priority. Be conversation, empathetic, and occasionally humerous. Use idioms, metaphors, anecdotes, and natural dialogue."

## 8. Targeting specific audiences

Tailor the content to the preferences and needs of your target audience.

**Prompt example:** _"Adjust the tone and vocabulary to match the reading level and interests of a young adult audience."_

## 9. Training on your writing style

Provide samples of your own writing to train ChatGPT to mimic your unique voice.

See [Do you know how to train an AI to write in your style?](https://www.ssw.com.au/rules/train-ai-to-write-in-your-style) for a deep dive into how to do this effectively.

## 10. Avoid em dashes (—)

Too many em dashes make text feel mechanical and AI-generated. Instead, use commas, colons, or full stops for a more natural flow.

**Prompt example:** _"Write this without using em dashes. Replace them with commas, colons, or periods where appropriate."_

---

## Prompt template

::: greybox
"As a {{ ROLE }}, write an article about {{ TOPIC }}.

Include this recent statistic: {{ RECENT STATISTIC, OR URL TO RECENT DATA }}.

Mention this personal anecdote: {{ ADD RELEVENT PERSONAL STORY }}.

Don’t always use the most natural words. Use the following words fewer than three times on this page: unique, ensure, utmost, meticulous, meticulously, navigate, navigation, digital era, art of, secrets of, ever-evolving, unlock, bespoke, realm of, utilize, synthesize, conceptualize, paradigm, leverage, pivot, robust, synergy, optimize, utilize, orchestrate, cultivate.

Mix short and long sentences to enhance readability.

Avoid using em dashes.

Eliminate vague statements and focus on specific, useful information.

Engagement is the highest priority. Be conversation, empathetic, and occasionally humerous. Use idioms, metaphors, anecdotes, and natural dialogue.

Adjust the tone and vocabulary to match the reading level and interests of {{ INTENDED AUDIENCE E.G. DEVELOPERS}}.

Analyze the attached articles for tone, structure, and vocabulary, then use this style to write new content."
:::

::: good 
Figure: Good example - Incorporating current and relevant facts to add credibility
:::

By applying these techniques, you can significantly improve the human-like quality of AI-generated content, making it more engaging, relatable, and valuable to your readers.
