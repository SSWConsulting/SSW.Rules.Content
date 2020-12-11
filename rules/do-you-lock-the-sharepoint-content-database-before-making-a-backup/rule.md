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


Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read-only mode, <span style="line-height:20.8px;">locking the content database.</span>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="line-height:1.6;">There are two options to lock the content database.</span></p><p>
   <span style="line-height:20.8px;">Option 1 (<strong>Recommended</strong>):</span> ​​ 
   <br></p><p>1.  Open <span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><strong>SharePoint Central Administration</strong> site, navigate to "<strong style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;">Application Management</strong>" | "<strong style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;">Site Collections</strong><span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;">" | "<span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><strong>Configure quotas and locks</strong>".</span></span></span></p><dl class="ssw15-rteElement-ImageArea">
   <img src="quotas-and-locks.jpg" alt="quotas-and-locks.jpg" data-pin-nopin="true" style="width:800px;" />
</dl><p>
   <span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;">2. Select the "site collection" which you would like to lock.</span></span></span></p><p>
   <span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;"><span style="color:#2a2a2a;font-family:'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height:18px;">​3. Choose "Read-only (blocks additions, updates, and deletions)", then click "OK".</span></span></span></p><dl class="ssw15-rteElement-ImageArea">
   <img src="read-only-status.jpg" alt="read-only-status.jpg" />
<dd>Note: Read more at <a href="https://technet.microsoft.com/en-us/library/cc263238%28v=office.15%29.aspx?f=255&MSPPError=-2147217396">Manage the lock status for site collections in SharePoint 2013</a></dd>
​​</dl><p>Option 2 (<strong>not recommended</strong>):</p><p>1.    On your database server open 
   <b>SQL Server Management Studio</b></p><p>2.    Right click on the content database associated with the site collection you're migrating<span style="line-height:1.6;"> | </span>
   <b style="line-height:1.6;">Properties</b></p><p>3.    Choose 
   <b>Options </b>| Scroll to the bottom of the options list</p><p>4.    For the 
   <b>Database Read-Only</b> choose True</p><dl class="image"><dt>
      <img src="LocLSQLDB.jpg" alt="" />
   </dt><dd>Figure - Database Properties | Options | Database-Read Only</dd></dl> ​ 
<p>5.    Now it’s safe to take a backup of your content database</p><p> <b>NOTE: </b> When some SharePoint timer services are run it may cause the site to display errors when the database is in read-only mode</p>


