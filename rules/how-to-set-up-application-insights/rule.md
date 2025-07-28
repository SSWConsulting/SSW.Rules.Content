---
seoDescription: Learn how to set up Application Insights and start monitoring your application's performance, exceptions, and user behavior.
type: rule
archivedreason:
title: Do you know how to set up Application Insights?
guid: 623a361d-a06e-443c-a6c7-d15c203e2d0d
uri: how-to-set-up-application-insights
created: 2015-07-24T04:48:34.0000000Z
authors:
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
related:
  - do-you-know-how-to-set-up-application-insights-in-sharepoint
  - do-you-use-an-analytics-framework-to-help-manage-exceptions
  - do-you-know-why-you-want-to-use-application-insights
  - infrastructure-health-checks
  - clean-failed-requests
redirects:
  - do-you-know-how-to-set-up-application-insights
---

The easiest way to get started with Application Insights is to [follow the documentation on Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).

Lets take a look at the overview and our tips to help you get the most out of Application Insights.

<!--endintro-->

## An overview of the setup steps

Application Insights requires that you make 2 general modifications to your application:

1. On the client side, manually [add a Javascript tracker to your web page header](https://learn.microsoft.com/en-us/azure/azure-monitor/app/javascript-sdk?tabs=javascriptwebsdkloaderscript) (i.e. by placing directly on each page or through a "master page" or "layout template"), this modification enables the "browser page loading time" monitor and can track client-side exceptions:

   ![Browser side stats have been enabled with the JavaScript tracker](app-insights-browser-loading-time.jpg)

2. On the server side, [install and configure the Azure.Monitor.OpenTelemetry.AspNetCore package](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=aspnetcore). These modifications enable the "server response time", "server request" and "failed requests" monitors.

  ![Server side stats have been enabled now that it has been added to the ASP.NET pipeline](server-response-requests-failed-requests.jpg)

## Tips

Now that you've added Application Insights, what can you do with it?

### Add Health Checks

Application Insights makes it easy to check the health of your app and its infrastructure - see [Do you Health Check your infrastructure?](/infrastructure-health-checks).

### Create a custom dashboard

A custom [Application Insights dashboard](https://learn.microsoft.com/en-us/azure/azure-monitor/app/overview-dashboard#create-custom-kpi-dashboards-using-application-insights) makes monitoring your application much easier. The KPIs that you would typically monitor for each component of your application are:

- How many requests each component is receiving.
- How long requests are taking.
- How many exceptions and dependency failures are being experienced by the app.
- [How many requests are failing.](/clean-failed-requests)

When designing your custom dashboard:

- Size charts based on their importance.
- Lay charts out so that it is easy to compare points in time between charts.
- Ensure that metrics with different scales are not on the same chart. For instance, the average server response time may vary between 250 and 500 milliseconds, but that variance may not be easily visible if the maximum server response time is plotted as taking 40 seconds on the same chart.

![Good example - Custom dashboard demonstrating the above points](good-example-custom-dashboard.png)
