---
type: rule
archivedreason: 
title: Do you know how to identify customizations on SharePoint webs
guid: 492a7867-15ba-4d50-9edb-526dd375d39f
uri: do-you-know-how-to-identify-customizations-on-sharepoint-webs
created: 2013-04-24T03:14:17.0000000Z
authors:
- id: 9
  title: William Yin
related: []

---

To do a successful migration, you must find all the customizations in your current environment. 
<!--endintro-->

* Use command " **stsadm.exe -o enumallwebs -includefeatures -includewebparts >C:\checkcustomizations.txt** " to list all the features and webparts on webs.


1. Run this command on both your current Production environment and Test migration environment to get the list of features and web parts.
![](GetCustomFeaturesAndWebParts.jpg)
2. Use text comparision tool, such as BeyondCompare or WinDiff, to compare your Production envionment to your Test migration environment list to identify custom features and web part.


* Go to Central Admin site to check which custom WSP package has been deployed


1. Go to  **Central Admin site** |  **System Settings** |  **Manage farm solutions** , to look for deployed custom solution package.
![](CustomSolutionPackages.jpg)
2. Compare web.config files between Production and Test environment as well to identify custom controls.
