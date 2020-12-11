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

Get rid of classic features in SharePoint Online.

<!--endintro-->

### Microfeed


Microfeed list is used to support the MicroFeed Classic web part. If you’re using Modern SharePoint Sites and Pages (and you should !) everywhere, you don’t need that list anymore.

To delete the Microfeed List, simply de-activate the Site Feed feature at the Web level:
<dl class="image">&lt;dt&gt;<img src="microfeed-sharepoint.png" alt="microfeed-sharepoint.png" style="width:750px;">&lt;/dt&gt;&lt;dt&gt;<img src="site-feed-sharepoint.png" alt="site-feed-sharepoint.png" style="width:750px;">&lt;/dt&gt;</dl>
### Company Announcements

"Announcements" is a default List that used to be created with classic Team Sites. If you’re not using it, chances are you will never do, and modern News should be your replacement for it.
<dl class="image">&lt;dt&gt;<img src="company-announcements-sharepoint.png" alt="company-announcements-sharepoint.png" style="width:750px;">&lt;/dt&gt;</dl>
To remove company News, click “Settings” | “Remove” from Site Contents:
<dl class="image">&lt;dt&gt;<img src="site-feed-sharepoint2.png" alt="site-feed-sharepoint2.png">&lt;/dt&gt;</dl>
### Drop Off Library

Drop Off Libraries (Content Organizer feature) were a way to automate moving documents around based on Metadata. This is no longer the optimal solution and you should use Power Automate instead. To remove Drop Off Library from your site, you need to disable the “Content Organizer” Web level feature:
<dl class="image">&lt;dt&gt;<img src="content-organizer-sharepoint.png" alt="content-organizer-sharepoint.png" style="width:750px;">&lt;/dt&gt;</dl>
### Deleting leftovers from Migrations


After migrating content from older versions of SharePoint, you may end up in a hybrid state where the abovementioned features are disabled, but associated libraries/lists are still present on your site. If that happens, you ideally want to clean it up.
The first thing you can try is enabling/disabling the feature again. In some cases, that will fix the issue and remove the unwanted list/library.
If that doesn’t work, however, there is a more radical approach: removing the list/library using Powershell:
<dl class="image">&lt;dt&gt;<img src="jean-migration-1.jpg" alt="jean-migration-1.jpg">&lt;/dt&gt;</dl>
(In case you prefer using code straight away instead of the screenshot)

Remove-PnPList -Identity "Workflow Tasks" -Force

However, on system Lists, you may get an error:
<dl class="image">&lt;dt&gt;<img src="jean-migration-2.jpg" alt="jean-migration-2.jpg">&lt;/dt&gt;</dl>
The workaround is to set the “AllowDeletion” flag to true before calling delete:
<dl class="image">&lt;dt&gt;<img src="jean-migration-3.png" alt="jean-migration-3.png">&lt;/dt&gt;</dl>
(In case you prefer using code straight away instead of the screenshot)

$list = Get-PnPList -Identity "Workflow Tasks"
$list.AllowDeletion = $true
$list.Update()
Remove-PnPList -Identity "Workflow Tasks" -Force
