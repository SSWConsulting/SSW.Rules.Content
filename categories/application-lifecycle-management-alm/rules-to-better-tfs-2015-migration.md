---
type: category
title: Rules to Better TFS 2015 Migration
guid: e4ee5fc0-9c66-408a-a224-e03e34654812
uid: rules-to-better-tfs-2015-migration
index:
- do-you-backup-your-databases
- do-you-disable-connections
- do-you-do-a-quick-test-after-the-upgrade-finishes
- do-you-get-a-developer-to-test-the-migration
- do-you-have-a-rollback-plan
- do-you-know-how-to-upgrade-your-tfs2013-update-4-system-the-big-one
- do-you-know-to-upgrade-your-third-party-tools
- do-you-know-your-migration-choices
- do-you-plan-your-additional-steps
- do-you-run-dog-food-stats-after
- do-you-run-your-dog-food-stats-before
- do-you-turn-off-database-mirroring-before-upgrading-your-tfs-databases
- do-you-verify-that-your-server-meets-the-minimum-requirements
- does-your-user-account-have-sql-server-system-administrator-privileges-in-sql-server

---
<p></p><p>Since 1990, SSW has supported the developer community by publishing all our best practices and rules for everyone to see.&#160;</p><p>If you still need help, visit&#160;<a href="http&#58;//www.ssw.com.au/ssw/Consulting/ALM.aspx">Application Lifecycle Management</a>&#160;<a href="http&#58;//www.ssw.com.au/ssw/Consulting/Default.aspx"> </a>and book in a consultant.<span style="line-height&#58;1.6;">​</span></p>
<p style="text-align&#58;justify;">​Migrating from TFS 2013 Update 4 to TFS 2015.</p><p>Upgrading Team Foundation Server can be a daunting task. Be assured that things have become easier and if you follow this guide, it will minimize your downtime.</p><p>In this page we will look at performing an in-place upgrade from TFS 2013 Update 4 to TFS 2015. In this walkthrough, we assume you are currently using a single server configuration, but might want to separate your SQL Server from your TFS server.&#160;We also assume you have a DNS entry setup for external access at tfs.northwind.com.</p>

