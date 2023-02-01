---
type: rule
archivedreason:
title: Do you know how to lable web-based form buttons consistently?
guid: f365576c-a2cd-4710-8e79-7bd5901d55e5
uri: do-you-label-web-based-form-buttons-consistently
created: 2023-02-01T3:43:00.0000000Z
authors:
- title: Toby Churches
  url: https://github.com/TobyChurches
- title: Piers Sinclair
  url: https://www.ssw.com.au/people/piers-sinclair
related:

---

Consistency is a key factor of software development, designing applications that minimise the learning curve through consistent use of components and functionality. If buttons with similar functionality are named inconsistently across an web application, it can cause a confusing experience for its users. For example, the buttons used to close a form should be named consistently across your app.

Additionally, buttons should have clear names so the user knows what to expect. For example, it is unclear if a button named "close" will save (or not save) when closing, so "cancel" would be clearer.

<!--endintro-->

::: bad  
![Figure: Bad Example - Unclear labels on the buttons](./BadButtonLabels.png)  
:::

* **Save** button alone is not explicit about the following action for the form (It could close or remain open)
* **Close** could save the fields, then close the form, when the **Cancel** button may be more appropriate.


We recommend the web standards of:

* **Save** - Save data without closing the form.
* **Save and Close** - Close the form and save any changed data.
* **Cancel**  - Close the form without saving.



::: good  
![Figure: Good Example - This form uses the standard button naming standards (and has the Default buttons set!)](./GoodFormButtonLabel.png)  
:::

We have a program called     [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
