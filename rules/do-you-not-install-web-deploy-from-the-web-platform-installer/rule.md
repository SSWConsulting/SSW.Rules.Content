---
type: rule
archivedreason: 
title: Do you not install Web Deploy from the Web Platform Installer?
guid: 44ecb0e3-2e08-4fee-9eec-84e3cb192a84
uri: do-you-not-install-web-deploy-from-the-web-platform-installer
created: 2013-02-06T18:38:16.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

You should not Install Web Deploy from the Web Platform Installer, but instead download the installation from the IIS web site (http://www.iis.net/downloads/microsoft/web-deploy).

The reason for this is that the Web Platform Installer does not install all of the components required for continuous deployment, but the downloaded package does.

<!--endintro-->

More information on this issue here: [Don't Install Web Deployment Tool using the Web Platform Installer](http://nicksnettravels.builttoroam.com/post/2010/04/22/Done28099t-Install-Web-Deployment-Tool-using-the-Web-Platform-Installer.aspx)
<dl class="badImage">&lt;dt&gt;
      <img src="web-platform-installer.jpg" alt="">
   &lt;/dt&gt;<dd>Figure: Bad Example - Installing Web Deploy from the Web Platform Installer does not install all the components required for continuous deployment</dd></dl><dl class="goodImage">&lt;dt&gt;
      <img src="web-deploy-installer.jpg" alt="">
   &lt;/dt&gt;<dd>Figure: Good Example - Install Web Deploy 3.0 by downloading the package from 
      <a target="_blank" href="http://www.iis.net/downloads/microsoft/web-deploy">http://www.iis.net/downloads/microsoft/web-deploy</a></dd></dl>
