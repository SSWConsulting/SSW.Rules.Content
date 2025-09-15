---
seoDescription: Configure your nodes identically to run Failover Cluster Manager efficiently and effectively, ensuring seamless virtual machine management.
type: rule
archivedreason:
title: Do you only use your nodes for Virtual Machine Management?
guid: 3b623c87-c003-4c25-bc46-1e8b63f94347
uri: do-you-make-sure-all-of-your-nodes-are-all-domain-controllers
created: 2012-03-02T19:35:14.0000000Z
authors: []
related: []
redirects:
  - do-you-only-use-your-nodes-for-virtual-machine-management
---

When setting up Failover Cluster Manager it is important that each Physical Machine, also known as a host or node be setup in an identical manner. This means each machine should be configured the same, with the same networks and same workloads running.

It is best practice to have your nodes only running the necessary features to run Failover Cluster Manager, leaving your VMs or other hosts not in the cluster to run everything else.

For this reason SSW recommends only running Failover Cluster Manager and Hyper-V roles on your nodes. It is also recommended that each node in the cluster is identical hardware, this is not strictly required but will assist in the ease of management.

<!--endintro-->
