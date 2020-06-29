---
type: rule
title: Do you know how to specify a Network for Live Migration?
uri: do-you-know-how-to-specify-a-network-for-live-migration
created: 2012-03-02T18:56:38.0000000Z
authors: []

---



<span class='intro'> <p>It is important have the Live Migration and Cluster traffic on a separate network interface than the iSCSI or SAN traffic. If you do not you will see a performance hit while migrating virtual machines and the process will be a lot slower.</p> </span>

<p>To specify the roles of each network adapter&#58;</p>
<ol>
<li>Open the Failover Cluster Manager</li>
<li>Expand the Networks section and you will see all of your network adapters listed</li>
<li>Right click on the network that you are using for LAN and ISCSI and make sure that the following setting is selected</li>
</ol>
<img src="cluster-network.jpg" alt="Network properties window" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Network properties window</span>

<p>This setting prevents ISCSI and LAN traffic from going over the cluster network</p>



