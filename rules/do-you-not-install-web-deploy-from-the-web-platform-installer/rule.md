---
type: rule
archivedreason: 
title: Do you not install Web Deploy from the Web Platform Installer?
guid: 44ecb0e3-2e08-4fee-9eec-84e3cb192a84
uri: do-you-not-install-web-deploy-from-the-web-platform-installer
created: 2013-02-06T18:38:16.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

You should not Install Web Deploy from the Web Platform Installer, but instead download the installation from the IIS website (http://www.iis.net/downloads/microsoft/web-deploy).

The reason for this is that the Web Platform Installer does not install all of the components required for continuous deployment, but the downloaded package does.

<!--endintro-->

More information on this issue here: [Don't Install Web Deployment Tool using the Web Platform Installer](http://nicksnettravels.builttoroam.com/post/2010/04/22/Done28099t-Install-Web-Deployment-Tool-using-the-Web-Platform-Installer.aspx)


::: bad  
![Figure: Bad Example - Installing Web Deploy from the Web Platform Installer does not install all the components required for continuous deployment](web-platform-installer.jpg)  
:::


::: good  
![Figure: Good Example - Install Web Deploy 3.0 by downloading the package from        http://www.iis.net/downloads/microsoft/web-deploy](web-deploy-installer.jpg)  
:::
