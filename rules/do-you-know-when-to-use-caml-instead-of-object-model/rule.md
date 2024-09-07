---
seoDescription: SharePoint developers can leverage CAML or object model to manage lists and site collections, with CAML ideal for querying and filtering elements across multiple lists.
type: rule
archivedreason:
title: Do you know when to use CAML instead of object model?
guid: dee537be-ad13-47b4-b9e4-52fe91ba7af2
uri: do-you-know-when-to-use-caml-instead-of-object-model
created: 2009-04-09T06:10:00.0000000Z
authors:
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
  - title: Jay Lin
    url: https://ssw.com.au/people/jay-lin
related: []
redirects: []
---

SharePoint utilizes CAML to do a lot of things - one of these is using CAML to define a query language to select elements from lists within SharePoint.

The development experience with CAML is not good.  CAML is unforgiving when it comes to errors, but it doesn't tell you what's wrong.  Thus earning it a bad name with SharePoint developers.  People don't like CAML.

<!--endintro-->

The SharePoint object model is very comprehensive and lets you select items from lists, select lists from sites, in site-collections within web-applications.

Naturally, using the object model is great for traversing all elements in a list.  Once you have a handle to the item, you can also easily modify that item.

On the other hand, one of the SharePoint class SPSiteDataQuery allows a developer to use CAML to specify a query condition that SharePoint can understand to search and return matching elements from across the entire site collection.

This is the underlying class that the Content Query Web Part relies on.

So, you need to use object model when you want to:

- Iterate all elements in a list
- Modify elements in a list

And you use CAML, whether in CQWP or in code with SPSiteDataQuery to:

- Select, filter elements from SharePoint lists
- Select elements from multiple lists
