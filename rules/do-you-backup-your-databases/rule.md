---
type: rule
title: Do you backup your databases?
uri: do-you-backup-your-databases
created: 2015-08-12T16:20:53.0000000Z
authors: []

---



<span class='intro'> <p>Before starting your upgrade, you should back up all your TFS databases.</p><p>​It's important that you backup TFS by using one of the supported methods, to ensure that you can reliably restore your data if needed.</p> </span>

<p><strong>​Tip&#58;&#160;</strong>The Team Foundation Server Team Foundation Server 2012 Update 2 and above has a built in Scheduled Backup tool which helps you to easily backup all TFS Databases. For versions prior to TFS 2012 Update 2 you have to use Backups tool&#160;from the&#160;<a href="http&#58;//visualstudiogallery.msdn.microsoft.com/b1ef7eb2-e084-4cb8-9bc7-06c3bad9148f">TFS Power Tools</a>&#160; &#160;package.</p><p><strong><br></strong></p><p><strong>Figure&#58; TFS Scheduled Backups Tool</strong></p><p>In some cases you won't be able to use this tool e.g. with TFS 2012 Power Tools RTM. This version has a bug which causes a failure of Tfs_Configuration DB when you try to restore it.</p><p><strong>Figure&#58; TFS Backup tool failed to restore the Tfs_Configuration DB – known bug in TFS 2012 Power Tools RTM</strong></p><p>In such case you will have to manually backup databases. Make sure all relevant databases have been backed up. This includes all those starting with &quot;Tfs_&quot;</p><p><strong>Figure&#58; Backup all relevant databases</strong></p><p>IMPORTANT</p><p>Manual backup requires additional user steps which involve creation of additional tables and stored procedures. These tables has to be created to keep TFS databases in sync.<br> Follow this instructions to properly backup your databases&#58;<a href="http&#58;//msdn.microsoft.com/en-us/library/ms253070.aspx">Manually back up Team Foundation Server</a>&#160; .</p><p><strong>Figure&#58; Add tbl_TfsTransactionLogMark table to every Tfs_* Database</strong></p><p><strong>Figure&#58; Add sp_SetTransactionLogMark stored procedure to every Tfs_* Database</strong></p><p>If you manually backup the TFS Databases make sure you add additional jobs that execute 1 minute before the backup kick off.</p><p><strong>Figure&#58; Add additional jobs to SQL Server Agent</strong></p><p>Make sure you back up the Reporting Services database if you'd like your reports to come across as well. </p><p>For Reporting Services make sure you have backed up the encryption key.</p><p><strong>Figure&#58; Backup Reporting Services encryption keys</strong></p>


