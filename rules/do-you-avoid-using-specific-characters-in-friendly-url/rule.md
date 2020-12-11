---
type: rule
archivedreason: 
title: Do you avoid using specific characters in friendly URL?
guid: c03c757d-86dc-4f31-9aa3-f1c6670c7d63
uri: do-you-avoid-using-specific-characters-in-friendly-url
created: 2017-04-26T20:15:26.0000000Z
authors:
- id: 9
  title: William Yin
related: []

---

When adding a friendly URL, please avoid using specific characters like “+, :, #, &, (, ), !, \*, [, ], {, }, @, /, =, $” and so on due to multiple reasons:

<!--endintro-->

1. When adding a friendly URL, we meant to make it “ **friendly** " and “ **easy** " for the user to read and remember, so avoid using specific characters and try to make it short.
2. Some characters are unsafe characters, they will be encoded, which end up making the URL really messy and ugly, e.g <br>       **double quote** (“) will be encoded to <br>       **%22** .


Some characters are reserved characters, which may not be supported by some features, based on our experience, “+" is not supported in “canonical" to redirect from      **http**  to      **https** .
<dl class="image">&lt;dt&gt;<img src="sharepoint-characters-not-allowed.jpg" alt="sharepoint-characters-not-allowed.jpg">&lt;/dt&gt;</dl>
In the above source code, the URL     [http://rules.ssw.com.au:80/do-you-know-when-to-use-+1](/do-you-know-when-to-use-+1)*[note: don't include as a hyperlink as it's a broken URL]* will throw a 404 error rather than redirecting to      **https://rules.ssw.com.au:80/do-you-know-when-to-use-+1** ,but it works fine if the URL doesn't include “+", e.g.     [https://rules.ssw.com.au/do-you-know-when-to-use-plus-one](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=d1f2a285-1ca6-45d6-8142-30bccb09c528).
