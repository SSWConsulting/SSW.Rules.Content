---
seoDescription: Learn how to set up Application Insights in SharePoint, a different approach from normal web applications.
type: rule
archivedreason:
title: Do you know how to set up Application Insights (in SharePoint)?
guid: c7ad6539-184a-4a70-8190-5c1ec9ddb822
uri: application-insights-in-sharepoint
created: 2015-09-01T00:28:34.0000000Z
authors:
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
related:
  - how-to-set-up-application-insights
redirects:
  - do-you-know-how-to-set-up-application-insights-in-sharepoint
  - do-you-know-how-to-set-up-application-insights-(in-sharepoint)
---

The best approach of setting up Application Insights in SharePoint is a bit different than adding to normal web application.

<!--endintro-->

::: greybox
**Note:** To check the normal way of setting up Application Insights via Visual Studio, please read "[How to set up Application Insights](/how-to-set-up-application-insights)"
:::

With a web application you are developing you have full control of web.config and have access to it in your Visual Studio project, and can follow "[How to set up Application Insights](/how-to-set-up-application-insights)" to set up Application Insights. This way Visual Studio will do all the modifications for you automatically.

But when you develop on SharePoint, you **do not** have a full copy of web.config in your Visual Studio project, the web.config will be initialized on the SharePoint server when a new SharePoint site is created. This means Visual Studio cannot be used to update the web.config for you. Although you can modify SharePoint web.config via coding, that involves lots of development and testing work against your SharePoint server.

The best process to implement Applications Insights in SharePoint can be split into two parts:

1. Implement App Insight JavaScript in master page (via Visual Studio)  or web pages individually via embedded code, there are two good articles include the detail steps:

* [https://docs.microsoft.com/en-us/azure/azure-monitor/app/sharepoint](https://docs.microsoft.com/en-us/azure/azure-monitor/app/sharepoint)
* [https://azure.microsoft.com/en-us/blog/understand-your-sharepoint-usage-with-application-insights-2/](https://azure.microsoft.com/en-us/blog/understand-your-sharepoint-usage-with-application-insights-2/)

2. Use Application Insights Status Monitor configuration tool to add DLLs reference and update web.config (no coding work involved), there are two articles include the detail steps:
   * [https://devblogs.microsoft.com/devops/monitoring-your-existing-applications/](https://devblogs.microsoft.com/devops/monitoring-your-existing-applications/)
   * [https://docs.microsoft.com/en-us/azure/azure-monitor/app/monitor-performance-live-website-now](https://docs.microsoft.com/en-us/azure/azure-monitor/app/monitor-performance-live-website-now)
