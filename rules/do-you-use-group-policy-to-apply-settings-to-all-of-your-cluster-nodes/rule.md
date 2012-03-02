---
type: rule
archivedreason: 
title: Do you use Group Policy to Apply Settings to all of your Cluster Nodes?
guid: 9a9c8925-bfc8-4463-ae14-2b9daa471a3e
uri: do-you-use-group-policy-to-apply-settings-to-all-of-your-cluster-nodes
created: 2012-03-02T18:43:20.0000000Z
authors: []
related: []

---


<p>Don't log in and make manual changes to the clustered nodes.</p>
<p>When working with clustered environments it is important that settings be consistent across every node. The best way to handle this is through group policy.
</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Create a policy that you would like applied to each node of the cluster using the <strong>Group Policy Management</strong>.</p>
<img class="ms-rteCustom-ImageArea" alt="Group policy bad" src="/ITAndNetworking/Rules-to-Better-Hyper-V-Clustering/PublishingImages/group-policy-bad.jpg" />
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Do not manually change settings on each node</span>

<img class="ms-rteCustom-ImageArea" alt="Group policy good" src="/ITAndNetworking/Rules-to-Better-Hyper-V-Clustering/PublishingImages/group-policy-good.jpg" />
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example - Changing settings through Group Policy keeps node settings the same</span>


