---
type: rule
archivedreason: 
title: Do you have the iSCSI and Cluster networks on their own VLAN (or even better their own switch)?
guid: 880d650c-1182-48bf-b1c7-ffc9bc2ab055
uri: do-you-have-the-iscsi-and-cluster-networks-on-their-own-vlan-or-even-better-their-own-switch
created: 2012-03-02T18:28:49.0000000Z
authors: []
related: []
redirects:
- do-you-have-the-iscsi-and-cluster-networks-on-their-own-vlan-(or-even-better-their-own-switch)

---

Having the network flooded with a virus is bad news – but it will be worse news if iSCSI traffic is going across the same network. This is why you should have your iSCSI or SAN traffic on a different VLAN.  
<!--endintro-->
![VLAN](switch-for-vlan.jpg)**Figure: A managed switch allows VLANing** 
Note: An even better and more expensive solution is purchase a separate Switch for each network (this example means 3 network adapters = 3 networks)
