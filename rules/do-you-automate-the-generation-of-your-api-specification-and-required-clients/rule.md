---
type: rule
title: Do you automate the generation of your API specification and required clients?
uri: do-you-automate-the-generation-of-your-api-specification-and-required-clients
created: 2019-05-25T01:58:58.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>If your changes to your WebAPI break your client, then you want to know right away.<br></p><p>Using NSwag you should generate your API client eg. Angular Client.<br></p><ul><li>You run nswag.exe on the post-build event<br></li><li>Nswag will generate the client code and update the API client file directly<br></li></ul> </span>

<dl class="goodImage"><dt>​<img src="/PublishingImages/using-nswag-helps-automation.jpg" alt="using-nswag-helps-automation.jpg" /></dt><dd>Figure&#58; Good example – using NSwag config file helps with automation. Since the API client is generated automatically next time we build, any breaking changes will be obvious immediately<br></dd></dl><p>Now this is automated this is no longer a concern we need to deal with.<br></p><p><b>More info&#58;</b> 
      <a href="http&#58;//www.codingflow.net/building-single-page-applications-on-asp-net-core-2-1-with-angular-6-part-3-implementing-open-api/">http&#58;//www.codingflow.net/building-single-page-applications-on-asp-net-core-2-1-with-angular-6-part-3-implementing-open-api/</a>​</p>


