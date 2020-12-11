---
type: rule
archivedreason: 
title: Do you have a migration plan
guid: 2f943ab1-a970-4c64-9f45-396f4d2d194a
uri: do-you-have-a-migration-plan
created: 2016-05-20T02:01:48.0000000Z
authors:
- id: 15
  title: Mark Liu
- id: 9
  title: William Yin
related: []

---

At a high level, the plan is:
<!--endintro-->





* **Install**  **SharePoint **


1. Install with topology of your choice in SharePoint 2016 (or use [AutoSPInstaller](https&#58;//autospinstaller.codeplex.com/))
2. Configure Application services







> * Run the wizard (or use script. the community script wasn't ready when Thiago and I was migrating intranet)
> * Configure user profile and its permission configuration (see [msdn](https&#58;//technet.microsoft.com/en-us/library/ee721052.aspx))




* **Test Migration**



1. [Install required WSP packages in 2016](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=50de290c-7bc6-4e9b-a784-e91367f2031d)
2. [Test migrating content database from old to new](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=352a79b1-165c-411f-b3cd-0328c8a7b618)
3. Fix all the missing customizations error in the above step, then do the [content database migration](https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx)
4. (Optional) [Migrate services database](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=65a88cf2-5b8e-4b13-a3e7-4e7c94ab7ea0) (depends on which service applications do you use)


* **Post migration setup**


1. Configure search
    * [Do you use default zone URL in search content source](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=dd856670-181b-45d0-8d7b-84bbfccc6d4e)
    * [Do you add https by extending web application](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=50516324-31ec-49b9-9dd5-2cedb7e1104f)
    * [Do you fix search with Office App for content preview ? (on premise only)](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=9ec780bc-a7a7-475a-b975-0a1e3448f5af)
2. Configure metadata (optional)


* **Test test**                **tes**  **t**
* **Go-live migration**


1. [Put old SharePoint into read-only](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=0ae3a717-ad22-4d2e-bd7c-a5f058393087)
2. [Refresh content & service database from SP 2013 to 2016](https&#58;//technet.microsoft.com/en-us/library/ff607581%28v=office.16%29.aspx)
3. Update DNS
4. Decommission old SharePoint server and database (after 2 weeks when you're confident with the new environment)
