---
type: rule
archivedreason: 
title: Do you chose efficient anchor names?
guid: d4394c48-e266-4d14-8570-9ffa9f1685ec
uri: do-you-chose-efficient-anchor-names
created: 2016-08-05T19:57:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- chose-efficient-anchor-names

---

These are the things you should consider when creating an anchor link:

<!--endintro-->

1. **Meaningful** - When you use named anchors in a web page, use meaningful names. When you are sending the URL by email it helps indicate what you are talking about, and in addition, list numbers often change. An anchor like "#13" becomes incorrect when the order changes.
2. **Case sensitive** - Are "http://www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx#usergroups" and "http://www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx#UserGroups" the same? The answer is "no" because they might be not case sensitive when they test in some browsers.
3. **No spacing** - When you are defining an anchor name, make sure there are no spaces within the name. 

::: bad
Bad: &lt;a name="Some Anchor Name"&gt; 

:::

::: good
Good: &lt;a name="SomeAnchorName"&gt; 

:::

4. **Don't start with a #** - When you are defining an anchor name you DO NOT use a #.
When you are referencing an anchor you DO use a #.
This is a common mistake because the # is used on the "href".

::: bad
Bad: &lt;a name="#SomeAnchorName"&gt; 

:::

::: good
Good: &lt;a name="SomeAnchorName"&gt; 

:::


We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) to check for #3 and #4 on this rule.
