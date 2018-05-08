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



<span class='intro'> <p>During the&#160;migration the site can't be locked if you are&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=4ee88718-590a-43fe-bbd8-4557633d1d6f">using Sharegate</a>, there is a chance that employees will ignore the instructions in the ribbon and still make changes. <br></p><p>​Furthermore, they might also be automated processes that are putting records in your old SharePoint Server. <br></p><p>So to ensure the migration process did not miss any items, ensure nobody modified documents on your old Intranet SharePoint Server. To do that&#58;<br></p> </span>

<ol><li>​​<span style="color&#58;#444444;">Navigate to &quot;Site Settings&quot; | &quot;Audit log reports&quot; which will take you there&#58;&#160;&#160;</span><br>
      <dl class="image"><dt> <img src="/PublishingImages/no-intranet-modifications.jpg" alt="no-intranet-modifications.jpg" /> </dt><dd>Figure&#58; check nobody was modifying the intranet during the long migration<br></dd></dl></li><li>Click &quot;Content Modifications&quot;</li><li>Order the generated Excel data by modification date (&quot;Occurred&quot; ) and look for modifications done by users.</li><li>Chase the people who did the modifications and ask them either to&#58; <br> 
      <p></p><ul><li>Redo their modification in your new Cloud intranet (likely)<br></li><li>Confirm that the modification is not important and does not require manual migration (less likely)<p class="ssw15-rteElement-GreyBox">Hey xxx,<br><br>I have noticed that you changed the file “yyy” (link to the file&#58; https&#58;//zzz.sharepoint.com/yyy.pdf).<br>Could you please&#58;<br>1. Let me know what were the changes?​<br>2. Tell me why you did these changes (task, etc…)?<br><br>Please note that these changes will be lost as part of the old SharePoint server decommission. If the changes are important, please redo the modifications on the new Online Intranet.<br>Regards,<br><br>-SharePoint Admin Team</p>​<br></li></ul><p>After you export to Excel, follow this example&#58;</p><dl class="image"><dt> <img src="/PublishingImages/old-sharepoint-modification.jpg" alt="old-sharepoint-modification.jpg" /> </dt><dd>Figure&#58; Modifications are done on the old SharePoint intranet during the migration process (hence not migrated to the cloud)</dd></dl><p>
         <b><span style="color&#58;#008000;">Green&#58;</span>&#160;</b>non-important data (automated logging info) - ignore</p><p>
         <b><span style="color&#58;#cc9900;"><span style="color&#58;#cc9900;">Orange&#58;</span></span> </b>potentially important data (user made changes) – ask the user</p><p>
         <span style="color&#58;#cc0000;"><b>Red&#58;</b></span> critical data (invoices !) – Migrate these documents&#160;<br></p></li></ol> 
<br>


