---
type: rule
archivedreason: 
title: Do you always use Site Columns instead of List Columns?
guid: 25745476-6892-4414-a8be-f3fa25c30f19
uri: do-you-always-use-site-columns-instead-of-list-columns
created: 2009-04-21T03:22:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 1
  title: Adam Cogan
related: []

---

A site column is created on a site level and visible to all lists and content types within that site (and subsites).

You should always try to use Site Columns instead of List Columns

<!--endintro-->

* New in WSS v3 (SharePoint 2007)
* The same column can be added to different Content Types, lists, list templates
* Allows you to make modifications at one place and SharePoint can apply the changes for you across the different lists and content types (doesn't try to fix the content for you though)
* More visibility of the customization we are applying to the SharePoint website
* Make sure the site column is added to our own group description such as "SSW Columns" - this is important for filtering and exporting site column customizations for deployment.  Also great because they are now grouped in the UI.

<dl class="badImage">    &lt;dt&gt;<img alt="" src="ListColumn.png"> &lt;/dt&gt;
    <dd>Figure: Create column - Bad Example </dd></dl><dl class="goodImage">    &lt;dt&gt;<img alt="" src="SiteColumn.png"> &lt;/dt&gt;
    <dd>Figure: Add from existing site columns - Good Example </dd></dl><dl class="goodImage">    &lt;dt&gt;<img alt="" src="SSWColumns_small.jpg"> &lt;/dt&gt;
    <dd>Figure: Site Columns - Good Example </dd></dl>




Sometimes you still may want to use a List Column.

* You are Mary and want to create a simple list to track supplies, but you do not have site permissions to create site columns
