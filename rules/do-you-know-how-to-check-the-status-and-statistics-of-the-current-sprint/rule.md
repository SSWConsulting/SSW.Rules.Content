---
type: rule
archivedreason: 
title: Do you know how to check the status and statistics of the current Sprint?
guid: c09e24e8-2a9e-449c-b0f5-180a1836d51c
uri: do-you-know-how-to-check-the-status-and-statistics-of-the-current-sprint
created: 2012-08-01T18:29:05.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
related: []

---

Developers think they are done when they finish coding and check in.

Wrong. It is much better to [use Microsoft Test Manager (MTM) and step through the Acceptance Tests.](/Pages/Do-You-Run-Acceptance-Tests.aspx)

Once you are doing that, this is how you check the status of the current Sprint:

<!--endintro-->
<dl class="image">&lt;dt&gt;<img alt="run acceptance tests" src="check-sprint-status.jpg">&lt;/dt&gt;<dd>Figure: Good example - This Sprint currently has 2 'Failed' tests (red), and 1 'Active' test (blue). (This 'Results' view is new in MTM 2012) </dd></dl>
Key:

* The red is work remaining for the developers, and
* The blue is working remaining for the testers (unfinished testing)
