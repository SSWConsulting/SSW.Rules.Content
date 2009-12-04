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



<br><excerpt class='endintro'></excerpt><br>
<p>When you want to create a SharePoint environment, you would need to create a new Virtual Machine from the SysPrep image. </p>
<ol>
<li>Make a copy of the latest version of sysprep.vhd and <b>do not run the base one</b> 
<ol>
<li>Rename sysprep.vhd so it will say what you are using it for.<br>e.g. client_project_v7.vhd 
<li>You will retain the version number so can we know from which sysprep.vhd it was made from </li></ol>
<li>In Hyper-V or Virtual PC, you create a new VM and link it to your copy of the sysprep.vhd 
<ol>
<li>You will need to allocate 2GB of RAM for this image 
<li>You will need plenty of hard drive space (at least 25GB to 30GB) 
<li>You will also need time - it is best to run this on a different machine if you plan to use your laptop at the same time when you are setting up this Virtual Machine </li></ol>
<li>You want to have the undo disk off initially, so that the installation commits changes directly to the VHD. Start the VM 
<li>Once the VM starts up, you will be asked to login - use our SharePoint dev password for the administrator account 
<li>Setup scripts will run for the administrator - this will rename the machine and install SQL Server 
<li>When the process is completed, the machine will restart, and prompt you to login again as the MOSSFarm account - use our SharePoint dev password for the MOSSFarm account 
<li>A second set of setup scripts will run for this account - this will install MOSS, SP1 
<li>When this is all done, you will power down the VM, and commit all changes to disk 
<ol>
<li>You will consider setting up either snapshots or undo-disk at this point.</li></ol></li></ol>


