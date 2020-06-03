---
type: rule
title: Do you use Report Server Project?
uri: do-you-use-report-server-project
created: 2018-12-04T21:54:10.0000000Z
authors:
- id: 34
  title: Brendan Richards
- id: 84
  title: Patricia Barros

---



<span class='intro'> <p>​When working with SSRS reports, you need to have the right type of project otherwise it will be difficult for a developer, to create new reports or update existing ones.<br></p><p>If you have some reports and want to check them into source control, if you add them to project that is not a report project, your reports will not open in the design/preview view (allowing to see the DataSource and DataSets). They will open in the XML view (which is not pretty to work with).</p> </span>

<dl class="badImage"><dt><img src="/PublishingImages/report-server-project1.png" alt="report-server-project1.png" /></dt><dd>Figure&#58; Bad example – C# project with reports opening as XML</dd></dl><p>To open the reports in the right view you will need to&#58;</p><ol><li>Be sure that you VS has the tool/extensions Microsoft Reporting Services Projects installed, go to <b>Tools</b> | <b>Extensions and Updates</b> | <b>Online</b>,&#160;and search for services<br>
<dl class="image"><dt><img src="/PublishingImages/report-server-project2.png" alt="report-server-project2.png" /></dt><dd>Figure&#58; Checking Microsoft Reporting Services Projects is installed</dd></dl><ul><li>In the micros&#160;Microsoft Download and install <a href="https&#58;//docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-2017">SQL Server Data Tools (SSDT) for Visual Studio website</a> you will find all the instructions to install the tool via Marketplace or SSDT standalone installer.</li></ul></li><li>Create the project selecting <b>Business Intelligence</b> | <b>Reporting Services </b>| <b>Report Server Project</b><br>
<dl class="image"><dt><img src="/PublishingImages/report-server-project3.png" alt="report-server-project3.png" /></dt></dl></li><li>Add existing reports and create your new DataSource (based in the information on your Report Portal)<br>
<dl class="goodImage"><dt><img src="/PublishingImages/report-server-project4.png" alt="report-server-project4.png" /></dt><dd>Figure&#58; Good Example – Report Server project with reports opening in the design/preview view </dd></dl></li></ol><br>


