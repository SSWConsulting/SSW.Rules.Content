---
type: rule
title: Do you have the iSCSI and Cluster networks on their own VLAN (or even better their own switch)?
uri: do-you-have-the-iscsi-and-cluster-networks-on-their-own-vlan-or-even-better-their-own-switch
created: 2012-03-02T18:28:49.0000000Z
authors: []

---



<span class='intro'> Having the network flooded with a virus is bad news – but it will be worse news if iSCSI traffic is going across the same network. This is why you should have your iSCSI or SAN traffic on a different VLAN.  </span>

<img class="ms-rteCustom-ImageArea" alt="VLAN" src="/ITAndNetworking/Rules-to-Better-Hyper-V-Clustering/PublishingImages/vlan.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; A managed switch allows VLANing</span>
<p>Note&#58; An even better and more expensive solution is purchase a separate Switch for each network (this example means 3 network adapters = 3 networks)</p>



