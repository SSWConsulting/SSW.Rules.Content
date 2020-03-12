---
type: rule
archivedreason: 
title: Do you know when functions are too complicated?
guid: 3198a586-9314-431d-8226-51dce77fac4f
uri: do-you-know-when-functions-are-too-complicated
created: 2020-03-12T21:53:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P">In general you should always be looking to simplify your code (e.g. heavily nested case statements). As a minimum look for the most complicated method you have and check that it needs simplifying.​​<br></p><p class="ssw15-rteElement-P">In VS 2008, there is inbuilt support for Cyclomatic Complexity analysis.​​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​1. Go to Developer &gt; Code Metrics &gt; Generate for Solution</p><dl class="image"><dt><img src="/PublishingImages/CodeMetrics.gif" alt="CodeMetrics.gif" /></dt><dd>Figure&#58; Cyclomatic Complexity analysis tool</dd></dl><p>2. Look at the largest Cyclomatic Complexity number and refactor.</p><dl class="image"><dt><img src="/PublishingImages/CyclomaticAnalysis.gif" alt="CyclomaticAnalysis.gif" /></dt><dd>Figure&#58; Results from Cyclomatic analysis these metrics give an indication on how complicated functions are</dd></dl>​<br>


