---
seoDescription: Create links to URLs in SharePoint libraries using 'Link to a document' content type or upload shortcut files (.url), ideal for navigating to different websites and documents.
type: rule
archivedreason:
title: Do you know how to create a link to a URL in SharePoint?
guid: f7e772d8-748f-4f21-8890-c25ef13718f9
uri: do-you-know-how-to-create-a-link-to-a-url-in-sharepoint
created: 2013-07-26T00:38:30.0000000Z
authors:
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

You may need a link in a SharePoint document to help you navigate to a different URL (like shortcut in Windows), there are different ways to implement this.

<!--endintro-->

::: bad
A. Create a shortcut in windows, then upload the shortcut file (.url) to the document library.  
:::

::: good
B. Use "Link to a document" content type in SharePoint.  
:::

Details on how you to create a link to a document in a SharePoint library.

**A. Create a shortcut in windows, then upload the shortcut file (.url) to the document library.**

To do this, you need to remove .url file type from your blocked file types in your web application. This will bring some security risk, which is not recommended, and I won't show the step details here.

**B. Use "Link to a document" content type in SharePoint.**

1. Enable "Content Type management" in your document library.
   ![Figure: Enable Content Type management in library setting](EnableContentTypeDocument.png)
   
2. Add "Link to a Document" content type into the library.
   ![Figure: Add from existing site content type](AddExistContentType.png) 

   ![Figure: Select "Link to a Document" content type](SelectLinkToADocumentType.png)

3. Create a "Link to a document" instance
   ![Figure: select "File | New Document (dropdown) | Link to a document"](CreateLinkToADocumentInstance.png)
   
   ![Figure: Input "Name" and "URL"](InputLinkUrlAndName.png) 

4. Done

You should be able to see the link type document in your library:

![Figure: Link type documents with the lovely shortcut icon](LinksTypeDocumentsWithShortcutIcon.png)
