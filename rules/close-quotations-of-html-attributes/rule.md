---
type: rule
title: Do you close quotations of all your HTML attributes?
uri: close-quotations-of-html-attributes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-remember-to-close-quotations-of-all-your-html-attributes
created: 2016-08-12T20:46:20.000Z
archivedreason: null
guid: f3618de2-2941-4967-a5ca-4a3cfa213330
---

Make sure there are equivalent closing quotations for HTML attributes. A small mistake of missing a quotation could lead to undesired results on a web page.

<!--endintro-->

```html
<span style="font-size:12pt; background: #ccc;>
```
::: bad
Figure: Bad code - Can you spot the missing quote? Code Auditor can
:::

```html
<span style="font-size:12pt; background: #ccc;">
```
::: good
Figure: All OK
:::

As you can see from the above example, just missing a quotation makes the whole layout of the text different. So be very careful that you make sure you have closed all opening quotations of attributes with equivalent closing quotations.

We have a program called [SSW Code Auditor](https://codeauditor.com) to check for this rule.
