---
type: rule
archivedreason: 3rd-party "how to" | Follow https://wpengine.com/support/copy-site/ for details
title: Do you know how to deploy changes from Staging to Live?
guid: 7b2715f6-90fa-4865-bb79-76e0524c3f46
uri: do-you-know-how-to-deploy-changes-from-staging-to-live
created: 2016-01-19T06:12:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

By default, only your files will be copied back to LIVE. You can move content by checking the tables you would like to move below. Keep in mind these tables will replace the LIVE version with the STAGING version. So for instance, if you choose to move wp\_posts all posts added to the LIVE site since the staging site was created will be removed. However, a  **checkpoint of your site will be created so you can 'undo' the changes if necessary** .

<!--endintro-->

After logging into your live site's /wp-admin click the WP Engine button on the top left-hand side. Then, click the "Staging" tab.

![Figure: Staging tab in WordPress](staging-tab.jpg)  

Then, choose from the following options:

![](wp-tables.png)  
 
When pushing changes from staging to live the file system from staging does not overwrite the live file system but instead, merges with the live file system.

This means any updated files in staging will be updated on live after a push, but any deleted files in staging would not be deleted in live.

**If you want to push all changes, except for pages, posts and users to your live site,** select all database tables **except:**

* wp\_posts,
* wp\_postmeta,
* wp\_users and wp\_usermeta.

**If you push no database tables,** only changes to theme files, core WordPress files and plugin files will be pushed to the live site.

**If you select all tables, any new posts, pages or users changes made to the live site during your work in the staging area will be overwritten.**


