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

When adding a friendly URL, please avoid using specific characters like “+, :, #, &, (, ), !, \*, [, ], {, }, @, /, =, $” and so on due to multiple reasons:

<!--endintro-->

1. When adding a friendly URL, we meant to make it “ **friendly** " and “ **easy** " for the user to read and remember, so avoid using specific characters and try to make it short.

2. Some characters are unsafe characters, they will be encoded, which end up making the URL really messy and ugly, e.g 
::: greybox
**double quote** (“) will be encoded to **%22**.
:::

SharePoint - Some characters are reserved characters, which may not be supported by some features, based on our experience, “+" is not supported in “canonical" to redirect from **http** to **https**.

![Figure: Not allowed characterst in SharePoint](sharepoint-characters-not-allowed.jpg)  

In the above source code, the URL **rules.ssw.com&#46;au/do-you-know-when-to-use-+1** will throw a 404 error rather than redirecting to      **rules.ssw.com&#46;au/do-you-know-when-to-use-+1**.

It works fine if the URL doesn't include “+", like: **rules&#46;ssw.com&#46;au/do-you-know-when-to-use-plus-one**.
