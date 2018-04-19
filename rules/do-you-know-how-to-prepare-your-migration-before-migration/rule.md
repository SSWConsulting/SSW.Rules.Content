---
type: rule
title: Do you know how to prepare your migration? (before migration)
uri: do-you-know-how-to-prepare-your-migration-before-migration
created: 2018-01-17T23:31:47.0000000Z
authors:
- id: 69
  title: Jean Thirion
- id: 9
  title: William Yin

---



<span class='intro'> ​<p>Before migrating your content over SharePoint Online, you want to get rid of unused or old content. Migration is the perfect time to audit your content and delete what you can. You may also use the migration to identify (and get rid of) Orphan Users, and Documents with Custom permissions (look for SharePoint best practices on permissions).<br></p> </span>

<p>Use the Sharegate migration tool to generate reports on your site collections and sites, so you can easily identify problems. Reporting tool comes with a lot of out of the box reports, and you can even create custom ones.<br></p><dl class="image"><dt><img src="/PublishingImages/sharegate-4-main-reports.png" alt="sharegate-4-main-reports.png" style="width&#58;750px;" />​​​<br></dt><dd>Figure&#58; Sharegate reporting menu have 4 main reports</dd></dl><p>Once identified, check with Site Owners to ensure the content can be deleted. Alternatively, if you don't want to delete content, you can ZZed it.​​<br></p><p>Ideally,&#160;before migration starts,&#160;you should put your source sites to read-only mode using&#160;&quot;site collection lock&quot;. But&#160;if you cannot put your source sites into read-only mode due to some reasons (e.g. migration tool needs to write auditing logs), then at least&#160;put a notification bar on the top of your site to prevent users editing it during the migration.<br></p><dl class="ssw15-rteElement-ImageArea"><img src="/SiteAssets/how-to-prepare-before-migration/migration_notification_bar.jpg" alt="migration_notification_bar.jpg" style="margin&#58;5px;width&#58;743px;" /></dl><p><br></p><p>Sharegate supports 'Pre-check' before kicking off the real migration, it can tell the potential errors. For example, you might have orphen users&#160;do not exist in Office 365, which you might have to temporarily enable to ensure the &quot;Created By&quot; and &quot;Modified By&quot; user info is correctly migrated for ASPX pages (ASPX pages&#160;do not support insant mode).<br></p>


