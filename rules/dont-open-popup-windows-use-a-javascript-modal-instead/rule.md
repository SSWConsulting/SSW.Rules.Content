---
type: rule
archivedreason: 
title: Do you know you should not open popup windows and use a javascript modal instead?
guid: e240b831-4ab1-49e3-b6b6-22218f6ca97b
uri: dont-open-popup-windows-use-a-javascript-modal-instead
created: 2016-11-17T16:15:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-you-should-not-open-popup-windows-and-use-a-javascript-modal-instead

---

The popup blockers in several browsers prevent JavaScript from being used to open windows without user interaction (e.g. clicking a link). You should use an anchor tag instead.

<!--endintro-->

```html
<body onload="window.open('http://www.mydomain.com/document.html');return true;">
```

::: bad
Figure: Bad example - Using JavaScrip in OnLoad event
:::

```html
<a href="http://www.mydomain.com/document.html" target="_new">Document</a>
```

::: good
Figure: Good example - Using HTML anchor tag. This will open in a new tab or window depending upon browser configuration
:::


```html
<a href="#" onclick="window.open('http://www.mydomain.com/document.html');return false;">Document</a>
```

::: good
Figure: Good example - Using Javascript in an onclick event means you can force a popup window in preference to a new tab and also control the size and placement of the window  
:::

We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
