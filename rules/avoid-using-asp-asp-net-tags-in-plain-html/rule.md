---
type: rule
title: Do you avoid using ASP/ASP.NET tags in plain HTML?
uri: avoid-using-asp-asp-net-tags-in-plain-html
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-avoid-using-asp-asp-net-tags-in-plain-html
created: 2016-08-05T18:44:10.000Z
archivedreason: null
guid: a13ede8c-5389-4d69-85d4-bd016addf917
---

ASP and ASP.NET tags have no place in plain HTML pages. They simply increase the size of the file and are ignored by browsers, because the need to be processed on the server. When converting ASP.NET pages to plain HTML you must be careful to remove all of these tags.

<!--endintro-->

```cs
<%@ Page Language="C#" %>
<html>
<ssw:inctop id="inctop" runat="server"></ssw:inctop>
```

::: bad
Figure: Bad example - ASP.NET tags accidentaly placed in a plain HTML documents
:::

We have a program called [SSW Code Auditor](https://codeauditor.com) to check for this rule.
