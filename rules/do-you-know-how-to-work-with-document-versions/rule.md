---
type: rule
title: Do you know how to work with document versions?
uri: do-you-know-how-to-work-with-document-versions
authors:
  - title: John Liu
    url: https://ssw.com.au/people/john-liu
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2009-07-23T03:16:53.000Z
archivedreason: null
guid: 976fe4d1-ecfa-41c8-b597-e22cb7bd6b81

---

This is how you should work with **document versions**:

<!--endintro-->

1. Make sure your document library is configured to use versioning.   
   **Tip:** You can configure this in **Settings | Versioning Settings**
2. Make sure you are showing the version column in your document view.  
   ![Figure: You can add the column by selecting Modify View](VersionColumn_Small.jpg)

3. Whenever you edit the document and check it in, SharePoint will automatically increase the version number. If you need to send this document to a client then it is important to:
    1. Save the file locally by selecting **Send To | Download a Copy**    
![](SaveFileLocally_Small.jpg)
    2. Add the version to the end of the filename e.g. Specifications\_v2.0.docx
    3. Then email it to the client.
    4. We do this so that we can track what version of the document was sent to the client. 
   **Tip:** If you are not working with SharePoint then we recommend you [include version numbers in your file names](/show-version-numbers/).
