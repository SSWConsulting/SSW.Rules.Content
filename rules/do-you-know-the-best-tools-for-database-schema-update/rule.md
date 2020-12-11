---
type: rule
archivedreason: 
title: Do you know the best tools for Database Schema Update?
guid: 8d700b5d-5bc6-47ea-a3aa-025b77487475
uri: do-you-know-the-best-tools-for-database-schema-update
created: 2009-10-06T23:23:45.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 40
  title: Igor Goldobin
- id: 24
  title: Adam Stephensen
- id: 53
  title: Thiago Passos
- id: 34
  title: Brendan Richards
related: []

---

It is important when deploying your database for the database to be updated automatically.

<!--endintro-->

There are a number of tools that can be used to update the database as the application can be updated.

* [Entity Framework Core Migrations](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/) (This is the suggested method if you are starting a new project)
* [DAC Support For SQL Server Objects and Versions](https://technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx)  (.dacpac files)
* [DBUp](https://dbup.readthedocs.io/en/latest/)


Legacy full framework

* [SQL Deploy](http://sqldeploy.com/)  (This is the suggested tool if you are not using Entity Framework Code First)
* DBUp + <br>      [SQL verify](https://www.nuget.org/packages/SSW.SqlVerify.Core/)
* [Navicat for MySQL](https://navicat.com/manual/online_manual/en/navicat/win_manual/#/structure_sync)
* [DataGrip](https://www.jetbrains.com/help/datagrip/differences-viewer-for-routines.html)


Bad options for updating database schema - No ability to validate that the database hasn't been tampered with

* SQL Management Studio + OSQL  (Free and roll your own)
* Visual Studio + [SQL Server Data Tools](https://visualstudio.microsoft.com/vs/features/ssdt/) (Formerly Data Dude) + Deploy (post-development model)
* Red Gate SQL Compare + Red Gate SQL Packager (post-development model)

<dl class="badImage">&lt;dt&gt;<img src="DataDude-BadExample.jpg" alt="">&lt;/dt&gt;<dd>Figure: Don't use Data Dude</dd></dl>
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


::: good
Good Example - Data motion with EF Migrations

:::


### Related Rule



* [Do you make sure that the database structure is handled automatically via 3 buttons "Create", "Upgrade" and "Reconcile"?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=422274e3-db29-4950-b4e7-05361b3a37e0)
