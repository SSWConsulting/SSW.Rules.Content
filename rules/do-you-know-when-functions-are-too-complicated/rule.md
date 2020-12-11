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

In general you should always be looking to simplify your code (e.g. heavily nested case statements). As a minimum look for the most complicated method you have and check that it needs simplifying.

In Visual Studio, there is inbuilt support for Cyclomatic Complexity analysis.

<!--endintro-->

1. Go to Developer > Code Metrics > Generate for Solution
<dl class="image">&lt;dt&gt;<img src="CodeMetrics.gif" alt="CodeMetrics.gif">&lt;/dt&gt;<dd>Figure: Cyclomatic Complexity analysis tool</dd></dl>
2. Look at the largest Cyclomatic Complexity number and refactor.
<dl class="image">&lt;dt&gt;<img src="CyclomaticAnalysis.gif" alt="CyclomaticAnalysis.gif">&lt;/dt&gt;<dd>Figure: Results from Cyclomatic analysis these metrics give an indication on how complicated functions are</dd></dl>Tip: Maintainability index > 85 is good and < 65 is hard to maintain
