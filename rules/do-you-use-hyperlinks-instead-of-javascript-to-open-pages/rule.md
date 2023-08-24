---
type: rule
archivedreason: 
title: Do you use Hyperlinks instead of JavaScript to open pages?
guid: b075ee50-fa00-4974-a0cb-71d2b157886f
uri: do-you-use-hyperlinks-instead-of-javascript-to-open-pages
created: 2013-07-28T03:04:16.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related:
- do-you-use-bundling-and-or-amd
- do-you-treat-javascript-like-a-real-language
- do-you-know-which-version-of-jquery-to-use
redirects: []

---

If possible you should always use hyperlinks to open new pages on your site instead of using JavaScript.

<!--endintro-->

There are two good reasons for avoiding JavaScript-powered links:

1. Copying and pasting sections of the site to an email or a document will maintain the clickable links
2. There's an (ever-decreasing) chance a user won't have JavaScript enabled and won't be able to click the link

```html
<div onclick="window.open('mynewpage.html');">Open a new page</div>
```

::: bad
Figure: Bad Example - This link can't be clicked on if you paste it into an email or if JavaScript is off  
:::

```html
<a href="mynewpage.html">Open a new page</a>
```

::: good
Figure: Good Example - This link can still be clicked on when pasted and when JavaScript is turned off  
:::
