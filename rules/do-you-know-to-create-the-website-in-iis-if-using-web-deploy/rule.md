---
type: rule
title: Do you know to Create the Website in IIS if using Web Deploy?
uri: do-you-know-to-create-the-website-in-iis-if-using-web-deploy
created: 2013-02-06T18:43:08.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>In theory WebDeploy can create a site for you when you deploy. The issue with this is that many settings are assumed.</p> </span>

<p>Always create the site before deploying to it, so that you can specify the exactly the settings that you desire. E.g. the directory where you want the files for the site to be saved, the app pool to use and the version of .Net.</p><dl class="image"><dt><img src="/TFS/Rules-to-Better-Continuous-Deployment/Pages/Create-the-Website-in-IIS.aspx?ControlMode=Edit&amp;DisplayMode=Design" alt="" /></dt><dd>Figure&#58; Create the website in IIS</dd></dl><br>


