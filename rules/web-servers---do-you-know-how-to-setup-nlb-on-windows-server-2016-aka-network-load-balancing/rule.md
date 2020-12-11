---
type: rule
archivedreason: 
title: Web Servers - Do you know how to Setup NLB on Windows Server 2016? (aka Network Load Balancing)
guid: c500d5e7-736c-47a8-a3bc-4e6f6bccf229
uri: web-servers---do-you-know-how-to-setup-nlb-on-windows-server-2016-aka-network-load-balancing
created: 2011-11-14T15:08:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 21
  title: Matthew Hodgkins
related: []

---

Downtime occurs when you have a single server setup.

**TODO: This is 2008 R2 – update to 2016** 
 **Note:** 2008 R2 was not as reliable as later versions. So it would be better to use failover cluster in Server 2012 R2 or 2016 for a more reliable infrastructure configuration.

Use NLB to allow load balancing and failover. On each of your Windows Servers, you will host your website.

You need to follow these steps to get it up and running:

<!--endintro-->

1. On all nodes of the NBL cluster, the Network Load Balancing Feature needs to be installed.

![Install the NLB Feature](NLB1.png)
2. Open the Network Load Balancing Manager from Administrative Tools

![Under the Cluster menu item, click New](NLB22.png)
3. Enter the first node in the cluster in ‘Host’ and press ‘Connect’

![Select the interface for the node](NLB33.png)
4. Enter a Priority as 1 (this is just a host identifier)

![In 'Priority' enter '1'](NLB44.png)
5. 
![Enter a virtual IP address for the cluster. eg. 192.168.1.12](NLB55.png)
6. Choose the IP address of your cluster from the dropdown list Set a Full Internet Name eg. spcluster.sydney.ssw.com.au. 
Ensure the Multicast Cluster operation mode is selected.

![Set the 3 cluster parameters](NLB66.png)
7. You want sticky sessions so you don’t mistakenly bounce between servers (and lose your state)

![Leave the Port Rule as default. This will provide sticky session](NLB77.png)

![Success. The cluster configuration will show a green icon](NLB88.png)
8. Right click the name of the cluster eg. spcluster.sydney.ssw.com.au Click Add Host To Cluster

![Add the 2nd web server with a priority of 2](NLB99.png)
9. Open a command prompt and type in wlbs query to verify the cluster:

![Type in wlbs query to verify the cluster](Setup-NLB-13.jpg)
10. Ping both nodes and the virtual IP address externally to verify they are all working
