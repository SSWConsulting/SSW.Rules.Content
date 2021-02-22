---
type: rule
archivedreason: 
title: Do you snapshot Virtual Machines before big changes?
guid: 4c2176dd-f101-43c5-b472-62f567080ea3
uri: do-you-shut-down-a-virtual-machine-before-running-a-snapshot
created: 2011-02-14T06:18:58.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects:
- do-you-snapshot-virtual-machines-before-big-changes

---

Snapshots are a very easy way to back up a system before a big change is made. They can also be easily restored if something goes wrong during the change.

<!--endintro-->

1. In the  **Hyper-V Manager** , ensure the Virtual Machine has the state of  **Off**
2. Right click on the virtual machine you wish to snapshot and click  **Snapshot**
3. The snapshot should run very quickly and you will notice the snapshot in the  **Snapshots** area of the  **Hyper-V Manager

![You will see the snapshots associated with a Virtual Machine when you click on them](snapshot-while-off.jpg)**


::: good
**You will see the snapshots associated with a Virtual Machine when you click on them**
:::
