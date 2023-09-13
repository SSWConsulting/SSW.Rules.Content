---
type: rule
title: Do you use meaningful PBI titles?
uri: meaningful-pbi-titles
authors:
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
related:
  - good-email-subject
redirects:
  - do-you-use-meaningful-pbi-titles
created: 2022-12-08T07:23:54.000Z
archivedreason: null
guid: 47cff095-9ee2-432f-bac4-4cbbeb2314b5
---

Product Backlog Items (PBIs) are the cornerstone of a well-oiled project. They track features, bugs, tasks, and much more. When a developer or Product Owner is looking through the backlog, it's important that - at a glance - they can read the titles of PBIs and have a decent understanding of them.

So what separates a **good** PBI title from a **bad** one?

<!--endintro-->

`youtube: https://www.youtube.com/embed/Wob4UgGmqdU`
**Video: Do you use meaningful PBI titles? | [Luke Cook](https://ssw.com.au/people/luke-cook/) | SSW Rules (5 min)**

::: info
**Note:** Usually, we use the term PBI to encompass all types of backlog items, including those related to DevOps, Trello, GitHub, or any other platform.
:::

## How to create meaningful, yet efficient titles?

Without a meaningful title, you need to drill down into the details. If your backlog is substantial, it quickly becomes time-consuming and tedious to drill into each and every item to see what it's about. Even worse... next time you visit the backlog, chances are you won't remember the details and will have to re-read every PBI again!

::: greybox
Fix menu bug
:::
::: bad
Figure: Bad example – What bug? How important is this?
:::

::: greybox
🔥 🐛 BUG | Menu disappears on mobile devices
:::

::: good
Figure: Good example - "Fire" emoji to bring attention to the PBI's importance, "Bug" emoji to indicate the PBI type, and a clear description of the issue
:::

### Don't

❌ Be generic (e.g. "Fix bug in site")  
❌ Write a novel in the title  
❌ Ignore the importance of urgent PBIs

### Do

✅ Be specific (e.g. "{{Area}} | {{behaviour}}"). See our rule to [order of instructions](/use-the-right-order-of-instructions)   
✅ Prefix the area/form  
✅ Identify its urgency (e.g. 🔥)  
✅ Identify the bugs (e.g. "Bug" and/or 🐛). Bugs are special case - they should have [greater visibiliy](/management-do-you-fix-bugs-first)  
✅ Use emojis. See our rule on [emojis in Scrum](/which-emojis-to-use-in-scrum)


### Good PBI titles examples

Using this structure: **{{ EMOJI FOR PBI TYPE }} {{ BUSINESS AREA TOUCHED }} | {{ SHORT DESCRIPTION }}**

Bugs:

::: greybox
🐛 Newsletter form | returns HTTP 500
:::

Features:

::: greybox
✨ Newsletter form | Validate email address
:::

UI/Styling:

::: greybox
💄 Header | Update site header with new logo
:::

DevOps/Infra:

::: greybox
👷‍♂️ DevOps | Add ephemeral deployment slots for PRs
:::

Urgent tasks:

::: greybox
🔥🐛👷‍♂️ SysAdmin | Northwind app inaccessible through company VPN
:::
  
Other examples:

::: greybox
🐛 Invoices | Invoice totals are rounded incorrectly  
  
⚒️ Infrastructure | Implement staging deployment pipeline 

✨ Clients page | Add create/edit client fields 
:::

Great titles are also important on [Pull Requests](/write-a-good-pull-request/#1-write-a-concise-and-self-explanatory-title), and [email subjects](/good-email-subject).

::: info
**Emojis** 

Love them or hate them, emojis have become a staple in the development world. As the old saying goes... _"a picture is worth a thousand words"_. You can use emojis (responsibly!) to categorize PBIs/Issues/PRs/Emails, as well as bring attention to important items in a way that is easily interpreted by other people.

Regardless of whether or not you choose to adopt the emoji language, you should always be mindful of the title's text. 

Always ask yourself: _"Can a developer (or Product Owner) interpret the task and its importance without needing to dive into the details?"_
:::
