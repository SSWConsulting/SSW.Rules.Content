---
type: rule
archivedreason: 
title: Do you export a Virtual Machine if you need to move it?
guid: 2ea30567-a9d5-406a-ab47-ee6ae4e7ff1c
uri: do-you-export-a-virtual-machine-if-you-need-to-move-it
created: 2011-02-14T06:14:31.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---

If you need to move a virtual machine from one Hyper-V server to another, you should using the Hyper-V Managers export option rather than just moving the VHD files.

If your machine has snapshots and you copy them rather than export them, it can cause issues with the VHD’s and AVHD’s (Snapshot VHD’s) because Hyper-V does not know there has been a snapshot when you load it onto the new Hyper-V Host. You also lose the settings for your Network Adapter, like its static IP address.

<!--endintro-->
 To export a Virtual Machine from the  **Hyper-V Manager** :

1. Right click on it when it is shut down and clicking  **Export...**
2. Choose the location you wish to export the Virtual Machine to and click on  **Export**
