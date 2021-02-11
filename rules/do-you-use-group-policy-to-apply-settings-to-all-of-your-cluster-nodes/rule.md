---
type: rule
archivedreason: 
title: Do you use Group Policy to Apply Settings to all of your Cluster Nodes?
guid: 9a9c8925-bfc8-4463-ae14-2b9daa471a3e
uri: do-you-use-group-policy-to-apply-settings-to-all-of-your-cluster-nodes
created: 2012-03-02T18:43:20.0000000Z
authors: []
related: []
redirects: []

---

Don't log in and make manual changes to the clustered nodes.

When working with clustered environments it is important that settings be consistent across every node. The best way to handle this is through group policy.

<!--endintro-->

Create a policy that you would like applied to each node of the cluster using the  **Group Policy Management** .
![Group policy bad](group-policy-bad.jpg)Figure: Bad Example - Do not manually change settings on each node![Group policy good](group-policy-good.jpg)Figure: Good Example - Changing settings through Group Policy keeps node settings the same
