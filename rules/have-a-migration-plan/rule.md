---
type: rule
archivedreason: 
title: Do you have a Migration plan?
guid: 3c85bc70-7cc7-4d19-b427-fc3dbe43d97a
uri: have-a-migration-plan
created: 2018-01-17T19:21:26.0000000Z
authors:
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-have-a-migration-plan

---

At a high level, the plan is:

<!--endintro-->

* Choose your SharePoint Online Plan (for most companies already included in o365 plan) 
      
[Compare SharePoint Online options](https&#58;//products.office.com/en-us/sharepoint/compare-sharepoint-plans)
* Choose a migration tool to help you migrate the content online 
      
i.e. at SSW we use Sharegate
* Install the migration tool 

* Migration tool - Configure connections to your source and target SharePoint site collections
* Migration tool - Migrate your content
    * Structure migration and content (dry-run)
    * Analyse result reports
    * Fix potential errors and warnings (repeat until you get to zero - see rule #2)
    * Structure migration and content (for real)
* Remove permissions on your on-premises SharePoint site(s) and give access to SharePoint Online
* After a week, decommission your on-premises farm
