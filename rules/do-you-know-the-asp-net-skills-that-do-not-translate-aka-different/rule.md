---
type: rule
archivedreason: 
title: Do you know the ASP.NET skills that do not translate (aka different) ?
guid: aaea5b2c-6192-4bad-97de-6de045cc66f2
uri: do-you-know-the-asp-net-skills-that-do-not-translate-aka-different
created: 2009-05-21T07:21:58.0000000Z
authors:
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects:
- do-you-know-the-asp-net-skills-that-do-not-translate-(aka-different)

---

ASP.NET is file system driven, SharePoint is database driven – all SharePoint content and meta data comes from a database, include images, HTML, Master Page, etc. SharePoint provides a framework where components can be plugged in, and out of the box these areas are improved:

* Security model, membership, permissions
* There’s a relatively consistent UI framework
* Menus, navigation and site maps
* Administration of access, site owners can change permissions for that site – without admins


Deployment model is very different:

* ASP.NET has MSI file or XCopy deployment – individual server
* SharePoint deployment is via Solution Package – but goes cross site farms
* Deployment is both declarative in XML format, as well as in code with Feature and Event receivers


Tools:

* ASP.NET is mostly done in Visual Studio .NET
* SharePoint development is split among:
    * Internet Explorer – SharePoint configurations (note: non IE browsers remain 2nd level and isn’t as good as IE with SharePoint)
    * Microsoft SharePoint Designer – SharePoint HTML page design and customization
    * Visual Studio .NET – custom web parts, custom workflows, solution packages


<!--endintro-->
