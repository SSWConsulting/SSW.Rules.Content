---
seoDescription: Learn how to include or exclude files when syncing a folder in Advanced Installer, and keep your package organized and clean.
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

If you are syncing your Application Folder (or any other) with a local folder on a disk, you can specify which file or folders you want to sync. This is a very convenient way to keep your package smaller and clean.

Here is how you do it:

<!--endintro-->

1. Right click the
   **Application Folder** and choose
   **Properties**
2. Click on Filters button to open the
   **Edit Filters** dialog
3. Click on
   **New** button to create Include pattern. Alternatively you can switch to
   **Exclude Filters** tab
4. Enter the Pattern and press
   **OK** on each screen

![Figure: Edit Filters dialog](installers-include-exclude-1.jpg)

::: bad  
![Figure: Bad Example - Synced folder contains files that are not supposed to be deployed](installers-include-exclude-2.jpg)  
:::

::: good  
![Figure: Good Example - Synced folder is filtered so that it includes only files we want to deploy](installers-include-exclude-3.jpg)  
:::
