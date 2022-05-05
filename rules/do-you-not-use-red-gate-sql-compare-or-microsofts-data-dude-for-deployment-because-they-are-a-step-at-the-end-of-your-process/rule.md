---
type: rule
title: Do you know why you shouldn't compare schemas during deployment?
uri: should-you-compare-schemas
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-not-use-red-gate-sql-compare-(or-microsofts-data-dude)-for-deployment-(because-they-are-a-step-at-the-end-of-your-process)
  - do-you-not-use-red-gate-sql-compare-or-microsofts-data-dude-for-deployment-because-they-are-a-step-at-the-end-of-your-process
created: 2009-10-05T23:21:49.000Z
archivedreason: null
guid: 089dc980-69cf-4b81-9320-57c2539c1f02
---
SQL Compare is a good tool to find out the differences between two databases. It can help you answer the question "Is your database the same as mine?". 

However, if you are doing this at the end of your release cycle, you have a problem.  Your schema deployment process is broken...

<!--endintro-->

What you should be doing is seeing your [Schema Master](/have-a-schema-master "Database Schema Master") each time you have a new .sql file. You do this **during the development process**, not at the end in the package and deployment process.

::: greybox
**Tip:** If you are using modern methods such as Entity Framework code first migrations you will already be doing most of this.
:::

Tools like [Red Gates SQL Compare](https://www.red-gate.com/products/sql-development/sql-compare/) and [Microsoft's Schema Compare (aka Data Dude)](https://docs.microsoft.com/en-us/sql/ssdt/how-to-use-schema-compare-to-compare-different-database-definitions) will compare schemas really well but aren't useful when you are deploying as it won't be repeatable. 

![Figure: Using Red Gates SQL Compare](red-gate-sql-compare.png)  

![Figure: Using Visual Studio SQL Schema Compare](microsoft-schema-compare.png)  

