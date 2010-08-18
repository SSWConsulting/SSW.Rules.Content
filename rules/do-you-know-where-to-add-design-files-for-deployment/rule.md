---
type: rule
title: Do you know where to add design files for deployment?
uri: do-you-know-where-to-add-design-files-for-deployment
created: 2009-04-20T00:13:00.0000000Z
authors:
- id: 8
  title: John Liu

---



<span class='intro'> 
  <p>When a designer (or a developer) adds&#160;design/style&#160;files to SharePoint - care must be taken regarding where the files are placed&#58;</p>
<ul>
    <li>Some places are are not suitable because they are not good for deployment </li>
    <li>Other places may have permission issues - designers can't access them </li>
    <li>Some files are part of the site definition and should not be customized </li>
</ul>
 </span>


  <p>So our rules are&#58;</p>
<ol>
    <li>Never modify out of the box SharePoint files in /Style Library/ -&#160;those files are part of the site definition, if you customize them they are hard to deploy </li>
    <li>Start with a clean, minimal masterpage </li>
    <li>Create and reference&#160;your own CSS files and put them&#160;under /Style Library/CSS/&lt;client&gt;/ </li>
    <li>You may want to further divide your CSS paths according to the areas of the site that your CSS is designed for&#58;<br>
    E.g. /Style Library/CSS/SSW/Clients/layout.css </li>
    <li>Designers can modify the XSL file as well!<br>
    put them under /Style Library/XSL Style Sheets/&lt;client&gt;/ </li>
</ol>



