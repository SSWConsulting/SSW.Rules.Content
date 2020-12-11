---
type: rule
archivedreason: 
title: Do you know how to specify a Network for Live Migration?
guid: 7b758bc3-ccb7-4bc9-ba37-9df0e5210be4
uri: do-you-know-how-to-specify-a-network-for-live-migration
created: 2012-03-02T18:56:38.0000000Z
authors: []
related: []

---

It is important have the Live Migration and Cluster traffic on a separate network interface than the iSCSI or SAN traffic. If you do not you will see a performance hit while migrating virtual machines and the process will be a lot slower.

<!--endintro-->

To specify the roles of each network adapter:

1. Open the Failover Cluster Manager
2. Expand the Networks section and you will see all of your network adapters listed
3. Right click on the network that you are using for LAN and ISCSI and make sure that the following setting is selected


![Network properties window](cluster-network.jpg)
This setting prevents ISCSI and LAN traffic from going over the cluster network
