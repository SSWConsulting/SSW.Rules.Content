---
seoDescription: Optimize form design by anchoring and docking single-line textboxes horizontally only to ensure proper resizing as forms widen.
type: rule
title: Anchoring and Docking - Do you use Anchoring and Docking (horizontal
  only) with single line textboxes?
uri: use-anchoring-and-docking-horizontal-only-with-single-line-textboxes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: 422365e9-ddc8-45a7-8428-cfb712c58c12
---

If you add a text box in a form you should add anchoring and/or docking properties to allow it to grow as the form widens, but not as it increases in height.

<!--endintro-->

::: bad
![Figure: Bad example - Wrong settings in the designer](wrongsettings01.jpg)
:::

::: good
![Figure: Good example - Set Anchor property to Top, Bottom, Left, Right in the designer](setanchorproperty01.jpg)
:::

::: bad
![Figure: Bad example - Textbox with the wrong anchoring and/or docking properties](wronganchoranddock01.jpg)
:::

::: good
![Figure: Good example - Textbox with the correct anchoring and/or docking properties](correctanchoringanddocking01.jpg)
:::
We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule
