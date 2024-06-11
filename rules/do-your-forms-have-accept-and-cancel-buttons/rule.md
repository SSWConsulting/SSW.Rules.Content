---
seoDescription: Ensure your forms have both Accept and Cancel buttons to provide users with control using "Enter" and "Esc".
type: rule
title: Do your forms have Accept and Cancel buttons?
uri: do-your-forms-have-accept-and-cancel-buttons
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T06:52:00.000Z
guid: 71e8c6f0-fcb0-42cb-b536-e25a202d224b
---

If you have a button in a form you must have an accept or a cancel button. As a result user can use "Enter" and "Esc" to control the form.

<!--endintro-->

::: good
![Figure: Good example - Next button is set as the accept button](acceptbuttonexample_good.jpg)
:::

We have a program called [SSW CodeAuditor](https://ssw.com.au/ssw/CodeAuditor/Rules.aspx#ANCBTN) to check for this rule.

**Note:** The CodeAuditor Rule will just test the buttons on the Base form and ignore all the inherit forms, because for more reusable code, the Accept and Cancel buttons should be in the base form.
