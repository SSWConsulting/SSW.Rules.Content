---
type: rule
archivedreason: The rule is either out of date or needs to be updated.
title: Do you include Application Insights for Visual Studio Online in your website?
guid: eacb0254-964d-451c-bda5-7024d2532159
uri: do-you-include-application-insights-for-visual-studio-online-in-your-website
created: 2014-08-20T04:10:49.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Application Insights for Visual Studio Online gives you a great insight into how, when and where your website is used. 
<!--endintro-->



If you're not using an analytics package in your website, you're flying blind when it comes to understanding how, when and where your webiste is used.

To add Application Insights to your website, follow these steps.

![](apin1-compressor.png)
 **Figure: In Visual Studio, go to Tools | Extensions and Updates... and download Application Insights Tools for Visual Studio**

**
**

![](apin5-compressor.png)
 **Figure: Once Visual Studio has been restarted, open your solution. Right-click on your web project and select Add Application Insights Telemetry to Project...**

(Add Application Insights Telemetry to Project... not displaying? See instructions at the end of this rule)

![](apin6-compressor.png)
 **Figure:** **Sign in with your VSO account if required. Then click Add Application Insights To Project**



![](apin7-compressor.png)
 **Figure: This will update your project with the NuGet package and settings to include Application Insights in your project. Check this in and deploy your website.**



![](apin9-compressor.png)
 **Figure: Now when you right-click on your web project there is a new option Open Application Insights Portal...**

**
**

![](apin10-compressor.png)
**Figure: Dashboard showing summary and application metrics**



Once deployed, Application Insights will start tracking metrics and interacting with your Visual Studio Online dashboards.

Application Insights tracks a lot of metrics in your website but one of the most useful is the breakdown of visits by each browser (IE, Chrome etc).

![](apin4-compressor.png)
 **Figure: Breakdown of which browsers are used to access your website**

**Note:** Make sure Server Performance Monitoring is set up (currently not available for Azure Websites)

![1.png](AnyConnect 1.png)

**Figure: Ensure you complete this process to add Server Monitoring**

Sometimes you will be trying to add Application Insights to an existing project and the context menu item will not be there. There is a manual way to add Application Insights if this is the case.

![](2014-09-05_14-49-56-compressor.png)
 **Figure: Sign into Visual Studio Online, and navigate to Application Insights | Add Application**



![](2014-09-05_14-59-06-compressor.png)
 **Figure: Use these settings to generate the manual instructions**



![](2014-09-05_15-26-32-compressor.png)
 **Figure: Follow these steps to add the Application Insights JavaScript code to your website**
