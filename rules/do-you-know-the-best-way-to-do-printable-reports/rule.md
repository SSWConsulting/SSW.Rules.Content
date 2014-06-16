---
type: rule
title: Do you know the best way to do printable reports?
uri: do-you-know-the-best-way-to-do-printable-reports
created: 2014-01-31T00:32:32.0000000Z
authors:
- id: 38
  title: Drew Robson
- id: 45
  title: Chris Briggs

---



<span class='intro'> ​​​​​​​You can use SQL Server Reporting Services in MVC even though its only supported by WebForms.​ </span>

<p>​<br>It's great to include&#160;​SQL Server Reporting Services (SSRS)&#160;reports in your web application, which can be done with the Microsoft ReportViewer web control...however this only applies to ASP.NET WebForms.</p><p>With an iframe and a little bit of code, your reports can also be viewed in your ASP.NET MVC application.</p><p>In your MVC project, add a new item of type WebForm.<br></p><p><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/16-06-2014%2010-44-12%20AM.png" alt="16-06-2014 10-44-12 AM.png" style="margin&#58;5px;" /><br></p><p><strong>Figure&#58; Add a new WebForm</strong></p><p>Then add the ReportViewer control to the WebForm.<br></p><p><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/16-06-2014%2010-46-58%20AM.png" alt="16-06-2014 10-46-58 AM.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p><strong>Figure&#58; Add the ReportViewer control</strong></p><p>In the View you want to display the report in, add an iframe pointing to your WebForm.&#160;</p><p><span style="line-height&#58;20.799999237060547px;">​T</span><span style="line-height&#58;20.799999237060547px;">ie them together, by getting your report parameters from the MVC page and appending them to the query string of the iframe URL.</span><br></p><p><span style="line-height&#58;20.799999237060547px;">(The below example uses JavaScript to execute this part from user input)</span><br></p><p><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/16-06-2014%2010-50-55%20AM.png" alt="16-06-2014 10-50-55 AM.png" style="margin&#58;5px;width&#58;650px;" />&#160;</p><p><strong>Figure&#58; Add an iframe</strong></p><p>Now you have your SSRS report in your MVC application.<br></p><p><strong style="line-height&#58;1.6;">​​<img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/17-06-2014%208-33-37%20AM.png" alt="17-06-2014 8-33-37 AM.png" style="margin&#58;5px;" />​<br>Figure&#58; The final report in an MVC application</strong></p><p><strong style="line-height&#58;1.6;"><br></strong></p><p><strong style="line-height&#58;1.6;"><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/16-06-2014%2010-38-51%20AM.png" alt="16-06-2014 10-38-51 AM.png" style="margin&#58;5px;" /><br></strong></p><p><strong style="line-height&#58;1.6;">Figure&#58; Export your report with the in-build SSRS functionality</strong></p>


