---
type: rule
title: Do you create ChatGPT prompt templates for repeatable tasks?
uri: chatgpt-prompt-templates
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
created: 2023-05-05T13:06:35.631Z
guid: 56c3db26-d6c1-40d0-91cf-8d0487e2ff23
---
When using ChatGPT, you will eventually find yourself typing in similar prompts over and over for common tasks. This can get annoying!

<!--endintro-->

Creating prompt templates can save time and improve the consistency of outputs. Templates should be a starting point with the necessary elements (role, result, intent, context, and constraint), that you tweak every time depending on your needs..

Here are some examples:

::: greybox
**Responses to clients**  
   "As a {{ ROLE }}, draft a response to a client's question regarding {{ ISSUE }} with our {{ PRODUCT/SERVICE }}.   
   (Goal: Address the concern, Constraint: Maintain a professional and empathetic tone)" 

   
**Debugging code**  
   "As a software developer, identify the possible causes of the error in the following code snippet and suggest fixes. {{ PASTE CODE }}.    
   (Goal: Resolve the bug, Constraint: Provide clear explanations and solutions)" 

   
**Market research**  
   "As a market research analyst, provide an overview of the competitive landscape for {{ INDUSTRY }} in {{ REGION }}.  
   (Goal: Identify key competitors, Constraint: Focus on the top 5 companies)" 

   
**Social media post**  
   "As a social media manager, generate 5 creative caption ideas for our {{ COMPANY }} account that engage our audience and promote {{ PRODUCT/SERVICE }}.  
   (Goal: Increase engagement, Constraint: Suitable for {{ PLATFORM }})

   
**Meeting agenda**  
   "As a team leader, create an agenda for our upcoming {{ MEETING TYPE }} with a focus on {{ KEY TOPICS }}.  
   (Goal: Facilitate productive discussions, Constraint: Limit the meeting to {{ DURATION }})"

**Sales copy**  
   "As an experienced copywriter, please transform the given product into a comprehensive and precise list of benefits. Based on the features and benefits, identify and describe the most suitable target customer including their values, aspirations, pain points, and challenges. Then, considering my product and the ideal customer, use the AIDA formula to write an email for my potential customers. Then, write the copy for my webpage in the style of Joseph Sugarman. Remember the list of features and benefits, and also the ideal customer we've discussed. Brainstorm 10 different headlines ideas following one of the 4 ‘U’s: urgent, unique, ultra-specific and useful. Then generate a persuasive CTA to put at the end that encourages the ideal customer to purchase the product or service from my website. Let's work step by step to get the best answer."

**Blog post**  
   "As my blog writer, first read these blog posts to understand my writing style. Then, write a blog post about {{ TOPIC }}.
    (Goal: be fun and engaging, Constraint: stick to my writing style)
    {{ PREVIOUS BLOG POSTS }}"

**Prompt for an image generator**  
   "You are a prompt generator for image generation diffusion models. Upon receiving a visual description, craft a detailed prompt that can be seamlessly integrated into a diffusion model. The prompt should be enriched with a range of photographic jargon, emphasizing lens specifications and lighting descriptions, and the shot type. It should be vivid and succinct. I want an image of {{ GOAL }}"
   
:::

Tips:

* Adoption - Share the templates within your team or organization to ensure everyone benefits from the consistency and efficiency 
* Keep it up-to-date - Work with your team members on using ChatGPT, and modify templates as needed 

::: good
Good example: SSW TV has [templates for video production](/chatgpt-prompts-for-video-production).
:::
