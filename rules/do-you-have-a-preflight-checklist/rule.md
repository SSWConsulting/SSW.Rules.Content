---
seoDescription: Ensure a smooth start by checking unit tests, unhandled exceptions, and performance issues in Application Insights before diving into work.
type: rule
archivedreason:
title: Do you have a Preflight Checklist?
guid: 8657ba34-afda-47b8-8728-f971fd3f699b
uri: do-you-have-a-preflight-checklist
created: 2015-11-01T21:13:26.0000000Z
authors:
  - title: Ben Cull
    url: https://ssw.com.au/people/ben-cull
related: []
redirects: []
---

Before starting any work, you should ensure developers take a look at your Application Insights data to make sure everything is performing correctly.

<!--endintro-->

Most developers check only this first item before starting their work:

1. Check Unit Tests are Green

![](unittests.png)

**Figure: Tests are green. I'm ready to start work... or am I?**

More advanced teams check their application insights data as well. This includes:

2. Look for any new Unhandled Exceptions

> See [Do you know the daily process to improve the health of your web application?](/do-you-know-the-process-to-improve-the-health-of-your-web-application)

> ![](App-Insights-Failures_1710232021934.png)
>
> **Figure: Unhandled Exceptions - Is there anything you don't know about here?**

3. Look for any obvious performance issues (Server then client).

> See [Do you know how to find performance problems with Application Insights?](/do-you-know-how-to-find-performance-problems-with-application-insights)

> ![](performance-4_1710232021934.jpg)
>
> **Figure: Performance - The Server Responses tab shows the slowest running pages.**
