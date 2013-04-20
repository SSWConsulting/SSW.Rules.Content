---
type: rule
archivedreason: 
title: Do you use a Microsoft supported network setup for Hyper-V Clustering?
guid: c24c1d6e-4750-469e-aa6e-8c46c9bda91f
uri: do-you-use-a-microsoft-supported-network-setup-for-hyper-v-clustering
created: 2012-03-02T18:23:04.0000000Z
authors: []
related: []

---


<p>Microsoft lists several recommended and supported network configurations. It is very important that you configure your Hyper-V Cluster with one of the supported network types otherwise you will have performance issues once you load up the cluster.</p>
<br><excerpt class='endintro'></excerpt><br>
<img src="/PublishingImages/config-page.jpg" alt="Hyper-v configuration page" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Check you have one of the supported configurations listed on the <a href="http&#58;//technet.microsoft.com/en-us/library/ff428137%28WS.10%29.aspx">&gt;Microsoft Hyper-V Live Migration – Network Configuration</a> page (this example has 3 networks)</span>
<p>It may work fine initially on a non-supported configuration but when you start loading more Virtual Machines on to the cluster the performance will be degrade dramatically.</p>


