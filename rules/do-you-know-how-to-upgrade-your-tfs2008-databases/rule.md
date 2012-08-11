---
type: rule
archivedreason: 
title: Do you know how to upgrade your TFS2008 databases?
guid: 3edaeb78-d469-41d0-94de-1ba2e848155e
uri: do-you-know-how-to-upgrade-your-tfs2008-databases
created: 2009-11-08T00:23:52.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---


<div>Since <a href="/Pages/MigrationChoices.aspx" shape="rect">we recommend doing a &quot;move based upgrade&quot;</a>, we don’t like the &quot;in place upgrade&quot; option, these are the steps&#58;</div>
<div><ol><li>Copy the TFS2008 backups to TFS2010 server (e.g. C&#58;\TfsBackups) </li>
<li>Restore all the databases to TFS2010’s instance of SQL 2008 </li>
<li>Install Team Foundation Server 2010 </li>
<li>After the install has completed the Team Foundation Server Configuration Wizard will open </li>
<li>Select Upgrade | Start Wizard<br><span><img alt="TFS Config - Upgrade" src="/PublishingImages/01-TFS%20Config%20-%20Upgrade.png" style="width&#58;500px;height&#58;375px;" /></span> </li>
<li><span>Click &quot;Next&quot;<br><span><img src="/PublishingImages/02-TFS%20Upgrade%20Wizard%20-%20Upgrade.png" alt="" style="width&#58;500px;height&#58;375px;" /></span></span> </li>
<li><span><span>Click &quot;List Available Databases&quot;</span></span> </li>
<li><span><span>Select the TfsIntegration database</span></span> </li>
<li><span><span>Check &quot;By checking this box, I confirm that I have a current backup&quot;</span></span> </li>
<li><span><span>Click &quot;Next&quot;<br><span><img src="/PublishingImages/03-TFS%20Upgrade%20Wizard%20-%20Databases.png" alt="" style="width&#58;500px;height&#58;375px;" /></span></span></span> </li>
<li><span><span><span>Select &quot;NT AUTHORITY\NETWORK SERVICE&quot; for the System account</span></span></span> </li>
<li><span><span><span>Click &quot;Next&quot;&#160;<br><span><img alt="TFS Upgrade Wizard - Account" src="/PublishingImages/04-TFS%20Upgrade%20Wizard%20-%20Account.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span> </li>
<li><span><a shape="rect" name="StartMigration"></a>Click &quot;Next&quot;<br><img alt="TFS Upgrade Wizard - Application Tier" src="/PublishingImages/05-TFS%20Upgrade%20Wizard%20-%20Application%20Tier.png" style="width&#58;500px;height&#58;375px;" /></span> </li>
<li><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Reporting" src="/PublishingImages/06-TFS%20Upgrade%20Wizard%20-%20Reporting.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Reporting - Reporting Services" src="/PublishingImages/07-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Reporting%20Services.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Reporting - Analysis Services" src="/PublishingImages/08-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Analysis%20Services.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span>Specify the TFSService account</span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Reporting - Report Reader Account" src="/PublishingImages/09-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Report%20Reader%20Account.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Sharepoint" src="/PublishingImages/10-TFS%20Upgrade%20Wizard%20-%20Sharepoint.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Sharepoint - Settings" src="/PublishingImages/11-TFS%20Upgrade%20Wizard%20-%20Sharepoint%20-%20Settings.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Project Collection" src="/PublishingImages/12-TFS%20Upgrade%20Wizard%20-%20Project%20Collection.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Review" src="/PublishingImages/13-TFS%20Upgrade%20Wizard%20-%20Review.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Configure&quot;<br><span><img alt="TFS Upgrade Wizard - Readiness Checks" src="/PublishingImages/14-TFS%20Upgrade%20Wizard%20-%20Readiness%20Checks.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Have coffee (2 hours)<br><span><img alt="Coffee" src="/PublishingImages/ssw-coffee.png" style="width&#58;200px;" /></span><br>BTW&#58; A good user interface should have a coffee image <br>[TODO&#58; Martin to create new rule in &quot;Rules to better UI&quot;]<br>[TODO&#58; Martin to add suggestion to TFS]<br><img alt="TFS Upgrade Wizard - Configure - Upgrade Process" src="/PublishingImages/15-TFS%20Upgrade%20Wizard%20-%20Configure%20-%20Upgrade%20Process.png" style="width&#58;500px;height&#58;376px;" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br><span><img alt="TFS Upgrade Wizard - Configure - Upgrade Process Success" src="/PublishingImages/16-TFS%20Upgrade%20Wizard%20-%20Configure%20-%20Upgrade%20Process%20Success.png" style="width&#58;500px;height&#58;374px;" /></span><br></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Close&quot;<br><span><img alt="TFS Upgrade Wizard - Complete" src="/PublishingImages/17-TFS%20Upgrade%20Wizard%20-%20Complete.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Close&quot;<br><span><img alt="TFS Config - Application Server Complete" src="/PublishingImages/18-TFS%20Config%20-%20Application%20Server%20Complete.png" style="width&#58;500px;height&#58;375px;" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Change the DNS entry for tfs.northwind.com to point to TFS2010 on</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> <ol><li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Internal DNS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
<li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>External DNS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li></ol>
<div><table><tbody><tr><td style="width&#58;32px;height&#58;32px;"><img alt="Red Bull Can" src="/PublishingImages/redbull.jpg" style="width&#58;32px;height&#58;32px;" /></td>
<td>Since you have to deal with your system admins, this job will take the longest. Speed it up by buying a Red Bull for your system admin</td></tr></tbody></table></div></li></ol></div>

<br><excerpt class='endintro'></excerpt><br>



