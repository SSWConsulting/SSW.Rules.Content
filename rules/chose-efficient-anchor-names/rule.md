---
type: rule
archivedreason: 
title: Do you chose effective anchor names?
guid: d4394c48-e266-4d14-8570-9ffa9f1685ec
uri: chose-efficient-anchor-names
created: 2016-08-05T19:57:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-chose-efficient-anchor-names

---

These are the things you should consider when creating an anchor link:

<!--endintro-->

1. **Make it meaningful** - When you define anchors names, use meaningful names. When you are sending the URL by email it helps indicate what you are talking about. Avoid list numbers, as they often change. An anchor like "#13" becomes incorrect when the order changes.

2. **Know they are case sensitive** - Are `https://www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx#usergroups` and `https://www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx#UserGroups` the same? The answer is "no" because they might be not case sensitive when they test in some browsers.

3. **Don't add spacing** - When you are defining an anchor name, make sure there are no spaces within the name

``` html
<a name="Some Anchor Name">
```

::: bad
Bad example - Spaces within anchor name
:::

```
<a name="SomeAnchorName">
```

::: good
Good example - No spaces within anchor name
:::

4. **Don't define names starting  with a #** - This is a common mistake because the # is used on the "href"

When you are **defining** an anchor name you **do not** use a hashtag.  
Bear in mind that when you are **referencing** an anchor you **do** use a hashtag.

``` htmk
<a name="#SomeAnchorName">
```

::: bad
Bad example - Hashtag on anchor name
:::

``` html
<a name="SomeAnchorName">
```

::: good
Good example - No hashtag on anchor name
:::

We have a program called [SSW Code Auditor](https://www.ssw.com.au/ssw/codeauditor) to check for #3 and #4 on this rule.
