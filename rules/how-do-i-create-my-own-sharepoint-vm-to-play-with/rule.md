---
type: rule
archivedreason: 
title: How do I create my own SharePoint VM to play with?
guid: 5128143d-5814-4a74-a5d2-012015224cb1
uri: how-do-i-create-my-own-sharepoint-vm-to-play-with
created: 2009-02-26T02:03:39.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

When you want to create a SharePoint environment, you would need to create a new Virtual Machine from the SysPrep image.  
<!--endintro-->

When you want to create a SharePoint environment, you would need to create a new Virtual Machine from the SysPrep image.

1. Make a copy of the latest version of sysprep.vhd and  **do not run the base one**
    1. Rename sysprep.vhd so it will say what you are using it for.
e.g. client\_project\_v7.vhd
    2. You will retain the version number so can we know from which sysprep.vhd it was made from
2. In Hyper-V or Virtual PC, you create a new VM and link it to your copy of the sysprep.vhd
    1. You will need to allocate 2GB of RAM for this image
    2. You will need plenty of hard drive space (at least 25GB to 30GB)
    3. You will also need time - it is best to run this on a different machine if you plan to use your laptop at the same time when you are setting up this Virtual Machine
3. You want to have the undo disk off initially, so that the installation commits changes directly to the VHD. Start the VM
4. Once the VM starts up, you will be asked to login - use our SharePoint dev password for the administrator account
5. Setup scripts will run for the administrator - this will rename the machine and install SQL Server
6. When the process is completed, the machine will restart, and prompt you to login again as the MOSSFarm account - use our SharePoint dev password for the MOSSFarm account
7. A second set of setup scripts will run for this account - this will install MOSS, SP1
8. When this is all done, you will power down the VM, and commit all changes to disk
    1. You will consider setting up either snapshots or undo-disk at this point.
