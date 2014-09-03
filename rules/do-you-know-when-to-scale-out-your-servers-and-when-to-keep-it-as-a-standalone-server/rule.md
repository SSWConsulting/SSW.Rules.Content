---
type: rule
archivedreason: 
title: Do you know when to scale out your servers and when to keep it as a standalone server?
guid: 0437a5be-2ea8-4d12-843f-b634706aee55
uri: do-you-know-when-to-scale-out-your-servers-and-when-to-keep-it-as-a-standalone-server
created: 2014-09-03T19:33:29.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p> You should use&#160;virtualized standalone servers because&#58; </p><ul><li>If one server goes down it does not affect other servers (e.g. a centralized SQL server fails and brings down&#58; CRM, TFS, Reports, Web Server)</li><li>You can just copy the VPC to another computer and it just works, no need to worry about reconfiguring the SQL connection string or web services</li><li>You can just backup the VPC</li></ul><p>

                    However, you should scale out your servers if&#58;

                </p><ul><li>You want the best performance (e.g. A different server for SQL backend and Web frontend)</li></ul>​​
<br><excerpt class='endintro'></excerpt><br>



