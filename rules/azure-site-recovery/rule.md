---
type: rule
title: Backups - Do you use Azure Site Recovery?
uri: azure-site-recovery
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kiki
created: 2021-10-14T04:11:36.379Z
guid: 48e1b450-5254-490a-bade-564c390bfb59
---
Azure Site Recovery helps ensure business continuity by keeping business apps and workloads running during outages. It is one of the fastest ways to get redundancy for your VMs on a secondary location.

<!--endintro-->

Ensuring business continuity is priority for the System Administrator team, and is part of any good disaster recovery plan. Azure Site Recovery helps with this by replicating and syncing Virtual Machines from on-premises (or even different Azure regions) to Azure.

This means that, in case of a disaster, there will be no need to go for backups - you just switch over to the VMs in Azure! They will keep the business running while the on-premises crisis is dealt with. This is your redundancy working, the machines are in the same state they were when they went down. Nothing is being recovered, only continued in another location.

![Figure: Azure Site Recovery](https://i.ytimg.com/vi/rKKiiHOuV74/hqdefault.jpg)