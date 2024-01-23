---
type: rule
title: Do you know where to add new lines?
uri: format-new-lines
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
  - add-useful-and-concise-figure-captions
  - use-the-right-html-figure-caption
created: 2021-07-06T01:13:05.707Z
archivedreason: ""
guid: e05522a7-1822-412c-80ee-5619039f7d96
---

Sometimes when writing content, you need to make the decision to keep it on the same line or put it on a new line.

It is recommended that notes, tips and figures should be on a new line to enable better readability. It can also be beneficial to bold those words.

::: greybox
Good way: use the Dynamics 365 (formerly CRM 2016) toolbar? 
**Note:** We have a suggestion that Outlook should allow you to put the CRM2016 URL into Tools | Options so this is better integrated
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

Check out this awesome new video about the SSW Cultural Exchange Program! https://youtu.be/dfE_Y8fy_wo?si=NEcQLAPafAWKa7m5

:::
::: bad  
Figure: Bad Example - No line break before the URL.
:::

::: greybox
Hey Bob, 

Check out this awesome new video about the SSW Cultural Exchange Program! 

https://youtu.be/dfE_Y8fy_wo?si=NEcQLAPafAWKa7m5
:::
::: good  
Figure: Good Example - The URL being on a fresh line makes it much easier to read.
:::

This is also recommended when sending PBIs for better readability.

::: greybox
Hey Adam, 

I have 2 PBIs on my next to-do in the coming sprint: [Product Backlog Item 88994](https://dev.azure.com/ssw/SSW.Induction/_workitems/edit/88994): ⚡Performance | Create a new App Service plan and [Product Backlog Item 88823](https://dev.azure.com/ssw/SSW.Induction/_workitems/edit/88823): 🚗 Azure | Create a new App Service Plan in West US for SL production resource group.
I will do the IoC after.

:::
::: bad  
Figure: Bad Example - No new lines for PBIs.
:::

::: greybox
Hey Adam,

I have 2 PBIs in this Sprint:
- [PBI 88994](https://dev.azure.com/ssw/SSW.Induction/_workitems/edit/88994): ⚡Performance | Create a new App Service plan 
- [PBI 88823](https://dev.azure.com/ssw/SSW.Induction/_workitems/edit/88823): 🚗 Azure | Create a new App Service Plan in West US for SL production resource group.
I will do the IoC after.

:::
::: good  
Figure: Good Example - PBIs on a new line.
:::

<!-- TODO: Add CodeAuditor box -->
::: info 
This rule is enforced by CodeAuditor. https://codeauditor.com/rules
:::

See the [Markdown Guide](https://www.markdownguide.org/basic-syntax/#line-breaks) for more information on line breaks.


