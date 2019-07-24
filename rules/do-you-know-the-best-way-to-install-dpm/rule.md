---
type: rule
archivedreason: 
title: Do you know the best way to install DPM?
guid: 2c39840c-6e01-4707-8106-b62d287b18b1
uri: do-you-know-the-best-way-to-install-dpm
created: 2011-06-15T02:32:32.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
- id: 71
  title: Steven Andrews
- id: 19
  title: Sumesh Ghimire
related: []

---


It might make sense in your environment to install a DPM Server inside a Virtual Machine. While it is supported by Microsoft, there are a few limitations you need to be aware of.
<br>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>The Hyper-V role cannot be installed on the DPM server when it has been virtualized. This prevents you doing item level restores from inside Hyper-V virtual machines.</li><li>You are unable to use hardware tape libraries inside the Virtual Machine. You are still able to use iSCSI or Virtual Tape libraries though.</li></ul><p>Further to this, it is also recommend that you use iSCSI or Pass-Through disks if you are going to be using DPM inside a Virtual Machine. Using VHD’s in the storage pool is going to give you poor performance.<br></p>
<div class="greyBox">
   <p> 
      <strong>WARNING&#58; </strong>Although Microsoft recommend running the latest OS (being Windows Server 2019 and DPM 2019). SSW recommends Windows Server 2012 R2 with DPM 2019.&#160;<br></p><p>The reason for this is currently there are some known issues with the use of ReFS files structure in current versions of DPM (2016/2019). When installed on Windows Server 2016 and 2019 ReFS is used as default and there is no option given to use another file structure. The issues are causing backups to take exceptionally long times and in a lot of cases failing.&#160;E.g&#58;</p><ul><li>Exchange VM taking 100+ hours to backup and then failing when running Windows 2016 and DPM 2016</li><li>Exchange VM taking &lt;3 hours to backup when running Windows 2012&#160;R2 and DPM 2019<br></li></ul><p>Microsoft have released many updates to fix ReFS but people are still seeing issues, so it is recommended until this is resolved to continue operating DPM on Windows Server 2012 R2 as it allows you to continue using NTFS which is working without issues.​<br></p><p>Related link&#58;&#160;<a href="https&#58;//social.technet.microsoft.com/Forums/en-US/7e4e4da4-1168-46cd-900f-9ca2bc364d5a/dpm-2016-mbs-performance-downward-spiral">https&#58;//social.technet.microsoft.com/Forums/en-US/7e4e4da4-1168-46cd-900f-9ca2bc364d5a/dpm-2016-mbs-performance-downward-spiral​</a><br></p></div>


