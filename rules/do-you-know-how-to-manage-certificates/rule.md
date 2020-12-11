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


At SSW we have moved away from paid certificates for our websites and web apps. We now use <a href="https://letsencrypt.org/">Let's Encrypt</a> managed by <a href="https://certifytheweb.com/">Certify The Web</a>.  <br> <br>Previously the way we managed our certificates was using a SharePoint list as well as calendar reminders to inform us when they were going to expire. The issue with using this system is the SharePoint list as well as ensuring the certificates remained up to date was a manual process. This left a lot of room for human error especially when managing hundreds of certificates. There are of course commercial solutions to manage certificates but these haven't been econmical for our environment.   <br><br><br>With Certify the Web and Let's Encrypt, we remove this human error and manual handling, ensuring that our certificates never expire. <br> <br>You should use <a href="https://certifytheweb.com/">Certify the Web​</a>. ​<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="manage-certificates-bad.png" alt="manage-certificates-bad.png" style="width:750px;height:386px;" /></dt><dd>Figure: Bad example - Keeping a database is unnecessary</dd></dl><dl class="goodImage"><dt><img src="manage-certificates-good.png" alt="manage-certificates-good.png" style="width:750px;height:335px;" /></dt><dd>Figure: Good example - Using Certify The Web​<br></dd></dl>


