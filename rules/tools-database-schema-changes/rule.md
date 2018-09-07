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


<p class="ssw15-rteElement-P">It is important when deploying your database for the database to be updated automatically.<br></p><p class="ssw15-rteElement-P">There are a number of tools that can be used to update the database as the application can be updated.</p><ul><li><a href="https&#58;//docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/" style="line-height&#58;21px;">Entity Framework Core Migrations </a>&#160;(This is the suggested method if you are starting a new project)</li><li><a href="https&#58;//technet.microsoft.com/en-us/library/ee210549%28v=sql.110%29.aspx" style="background-color&#58;initial;">DAC Support For SQL Server Objects and Versions</a><span style="background-color&#58;initial;">&#160;</span><span style="background-color&#58;initial;">&#160;(.dacpac files)</span></li><li><span style="line-height&#58;20px;background-color&#58;initial;"><span style="background-color&#58;initial;"></span></span><span style="line-height&#58;20px;background-color&#58;initial;"><a href="https&#58;//dbup.readthedocs.io/en/latest/">DBUp<span></span><span></span> </a></span></li></ul><div><br></div><div>Legacy full framework<br><ul><li>​<span></span><a href="http&#58;//sqldeploy.com/">SQL Deploy </a>&#160;&#160;(This is the suggested tool if you are not using Entity Framework&#160;Code First)<br></li><li>DBUp&#160;+ SQL verify<br></li></ul>​<br></div><div>Bad options for updating database schema - No ability to validate that the database hasn't been tampered with <br></div><ul><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;">SQL Management </span><span style="background-color&#58;initial;">Studio + OSQL&#160; (Free and roll your own) </span></p></li><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;"></span><span style="background-color&#58;initial;">Visual Studio 2017 +&#160;</span><a href="https&#58;//visualstudio.microsoft.com/vs/features/ssdt/" style="background-color&#58;initial;">SQL Server Data Tools </a><span style="background-color&#58;initial;"> &#160;(Formerly&#160;Data Dude) + Deploy&#160;(post-development model)</span></p></li><li><p class="ssw15-rteElement-P"><span style="background-color&#58;initial;">Red Gate SQL Compare + Red Gate SQL Packager (post-development model)</span></p></li></ul><span style="line-height&#58;21px;"><p></p></span>

<br><excerpt class='endintro'></excerpt><br>



