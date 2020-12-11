---
type: rule
archivedreason: 
title: Menu - Do you include a "Tools | Validate Data"?
guid: 8afbe219-50fc-439c-a866-df3f4e085221
uri: menu---do-you-include-a-tools--validate-data
created: 2012-11-27T02:53:35.0000000Z
authors: []
related: []

---


<p>A common oversight is applications don't check for invalid data. You should add "Tools | Validate Data" to your application.</p>
<br><excerpt class='endintro'></excerpt><br>
​<div>So when you add business rules to the middle tier, consider scenarios such as importing data and any other areas that side step business rules. Therefore we always make validate queries that if they return records, they must be fixed. Examples are:</div>
<ul><li>For SQL Server we use <strong>vwValidateClient_MustHaveACategoryID</strong>, or <strong>procValidateClient_MustHaveACategoryID</strong></li>
<li>For Access we use <strong>qryValidateClient_MustHaveACategoryID</strong></li></ul>
<dl class="goodImage"><dt><img alt="Data Validation" src="../../assets/TimeProValidateData.png" /></dt>
<dd>Figure: Good Example - This application, while not the prettiest, has a handy validation tool to check for incorrect data</dd></dl>
<h1>Related Links</h1>
<div><a href="/do-you-validate-each-＂denormalized-field＂-with-procvalidate">Do you validate each "Denormalized Field" with procValidate?</a></div>



