---
type: rule
title: Do you always use Site Columns instead of List Columns?
uri: do-you-always-use-site-columns-instead-of-list-columns
created: 2009-04-21T03:22:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>A site column is created on a site level and visible to all lists and content types within that site (and subsites). </p>
<p>You should always try to use Site Columns instead of List Columns</p>
 </span>


  <ul>
    <li>New in WSS v3 (SharePoint 2007) </li>
    <li>The same column can be added to different Content Types, lists, list templates </li>
    <li>Allows you to make modifications at one place and SharePoint can apply the changes for you across the different lists and content types (doesn't try to fix the content for you though) </li>
    <li>More visibility of the customization we are applying to the SharePoint website </li>
    <li>Make sure the site column is added to our own group description such as &quot;SSW Columns&quot; - this is important for filtering and exporting site column customizations for deployment.&#160; Also great because they are now grouped in the UI.</li>
</ul>
<dl class="badImage">
    <dt><img alt="" src="ListColumn.png" /> </dt>
    <dd>Figure&#58; Create column - Bad Example </dd>
</dl>
<dl class="goodImage">
    <dt><img alt="" src="SiteColumn.png" /> </dt>
    <dd>Figure&#58; Add from existing site columns - Good Example </dd>
</dl>
<dl class="goodImage">
    <dt><img alt="" src="SSWColumns_small.jpg" /> </dt>
    <dd>Figure&#58; Site Columns - Good Example </dd>
</dl>
<p>&#160;</p>
<p>&#160;</p>
<p>Sometimes you still may want to use a List Column.</p>
<ul>
    <li>You are Mary and want to create a simple list to track supplies, but you do not have site permissions to create site columns</li>
</ul>



