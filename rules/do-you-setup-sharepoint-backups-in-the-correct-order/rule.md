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
To back up the SharePoint Server properly in DPM&#58;
<div><br>
</div>
<div>
<ol>
    <li>Create a new Protection Group, for our example we will call it SharePoint Protection</li>
    <li>In the new Protection Group, add protection for the for the SharePoint role on your SharePoint server&#58;<br>
    <br>
    </li>
</ol>
</div>



