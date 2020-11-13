---
type: rule
archivedreason: 
title: SharePoint Online - Do you get rid of classic features?
guid: 295eef0e-b089-4931-aaca-1e9632adf89f
uri: sharepoint-online---do-you-get-rid-of-classic-features
created: 2020-11-12T23:55:29.0000000Z
authors:
- id: 69
  title: Jean Thirion
related: []

---


Get rid of classic features in SharePoint Online.<br>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Microfeed​<br></h3><p>Microfeed list is used to support the MicroFeed Classic web part. If you’re using Modern SharePoint Sites and Pages (and you should !) everywhere, you don’t need that list anymore.<br><br>To delete the Microfeed List, simply de-activate the Site Feed feature at the Web level&#58;</p><dl class="image"><dt><img src="/PublishingImages/microfeed-sharepoint.png" alt="microfeed-sharepoint.png" style="width&#58;750px;" /></dt><dt><img src="/PublishingImages/site-feed-sharepoint.png" alt="site-feed-sharepoint.png" style="width&#58;750px;" /></dt></dl><h3 class="ssw15-rteElement-H3">Company Announcements</h3><p>&quot;Announcements&quot; is a default List that used to be created with classic Team Sites. If you’re not using it, chances are you will never do, and modern News should be your replacement for it.</p><dl class="image"><dt><img src="/PublishingImages/company-announcements-sharepoint.png" alt="company-announcements-sharepoint.png" style="width&#58;750px;" /></dt></dl><p>To remove company News, click “Settings” | “Remove” from Site Contents&#58;</p><dl class="image"><dt><img src="/PublishingImages/site-feed-sharepoint2.png" alt="site-feed-sharepoint2.png" /></dt></dl><h3 class="ssw15-rteElement-H3">Drop Off Library​​</h3><p>Drop Off Libraries (Content Organizer feature) were a way to automate moving documents around based on Metadata. This is no longer the optimal solution and you should use&#160;Power Automate instead. To remove Drop Off Library from your site, you need to disable the “Content Organizer” Web level feature&#58;</p><dl class="image"><dt><img src="/PublishingImages/content-organizer-sharepoint.png" alt="content-organizer-sharepoint.png" style="width&#58;750px;" /></dt></dl><h3 class="ssw15-rteElement-H3">Deleting leftovers from Migrations​<br></h3><p>After migrating content from older versions of SharePoint, you may end up in a hybrid state where the abovementioned features are disabled, but associated libraries/lists are still present on your site. If that happens, you ideally want to clean it up.<br>The first thing you can try is enabling/disabling the feature again. In some cases, that will fix the issue and remove the unwanted list/library.<br>If that doesn’t work, however, there is a more radical approach&#58; removing the list/library using Powershell&#58;</p><dl class="image"><dt><img src="/PublishingImages/jean-migration-1.jpg" alt="jean-migration-1.jpg" /></dt></dl><p>(In case you prefer using code straight away instead of the screenshot)</p><p class="ssw15-rteElement-CodeArea">Remove-PnPList -Identity &quot;Workflow Tasks&quot; -Force&#160;</p><p>However, on system Lists, you may get an error&#58;&#160;
</p><dl class="image"><dt><img src="/PublishingImages/jean-migration-2.jpg" alt="jean-migration-2.jpg" /></dt></dl><p>The workaround is to set the “AllowDeletion” flag to true before calling delete&#58;</p><dl class="image"><dt><img src="/PublishingImages/jean-migration-3.png" alt="jean-migration-3.png" /></dt></dl><p>(In case you prefer using code straight away instead of the screenshot)</p><p class="ssw15-rteElement-CodeArea">$list = Get-PnPList -Identity &quot;Workflow Tasks&quot;<br>$list.AllowDeletion = $true<br>$list.Update()<br>Remove-PnPList -Identity &quot;Workflow Tasks&quot; -Force&#160;</p>​<br>


