---
type: rule
archivedreason: 
title: Do you stop dealing with Data and Schema?
guid: d8a098fd-b81e-4f70-92ae-c03af30915f5
uri: do-you-stop-dealing-with-data-and-schema
created: 2009-03-10T06:36:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


<p>Why don't most developers plan ahead? Take an average VB or Access application that you sell to a few customers. When the customer wants a new version, there is no problem giving the customer the new mdb or exe. But what if you made a back-end structural <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/DataSchemaStandard.aspx"> changes to your database</a>? Big hassle! You need to compare the database to remind you what was changed. Sure there are utilities for this - for Access backends you can use <a href="http&#58;//www.ssw.com.au/ssw/DataRenovator/Default.aspx">SSW Data Renovator</a> or for SQL Server backends there is <a href="http&#58;//www.ssw.com.au/ssw/Redirect/RedGateSQLDataCompare.htm" target="_blank">Red-gate SQL Compare</a>  - but why go to this trouble?</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Take a version control approach. It doesn't have to be too complicated, but you should keep a history of structure changes in a table. Some developers <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLServerDatabases.aspx#General">use a text file (.sql)</a> or hardcode it in code, that's fine, just don't make changes in the interface (i.e.. Access or Enterprise Manager). Changes should be made programmatically, or in a method that they can be played back.</p><p>An assumption to this is you have a front-end and backend table that is used to record the version number.</p> 
<img border="0" src="/PublishingImages/imgTableWithCrossThroughIt.gif" alt="Table with cross through it" class="ms-rteCustom-ImageArea" style="border-width&#58;0px;border-style&#58;solid;border-color&#58;initial;width&#58;330px;height&#58;282px;" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Never make a change manually in Enterprise Manager or Access </span> <img border="0" src="/PublishingImages/SaveChangeScript.gif" alt=" " class="ms-rteCustom-ImageArea" style="border-width&#58;0px;border-style&#58;solid;border-color&#58;initial;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Always save your changes in script</span> <img border="0" src="/PublishingImages/ChangeScripts.gif" alt=" " class="ms-rteCustom-ImageArea" style="border-width&#58;0px;border-style&#58;solid;border-color&#58;initial;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Name them in the order they're executed </span> <img border="0" src="/PublishingImages/SampleTable.gif" alt=" " class="ms-rteCustom-ImageArea" style="border-width&#58;0px;border-style&#58;solid;border-color&#58;initial;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; An example of a backend table recording the version numbers </span> 
<p>
   <b>Tip&#58;</b> If you’re using Next Gen and you’re changing just one table, then just regenerate for that table</p><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="http&#58;//www.ssw.com.au/ssw/SQLDeploy/Default.aspx">SSW SQL Deploy</a> to solve this problem and automatically make schema changes.</p> 


