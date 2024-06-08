---
type: rule
archivedreason: 
title: Do You Create Different App.Config for Different Environment?
guid: 8c6e4f21-3c36-42bf-9246-f9da9b8c3c03
uri: do-you-create-different-app-config-for-different-environment
created: 2009-12-10T05:23:58.0000000Z
authors:
- title: Andy Taslim
  url: https://ssw.com.au/people/andy-taslim
related: []
redirects: []

---

Every application has different settings depending on the environment it is running on, e.g. production, testing or development environment.
 It is much easier and efficient if app.config is provided in several environment types, so then the developer can just copy and paste the required app.config.

![](AppConfigBad.jpg)



::: bad
Figure: Bad Example - Only 1 App.config provided  
:::

![](App.config.jpg)



::: good
Figure : Good Example - Several App.config are provided  
:::

<!--endintro-->
