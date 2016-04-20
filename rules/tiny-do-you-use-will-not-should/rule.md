---
type: rule
title: 'Tiny: Do you use "will", not "should"?'
uri: tiny-do-you-use-will-not-should
created: 2016-04-20T02:23:15.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​When explaining steps in a process, e.g. Printing a file, make sure to say something &quot;will&quot; happen or is happening. This is especially important when describing your own software, because saying something &quot;should&quot; happen implies that it may or may not happen, i.e. there could be bugs!</p> </span>

​To print your document&#58;<br>1.&#160;&#160;&#160; Select&#160;<strong>File | Print</strong>. The Print dialog should now show.<br>2.&#160;&#160;&#160; Select the number of copies and click&#160;<strong>Print</strong>. The file should now print.<dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Using &quot;should&quot; implies uncertainty</dd><br>To print your document&#58;<br>3.&#160;&#160;&#160; Select&#160;<strong>File | Print.</strong> The Print dialog is shown.<br>4.&#160;&#160;&#160; Select the number of copies and click&#160;<strong>Print</strong>. The file will now print.<dd class="ssw15-rteElement-FigureGood">Good example - Using present or future tense implies confidence</dd><br>This is *not* detected by&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor&#160;​</a>because it picks up false positives.​


