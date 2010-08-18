---
type: rule
title: Do you know to *never* touch a production environment with SharePoint designer?
uri: do-you-know-to-never-touch-a-production-environment-with-sharepoint-designer
created: 2009-04-20T08:31:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <ul>
    <li>SharePoint designer can silently reformat your code and introduce errors. </li>
    <li>If you modify any master page or page layout file with SharePoint designer, it becomes customized. This means that SharePoint is now looking at a customized version stored in the database rather than the version on the file system. You then can't deploy future changes, because SharePoint will now always serve the customized version instead of the ghosted version in the solution package.</li>
</ul>
 </span>




