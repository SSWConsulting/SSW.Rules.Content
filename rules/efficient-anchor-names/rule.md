---
seoDescription: Choose effective anchor names by considering these key points - Make it meaningful, know they're case sensitive, don't add spacing, and avoid starting with a #.
type: rule
archivedreason: 
title: Do you choose effective anchor names?
guid: d4394c48-e266-4d14-8570-9ffa9f1685ec
uri: efficient-anchor-names
created: 2016-08-05T19:57:36.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - anchor-links
redirects:
  - do-you-chose-efficient-anchor-names
  - chose-efficient-anchor-names
  - choose-efficient-anchor-names
---

It is often that developers find themselves using the incorrect/inefficient anchor names.

<!--endintro-->

According to [W3C](https://www.w3.org/TR/REC-html40/struct/links.html), anchor names must observe the following rules:

* Anchor names **must be unique** within a document
* **Begin with a letter** (A-Z, a-z) and may be followed by any number of letters, digits (0-9), hyphens ("-"), underscores ("_"), colons (":"), and periods (".")
* **Don't add spacings** - When you are defining an anchor name, make sure there are no spaces within the name
* Anchor name **cannot start with `#`**

These are the things you should consider when creating an anchor link:

* **Make it meaningful** - When you are sending the URL by email it helps indicate what you are talking about
* **Avoid list numbers** - They often change. An anchor like `#13` becomes incorrect when the order changes
* **Know they are case sensitive** - `#usergroups` is **not** the same as `#UserGroups`. Always check your links and anchor names are identical, matching the capitalization

```html
<a name="1st section"></a>
```

::: bad
Bad example - Beginning with a number, spaces within, and meaningless anchor name
:::

```html
<a name="get-started"></a>
```

::: good
Good example - Beginning with a letter, no spaces, and a meaningful anchor name
:::
