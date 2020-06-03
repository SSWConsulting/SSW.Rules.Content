---
type: rule
title: Do you know the right way to define a connection string?
uri: do-you-know-the-right-way-to-define-a-connection-string
created: 2018-04-26T22:05:50.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> The bad practice below because the application can now do anything it wants to the SQL server (e.g. DROP other databases). <br><div><p class="ssw15-rteElement-CodeArea">Server=DRAGON;Database=SSWData2005;Uid=sa;Pwd=password;<br></p></div><div><dd class="ssw15-rteElement-FigureBad">Bad example - The connection string use 'sa' in Uid <br></dd></div> </span>

<p class="ssw15-rteElement-CodeArea">If using SQL Authentication<br>Server=DRAGON;Database=SSWData2005;Uid=SSWWebsite;Pwd=password;Application Name=SSWWebsite <br>If using Windows Authentication (Recommended)<br>Server=DRAGON;Database=SSWData2005;Integrated Security=True;Application Name=SSWWebsite</p><dd class="ssw15-rteElement-FigureGood"> &#160;​Good example - The connection string with Application Name</dd><div><ul><li><p class="ssw15-rteElement-P">Application Name (e.g. SSWWebsite)</p><ul><li>This makes profiling the database easier as you can filter by Application Name</li></ul></li><li>Application Specific Login/Windows Integrated security with a Domain Account for the application (e.g. SSWWebsite)<ul><li>These logins should only have access to the databases they use (e.g. SSWData2005)​<br></li></ul></li></ul></div>


