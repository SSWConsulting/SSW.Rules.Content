

---
authors:

---




<span class='intro'> <p>Don't log in and make manual changes to the clustered nodes.</p>
<p>When working with clustered environments it is important that settings be consistent across every node. The best way to handle this is through group policy.
</p> </span>

<p>Create a policy that you would like applied to each node of the cluster using the <strong>Group Policy Management</strong>.</p>
<img class="ms-rteCustom-ImageArea" alt="Group policy bad" src="/ITAndNetworking/Rules-to-Better-Hyper-V-Clustering/PublishingImages/group-policy-bad.jpg" />
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Do not manually change settings on each node</span>

<img class="ms-rteCustom-ImageArea" alt="Group policy good" src="/ITAndNetworking/Rules-to-Better-Hyper-V-Clustering/PublishingImages/group-policy-good.jpg" />
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example - Changing settings through Group Policy keeps node settings the same</span>


