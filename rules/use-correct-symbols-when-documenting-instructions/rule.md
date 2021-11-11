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
- reference-do-you-use-the-right-order-of-instructions
- do-you-highlight-actions-correctly-in-your-document
- do-you-make-numbers-more-readable
- awesome-documentation
redirects:
- reference-do-you-use-the-correct-symbols-when-documenting-instructions

---

An important area which Microsoft does not apply strict standards to, is documenting instructions. This is often a confusing dilemma for many people, as the way in which instructions are worded and arranged is very important in helping the user understand the instructions. Therefore, the instructions should be minimalistic, clear and concise.

<!--endintro-->

In Ken Getz's words, you MUST ALWAYS list the items in the order the user selects them. We often see on Microsoft documentation: 'Select All Programs from the Start menu'. That's bad!

::: greybox
Click Start, then All Programs, then Accessories, then Calculator.  
:::
::: bad
Figure: Bad Example - No visual cue is given for separate steps  
:::

::: greybox
Start - All Programs - Accessories - Calculator  
:::
::: bad
Figure: Bad Example - Dashes are easy to glance over  
:::

::: greybox
Start --&gt; All Programs --&gt; Accessories --&gt; Calculator  
:::
::: bad
Figure: Bad Example - This is better but looks unprofessional  
:::

::: greybox
Start | All Programs | Accessories | Calculator  
:::
::: good
Figure: Good Example - Makes it easy to follow
:::
