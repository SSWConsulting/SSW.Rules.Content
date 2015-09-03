---
type: rule
title: Do you add Web Tests to Application Insights to monitor trends over time?
uri: do-you-add-web-tests-to-application-insights-to-monitor-trends-over-time
created: 2015-09-02T09:09:08.0000000Z
authors:
- id: 45
  title: Chris Briggs

---



<span class='intro'> <p>As soon as you have configured Application Insights, you should immediately add a Web Test to track general performance trends&#160;over time. You can configure test agents to access your application from different locations around the globe to give a general idea of&#160;what users will experience.&#160;<br>Instructions on how to add Web Tests can be found on MSDN&#160;<a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-web-app-availability/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-web-app-availability/ </a></p> </span>

<p>Setting up a Web Test will allow you to query and see how the performance of your application has&#160;​changed over a period of time and to help you spot any anomalies. It can be useful to query over a long period of time (e.g. a year) and see if the performance has stayed the same or if there have been any regressions in responsiveness.​</p><p>In the screenshot below, you can clearly see the point where we deployed a fix to production to improve the initial page load.<br><img src="/PublishingImages/App-Insights-Web-Test.png" alt="App Insights Web Test.png" style="line-height&#58;1.6;margin&#58;5px;width&#58;742px;height&#58;350px;" /><span style="line-height&#58;1.6;">​​​​</span></p><p><span style="line-height&#58;1.6;">You have the ability to drill down into web test results, to get an overview of the response time of the resources on a page. This can help discover if certain resources are slowing the response time.<br><img src="/PublishingImages/App-Insights-Web-Test-drilldown.png" alt="App Insights Web Test drilldown.png" style="margin&#58;5px;width&#58;650px;" /></span></p>


