---
type: rule
title: Do you know you should not open popup windows and use a javascript modal instead?
uri: do-you-know-you-should-not-open-popup-windows-and-use-a-javascript-modal-instead
created: 2016-11-17T16:15:13.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">The popup blockers in several browsers prevent JavaScript from being used to open windows without user interaction (e.g. clicking a link). You should use an anchor tag instead.<br></p> </span>

<p class="ssw15-rteElement-CodeArea">​&lt;body onload=&quot;window.open('http&#58;//www.mydomain.com/document.html');return true;&quot;&gt; 
   <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - using JavaScrip in OnLoad event​<br></dd><p class="ssw15-rteElement-CodeArea">​&lt;a href=&quot;http&#58;//www.mydomain.com/document.html&quot; target=&quot;_new&quot;&gt;Document&lt;/a&gt; </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using HTML anchor tag. This will open in a new tab or window depending upon browser configuration​​<br></dd>
<p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;#&quot; onclick=&quot;window.open('http&#58;//www.mydomain.com/document.html');return false;&quot;&gt;Document&lt;/a&gt; </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using Javascript in an onclick event means you can force a popup window in preference to a new tab and also control the size and placement of the window</dd><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/" target="_blank">SSW Code Auditor</a>&#160;to check for this rule.<br></p><p>​<br></p>


