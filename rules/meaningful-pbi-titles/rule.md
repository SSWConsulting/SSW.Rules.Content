---
type: rule
archivedreason: 
title: Do you use meaningful PBI titles?
guid: 47cff095-9ee2-432f-bac4-4cbbeb2314b5
uri: meaningful-pbi-titles
created: 2022-12-08T07:23:54.0000000Z
authors:
- title: Luke Cook
  url: https://ssw.com.au/people/luke-cook
related:
  - good-email-subject
redirects:
  -do-you-use-meaningful-pbi-titles

---
Product Backlog Items (PBIs) are the cornerstone of a well-oiled project. They track features, bugs, tasks, and much more. When a developer or Product Owner is looking through the backlog, it's important that - at a glance -  they can read the titles of PBIs and have a decent understanding of them.

So what separates a good PBI title from a bad one?

<!--endintro-->

```
Fix menu bug
```
::: bad
Figure: Bad Example – what bug? How important is this?
:::

Without a meaningful title, you need to drill down into the details. If your backlog is substantial, it quickly becomes time-consuming and tedious to drill into each and every item to see what it's about. Even worse - next time you visit the backlog, chances are you won't remember the details and will have to re-read every PBI again!

```
🔥🐛 BUG | Menu disappears on mobile devices
```
::: good
Figure: Good Example - Fire emoji to bring attention to the PBI's importance, bug emoji to indicate the PBI type, and a clear description of the bug
:::

Emojis - love them or hate them - have become a staple in the development world. As the old saying goes; a picture is worth a thousand words. You can use emojis (responsibly!) to categorize PBIs, as well as bring attention to important items in a way that is easily interpreted by other people.

Regardless of whether or not you choose to adopt the emoji language, you should always be mindful of the title's text. Always ask yourself: can a developer (or Product Owner) interpret the task and its importance without needing to dive into the details?

### Don't

- ❌ Write a novel in the title
- ❌ Be generic (e.g. "Fix bug in site")
- ❌ Ignore the importance of urgent PBIs


### Do

- ✅ Identify its urgency (e.g. 🔥)
- ✅ Identify the bugs (e.g. "Bug" and/or 🐛)
Bugs are special case - they should have [greater visibiliy](https://www.ssw.com.au/rules/management-do-you-fix-bugs-first)
- ✅ Use emojis (see our rule on [emojis in scrum](https://www.ssw.com.au/rules/which-emojis-to-use-in-scrum))
- ✅ Prefix the area/form
- ✅ Be specific (e.g. "[Area] | [behaviour]". See our rule to [order of instructions](https://www.ssw.com.au/rules/use-the-right-order-of-instructions))


### Good PBI title examples

- Bugs:

  ::: greybox
  🐛 Newsletter form | returns HTTP 500
  :::

- Features:

  ::: greybox
  ✨ Newsletter form | Validate email address
  :::

- UI/Styling:

  ::: greybox
  💄 Header | Update site header with new logo
  :::

- DevOps/Infra:

  ::: greybox
  👷‍♂️ DevOps | Add ephemeral deployment slots for PRs
  :::

- Urgent tasks:

  ::: greybox
  🔥🐛👷‍♂️ SysAdmin | Northwind app inaccessible through company VPN
  :::

### What about email subjects?

Email subjects need some additional context because you don't have the context of the backlog.

So, add the project as a prefix to email subjects. Here is what those would look like:

#### PBIs 

{{ EMOJI FOR PBI TYPE }} - {{ BUSINESS AREA TOUCHED }} - {{ SHORT DESCRIPTION }}
e.g.
🐛 Invoices - Invoice totals are rounded incorrectly
⚒️ Infrastructure - Implement staging deployment pipeline
✨ Clients - Add create/edit client page 

#### Emails 

{{ PROJECT TOUCHED }} - {{ EMOJI FOR PBI TYPE }} - {{ BUSINESS AREA TOUCHED }} - {{ SHORT DESCRIPTION }}
e.g.
🐛 SSW TimePro - Invoices - Invoice totals are rounded incorrectly
⚒️ SSW Website - Infrastructure - Implement staging deployment pipeline
✨ Northwind - Clients - Add create/edit client page 
