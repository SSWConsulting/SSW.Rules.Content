---
type: rule
archivedreason: 
title: Do you automate the generation of your API specification and required clients?
guid: 83b61858-d33b-40cb-ae0e-4bb8ba301e3b
uri: do-you-automate-the-generation-of-your-api-specification-and-required-clients
created: 2019-05-25T01:58:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- automate-the-generation-of-your-api-specification-and-required-clients

---

If your changes to your WebAPI break your client, then you want to know right away.

Using NSwag you should generate your API client eg. Angular Client.

* You run nswag.exe on the post-build event
* Nswag will generate the client code and update the API client file directly


<!--endintro-->


::: good  
![Figure: Good example – using NSwag config file helps with automation. Since the API client is generated automatically next time we build, any breaking changes will be obvious immediately](using-nswag-helps-automation.jpg)  
:::

Now this is automated this is no longer a concern we need to deal with.

**More info:** http://www.codingflow.net/building-single-page-applications-on-asp-net-core-2-1-with-angular-6-part-3-implementing-open-api/
