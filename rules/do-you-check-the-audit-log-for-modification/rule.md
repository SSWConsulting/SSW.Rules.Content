---
type: rule
title: Do you check the audit log for modification?
uri: do-you-check-the-audit-log-for-modification
created: 2018-05-04T23:38:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 69
  title: Jean Thirion

---



<span class='intro'> <p>Because the site can't be locked using Sharegate (see rule number X), there is a chance that employees will ignore the instructions in the ribbon and still make changes.</p><p>Furthermore, they might also be automated processes that are putting records in your old SharePoint Server.​<br></p><p>So to ensure the migration process did not miss any items, ensure nobody modified documents on your old Intranet SharePoint Server. To do that&#58;<br></p> </span>

<ol><li>​​<span style="color&#58;#444444;">Navigate to “Site Settings&quot; | “Audit log reports&quot; which will take you there&#58;&#160;&#160;</span><br> 
      <dl class="image"><dt><img src="/PublishingImages/no-intranet-modifications.jpg" alt="no-intranet-modifications.jpg" /></dt><dd>Figure&#58; check nobody was modifying the intranet during the long migration</dd></dl>
      <p>Click &quot;Content Modifications&quot;</p></li><li>Order the generated Excel data by modification date (“Occurred”) and look for modifications done by users.</li><li>Chase the people who did the modifications and ask them either to&#58; <br>
      <p></p><ul><li>Redo their modification in your new Cloud intranet (likely)<br></li><li>Confirm that the modification is not important and does not require manual migration (less likely)<br></li></ul><p>Example&#58;</p><dl class="image"><dt><img src="/PublishingImages/old-sharepoint-modification.jpg" alt="old-sharepoint-modification.jpg" /></dt><dd>Figure&#58; Modifications are done on the old SharePoint intranet during the migration process (hence not migrated to the cloud)</dd></dl><p><b><span style="color&#58;#008000;">Green&#58;</span>&#160;</b>non-important data (automated logging info) - ignore</p><p><b><span style="color&#58;#cc9900;"><span style="color&#58;#cc9900;">Orange&#58;</span></span> </b>potentially important data (user made changes) – ask the user</p><p><span style="color&#58;#cc0000;"><b>Red&#58;</b></span> critical data (invoices !) – Migrate these documents&#160;<br></p></li></ol>
<br>


