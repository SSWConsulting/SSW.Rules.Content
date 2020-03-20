

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​In general you should always be looking to simplify your code (e.g. heavily nested case statements). As a minimum look for the most complicated method you have and check that it needs simplifying.​​<br></p><p class="ssw15-rteElement-P">In Visual Studio, there is inbuilt support for Cyclomatic Complexity analysis.​​​<br></p> </span>

<p>​1. Go to Developer &gt; Code Metrics &gt; Generate for Solution</p><dl class="image"><dt><img src="/PublishingImages/CodeMetrics.gif" alt="CodeMetrics.gif" /></dt><dd>Figure&#58; Cyclomatic Complexity analysis tool</dd></dl><p>2. Look at the largest Cyclomatic Complexity number and refactor.</p><dl class="image"><dt><img src="/PublishingImages/CyclomaticAnalysis.gif" alt="CyclomaticAnalysis.gif" /></dt><dd>Figure&#58; Results from Cyclomatic analysis these metrics give an indication on how complicated functions are</dd></dl>​<br>


