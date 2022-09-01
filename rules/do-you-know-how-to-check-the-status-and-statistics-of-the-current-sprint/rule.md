---
type: rule
title: Do you know how to check the status and statistics of the current Sprint?
uri: do-you-know-how-to-check-the-status-and-statistics-of-the-current-sprint
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-08-01T18:29:05.000Z
archivedreason: null
guid: c09e24e8-2a9e-449c-b0f5-180a1836d51c
---
Developers sometimes think they're done when they finish coding and check in.

It's easy to forget about testing, but this will often result in rework or bug fixes for the developers - in other words, more work!

Keeping an eye on the results of [acceptance testing](/do-you-run-acceptance-tests) can help you understand where things are really at in the sprint.

<!--endintro-->

Azure Test Plans provides two different ways to see testing status, a built-in [Progress Report](https://docs.microsoft.com/en-us/azure/devops/test/progress-report?view=azure-devops) and customizable [Test Status](https://docs.microsoft.com/en-us/azure/devops/test/track-test-status?view=azure-devops) charts.




::: good  
![Figure: Good example - This Sprint currently has 2 'Failed' tests (red), and 1 'Active' test (blue). (This 'Results' view is new in MTM 2012)](check-sprint-status.jpg)  
:::

Key:

* The red (representing failed tests) is work remaining for the developers, and
* The blue (representing unfinished tests) is working remaining for the testers.