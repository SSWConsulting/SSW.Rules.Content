---
type: rule
archivedreason: 
title: Do you know that the VHD file will expand to the size of the partition inside the VHD when you boot into it?
guid: 71b7af02-6624-4208-8329-5bc9af55684c
uri: do-you-know-that-the-vhd-file-will-expand-to-the-size-of-the-partition-inside-the-vhd-when-you-boot-into-it
created: 2011-04-13T06:01:36.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---

When preparing a Boot to VHD image it is important to know the size of the partition which is setup inside the VHD file – you should make a note of this when you create the VHD image. The reason for this is because the VHD file will expand to the size of the partition  **INSIDE** the VHD.  
<!--endintro-->

For Example:

* A Windows installation called  **WindowsInVHD** inside the VHD file has a partition size of 60GB.
* It is copied to the D:\ drive of a laptop called  **Frog** and only takes up 10GB of space (as it is a dynamic expanding VHD).
* When you boot into  **WindowsInVHD** (the VHD sitting on  **Frog’s** D:\ drive), the VHD file expands to 60GB - the partition size of  ** WindowsInVHD. **
* This means you will need at least 60GB of free space on  **Frog’s** D:\ drive free


If you do not have free space equal to the size of the partition inside the VHD image, you will get a blue screen telling you that you are out of hard drive space.
