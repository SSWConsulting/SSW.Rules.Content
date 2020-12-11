---
type: rule
archivedreason: 
title: Do you use more meaningful names than Hungarian short form?
guid: 2d7b5600-f65a-4172-9656-b5a3c8a402b0
uri: do-you-use-more-meaningful-names-than-hungarian-short-form
created: 2009-05-05T07:29:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee
related: []

---

Hungarian notation is used in VB6. In .NET, there are over 35,000 classes, so we can't just call them with three letter short form. We would suggest the developer use the full class name as  in example below. As a result, the code will be much easier to read and follow up.   
<!--endintro-->
<dl class="badCode">    <dt style="width&#58;92.04%;height&#58;206px;">
    <pre>                          //Bad Code<br><br>
                          DateTime dt = new DateTime.Now();
<br>
                          DataSet ds = new DataSet();
<br>
                          // It could be confused with Date time.
<br>
                          DataTable dt = ds.Tables[0];</pre>
    &lt;/dt&gt;
    <dd>Bad code - Without meaningful name. </dd></dl><dl class="goodCode">    <dt style="width&#58;92.33%;height&#58;170px;">
    <pre>                     //Good Code<br><br>
                     DateTime currentDateTime = new DateTime.Now();
<br>
                     DataSet employmentDataSet = new DataSet();
<br>
                     DataTable ContactDetailsDataTable = ds.Tables[0];</pre>
    &lt;/dt&gt;
    <dd>Good code - With meaningful name. </dd></dl>
[More information on naming convention](http&#58;//www.ssw.com.au/ssw/Standards/DeveloperDotNet/DotNetStandard_ObjectNaming.aspx).




| We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule |
| --- |
