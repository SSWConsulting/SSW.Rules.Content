---
type: rule
archivedreason: 
title: Do you avoid using ASP/ASP.NET tags in plain HTML?
guid: a13ede8c-5389-4d69-85d4-bd016addf917
uri: avoid-using-asp-asp-net-tags-in-plain-html
created: 2016-08-05T18:44:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-using-asp-asp-net-tags-in-plain-html

---


<span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;"></span>ASP and ASP.NET tags have no place in plain HTML pages. They simply increase the size of the file and are ignored by browsers, because the need to be processed on the server. When converting ASP.NET pages to plain HTML you must be careful to remove all of these tags.​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​&lt;%@ Page Language=&quot;C#&quot; %&gt;<br>&lt;html&gt;<br>&lt;ssw&#58;inctop id=&quot;inctop&quot; runat=&quot;server&quot;&gt;&lt;/ssw&#58;inctop&gt;</p><dd class="ssw15-rteElement-FigureBad"><span style="font-size&#58;0.9rem;line-height&#58;1.5em;">​​​​​Figure&#58; Bad Example - ASP.NET tags accidentaly placed in a plain HTML documents</span></dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/codeauditor/">SSW Code Auditor​</a>&#160;to check for this rule.</p><p>​<br></p>


