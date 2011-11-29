---
type: rule
title: ASP.NET vs SharePoint development - do you know deployment is different?
uri: aspnet-vs-sharepoint-development---do-you-know-deployment-is-different
created: 2009-06-16T00:59:28.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <p>In ASP.NET deployment is a simple xcopy. Or you can&#160;right click the Web Site project and &#160;&quot;Publish Web Site&quot; in Visual Studio. </p>
<dl class="goodImage">
    <dt><img alt="" src="/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/PublishWebSite.png" /> </dt>
    <dd>Fugure&#58; Publish Web Site in Visual Studio </dd>
</dl>
<p>&#160;</p>
 </span>


  <p class="MsoNormal">In SharePoint the way to deploy a set of changes is via a solution package.</p>
<p class="MsoNormal">SharePoint provides additional layer and infrastructure on top of ASP.NET&#160; - part of this layer is the support for administrators (who may not be developers) to quickly add, remove, activate and deactivate features across a SharePoint site farm.</p>
<p class="MsoNormal">These are awesome features and something that basic ASP.NET does not have, but it does add additional development overhead to build the solution packaging.</p>
<ol>
    <li>You need to create such a package via VSeWSS (or a similar tool such as WSP Builder) </li>
    <li>Add entries for all the files you want to include in the package </li>
    <li>Update and get the latest version of the files from development SharePoint or TFS </li>
    <li>Compile the package into a WSP file (which is a cab file) </li>
    <li>Test the package on a staging server. </li>
    <li><span style="font-family&#58;'calibri', 'sans-serif';font-size&#58;11pt;">Deploy it on a production server.</span> </li>
</ol>



