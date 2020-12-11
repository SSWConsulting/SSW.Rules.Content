---
type: rule
archivedreason: 
title: Do you do a pre-migration check on the SharePoint 2007 Server
guid: 07b8d204-ea81-4e1e-ab6b-5ff1295216d5
uri: do-you-do-a-pre-migration-check-on-the-sharepoint-2007-server
created: 2010-12-23T02:47:08.0000000Z
authors:
- id: 8
  title: John Liu
- id: 21
  title: Matthew Hodgkins
- id: 9
  title: William Yin
related: []

---

It is a good idea to run a pre-migration check on the SharePoint 2007 before starting the migration process.

1. Check you have followed [Do you add stsadm to the environmental variables?](/Pages/Do-you-add-stsadm-to-environmental-variables.aspx)
2. Open up  **cmd** with Administrator privileges
3. Run the following command:  **stsadm –o preupgradecheck

** 
![](preupgradecheck.png)**
<font class="ms-rteCustom-FigureNormal">Figure 3 - Check the pre-migration report. The only thing that is allowed to fail is “FeatureInfo”. This is because a custom feature won’t migrate and developers need to create a build targeted for SharePoint 2010</font>**
4. Save the HTML file that was generated and email it to your companies SharePoint Master. (Don’t print it as its very large)
5. Have the [SharePoint Master](/Pages/Do-you-have-a-SharePoint-Master.aspx) sign off on the pre-migration check and inform you if there are any site collections or content sources that are no longer needed and can be ignored for migration




<!--endintro-->
