---
type: rule
title: Do you avoid hardcoding URLs (“../”, “~/”, or “/”) and use Url.Action or
  Html.ActionLink instead?
uri: do-you-avoid-hardcoding-urls-or-and-use-url-action-or-html-actionlink-instead
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects:
  - do-you-avoid-hardcoding-urls-(-or-)-and-use-url-action-or-html-actionlink-instead
created: 2013-03-07T18:51:39.000Z
archivedreason: null
guid: 582c7a84-24ff-40ca-b1ff-332ec3a191a2
---
Hard-coding URLs in your View can cause problems if your routes or page names need to change. Instead, you should always use the Url and Html helpers to refer to different pages in your MVC application.

<!--endintro-->

```html
<a href="/Rule/Create">Create a Rule</a>
```
::: bad
Figure: Bad example – Hard-coded URLs may lead to broken links if routes change
:::

```cs
@Html.ActionLink("Create a Rule", "Create", "Rule")
```
::: good
Figure: Good example – Use the Url or Html helpers to provide links
:::
