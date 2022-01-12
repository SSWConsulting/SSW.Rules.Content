---
type: rule
archivedreason: 
title: Do you know where to keep your design files?
guid: 77730639-c6a0-490a-8892-a96e56b25f7d
uri: where-to-keep-your-design-files
created: 2014-03-03T04:11:03.0000000Z
authors:
- title: Rebecca Liu
  url: https://ssw.com.au/people/rebecca-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ken Shi
  url: https://ssw.com.au/people/ken-shi
related:
- software-for-product-design
- hand-over-mockups-to-developers
- version-control-software-for-designers
redirects: 
- do-you-know-the-best-source-control-for-designers

---

Design files should never be stored in Azure DevOps (was VSTS/TFS) or any other development file system.

<!--endintro-->

::: bad  
![Figure: Bad example – Azure DevOps (was VSTS/TFS) takes too long to set up and too slow to use](Designer-Source-Control-TFS.png)  
:::

::: good  
![Figure: Good Example – Dropbox or OneDrive](Designer-Source-Control-DropBox.png)  
:::

::: good  
![Figure: Good Example – OneDrive and Teams](Teamsfiles.png)  
:::

::: china
Google Drive and Dropbox don’t work in China, so SSW prefers to use OneDrive.
:::

For developers, see [Do you know where to keep your files?](/do-you-know-where-to-keep-your-files)
