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


<p>Downtime occurs when you have a single server setup.<br></p><p class="ssw15-rteElement-InfoBox"><b>TODO: This is 2008 R2 – update to 2016</b><br><b>Note: </b>2008 R2 was not as reliable as later versions. So it would be better to use failover cluster in Server 2012 R2 or 2016 for a more reliable infrastructure configuration. </p><p>​​Use NLB to allow load balancing and failover. On each of your Windows Servers, you will host your website.</p>
<p>You need to follow these steps to get it up and running:</p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>On all nodes of the NBL cluster, the Network Load Balancing Feature needs to be installed.<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB1.png" style="width:600px;height:428px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Install the NLB Feature</span> </li>
<li>Open the Network Load Balancing Manager from Administrative Tools<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB22.png" style="width:600px;height:424px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Under the Cluster menu item, click New</span> </li>
<li>Enter the first node in the cluster in ‘Host’ and press ‘Connect’<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB33.png" style="width:400px;height:383px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Select the interface for the node</span> </li>
<li>Enter a Priority as 1 (this is just a host identifier)<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB44.png" style="width:400px;height:380px;" /> <span class="ms-rteCustom-FigureNormal">Figure: In 'Priority' enter '1'</span> </li>
<li><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB55.png" style="width:400px;height:386px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Enter a virtual IP address for the cluster. eg. 192.168.1.12</span> </li>
<li>Choose the IP address of your cluster from the dropdown list Set a Full Internet Name eg. spcluster.sydney.ssw.com.au. <br>Ensure the Multicast Cluster operation mode is selected.<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB66.png" style="width:400px;height:382px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Set the 3 cluster parameters</span> </li>
<li>You want sticky sessions so you don’t mistakenly bounce between servers (and lose your state)<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB77.png" style="width:400px;height:382px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Leave the Port Rule as default. This will provide sticky session</span><br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB88.png" style="width:700px;height:123px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Success. The cluster configuration will show a green icon</span> </li>
<li>Right click the name of the cluster eg. spcluster.sydney.ssw.com.au Click Add Host To Cluster<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="NLB99.png" style="width:700px;height:208px;" /> <span class="ms-rteCustom-FigureNormal">Figure: Add the 2nd web server with a priority of 2</span></li><li>Open a command prompt and type in wlbs query to verify the cluster:<br><img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="Setup-NLB-13.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure: Type in wlbs query to verify the cluster</span> </li>
<li>Ping both nodes and the virtual IP address externally to verify they are all working</li></ol>


