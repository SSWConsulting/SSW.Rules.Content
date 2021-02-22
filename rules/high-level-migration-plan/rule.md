---
type: rule
archivedreason: 
title: Do you have a migration plan
guid: 2f943ab1-a970-4c64-9f45-396f4d2d194a
uri: high-level-migration-plan
created: 2016-05-20T02:01:48.0000000Z
authors:
- title: Mark Liu
  url: https://ssw.com.au/people/mark-liu
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-have-a-migration-plan

---

At a high level, the plan is:
<!--endintro-->





* **Install**  **SharePoint **


1. Install with topology of your choice in SharePoint 2016 (or use [AutoSPInstaller](https&#58;//autospinstaller.codeplex.com/))
2. Configure Application services







> * Run the wizard (or use script. the community script wasn't ready when Thiago and I was migrating intranet)
> * Configure user profile and its permission configuration (see [msdn](https&#58;//technet.microsoft.com/en-us/library/ee721052.aspx))




* **Test Migration**



1. [Install required WSP packages in 2016](/do-you-know-how-to-identify-customizations-on-sharepoint-webs)
2. [Test migrating content database from old to new](/run-test-spcontentdatabase-before-actual-migration)
3. Fix all the missing customizations error in the above step, then do the [content database migration](https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx)
4. (Optional) [Migrate services database](/have-you-migrated-your-service-application-databases) (depends on which service applications do you use)


* **Post migration setup**


1. Configure search
    * [Do you use default zone URL in search content source](/use-default-zone-url-in-search-content-source)
    * [Do you add https by extending web application](/extend-web-application-for-https)
    * [Do you fix search with Office App for content preview ? (on premise only)](/fix-search-with-office-app-preview)
2. Configure metadata (optional)


* **Test test**                **tes**  **t**
* **Go-live migration**


1. [Put old SharePoint into read-only](/do-you-lock-the-sharepoint-content-database-before-making-a-backup)
2. [Refresh content & service database from SP 2013 to 2016](https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx)
3. Update DNS
4. Decommission old SharePoint server and database (after 2 weeks when you're confident with the new environment)
