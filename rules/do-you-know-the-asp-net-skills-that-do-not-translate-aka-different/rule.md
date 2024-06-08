---
type: rule
title: Do you know the ASP.NET skills that do not translate (aka are different) ?
uri: do-you-know-the-asp-net-skills-that-do-not-translate-aka-different
authors:
  - title: Jay Lin
    url: https://ssw.com.au/people/jay-lin
related: []
redirects:
  - do-you-know-the-asp-net-skills-that-do-not-translate-(aka-different)
created: 2009-05-21T07:21:58.000Z
archivedreason: null
guid: aaea5b2c-6192-4bad-97de-6de045cc66f2
---
ASP.NET is file system driven, whilst SharePoint is database driven. All SharePoint content and meta data comes from a database, including images, HTML, Master Page, etc. SharePoint provides a framework where components can be plugged in, and as a result these areas are improved out-of-the-box:

* Security model, membership, permissions.
* The UI framework becomes relatively consistent.
* Menus, navigation, and site maps.
* Administration of access i.e., site owners can change permissions for that site – without the need for administrators.

Deployment model is very different:

* ASP.NET has MSI file or XCopy deployment – individual server.
* SharePoint deployment is via Solution Package – but goes cross-site farms.
* Deployment is both declarative in (XML format), as well as in code with Feature and Event receivers.

Tools:

* ASP.NET is mostly done in Visual Studio .NET.
* SharePoint development is split among:

  * Internet Explorer – SharePoint configurations (note: non-IE browsers remain 2nd level and isn’t as good as IE with SharePoint)
  * Microsoft SharePoint Designer – SharePoint HTML page design and customization
  * Visual Studio .NET – custom web parts, custom workflows, solution packages

<!--endintro-->