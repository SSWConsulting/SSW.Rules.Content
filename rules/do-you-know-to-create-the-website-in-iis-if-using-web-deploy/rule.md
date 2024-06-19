---
seoDescription: Create a website in IIS before deploying with WebDeploy to specify settings like directory, app pool, and .Net version.
type: rule
archivedreason:
title: Do you know to Create the Website in IIS if using Web Deploy?
guid: 9a47c774-bad4-46c4-960a-e5ac196b2ce8
uri: do-you-know-to-create-the-website-in-iis-if-using-web-deploy
created: 2013-02-06T18:43:08.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
---

In theory WebDeploy can create a site for you when you deploy. The issue with this is that many settings are assumed.

<!--endintro-->

Always create the site before deploying to it, so that you can specify the exactly the settings that you desire. E.g. the directory where you want the files for the site to be saved, the app pool to use and the version of .Net.

![Figure: Create the website in IIS](create-iis.jpg)
