---
type: rule
title: Do you know the best tools for Database Schema Update?
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
redirects:
  - do-you-know-the-tools-that-can-help
  - do-you-know-the-best-tools-for-database-schema-update
created: 2009-10-06T23:23:45.000Z
archivedreason: null
guid: 8d700b5d-5bc6-47ea-a3aa-025b77487475
---
It is important when deploying your database for the database to be updated automatically.

<!--endintro-->

There are a number of tools that can be used to update the database as the application can be updated.

* [Entity Framework Core Migrations](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/) (This is the suggested method if you are starting a new project)
* [DAC Support For SQL Server Objects and Versions](https://technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx)  (.dacpac files)
* [DBUp](https://dbup.readthedocs.io/en/latest/)


Legacy full framework

* [SQL Deploy](http://sqldeploy.com/)  (This is the suggested tool if you are not using Entity Framework Code First)
* DBUp + 
      [SQL verify](https://www.nuget.org/packages/SSW.SqlVerify.Core/)
* [Navicat for MySQL](https://navicat.com/manual/online_manual/en/navicat/win_manual/#/structure_sync)
* [DataGrip](https://www.jetbrains.com/help/datagrip/differences-viewer-for-routines.html)


❌  Bad options for updating database schema - No ability to validate that the database hasn't been tampered with

* SQL Management Studio + OSQL  (Free and roll your own)
* Visual Studio + [SQL Server Data Tools](https://visualstudio.microsoft.com/vs/features/ssdt/) (Formerly Data Dude) + Deploy (post-development model)
* Red Gate SQL Compare + Red Gate SQL Packager (post-development model)

::: bad  
![Figure: Don't use Data Dude](DataDude-BadExample.jpg)  
:::


```cs
public partial class GenderToString : DbMigration
{
   public override void Up()
   {
      AddColumn("dbo.Customers", "GenderTemp", c => c.Boolean(nullable: false));
      Sql("UPDATE [dbo].[Customers] set GenderTemp = Gender");
      DropColumn("dbo.Customers", "Gender");
      AddColumn("dbo.Customers", "Gender", c => c.String(maxLength: 2));
      Sql("UPDATE [dbo].[Customers] set Gender = 'M' where GenderTemp=1");
      Sql("UPDATE [dbo].[Customers] set Gender = 'F' where GenderTemp=0");
      DropColumn("dbo.Customers", "GenderTemp");
   }
}
```

::: good
Good Example - Data motion with EF Migrations
:::