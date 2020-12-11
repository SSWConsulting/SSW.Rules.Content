---
type: rule
archivedreason: 
title: How do I update and create a new version of the Sysprep VM ?
guid: 77fa8f08-6e60-416b-a334-0e7ff792dd51
uri: how-do-i-update-and-create-a-new-version-of-the-sysprep-vm-
created: 2009-02-26T02:03:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

When MS releases a new service pack, or new Windows update, we install these to the master image and create a new version of the Sysprep image for future VMs.  
<!--endintro-->

1. Update SQL Server service packs
2. Update Windows Server 2003 service packs
3. Update Windows
4. Update VS.NET service packs
5. Update SharePoint service packs
6. Update MS Office SharePoint Designer service packs


To create a new VM:

1. Make a copy of the master.vhd, rename it to the next version
2. Create a VM using this new vhd
3. Copy additional setup files to D:\install\
4. Modify the scripts in D:\scripts\
5. When finished, power down the VM. Make a copy of this and rename it to sysprep-vNext.vhd
6. Create a new VM using this new vhd
7. Start it up, and then run the sysprep command in D:\sysprep\
8. This will generalize the computer's settings and shut it down
9. Don't start up the VM again - or it'll run the start up scripts
10. Zz old copies of the master.vhd and sysprep.vhd
