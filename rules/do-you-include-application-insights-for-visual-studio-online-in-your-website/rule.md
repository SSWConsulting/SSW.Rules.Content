---
type: rule
archivedreason: The rule is either out of date or needs to be updated.
title: Do you include Application Insights for Visual Studio Online in your website?
guid: eacb0254-964d-451c-bda5-7024d2532159
uri: do-you-include-application-insights-for-visual-studio-online-in-your-website
created: 2014-08-20T04:10:49.0000000Z
authors:
- id: 38
  title: Drew Robson
- id: 1
  title: Adam Cogan
related: []

---

Application Insights for Visual Studio Online gives you a great insight into how, when and where your website is used. 
<!--endintro-->



If you're not using an analytics package in your website, you're flying blind when it comes to understanding how, when and where your webiste is used.

To add Application Insights to your website, follow these steps.


![In Visual Studio, go to Tools | Extensions and Updates... and download Application Insights Tools for Visual Studio](apin1-compressor.png)

**
**


![Once Visual Studio has been restarted, open your solution. Right-click on your web project and select Add Application Insights Telemetry to Project...](apin5-compressor.png)

(Add Application Insights Telemetry to Project... not displaying? See instructions at the end of this rule)


![ Sign in with your VSO account if required. Then click Add Application Insights To Project](apin6-compressor.png)




![This will update your project with the NuGet package and settings to include Application Insights in your project. Check this in and deploy your website.](apin7-compressor.png)




![Now when you right-click on your web project there is a new option Open Application Insights Portal...](apin9-compressor.png)

**
**


![Dashboard showing summary and application metrics](apin10-compressor.png)



Once deployed, Application Insights will start tracking metrics and interacting with your Visual Studio Online dashboards.

Application Insights tracks a lot of metrics in your website but one of the most useful is the breakdown of visits by each browser (IE, Chrome etc).


![Breakdown of which browsers are used to access your website](apin4-compressor.png)

**Note:** Make sure Server Performance Monitoring is set up (currently not available for Azure Websites)


![Ensure you complete this process to add Server Monitoring](AnyConnect 1.png)

Sometimes you will be trying to add Application Insights to an existing project and the context menu item will not be there. There is a manual way to add Application Insights if this is the case.


![Sign into Visual Studio Online, and navigate to Application Insights | Add Application](2014-09-05_14-49-56-compressor.png)




![Use these settings to generate the manual instructions](2014-09-05_14-59-06-compressor.png)




![Follow these steps to add the Application Insights JavaScript code to your website](2014-09-05_15-26-32-compressor.png)
