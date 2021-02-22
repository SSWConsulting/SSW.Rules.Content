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


​​​​​​​​​​Application Insights for Visual Studio Online gives you a great insight into how, when and where your website is used.
<br><excerpt class='endintro'></excerpt><br>
<p>​</p><p>If you're not using an analytics package in your website, you're flying blind when it comes to understanding how, when and where your webiste is used.<br></p><p>To add Application Insights to your website, follow these steps.</p><p><img src="apin1-compressor.png" alt="apin1-compressor.png" style="margin:5px;width:650px;" /><br><strong>Figure: In Visual Studio, go to Tools | Extensions and Updates... and download Application Insights Tools for Visual Studio</strong></p><p><strong><br></strong></p><p><img src="apin5-compressor.png" alt="apin5-compressor.png" style="margin:5px;width:650px;" /><br><strong>Figure: Once Visual Studio has been restarted, open your solution. Right-click on your web project and select Add Application Insights Telemetry to Project...</strong></p><p>(Add Application Insights Telemetry to Project... not displaying? See instructions at the end of this rule)</p><p><img src="apin6-compressor.png" alt="apin6-compressor.png" style="margin:5px;width:650px;" /><br><strong>Figure: </strong><strong>Sign in with your VSO account if required. Then click Add Application Insights To Project</strong></p><p><br></p><p><img src="apin7-compressor.png" alt="apin7-compressor.png" style="margin:5px;" /><br><strong>Figure: This will update your project with the NuGet package and settings to include Application Insights in your project. Check this in and deploy your website.</strong></p><p><br></p><p>​<img src="apin9-compressor.png" alt="apin9-compressor.png" style="margin:5px;" /><br><strong>Figure: Now when you right-click on your web project there is a new option Open Application Insights Portal...</strong></p><p><strong><br></strong></p><p><img src="apin10-compressor.png" alt="apin10-compressor.png" style="margin:5px;width:650px;" /><br><strong style="line-height:20.7999992370605px;">Figure: Dashboard showing summary and application metrics​</strong> <br></p><p><br></p><p>Once deployed, Application Insights will start tracking metrics and interacting with your Visual Studio Online dashboards.</p><p>Application Insights tracks a lot of metrics in your website but one of the most useful is the breakdown of visits by each browser (IE, Chrome etc).</p><p><img src="apin4-compressor.png" alt="apin4-compressor.png" style="margin:5px;width:650px;" /><br><strong>Figure: Breakdown of which browsers are used to access your website</strong></p><p><strong>Note: </strong> Make sure Server Performance Monitoring is set up (currently not available for Azure Websites)</p><p><img src="AnyConnect 1.png" alt="1.png" style="margin:5px;" /><br></p><p><strong>Figure: Ensure you complete this process to add Server Monitoring</strong></p><p>Sometimes you will be trying to add Application Insights to an existing project and the context menu item will not be there. There is a manual way to add Application Insights if this is the case.</p><p><img src="2014-09-05_14-49-56-compressor.png" alt="2014-09-05_14-49-56-compressor.png" style="margin:5px;" /><br><strong>Figure: Sign into Visual Studio Online, and navigate to Application Insights | Add Application</strong></p><p><br></p><p><img src="2014-09-05_14-59-06-compressor.png" alt="2014-09-05_14-59-06-compressor.png" style="margin:5px;" /><br><strong>Figure: Use these settings to generate the manual instructions</strong></p><p><br></p><p><img src="2014-09-05_15-26-32-compressor.png" alt="2014-09-05_15-26-32-compressor.png" style="margin:5px;" /><br><strong>Figure: Follow these steps to add the Application Insights JavaScript code to your website</strong></p><p><br></p>


