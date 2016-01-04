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



<span class='intro'> <p class="ssw15-rteElement-P">​​It is important when deploying your database for the database to be updated automatically.<br></p><p class="ssw15-rteElement-P">There are a number of tools that can be used to update the database as the application can be updated.</p><ul><li><a href="https&#58;//msdn.microsoft.com/en-us/data/jj591621.aspx" style="line-height&#58;21px;">Entity Framework Code First Migrations​​​​</a>&#160;(This is the suggested method if you are starting a new project)</li><li><a href="http&#58;//sqldeploy.com/" style="line-height&#58;20px;background-color&#58;initial;">SQL Deploy</a><span style="line-height&#58;20px;background-color&#58;initial;">&#160;(Th</span><span style="line-height&#58;20px;background-color&#58;initial;">is is the suggested tool if you are not using Entity Framework</span><span style="line-height&#58;20px;background-color&#58;initial;"> Code First)</span></li><li><span style="line-height&#58;20px;background-color&#58;initial;"><a href="https&#58;//technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx" style="background-color&#58;initial;">DAC Support For SQL Server Objects and Versions</a><span style="background-color&#58;initial;">&#160;</span><span style="background-color&#58;initial;">&#160;(.dacpac files)</span></span></li><li><span style="line-height&#58;20px;background-color&#58;initial;"><span style="background-color&#58;initial;"></span></span><span style="line-height&#58;20px;background-color&#58;initial;">DBUp + SQL verify</span></li></ul><div>​Bad options for updating database schema​ - No ability to validate that the database hasn't been tampered with​<br></div><ul><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;">SQL Management </span><span style="background-color&#58;initial;">Studio + OSQL&#160; (Free and roll your own)​</span></p></li><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;"></span><span style="background-color&#58;initial;">Visual Studio 2015 +&#160;</span><a href="https&#58;//msdn.microsoft.com/en-us/library/hh272686%28v=vs.103%29.aspx" style="background-color&#58;initial;">SQL Server Data Tools​</a><span style="background-color&#58;initial;">​&#160;(Formerly&#160;Data Dude) + Deploy&#160;(post development model)</span></p></li><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;">Red Gate SQL Compare + Red Gate SQL Packager (post development model)</span></p></li></ul><span style="line-height&#58;21px;"><p></p></span>
 </span>




