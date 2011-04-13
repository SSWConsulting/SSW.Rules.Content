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



  <p>When preparing a Boot to VHD image it is important to know the size of the partition which is setup inside the VHD file – you should make a note of this when you create the VHD image. The reason for this is because the VHD file will expand to the size of the partition <strong>INSIDE </strong>the VHD.</p>
<p>For Example&#58;&#160;</p>
<ul>
    <li>A Windows installation called <strong>WindowsInVHD </strong>inside the VHD file has a partition size of 60GB. </li>
    <li>It is copied to the D&#58;\ drive of a laptop called <strong>Frog </strong>and only takes up 10GB of space (as it is a dynamic expanding VHD).&#160; </li>
    <li>When you boot into&#160;<strong>WindowsInVHD&#160;</strong>(the VHD sitting on <strong>Frog’s </strong>D&#58;\ drive), the VHD file expands to 60GB - the partition size of&#160;<strong><strong>WindowsInVHD.</strong></strong> </li>
    <li>This means you will need at least 60GB of free space on <strong>Frog’s </strong>D&#58;\ drive free </li>
</ul>
<p>If you do not have free space equal to the size of the partition inside the VHD image, you will get a blue screen telling you that you are out of hard drive space.</p>

<br><excerpt class='endintro'></excerpt><br>



