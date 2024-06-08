---
type: rule
archivedreason: 
title: Do you disable NetBIOS on all dedicated purpose adapters (iSCSI and Cluster Communications)?
guid: 44c7cc78-136b-4dba-953e-f592b8b3023a
uri: do-you-disable-netbios-on-all-dedicated-purpose-adapters-iscsi-and-cluster-communications
created: 2012-03-02T19:44:44.0000000Z
authors: []
related: []
redirects:
- do-you-disable-netbios-on-all-dedicated-purpose-adapters-(iscsi-and-cluster-communications)

---

To improve performance, it's a good idea to disable NetBIOS over TCP/IP on your cluster NIC and iSCSI NIC. NetBIOS isn't used in Server 2008 R2 clusters. 
<!--endintro-->
![Disable netBIOS](disable-netbios.jpg)Figure: Good example – the NetBIOS is disabled on the dedicated NIC's (iSCSI & Cluster Communications)
