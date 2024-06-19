---
seoDescription: Use correct symbols when documenting instructions to avoid user confusion and improve understanding by clearly listing steps in the correct order.
type: rule
title: Reference - Do you use the correct symbols when documenting instructions?
uri: use-correct-symbols-when-documenting-instructions
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-highlight-actions-correctly-in-your-document
  - do-you-make-numbers-more-readable
  - awesome-documentation
redirects:
  - reference-do-you-use-the-correct-symbols-when-documenting-instructions
created: 2016-03-22T04:45:05.000Z
archivedreason: null
guid: ff9b08bd-f85d-41c8-883a-9d226b3b9fc5
---

An important area to apply strict standards to is documenting instructions. The way in which instructions are worded and arranged is very important in helping the user understand the instructions. Therefore, the instructions should be minimalistic, clear and concise.

We often see documentation like: _'...then you click on Select All Programs from the Start menu'_. This is bad! You should keep it simple and **always** list the items in the order the user selects them.

Be sure you keep the operations clearly in the right order:

<!--endintro-->

::: greybox
...then you click on All Apps from the Start menu
:::
::: bad
Figure: Bad example - Wrong order and too many words  
:::

::: greybox
Click Start, then All Apps, then Accessories, then Calculator.  
:::
::: bad
Figure: Bad example - No visual cue is given for separate steps  
:::

::: greybox
Start - All Apps - Accessories - Calculator  
:::
::: bad
Figure: Bad example - Dashes are easy to glance over  
:::

::: greybox
Start --&gt; All Apps --&gt; Accessories --&gt; Calculator  
:::
::: bad
Figure: Bad example - This is better but may be interpreted incorrectly
:::

::: greybox
Start | All Apps | Accessories | Calculator  
:::
::: good
Figure: Good example - Makes it easy to follow
:::

If you follow this rule, users won't be confused.
