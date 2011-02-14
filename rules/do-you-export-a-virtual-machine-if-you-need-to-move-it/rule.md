---
type: rule
title: Do you export a Virtual Machine if you need to move it?
uri: do-you-export-a-virtual-machine-if-you-need-to-move-it
created: 2011-02-14T06:14:31.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> 
  <p>If you need to move a virtual machine from one Hyper-V server to another, you should using the Hyper-V Managers export option rather than just moving the VHD files. </p>
<p>If your machine has snapshots and you copy them rather than export them, it can cause issues with the VHD’s and AVHD’s (Snapshot VHD’s) because Hyper-V does not know there has been a snapshot when you load it onto the new Hyper-V Host. You also lose the settings for your Network Adapter, like its static IP address.</p>
 </span>

To export a Virtual Machine from the <strong>Hyper-V Manager</strong>&#58;<br>
<ol>
    <li>Right click on it when it is shut down and clicking <strong>Export...</strong></li>
    <li>Choose the location you wish to export the Virtual Machine to and click on <strong>Export</strong></li>
</ol>



