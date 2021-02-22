---
type: rule
archivedreason: 
title: Do you backup your databases?
guid: b72a8d91-b030-4522-8059-6daee855c6e6
uri: do-you-backup-your-databases1
created: 2015-08-12T16:20:53.0000000Z
authors: []
related: []
redirects:
- do-you-backup-your-databases

---


<p>Before starting your upgrade, you should back up all your TFS databases.</p><p>​It's important that you backup TFS by using one of the supported methods, to ensure that you can reliably restore your data if needed.</p>
<br><excerpt class='endintro'></excerpt><br>
<p><strong>​Tip: </strong>The Team Foundation Server Team Foundation Server 2012 Update 2 and above has a built in Scheduled Backup tool which helps you to easily backup all TFS Databases. For versions prior to TFS 2012 Update 2 you have to use Backups tool from the <a href="http://visualstudiogallery.msdn.microsoft.com/b1ef7eb2-e084-4cb8-9bc7-06c3bad9148f">TFS Power Tools</a>   package.</p><p><strong><img src="tfs scheduled.jpg" alt="tfs scheduled.jpg" style="margin:5px;" /><br></strong></p><p><strong>Figure: TFS Scheduled Backups Tool</strong></p><p>In some cases you won't be able to use this tool e.g. with TFS 2012 Power Tools RTM. This version has a bug which causes a failure of Tfs_Configuration DB when you try to restore it.</p><p><img src="tfs backup.jpg" alt="tfs backup.jpg" style="margin:5px;" /><br></p><p><strong>Figure: TFS Backup tool failed to restore the Tfs_Configuration DB – known bug in TFS 2012 Power Tools RTM</strong></p><p>In such case you will have to manually backup databases. Make sure all relevant databases have been backed up. This includes all those starting with "Tfs_"</p><p><strong><br></strong></p><p><strong><img src="backup all.jpg" alt="backup all.jpg" style="margin:5px;" /></strong> </p><p><strong>Figure: Backup all relevant databases</strong></p><p>IMPORTANT</p><p>Manual backup requires additional user steps which involve creation of additional tables and stored procedures. These tables has to be created to keep TFS databases in sync.<br> Follow this instructions to properly backup your databases:<a href="http://msdn.microsoft.com/en-us/library/ms253070.aspx">Manually back up Team Foundation Server</a>  .</p><p><strong><br></strong></p><p><strong><img src="add tbl.jpg" alt="add tbl.jpg" style="margin:5px;" /></strong> </p><p><strong>Figure: Add tbl_TfsTransactionLogMark table to every Tfs_* Database</strong></p><p><strong><img src="add spset.jpg" alt="add spset.jpg" style="margin:5px;" /><br></strong></p><p><strong>Figure: Add sp_SetTransactionLogMark stored procedure to every Tfs_* Database</strong></p><p>If you manually backup the TFS Databases make sure you add additional jobs that execute 1 minute before the backup kick off.</p><p><img src="add additional.jpg" alt="add additional.jpg" style="margin:5px;" /><br></p><p><strong>Figure: Add additional jobs to SQL Server Agent</strong></p><p>Make sure you back up the Reporting Services database if you'd like your reports to come across as well. </p><p>For Reporting Services make sure you have backed up the encryption key.</p><p><img src="backup reporting.jpg" alt="backup reporting.jpg" style="margin:5px;" /><br></p><p><strong>Figure: Backup Reporting Services encryption keys</strong></p>


