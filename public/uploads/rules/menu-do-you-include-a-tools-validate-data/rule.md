---
seoDescription: Ensure data integrity by including a "Tools | Validate Data" feature in your application to prevent invalid data from entering the system.
type: rule
archivedreason:
title: Menu - Do you include a "Tools | Validate Data"?
guid: 8afbe219-50fc-439c-a866-df3f4e085221
uri: menu-do-you-include-a-tools-validate-data
created: 2012-11-27T02:53:35.0000000Z
authors: []
related:
  - validate-each-denormalized-field-with-procvalidate
redirects:
  - menu-do-you-include-a-＂tools-validate-data＂
---

A common oversight is applications don't check for invalid data. You should add "Tools | Validate Data" to your application.

<!--endintro-->

So when you add business rules to the middle tier, consider scenarios such as importing data and any other areas that side step business rules. Therefore we always make validate queries that if they return records, they must be fixed. Examples are:

- For SQL Server we use **vwValidateClient_MustHaveACategoryID** , or **procValidateClient_MustHaveACategoryID**
- For Access we use **qryValidateClient_MustHaveACategoryID**

::: good  
![Figure: Good Example - This application, while not the prettiest, has a handy validation tool to check for incorrect data](../../assets/TimeProValidateData.png)  
:::
