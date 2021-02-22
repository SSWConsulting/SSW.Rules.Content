---
type: rule
archivedreason: 
title: Do you have a migration plan
guid: 2f943ab1-a970-4c64-9f45-396f4d2d194a
uri: high-level-migration-plan
created: 2016-05-20T02:01:48.0000000Z
authors:
- title: Mark Liu
  url: https://ssw.com.au/people/mark-liu
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-have-a-migration-plan

---


<span style="line-height&#58;20.8px;">​​​At a high level, the plan is&#58;</span>
<br><excerpt class='endintro'></excerpt><br>
<p></p><p></p><ul><li><span style="line-height&#58;1.6;"><strong>Install </strong></span><span style="line-height&#58;1.6;"><strong>SharePoint&#160;​</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;background-color&#58;initial;">I</span><span style="line-height&#58;1.6;background-color&#58;initial;">nstall with topology of your choice in SharePoint 2016 (or use <a href="https&#58;//autospinstaller.codeplex.com/">AutoSPInstaller</a>)</span><br></li><li><span style="line-height&#58;1.6;background-color&#58;initial;">Configure Application services</span><br></li></ol><p></p><p></p><blockquote style="margin&#58;0px 0px 0px 40px;border&#58;none;padding&#58;0px;"><ul><li>Run the wizard (or use script. the community script wasn't ready when Thiago and I was migrating intranet)​</li><li><span style="line-height&#58;1.5em;">Configure user profile and its permission configuration (see <a href="https&#58;//technet.microsoft.com/en-us/library/ee721052.aspx">msdn</a>​)​</span></li></ul></blockquote><div><div><ul><li><span style="line-height&#58;1.5em;"><strong>Test Migration</strong></span><br></li></ul></div><ol><li><span style="line-height&#58;1.6;"><a href=/do-you-know-how-to-identify-customizations-on-sharepoint-webs>Install required WSP packages in 2016</a></span><br></li><li><span style="line-height&#58;1.6;"><a href=/run-test-spcontentdatabase-before-actual-migration>Test migrating&#160;content database from old to new</a>​</span></li><li>Fix all the missing customizations error in the above step, then do the <a href="https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx">content database migration</a></li><li><span style="line-height&#58;1.6;">(</span><span style="line-height&#58;1.6;">Optional) <a href=/have-you-migrated-your-service-application-databases>Migrate services database</a>&#160;(depends on which service applications do you use)</span><br></li></ol><ul><li><span style="line-height&#58;1.6;"><strong>Post migration setup</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;">Configure search</span><ul><li><a href=/use-default-zone-url-in-search-content-source>Do you use default zone URL in search content source</a><br></li><li><a href=/extend-web-application-for-https>Do you add https by extending web application</a></li><li><a href=/fix-search-with-office-app-preview>Do you fix search with Office App for content preview ? (on premise only)</a>​</li></ul></li><li><span style="line-height&#58;1.6;">Configure metadata (optional)</span><br></li></ol><ul><li><span style="line-height&#58;1.6;"><strong>Test test </strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong></strong></span><span style="line-height&#58;1.6;"><strong>tes</strong></span><span style="line-height&#58;1.6;"><strong>t</strong></span><br></li><li><span style="line-height&#58;1.6;"><strong>Go-live migration</strong></span><br></li></ul><ol><li><span style="line-height&#58;1.6;"><a href=/do-you-lock-the-sharepoint-content-database-before-making-a-backup>Put old SharePoint into read-only</a></span><br></li><li><span style="line-height&#58;1.6;"><a href="https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx">Refresh content &amp; service database from SP 2013 to 2016</a></span><br></li><li><span style="line-height&#58;1.6;">Update DNS</span><br></li><li><span style="line-height&#58;1.5em;">Decomm​ission old SharePoint server and</span><span style="line-height&#58;1.5em;"> database (after 2 weeks when you're confident with the new environment)</span></li></ol><br><p><br></p></div>


