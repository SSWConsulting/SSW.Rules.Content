---
type: rule
archivedreason: 
title: Do you manage Windows Update Services through Virtual Machine manager (VMM)?
guid: cf88f229-4e5a-4127-8a5a-cbab098c2b37
uri: do-you-manage-windows-update-services-through-virtual-machine-manager-vmm
created: 2019-10-17T23:27:29.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-manage-windows-update-services-through-virtual-machine-manager-(vmm)

---

You can use Virtual Machine Manager (VMM) to manage your Windows Update Services (WSUS) directly, instead of using the server management itself.

<!--endintro-->

To find full explained instructions on how to set this up, see [here](https&#58;//docs.microsoft.com/en-us/system-center/vmm/update-server?view=sc-vmm-2019).

Before starting, you should take some things into consideration:

1. The WSUS server must be in the same domain as the VMM server;
  2. Best practices dictates that you should use a separate server to be a WSUS server;
  3. After you add a WSUS server to VMM, you should use the VMM console to manage it, and not the WSUS console.

After taking these into consideration, you can start deploying update baselines, which contains a set of required updates scoped to objects, and adding update exemptions as necessary.
