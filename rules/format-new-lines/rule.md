---
type: rule
title: Do you enhance readability with line breaks and spacing?
uri: format-new-lines
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan/
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman/
related:
  - add-useful-and-concise-figure-captions
  - use-the-right-html-figure-caption
created: 2021-07-06T01:13:05.707Z
archivedreason: ""
guid: e05522a7-1822-412c-80ee-5619039f7d96
---

Sometimes when writing content, you need to make the decision to keep it on the same line or put it on a new line.

It is recommended that notes, tips and figures should be on a new line to enable better readability. It can also be beneficial to bold those words.

❗️ Important - Line breaks in web pages (HTML) can be used, but when done to create spacing it becomes a ❌ bad practice!
Learn more: <https://blog.hubspot.com/website/html-line-break>

When referring to emails and/or informal documents, line breaks can be used for spacing since they are easier than dealing with margins, and we don’t care about syntax.

It is recommended to include spaces after a figure description - in web design, use CSS margins to achieve this.

::: greybox
Test the login functionality thoroughly **Note:** try both valid and invalid credentials
:::
::: bad  
Figure: Bad Example - No line break before the note.
:::

::: greybox
Good way: use the Dynamics 365 (formerly CRM 2016) toolbar?  
**Note:** We have a suggestion that Outlook should allow you to put the CRM2016 URL into Tools | Options so this is better integrated
:::
::: good  
Figure: Good Example - The note being on a fresh line makes it much easier to read.
:::

This is also recommended when sending URLs for readability.

::: greybox
Hey Bob,

Check out this awesome new video about the SSW Cultural Exchange Program! <https://youtu.be/dfE_Y8fy_wo?si=NEcQLAPafAWKa7m5>

:::
::: bad  
Figure: Bad Example - No line break before the URL.
:::

::: greybox
Hey Bob,

Check out this awesome new video about the SSW Cultural Exchange Program!

<https://youtu.be/dfE_Y8fy_wo?si=NEcQLAPafAWKa7m5>
:::
::: good  
Figure: Good Example - The URL being on a fresh line makes it much easier to read.
:::

This is also recommended when sending PBIs for better readability.

::: greybox
Hey Adam,

I have 2 PBIs on my next to-do in the coming sprint: Product Backlog Item 88994: ⚡Performance | Create a new App Service plan and Product Backlog Item 88823: 🚗 Azure | Create a new App Service Plan in West US for SL production resource group.
I will do the IoC after.

:::
::: bad  
Figure: Bad Example - No list for spacing PBIs.
:::

::: greybox
Hey Adam,

I have 2 PBIs in this Sprint:
* PBI 88994: ⚡Performance | Create a new App Service plan
* PBI 88823: 🚗 Azure | Create a new App Service Plan in West US for SL production resource group.
I will do the IoC after.

:::
::: good  
Figure: Good Example - List is used to space PBIs.
:::

See the [Markdown Guide](https://www.markdownguide.org/basic-syntax/#line-breaks) for more information on line breaks.
