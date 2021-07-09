---
type: rule
title: Do you get rid of legacy items in SharePoint Online?
guid: 2156a33a-2b52-4ba7-89f0-96aa6a78f1a5
uri: do-you-get-rid-of-legacy-items-in-sharepoint-online
created: 2021-07-07T12:00:00.0000000Z
authors: 
- title: Jean Thirion
  url: https://www.ssw.com.au/people/jean-thirion
related: []
---

Most people have now moved to SharePoint Online, either from scratch or by migrating content from previous versions of SharePoint. In SharePoint Online, a lot of legacy features have been deprecated and replaced by more modern counterparts. Unfortunately, chances are you have ported a whole lot of useless things as part of your migration.

[TODO: Screenshot of Useless stuff]

Before removing seemingly useless or old stuff, you should always make sure that site owners are OK with the deletion and that the data is actually not useful. In most cases however, the libraries detailed below have been added to your site by default and contain only demo and/or defautl data.

<!--endintro-->

## Process

The process to remove legacy items is always the same regardless of the library/list you're trying to remove:
1. Find the product or feature that replaces it in SharePoint Online
2. Deactivate the site feature associated with the list or library:

Either manually via:
> Site Settings | Site Features | Feature XYZ | Deactivate

Or programmatically using:
``` Powershell
# Connect and get context
Connect-PnPOnline -Url https://contoso.sharepoint.com

# Get Feature Object
$Feature = Get-PnPFeature -Scope Web -Identity $FeatureId #Feature IDs below
 
# Get the Feature status
If($Feature.DefinitionId -ne $null)
{    
    # De-activate the Feature
    Disable-PnPFeature -Scope Web -Identity $FeatureId -Force
}
Else
{
    Write-host -f Yellow "Feature is not active!"
}
```

3. If feature is already disabled or if SharePoint throws an error on deactivation (can happen for very old features), perform a forced delete of the library using powershell.

``` Powershell
# Connect and get context
Connect-PnPOnline -Url https://contoso.sharepoint.com
$ctx = Get-PnPContext

# Get list object
$list = $ctx.Web.Lists.GetByTitle("Library_To_delete")

# Force delete (send to recycle bin)
$list.AllowDeletion = $True
$list.Update()
$ctx.ExecuteQuery()
$list.Recycle() | Out-Null 
$ctx.ExecuteQuery()
```

## MicroFeed

Microfeed has been replaced in SharePoint by **Yammer webparts** and is no longer supported.

Associated Site feature to disable: "Site Feed"
GUID: 15a572c6-e545-4d32-897a-bab6f5846e18

## Announcements

Annoucements are now replaced by the news webparts [TODO: Link to news webpart doc]

Associated Site feature to disable: "Announcement Tiles"
GUID: 00bfea71-d1ce-42de-9c63-a44004ce0104

## Workflow Tasks

SharePoint Worklow are deprecated and replaced by Power Automate [TODO:link to rule to PowerAutomate]

Associated Site feature to disable: "Workflow Task"
GUID: 57311b7a-9afd-4ff0-866e-9393ad6647b1

## Drop-Off Library

Drop-Off Library is **not** deprecated in SharePoint Online explicitely, however it is considered best practice to user Power Automate to achieve the same results with much greater flexibility and maintainability.

Associated Site feature to disable: "Content Organizer"
GUID: 7ad5272a-2694-4349-953e-ea5ef290e97c
