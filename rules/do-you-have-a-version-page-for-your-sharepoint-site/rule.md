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



  <p>Each time you deploy a new package to your SharePoint site, you should add a new entry in the version list.</p>
<p>This will enable you to quickly find out which version of the package your SharePoint site is using, and let users know what version they are running.</p>

<br><excerpt class='endintro'></excerpt><br>

  <p>
    <img alt="" style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" src="SP_version_small.jpg" />
  </p>
<p> </p>
<ul>
    <li>A custom list for Version should be created at the root level of a SharePoint site collection, and each time a package is deployed - a new record should be added to this version list. </li>
    <li>A simple blank page with a Content Query Web Part can display this versions list in a friendly manner. </li>
    <li>We do not change the version numbers in the .NET Assembly because the assemblies have to be strong-name signed and deployed to the GAC.  So having a versions list is crucial in working out what version of your package is deployed on which server.</li>
</ul>



