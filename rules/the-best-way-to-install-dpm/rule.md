---
type: rule
archivedreason: 
title: Do you know the best way to install DPM?
guid: 2c39840c-6e01-4707-8106-b62d287b18b1
uri: the-best-way-to-install-dpm
created: 2011-06-15T02:32:32.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
- title: Sumesh Ghimire
  url: https://ssw.com.au/people/sumesh-ghimire
related: []
redirects:
- do-you-know-the-limitations-when-installing-dpm-as-a-virtual-machine
- do-you-know-the-best-way-to-install-dpm

---


It might make sense in your environment to install a DPM Server inside a Virtual Machine. While it is supported by Microsoft, there are a few limitations you need to be aware of.

<br><excerpt class='endintro'></excerpt><br>

  <ul>
    <li>The Hyper-V role cannot be installed on the DPM server when it has been virtualized. This prevents you doing item level restores from inside Hyper-V virtual machines.</li>
    <li>You are unable to use hardware tape libraries inside the Virtual Machine. You are still able to use iSCSI or Virtual Tape libraries though.</li>
</ul>
<p>Further to this, it is also recommend that you use iSCSI or Pass-Through disks if you are going to be using DPM inside a Virtual Machine. Using VHD’s in the storage pool is going to give you poor performance.</p>



