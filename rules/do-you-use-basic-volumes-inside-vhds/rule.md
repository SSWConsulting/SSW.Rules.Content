---
type: rule
archivedreason: 
title: Do you use Basic Volumes inside VHD's?
guid: 0c428023-a683-4a2c-98a7-71ba82f2432c
uri: do-you-use-basic-volumes-inside-vhds
created: 2011-02-14T03:23:59.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---

When formatting a new virtual disk you have attached to a Hyper-V Virtual Machine, you can choose to to format the disk as a  **Basic disk** or  **Dynamic** **disk** .

 A  **Dynamic** **disk** might be useful in situations where you want to create a software RAID array, but when using Hyper-V this not a good idea because it prevents Microsoft Data Protection Manager (DPM) from doing Child State Backups (backups while the machine is running).

 For this reason, never use  **Dynamic disks** inside Hyper-V Virtual Machines.


![](basicvolumes-badexample.jpg)
<font class="ms-rteCustom-FigureBad">Figure: Bad Example - DPM cannot backup this Virtual Machine's child state as it has a Dynamic Disk<br></font>

![](basicvolumes-goodexample.jpg)
<font class="ms-rteCustom-FigureGood">Good example – Using Basic Volumes allows DPM to backup the Virtual Machine’s child state</font>
<!--endintro-->
