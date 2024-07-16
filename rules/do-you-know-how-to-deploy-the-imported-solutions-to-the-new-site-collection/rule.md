---
seoDescription: Deploy SharePoint solutions to new site collections before resorting the content database to ensure a seamless transition between servers.
type: rule
archivedreason:
title: Do you know how to deploy the imported solutions to the new site collection
guid: 48ce8526-073d-45e6-be48-42c36e3254e6
uri: do-you-know-how-to-deploy-the-imported-solutions-to-the-new-site-collection
created: 2010-12-23T06:36:51.0000000Z
authors:
  - title: William Yin
    url: https://ssw.com.au/people/william-yin
related: []
redirects: []
---

Solutions must be deployed to the new site collection **before** the content database is resorted to the SharePoint 2010/2013/2016 server:

1. Open **SharePoint Central Administration** | **System Settings** | **Manage Farm Solutions**
2. Click on **Deploy Solution**
3. Refer to the table you completed in the rule [Do you confirm your list of installed Solutions](/do-you-confirm-your-list-of-installed-sharepoint-2007-solutions) and deploy the solutions to the same site collections they were deployed to on the SharePoint 2007/2010/2013 server.

<!--endintro-->
