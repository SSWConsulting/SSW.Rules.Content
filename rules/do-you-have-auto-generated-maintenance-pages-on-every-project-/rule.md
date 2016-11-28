---
type: rule
title: Do you have auto-generated maintenance pages on every project ?
uri: do-you-have-auto-generated-maintenance-pages-on-every-project-
created: 2016-11-28T18:52:32.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Nowadays, most application are dealing with Data. And it would be nice to have maintenance pages to manage data (select, insert, update and delete).</p><p>We recommend you create the maintenance pages by netTiers.&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Developergeneral/netTools.aspx#NetTiers">netTiers</a>&#160;is a set of open source code templates used in CodeSmith for object-relational mapping. It automatically generates a personalized Data Tiers application (on a base of a SQL Server Database) in just a few minutes. With the application it generated, you can manage data of a web application easily and efficiently.</p><p>Please follow these steps to create your maintenance pages.&#160; <br></p> </span>

<ol><li>
      <a href="/ssw/redirect/CodeSmith.htm" target="_blank">Download</a>&#160;CodeSmith.</li><li>
      <a href="/ssw/redirect/nettiers.htm" target="_blank">Download</a> .netTiers and extract to a folder (e.g., C&#58;\Program Files\Net Tiers)</li><li>Install CodeSmith.</li><li>Run C&#58;\Program Files\Net Tiers\NetTiers.cst.</li><li>Set requires properties following ​<a href="/ssw/redirect/nettiers.htm" target="_blank">instructions</a>.</li><dl class="image"><dt>
         ​<img src="/PublishingImages/NetTiersConfig.jpg" alt="" />  
         <br>
      </dt><dd>Figure&#58; Properties Window</dd></dl><li>Generate.</li><li>Open the solution.<br></li><li>Build it and run it in IE.</li><li>Congratulations! It's up and running.</li>
   <dl class="image">
      <dt>
         <img src="/PublishingImages/RunNorthwind.jpg" alt="" />
      </dt><dd>Figure&#58; The application is running</dd></dl></ol><p>Code Smith enables to do this generate with a single command. If you want to generate it again, just run this command.</p><dl class="code"><dt><pre>cs D&#58;\DataDavidBian\Personal\New12345\NetTiers.csp</pre></dt><dd>Figure&#58; An example of command line of Code Smith for NorthWind</dd></dl><p>We recommend you put this command in a file called &quot;_Regenerate.bat&quot; and add it in the solution in case you will generate it again in future.</p>
<br>


