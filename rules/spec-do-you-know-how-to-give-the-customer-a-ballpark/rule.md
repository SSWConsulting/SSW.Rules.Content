---
type: rule
archivedreason: 
title: Spec - Do you know how to give the customer a ballpark?
guid: 1ac29d3d-fc89-462a-b0c5-d17c6889e66c
uri: spec-do-you-know-how-to-give-the-customer-a-ballpark
created: 2009-11-04T08:35:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: []
redirects: []

---


<p><strong>How to create an Estimate For a Spec Review (Summary)</strong><strong><br></strong></p>
<p>This process can take up to a few days, so if you're just after a ballpark, use epics instead of PBIs (Product Backlog Items).</p>
<ol><li>Usually using the browser, list all of the PBIs in TFS, sizing them with story points.</li>
<li>Using Visual Studio, export the list of PBIs and Story Points to Excel.</li>
<li>In Excel, add a colum called &quot;Days&quot;<br>Convert the story points to&#160;days by deciding on a scaling factor based on your team's velocity.&#160;(e.g. Days =&#160;Effort/5... assuming&#160;you get about 5 story points done per day). <br>Note&#58; Once we move to estimating in days, this is no longer Scrum.</li>
<li>In Excel, copy this list and paste into&#160;another spreadsheet called the <a href="/Management/RulesToBetterProjectManagement/Documents/SSWPrioritiesEstimatesTemplate.xlsx" shape="rect" target="_blank">Excel template calcul​ator</a>,&#160;in order to add all of the extra items (training, testing, Project management, etc.).<br>Note&#58; It would be great if TFS Web Access had functionality to add <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#StandardItems" shape="rect"><font color="#3a66cc">standard items to a Release</font></a> (aka iteration)</li>
<li>Run&#160;a <a href="/Management/RulesToSuccessfulProjects/Pages/InternalTestPlease.aspx" shape="rect">test please</a>&#160;on this.</li>
<li>Add this spreadsheet to your specification review document.</li>
<li>When the Estimate is approved by the client,&#160;start work following these rules&#58;&#160;<a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterProjectManagementWithTFS.aspx" shape="rect">Rules to Better Project Management with TFS</a>. </li></ol>
TODO - Ask Eric - We also set&#160;our SharePoint document library's default template to be this file to allow developers to find it easily. ​​​
<br><excerpt class='endintro'></excerpt><br>
<p><font class="ms-rteCustom-GreyBox"><p><strong><strong><strong><strong>Why Microsoft Project isn't recommended</strong></strong></strong></strong></p>
<ul><li>Tasks are auto scheduled based on dependency and resource allocation (who is assigned to it). This generates an estimated completion date which is never accurate, due to annual leave, public holidays and general shuffling of people in the team </li>
<li>It gets the summing wrong (the totals don't seem to update and no way to trigger it) </li>
<li>It's hard to synchronize with timesheets (as it doesn't connect to 3rd party timesheet systems out of the box – however, it does have&#160;its own time sheeting system, that is missing billing information!) </li>
<li><s>You cannot allocate two people to a task. This create a lot of additional overhead to get it right. **fixed in TFS 2008**</s> </li></ul></font></p>
<p><strong>How to create a Release Plan<br></strong><br><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Use SharePoint Document Library Template for creating consistent ballpark</font><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate-Instructions.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Read the instructions about how to use this template</font> <br><br><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate-MenuCalc.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Use Menu Calculator to understand the common estimates</font> <br><br><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate-Resources.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Use Resources sheet to assign resources</font> <br><br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate-Ballpark.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Use the Release sheet to enter all the work items and calculate ballpark</font> <br>Finally, you should copy and paste this Release sheet into an email and send to your client. Before that, make sure&#160;you talk your client through it first. <br><br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/SSWBallPark-SharePointTemplate-Email.jpg" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Send the ballpark by Email</font>&#160;&#160;&#160;&#160;&#160;<br><br><strong>Winning the Project- Publish these Work Items to TFS</strong></p>
<ol><li>&#160;Open Visual Studio </li>
<li>&#160;Create a new Project in Team Explorer </li></ol>
<p><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/CreateNewProjectInTE.jpg" alt="" />&#160;</p>
<p>&#160;&#160;&#160; 3. &#160;Define new Iterations<br><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/AreasAndIterations.jpg" alt="" /><br><font class="ms-rteCustom-FigureNormal">Figure&#58; Accessing the Areas and Iterations menu from your project in Team Explorer<br></font><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/NamedIterations.jpg" alt="" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Add appropriate named iterations<br></font><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;4.&#160;In SharePoint, open your Release Summary<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;5.&#160;Create a new Worksheet in the same Workbook for your release plan. Rename&#160; it to &quot;TFS Work Items&quot;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 6.&#160;From the &quot;Team&quot; ribbon tab, click &quot;New List&quot;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 7.&#160;Select the Team Project you Created<br><img class="ms-rteCustom-ImageArea" src="/Management/RulesToBetterProjectManagement/PublishingImages/TeamProjectYouCreate.jpg" alt="" /><br><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;8.&#160;Click &quot;Input List&quot;. This will connect Excel to TFS, and allow you to enter Work Items to be published<br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/InputList.jpg" alt="" /><br><br>&#160;&#160;&#160; After you do this, it will generate a worksheet that looks like this&#58;<br><br><br>&#160;&#160;&#160; 9.&#160;Click &quot;Choose Columns&quot;, and make sure these columns are selected in the following order&#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; a.&#160;ID (will be included automatically);<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; b.&#160;Title<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; c.&#160;Baseline Work<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; d.&#160;Work&#160; Item Type<br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/ChooseColumns.jpg" alt="" /><br><br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/Columns.jpg" alt="" /><br><br><br>&#160;&#160;&#160; 10.&#160;Copy the first four columns of the release summary onto a blank section of the TFS Work Items work sheet<br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/CopyColumnsToWorksheet.jpg" alt="" /><br><br>&#160;&#160;&#160; 11.&#160;Delete the Resources and Hours per resource column<br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/DeleteRHColumn.jpg" alt="" /></p>
<p>&#160;&#160;&#160; 12.&#160;Cut the Task and Man Hours column and paste it into the input list. You MUST use “Paste-Special”, and select Values, otherwise you will get an error.</p>
<p>&#160;&#160;&#160; 13.&#160;Set the &quot;Work Item Type&quot;&#58;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; a.&#160;Subheading/Categories are considered &quot;Scenarios&quot; in TFS<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; b.&#160;Work Items are set as &quot;Task&quot;</p>
<p>&#160;&#160;&#160; 14.&#160;Click the &quot;Publish&quot; button from the ribbon. <br><img src="/Management/RulesToBetterProjectManagement/PublishingImages/ClickPublish.jpg" alt="" /></p>
<br>


