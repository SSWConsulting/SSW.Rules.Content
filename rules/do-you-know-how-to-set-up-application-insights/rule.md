---
type: rule
title: Do you know how to set up Application Insights?
uri: do-you-know-how-to-set-up-application-insights
created: 2015-07-24T04:48:34.0000000Z
authors:
- id: 45
  title: Chris Briggs

---



<span class='intro'> <p class="ssw15-rteElement-P">​The easiest way to get started with Application Insights is to follow the documentation on MSDN <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/</a>&#160;</p><p class="ssw15-rteElement-P">Lets take a look at the overview and our tips to&#160;help you get the most out of Application Insights.</p> </span>

<p>
   <strong>An overview of the setup steps</strong> Application Insights requires that you make 2 general modifications to your application&#58;</p><ol><li>On the client side, manually<a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-javascript/"> add a Javascript tracker to your web page header</a>&#160;(i.e. by placing directly on each page or&#160;through a &quot;master page&quot; or &quot;layout template&quot;), this modification&#160;enables the &quot;browser page loading time&quot; monitor and can track client-side exceptions&#58; <dl class="image"><dt><img alt="app-insights-browser-loading-time.jpg" src="/PublishingImages/app-insights-browser-loading-time.jpg" style="width&#58;370px;" /></dt><dd> Browser side stats have been enabled with the JavaScript tracker</dd></dl></li><li>On the server side, <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-start-monitoring-app-health-usage/">add the Application Insights DLL references and update web.config</a>, these modifications enable&#160;the &quot;server response time&quot;, &quot;server request&quot; and &quot;failed requests&quot; monitors.&#160;<span style="font-family&#58;&quot;segoe ui&quot;;">This step can either be done within Visual Studio when right-clicking on a project in Solution Explorer, but it can also be done with the server monitoring tool on&#160;ASP.NET applications you don't have control over (e.g. SharePoint).</span></li><li><dl class="image"><dt><img alt="server-response-requests-failed-requests.jpg" src="/PublishingImages/server-response-requests-failed-requests.jpg" style="width&#58;382px;" /></dt><dd>Server side&#160;stats have been enabled now that it has been added to the ASP.NET pipeline </dd></dl></li></ol><p>
   <strong>Tip #1&#160;– Add enhanced Exception tracking to your application</strong>&#160;<br>The&#160;default set up and configuration of Application Insights will send generic performance stats and Exceptions. If you will be using Application Insights to look&#160;deeper into these&#160;Exceptions then it is important to make sure the full stack trace is sent when Exceptions occur. This can be added to your application by adding code for all unhandled exceptions. Follow this documentation page for more information <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/</a></p><p>
   <strong>Tip #2&#160;– Add Web tests to monitor performance metrics over time<br></strong> As soon as you have configured Application Insights, you should immediately add a web test to track the general performance trends&#160; over time. More information can be found at this rule <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=1ff43a84-e259-48c5-8b7a-f48433a7ec3c"> https&#58;//rules.ssw.com.au/do-you-add-web-tests-to-application-insights-to-montior-trends-over-time </a></p><p>
      <strong>Tip #3&#160;– What if you don't have the source code of your ASP.NET&#160;application </strong></p><p>This rule on how to add Application Insights to a SharePoint application shows that you can use the Application Insights monitor to add the .dlls and modify the web.config file of a deployed application <a>https&#58;//rules.ssw.com.au/application-insights-in-sharepoint</a> <br></p>


