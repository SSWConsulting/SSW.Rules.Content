---
seoDescription: Master the art of designing multiline textboxes by using anchoring and docking properties to ensure they expand with your form's resize.
type: rule
title: Do you use Anchoring and Docking (full) for multiline textboxes?
uri: use-anchoring-and-docking-if-you-have-a-multiline-textboxes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: 8a009c23-899e-4c20-8dbb-4ddb16df5357
---

If you add a multiline textbox in a form, you should add anchoring and/or docking properties to allow it to expand when the form is resized.

<!--endintro-->

::: bad
![Figure: Bad example - Wrong settings in the designer](wrongsettings.jpg)
:::

::: good
![Figure: Good example - Set Anchor property to Top, Bottom, Left, Right in the designer](setanchorproperty.jpg)
:::

::: bad
![Figure: Bad example - Multiline textbox with the wrong anchoring and/or docking properties](wronganchoranddock.jpg)
:::

::: good
![Figure: Good example - Multiline textbox with the correct anchoring and/or docking properties](correctanchoringanddocking.jpg)
:::

We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule
