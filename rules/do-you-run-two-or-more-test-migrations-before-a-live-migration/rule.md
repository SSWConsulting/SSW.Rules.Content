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


<span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.6;">It is recommended that you should run at least 2 or more successful test migrations before running a live migration. The following steps describe the process of setting up a test environment for migration&#58;</span><br>
<br><excerpt class='endintro'></excerpt><br>
<p>​<span style="font-size&#58;1em;line-height&#58;21px;font-family&#58;verdana, sans-serif;">Back up your CRM 3 existing environment including customizations, custom codes, sitemap...</span></p><ol style="padding-left&#58;0px;margin-left&#58;10px;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;17px;color&#58;#000000;"><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Configure a new environment with SQL Server and all necessary components (Do not install CRM yet!)</li><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Restore database that you have backup from existing environment​ to the new environment</li><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Redeploy CRM to the new environment</li><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Test to see if the new environment works as expected</li><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Upgrade the new environment to CRM 4</li><li style="padding-bottom&#58;0px;padding-left&#58;15px;margin-left&#58;10px;font-size&#58;1em;line-height&#58;21px;">Test the new environment after upgrading​</li></ol>


