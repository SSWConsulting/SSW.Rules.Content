---
type: rule
archivedreason: 
title: Do you know the best tools for Database Schema Update?
guid: 8d700b5d-5bc6-47ea-a3aa-025b77487475
uri: tools-database-schema-changes
created: 2009-10-06T23:23:45.0000000Z
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
related: []
redirects:
- do-you-know-the-tools-that-can-help
- do-you-know-the-best-tools-for-database-schema-update

---


<p class="ssw15-rteElement-P">​It is important when deploying your database for the database to be updated automatically.​​​<br></p>

<br><excerpt class='endintro'></excerpt><br>
<p>There are a number of tools that can be used to update the database as the application can be updated.<br></p><ul><li>
      <a href="https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/">Entity Framework Core Migrations </a> (This is the suggested method if you are starting a new project)</li><li>
      <a href="https://technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx">DAC Support For SQL Server Objects and Versions</a>  (.dacpac files)</li><li>
      <a href="https://dbup.readthedocs.io/en/latest/">DBUp</a><br></li></ul><p>Legacy full framework​<br></p><ul><li>
      <a href="http://sqldeploy.com/">SQL Deploy </a>  (This is the suggested tool if you are not using Entity Framework Code First)<br></li><li>DBUp + 
      <a href="https://www.nuget.org/packages/SSW.SqlVerify.Core/">SQL verify​</a><br></li><li><a href="https://navicat.com/manual/online_manual/en/navicat/win_manual/#/structure_sync">Navicat for MySQL​</a><br></li><li><a href="https://www.jetbrains.com/help/datagrip/differences-viewer-for-routines.html">DataGrip</a><br>​<br></li></ul><p>Bad options for updating database schema - No ability to validate that the database hasn't been tampered with <br></p><ul><li>SQL Management Studio + OSQL  (Free and roll your own)</li><li>Visual Studio + <a href="https://visualstudio.microsoft.com/vs/features/ssdt/">SQL Server Data Tools </a> (Formerly Data Dude) + Deploy (post-development model)</li><li>Red Gate SQL Compare + Red Gate SQL Packager (post-development model)<br></li></ul><dl class="badImage"><dt><img src="DataDude-BadExample.jpg" alt="" /></dt><dd>Figure: Don't use Data Dude</dd></dl><p class="ssw15-rteElement-CodeArea">public partial class GenderToString : DbMigration<br> {<br> public override void Up()<br> {<br> AddColumn("dbo.Customers", "GenderTemp", c =&gt; c.Boolean(nullable: false));<br> Sql("UPDATE [dbo].[Customers] set GenderTemp = Gender");<br> DropColumn("dbo.Customers", "Gender");<br> AddColumn("dbo.Customers", "Gender", c =&gt; c.String(maxLength: 2));<br> Sql("UPDATE [dbo].[Customers] set Gender = 'M' where GenderTemp=1");<br> Sql("UPDATE [dbo].[Customers] set Gender = 'F' where GenderTemp=0");<br> DropColumn("dbo.Customers", "GenderTemp");<br> }</p><dd class="ssw15-rteElement-FigureGood">​Good Example - Data motion with EF Migrations<br></dd>​

<h3 class="ssw15-rteElement-H3">Related Rule​​<br></h3><div><ul><li>​<a href=/the-application-do-you-make-sure-that-the-database-structure-is-handled-automatically-via-3-buttons-create-upgrade-and-reconcile>Do you make sure that the database structure is handled automatically via 3 buttons "Create", "Upgrade" and "Reconcile"?</a></li></ul></div>


