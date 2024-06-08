---
type: rule
archivedreason: 
title: Do you know that you can't use 2010 Managed Metadata with Office 2007 out of the box?
guid: 6e47f490-e7cf-45ee-8dd2-f11077c947fd
uri: do-you-know-that-you-cant-use-2010-managed-metadata-with-office-2007-out-of-the-box
created: 2010-12-23T07:51:54.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

SharePoint 2010 and Office 2010 ships with a fantastic document management feature "Managed Metadata Service". This new service provides first class support for enterprise taxonomy within a standard SharePoint 2010 environment. 

 Unfortunately, Office 2007 and Office 2003 can't work with managed metadata fields out of the box. 

<!--endintro-->

Office 2010:1. Works fine


Office 2007:1. Document information can't display managed metadata
2. You can still save documents to SharePoint
3. But you can't check-in (if metadata fields are required)
4. User needs to perform a web check-in


Office 2003:1. Can't create new or Open documents with managed metadata
2. Install Office 2007 document support upgrade, this bring the experience a bit better similar to Office 2007.

 

 
Best Solution:

 Use a 3rd party solution - the best one being OnePlaceMail which provides a UI for managed metadata via the "Save to SharePoint". Works with all three versions of Office so users get a consistent UI.     

![](OnePlaceMail.jpg)
**Figure: The optional save dialog that pops up when saving document to SharePoint - allowing use of Managed Metadata from Office 2003, 2007 and File Explorer**
