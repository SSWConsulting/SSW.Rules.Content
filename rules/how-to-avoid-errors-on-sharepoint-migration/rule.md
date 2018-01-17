---
type: rule
archivedreason: 
title: Do you know how to avoid errors?
guid: 94ef1ccc-e1a5-409d-a29d-258231e43ce4
uri: how-to-avoid-errors-on-sharepoint-migration
created: 2018-01-17T22:59:30.0000000Z
authors:
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-know-how-to-avoid-errors

---


<p>There are certain features in SharePoint on-premises that are no longer supported with SharePoint Online.&#160;</p><p>If you migrate using the Sharegate migration tool, you want to have zero errors in their reports. To do so, here are what you should do before considering migration&#58;&#160;<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>Get rid of SharePoint Designer customizations on List form<br></li></ul><dl class="badImage"><dt><img src="/PublishingImages/avoid-errors-sp-migration1.png" alt="avoid-errors-sp-migration1.png" style="width&#58;750px;" /></dt><dd>Bad example&#58; Page customized using SharePoint Designer</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/avoid-errors-sp-migration2.png" alt="avoid-errors-sp-migration2.png" style="width&#58;750px;" />
 </dt><dd>Good example&#58; Out of the box list view page</dd></dl><p>Remove unsupported columns such as&#58;</p><ul><li>Publishing HTML</li><li>Publishing Hyperlinks</li><li>Calculated Columns with volatile functions ('Me', 'Today'…)</li><li>Managed Metadata columns on folders</li><li>Get rid of MicroFeed<br></li></ul><dl class="badImage"><dt><img src="/PublishingImages/avoid-errors-sp-migration3.png" alt="avoid-errors-sp-migration3.png" style="width&#58;750px;" />
   </dt><dd>Bad example&#58; Sharegate migration report shows error if MicroFeed(s) have not been removed​<br></dd></dl>


