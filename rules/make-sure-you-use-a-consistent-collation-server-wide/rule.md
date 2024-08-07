---
seoDescription: Ensure consistent collation server-wide to simplify development and avoid errors when joining tables across databases.
type: rule
archivedreason:
title: DBAs - Do you make sure you use a consistent Collation server-wide?
guid: 4ef6c98b-e828-4e98-98b2-cf0249bdb172
uri: make-sure-you-use-a-consistent-collation-server-wide
created: 2019-11-22T20:49:31.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-make-sure-you-use-a-consistent-collation-server-wide
---

Collation is the combination of language and sort orders, and you typically don't notice it until you start running cross-database queries.

It would make development simpler if the whole world spoke one language but even if you are using English, you will still encounter collation issues if you are not careful. The most common issue is the dreaded 'Cannot resolve collation conflict for equal to operation' error when joining on columns that have different collation orders. Collation is a great feature for international companies, but if you are not consciously using it then you should have ALL the objects in ALL the databases on ALL the servers using a consistent collation.

<!--endintro-->

Flexibility with collation orders has increased a lot since SQL 7.0:

* SQL 7: Back in SQL Server 7, you could only define the collation at the server level and, once it was set, you could not change it without rebuilding the master database.
* SQL 2000: This added the ability to have Column level collation which allows you to set it at the database or column level.

However, with this column-level flexibility come additional issues. It is ideal for those who only want the column name 'FirstName' to be represented in accent insensitive sort order. However, one of the side effects, if you are not taking notice of collation, is that you end up with many different collations on many different databases.

We feel that the only time you need inconsistent collations is when you have a rogue 3rd Party application like Microsoft Great Plains that enforces its own collation.

See these Knowledge Base articles for more information about the issues you will encounter when you have inconsistent collations:

* **Why do I get the error 'Cannot resolve collation conflict for equal to operation'?**
  The database collation differs from the SQL Server default collation because it was attached or created with a different collation order. This causes issues when you attempt to join tables in databases that have different collation orders. For example, if your tempdb database and Northwind each have a different collation you will get the following error 'Cannot resolve collation conflict for equal to operation' when you attempt to do a join between tables from these databases
* **How do I change the collation order in my SQL Server 2000 or 7.0 database?**
  There is no 'recommended' collation as different collations will be used in different countries but as a guideline, installations in the United States and installations that require compatibility with SQL Server 7 databases should use the SQL_Latin1_General_Cp1_CI_AS collation. Non-United States installations in English speaking countries should use the Latin1_General_CI_AS collation

![Figure: Setting the collation in SQL 2019 Setup - Choose Case Insensitive(CI), Accent Sensitive (AS)](Sql2019_CollationSettingsAtSetup.png)
