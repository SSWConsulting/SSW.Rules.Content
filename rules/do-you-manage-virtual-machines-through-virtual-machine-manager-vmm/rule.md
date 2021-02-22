---
type: rule
archivedreason: 
title: Do you manage Virtual Machines through Virtual Machine Manager (VMM)?
guid: 8e37f938-704d-42d0-818a-ff4018d1c856
uri: do-you-manage-virtual-machines-through-virtual-machine-manager-vmm
created: 2019-10-18T00:15:26.0000000Z
authors: []
related: []
redirects:
- do-you-manage-virtual-machines-through-virtual-machine-manager-(vmm)

---

Virtual Machine Manager (VMM) is made for managing Virtual Machines (VM)!
Everything is easy to set up and deploy using VMM.

<!--endintro-->

You can provision VMs using a number of different approaches in VMM:

1. [Create VMs from a blank virtual disk](https&#58;//docs.microsoft.com/en-us/system-center/vmm/vm-blank-disk?view=sc-vmm-2019);
  2. [Create VMs from existing hard disks](https&#58;//docs.microsoft.com/en-us/system-center/vmm/vm-existing-disk?view=sc-vmm-2019);
  3. [Clone a VM from existing VM](https&#58;//docs.microsoft.com/en-us/system-center/vmm/vm-clone?view=sc-vmm-2019);
  4. [Create VM from a template](https&#58;//docs.microsoft.com/en-us/system-center/vmm/vm-template?view=sc-vmm-2019);
  5. Create VM in a service deployment;
  6. [Rapidly provision a VM using storage area network (SAN) copy](https&#58;//docs.microsoft.com/en-us/system-center/vmm/vm-san-copy?view=sc-vmm-2019).

You can also deploy VM guest clusters that acts as a failover cluster for your VMs, sharing the same .vhdx files as the main ones!

VMM uses an algorithm to intelligently place your newly created virtual machine on an available host, depending on a few factors:

1. CPU rating;
  2. RAM rating;
  3. Disk I/O rating;
  4. Network rating.

It then places the VM in the best host available for it.

VMM does this and much more for VMs, and you can read a bigger explanation [here](https&#58;//docs.microsoft.com/en-us/system-center/vmm/provision-vms?view=sc-vmm-2019).
