---
type: rule
archivedreason: 
title: Reference - Do you use the correct symbols when documenting instructions?
guid: ff9b08bd-f85d-41c8-883a-9d226b3b9fc5
uri: use-correct-symbols-when-documenting-instructions
created: 2016-03-22T04:45:05.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-highlight-actions-correctly-in-your-document
- do-you-make-numbers-more-readable
- awesome-documentation
redirects:
- reference-do-you-use-the-correct-symbols-when-documenting-instructions

---

An important area to apply strict standards to is documenting instructions. The way in which instructions are worded and arranged is very important in helping the user understand the instructions. Therefore, the instructions should be minimalistic, clear and concise.

We often see documentation like: _'...then you click on Select All Programs from the Start menu'_. This is bad! You should keep it simple and **always** list the items in the order the user selects them.

Be sure you keep the operations clearly in the right order:

<!--endintro-->


::: greybox
...then you click on Select All Programs from the Start menu
:::
::: bad
Figure: Bad example - Wrong order and too much words  
:::

::: greybox
Click Start, then All Programs, then Accessories, then Calculator.  
:::
::: bad
Figure: Bad example - No visual cue is given for separate steps  
:::

::: greybox
Start - All Programs - Accessories - Calculator  
:::
::: bad
Figure: Bad example - Dashes are easy to glance over  
:::

::: greybox
Start --&gt; All Programs --&gt; Accessories --&gt; Calculator  
:::
::: bad
Figure: Bad example - This is better but may be interpreted wrongly 
:::

::: greybox
Start | All Programs | Accessories | Calculator  
:::
::: good
Figure: Good example - Makes it easy to follow
:::

If you follow this rule, users won't be confused.
