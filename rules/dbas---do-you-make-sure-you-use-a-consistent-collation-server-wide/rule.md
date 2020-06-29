---
type: rule
title: DBAs - Do you make sure you use a consistent Collation server-wide?
uri: dbas---do-you-make-sure-you-use-a-consistent-collation-server-wide
created: 2019-11-22T20:49:31.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​Collation is the combination of language and sort orders, and you typically don't notice it until you start running cross-database queries.<br></p><p>It would make development simpler if the whole world spoke one language but even if you are using English, you will still encounter collation issues if you are not careful. The most common issue is the dreaded 'Cannot resolve collation conflict for equal to operation' error when joining on columns that have different collation orders. Collation is a great feature for international companies, but if you are not consciously using it then you should have ALL the objects in ALL the databases on ALL the servers using a consistent collation.​​<br></p> </span>

<p>Flexibility with collation orders has increased a lot since SQL 7.0&#58;<br></p><ul><li>SQL 7&#58; Back in SQL Server 7, you could only define the collation at the server level and, once it was set, you could not change it without rebuilding the master database.</li><li>SQL 2000&#58; This added the ability to have Column level collation which allows ​you to set it at the database or column level.</li></ul><p>However, with this column-level flexibility come additional issues. It is ideal for those who only want the column name 'FirstName' to be represented in accent insensitive sort order. However, one of the side effects, if you are not taking notice of collation, is that you end up with many different collations on many different databases.<br></p><p>We feel that the only time you need inconsistent​​ collations is when you have a rogue 3rd Party application like Microsoft Great Plains that enforces its own collation.</p><p>See these Knowledge Base articles for more information about the issues you will encounter when you have inconsistent collations&#58;</p><ul><li>
      <a href="https&#58;//www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q211874"><strong>Q211874</strong>&#160;- Why do I get the error 'Cannot resolve collation conflict for equal to operation'?</a></li><p>The database collation differs from the SQL Server default collation because it was attached or created with a different collation order. This causes issues when you attempt to join tables in databases that have different collation orders. For example, if your tempdb database and Northwind each have a different collation you will get the following error 'Cannot resolve collation conflict for equal to operation' when you attempt to do a join between tables from these databases<br></p><li>
      <a href="https&#58;//www.ssw.com.au/ssw/KB/KB.aspx?KBID=Q711843"><strong>Q711843</strong>&#160;- How do I change the collation order in my SQL Server 2000 or 7.0 database?</a></li><p>There is no 'recommended' collation as different collations will be used in different countries but as a guideline, installations in the United States and installations that require compatibility with SQL Server 7 databases should use the SQL_Latin1_General_Cp1_CI_AS collation. Non-United States installations in English speaking countries should use the Latin1_General_CI_AS collation​​<br></p></ul><dl class="image"><dt>​<img src="Sql2019_CollationSettingsAtSetup.png" alt="" style="margin&#58;5px;width&#58;653px;height&#58;455px;" /><br></dt><dd>Figure​&#58; Setting the collation in SQL 2019&#160;Setup - Choose Case Insensitive(CI), Accent Sensitive (AS)<br></dd></dl>


