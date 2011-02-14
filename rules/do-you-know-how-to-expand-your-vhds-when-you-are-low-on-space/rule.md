---
type: rule
archivedreason: 
title: Do you know how to expand your VHD's when you are low on space?
guid: 94272c6a-c684-4304-9bf8-66dab586fa97
uri: do-you-know-how-to-expand-your-vhds-when-you-are-low-on-space
created: 2011-02-14T03:46:30.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---


Occasionally when you estimate the size of a VHD that you will be using in a server, you can get it wrong and you will need to give the Virtual Machine some more space. Instead of adding a bigger data disk in the Virtual Machine and migrating data, you can expand the existing disk.

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Open the &quot;Hyper-V Manager&quot; on the server hosting the Virtual Machine</li>
    <li>Shutdown the virtual machine</li>
    <li>Click <strong>Edit Disk...</strong> in the <strong>Actions </strong>pane of the <strong>Hyper-V Manager<br>
    <img alt="You expand a VHD from the Actions Menu | Edit Disk" src="/ITAndNetworking/RulesToBetterHyperV/PublishingImages/actions-expand.jpg" /><br>
    </strong><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; You expand a VHD from the Actions Menu | Edit Disk</font></li>
    <li>In the <b>Edit Virtual Hard Disk Wizard</b> window, choose the VHD you want to edit and choose <b>Next</b>.&lt;\li&gt; </li>
    <li>Select <b>Expand</b> and click <b>Next</b></li>
    <li>Enter the new size of the VHD and click <b>Next</b></li>
</ol>
<p>You will now have a resized VHD. Next step is to boot up into the virtual machine and tell disk manager to resize the partition on the VHD to use the free space which has been added at the end of the VHD. Windows Server 2008 makes this very simple&#58; </p>
<p>&#160;</p>
<ol>
    <li>Boot into the virtual machine </li>
    <li>Open <b>Computer Management</b> and choose <b>Disk Management</b> </li>
    <li>Right click on the partition sitting at the front of the newly resized disk and click on <b>Extend Volume...<br>
    <img alt="The first partition on the disk needs to be expanded to use up the unallocated space created when expanding the VHD" src="/ITAndNetworking/RulesToBetterHyperV/PublishingImages/expand-freespace.jpg" /><br>
    </b><font class="ms-rteCustom-FigureNormal" size="+0"><b>Figure&#58; The first partition on the disk needs to be expanded to use up the unallocated space created when expanding the VHD</b></font> </li>
    <li>4.&#160;You will have to use all the available space when you extend the volume as it is a Simple Volume. (See Rule&#58; <a shape="rect" href="/ITAndNetworking/RulesToBetterHyperV/Pages/Do-you-use-Basic-Volumes-inside-VHDs.aspx">Do you use Basic Volumes inside VHD’s? </a>) When you are asked to select your disks just click <strong>Next</strong></li>
    <li>Click <strong>Finish<br>
    <img alt="The disk is now using all the available space inside the VHD " src="/ITAndNetworking/RulesToBetterHyperV/PublishingImages/expand-fullspaceused.jpg" /></strong></li>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; The disk is now using all the available space inside the VHD</font></ol>



