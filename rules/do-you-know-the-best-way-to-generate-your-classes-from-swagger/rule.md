---
type: rule
archivedreason: 
title: Do you know the best way to generate your classes from swagger?
guid: 1914ad2e-4d23-4963-9bc4-ba8d8af66070
uri: do-you-know-the-best-way-to-generate-your-classes-from-swagger
created: 2017-03-10T20:30:41.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
- id: 9
  title: William Yin
related: []

---

You can save time and reduce human error by automatically generating clients for your APIs.

<!--endintro-->

The best tool for this is [NSwag](https://github.com/RicoSuter/NSwag).

This is Microsoft's recommended approach, and you can read more about how to set this up in your ASP.Net Core project at [the official documentation](https://docs.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-nswag?view=aspnetcore-3.1&tabs=visual-studio).

If you use the Clean Architecture template developed by SSW's @JasonTaylorDev, this is built in out of the box. See our [rule on getting started with clean architecture](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=ae1a999d-0c34-45d7-af89-7d50a9939370).
<dl class="goodImage">&lt;dt&gt;<img src="nswag-studio.png" alt="nswag-studio.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Good Example - NSwag Studio lets you customise your nswag config</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="jt-nswag.png" alt="jt-nswag.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Good Example - @JasonTaylorDev's Clean Architecture templace comes with this built in<br></dd></dl>
