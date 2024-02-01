---
type: rule
archivedreason:
title: Do you use ChatGPT for better emails?
guid: ba44fc09-77a7-4d40-bc74-cc8db101db22
uri: chatgpt-for-email
created: 2023-07-06T12:00:00.0000000Z
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
related:
 - use-different-tones
 - shot-prompts
 - generating-multiple-responses-from-chatgpt
 - chatgpt-prompt-templates

---

Writing the perfect email can be a time-consuming and challenging task. From drafting the initial message to ensuring the tone is just right, there's a lot to consider. This is where ChatGPT can be a powerful tool.

<!--endintro-->

# Drafting emails

ChatGPT can help you draft entire emails or parts of them. For example, if you are unsure how to begin an email to a potential employer, you can ask ChatGPT for suggestions.

::: greybox
"I need to inform our users about a scheduled system downtime for maintenance. Could you help me draft an email that clearly communicates the details and minimizes any inconvenience?"

"I need to write an email to our software development team commending them for their hard work and commitment during a recent product launch. Could you help me draft this appreciation email?"
:::

# Ask for options

You can ask for [multiple options](/generating-multiple-responses-from-chatgpt/), from which you can choose the best one.

::: greybox
“Give me 3 different options to use”
:::

# Length Adjustment

ChatGPT can adjust the length of an email response according to your requirements.

::: greybox
“Shorten this email for me”

“Expand these points into an email {{ PASTE IDEAS }}
:::

# Summarize long emails

Sometimes the important points in an email are buried inside walls of text.

::: greybox
“I received this email. Can you read it and give me the gist of it? {{ PASTE EMAIL }}”
:::

# Polishing

If you've written an email but aren't satisfied with the wording, you can ask ChatGPT to help improve it. It can help make your language more professional, courteous, concise, or whatever else you need.

::: greybox
“Rephrase this to sound more polite/professional/direct: {{ PASTE EMAIL }}”

“Proofread this email and give suggestions: {{ PASTE EMAIL }}”

“Check my spelling: {{ PASTE EMAIL }}”
:::

# Tone Analysis

You can use ChatGPT to analyze the tone of the emails you receive or send. For example, you can ask it to identify if an email sounds angry, respectful, sarcastic, etc. This can help you craft appropriate responses. Tip: ask for an informal style

::: greybox
“Is this an angry email?”

“Will this email sound too forceful to my client?”

“This email is confusing. What are they telling me?”
:::

# Customizing for context

You can instruct ChatGPT to [adjust the content and tone](/use-different-tones/) of the generated email response based on your needs. For example, if you want to decline a proposal, you can ask ChatGPT to write a polite declination.

::: greybox
“This email is going to my client. How can I make it better?”

“Rewrite this in a polite way for my boss.”

“Make this announcement more engaging for my employees."
:::

# Replying to a thread

Sometimes you don't know where to start when replying to a thread of messages. You can use ChatGPT to get a quick start.

::: greybox
“You are me, and my name is {{ NAME }}. Draft a reply to the email thread below. Be semi-formal, direct, and concise. If I include requests to the recipient, use a numbered list.
Here is the thread: {{ PASTE THREAD }}”
:::

# Personal email template

When using ChatGPT to draft emails for you, it can be useful to have your own repeatable prompt (link) to use each time.

**Tip \#1:** Give [multiple shot prompts](/shot-prompts/) so it learns your email style.

**Tip \#2:** Create a [prompt template](/chatgpt-prompt-templates/) so it writes in your style.

Your personal prompt might look like this:

::: greybox
“Help me craft a semi-formal, direct, friendly, and concise email. The subject is {{ SUBJECT }}. Start with 'Hi {{ NAME }},' and in the email, include the following action items in a numbered list: {{ ACTION ITEMS }}. Refer to our previous conversation about {{ TOPIC }} in this email thread, and ask me any questions you need for context: {{ PASTE THREAD }}”
:::

You can do this for specific scenarios too:

::: greybox
“Write a follow-up email to a client named {{ NAME }} who inquired about our services. I'm the account manager handling this client, my name is {{ NAME }}, and I can be reached at {{ NUMBER }}. Please also include a link to our scheduling tool, {{ LINK }}, to book a call at a convenient time. Make the email semi-formal, courteous, friendly, and concise.”
:::

# General tips

* Avoid ChatGPT for emails that you want to have a personal feel.
* Be aware that ChatGPT emails can sound robotic and insincere. Don’t be afraid to make edits – remove parts and add parts to make it sound more like you.
