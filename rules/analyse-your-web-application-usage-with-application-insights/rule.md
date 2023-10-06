---
type: rule
archivedreason: 
title: Do you know how to analyse your web application usage with Application Insights?
guid: 5c6458c0-4227-406a-ba7d-27717272057c
uri: analyse-your-web-application-usage-with-application-insights
created: 2015-10-27T15:19:19.0000000Z
authors:
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
- title: Gordon Beeming
  url: https://ssw.com.au/people/gordon-beeming
related: []
redirects: 
- do-you-know-how-to-analyse-your-web-application-usage-with-application-insights

---

You've set up your Application Insights as per the rule 'Do you know how to set up Application Insights.

Your daily failed requests are down to zero & You've tightened up any major performance problems.

Now you will discover that understanding your users' usage within your app is child's play.

<!--endintro-->

The Application Insights provides devs with two different levels of usage tracking. The first is provided out of the box, made up of the user, session, and page view data. However, it is more useful to set up custom telemetry, which enables you to track users effectively as they move through your app.

![Figure: Easily track and compare custom events](custom-events-in-app-insights.jpg)  

It is very straightforward to add these to an application by adding a few lines of code to the hot points of your app. Follow [Application Insights API for custom events and metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/app/api-custom-events-metrics) to learn more.

If you feel constricted by the Application Insights custom events blade? Then you can export your data and display it in PowerBI, take a look at [Using Azure Log Analytics in Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/log-analytics/desktop-log-analytics-overview)

