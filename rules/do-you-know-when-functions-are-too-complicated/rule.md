---
type: rule
title: Do you know when functions are too complicated?
uri: do-you-know-when-functions-are-too-complicated
created: 2020-03-12T21:53:03.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​In general you should always be looking to simplify your code (e.g. heavily nested case statements). As a minimum look for the most complicated method you have and check that it needs simplifying.​​<br></p><p class="ssw15-rteElement-P">In Visual Studio, there is inbuilt support for Cyclomatic Complexity analysis.​​​<br></p> </span>

<p>​1. Go to Developer &gt; Code Metrics &gt; Generate for Solution</p><dl class="image"><dt><img src="./CodeMetrics.gif" alt="CodeMetrics.gif" /></dt><dd>Figure&#58; Cyclomatic Complexity analysis tool</dd></dl><p>2. Look at the largest Cyclomatic Complexity number and refactor.</p><dl class="image"><dt><img src="./CyclomaticAnalysis.gif" alt="CyclomaticAnalysis.gif" /></dt><dd>Figure&#58; Results from Cyclomatic analysis these metrics give an indication on how complicated functions are</dd></dl>​Tip&#58; Maintainability index &gt; 85 is good and &lt; 65&#160;is hard to maintain<br>


