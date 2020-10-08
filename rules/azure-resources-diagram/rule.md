---
type: rule
archivedreason: 
title: Visualizing - Do you have an Azure resources diagram?
guid: 9c0aa4a1-0333-48d2-994f-9cd5d55ec01f
uri: azure-resources-diagram
created: 2020-10-06T00:15:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- azure-resources-visualizing
- visualizing-do-you-have-an-azure-resources-diagram

---


<p>Looking at a long list of Azure resources is not the best way to be introduced to a new project. It is much better to visualize your resources.<br></p><p>You need an&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=7b588070-e0d2-46f4-811e-87b15a8c190d">architecture diagram</a>, but this is often high level, just outlining the most critical components from the 50,000ft view, often abstracted into logical functions or groups. So, once you have your architecture&#160;diagram,&#160;the next step is to create your Azure resources diagram.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify s4-wpActive"><iframe width="750" height="422" src="https&#58;//www.youtube.com/embed/mSg4CM8FbXo" frameborder="0"></iframe>&#160;</div><h3 class="ssw15-rteElement-H3">Option A&#58; Just viewing a list of resources in the Azure portal</h3><ul><li>​When there are a lot of resources this doesn't work.</li></ul><p></p><dl class="badImage"><dt> 
      <img src="/SiteAssets/azure-resources-diagram/azure%20resources.png" alt="AZURE-VIEW0-BAD.png" style="width&#58;752px;" /> 
   </dt><dd>Figure&#58; Bad Example – Using the&#160;Azure Portal to view your resources</dd><h3 class="ssw15-rteElement-H3">
      <br>
   </h3><h3 class="ssw15-rteElement-H3">​​​​Option B&#58; Visually viewing the resources<br></h3></dl><dl class="goodImage"><dt> 
      <img src="/PublishingImages/AZURE-VIEW-GOOD.png" alt="AZURE-VIEW-GOOD.png" style="width&#58;750px;" /> 
   </dt><dd>Figure&#58; Good Example – Viewing the resources in VS Code using the ARM Template Viewer&#160;extension</dd></dl><p></p><p>
   <a href="https&#58;//marketplace.visualstudio.com/items?itemName=bencoleman.armview">https&#58;//marketplace.visualstudio.com/items?itemName=bencoleman.armview​</a></p><p>
   <b>Suggestion to Microsoft&#58;</b><br>Add an auto-generated diagram in the Azure portal. Have an option in the combo box (in addition to List View) for Diagram View.<br></p><p>UPDATE&#58; This is now happening.<br></p><blockquote class="twitter-tweet"><p class="ssw15-rteElement-Reference">BIG NEWS! My ARM visualiser is now a native part of the Azure portal &#128513; The engineering team did most of the hard work, but I'm chuffed to bits. It's currently in the special RC portal, please try it out (in the 'export template' view) 
      <a href="https&#58;//t.co/iEvAhxxGRK">https&#58;//t.co/iEvAhxxGRK</a> &amp; provide feedback! 
      <a href="https&#58;//t.co/4KTu7GGOeQ">pic.twitter.com/4KTu7GGOeQ</a>​<br>​— Ben Coleman (@BenCodeGeek) 
      <a href="https&#58;//twitter.com/BenCodeGeek/status/1248272453509484550?ref_src=twsrc%5etfw">April 9, 2020</a></p></blockquote> ​ 
<p>​<br></p><p class="ssw15-rteElement-P">
   <b>Scrum Warning&#58; </b>Like the architecture diagram, this is technical debt as it needs to be kept up to date each Sprint. However, unlike the architecture diagram, this one is much easier to maintain as it can be refreshed with a click.​ You&#160;could reduce this technical debt by automatically saving the .png to the same folder as your architecture diagram.&#160;It is easy to do this by using&#160;Azure Event Grid and Azure Functions to generate&#160;these for you when you make changes to your resources.</p>


