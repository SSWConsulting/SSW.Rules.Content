---
type: rule
title: Do you use the best exception handling library?
uri: do-you-use-the-best-exception-handling-library
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
related:
  - do-you-use-the-best-exception-handling-library
redirects: []
created: 2013-09-11T19:17:07.000Z
archivedreason: null
guid: 4758ac66-d4a5-4ccd-93cc-85c1f2d369da
---

When developing software, exceptions are a fact-of-life you will need to deal with. Don't reinvent the wheel, use an existing exception handling library or service.

Your users should never see the “yellow screen of death” in ASP.NET, or the “unhandled exception” message in a Windows application. Errors should always be caught and logged – preferably in a SQL database. As developers you should be alerted when something is going wrong and be able to see details to help you track down and fix bugs.

::: bad
![Figure: Bad - If you see this, you are doing something wrong!](default-asp-error-500_small.png)
:::

<!--endintro-->

At SSW we use [Application Insights](/rules-to-better-application-insights) where possible. If you are still developing Windows applications, then you can still use Application Insights, read [here](https://docs.microsoft.com/en-us/azure/azure-monitor/app/windows-desktop) for more details.

::: greybox
**Application Insights** will tell you if your application goes down or runs slowly under load. If there are any uncaught exceptions, you’ll be able to drill into the code to pinpoint the problem. You can also find out what your users are doing with the application so that you can tune it to their needs in each development cycle.
:::

If Application Insights is not available we use Seq when developing web applications. From its [page](https://datalust.co/seq):

::: greybox
**Seq** is built for modern structured logging with message templates. Rather than waste time and effort trying to extract data from plain-text logs with fragile log parsing, the properties associated with each log event are captured and sent to Seq in a clean JSON format. Message templates are supported natively by ASP.NET Core, Serilog, NLog, and many other libraries, so your application can use the best available diagnostic logging for your platform.
:::

Application Insights gives you very useful graphs and analysis which give you a good overview of how things are going. See [here](/rules-to-better-application-insights) for more details. Seq is great for identifying specific issues and how to fix them, but is not as good at letting you see the big picture.

::: good
![Figure: Good - Seq provides you with plenty of details about what is happening, but if you don't already know what you're looking for, it can be tricky to parse](xn4QHnmBS0Kx39gOv0wM_GettingStarted-1.png)
:::

::: good
![Figure: Good - Application Insights gives you graphs and analysis that help you find issues, but also lets you drill down to get the details as well](overview.png)
:::
