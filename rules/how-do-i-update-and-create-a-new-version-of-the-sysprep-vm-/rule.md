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



<br><excerpt class='endintro'></excerpt><br>
<p>When MS releases a new service pack, or new Windows update, we install these to the master image and create a new version of the Sysprep image for future VMs. </p>
<ol>
<li>Update SQL Server service packs 
<li>Update Windows Server 2003 service packs 
<li>Update Windows 
<li>Update VS.NET service packs 
<li>Update SharePoint service packs 
<li>Update MS Office SharePoint Designer service packs </li></ol>
<p>To create a new VM&#58; </p>
<ol>
<li>Make a copy of the master.vhd, rename it to the next version 
<li>Create a VM using this new vhd 
<li>Copy additional setup files to D&#58;\install\ 
<li>Modify the scripts in D&#58;\scripts\ 
<li>When finished, power down the VM. Make a copy of this and rename it to sysprep-vNext.vhd 
<li>Create a new VM using this new vhd 
<li>Start it up, and then run the sysprep command in D&#58;\sysprep\ 
<li>This will generalize the computer's settings and shut it down 
<li>Don't start up the VM again - or it'll run the start up scripts 
<li>Zz old copies of the master.vhd and sysprep.vhd </li></ol>


