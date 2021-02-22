---
type: rule
archivedreason: 
title: Do you keep your file servers clean?
guid: 5918c87e-1350-450a-8acf-2ed58235018a
uri: keep-your-file-servers-clean
created: 2017-06-30T23:58:40.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects:
- do-you-keep-your-file-servers-clean

---


How often do you find files on your network file server that clearly shouldn't be there? Developers are notorious for creating temporary files and littering your file system with them. So how can you identify exactly who created or modified the file, and when?​<br><br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> <img src="DuplicateFile.png" alt="networkauditing_00.gif" style="width:500px;height:408px;" /> </dt><dd>Figure: Who created this file?</dd></dl><dl class="image"><dt> <img src="RDP.png" alt="networkauditing_06.gif" style="width:400px;height:253px;" /> </dt><dd>Figure: Terminal into your file server using Terminal Services</dd></dl><dl class="image"><dt> <img src="FileOwner.png" alt="networkauditing_07.gif" style="width:350px;height:501px;" /> </dt><dd>Figure: It was Jatin! </dd></dl><p>The easiest way is to configure <strong>Windows file auditing</strong>.</p><p>Thankfully, Windows Server come with built-in file auditing. Any changes create and delete can be logged to your system event log. Here's how to set it up.</p><h3>How to implement auditing on your file server</h3><ol><li>Terminal Server into the file server</li><li>In Windows Explorer, locate the directory you want to configure logging for (e.g. <strong>C:\Inetpub\wwwroot</strong> for logging changes to your website files)</li><li>Select <strong>Security</strong> tab | <strong>Advanced</strong> <dl class="image"><dt> <img src="networkauditing_01.gif" alt="networkauditing_01.gif" /> </dt><dd>Figure: Select the folder you want to configure auditing for</dd></dl></li><li>Click the <strong>Auditing</strong> tab<br></li><li>Select the users whose usage you want to monitor (usually all users, so select <strong>Everyone</strong>) <dl class="image"><dt> <img src="networkauditing_02.gif" alt="networkauditing_02.gif" /> </dt><dd>Figure: Select Everyone so that anyone who modifies any of the files will be logged<br></dd></dl></li><li>Select what you want to monitor. For best performance, we only tick the options in shown in the figure below - there's no need to log when someone opens a file. <dl class="image"><dt> <img src="networkauditing_03.gif" alt="networkauditing_03.gif" /> </dt><dd>Figure: Select these 4 options (only audit the events you need to audit - there's no need to log when someone opens a file)</dd></dl></li><li>Click <strong>OK</strong> and <strong>OK</strong> again to apply the changes. The process may take some time depending on the number of subfolders and files selected.<br>Now you need to configure the system event log.<br></li><li>Open <strong>Control Panel-&gt;Administrative Tools-&gt;Event Viewer</strong></li><li>Right-click the <strong>Security</strong> node and Control Panel | Administrative Tools | Event Viewer</li><li>Right-click the sure <strong>Overwrite events as needed</strong> is checked <dl class="image"><dt> <img src="networkauditing_04.gif" alt="networkauditing_04.gif" /> </dt><dd>Figure: Keep your log file to about 250MB - otherwise, your system performance may suffer<br></dd></dl></li></ol>
​
      <h3>Checking who created the file</h3><p>Now test to see if auditing is working.</p><ol><li>On the server, create a file called "test.aspx" somewhere in the path that is being audited</li><li>Open <strong>Control Panel-&gt;Administrative Tools-&gt;Event Viewer</strong></li><li>Select the <strong>Security</strong> node, and notice the entries that have been created. They will have a similar format to the figure below. <dl class="image"><dt> <img src="networkauditing_05.gif" alt="networkauditing_05.gif" /> </dt><dd>Figure: Any creates, deletes and updates now get logged to the Event Log</dd></dl></li></ol><p>That's all! It is also great for finding out who accidentally deleted files from the file system.</p><p>Furthermore, we can dump the event log to an Access or SQL Server database to make it easier to handle. Here is how to do it:<br></p><ul><li> 
            <a href="/Documents/DumpEventLog2Db.zip">Download the scripts</a>: one for Access database and the other for SQL Server.</li><li>Find and change the strEventDBConn variable to your connection string, also, modify strEventDB and tblEvents variable to your database name and table name.</li><li>Write down the names of the servers to monitor in EventHosts.txt.</li></ul><p>Done, now you need only double-click to start it.</p><dl class="image"><dt> <img src="EventLogger.gif" alt="EventLogger.gif" /> </dt><dd>Figure: Caught an action on remote server and logged it to database<br></dd></dl><p>This script is originally from <a href="https://www.ssw.com.au/ssw/Redirect/logicalexpressions.htm">http://pubs.logicalexpressions.com/pub0009/LPMArticle.asp?ID=340</a>.​​</p>


