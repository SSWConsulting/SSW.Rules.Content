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

If you are dealing with a single server, there is no way to achieve 100% uptime, when updating or restarting a server.

So set your website up correctly with at least 2 front ends, and 1 backend (the SQL Server).

<!--endintro-->

[[goodExample]]
| ![When one server goes down, the web site remains up](Server-down-Site-up.jpg)
Then, use a Network Load Balancer (we recommend Microsoft’s build in NLB) which allows you to spread web site load to multiple servers, but even more helpful when you need to do Windows Updates or make changes to web servers in your environment.

Follow the below steps on your test server first, get the application tested passed, then move on to production.

1. Open the  **Network Load Balancing Manager**
2. Right click on the machine you want to update | Select  **Control Host** | Click  **Drain Stop** 
![The 2 green icons indicate both servers are live with users - Do a drain stop on the server you want to make changes too](Server-drainstop.jpg)
3. To view the current connections on the server, open a command prompt and enter netstat -an. You will be able to see the connections list dropping as users are sent to the other server 
![Run "netstat -an" to view the current connections on the server](Server-netstat.jpg)
4. Allow the NLB to finish sending the connections to the remaining servers. The server you have drain stopped, will turn red when all the users have been moved to the other server

![When the server turns red, the connections have been dropped and you're ready to update](Server-red.jpg)
5. Optional – if you are using Hyper-V, take a snapshot of the server you are about to make changes on
6. Restart

![Now that the server isn't being hit with users, perform your updates. Click "Restart Now"7. Optional – Do a smoke test](Server-restart.jpg)(open the site and check its working)
8. Optional – Run any automated tests (for example Telerik Tests)
9. When the server ready, add it back into the load balancer. Right click on the machine | Select  **Control Host** | Click  **Start**
10. The server icon will return to green, and users will start being sent to the server again

![The server will now accept connections again11. Follow the same process for the other server](Server-green.jpg)(or multiple)


Congratulations you've just updated your servers with 100% uptime.
