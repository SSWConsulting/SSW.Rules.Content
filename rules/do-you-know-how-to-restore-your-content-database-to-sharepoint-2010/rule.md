---
type: rule
title: Do you know how to restore your content database to SharePoint 2010?
uri: do-you-know-how-to-restore-your-content-database-to-sharepoint-2010
created: 2010-12-23T07:23:48.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> 
  <p>This is the meat of the migration process. First we need to detach the current content database from the Web Application&#58;</p>
<ol>
    <li>On the SharePoint 2010 server, open <b>SharePoint Central Administration </b>| <b>Application Management </b>| <b>Manage Content Databases</b> </li>
    <li>Set the <b>Database Status</b> to <b>offline </b>| tick <b>Remove content database</b> </li>
    <li>Open <b>SQL Server Management Studio</b> and delete the database you just removed from the web application </li>
</ol>
<p>Now we need to attach the database backup we took of our SharePoint 2007 server&#58;</p>
 </span>


  <ol>
    <li>In <b>SQL Server Management Studio</b> right click on <b>Databases</b> | <b>Restore Database…<br>
    <br>
    <img alt="" src="RestoreDatabase.png" /><br>
    <b><font class="ms-rteCustom-FigureNormal" size="+0"><b>Figure 6 - Select “Restore Database”</b><br>
    </font></b>
    <li>Follow the prompts to restore your database </li>
    </b></li>
    <li>Take the database out of read only mode (it will be in read only mode because we backed it up in read only mode) </li>
</ol>
<p>Now we need to attach the content database to the web application&#58;</p>
<ol>
    <li>Open up the <b>SharePoint 2010 Management Shell</b> with administrative permissions. </li>
    <li>Run the following command to attach the database to the web application (replacing the red text to match your environment)
    <p class="ms-rteCustom-CodeArea"><b>stsadm –o addcontentdb –url </b><b>http&#58;//sp2010rc/</b><b> –databaseserver &lt;DatabaseServerName&gt; –databasename &lt;ContentDatabaseName&gt;</b> </p>
    </li>
    <li>After the database has been restored you will get a status message telling you how the upgrade went, with the path to a log file. Send this file to the SharePoint developers to determine if any issues occurred during the migration </li>
</ol>



