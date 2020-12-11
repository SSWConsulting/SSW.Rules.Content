---
type: rule
archivedreason: 
title: Search - Do you add https by extending web application
guid: aa23853e-3239-4739-bfb5-a01328416962
uri: search---do-you-add-https-by-extending-web-application
created: 2016-05-20T06:51:56.0000000Z
authors: []
related: []

---

It is recommended to bind https by extending web applications in central admin site, rather than configuring in IIS

<!--endintro-->
<dl class="ssw15-rteElement-ImageArea"><img src="configurationInIIS.jpg" alt="configurationInIIS.jpg" style="margin:5px;width:653px;"></dl>

::: bad
Bad example: Add https binding in IIS
:::

<dl class="ssw15-rteElement-ImageArea"><img src="extendwebapplication.jpg" alt="extendwebapplication.jpg" style="margin:5px;width:808px;"></dl>

::: good
Good example: Extend web application and assign https to the Internet zone
:::
