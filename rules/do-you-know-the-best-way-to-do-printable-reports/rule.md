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



<span class='intro'> Making reports on websites printable can be difficult. While there are CSS media and rules to help make pages printable, there are always issues with page breaks, browser quirks and tables.&#160; ​<br>
<dl class="image"><dt><img src="/PublishingImages/print-reports-bad-1.png" alt="print-reports-bad-1.png" /></dt><dd>Figure&#58; Beautiful HTML report <br></dd></dl> </span>

<dl class="badImage"><dt> <img src="/PublishingImages/print-reports-bad-2.png" alt="print-reports-bad-2.png" /> </dt><dd>Figure&#58; Bad Example – The printed layout looks nothing like the HTML</dd></dl><dl class="image"><dt> <img src="/PublishingImages/print-reports-bad-3.png" alt="print-reports-bad-3.png" /> </dt><dd>Figure&#58; Beautiful PowerBI HTML report</dd></dl><dl class="badImage"><dt> <img src="/PublishingImages/print-reports-bad-4.png" alt="print-reports-bad-4.png" /> </dt><dd>Figure&#58; Bad example – PowerBI print preview scales everything down to fit on a page, you have no real control over how things flow onto multiple pages</dd></dl><p>The best and most accurate print solution is to use SQL Server Reporting Services (SSRS). You can use SQL Server Reporting Services in MVC even though&#160;its&#160;only supported by WebForms.&#160;<br></p><p>It's great to include&#160; SQL Server Reporting Services (SSRS)&#160;reports in your web application, which can be done with the Microsoft ReportViewer web control...however this only applies to ASP.NET WebForms.</p><p>With an iframe and a little bit of code, your reports can also be viewed in your ASP.NET MVC application.</p><p>In your MVC project, add a new item of type WebForm.<br></p><dl class="image"><dt> <img src="/PublishingImages/16-06-2014%2010-44-12%20AM.png" alt="16-06-2014 10-44-12 AM.png" /> </dt><dd>Figure&#58; Add a new WebForm</dd></dl><p>Then add the ReportViewer control to the WebForm.<br></p><dl class="image"><dt> <img src="/PublishingImages/16-06-2014%2010-46-58%20AM.png" alt="16-06-2014 10-46-58 AM.png" style="width&#58;800px;" /> </dt><dd>Figure&#58; Add the ReportViewer control</dd></dl><p>In the View you want to display the report in, add an iframe pointing to your WebForm.&#160;</p><p>Tie them together, by getting your report parameters from the MVC page and appending them to the query string of the iframe URL.<br></p><p>(The below example uses JavaScript to execute this part from user input)<br></p><dl class="image"><dt> <img src="/PublishingImages/16-06-2014%2010-50-55%20AM.png" alt="16-06-2014 10-50-55 AM.png" style="width&#58;800px;" /> </dt><dd>Figure&#58; Add an iframe</dd></dl><p>Now you have your SSRS report in your MVC application.<br></p><dl class="image"><dt> <img src="/PublishingImages/17-06-2014%208-33-37%20AM.png" alt="17-06-2014 8-33-37 AM.png" /> </dt><dd>Figure&#58; The final report in an MVC application</dd></dl><dl class="image"><dt> <img src="/PublishingImages/16-06-2014%2010-38-51%20AM.png" alt="16-06-2014 10-38-51 AM.png" /> </dt><dd>Figure&#58; Export your report with the in-build SSRS functionality</dd></dl><h3 class="ssw15-rteElement-H3">When using Web-API the method above is difficult and time-consuming!</h3><dl class="image"><dt> <img src="/PublishingImages/2015-04-29_10-09-56-compressor.png" alt="2015-04-29_10-09-56-compressor.png" style="width&#58;650px;" /> </dt></dl><p>The easy solution is to render the report within the API and return it to the user&#160; as a pdf. For an example of how to implement the functionality, read the following series&#160; of&#160;articles on <a href="http&#58;//blog.chrisbriggsy.com/the-first-step-towards-integration/" target="_blank">'Integrating SSRS Web-API and AngularJS' </a>. <br></p>


