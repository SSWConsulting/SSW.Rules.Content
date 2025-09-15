---
seoDescription: Learn when to refactor functions and simplify code using Visual Studio's built-in Code Metrics tool and Cyclomatic Complexity analysis.
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

You should generally be looking for ways to simplify your code (e.g. removing heavily-nested case statements). As a minimum, look for the most complicated method you have and check whether it needs simplifying.

In Visual Studio, there is built-in support for Cyclomatic Complexity analysis.

<!--endintro-->

1. Go to Analyze | Calculate Code Metrics | For Solution

![Figure: Launching the Code Metrics tool within Visual Studio](calculate_code_metrics.jpg "Screenshot of how to launch the Code Metrics tool within Visual Studio")

2. Look at the function with the largest Cyclomatic Complexity number and consider refactoring to make it simpler.

![Figure: Results from cyclomatic analysis (and other analyses) give an indication of how complicated functions are](code_metrics_report.jpg "Screenshot of the Code Metrics Results in Visual Studio")

:::greybox

**Tip:** Aim for "green" against each function's Maintainability Index.
:::
