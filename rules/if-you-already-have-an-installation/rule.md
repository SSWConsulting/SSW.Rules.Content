---
type: rule
archivedreason: 
title: If you already have an installation
guid: 46d7e5f8-996e-425b-833e-a490fb009293
uri: if-you-already-have-an-installation
created: 2009-11-08T02:17:48.0000000Z
authors: []
related: []

---



  <p>If you have already done some test migrations on the new server there is no need to start from scratch. Just follow these simple steps and you will be up and running in no time.</p>
<ol>
    <li>Open the Team Foundation Server Admin Console </li>
    <li>Click Application Tier | Team Project Collections | Detach Team Project Collection<br>
    <span><img style="width:500px;height:375px;" alt="Detach Team Project Collection" src="Detach Team Project Collection.png" /></span> <br>
    <font class="ms-rteCustom-FigureNormal" size="+0">Figure: Remove the old Team Project Collection from the server.</font> </li>
    <li>Delete the Tfs_* databases except Tfs_Configuration from SQL Server Management Studio </li>
    <li>Delete the Tfs_Analysis database from SQL Server Analysis Server. </li>
    <li>Copy the TFS2010 backups to TFS2010 server (e.g. C:\TfsBackups) </li>
    <li>Restore the databases to the TFS2010’s SQL 2008 Server </li>
    <li>In the Team Foundation Server Admin Console </li>
    <li>Click Application Tier | Team Project Collections |Attach Team Project Collection<br>
    <span><img style="width:500px;height:375px;" alt="Attach Team Project Collection" src="Attach Team Project Collection.png" /></span> </li>
    <li>Follow the wizard, <a shape="rect" href="/Pages/UpgradeTFS2008Databases.aspx">rule #8 from step 13</a>. </li>
</ol>
<div><br>
</div>

<br><excerpt class='endintro'></excerpt><br>



