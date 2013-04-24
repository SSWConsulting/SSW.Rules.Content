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
<br><excerpt class='endintro'></excerpt><br>
<ul><li>Use command &quot;<strong>stsadm.exe -o enumallwebs -includefeatures -includewebparts &gt;C&#58;\checkcustomizations.txt</strong>&quot; to list all the features and webparts on webs.</li></ul><span style="line-height&#58;21px;"><ol><li>Run this command on both your current Production environment and Test migration environment to get the list of features and web parts.<img src="/PublishingImages/GetCustomFeaturesAndWebParts.jpg" alt="GetCustomFeaturesAndWebParts.jpg" class="ssw-rteStyle-ImageArea" style="margin-right&#58;5px;margin-left&#58;5px;width&#58;593px;" /></li><li>Use text comparision tool, such as BeyondCompare or WinDiff, to compare your Production envionment to your Test migration environment list to identify custom features and web part.</li></ol></span><span style="line-height&#58;21px;"><ul><li>Go to Central Admin site to check which custom WSP package has been deployed<br></li></ul></span><span style="line-height&#58;21px;"><ol><li>Go to <strong>Central Admin site</strong> | <strong>System Settings</strong> |&#160;<strong>Manage farm solutions</strong>, to look for deployed custom solution package.<img src="/PublishingImages/CustomSolutionPackages.jpg" alt="CustomSolutionPackages.jpg" class="ssw-rteStyle-ImageArea" style="margin-right&#58;5px;margin-left&#58;5px;width&#58;593px;" /></li><li><span style="line-height&#58;21px;">Compare web.config files&#160;between Production and Test environment as well to identify custom controls.</span></li></ol></span>


