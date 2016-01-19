---
type: rule
title: Do you know how to deploy changes from Staging to Live?
uri: do-you-know-how-to-deploy-changes-from-staging-to-live
created: 2016-01-19T06:12:14.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <h3 class="ssw15-rteElement-H3">Pushing Staging to Live</h3><p>&#160;</p><p>By default only your files will be copied back to LIVE. You can move content by checking the tables you would like to move below. Keep in mind these tables will replace the LIVE version with the STAGING version. So for instance, if you choose to move wp_posts all posts added to the LIVE site since the staging site was created will be removed. However, a <strong>checkpoint of your site will be created so you can 'undo' the changes if necessary</strong>.</p><p>&#160;</p><p>After logging into your live site's /wp-admin click the WP Engine button on the top left hand side. Then, click the &quot;Staging&quot; tab.</p><dl class="ssw15-rteElement-ImageArea">&#160; <img src="/PublishingImages/staging-tab.jpg" alt="staging-tab.jpg" style="margin&#58;5px;" /></dl><p><span style="color&#58;#555555;font-size&#58;11px;font-weight&#58;bold;line-height&#58;1.6;"> Figure&#58; Staging tab in WordPress</span></p><p><br>Then, chose from the following options&#58;</p><dl class="ssw15-rteElement-ImageArea"><img src="/PublishingImages/wp-tables.png" alt="wp-tables.png" style="margin&#58;5px;" /></dl><img src="file&#58;///D&#58;/Users/davidberkes.SSW2000/AppData/Local/Temp/msohtmlclip1/01/clip_image003.jpg" alt="" style="width&#58;555px;margin&#58;5px;" /> <p><span style="line-height&#58;1.6;">When pushing changes from staging to live the file system from staging does not overwrite the live file system but instead merges with the live file system.&#160;</span></p><p>This means any updated files in staging will be updated on live after a push, but any deleted files in staging would not be deleted in live.</p><p>&#160;<strong style="line-height&#58;1.6;">If you want to push all changes, except for pages, posts and users to your live site&#58;</strong></p><p>select all database tables&#160;<strong>except&#58;</strong></p><p>wp_posts,</p><p>wp_postmeta,</p><p>wp_users and wp_usermeta.</p><p>&#160;<strong style="line-height&#58;1.6;">If you push no database tables</strong><span style="line-height&#58;1.6;">, only changes to theme files, core WordPress files and plugin files will be pushed to the live site.</span></p><p>&#160;<strong style="line-height&#58;1.6;">If you select all tables, any new posts, pages or users changes made to the live site during your work in the staging area will be overwritten.</strong></p> </span>




