---
type: rule
archivedreason: 
title: ASP.NET vs SharePoint development - do you know deployment is different?
guid: 5670dd01-3d85-4374-adfd-f9bbf0f2ebb8
uri: asp-net-vs-sharepoint-development-do-you-know-deployment-is-different
created: 2009-06-16T00:59:28.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---



  <p>In ASP.NET deployment is a simple xcopy. Or you can right click the Web Site project and  "Publish Web Site" in Visual Studio. </p>
<dl class="goodImage">
    <dt><img src="PublishWebSite.png" alt="" /> </dt>
    <dd>Fugure: Publish Web Site in Visual Studio </dd>
</dl>
<p> </p>

<br><excerpt class='endintro'></excerpt><br>

  <p class="MsoNormal">In SharePoint the way to deploy a set of changes is via a solution package.</p>
<p class="MsoNormal">SharePoint provides additional layer and infrastructure on top of ASP.NET  - part of this layer is the support for administrators (who may not be developers) to quickly add, remove, activate and deactivate features across a SharePoint site farm.</p>
<p class="MsoNormal">These are awesome features and something that basic ASP.NET does not have, but it does add additional development overhead to build the solution packaging.</p>
<ol>
    <li>You need to create such a package via VSeWSS (or a similar tool such as WSP Builder) </li>
    <li>Add entries for all the files you want to include in the package </li>
    <li>Update and get the latest version of the files from development SharePoint or TFS </li>
    <li>Compile the package into a WSP file (which is a cab file) </li>
    <li>Test the package on a staging server. </li>
    <li><span style="font-family:'calibri','sans-serif';font-size:11pt;">Deploy it on a production server.</span> </li>
</ol>



