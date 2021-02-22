---
type: rule
archivedreason: 
title: Why do we use VM for SharePoint development?
guid: 3af8b6aa-2559-45aa-a7ab-6a30bebd0866
uri: why-do-we-use-vm-for-sharepoint-development
created: 2009-02-26T02:03:30.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: John Liu
  url: https://ssw.com.au/people/john-liu
related:
- sharepoint-search
redirects: []

---

All SharePoint customization and development must be done on a Virtual Machine.  
<!--endintro-->



1. It's very important to correctly setup a SharePoint environment for development. Correctly configured, this will save you a lot of trouble later on.
2. From time to time, you can seriously damage a SharePoint installation during development and it is best not to install SharePoint on your everyday working machine. Additionally, when you start a new SharePoint project you don't want to carry all the luggage from a previous customization that could potentially affect your new project.
3. Virtual machines can be fired up and shut down easily
4. Virtual machines can be relocated on a different server and thus it doesn't waste developers' own computer resources
5. Virtual machines can be copied and brought to a client for demostration.
6. Very easy for someone to quickly create a new SharePoint server to quickly test or experiment with SharePoint.
7. Bad: There might be more work required to activate additional servers.
