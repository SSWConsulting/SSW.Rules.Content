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


​​​​​​You can use SQL Server Reporting Services in MVC even though its only supported by WebForms.​
<br><excerpt class='endintro'></excerpt><br>
<p>​</p><p>​SQL Server Reporting Services reports can be viewed in a web page with the ReportViewer&#160;control...however this only applies to ASP.NET WebForms.</p><p>​However, with an iframe and a little bit of code, your reports can be viewed in your ASP.NET MVC application.<br></p><p>In your MVC project, add a new item of type WebForm.<br></p><p>​Add the ReportViewer control.<br></p><p>In the MVC view you want to display the report in, add an iframe pointing to this WebForm.</p><p>Now to tie them together, by getting your report parameters from the MVC page and appending them to the query string of the iframe URL.</p>


