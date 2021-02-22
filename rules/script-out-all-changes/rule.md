---
type: rule
archivedreason: 
title: ​DBAs - Do you script out all changes?
guid: 94b925fd-1c39-4761-a61b-27ad9b899060
uri: script-out-all-changes
created: 2019-11-18T19:21:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- dbas-do-you-script-out-all-changes

---


<p>​Every time a change is made to your product's SQL Server Database, script out the change. You can use Enterprise Manager, VS.NET or Query Analyzer but every time you make changes you must save the change as a .sql script file so any alterations are scripted. Everything at SSW is usually done three times, once on Development, once on Staging and once on Production. Change control is one of the most important processes in ensuring a stable database system.<br></p><p>Keep the scripts in a separate directory to any other scripts or files. This way you can always go back to them and find out what alterations you have made to the database in version xxx to find errors. If you have all the scripts you are able to rebuild the database from scratch. At SSW we name this folder SQLChangeScripts so as to not confuse it with other script folders.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>
      <img src="SQLChangeScripts.jpg" alt="SQLChangeScripts.jpg" />
   </dt><dd>Figure: A list of change SQL scripts, each file name is in the correct format</dd></dl><p>The script file format should be: &lt;version&gt;_&lt;description&gt;.sql</p><p>The &lt;version&gt; should be a number which is padded with leading zeros (0) on the right to firm 3 or 4 digits (however long we need).​​​​<br><br></p>


