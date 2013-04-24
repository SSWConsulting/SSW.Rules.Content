---
type: rule
archivedreason: 
title: Do you lock the SharePoint Content Database before making a backup?
guid: 8dad04d4-ba19-4338-b35a-4eaad6b34fbc
uri: do-you-lock-the-sharepoint-content-database-before-making-a-backup
created: 2010-12-23T06:55:11.0000000Z
authors:
- id: 36
  title: Daniel Šmon
- id: 9
  title: William Yin
- id: 21
  title: Matthew Hodgkins
related: []

---


Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read only mode.&#160;

<br><excerpt class='endintro'></excerpt><br>
<p>Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read only mode.</p><p>1.&#160;&#160;&#160; On your database server open 
   <b>SQL Server Management Studio</b></p><p>2.&#160;&#160;&#160; Right click on the content database associated with the site collection your migrating | 
   <b>Properties</b></p><p>3.&#160;&#160;&#160; Choose 
   <b>Options </b>| Scroll to the bottom of the options list</p><p>4.&#160;&#160;&#160; For the 
   <b>Database Read-Only</b> choose 
   <b>True<img src="/PublishingImages/LocLSQLDB.jpg" alt="" style="width&#58;560px;" /></b><b><br> </b></p><p> 
   <font class="ms-rteCustom-FigureNormal" size="+0">Figure - Database Properties | Options | Database-Read Only</font></p><p>5.&#160;&#160;&#160; Now it’s safe to take a backup of your content database</p><p>&#160;<b>NOTE&#58; </b>&#160;When some SharePoint timer services are run it may cause the site to display errors when the database is in read only mode</p>


