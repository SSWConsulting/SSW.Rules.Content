---
type: rule
title: ASP.NET vs SharePoint development - do you know source control is different?
uri: aspnet-vs-sharepoint-development---do-you-know-source-control-is-different
created: 2009-12-04T09:42:07.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> 
  <p>In ASP.NET<br>
Typically, the team will store the code on a source control system such as TFS (Team Foundation Server), check it out to their own local system, develop and test locally then check it back into source control for sharing.</p>
<p>In SharePoint<br>
SharePoint comes with its own document control and version history out of the box.&#160;This is great for collaborating between developers and designers, but isn’t available for everything.</p>
<p>Differences<br>
Unlike TFS, SharePoint does not support multiple check-out so each file can only be checked out to one person at a time.&#160; The modification must be checked back into SharePoint. </p>
 </span>


  <p>We think the following are best tracked on a development SharePoint server&#58; </p>
<ul>
    <li>Master page </li>
    <li>Page Layouts </li>
    <li>XSL </li>
    <li>CSS </li>
</ul>
<p>And these should not (or cannot) be version controlled on SharePoint server&#58; </p>
<ul>
    <li>Low level customizations such as custom web parts should still be developed in VS.NET and stored in TFS. </li>
    <li>Package files to build solution packages should be stored in TFS. </li>
</ul>



