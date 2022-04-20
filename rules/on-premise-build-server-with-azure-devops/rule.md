---
type: rule
archivedreason: 
title: Do you know when to use an on-premises build server with Azure DevOps?
guid: 3ef53ffe-23ec-452a-83ac-c57b307febb7
uri: on-premise-build-server-with-azure-devops
created: 2014-08-25T05:28:30.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related:
- do-you-use-the-best-deployment-tool
- do-you-estimate-all-tasks-at-the-start-of-the-sprint
redirects:
- do-you-know-when-to-use-an-on-premises-build-server-with-visual-studio-online

---

If you are using [Azure DevOps](https://dev.azure.com/), there's an awesome [Hosted Build Server](https://devblogs.microsoft.com/bharry/configuring-a-build-server-against-your-shiny-new-hosted-tfs-account/) option you can use to perform your builds with little to no setup. But if you're working on a project that has continuous integration and a long build time, it's not long before those build minutes start to add up.

<!--endintro-->

To reduce your build costs, you could reduce the number of builds or try to reduce the build time. Continuous integration is very important so you don't want to turn that off, and [we encourage checking in early and often](/do-you-know-to-get-visual-studio-to-remind-you-to-check-in). Reducing the build time is a nice idea, but you can't always reduce it enough to make a difference.

For large, expensive projects, the best option is to configure an on-premises build server rather than using hosted builds.

To configure an on-premises build server for Azure DevOps, check out [Anthony Borton's great walkthrough](https://anthonyborton.com/2014/04/configuring-on-premises-build-server-for-visual-studio-online/).

Once you have a build server configured, you'll be able to see the build controller as an option when you configure a new build definition.

::: good  
![Figure: Good Example - We have the option of an on-premises build controller as well as the Hosted Build controller](vso\_build.png)  
:::
