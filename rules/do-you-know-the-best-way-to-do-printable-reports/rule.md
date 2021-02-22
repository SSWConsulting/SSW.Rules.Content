---
type: rule
archivedreason: 
title: Do you know the best way to do printable reports?
guid: beb3aa9f-57f8-4154-9acb-9ce5d70e9ded
uri: do-you-know-the-best-way-to-do-printable-reports
created: 2014-01-31T00:32:32.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
related: []
redirects: []

---


Making reports on websites printable can be difficult. While there are CSS media and rules to help make pages printable, there are always issues with page breaks, browser quirks and tables.  ​<br>
<dl class="image"><dt><img src="print-reports-bad-1.png" alt="print-reports-bad-1.png" /></dt><dd>Figure: Beautiful HTML report <br></dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt> <img src="print-reports-bad-2.png" alt="print-reports-bad-2.png" /> </dt><dd>Figure: Bad Example – The printed layout looks nothing like the HTML</dd></dl><dl class="image"><dt> <img src="print-reports-bad-3.png" alt="print-reports-bad-3.png" /> </dt><dd>Figure: Beautiful PowerBI HTML report</dd></dl><dl class="badImage"><dt> <img src="print-reports-bad-4.png" alt="print-reports-bad-4.png" /> </dt><dd>Figure: Bad example – PowerBI print preview scales everything down to fit on a page, you have no real control over how things flow onto multiple pages</dd></dl><p>The best and most accurate print solution is to use SQL Server Reporting Services (SSRS). You can use SQL Server Reporting Services in MVC even though its only supported by WebForms. <br></p><p>It's great to include  SQL Server Reporting Services (SSRS) reports in your web application, which can be done with the Microsoft ReportViewer web control...however this only applies to ASP.NET WebForms.</p><p>With an iframe and a little bit of code, your reports can also be viewed in your ASP.NET MVC application.</p><p>In your MVC project, add a new item of type WebForm.<br></p><dl class="image"><dt> <img src="16-06-2014 10-44-12 AM.png" alt="16-06-2014 10-44-12 AM.png" /> </dt><dd>Figure: Add a new WebForm</dd></dl><p>Then add the ReportViewer control to the WebForm.<br></p><dl class="image"><dt> <img src="16-06-2014 10-46-58 AM.png" alt="16-06-2014 10-46-58 AM.png" style="width:800px;" /> </dt><dd>Figure: Add the ReportViewer control</dd></dl><p>In the View you want to display the report in, add an iframe pointing to your WebForm. </p><p>Tie them together, by getting your report parameters from the MVC page and appending them to the query string of the iframe URL.<br></p><p>(The below example uses JavaScript to execute this part from user input)<br></p><dl class="image"><dt> <img src="16-06-2014 10-50-55 AM.png" alt="16-06-2014 10-50-55 AM.png" style="width:800px;" /> </dt><dd>Figure: Add an iframe</dd></dl><p>Now you have your SSRS report in your MVC application.<br></p><dl class="image"><dt> <img src="17-06-2014 8-33-37 AM.png" alt="17-06-2014 8-33-37 AM.png" /> </dt><dd>Figure: The final report in an MVC application</dd></dl><dl class="image"><dt> <img src="16-06-2014 10-38-51 AM.png" alt="16-06-2014 10-38-51 AM.png" /> </dt><dd>Figure: Export your report with the in-build SSRS functionality</dd></dl><h3 class="ssw15-rteElement-H3">When using Web-API the method above is difficult and time-consuming!</h3><dl class="image"><dt> <img src="2015-04-29_10-09-56-compressor.png" alt="2015-04-29_10-09-56-compressor.png" style="width:650px;" /> </dt></dl><p>The easy solution is to render the report within the API and return it to the user  as a pdf. For an example of how to implement the functionality, read the following series  of articles on <a href="http://blog.chrisbriggsy.com/the-first-step-towards-integration/" target="_blank">'Integrating SSRS Web-API and AngularJS' </a>. <br></p>


