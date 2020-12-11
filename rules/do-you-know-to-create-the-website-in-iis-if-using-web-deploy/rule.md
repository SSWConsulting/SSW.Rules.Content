---
type: rule
archivedreason: 
title: Do you know to Create the Website in IIS if using Web Deploy?
guid: 9a47c774-bad4-46c4-960a-e5ac196b2ce8
uri: do-you-know-to-create-the-website-in-iis-if-using-web-deploy
created: 2013-02-06T18:43:08.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

In theory WebDeploy can create a site for you when you deploy. The issue with this is that many settings are assumed.

<!--endintro-->

Always create the site before deploying to it, so that you can specify the exactly the settings that you desire. E.g. the directory where you want the files for the site to be saved, the app pool to use and the version of .Net.

<dl class="image">&lt;dt&gt;<img src="create-iis.jpg" alt="">&lt;/dt&gt;
   <dd>Figure: Create the website in IIS</dd></dl>
