---
type: rule
archivedreason: 
title: Do you know how to include or exclude files when syncing a folder in Advanced Installer?
guid: 763c4bc1-669d-4ab9-b899-3656f4f3025b
uri: do-you-know-how-to-include-or-exclude-files-when-syncing-a-folder-in-advanced-installer
created: 2014-09-18T20:30:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects: []

---


<p class="p1">If you are syncing your Application Folder (or any other) with a local folder on a disk, you can specify which file or folders you want to sync. This is a very convenient way to keep your package smaller and clean.</p><p class="p1">Here is how you do it&#58;</p>
<br><excerpt class='endintro'></excerpt><br>
<ol class="ol1"><li class="li1">​Right click the 
      <strong>Application Folder</strong> and choose 
      <strong>Properties</strong></li><li class="li1">Click on Filters button to open the 
      <strong>Edit Filters</strong> dialog</li><li class="li1">Click on 
      <strong>New</strong> button to create Include pattern. Alternatively you can switch to 
      <strong>Exclude Filters</strong> tab</li><li class="li1">​Enter the Pattern and press 
      <strong>OK</strong> on each screen</li></ol><dl class="image"><dt><img src="/SoftwareDevelopment/RulesToBetterInstallers/PublishingImages/installers-include-exclude-1.jpg" alt="" /></dt><dd>Figure&#58; Edit Filters dialog</dd></dl><dl class="badImage"><dt><img src="/SoftwareDevelopment/RulesToBetterInstallers/PublishingImages/installers-include-exclude-2.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - Synced folder contains files that are not supposed to be deployed</dd></dl><dl class="goodImage"><dt><img src="/SoftwareDevelopment/RulesToBetterInstallers/PublishingImages/installers-include-exclude-3.jpg" alt="" /></dt><dd>Figure&#58; Good Example - Synced folder is filtered so that it includes only files we want to deploy</dd></dl>


