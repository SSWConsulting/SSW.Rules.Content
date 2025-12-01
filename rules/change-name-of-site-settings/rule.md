---
seoDescription: Modify SSRS site settings by adding version numbers to easily identify your Reporting Services edition.
type: rule
archivedreason: Similar to the rule [Layout - Do you show which version of Reporting Services you are running?](https://www.ssw.com.au/rules/reporting-services-version)
title: Do you change the name of site settings?
guid: 8affbe6d-5be5-423c-8176-759c6fb43f76
uri: change-name-of-site-settings
created: 2024-09-16T09:05:00.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

The default site settings name of SSRS is "SQL Server Reporting Services" regardless of version 2005 or 2008. So we'd better add the version to the site settings name then users can find the version of SSRS here.

<!--endintro-->

::: bad  
![Figure: Bad example - Site settings without SSRS version](BadSiteSetting.gif)  
:::

::: good  
![Figure: Good example - Site settings with version of SSRS 2005](GoodSiteSetting2005.gif)
:::

::: good  
![Figure: Good example - Site settings with version of SSRS 2008](GoodSiteSetting2008.gif)
:::
