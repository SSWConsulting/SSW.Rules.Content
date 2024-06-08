---
type: rule
title: Do you know why to use Application Insights?
uri: why-you-want-to-use-application-insights
authors:
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-use-an-analytics-framework-to-help-manage-exceptions
  - how-to-set-up-application-insights
redirects:
  - do-you-know-why-you-want-to-use-application-insights
created: 2015-07-24T04:40:05.000Z
archivedreason: null
guid: af36ac71-56ce-4879-bb04-0d3cb42b7beb
---

Knowing the holistic health of your application is important once it has been deployed into production. Getting feedback on your Availability, errors, performance, and usage is an important part of DevOps.
We recommend using Application Insights, as getting it set up and running is quick, simple and relatively painless.

Application Insights will tell you if your application goes down or runs slowly under load. If there are any uncaught exceptions, you'll be able to drill into the code to pinpoint the problem. You can also find out what your users are doing with the application so that you can tune it to their needs in each development cycle.

<!--endintro-->

![Figure:  When developing a public website, you wouldn't deploy without Google Analytics to track metrics about user activity.](Google-analytics.png)  

![Figure: For similar reasons, you shouldn't deploy a web application without metric tracking on performance and exceptions](2020-03-24\_15-27-26.jpg)  

1. You need a portal for your app
2. You need to know spikes are dangerous
3. You need to monitor:
    1. Errors
    2. Performance
    3. Usage


![Figure: Spikes on an Echidna are dangerous](../../assets/r437355\_2104314.jpg)  

![Figure: Spikes on a graph are dangerous](../../assets/sockeye-daily-count.jpg)  

To add Application Insights to your application, make sure you follow the rule [Do you know how to set up Application Insights?](/how-to-set-up-application-insights)

Can't use Application Insights? Check out the following rule [Do you use the best exception handling library](/do-you-use-the-best-exception-handling-library) ?
