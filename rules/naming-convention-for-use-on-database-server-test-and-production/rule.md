---
type: rule
title: Do you know the naming convention for use on database server test and
  production?
uri: naming-convention-for-use-on-database-server-test-and-production
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - general-do-you-know-the-naming-convention-for-use-on-database-server-test-and-production
created: 2019-11-14T21:59:12.000Z
archivedreason: null
guid: 34ceccd7-b18b-4b55-a49e-df311676238e
---

Generally, every client should have a dev and a test database, so the dev database needs to have the postfix "Dev" and the test database need to have the postfix "Test"(E.g. SSWCRMDev, SSWCRMTest). However, you don't need any postfix for the production database.

<!--endintro-->


::: bad  
![Figure: Bad Example - Database with bad names](BadDBName.gif)  
:::


::: good  
![Figure: Good Example - Database with standard names](GoodDBName.gif)  
:::
