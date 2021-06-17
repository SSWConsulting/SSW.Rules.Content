---
type: rule
archivedreason: 
title: Do you remove "Language" from your script tag?
guid: a5f42e3c-b24e-43de-8021-a85e9fed0656
uri: do-you-remove-language-from-your-script-tag
created: 2012-07-24T18:10:04.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-remove-＂language＂-from-your-script-tag

---

Years ago, it was common to have the "language" attribute within the script tags. This attribute was used to specify the scripting language of the contents of this element.

<!--endintro-->

Since these identifiers are not standard, this attribute has been deprecated in favor of "type".

```
<script href="script.js" language="javascript"></script>
```
::: bad
Figure: Bad example - Language attribute has been deprecated
:::

```
<script href="script.js" type="text/javascript"></script>
```
::: good
Figure: Good example - The scripting language is specified as a content type
:::

Read more on [W3C website](https://www.w3.org/TR/html4/interact/scripts.html#h-18.2.2).
