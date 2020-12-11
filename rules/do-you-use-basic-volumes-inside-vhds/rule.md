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


When formatting a new virtual disk you have attached to a Hyper-V Virtual Machine, you can choose to to format the disk as a <strong>Basic disk </strong>or <strong>Dynamic</strong> <strong>disk</strong>.<br>
<br>
A <strong>Dynamic</strong> <strong>disk </strong>might be useful in situations where you want to create a software RAID array, but when using Hyper-V this not a good idea because it prevents Microsoft Data Protection Manager (DPM) from doing Child State Backups (backups while the machine is running).<br>
<br>
For this reason, never use <strong>Dynamic disks </strong>inside Hyper-V Virtual Machines.<br>
<br>
<img alt="Bad Example - DPM cannot backup this Virtual Machine's child state as it has a Dynamic Disk" src="basicvolumes-badexample.jpg" /><br>
<font class="ms-rteCustom-FigureBad" size="+0">Figure: Bad Example - DPM cannot backup this Virtual Machine's child state as it has a Dynamic Disk<br>
</font><br>
<img alt="Good example – Using Basic Volumes allows DPM to backup the Virtual Machine’s child state" src="basicvolumes-goodexample.jpg" /><br>
<font class="ms-rteCustom-FigureGood" size="+0">Good example – Using Basic Volumes allows DPM to backup the Virtual Machine’s child state</font> 

<br><excerpt class='endintro'></excerpt><br>



