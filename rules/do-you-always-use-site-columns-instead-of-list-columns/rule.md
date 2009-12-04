---
type: rule
archivedreason: 
title: Do you always use Site Columns instead of List Columns?
guid: 25745476-6892-4414-a8be-f3fa25c30f19
uri: do-you-always-use-site-columns-instead-of-list-columns
created: 2009-04-21T03:22:00.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
<ul>
<li>New in WSS v3 (SharePoint 2007) 
<li>The same column can be added to different Content Types, lists, list templates 
<li>Allows you to make modifications at one place and SharePoint can apply the changes for you across the different lists and content types (doesn't try to fix the content for you though) 
<li>More visibility of the customization we are applying to the SharePoint website 
<li>Make sure the site column is added to our own group description such as &quot;SSW Columns&quot; - this is important for filtering and exporting site column customizations for deployment.&#160; Also great because they are now grouped in the UI.</li></ul>
<dl class="badImage">
<dt><img src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/ListColumn.png" /></dt>
<dd>Figure&#58; Create column - Bad Example </dd></dl>
<dl class="goodImage">
<dt><img src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/SiteColumn.png" /></dt>
<dd>Figure&#58; Add from existing site columns - Good Example </dd></dl>
<dl class="goodImage">
<dt><img src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/SSWColumns_small.jpg" /></dt>
<dd>Figure&#58; Site Columns - Good Example </dd></dl>
<p></p>
<p>&#160;</p>
<p>Sometimes you still may want to use a List Column.</p>
<ul>
<li>You are Mary and want to create a simple list to track supplies, but you do not have site permissions to create site columns</li></ul>


