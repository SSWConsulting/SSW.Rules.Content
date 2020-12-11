---
type: rule
archivedreason: 
title: Do you avoid using ASP/ASP.NET tags in plain HTML?
guid: a13ede8c-5389-4d69-85d4-bd016addf917
uri: do-you-avoid-using-aspaspnet-tags-in-plain-html
created: 2016-08-05T18:44:10.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

ASP and ASP.NET tags have no place in plain HTML pages. They simply increase the size of the file and are ignored by browsers, because the need to be processed on the server. When converting ASP.NET pages to plain HTML you must be careful to remove all of these tags.

<!--endintro-->

&lt;%@ Page Language="C#" %&gt;
&lt;html&gt;
&lt;ssw:inctop id="inctop" runat="server"&gt;&lt;/ssw:inctop&gt;


::: bad
Figure: Bad Example - ASP.NET tags accidentaly placed in a plain HTML documents
:::


We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) to check for this rule.
