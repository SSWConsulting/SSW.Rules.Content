---
type: rule
title: Customization - Do you always make backup versions of the XML schema? (CRM 4 only)
uri: customization---do-you-always-make-backup-versions-of-the-xml-schema-crm-4-only
created: 2012-12-10T18:31:19.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>When the XML schema is published it re-generates the underlying SQL and .aspx code. If trouble hits, a &quot;refresh&quot; or &quot;rollback&quot; to an uncorrupted schema is always a backup plan. A versioning scheme is also required to keep track of different versions of the XML schema at different points in time. To make a backup of the schema from within Microsoft CRM navigate to Settings -&gt; Customization -&gt; Export Customizations. Browse to the location on your personal hard drive where the .XML file is to be stored. </p> </span>

<dl class="image"><dt><img alt="Microsoft CRM Customization Pane" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_CustomizationPane.jpg" /></dt>
<dd>Figure&#58; Export customizations as backup </dd></dl>
<p><strong>Tip #1&#58;</strong> Export only the customizations of entities that you customize and keep each entity customizations in a separate file, see the rule&#58;<a href="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/Pages/Only-export-the-customizations-and-related-ones-that-you-have-made.aspx">Customization</a><span></span><span> - Do you export only the customizations of entities that you did customize?</span></p>
<p><strong>Tip #2&#58;</strong> Put the date on the file names and while you are working you will be doing this multiple times a day. </p>
<p><strong>Tip #3&#58;</strong> don't save this on the Dev Virtual Machine. </p>


