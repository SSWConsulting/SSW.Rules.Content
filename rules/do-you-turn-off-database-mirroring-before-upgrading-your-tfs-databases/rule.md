---
type: rule
archivedreason: 
title: Do you turn off Database Mirroring before Upgrading your TFS databases?
guid: 2af8f969-0ea6-4262-a1de-9eda9c93a45f
uri: do-you-turn-off-database-mirroring-before-upgrading-your-tfs-databases
created: 2013-05-23T21:20:16.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

To avoid headaches while upgrading the TFS database schemas, you should manually turn off database mirroring prior to running the Verify step of your configuration.

<!--endintro-->

If database mirroring is enabled on your TFS database, an additional step is required to temporarily turn it off when upgrading the database schema.  This may require additional permissions that are difficult to check in the Verify step.  Verification may hang with no sign of what’s happening until you delve into the SQL Server logs.  It’s safer (and avoids problems) if you manually turn it off before you start.
