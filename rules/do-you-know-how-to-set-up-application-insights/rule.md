---
type: rule
title: Do you know how to set up Application Insights?
uri: do-you-know-how-to-set-up-application-insights
created: 2015-07-24T04:48:34.0000000Z
authors:
- id: 45
  title: Chris Briggs

---



<span class='intro'> <p>​​​​The easiest way to get started with Application Insights is to follow the documentation on MSDN <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-get-started/</a> <br>Below are our additional suggestions to help you get the most out of Application Insights.</p><p>&#160;</p> </span>

<div><strong>High&#160;level summary of setup</strong></div>Application Insights requires that you make 2 general modifications to your application&#58;<ol><li>Manually add a Javascript tracker to your web page header&#160;(can be done through&#160;master page), this modification&#160;enables the &quot;browser page loading time&quot; monitor and can track client side exceptions&#58;<br><img alt="app-insights-browser-loading-time.jpg" src="/SiteAssets/application-insights-in-sharepoint/app-insights-browser-loading-time.jpg" style="margin&#58;5px;width&#58;275px;" /></li><li>Add Application Insights DLL references and update web.config, these modifications enable&#160;the &quot;server response time&quot;, &quot;server request&quot; and &quot;failed requests&quot; monitors. <br>This is usually done&#160;via the tools&#160;within Visual Studio, but can&#160;be done via the server monitoring tool to an ASP.Net application you don't have control over (e.g. SharePoint).<br><img alt="server-response-requests-failed-requests.jpg" src="/SiteAssets/application-insights-in-sharepoint/server-response-requests-failed-requests.jpg" style="margin&#58;5px;width&#58;284px;" />&#160;<span>&#160;</span></li></ol><div><br></div><p>
   <strong>Tip #1&#160;– Add enhanced Exception tracking to your application</strong><br>The&#160;default set up and configuration of Application Insights will send generic performance stats and Exceptions. If you will be using Application Insights to look&#160;deeper into these&#160;Exceptions then it is important to make sure the full stack trace is sent when Exceptions occur. This can be added to your application by adding code for all unhandled exceptions. Follow this documentation page for more information <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-asp-net-exceptions/</a></p><p>
   <strong>Tip #2&#160;– Add Web tests to monitor performance metrics over time<br></strong>As soon as you have configured Application Insights, you should immediately add a web test to track the general performance trends&#160;​​over time. More information can be found at this rule &lt;Rule coming soon&gt;</p><p>
   <strong>Tip #3&#160;– You can add monitoring to ASP.Net applications you have deployed but don't have source control access over</strong><br>This rule on how to add Application Insights to a SharePoint application shows that you can use the Application Insights monitor to add the .dlls and modify the web.config file of a deployed application <a>https&#58;//rules.ssw.com.au/application-insights-in-sharepoint</a>​</p>


