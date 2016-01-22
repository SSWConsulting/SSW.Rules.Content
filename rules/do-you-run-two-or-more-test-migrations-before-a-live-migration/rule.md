---
type: rule
title: Do you run two or more test migrations before a live migration
uri: do-you-run-two-or-more-test-migrations-before-a-live-migration
created: 2013-11-11T07:47:10.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.6;">It is recommended that you should run at least 2 or more successful test migrations before running a live migration. The following steps describe the process of setting up a test environment for migration&#58;</span><br> </span>

<p>​Back up your CRM 3 existing environment including customizations, custom codes, sitemap...</p><ol><li>Configure a new environment with SQL Server and all necessary components (Do not install CRM yet!)</li><li>Restore database that you have backup from existing environment​ to the new environment</li><li>Redeploy CRM to the new environment</li><li>Test to see if the new environment works as expected</li><li>Upgrade the new environment to CRM 4</li>
   <li>​Test the new environment after upgrading​</li></ol>


