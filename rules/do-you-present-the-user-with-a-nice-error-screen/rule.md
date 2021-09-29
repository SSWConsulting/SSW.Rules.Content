---
type: rule
archivedreason: 
title: Do you present the user with a nice error screen?
guid: 4ee8ca41-78bb-40c1-94cc-cf44a3b47622
uri: do-you-present-the-user-with-a-nice-error-screen
created: 2013-09-11T21:08:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects:
- do-you-present-the-user-with-a-nice-error-screen-(web-only)
- do-you-present-the-user-with-a-nice-error-screen-web-only

---

Your users should never see the “yellow screen of death” in ASP.NET. Errors should be caught, logged and a user-friendly screen displayed to the user.

<!--endintro-->

This last part is done by specifying the customErrors element in the web.config file.

This will activate ASP.NET’s built in error page (e.g. MVC’s HandleErrorAttribute filter) which can then be customized to suit your application.

::: bad
![Figure: Bad Example – Yellow Screen of Death](error-screen-bad.png)
:::

::: good  
![Figure: Good Example - GitHub custom error page](error-screen-good.png)
:::

However, as a developer you still want to be able to view the detail of the exception in your local development environment. Use the below setting in your Web Application's web.config file to view the yellow screen locally but present a nice error screen to the user.

::: good
![Figure: Good Example - Don't hide the yellow screen of death in the local environment](14-08-2014-2-47-50-PM-compressor.png)
:::
