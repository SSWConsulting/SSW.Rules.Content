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

The process to remove legacy items is always the same regardless of the library/list you're trying to remove:
1. Find the product or feature that replaces it in SharePoint Online
2. Disable the site feature associated with the list or library
3. If feature is already disabled, perform a forced delete of the library using powershell 

## MicroFeed

Microfeed has been replaced in SharePoint by *Yammer webparts* and is no longer supported.



## Announcements

## Workflow Tasks

## DropOff Library
