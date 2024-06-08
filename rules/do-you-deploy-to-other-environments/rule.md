---
type: rule
archivedreason: Deprecated - Currently we deploy with PowerShell and Infrastructure-As-Code via platforms like GitHub and AzureDevOps.
title: Do you Deploy to other Environments?
guid: ed2c4951-62af-4e56-8e98-67c53a5fb67d
uri: do-you-deploy-to-other-environments
created: 2013-02-06T18:56:41.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

Once you have configured “Build Once, Deploy Many” you can open the folder for any build on the build server and deploy any build, to any environment.

<!--endintro-->

This means that if you deploy version 37, and then want to roll back to version 36 simply open the folder for 36 and re-run that batch file (assuming there has been no breaking DB schema changes).

::: todo
TODO: AdamS – Write a rule on non-breaking Schema changes
:::

![Figure: To deploy to staging and production, open the appropriate drops folder and execute the correct batch file from the drops folder](deploy-other-environments.jpg)
