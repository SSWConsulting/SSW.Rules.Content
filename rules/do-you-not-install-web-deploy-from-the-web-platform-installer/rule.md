---
type: rule
title: Do you not install Web Deploy from the Web Platform Installer?
uri: do-you-not-install-web-deploy-from-the-web-platform-installer
created: 2013-02-06T18:38:16.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>​​​You should not Install Web Deploy from the Web Platform Installer, but instead download the installation from the IIS web site (<a href="http&#58;//www.iis.net/downloads/microsoft/web-deploy" target="_blank">http&#58;//www.iis.net/downloads/microsoft/web-deploy</a>).</p>
<p>The reason for this is that the Web Platform Installer does not install all of the components required for continuous deployment, but the downloaded package does.
</p> </span>

<p>More information on this issue here&#58; <a href="http&#58;//nicksnettravels.builttoroam.com/post/2010/04/22/Done28099t-Install-Web-Deployment-Tool-using-the-Web-Platform-Installer.aspx">Don't Install Web Deployment Tool using the Web Platform Installer</a></p><dl class="badImage"><dt>
      <img src="web-platform-installer.jpg" alt="" />
   </dt><dd>Figure&#58; Bad Example - Installing Web Deploy from the Web Platform Installer does not install all the components required for continuous deployment​</dd></dl><dl class="goodImage"><dt>
      <img src="web-deploy-installer.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example - Install Web Deploy 3.0 by downloading the package from 
      <a target="_blank" href="http&#58;//www.iis.net/downloads/microsoft/web-deploy">http&#58;//www.iis.net/downloads/microsoft/web-deploy</a></dd></dl>


