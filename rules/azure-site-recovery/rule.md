---
type: rule
title: Redundancy - Do you use Azure Site Recovery?
uri: azure-site-recovery
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kiki
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwickleahy
created: 2021-10-14T04:11:36.379Z
guid: 48e1b450-5254-490a-bade-564c390bfb59
---
Azure Site Recovery is the best way to ensure business continuity by keeping business apps and workloads running during outages. It is one of the fastest ways to get redundancy for your VMs on a secondary location.

<!--endintro-->

Ensuring business continuity is priority for the System Administrator team, and is part of any good disaster recovery plan. Azure Site Recovery allows an organization to replicate and sync Virtual Machines from on-premises (or even different Azure regions) to Azure.  This replication can be set to whatever frequency the organization deems to be required, from Daily/Weekly through to constant replication.

This way when there is an issue, restoration can be in minutes - you just switch over to the VMs in Azure! They will keep the business running while the crisis is dealt with. The server will be in the same state as the last backup.  Or if the issue is software you can restore an earlier version of the virtual machine within a few minutes as well.  

![Figure: Azure Backup and Site Recovery backs up on-premises and Azure Virtual Machines](azurebackup.png)