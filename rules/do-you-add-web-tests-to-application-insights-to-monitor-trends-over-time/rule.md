---
type: rule
title: Do you add Web Tests to Application Insights to monitor trends over time?
uri: do-you-add-web-tests-to-application-insights-to-monitor-trends-over-time
created: 2015-09-02T09:09:08.0000000Z
authors:
- id: 45
  title: Chris Briggs

---



<span class='intro'> <p>As soon as you have configured Application Insights, you should immediately add a Web Test to track general performance trends&#160;over time. You can configure test agents to access your application from different locations around the globe to give a general idea of&#160;what users will experience.&#160;​<br></p> </span>

<p>Instructions on how to add Web Tests can be found on MSDN&#160;<a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-web-app-availability/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-web-app-availability</a>
   </p><p>Setting up a Web Test will allow you to query and see how the performance of your application has&#160; changed over a period of time and to help you spot any anomalies. It can be useful to query over a long period of time (e.g. a year) and see if the performance has stayed the same or if there have been any regressions in responsiveness.</p><dl class="goodImage"><dt> <img alt="App Insights Web Test.png" src="/PublishingImages/App-Insights-Web-Test.png" style="width&#58;742px;" /></dt><dd>Good Example - You can clearly see the point where we deployed a fix to production to improve the initial page load. </dd></dl><p>You have the ability to drill down into web test results, to get an overview of the response time of the resources on a page. This can help discover if certain resources are slowing the response time.</p><dl class="goodImage"><dt> <img alt="App Insights Web Test drilldown.png" src="/PublishingImages/App-Insights-Web-Test-drilldown.png" style="width&#58;650px;" /></dt><dd> Good Example - Reviewing the Web test results, provides vital information .​</dd></dl> <br>


