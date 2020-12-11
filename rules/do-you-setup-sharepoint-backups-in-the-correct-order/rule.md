---
type: rule
archivedreason: 
title: Do you setup SharePoint backups in the correct order?
guid: bd877a4f-5a2c-46e0-95db-07d432c0ab07
uri: do-you-setup-sharepoint-backups-in-the-correct-order
created: 2011-06-15T00:50:23.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---


DPM is great for backing up SharePoint data, but when you select to back up the SharePoint role of a server, DPM will only backup the SharePoint_Config database and the content databases, which is less than ideal. 

<br><excerpt class='endintro'></excerpt><br>
To back up the SharePoint Server properly in DPM:
<div><br>
</div>
<div>
<ol>
    <li>Create a new Protection Group, for our example we will call it <strong>SharePoint Protection </strong></li>
    <li>In the new Protection Group, add protection for the for the SharePoint role on your SharePoint server:<br>
    <br>
    <img alt="Notice that SharePoint protection only selects the SharePoint_Config and Content databases." src="dpm-spcorrectorder-1.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Notice that SharePoint protection only selects the SharePoint_Config and Content databases.</font></li>
    <li>Now browse to the SQL Server and add the entire SharePoint SQL Instance to the <strong>SharePoint Protection</strong> group. You will notice that you are unable to select some of the databases, as they are already being protected by SharePoint role protection.<br>
    <br>
    <img alt="Ensure you back up the remaining databases in the SharePoint SQL Instance" src="dpm-spcorrectorder-2.png" /><br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Ensure you back up the remaining databases in the SharePoint SQL Instance</font></li>
    <br>
</ol>
After following these steps you will have full protection of your SharePoint databases. </div>



