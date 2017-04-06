---
type: rule
archivedreason: 
title: Do you know how to handover a project?
guid: 15b06388-5103-45e4-a5ea-96c13554df77
uri: do-you-know-how-to-handover-a-project
created: 2010-03-15T06:22:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 13
  title: Paul Neumeyer
related: []

---


<p>A common source of pain, is picking up a project without a decent/complete handover. To have a successful project you must navigate over the problem of changing resources/people&#160;leaving etc.<br></p><p>Always ensure that you&#160;complete the following checklist and <em>always </em>send the email confirming the handover is complete.</p><p>Here are the&#160;8 steps you should follow for a good handover. <br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>Confirm current tasks</li><li>Confirm future tasks</li><li>Confirm the primary contacts</li><li>Do a code review</li><li>Review the client portal</li><li>Confirm location of info and procedures (hopefully, these are on a wiki or SharePoint document library)<ul><li>Source control</li><li>Database</li><li>Documents</li><li>How to Build and Package</li><li>Testing&#160;Steps&#160;and&#160;users and passwords to access&#160;the test and staging servers&#160;&#160;</li><li>Deployment Steps</li><li>Servers and Passwords</li><li>Failure &amp; Recovery Steps</li></ul></li><li>Test that the users, passwords, URLs and server details provided in the handover are correct by logging in with each</li><li>Complete the Handover by sending an email with&#58; As per our meeting the handover has been completed to my satisfaction</li></ol>
<font class="ms-rteCustom-GreyBox"> <p> 
      <b>From&#58;&#160;Andy<br>To&#58;&#160;Gracia<br>Subject&#58;&#160;SSW - Northwind handover</b></p>
   <p>Done</p>
   <ul><li> 
         <strong>Confirm outstanding tasks </strong>
         <p>Nothing.<br></p></li><li> 
         <strong>Confirm planned tasks </strong>
         <p>Get release 43 out.</p></li><li> 
         <strong>Confirm location </strong>
         <ul><li>Source control<p>Nothing</p></li><li>Data storage<p> 
                  <a shape="rect">file&#58;//server/DataSSW/SSWProducts/Northwind</a></p></li><li>Deployment<p>Make a build by using WISE<br>Test&#58;&#160;seadragon<br>Production&#58;&#160;squirrel</p></li><li>Failure &amp; Recovery<p>Do not work on the Master folder, work on local machine. If it has some issue, grab the file from master folder.<br>Always backup master folder’s file before uploading the changes to the master folder</p></li></ul></li><li> 
         <strong>Update the Employee Responsibilities in SSW intranet </strong>
         <p> 
            <b>TODO</b> </p></li></ul> </font> <strong class="ms-rteCustom-FigureBad">Figure Bad Example - This handover is incomplete and light on details</strong> <br><font class="ms-rteCustom-GreyBox"> <p> 
      <b>From&#58;&#160;Andy<br>To&#58; Gracia<br>Subject&#58;&#160;SSW - Northwind Handover</b> </p>
   <p>Done -&#160;As per our meeting the handover has been completed to my satisfaction <br></p>
   <ul><li> 
         <strong>Confirm outstanding tasks </strong>
         <p>Nothing.</p></li><li> 
         <strong>Confirm planned tasks </strong>
         <p>Next release is Release 43.<br>The aim of&#160;this release is to improve&#160;the reporting available from the management module with chart reports<br>Query&#160;= tfs\Northwind\Work Items\Team Queries\All Work Items - R43 - Management Module Reporting</p><p>Backlog is in TFS.<br>Query = tfs\Northwind\Work Items\Team Queries\All Work Items - Backlog</p></li><li> 
         <strong>Confirm location </strong>
         <ul><li>Source control<p>
                  <a shape="rect">file&#58;//tfs.ssw.com.au/tfs/Northwind</a></p></li><li>Data storage<p> 
                  <a shape="rect">file&#58;//server/DataSSW/SSWProducts/North wind</a></p></li><li>Deployment<ul><li>Make a build by using WISE</li><li>Test db to connect to&#58;<p>server&#58; seadragon<br>database&#58; SSWNorthwind_test</p></li><li>Production db to connect to&#58;<p>server&#58; squirrel<br>database&#58; SSWNorthwind&#160;<br></p></li></ul></li><li>Failure &amp; Recovery<p>Do not work on the Master folder, work on a local machine. If it has some issue, grab the file from the master folder.<br>Always backup master folder’s file before uploading the changes to the master folder.<br>If a problem occurs, restore the backup of the master folder and restart<br></p></li></ul></li><li> 
         <strong>Update the Employee Responsibilities in SSW intranet </strong>
         <p>DONE</p></li><li> 
         <strong>Complete Handover </strong></li></ul> </font> <strong class="ms-rteCustom-FigureGood">Figure&#58; Good Example - This handover has lots of URLs and is complete</strong><br>
<p>If you need to handover only a single task there are more details here&#58;&#160;<a shape="rect" href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2586b50a-21b6-40b0-8004-d90d1b029bec">Do you know how to hand over tasks (aka Emails) to others? ​</a><br></p>


