---
type: rule
archivedreason: 
title: Do you know how to manage certificates?
guid: 00ddce19-4692-4819-b535-ef4a90c640e5
uri: do-you-know-how-to-manage-certificates
created: 2020-09-09T21:26:04.0000000Z
authors:
- id: 71
  title: Steven Andrews
related: []

---

At SSW we have moved away from paid certificates for our websites and web apps. We now use [Let's Encrypt](https://letsencrypt.org/) managed by [Certify The Web](https://certifytheweb.com/).  
 
Previously the way we managed our certificates was using a SharePoint list as well as calendar reminders to inform us when they were going to expire. The issue with using this system is the SharePoint list as well as ensuring the certificates remained up to date was a manual process. This left a lot of room for human error especially when managing hundreds of certificates. There are of course commercial solutions to manage certificates but these haven't been econmical for our environment.   


With Certify the Web and Let's Encrypt, we remove this human error and manual handling, ensuring that our certificates never expire. 
 
You should use [Certify the Web](https://certifytheweb.com/). 

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="manage-certificates-bad.png" alt="manage-certificates-bad.png" style="width:750px;height:386px;">&lt;/dt&gt;<dd>Figure: Bad example - Keeping a database is unnecessary</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="manage-certificates-good.png" alt="manage-certificates-good.png" style="width:750px;height:335px;">&lt;/dt&gt;<dd>Figure: Good example - Using Certify The Web<br></dd></dl>
