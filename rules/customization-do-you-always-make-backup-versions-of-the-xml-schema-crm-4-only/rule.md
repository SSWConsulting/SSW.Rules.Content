---
seoDescription: When publishing XML schema in CRM 4, it's essential to maintain a versioning scheme and regularly back up the schema to avoid corruption. Export customizations from Settings > Customization > Export Customizations, naming files with dates for easy tracking.
type: rule
archivedreason:
title: Customization - Do you always make backup versions of the XML schema? (CRM 4 only)
guid: eb940a71-b172-409d-bbb4-d95eba36e8e5
uri: customization-do-you-always-make-backup-versions-of-the-xml-schema-crm-4-only
created: 2012-12-10T18:31:19.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - customization-do-you-always-make-backup-versions-of-the-xml-schema-(crm-4-only)
---

When the XML schema is published it re-generates the underlying SQL and .aspx code. If trouble hits, a "refresh" or "rollback" to an uncorrupted schema is always a backup plan. A versioning scheme is also required to keep track of different versions of the XML schema at different points in time. To make a backup of the schema from within Microsoft CRM navigate to Settings -&gt; Customization -&gt; Export Customizations. Browse to the location on your personal hard drive where the .XML file is to be stored.

<!--endintro-->

![Figure: Export customizations as backup](CRM_CustomizationPane.jpg)

**Tip #1:** Export only the customizations of entities that you customize and keep each entity customizations in a separate file, see the rule:[Customization](/customization-do-you-only-export-the-customizations-and-related-ones-that-you-have-made-only-for-crm-4-0) - Do you export only the customizations of entities that you did customize?

**Tip #2:** Put the date on the file names and while you are working you will be doing this multiple times a day.

**Tip #3:** don't save this on the Dev Virtual Machine.

In CRM 2011 we use Solutions and TFS Source Control.
