---
type: rule
archivedreason: 
title: Do you run two or more test migrations before a live migration
guid: 78945e5a-256e-4316-b035-1aa26585359b
uri: do-you-run-two-or-more-test-migrations-before-a-live-migration
created: 2013-11-11T07:47:10.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir
related: []

---

It is recommended that you should run at least 2 or more successful test migrations before running a live migration. The following steps describe the process of setting up a test environment for migration:

<!--endintro-->

Back up your CRM 3 existing environment including customizations, custom codes, sitemap...

1. Configure a new environment with SQL Server and all necessary components (Do not install CRM yet!)
2. Restore database that you have backup from existing environment to the new environment
3. Redeploy CRM to the new environment
4. Test to see if the new environment works as expected
5. Upgrade the new environment to CRM 4
6. Test the new environment after upgrading
