---
type: rule
title: Do you know when functions are too complicated?
uri: know-when-functions-are-too-complicated
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-when-functions-are-too-complicated
created: 2020-03-12T21:53:03.000Z
archivedreason: null
guid: 3198a586-9314-431d-8226-51dce77fac4f
---
![Figure: launching the Code Metrics tool within Visual Studio](calculate_code_metrics.jpg "Screenshot of how to launch the Code Metrics tool within Visual Studio")

You should generally be looking for ways to simplify your code (e.g. removing heavily-nested case statements). As a minimum, look for the most complicated method you have and check whether it needs simplifying.

In Visual Studio, there is built-in support for Cyclomatic Complexity analysis.

<!--endintro-->

1. Go to Analyze | Calculate Code Metrics | For Solution

![Figure: Cyclomatic Complexity analysis tool](calculate_code_metrics.jpg)

2. Look at the largest Cyclomatic Complexity number and refactor.

![Figure: Results from Cyclomatic analysis these metrics give an indication on how complicated functions are](CyclomaticAnalysis.gif)\
Tip: Maintainability index &gt; 85 is good and &lt; 65 is hard to maintain