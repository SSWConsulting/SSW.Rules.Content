---
type: rule
title: Do you always put JavaScript in a separate file?
uri: do-you-always-put-javascript-in-a-separate-file
created: 2016-09-01T18:32:24.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ASP.NET injects many lines during page rendering, so if you are using inline JavaScript, the line numbers will change during client side JavaScript debugging in VS.NET, FireBug or IE8 developer Tools.<br>​​​<br> </span>

<dl class="badImage"><dt><img src="/PublishingImages/JavaScriptBad1.jpg" alt="JavaScriptBad1.jpg" /></dt><dd>Figure&#58; Bad Code - Using Inline JavaScript</dd></dl><dl class="badImage"><dt><img src="/PublishingImages/JavaScriptBad.jpg" alt="JavaScriptBad.jpg" /></dt><dd>Figure&#58; Bad Code - On PostBack Line numbers are changed for Inline JavaScript</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/JavaScriptGood.jpg" alt="JavaScriptGood.jpg" /></dt><dd>Figure&#58; Good Code - Using JavaScript on Separate file ​<br></dd></dl><p>So you should always put JavaScript in a separate file.&#160; Then the line numbers will stay consistent during debugging.&#160;<br>Keeping JavaScript in a&#160;separate file is also good for production as it improves performance due to browser caching.&#160;<br><br><b>Note&#58; </b>During development, remember to hit CTRL-F5 to force the browser to re-fetch the files from the server or you may be debugging old version of the JavaScript file.</p>


