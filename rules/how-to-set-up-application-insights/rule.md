---
type: rule
archivedreason: 
title: Do you know how to set up Application Insights?
guid: 623a361d-a06e-443c-a6c7-d15c203e2d0d
uri: how-to-set-up-application-insights
created: 2015-07-24T04:48:34.0000000Z
authors:
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
related:
- do-you-know-how-to-set-up-application-insights-in-sharepoint
- do-you-use-an-analytics-framework-to-help-manage-exceptions
- do-you-know-why-you-want-to-use-application-insights
redirects:
- do-you-know-how-to-set-up-application-insights

---


<p class="ssw15-rteElement-P">​The easiest way to get started with Application Insights is to follow the documentation on MSDN <a href="https://azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/">https://azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/</a> </p><p class="ssw15-rteElement-P">Lets take a look at the overview and our tips to help you get the most out of Application Insights.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>
   <strong>An overview of the setup steps</strong> Application Insights requires that you make 2 general modifications to your application:</p><ol><li>On the client side, manually<a href="https://azure.microsoft.com/en-us/documentation/articles/app-insights-javascript/"> add a Javascript tracker to your web page header</a> (i.e. by placing directly on each page or through a "master page" or "layout template"), this modification enables the "browser page loading time" monitor and can track client-side exceptions: <dl class="image"><dt><img alt="app-insights-browser-loading-time.jpg" src="app-insights-browser-loading-time.jpg" style="width:370px;" /></dt><dd> Browser side stats have been enabled with the JavaScript tracker</dd></dl></li><li>On the server side, <a href="https://azure.microsoft.com/en-us/documentation/articles/app-insights-start-monitoring-app-health-usage/">add the Application Insights DLL references and update web.config</a>, these modifications enable the "server response time", "server request" and "failed requests" monitors. <span style="font-family:"segoe ui";">This step can either be done within Visual Studio when right-clicking on a project in Solution Explorer, but it can also be done with the server monitoring tool on ASP.NET applications you don't have control over (e.g. SharePoint).</span></li><li><dl class="image"><dt><img alt="server-response-requests-failed-requests.jpg" src="server-response-requests-failed-requests.jpg" style="width:382px;" /></dt><dd>Server side stats have been enabled now that it has been added to the ASP.NET pipeline </dd></dl></li></ol><p>
   <strong>Tip #1 – Add enhanced Exception tracking to your application</strong> <br>The default set up and configuration of Application Insights will send generic performance stats and Exceptions. If you will be using Application Insights to look deeper into these Exceptions then it is important to make sure the full stack trace is sent when Exceptions occur. This can be added to your application by adding code for all unhandled exceptions. Follow this documentation page for more information <a href="https://azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/">https://azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/</a></p><p>
   <strong>Tip #2 – Add Web tests to monitor performance metrics over time<br></strong> As soon as you have configured Application Insights, you should immediately add a web test to track the general performance trends  over time. More information can be found at this rule <a href=/do-you-add-web-tests-to-application-insights-to-montior-trends-over-time> https://rules.ssw.com.au/do-you-add-web-tests-to-application-insights-to-montior-trends-over-time </a></p><p>
      <strong>Tip #3 – What if you don't have the source code of your ASP.NET application </strong></p><p>This rule on how to add Application Insights to a SharePoint application shows that you can use the Application Insights monitor to add the .dlls and modify the web.config file of a deployed application <a>https://rules.ssw.com.au/application-insights-in-sharepoint</a> <br></p>


