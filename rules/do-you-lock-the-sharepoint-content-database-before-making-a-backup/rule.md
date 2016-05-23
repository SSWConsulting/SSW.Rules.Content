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


Even though you have advised staff members a migration is taking place – you can guarantee someone will try to check-in or edit documents. The best way to prevent this is to put your content database into read-only mode,&#160;<span style="line-height&#58;20.8px;">locking the&#160;content database.</span>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="line-height&#58;1.6;">There are two options to lock the content database.</span></p><p> 
   <span style="line-height&#58;20.8px;">Option 1 (<strong>Recommended</strong>)&#58;</span> ​​ 
   <br></p><p>1. &#160;Open&#160;<span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><strong>SharePoint Central Administration</strong> site, navigate&#160;to &quot;<strong style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;">Application Management</strong>&quot; |&#160;&quot;<strong style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;">Site Collections</strong><span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;">&quot; | &quot;<span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><strong>Configure quotas and locks</strong>&quot;.</span></span></span></p><dl class="ssw15-rteElement-ImageArea"> 
   <img src="/PublishingImages/quotas-and-locks.jpg" alt="quotas-and-locks.jpg" data-pin-nopin="true" style="width&#58;800px;" /> 
</dl><p> 
   <span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;">2. Select the &quot;site collection&quot; which you would like to lock.</span></span></span></p><p> 
   <span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;"><span style="color&#58;#2a2a2a;font-family&#58;'segoe ui', 'lucida grande', verdana, arial, helvetica, sans-serif;line-height&#58;18px;">​3. Choose &quot;Read-only (blocks additions, updates, and deletions)&quot;, then click &quot;OK&quot;.</span></span></span></p><dl class="ssw15-rteElement-ImageArea"> 
   <img src="/PublishingImages/read-only-status.jpg" alt="read-only-status.jpg" /> 
</dl><dl class="ssw15-rteElement-ImageArea"> 
   <strong>Note</strong>&#58; Read more at&#160;<a href="https&#58;//technet.microsoft.com/en-us/library/cc263238%28v=office.15%29.aspx?f=255&amp;MSPPError=-2147217396">Manage the lock status for site collections in SharePoint 2013 </a></dl><dl class="ssw15-rteElement-ImageArea"> 
   ​<br> 
</dl><p>Option 2 (<strong>not recommended</strong>)&#58;</p><p>1.&#160;&#160;&#160; On your database server open 
   <b>SQL Server Management Studio</b></p><p>2.&#160;&#160;&#160; Right click on the content database associated with the site collection you're migrating<span style="line-height&#58;1.6;"> | </span><b style="line-height&#58;1.6;">Properties</b></p><p>3.&#160;&#160;&#160; Choose 
   <b>Options </b>| Scroll to the bottom of the options list</p><p>4.&#160;&#160;&#160; For the 
   <b>Database Read-Only</b> choose True</p><dl class="image"><dt> 
      <img src="/PublishingImages/LocLSQLDB.jpg" alt="" /> 
   </dt><dd>Figure - Database Properties | Options | Database-Read Only</dd></dl> ​ 
<p>5.&#160;&#160;&#160; Now it’s safe to take a backup of your content database</p><p>&#160;<b>NOTE&#58; </b>&#160;When some SharePoint timer services are run it may cause the site to display errors when the database is in read-only mode</p>


