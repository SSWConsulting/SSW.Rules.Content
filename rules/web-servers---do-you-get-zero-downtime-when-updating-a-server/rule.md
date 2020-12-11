---
type: rule
archivedreason: 
title: Web Servers - Do you get Zero Downtime when Updating a Server?
guid: ce678b92-1047-4465-b6a2-4f016c1bcd35
uri: web-servers---do-you-get-zero-downtime-when-updating-a-server
created: 2012-03-02T15:46:51.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>If you are dealing with a single server, there is no way to achieve 100% uptime, when updating or restarting a server.<br></p>
<p>So set your website up correctly with at least 2 front ends, and 1 backend (the SQL Server).</p>

<br><excerpt class='endintro'></excerpt><br>
<img src="Server-down-Site-up.jpg" alt="Server down, site up" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureGood">Figure: Good Example – When one server goes down, the web site remains up</span>
<p>Then, use a Network Load Balancer (we recommend Microsoft’s build in NLB) which allows you to spread web site load to multiple servers, but even more helpful when you need to do Windows Updates or make changes to web servers in your environment.</p>
 
<p>Follow the below steps on your test server first, get the application tested passed, then move on to production.</p>
<ol>
<li>Open the <strong>Network Load Balancing Manager</strong></li>
<li>Right click on the machine you want to update | Select <strong>Control Host</strong> | Click <strong>Drain Stop</strong> <img src="Server-drainstop.jpg" alt="drain stop" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure: The 2 green icons indicate both servers are live with users - Do a drain stop on the server you want to make changes too </span>
</li>
<li>To view the current connections on the server, open a command prompt and enter netstat -an. You will be able to see the connections list dropping as users are sent to the other server <img src="Server-netstat.jpg" alt="netstat" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure: Run "netstat -an" to view the current connections on the server</span></li>
<li>Allow the NLB to finish sending the connections to the remaining servers. The server you have drain stopped, will turn red when all the users have been moved to the other server​<br>
<img src="Server-red.jpg" alt="Server turns red" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure: When the server turns red, the connections have been dropped and you're ready to update</span>
</li>
<li>Optional – if you are using Hyper-V, take a snapshot of the server you are about to make changes on</li>
<li>Restart</li>
<img src="Server-restart.jpg" alt="Windows update" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure: Now that the server isn't being hit with users, perform your updates. Click "Restart Now"</span>
<li>Optional – Do a smoke test (open the site and check its working)</li>
<li>Optional – Run any automated tests (for example Telerik Tests)</li>
<li>When the server ready, add it back into the load balancer. Right click on the machine | Select <strong>Control Host</strong> | Click <strong>Start</strong></li>
<li>The server icon will return to green, and users will start being sent to the server again</li>
<img src="Server-green.jpg" alt="Server OK" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure: The server will now accept connections again</span>
<li>Follow the same process for the other server (or multiple)</li>
</ol>
<p>Congratulations you've just updated your servers with 100% uptime.</p>




