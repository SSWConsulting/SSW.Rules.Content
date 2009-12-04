---
type: rule
archivedreason: 
title: Do you have a version page for your SharePoint site?
guid: 6b58735c-a6e7-4a67-b0b3-96e3050bfe3b
uri: do-you-have-a-version-page-for-your-sharepoint-site
created: 2009-04-20T09:20:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
<p><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/SP_version_small.jpg" /></p>
<p>&#160;</p>
<ul>
<li>A custom list for Version should be created at the root level of a SharePoint site collection, and each time a package is deployed - a new record should be added to this version list.</li>
<li>A simple blank page with&#160;a Content Query Web Part can display this versions list in a friendly manner.</li>
<li>We do not change the version numbers in the .NET Assembly because the assemblies have to be strong-name signed and deployed to the GAC.&#160; So having a versions list is crucial in working out what version of your package is deployed on which server.</li></ul>


