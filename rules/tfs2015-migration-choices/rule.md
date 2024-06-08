---
type: rule
archivedreason: 
title: Do you know your TFS 2015 migration choices?
guid: acd96e8e-9cac-47ce-bdf8-865d5c383e7e
uri: tfs2015-migration-choices
created: 2015-08-12T15:26:07.0000000Z
authors: []
related: []
redirects:
- do-you-know-your-migration-choices1

---

There are two main ways to move from TFS 2013 Update 4 to TFS 2015:

<!--endintro-->

**Option 1:** **In-place migration (Recommended)**

With an in-place migration, you essentially install TFS 2015 over the top of an existing TFS 2013 Update 4 installation. The benefits of this approach are that you don't need additional hardware, and don't need to change network settings like DNS addresses to change between environments.

**Option 2: Migration to a new environment**

Migrating to a new environment may be required if you need to move to new upgraded hardware, or if you are not confident with your rollback plan. The key benefit with migrating to a new environment is that you can quickly switch back to your original environment should anything go wrong during the upgrade.

**Reducing downtime**

With both options, you can also use the [TfsPreUpgrade tool to reduce downtime](https://msdn.microsoft.com/en-us/Library/vs/alm/TFS/upgrade/pre-upgrade). As per the article, the TfsPreUpgrade tool will:

* Enable compression for a small number of tables that were not compressed in 2013 but will be in 2015.
* Scan for and fix a very rare but well understood data corruption in TFS version control data.
* Create new tables and migrate existing data to them.
* Create triggers.
* Update stored procedures.
* Create indexes.

By using the TfsPreUpgrade tool, you can thereby reduce the downtime for the actual cut-over to the new version by ensuring that your databases are updated in advance.
