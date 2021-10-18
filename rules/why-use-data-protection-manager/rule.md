---
type: rule
title: Do you know why to use Data Protection Manager (DPM)?
uri: why-use-data-protection-manager
authors:
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
  - title: Kaique Biancatti
    url: https://www.ssw.com.au/people/kiki
related: []
redirects:
  - do-you-know-why-to-use-data-protection-manager-dpm
  - do-you-know-why-to-use-data-protection-manager-(dpm)
created: 2019-07-24T21:37:04.000Z
archivedreason: null
guid: d828541d-d6cb-4d99-a4c6-778c78e07259
---
Every company needs a business continuity and disaster recover plan. DPM is a robust backup solution used in many enterprises it can give you piece of mind knowing that your data is backed up, safe and easily restorable. It allows for backing up of:

<!--endintro-->

* Hyper-V
* Physical Machines
* Application Aware Backups

  * Exchange
  * SQL
  * SharePoint

It also allows for storage over many platforms:

* Disk
* Tape
* Cloud

DPM is great for the above tasks, but for off-site backups or cloud backups, other tools are best. You generally need to set up a physical machine with enough storage for DPM, so for file servers, an auto-expanding cloud backup is better e.g. MSP360 (was CloudBerry) and Backblaze.

![Figure: Good Example - Use MSP360 (was CloudBerry) with Backblaze for easy cloud backups](cloudberry.jpg)

It is fast and easy to recover VMs and files from DPM, making this the best tool to have your local backups on. 

It is also important to keep DPM backups healthy by monitoring their status frequently.

![Figure: Good Example - DPM - Healthy backups show green ticks](ppaspsappic.png)