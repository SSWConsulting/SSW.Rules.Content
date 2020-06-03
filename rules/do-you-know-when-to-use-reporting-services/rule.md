---
type: rule
title: Do you know when to use Reporting Services?
uri: do-you-know-when-to-use-reporting-services
created: 2013-07-02T08:25:41.0000000Z
authors: []

---



<span class='intro'> <span style="font&#58;12px/16.79px verdana, sans-serif;text-align&#58;left;color&#58;#000000;text-transform&#58;none;text-indent&#58;0px;letter-spacing&#58;normal;word-spacing&#58;0px;float&#58;none;display&#58;inline !important;white-space&#58;normal;font-size-adjust&#58;none;font-stretch&#58;normal;">Like any solution, Reporting Services has its pros and cons. From our experience, we have discovered these things about Reporting Services&#58;</span> </span>

<span class="ssw-rteStyle-FigureNormal"></span><span class="ssw-rteStyle-FigureNormal">Cons<br></span><ul><li>Parameters - you are forced to use built-in controls</li><li>Query string - when you change the parameters and refresh a report, the values do not appear directly in the query string, making it hard to copy/paste URLs</li><li>Can't separate SQL into a strongly-typed dataset or middle-tier object like in ASP.NET</li><li>There are potential difficulties with the deployment of RS reports and the exposing of them. However, once we have the infrastructure...</li></ul><strong>Pros</strong><br><ul><li>You can develop&#160;read only&#160;reports faster in Reporting Services than ASP.NET</li><li>Maintenance with RS is easier than ASP .NET, as with most cases you don't have to write any code</li><li>Flexibility with groupings and totals is easier. In ASP.NET you would need to iterate through the DataSet, keeping variables with the totals</li><li>Parameters are built-in. In ASP.NET there is code</li><li>Drilldown interactivity. In ASP.NET you need to code up a treeview</li><li>Users can have reports automatically emailed to them on a schedule</li><li>Users can export natively to PDF and XLS, plus a variety of other popular formats</li></ul>So in conclusion, if you will only ever need 1 report, go with ASP.NET - it is easier to get up and running. If you plan to have more than one report, use Reporting Services - it's worth the time to configure.<br><br>For a more detailed comparison between reporting solutions, take a look at our&#160;<a href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperDotNet/guidelinesforreportingwebclient.aspx">Guidelines for Report Solutions - Web Clients</a>.<br><br><p style="font&#58;12px/1.4em verdana, sans-serif;margin&#58;7px 0px;padding&#58;0px;text-align&#58;left;text-transform&#58;none;text-indent&#58;0px;letter-spacing&#58;normal;word-spacing&#58;0px;white-space&#58;normal;font-size-adjust&#58;none;font-stretch&#58;normal;"><img class="ssw-rteStyle-ImageArea" alt="RSRulesUseRS1.gif" src="/PublishingImages/RSRulesUseRS1.gif" style="margin&#58;5px;" /><span class="ssw-rteStyle-FigureNormal">Figure&#58; Reporting Services has built-in support for PDF/XLS export and can be embedded in your ASP.NET pages</span></p>


