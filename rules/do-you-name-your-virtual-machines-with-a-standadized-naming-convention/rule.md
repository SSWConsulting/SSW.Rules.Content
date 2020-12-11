---
type: rule
archivedreason: 
title: Do you name your Virtual Machines with a standadized naming convention?
guid: 95d89bf5-a456-4ccf-b636-5bd7e56300f6
uri: do-you-name-your-virtual-machines-with-a-standadized-naming-convention
created: 2011-02-14T05:06:05.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
related: []

---

When your Hyper-V environment is spread across multiple hosts and contains many Virtual Servers, it can get very confusing to find the one you are looking for amongst them all. This is why you should use a standard naming convention for all your Virtual machines.  
<!--endintro-->

![Bad](naming-badexample.jpg)

**NetBIOSName-ServiceName

** For example:  **Falcon-SCVMM
** 
 The standard we use for Development Virtual Machine naming is as follows:

**DEV-NetBIOSName-ServiceName-DeveloperInitials
** 
     For example:  **DEV-demo2010a-SP2010MSInfoWorker-JL** 


![](naming-goodexample.jpg)
<font class="ms-rteCustom-FigureGood">Good Example - It is easy to tell which VM is which when they are named to a standard<br></font>
