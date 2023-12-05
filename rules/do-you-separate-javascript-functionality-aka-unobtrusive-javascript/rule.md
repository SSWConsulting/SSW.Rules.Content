---
type: rule
archivedreason: 
title: Do you separate JavaScript functionality (aka Unobtrusive JavaScript)?
guid: f1b16439-54da-4f6f-85a8-c86aff65484e
uri: do-you-separate-javascript-functionality-aka-unobtrusive-javascript
created: 2012-07-24T18:09:29.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-separate-javascript-functionality-(aka-unobtrusive-javascript)

---

A website can be broken down into three main development parts: content, design and functionality. To optimize a website for search engines, it's important to separate the content  (crucial for search engines) from design and functionality (not important for SEO).

<!--endintro-->

All JavaScript code should go into an external .js file (linked to the document with a &lt;script&gt; tag in the head of the page) and not embedded within HTML. The same should be done for CSS files. Don't bloat your HTML file and confuse search engines. Separate the legitimate content from what is programming code.

```html
<a onclick="action()" href="#">Click Here</a>
```

::: bad
Figure: Bad example -  Never include JavaScript as inline attributes
:::

```html
<a href="backuplink.html" class="action">Click Here</a>
```

::: good
Figure: Good example - JavaScript (included in an external file) should use a class or id for its behaviours
:::
