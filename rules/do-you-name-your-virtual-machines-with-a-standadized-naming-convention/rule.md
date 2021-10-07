---
type: rule
archivedreason: 
title: Do you name your Virtual Machines with a standardized naming convention?
guid: 95d89bf5-a456-4ccf-b636-5bd7e56300f6
uri: name-your-virtual-machines-with-a-standardized-naming-convention
created: 2011-02-14T05:06:05.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
related: []
redirects: 
- do-you-name-your-virtual-machines-with-a-standadized-naming-convention
- do-you-name-your-virtual-machines-with-a-standardized-naming-convention

---

When your Hyper-V environment is spread across multiple hosts and contains many Virtual Servers, it can get very confusing to find the one you are looking for amongst them all. This is why you should use a standard naming convention for all your Virtual machines.  

<!--endintro-->

::: bad
![Bad Example - How do you know what machine is what?](naming-badexample.jpg)
:::

The standard we use for Production Virtual Machine naming is as follows: **NetBIOSName-ServiceName**.  
For example: **Falcon-SCVMM**.

The standard we use for Development Virtual Machine naming is as follows: **DEV-NetBIOSName-ServiceName-DeveloperInitials**.  
For example: **DEV-demo2010a-SP2010MSInfoWorker-JL**.

::: good
![Good Example - It is easy to tell which VM is which when they are named to a standard](naming-goodexample.jpg)
:::
