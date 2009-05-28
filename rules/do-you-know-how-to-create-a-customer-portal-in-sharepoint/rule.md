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



<span class='intro'> <p>You always need to collaborate with your customer.&#160; They want to see new mockups, comment on features, get new releases and participate in team discussions on their particular project.</p>
<p>So the first thing you should do is to create a customer portal in your SharePoint extranet, and give your&#160;customer a login so they can jump in and get involved!</p>
<p>We use a customized SharePoint Team Collaboration site template to quickly initialize a new site for our customers.</p>
<p>Do you know how to create a customer portal?</p> </span>

<p><font size="4">Follow the following steps to create a Client Site.</font></p>
<ul>
<li><font size="2">Go to the root where you want to create a site, i.e sharepoint.ssw.com.au</font> 
<li><font size="2">Click &quot;Site Actions&quot; on right hand top, select &quot;Manage Content and Structure</font> </li></ul>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Manage Content and Structure" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/ManageContentAndStructure.jpg" /></p>
<dt>
<dd>Figure&#58; Manage Content and Structure to view site collection </dd></dl>
<ul>
<li><font size="2">New window will open, on the left hand side, click on the dropdown of the clients and select New-&gt;Site. </font><font size="2"><font color="#ff0000">NOTE&#58;</font> If you don’t see this option, that means you don’t have permission to create site, talk to John or Joe to grant you appropriate permission. </font></li></ul>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Create New Site" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/CreateNewSiteStep1.jpg" /></p>
<dt>
<dd>Figure&#58; Create new site</dd></dl>
<ul>
<li>Now follow these steps when the new window opens,</li></ul>
<ol>
<li>Fill in the new client project <span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">website’s Title, Description and URL name.</span></li>
<li><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Select a template called “<b>ClientCollaboration_V1</b>” in the Custom tab.</span></span></li>
<li><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Check the template’s description looks like “<b>Site for Collaboration with SSW Clients</b>”.</span></span></span></li>
<li><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Select “<b>Use Unique permissions</b>” for this new site in “<b>Permissions</b>” as you need to give the client an account to visit this client project website “<b>only”</b>.</span></span></span></span></li>
<li><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Choice “<b>No</b>” in the “<b>Navigation Inheritance</b>” part as you don’t need to let client visit the other sites via the navigation. </span></span></span></span></span></li>
<li><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU"><span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Click “Create” to create the new website for the client project.</span></span></span></span></span></span></li></ol>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Info to create site" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/CreateNewSiteStep2.jpg" /></p>
<dt>
<dd>Figure&#58; Fill in the appropriate info to created site.</dd></dl>
<ul>
<li>You can setup groups and permission here, or through the &quot;People and Group&quot; as shown in next step.&#160;</li></ul>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Create new group Image" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/CreateNewSiteSetPermissionStep1.jpg" /></p>
<dt>
<dd>Figure&#58; Create a new group or select an existing group for the newly created site.</dd></dl>
<ul>
<li>Permissions&#58; After you created the website for the client project, you need to configure the permission to make sure the developers and the clients can visit the site with the current authority.</li></ul>
<ol>
<li>On the root of the current client site, Go to Site Action - People and Groups for the client project.</li>
<li>Create a group for visitors, New - New Group.</li>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Create new group" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/CreateNewSiteSetPermissionStep3.jpg" /></p>
<dt>
<dd>Figure&#58; <span style="font-family&#58;'calibri','sans-serif';font-size&#58;12pt;" lang="EN-AU">Create a new group for the site.</span></dd></dl>
<li>Give appropriate permission to this group.</li></ol>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Appropriate Permission" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/CreateNewSiteSetPermissionStep4.jpg" /></p>
<dt>
<dd>Figure&#58; Assign an appropriate permission to the created groups.</dd></dl>
<ul>
<li>&#160;Thats it all done.</li>
<li>Just keep following in mind while assigning permissions.</li></ul>
<dl class="goodImage">
<dt>
<p>&#160;<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Group explained" src="/Standards/CodeAndApplicationDesign/RulesToBeterSharePoint/PublishingImages/AdditionalInfo.jpg" /></p>
<dt>
<dd>Figure&#58; Groups explained.</dd></dl>


