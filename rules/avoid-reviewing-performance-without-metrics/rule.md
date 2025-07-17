---
seoDescription: Optimize your performance reviews by using metrics to measure and track progress, ensuring you're meeting clients' expectations and making informed improvements.
type: rule
archivedreason:
title: Do you avoid reviewing performance without metrics?
guid: 6bdcdd2d-695a-46fa-93cc-cd761276586a
uri: do-you-avoid-reviewing-performance-without-metrics
created: 2009-03-17T05:48:04.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related:
  - website-page-speed
  - keep-your-website-loading-time-acceptable
  - steps-required-to-implement-a-performance-improvement
redirects:
  - do-you-avoid-reviewing-performance-without-metrics
---

When a client complains about performance, it’s important not to jump straight into the code and make blind fixes. Instead of guessing what might help, we need to approach it methodically—starting with clear benchmarks, profiling, and data-driven decisions.

<!--endintro-->

For example, if a client says:

> _"This application is too slow, I don't really want to put up with such poor performance. Please fix."_

We don't jump in and look at the code and clean it up and reply with something like:

> _"I've looked at the code and cleaned it up. Please tell me if you are OK with the performance now."_

A better way is:

* Ask the client to tell us how slow it is (in seconds) and how fast they ideally would like it (in seconds)
* Add some code to record the time the function takes to run
* Reproduce the steps and record the time
* Change the code
* Reproduce the steps and record the time again
* Reply with metrics. E.g. _"It was 22 seconds, you asked for around 10 seconds. It is now 8 seconds."_

::: good  
![Figure: Good example – Add some code to check the timing, before fixing any performance issues (An example from SSW CodeAuditor)](Code-Auditor-performance.jpg)  
:::

Also, never forget to do incremental changes in your tests!

For example, if you are trying to measure the optimal number of processors for a server, do not go from 1 processor to 4 processors at once:

::: bad  
![Figure: Bad example - Going from 1 to 4 all at once gives you incomplete measurements and data](1to4.png)  
:::

Do it incrementally, adding 1 processor each time, measuring the results, and then adding more:

::: good  
![Figure: Good example - Going from 1 to 2, then measuring, then incrementally adding one more, measuring...](1234.png)  
:::

This gives you the most complete set of data to work from.

This is because performance is an emotional thing, sometimes it just \*feels\* slower. Without numbers, a person cannot really know for sure whether something has become quicker. By making the changes incrementally, you can be assured that there aren’t bad changes canceling out the effect of good changes.

## Measuring Performance

Depending on your tech stack, there are various tools available to measure performance. For frontends, Google Chrome's DevTools provides a performance measurement tool.

![Figure: Google Chrome has a handy Performance tab in the DevTools](chrome-perf-tools.png)

### Samples

For sample code on how to measure performance, please refer to [Do you have tests for Performance?](/have-tests-for-performance/) on [Rules To Better Unit Tests](/rules-to-better-unit-tests/).
