---
type: rule
archivedreason: 
title: Do you know the best way to do printable reports?
guid: beb3aa9f-57f8-4154-9acb-9ce5d70e9ded
uri: do-you-know-the-best-way-to-do-printable-reports
created: 2014-01-31T00:32:32.0000000Z
authors:
- id: 38
  title: Drew Robson
- id: 45
  title: Chris Briggs
related: []

---

Making reports on websites printable can be difficult. While there are CSS media and rules to help make pages printable, there are always issues with page breaks, browser quirks and tables.  
<dl class="image">&lt;dt&gt;<img src="print-reports-bad-1.png" alt="print-reports-bad-1.png">&lt;/dt&gt;<dd>Figure: Beautiful HTML report <br></dd></dl>
<!--endintro-->
<dl class="badImage">&lt;dt&gt; <img src="print-reports-bad-2.png" alt="print-reports-bad-2.png"> &lt;/dt&gt;<dd>Figure: Bad Example – The printed layout looks nothing like the HTML</dd></dl><dl class="image">&lt;dt&gt; <img src="print-reports-bad-3.png" alt="print-reports-bad-3.png"> &lt;/dt&gt;<dd>Figure: Beautiful PowerBI HTML report</dd></dl><dl class="badImage">&lt;dt&gt; <img src="print-reports-bad-4.png" alt="print-reports-bad-4.png"> &lt;/dt&gt;<dd>Figure: Bad example – PowerBI print preview scales everything down to fit on a page, you have no real control over how things flow onto multiple pages</dd></dl>
The best and most accurate print solution is to use SQL Server Reporting Services (SSRS). You can use SQL Server Reporting Services in MVC even though its only supported by WebForms.

It's great to include  SQL Server Reporting Services (SSRS) reports in your web application, which can be done with the Microsoft ReportViewer web control...however this only applies to ASP.NET WebForms.

With an iframe and a little bit of code, your reports can also be viewed in your ASP.NET MVC application.

In your MVC project, add a new item of type WebForm.
<dl class="image">&lt;dt&gt; <img src="16-06-2014 10-44-12 AM.png" alt="16-06-2014 10-44-12 AM.png"> &lt;/dt&gt;<dd>Figure: Add a new WebForm</dd></dl>
Then add the ReportViewer control to the WebForm.
<dl class="image">&lt;dt&gt; <img src="16-06-2014 10-46-58 AM.png" alt="16-06-2014 10-46-58 AM.png" style="width:800px;"> &lt;/dt&gt;<dd>Figure: Add the ReportViewer control</dd></dl>
In the View you want to display the report in, add an iframe pointing to your WebForm.

Tie them together, by getting your report parameters from the MVC page and appending them to the query string of the iframe URL.

(The below example uses JavaScript to execute this part from user input)
<dl class="image">&lt;dt&gt; <img src="16-06-2014 10-50-55 AM.png" alt="16-06-2014 10-50-55 AM.png" style="width:800px;"> &lt;/dt&gt;<dd>Figure: Add an iframe</dd></dl>
Now you have your SSRS report in your MVC application.
<dl class="image">&lt;dt&gt; <img src="17-06-2014 8-33-37 AM.png" alt="17-06-2014 8-33-37 AM.png"> &lt;/dt&gt;<dd>Figure: The final report in an MVC application</dd></dl><dl class="image">&lt;dt&gt; <img src="16-06-2014 10-38-51 AM.png" alt="16-06-2014 10-38-51 AM.png"> &lt;/dt&gt;<dd>Figure: Export your report with the in-build SSRS functionality</dd></dl>
### When using Web-API the method above is difficult and time-consuming!
<dl class="image">&lt;dt&gt; <img src="2015-04-29_10-09-56-compressor.png" alt="2015-04-29_10-09-56-compressor.png" style="width:650px;"> &lt;/dt&gt;</dl>
The easy solution is to render the report within the API and return it to the user  as a pdf. For an example of how to implement the functionality, read the following series  of articles on ['Integrating SSRS Web-API and AngularJS'](http://blog.chrisbriggsy.com/the-first-step-towards-integration/).
