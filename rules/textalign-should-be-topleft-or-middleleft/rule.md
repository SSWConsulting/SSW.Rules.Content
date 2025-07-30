---
seoDescription: Text alignment should be set to TopLeft or MiddleLeft in forms to allow text boxes to grow horizontally but not vertically.
type: rule
title: Do you know TextAlign should be TopLeft or MiddleLeft?
uri: textalign-should-be-topleft-or-middleleft
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:44:00.000Z
guid: ef0c7b24-336b-4c8a-87ae-7b8ce4b6598f
---

If you add a text box in a form you should add anchoring and/or docking properties to allow it to grow as the form widens, but not as it increases in height.

<!--endintro-->

::: bad
![Figure: Bad example - Wrong settings in the designer](textalign-bad.jpg)
:::

::: bad
![Figure: Bad example - Set Anchor property to Top, Bottom, Left, Right in the designer](textalignresult-bad.jpg)
:::

::: good
![Figure: Good example - Textbox with the wrong anchoring and/or docking properties](textalign-good.jpg)
:::

::: good
![Figure: Good example - Textbox with the correct anchoring and/or docking properties](textalignresult-good.jpg)
:::

We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule
