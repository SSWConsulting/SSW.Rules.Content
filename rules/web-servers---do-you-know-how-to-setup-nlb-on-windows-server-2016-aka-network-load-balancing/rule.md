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


<p>ThiDowntime occurs when you have a single server setup.</p>
<p>Use NLB to allow load balancing and failover. On each of your Windows Servers you will host your website. </p>
<p>You need to follow these steps to get it up and running&#58;</p>

<br><excerpt class='endintro'></excerpt><br>
<ol>
<li>On all nodes of the NBL cluster, the Network Load Balancing Feature needs to be installed.<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-1.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Install the NLB Feature</span>
</li>
<li>Open the Network Load Balancing Manager from Administrative Tools<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-2.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Under the Cluster menu item, click New</span>
</li>
<li>Enter the first node in the cluster in ‘Host’ and press ‘Connect’<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-3.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Select the interface for the node</span>
</li>
<li>Enter a Priority as 1 (this is just a host identifier)<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-4.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; In 'Priority' enter '1'</span>
</li>
<li>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-5.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Enter a virtual IP address for the cluster.  eg. 192.168.1.12</span>

</li>
<li>Choose the IP address of your cluster from the dropdown list 
Set a Full Internet Name eg.  spcluster.sydney.ssw.com.au. <br>
Ensure the Multicast Cluster operation mode is selected.<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-6.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Set the 3 cluster parameters</span>

</li>
<li>You want sticky sessions so you don’t mistakenly bounce between servers (and lose your state)<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-7.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Leave the Port Rule as default. This will provide sticky sessions</span><br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-8.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Success. The cluster configuration will show a green icon</span>
</li>
<li>Right click the name of the cluster eg. spcluster.sydney.ssw.com.au
Click Add Host To Cluster<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-9.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Add the 2nd web server</span>
</li>
<li>Enter the host name of the next node eg. SYDVMAPS2010P02<br>
Click connect<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-10.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Enter the 2nd web servers name</span>

</li>
<li>Take the default settings, assuring the ‘Priority (unique host identifier)’ is different than the first node&#58;<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-11.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Set the priority as #2</span>

</li>
<li>Take defaults on Port Rules page and click Finish</li>

<li>Success. The status of the cluster will now be Converged<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-12.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Success with 2 green icons</span>

</li>
<li>Open a command prompt and type in wlbs query to verify the cluster&#58;<br>
<img class="ms-rteCustom-ImageArea" alt="Setup NLB" src="/ITAndNetworking/RulesToBetterWindowsServers/PublishingImages/Setup-NLB-13.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Type in wlbs query to verify the cluster</span> 
</li>
<li>Ping both nodes and the virtual IP address externally to verify they are all working</li>
</ol>



