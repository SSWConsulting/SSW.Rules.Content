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


A common source of pain, is picking up a project without a decent/complete handover. To have a successful project you must navigate over the problem of changing resources/people&#160;leaving etc.<br>
<br>
Always ensure that you&#160;complete the following checklist and <em>always </em>send the email confirming the handover is complete.&#160;<br>
<br>
Here are the 7 steps you should follow for a good handover. &#160; &#160; 

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Confirm current tasks </li>
    <li>Confirm future tasks </li>
    <li>Confirm the primary contacts </li>
    <li>Do a code review </li>
    <li>Review the client portal </li>
    <li>Confirm location of info and procedures (hopefully these are on a wiki or SharePoint document library)
    <ul>
        <li>Source control </li>
        <li>Documents </li>
        <li>Deployment Steps </li>
        <li>Servers and Passwords </li>
        <li>Failure &amp; Recovery Steps </li>
    </ul>
    </li>
    <li>Complete Handover by sending an email with&#58; As per our meeting the handover has been completed to my satisfaction </li>
</ol>
<font class="ms-rteCustom-GreyBox">
<p><b>From&#58;&#160;Andy<br>
To&#58;&#160;Gracia<br>
Subject&#58;&#160;SSW - Northwind handover</b></p>
<p>Done</p>
<ul>
    <li><strong>Confirm outstanding tasks </strong>
    <p>Nothing.</p>
    </li>
    <li><strong>Confirm planned tasks </strong>
    <p>Get release 43 out.</p>
    </li>
    <li><strong>Confirm location </strong>
    <ul>
        <li>Source control
        <p>Nothing</p>
        </li>
        <li>Data storage
        <p><a shape="rect" href="file&#58;//server/DataSSW/SSWProducts/Northwind">file&#58;//server/DataSSW/SSWProducts/Northwind</a></p>
        </li>
        <li>Deployment
        <p>Make a build by using WISE<br>
        Test&#58;&#160;seadragon<br>
        Production&#58;&#160;squirrel</p>
        </li>
        <li>Failure &amp; Recovery
        <p>Do not work on the Master folder, work on local machine. If it has some issue, grab the file from master folder.<br>
        Always backup master folder’s file before uploading the changes to the master folder </p>
        </li>
    </ul>
    </li>
    <li><strong>Update the Employee Responsibilities in SSW intranet </strong>
    <p><b>TODO</b> </p>
    </li>
</ul>
</font><strong class="ms-rteCustom-FigureBad">Figure Bad Example - This handover is incomplete and light on details</strong> <br>
<br>
<font class="ms-rteCustom-GreyBox">
<p><b>From&#58;&#160;Andy<br>
To&#58; Gracia<br>
Subject&#58;&#160;SSW - Northwind Handover</b> </p>
<p>DONE -&#160;As per our meeting the handover has been completed to my satisfaction</p>
<p>&#160;</p>
<ul>
    <li><strong>Confirm outstanding tasks </strong>
    <p>Nothing.</p>
    </li>
    <li><strong>Confirm planned tasks </strong>
    <p>Next release is Release 43.<br>
    The aim of&#160;this release is to improve&#160;the reporting available from the management module with chart reports<br>
    Query&#160;= tfs\Northwind\Work Items\Team Queries\All Work Items - R43 - Management Module Reporting</p>
    <p>Backlog is in TFS.<br>
    Query = tfs\Northwind\Work Items\Team Queries\All Work Items - Backlog</p>
    </li>
    <li><strong>Confirm location </strong>
    <ul>
        <li>Source control
        <p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<a shape="rect">file&#58;//tfs.ssw.com.au/tfs/Northwind</a></p>
        </li>
        <li>Data storage
        <p><a shape="rect">file&#58;//server/DataSSW/SSWProducts/Norwind</a></p>
        </li>
        <li>Deployment
        <ul>
            <li>Make a build by using WISE </li>
            <li>Test db to connect to&#58;
            <p>server&#58; seadragon<br>
            database&#58; SSWNorthwind_test</p>
            </li>
            <li>Production db to connect to&#58;
            <p>server&#58; squirrel<br>
            database&#58; SSWNorthwind&#160;</p>
            </li>
        </ul>
        </li>
        <li>Failure &amp; Recovery
        <p>Do not work on the Master folder, work on local machine. If it has some issue, grab the file from master folder.<br>
        Always backup master folder’s file before uploading the changes to the master folder.<br>
        If a problem occurs restore the backup of the master folder and restart</p>
        </li>
    </ul>
    </li>
    <li><strong>Update the Employee Responsibilities in SSW intranet </strong>
    <p>DONE</p>
    </li>
    <li><strong>Complete Handover </strong></li>
</ul>
</font><strong class="ms-rteCustom-FigureGood">Figure&#58; Good Example - This handover has lots of URLs and is complete</strong><br>
<p>If you need to handover only a single task there are more details here&#58;<br>
<a shape="rect" href="/Standards/Communication/RulesToBetterEmail/Pages/HandOverTask.aspx">http&#58;//sharepoint.ssw.com.au/Standards/Communication/RulesToBetterEmail/Pages/HandOverTask.aspx</a></p>



