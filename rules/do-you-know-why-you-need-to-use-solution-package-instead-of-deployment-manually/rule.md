---
type: rule
archivedreason: 
title: Do you know why you need to use solution package instead of deployment manually?
guid: a7cc7bb5-c13f-4c56-86ae-312bb8c51d98
uri: do-you-know-why-you-need-to-use-solution-package-instead-of-deployment-manually
created: 2009-04-09T02:44:19.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---



  <p>As a server product, SharePoint supports lots of configuration, but the support for packaging and deploying changes between servers remains very week.</p>
<p>The experts agree that the best&#160;and preferred way&#160;to package a set of changes is to build a solution package.&#160; A SharePoint solution package includes all the components and dependent files packed in a cab file.</p>
<p>There are&#160;many reasons why you need to use solution package&#58; </p>

<br><excerpt class='endintro'></excerpt><br>

  <ol type="1">
    <li style="" class="MsoNormal"><span>All&#160;dependent files and components are in the package - allowing developers to&#160;quickly deploy development, testing, staging and production servers.&#160;</span> </li>
    <li style="" class="MsoNormal"><span>Manual steps are very long, and error prone</span> </li>
    <li style="" class="MsoNormal"><span>Solution packages are easy to retract</span> </li>
    <li style="" class="MsoNormal"><span>Minimize downtime in the SharePoint production server during an upgrade operation</span> </li>
    <li style="" class="MsoNormal"><span>No content data loss during upgrades - SharePoint backup/restore deployment methods will block users from making changes to the production the site during the upgrade period</span></li>
</ol>



