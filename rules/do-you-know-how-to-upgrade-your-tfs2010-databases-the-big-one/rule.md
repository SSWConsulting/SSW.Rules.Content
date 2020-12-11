---
type: rule
archivedreason: 
title: Do you know how to upgrade your TFS2010 databases? (the big one)
guid: 9a1bafe3-42cf-4859-ba69-f24d6b478f07
uri: do-you-know-how-to-upgrade-your-tfs2010-databases-the-big-one
created: 2012-06-02T01:36:36.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---


<p>We recommend doing a <a href="/Pages/MigrationChoices.aspx">move to a new environment</a> because it has a much easier rollback path if something goes wrong.</p>
<p>Note that these steps will also work for upgrading from TFS 2012 RC to RTM, or RTM to Update 1.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​These are the steps to migrate and upgrade to a new environment:</p>
<ol><li><a href="http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart">Send an email</a> to let everyone know the TFS server will be offline.</li>
<li>Take the TFS 2010 server offline</li>
<li>Copy the TFS 2010 database backups to the TFS server or the new SQL Server instance. Make sure the URL is accessible from the TFS server via a network share.</li>
<li>Install Team Foundation Server 2012 or TFS 2012 Update 1 (<a href="http://blog.damianbrady.com.au/2012/11/27/tfs-2012-with-update-1-done/">see Damian Brady's experiences</a>).</li>
<li>Make sure you have access to coffee while it's installing - it could take a while!<br><img alt="coffee.png" src="ssw-coffee.png" style="width:200px;" /></li>
<li>After the install has completed, the Team Foundation Server Configuration Center will start</li>
<li>Select Upgrade | Start Wizard<br><img alt="tfs_upgrade_existing.png" src="tfs_upgrade_existing.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Launch the Database Restore tool by clicking on the link</li>
<li>If necessary, change the Target SQL Server Instance and click Connect</li>
<li>In the Restore Database screen, Browse, then navigate to the folder with your database backups. Make sure all of them are ticked, then click Restore.<br><img alt="tfs_restore_dbs.png" src="tfs_restore_dbs.png" style="margin:5px;width:600px;height:449px;" /></li>
<li>Click Close, then click Next in the Upgrade Wizard</li>
<li>Choose the configuration database by specifying the SQL Server Instance and clicking List Available Databases</li>
<li>Check "By checking this box, I confirm that I have a current backup.", then click Next<br><img alt="tfs_config_db.png" src="tfs_config_db.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Leave Network Service as the service account for the Application Tier, then click Next</li>
<li>Check the checkbox to confirm we want to configure Reporting Services, then click Next</li>
<li>Make sure the Reporting Services instance and URLs are correct, then click Next<br><img alt="tfs_config_reporting.png" src="tfs_config_reporting.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Update the SQL Server Instance for our Warehouse Database, and click Test to test the connection</li>
<li>Click List Available Databases and check the Tfs_Warehouse database is shown, then click Next<br><img alt="tfs_warehouse.png" src="tfs_warehouse.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Click Next on the Analysis Services page</li>
<li>Provide details of the TFSService account your reports will run as then click Next<br><img alt="tfs_reports_run_as.png" src="tfs_reports_run_as.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Check the checkbox to say we want to configure SharePoint, then click Next</li>
<li>Choose "Use current SharePoint settings", then click Next<br><img alt="tfs_sharepoint.png" src="tfs_sharepoint.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Confirm the details on the Summary page and click Verify<br><img alt="tfs_summary.png" src="tfs_summary.png" style="margin:5px;width:600px;height:450px;" /><br><strong>Note:</strong> At this point, you may be asked to reboot and start the wizard again.  Don't despair - it's quicker the second time!</li>
<li>Once you have all green ticks, click Configure<br><img alt="tfs_final_configure.png" src="tfs_final_configure.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Have a coffee<br><img alt="coffee.png" src="ssw-coffee.png" style="width:200px;" /></li>
<li>Click Next<br><img alt="tfs_upgrade_complete.png" src="tfs_upgrade_complete.png" style="margin:5px;width:600px;height:450px;" /></li>
<li>Click Close, then Close again.</li>
<li>Change the DNS entries for your TFS server to point to the new TFS 2012 server<br><img alt="tfs_dns.png" src="tfs_dns.png" style="margin:5px;" /><br><strong>Note:</strong> It's a good idea to get the SysAdmins involved at this stage</li></ol>



