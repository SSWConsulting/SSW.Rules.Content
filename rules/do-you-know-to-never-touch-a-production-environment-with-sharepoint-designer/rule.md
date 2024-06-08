---
type: rule
archivedreason: 
title: Do you know to *never* touch a production environment with SharePoint designer?
guid: 9a0ac53a-5f73-4769-bcc4-e2cfa2ed0f98
uri: do-you-know-to-never-touch-a-production-environment-with-sharepoint-designer
created: 2009-04-20T08:31:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

* SharePoint designer can silently reformat your code and introduce errors.
* If you modify any master page or page layout file with SharePoint designer, it becomes customized. This means that SharePoint is now looking at a customized version stored in the database rather than the version on the file system. You then can't deploy future changes, because SharePoint will now always serve the customized version instead of the ghosted version in the solution package.


<!--endintro-->
