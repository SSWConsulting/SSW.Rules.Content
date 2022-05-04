---
type: rule
title: Should you compare schemas for deployment?
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
Modern frameworks such as Entity Framework remove the need for comparing databases between environments especially if you are using the code first approach with migrations.

With legacy applications and sometimes with modern frameworks a comparison tool needs to be used to answer the question, "Is your database the same as mine?". 

<!--endintro-->

Tools like [Red Gates SQL Compare](https://www.red-gate.com/products/sql-development/sql-compare/) and [Microsoft's Schema Compare](https://docs.microsoft.com/en-us/sql/ssdt/how-to-use-schema-compare-to-compare-different-database-definitions) will do the job. 

![Figure: Using Red Gates SQL Compare](red-gate-sql-compare.png)  

![Figure: Using Microsoft's Schema Compare](microsoft-schema-compare.png)  

However, if you are doing this at the end of your release cycle, you have a problem.  Your schema deployment process is broken.

What you should be doing is seeing your [Schema Master](/have-a-schema-master "Database Schema Master") each time you have a new .sql file. You do this **during the development process**, not at the end in the package and deployment process.
