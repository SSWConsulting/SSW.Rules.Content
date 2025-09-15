---
seoDescription: Use meaningful PBI titles to effectively communicate requirements and facilitate prioritization. (Note - The original text is quite long, so I've condensed it into a shorter summary that still captures the main points.)
type: rule
title: Do you use meaningful PBI titles?
uri: pbi-titles
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
related:
  - zooming-in-and-out
  - catering-to-audience
  - defining-pbis
created: 2023-01-25T08:47:53.492Z
guid: b4b9e315-5c7f-413c-9456-e53a23cbbdac
archivedreason: duplicate of https://ssw.com.au/rules/meaningful-pbi-titles
---

PBI titles are the fastest way to get information about an issue. Unfortunately, backlogs are often filled with poorly named PBIs, making it hard for the key stakeholders to sift through.

A well-thought-out PBI title can be the difference between an excellent Sprint Planning and a poor one.

<!--endintro-->

Many factors go into a good PBI title. Some of the core aspects are:

* Audience interpretation
* Importance
* Business area
* Type of PBI
* Number of words

### Audience Interpretation

People interpret things in different ways. Those interested in PBIs generally include:

* Developers
* Product Owners
* External Stakeholders

Consider the background of all interested and change the title accordingly. For example, a Product Owner might not know what "dependency" means, so it might be better to avoid including that in a PBI title.

Usually, sticking to the business value is a good rule of thumb.

::: grey
Fix broken dependency
:::
::: bad
**Figure: Bad Example - Many Product Owners would have no idea what this means**
:::

::: grey
IDateTimeProvider - New 3rd party code breaks app
:::
::: good
**Figure: Good Example - The Product Owner can see that there is new code that has broken the app**
:::

### Importance

Indicating the relative priority of a PBI helps stakeholders prioritise it at a glance.

Adding a fire emoji to critical PBIs helps communicate that it should be actioned ASAP.

::: grey
CI/CD - Deployment pipeline broken
:::
::: bad
**Figure: Bad Example - The Product Owner might not realise this is a crucial PBI**
:::

::: grey
CI/CD - Deployment pipeline broken 🔥
:::
::: good
**Figure: Good Example - The Product Owner won't miss this PBI with the help of an emoji**
:::

### Prefixes

Prefixes help the team understand the area a PBI is touching. For example, prefixing with the business area helps give a zoomed-out view of which part of the app is being touched. Then it becomes easier to understand the zoomed-in details.

::: grey
Add new profile picture
:::
::: bad
**Figure: Bad Example - It isn't clear where the profile picture is going**
:::

::: grey
Company Contacts - Add new profile picture
:::
::: good
**Figure: Good Example - It's immediately clear that company contacts will get a profile picture**
:::

### Type of PBI

Knowing what kind of PBI it is can help with prioritisation. If the Product Owner knows it's a bug, they will likely want it actioned ASAP!

Adding an emoji at the start of the PBI communicates the type at a glance.

::: grey
Company Details - Cannot save changes
:::
::: bad
**Figure: Bad Example - The Product Owner needs to read and process the whole title to realise it is a bug**
:::

::: grey
Company Contacts - Add new profile picture
:::
::: good
**Figure: Good Example - Straightaway, the Product Owner can see from the emoji that it is a bug**
:::

### Number of words

Sometimes less is more. Try to limit the number of words included and make those words as high-impact as possible.

::: grey
Company Details - Add a new feature with the functionality to set a description in order to improve user comprehension
:::
::: bad
**Figure: Bad Example - The description is needlessly wordy**
:::

::: grey
Company Details - Add a description to improve user comprehension
:::
::: good
**Figure: Good Example - The description is half as long but communicates the same info**
:::
