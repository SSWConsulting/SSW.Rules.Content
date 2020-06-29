---
type: rule
title: Do you use Group Policy to Apply Settings to all of your Cluster Nodes?
uri: do-you-use-group-policy-to-apply-settings-to-all-of-your-cluster-nodes
created: 2012-03-02T18:43:20.0000000Z
authors: []

---



<span class='intro'> <p>Don't log in and make manual changes to the clustered nodes.</p>
<p>When working with clustered environments it is important that settings be consistent across every node. The best way to handle this is through group policy.
</p> </span>

<p>Create a policy that you would like applied to each node of the cluster using the <strong>Group Policy Management</strong>.</p>
<img src="group-policy-bad.jpg" alt="Group policy bad" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Do not manually change settings on each node</span>

<img src="group-policy-good.jpg" alt="Group policy good" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example - Changing settings through Group Policy keeps node settings the same</span>


