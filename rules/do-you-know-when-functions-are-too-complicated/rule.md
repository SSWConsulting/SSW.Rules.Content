---
type: rule
archivedreason: 
title: Do you know when functions are too complicated?
guid: 3198a586-9314-431d-8226-51dce77fac4f
uri: do-you-know-when-functions-are-too-complicated
created: 2020-03-12T21:53:03.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- know-when-functions-are-too-complicated

---

In general you should always be looking to simplify your code (e.g. heavily nested case statements). As a minimum look for the most complicated method you have and check that it needs simplifying.

In Visual Studio, there is inbuilt support for Cyclomatic Complexity analysis.

<!--endintro-->

1. Go to Developer &gt; Code Metrics &gt; Generate for Solution


::: ok  
![Figure: Cyclomatic Complexity analysis tool](CodeMetrics.gif)  
:::

2. Look at the largest Cyclomatic Complexity number and refactor.


::: ok  
![Figure: Results from Cyclomatic analysis these metrics give an indication on how complicated functions are](CyclomaticAnalysis.gif)  
:::
Tip: Maintainability index &gt; 85 is good and &lt; 65 is hard to maintain
