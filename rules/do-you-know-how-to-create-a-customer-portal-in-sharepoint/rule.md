---
type: rule
title: Do you know how to create a "Customer Portal" (in SharePoint)?
uri: do-you-know-how-to-create-a-customer-portal-in-sharepoint
created: 2009-05-28T06:51:18.0000000Z
authors:
- id: 9
  title: William Yin
- id: 19
  title: Sumesh Ghimire
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>​You should do anything that helps a project succeed. The best thing is to enable great collaboration, by giving your customer an awesome 'Customer&#160;Portal'.&#160; Then they can see new mockups, comment on features, get new releases and participate in team discussions on their particular project.<br></p>
<p>So the first thing you should do is to create a 'Customer Portal' in your SharePoint extranet. Then give your&#160;customer a login,&#160;send them an email and they are now going&#160;to really get involved!</p>
<p>There are many means by which you could provide this functionality to your client. </p>
<p>If you are using SharePoint then....</p>
<p>It is advised that you create a customized SharePoint Team Collaboration site template. That way you can very quickly initialize a new site, for each new customer.</p>
<p>Once you have the template, follow these steps to create a customer portal with SharePoint 2007&#58;</p>
 </span>

<ol><li>Go to the root where you want to create a site. E.g. sharepoint.ssw.com.au</li><li>
      <font size="2">Click &quot;Site Actions&quot; on right-hand top, select &quot;Manage Content and Structure</font> </li></ol><dl class="goodImage"><dt><p>&#160;<img border="0" src="/PublishingImages/ManageContentAndStructure.jpg" alt="Manage Content and Structure" style="border-width&#58;0px;border-style&#58;solid;" /></p></dt><dt></dt><dd>Figure&#58; The first step to creating a 'Customer Portal' is to select 'Manage Content and Structure' to view site collection </dd></dl><p>
   <font size="2">Once the new window opens, on the left-hand side, click on the 'Clients' dropdown select New&#160;-&gt; Site. <br> </font> <font size="2"> <font color="#400040">Note&#58; If you </font>don’t see this option, that means you don’t have permission to create the site.</font></p><dl class="goodImage"><dt><p>&#160;<img border="0" src="/PublishingImages/CreateNewSiteStep1.jpg" alt="Create New Site" style="border-width&#58;0px;border-style&#58;solid;" /><br></p></dt><dt></dt><dd>Figure&#58; Create new site </dd></dl><p>Now follow these steps when the new window opens fill in the fields below.</p><dl class="goodImage"><dt><p>
         <img border="0" src="/PublishingImages/CreateNewSiteStep2.jpg" alt="Info to create site" style="border-width&#58;0px;border-style&#58;solid;" />&#160;</p></dt><dt></dt><dd>Figure&#58; Fill in the appropriate info then click &quot;Create&quot; </dd></dl><p>More Information&#58;</p><ol><li>Fill in the fields for the new client site <br>eg. Title, Description, and URL</li><li>Select the template <br>e.g “<b>ClientCollaboration_V1</b>” in the Custom tab.<br>Note&#58; Your selection is confirmed in the picture. In this example, the template’s description looks like “<b>Site for Collaboration with SSW Clients</b>”.</li><li>Select “<b>Use Unique permissions</b>” as you need to give the client an account to visit.</li><li>In the “<b>Navigation Inheritance</b>” choose&#160;“<b>No</b>” as you don’t need to let client visit the other client sites via the navigation.</li><li>Click “<strong>Create</strong>”</li></ol><p>&#160;</p><p>Next step is to setup the groups and permissions.</p> 
<img src="/PublishingImages/SetUpGroupForSite.jpg" class="ms-rteCustom-ImageArea" alt="" />&#160;&#160;<font size="-0" class="ms-rteCustom-FigureGood">Figure&#58; Create a 'new group' or select an 'existing group' for the newly created site</font> 
<p>More Information&#58;<br></p><ul><li>Permissions&#58; After you created the website for the client project, you need to configure the permission to make sure the developers and the clients can visit the site with the current authority. By default&#58;</li></ul><ol><li>
      <strong>Visitors to the site - Read&#58; </strong> 
      <ul><li>Visitors need to read most of the site.</li><li>They can't read team discussions (not used)</li><li>They can download from 'release files' document library.</li><li>They can <span style="font-family&#58;verdana, sans-serif;color&#58;#555555;font-size&#58;9pt;">synchronize their calendar </span>to the team calendar in SharePoint (not used - one day it should read from CRM)</li></ul></li><li>
      <strong>Members of this Site - Contribute&#58;</strong> 
      <ul><li>Can view, add, update and delete.</li></ul></li><li>
      <strong>Owners of this Site - Full Control&#58;</strong> 
      <ul><li>Has a full control.</li></ul></li></ol><p>In this case, we are using 'create a new group' option because we want this group to be able to access only for this particular site&#160; - It is a good practice to create a new group for every site you create, because it will be easier to add or delete users in the group for that specific site.</p><p>Note&#58; you can also access this through the &quot;People and Group&quot; option on &quot;Site Action&quot; link on right-hand top of the page&#160;if you need to manage permission in future.</p><p>Click &quot;OK&quot;, and the portal is created.</p><dl class="goodImage"><dt><p>
         <img border="0" src="/PublishingImages/Northwind%20Portal.jpg" alt="Northwind Portal" style="border-width&#58;0px;border-style&#58;solid;" /><br></p></dt><dt></dt><dd>Figure&#58; Northwind portal<br></dd></dl><p>Note&#58; SharePoint will send &quot;welcome email&quot; to all the members of the groups you created&#160;for the site with basic information, but you still need to send an&#160;email to your customer with the login details like URL, username, and password.</p>


