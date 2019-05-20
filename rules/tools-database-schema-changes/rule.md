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


<p class="ssw15-rteElement-P">It is important when deploying your database for the database to be updated automatically.​​​<br></p>

<br><excerpt class='endintro'></excerpt><br>
<p>There are a number of tools that can be used to update the database as the application can be updated.<br></p><ul><li><a href="https&#58;//docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/">Entity Framework Core Migrations&#160;</a>&#160;(This is the suggested method if you are starting a new project)</li><li><a href="https&#58;//technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx">DAC Support For SQL Server Objects and Versions</a>&#160;&#160;(.dacpac files)</li><li><a href="https&#58;//dbup.readthedocs.io/en/latest/">DBUp</a></li></ul><p>Legacy full framework<br></p><ul><li><a href="http&#58;//sqldeploy.com/">SQL Deploy&#160;</a>&#160;&#160;(This is the suggested tool if you are not using Entity Framework&#160;Code First)<br></li><li>DBUp&#160;+ SQL verify<br></li></ul><p>Bad options for updating database schema - No ability to validate that the database hasn't been tampered with&#160;<br></p><ul><li>SQL Management&#160;Studio + OSQL&#160; (Free and roll your own)</li><li>Visual Studio 2017 +&#160;<a href="https&#58;//visualstudio.microsoft.com/vs/features/ssdt/">SQL Server Data Tools&#160;</a>&#160;(Formerly&#160;Data Dude) + Deploy&#160;(post-development model)</li><li>Red Gate SQL Compare + Red Gate SQL Packager (post-development model)<br></li></ul>


