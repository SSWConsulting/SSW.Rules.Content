---
type: rule
archivedreason: This rule has been replaced by [https://www.ssw.com.au/rules/label-buttons-consistently/](/rules/label-buttons-consistently/)
title: Do you label your form buttons consistently?
guid: 9963337e-8c40-491d-a1bb-43912e547d0d
uri: do-you-label-your-form-buttons-consistently
created: 2014-12-01T00:09:41.0000000Z
authors: []
related: []
redirects: []

---

If buttons with similar functionality are named inconsistently across an app, it can cause a confusing experience for users. For example, the buttons used to close a form should be named consistently across your app.

Additionally, buttons should have clear names so the user knows what to expect. For example, it is unclear if a button named "close" will save (or not save) when closing, so "cancel" would be clearer.

<!--endintro-->

::: bad  
![Figure: Bad Example - Unclear labels on the buttons](../../assets/ButtonLabels\_Bad.gif)  
:::

* **Save** button could possibly update the fields but keep the form open.
* **Close** could save the fields, then close the form, when the
       **Cancel** button may be more appropriate.

We recommend the age-old standards of:

* **OK** . Close the form and save any changed data. This should be referenced by the form's AcceptButton property.
* **Cancel** . Close the form without saving. This should be referenced by the form's CancelButton property.
* **Apply** . Save data without closing the form.

::: good  
![Figure: Good Example - This form uses the standard button naming standards (and has the Default buttons set!)](../../assets/OKCancelExampleDialog.jpg)  
:::

We have a program called     [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
