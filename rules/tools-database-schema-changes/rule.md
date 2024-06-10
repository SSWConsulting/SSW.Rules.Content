---
seoDescription: Discover recommended tools for updating database schemas and ensure seamless deployment of your application updates with .NET 8.
type: rule
title: Do you know the best tools for updating database schemas?
uri: tools-database-schema-changes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Igor Goldobin
    url: https://ssw.com.au/people/igor-goldobin
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Thiago Passos
    url: https://ssw.com.au/people/thiago-passos
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related:
  - the-application-do-you-make-sure-that-the-database-structure-is-handled-automatically-via-3-buttons-create-upgrade-and-reconcile
  - use-code-migrations
redirects:
  - do-you-know-the-tools-that-can-help
  - do-you-know-the-best-tools-for-database-schema-update
created: 2009-10-06T23:23:45.000Z
archivedreason: null
guid: 8d700b5d-5bc6-47ea-a3aa-025b77487475
---

In the fast-evolving world of software development, it's crucial for your database deployment process to be as efficient and reliable as your application updates. With the advent of .NET 8, there are several modern tools and methods that can help you achieve this seamlessly.

<!--endintro-->

### ✅ Recommended Tools for Database Schema Updates

- [Entity Framework Core Migrations](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/): EF Core Migrations has become the de facto standard for managing database schema changes. It offers robust, integrated support for versioning and deploying database changes, making it the preferred choice for both new and existing projects.

- [DAC Support For SQL Server Objects and Versions](https://learn.microsoft.com/en-us/sql/relational-databases/data-tier-applications/data-tier-applications?view=sql-server-ver16) (.dacpac files): Still relevant for SQL Server database management, particularly in complex deployment scenarios.

### ❌ Not Recommended

These methods are outdated and lack the comprehensive features required for modern database schema management, With no ability to validate that the database hasn't been tampered with:

- [SQL Deploy](http://sqldeploy.com/) (This is the suggested tool if you are not using Entity Framework Code First)
- [DbUp](https://dbup.readthedocs.io/en/latest/) + [SQL verify](https://www.nuget.org/packages/SSW.SqlVerify.Core/)
- [Navicat for MySQL](https://navicat.com/manual/online_manual/en/navicat/win_manual/#/structure_sync)
- [DataGrip](https://www.jetbrains.com/help/datagrip/differences-viewer-for-routines.html)
- SQL Management Studio + OSQL (Free and roll your own)
- Visual Studio + [SQL Server Data Tools](https://visualstudio.microsoft.com/vs/features/ssdt/) (Formerly Data Dude) + Deploy (post-development model)
- Red Gate SQL Compare + Red Gate SQL Packager (post-development model)
