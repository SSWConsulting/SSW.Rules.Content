---
type: rule
archivedreason: 
title: Do you know why you need to use solution package instead of deployment manually?
guid: a7cc7bb5-c13f-4c56-86ae-312bb8c51d98
uri: do-you-know-why-you-need-to-use-solution-package-instead-of-deployment-manually
created: 2009-04-09T02:44:19.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

As a server product, SharePoint supports lots of configuration, but the support for packaging and deploying changes between servers remains very week.

The experts agree that the best and preferred way to package a set of changes is to build a solution package.  A SharePoint solution package includes all the components and dependent files packed in a cab file.

There are many reasons why you need to use solution package:

<!--endintro-->

1. All dependent files and components are in the package - allowing developers to quickly deploy development, testing, staging and production servers.
2. Manual steps are very long, and error prone
3. Solution packages are easy to retract
4. Minimize downtime in the SharePoint production server during an upgrade operation
5. No content data loss during upgrades - SharePoint backup/restore deployment methods will block users from making changes to the production the site during the upgrade period
