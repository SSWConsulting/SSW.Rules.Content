---
type: rule
title: ASP.NET vs SharePoint development - do you know source control is different?
uri: aspnet-vs-sharepoint-development---do-you-know-source-control-is-different
created: 2009-12-04T09:42:07.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>We think the following are best tracked on a development SharePoint server&#58; </p>
<ul>
    <li>Master page</li>
    <li>Page Layouts</li>
    <li>XSL</li>
    <li>CSS</li>
</ul>
<p>And these should not (or cannot) be version controlled on SharePoint server&#58; </p>
<ul>
    <li>Low level customizations such as custom web parts should still be developed in VS.NET and stored in TFS.</li>
    <li>Package files to build solution packages should be stored in TFS. </li>
</ul>



