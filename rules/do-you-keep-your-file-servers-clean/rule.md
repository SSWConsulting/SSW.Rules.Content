---
type: rule
archivedreason: 
title: Do you keep your file servers clean?
guid: 5918c87e-1350-450a-8acf-2ed58235018a
uri: do-you-keep-your-file-servers-clean
created: 2017-06-30T23:58:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 47
  title: Stanley Sidik
related: []

---

How often do you find files on your network file server that clearly shouldn't be there? Developers are notorious for creating temporary files and littering your file system with them. So how can you identify exactly who created or modified the file, and when?


<!--endintro-->
<dl class="image">&lt;dt&gt; <img src="DuplicateFile.png" alt="networkauditing_00.gif" style="width:500px;height:408px;"> &lt;/dt&gt;<dd>Figure: Who created this file?</dd></dl><dl class="image">&lt;dt&gt; <img src="RDP.png" alt="networkauditing_06.gif" style="width:400px;height:253px;"> &lt;/dt&gt;<dd>Figure: Terminal into your file server using Terminal Services</dd></dl><dl class="image">&lt;dt&gt; <img src="FileOwner.png" alt="networkauditing_07.gif" style="width:350px;height:501px;"> &lt;/dt&gt;<dd>Figure: It was Jatin! </dd></dl>
The easiest way is to configure  **Windows file auditing** .

Thankfully, Windows Server come with built-in file auditing. Any changes create and delete can be logged to your system event log. Here's how to set it up.

### How to implement auditing on your file server

1. Terminal Server into the file server
2. In Windows Explorer, locate the directory you want to configure logging for (e.g.  **C:\Inetpub\wwwroot** for logging changes to your website files)
3. Select  **Security** tab |  **Advanced** <dl class="image">&lt;dt&gt; <img src="networkauditing_01.gif" alt="networkauditing_01.gif"> &lt;/dt&gt;<dd>Figure: Select the folder you want to configure auditing for</dd></dl>
4. Click the  **Auditing** tab
5. Select the users whose usage you want to monitor (usually all users, so select  **Everyone** ) <dl class="image">&lt;dt&gt; <img src="networkauditing_02.gif" alt="networkauditing_02.gif"> &lt;/dt&gt;<dd>Figure: Select Everyone so that anyone who modifies any of the files will be logged<br></dd></dl>
6. Select what you want to monitor. For best performance, we only tick the options in shown in the figure below - there's no need to log when someone opens a file. <dl class="image">&lt;dt&gt; <img src="networkauditing_03.gif" alt="networkauditing_03.gif"> &lt;/dt&gt;<dd>Figure: Select these 4 options (only audit the events you need to audit - there's no need to log when someone opens a file)</dd></dl>
7. Click  **OK** and  **OK** again to apply the changes. The process may take some time depending on the number of subfolders and files selected.
Now you need to configure the system event log.
8. Open  **Control Panel->Administrative Tools->Event Viewer**
9. Right-click the  **Security** node and Control Panel | Administrative Tools | Event Viewer
10. Right-click the sure  **Overwrite events as needed** is checked <dl class="image">&lt;dt&gt; <img src="networkauditing_04.gif" alt="networkauditing_04.gif"> &lt;/dt&gt;<dd>Figure: Keep your log file to about 250MB - otherwise, your system performance may suffer<br></dd></dl>


### Checking who created the file

Now test to see if auditing is working.

1. On the server, create a file called "test.aspx" somewhere in the path that is being audited
2. Open  **Control Panel->Administrative Tools->Event Viewer**
3. Select the  **Security** node, and notice the entries that have been created. They will have a similar format to the figure below. <dl class="image">&lt;dt&gt; <img src="networkauditing_05.gif" alt="networkauditing_05.gif"> &lt;/dt&gt;<dd>Figure: Any creates, deletes and updates now get logged to the Event Log</dd></dl>


That's all! It is also great for finding out who accidentally deleted files from the file system.

Furthermore, we can dump the event log to an Access or SQL Server database to make it easier to handle. Here is how to do it:

* [Download the scripts](/Documents/DumpEventLog2Db.zip): one for Access database and the other for SQL Server.
* Find and change the strEventDBConn variable to your connection string, also, modify strEventDB and tblEvents variable to your database name and table name.
* Write down the names of the servers to monitor in EventHosts.txt.


Done, now you need only double-click to start it.
<dl class="image">&lt;dt&gt; <img src="EventLogger.gif" alt="EventLogger.gif"> &lt;/dt&gt;<dd>Figure: Caught an action on remote server and logged it to database<br></dd></dl>
This script is originally from [http://pubs.logicalexpressions.com/pub0009/LPMArticle.asp?ID=340](https://www.ssw.com.au/ssw/Redirect/logicalexpressions.htm).
