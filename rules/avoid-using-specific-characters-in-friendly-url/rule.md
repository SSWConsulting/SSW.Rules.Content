---
type: rule
archivedreason: 
title: Do you avoid using specific characters in friendly URL?
guid: c03c757d-86dc-4f31-9aa3-f1c6670c7d63
uri: avoid-using-specific-characters-in-friendly-url
created: 2017-04-26T20:15:26.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-avoid-using-specific-characters-in-friendly-url

---

When adding a friendly URL, please avoid using specific characters like `+ : # & , ) ( ! \ } {  @ / = $` (and so on) due to these reasons:

<!--endintro-->

1. When adding a friendly URL, we meant to make it **friendly** and **easy** for the user to read and remember, and these characters add complexity

2. Some characters are unsafe characters, they will be encoded, which end up making the URL really messy and ugly. Example: **double quote (“)** will be encoded as **%22**.

### SharePoint

Some characters are reserved characters, which may not be supported by some features, based on our experience, “+" is not supported in “canonical" to redirect from **http** to **https**.

::: greybox
`http://ssw.com.au/rules/when-to-use-+1`
:::
::: bad
Figure: Bad example -  This URL will throw a 404 error rather than redirecting to https://
:::

::: greybox
`http://ssw.com.au/rules/when-to-use-plus-1`
:::
::: good
Figure: Good example - Redirect works fine if the URL doesn't include “+"
:::
