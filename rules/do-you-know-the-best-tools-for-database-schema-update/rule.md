---
type: rule
title: Do you know the best tools for Database Schema Update?
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

---



<span class='intro'> <p class="ssw15-rteElement-P">It is important when deploying your database for the database to be updated automatically.​​​<br></p>
 </span>

<p>There are a number of tools that can be used to update the database as the application can be updated.<br></p><ul><li>
      <a href="https&#58;//docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/">Entity Framework Core Migrations&#160;</a>&#160;(This is the suggested method if you are starting a new project)</li><li>
      <a href="https&#58;//technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx">DAC Support For SQL Server Objects and Versions</a>&#160;&#160;(.dacpac files)</li><li>
      <a href="https&#58;//dbup.readthedocs.io/en/latest/">DBUp</a></li></ul><p>Legacy full framework<br></p><ul><li>
      <a href="http&#58;//sqldeploy.com/">SQL Deploy&#160;</a>&#160;&#160;(This is the suggested tool if you are not using Entity Framework&#160;Code First)<br></li><li>DBUp&#160;+ 
      <a href="https&#58;//www.nuget.org/packages/SSW.SqlVerify.Core/">SQL verify​</a><br></li></ul><p>Bad options for updating database schema - No ability to validate that the database hasn't been tampered with&#160;<br></p><ul><li>SQL Management&#160;Studio + OSQL&#160; (Free and roll your own)</li><li>Visual Studio 2017 +&#160;<a href="https&#58;//visualstudio.microsoft.com/vs/features/ssdt/">SQL Server Data Tools&#160;</a>&#160;(Formerly&#160;Data Dude) + Deploy&#160;(post-development model)</li><li>Red Gate SQL Compare + Red Gate SQL Packager (post-development model)<br></li></ul><dl class="badImage"><dt><img src="/PublishingImages/DataDude-BadExample.jpg" alt="" /></dt><dd>Figure&#58; Don't use Data Dude</dd></dl><p class="ssw15-rteElement-CodeArea">public partial class GenderToString &#58; DbMigration<br> &#123;<br> public override void Up()<br> &#123;<br> AddColumn(&quot;dbo.Customers&quot;, &quot;GenderTemp&quot;, c =&gt; c.Boolean(nullable&#58; false));<br> Sql(&quot;UPDATE [dbo].[Customers] set GenderTemp = Gender&quot;);<br> DropColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;);<br> AddColumn(&quot;dbo.Customers&quot;, &quot;Gender&quot;, c =&gt; c.String(maxLength&#58; 2));<br> Sql(&quot;UPDATE [dbo].[Customers] set Gender = 'M' where GenderTemp=1&quot;);<br> Sql(&quot;UPDATE [dbo].[Customers] set Gender = 'F' where GenderTemp=0&quot;);<br> DropColumn(&quot;dbo.Customers&quot;, &quot;GenderTemp&quot;);<br> &#125;</p><dd class="ssw15-rteElement-FigureGood">​Good Example - Data motion with EF Migrations<br></dd>​

<h3 class="ssw15-rteElement-H3">Related Rule​​<br></h3><div><ul><li>​<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=422274e3-db29-4950-b4e7-05361b3a37e0">Do you make sure that the database structure is handled automatically via 3 buttons &quot;Create&quot;, &quot;Upgrade&quot; and &quot;Reconcile&quot;?</a></li></ul></div>


