---
type: rule
archivedreason: 
title: Do you publish simple websites directly to Windows Azure from Visual Studio Online?
guid: b020ff72-3b77-405b-9e8c-0fb11a96abe7
uri: do-you-publish-simple-websites-directly-to-windows-azure-from-visual-studio-online
created: 2013-06-03T19:20:33.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

TFS and Windows Azure work wonderfully together. It only takes a minute to configure continuous deployment from Visual Studio Online (visualstudio.com) to a Windows Azure website or Cloud Service.

This is by far the most simple method to achieve continuous deployment of your websites to Azure.
But, if your application is more complicated, or you need to run UI tests as part of your deployment, you should be using Octopus Deploy instead according to the [Do you use the best deployment tool](/do-you-use-the-best-deployment-tool) rule.
<!--endintro-->

![Figure: Setting up deployment from source control is simple from within the Azure portal](integrate-source-control.jpg)  

![Figure: Deployment is available from a number of different source control repositories](TFS\_Deployment.png)  

Suggestion to Microsoft: We hope this functionality comes to on-premise TFS and IIS configurations in the next version.
