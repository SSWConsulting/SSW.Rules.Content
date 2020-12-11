---
type: rule
archivedreason: 
title: Do you know you should not open popup windows and use a javascript modal instead?
guid: e240b831-4ab1-49e3-b6b6-22218f6ca97b
uri: do-you-know-you-should-not-open-popup-windows-and-use-a-javascript-modal-instead
created: 2016-11-17T16:15:13.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The popup blockers in several browsers prevent JavaScript from being used to open windows without user interaction (e.g. clicking a link). You should use an anchor tag instead.

<!--endintro-->

&lt;body onload="window.open('http://www.mydomain.com/document.html');return true;"&gt;


::: bad
Figure: Bad Example - using JavaScrip in OnLoad event

:::


&lt;a href="http://www.mydomain.com/document.html" target="\_new"&gt;Document&lt;/a&gt;


::: good
Figure: Good Example - Using HTML anchor tag. This will open in a new tab or window depending upon browser configuration

:::


&lt;a href="#" onclick="window.open('http://www.mydomain.com/document.html');return false;"&gt;Document&lt;/a&gt;


::: good
Figure: Good Example - Using Javascript in an onclick event means you can force a popup window in preference to a new tab and also control the size and placement of the window
:::


We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
