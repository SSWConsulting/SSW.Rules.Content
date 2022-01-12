---
type: rule
title: Certificate - Do you know how to manage certificates?
uri: how-to-manage-certificates
authors:
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
related: []
redirects:
  - do-you-know-how-to-manage-certificates
created: 2020-09-09T21:26:04.000Z
archivedreason: null
guid: 00ddce19-4692-4819-b535-ef4a90c640e5
---

At SSW we have moved away from paid certificates for our websites and web apps. We now use [Let's Encrypt](https://letsencrypt.org/) managed by [Certify The Web](https://certifytheweb.com/).  
 
Previously the way we managed our certificates was using a SharePoint list as well as calendar reminders to inform us when they were going to expire. The issue with using this system is the SharePoint list as well as ensuring the certificates remained up to date was a manual process. This left a lot of room for human error especially when managing hundreds of certificates. There are of course commercial solutions to manage certificates but these haven't been econmical for our environment.   


With Certify the Web and Let's Encrypt, we remove this human error and manual handling, ensuring that our certificates never expire. 
 
You should use [Certify the Web](https://certifytheweb.com/). 

<!--endintro-->


::: bad  
![Figure: Bad example - Keeping a database is unnecessary](manage-certificates-bad.png)  
:::


::: good  
![Figure: Good example - Using Certify The Web](manage-certificates-good.png)  
:::
