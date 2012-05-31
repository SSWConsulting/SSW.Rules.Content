---
type: rule
archivedreason: 
title: Do you confirm there is no checked out data?
guid: 12122af0-1a73-42e8-aa52-6fcc520c5cc7
uri: do-you-confirm-there-is-no-checked-out-data
created: 2012-05-31T03:08:59.0000000Z
authors:
- id: 70
  title: Greg Harris
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin
related: []

---


<p>Pages in SharePoint are easily checked out, and the changes not checked-in will not be migrated when you do migration for SharePoint data.</p>
<p>In SSW, we have two ways to check the &quot;checked out files&quot; regularly&#58;</p>
<ul><li><strong>A. Manage Content and Structure Report (No Code)</strong></li>
<li><strong><strong>B. Custom application report (Includes some coding work)</strong></strong></li></ul>
<br><excerpt class='endintro'></excerpt><br>
​ <div><strong>A. Manage Content and Structure Report (No Code)</strong></div>
<div>1. Create CAML query in site content and structure</div>
<div>Go to &quot;Site Settings | Manage Content and Structure | Content and Structure Reports&quot;, click &quot;New&quot;&#58;</div>
<div><img class="ssw-rteStyle-ImageArea" alt="ContentAndStructureReportsNew.png" src="/ITAndNetworking/SharePointMigration/PublishingImages/ContentAndStructureReportsNew.png" style="margin&#58;5px;" /></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Create a new report</span> <div><span>Fill the</span><span>&#160;&quot;CAML Query&quot;&#58;</span> <div class="ssw-rteStyle-CodeArea">&lt;Where&gt;&lt;IsNotNull&gt;&lt;FieldRef Name=&quot;CheckoutUser&quot; LookupId=&quot;TRUE&quot;/&gt;&lt;/IsNotNull&gt;&lt;/Where&gt;</div>
<div>&#160;</div></div>
<div>Fill the other fields like below&#58;</div>
<div><img class="ssw-rteStyle-ImageArea" alt="NewReportForm.png" src="/ITAndNetworking/SharePointMigration/PublishingImages/NewReportForm.png" style="margin&#58;5px;" /></div>
<div><span class="ssw-rteStyle-FigureNormal">Figure&#58; Fill in form</span><br></div>
<span class="ssw-rteStyle-FigureNormal"></span><div><br>2. Run Checked Out report</div>
<div>&#160;</div>
<div>Run the checkout report from &quot;Site Settings | Manage Content and Structure | View&#58; Checked out documents&quot;&#58;</div>
<div><img class="ssw-rteStyle-ImageArea" alt="CheckedOutDocuments.png" src="/ITAndNetworking/SharePointMigration/PublishingImages/CheckedOutDocuments.png" style="margin&#58;5px;" /><br></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Checked Out Documents report link</span> make sure there are no files checked out, otherwise, go step 3. <div><br>3. Go chase after the users.</div>
<div><br></div>
<div><strong>B. Custom application report (Includes some coding work)</strong><br>In SSW, to make the chase work easier, we have a custom page to show the &quot;Checked out files&quot; and send the notification email to naughty people&#58;</div>
<div><img class="ssw-rteStyle-ImageArea" alt="CheckedOutFilesApplicationReport.png" src="/ITAndNetworking/SharePointMigration/PublishingImages/CheckedOutFilesApplicationReport.png" style="margin&#58;5px;" /></div>
<span class="ssw-rteStyle-FigureNormal">Figure&#58; Checked out Files custom application report</span> 


