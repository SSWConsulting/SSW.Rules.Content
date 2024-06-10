---
seoDescription: Take SharePoint data offline with SharePoint Workspace, synchronizing entire sites and avoiding burdens on Outlook.
type: rule
archivedreason:
title: Do you know the best way to take SharePoint data offline?
guid: 484c1056-30ba-4419-9321-d6424fbefb78
uri: do-you-know-the-best-way-to-take-sharepoint-data-offline
created: 2009-12-15T07:50:38.0000000Z
authors:
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
related: []
redirects: []
---

In SharePoint 2010, there are quite a few tools that we can use to take SharePoint data offline. Let’s look at our options:

- use Outlook to synchronize document libraries, calendar and contacts offline.
- use Excel to take read-only copies of list data offline.
- use Access to take list data offline – Access also lets you edit offline and synchronize back.
- use SharePoint Workspace (this was Groove) to take entire Site offline, unfortunately this doesn’t work for calendars.

<!--endintro-->

We think the best way is to use Workspace instead of Outlook:

1. SharePoint Workspace synchronize an entire site

   a. So when lists are renamed it knows about it.

   b. It also knows about new lists that are added to a SharePoint site ![](Synchronize.jpg) **Figure: SharePoint Workspace synchronizing an entire site**

2. Outlook can be quite busy when synchronizing to Exchange server; it is good to not burden it with more work.

While SharePoint Workspace is quite good, we don’t like to store lists in it:

1. Access has better filtering, sorting options when offline
