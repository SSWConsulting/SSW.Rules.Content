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



  <div>Since <a shape="rect" href="/TFS/RulesToBetterTFS2010Migration/Pages/MigrationChoices.aspx">we recommend doing a &quot;move based upgrade&quot;</a>, we don’t like the &quot;in place upgrade&quot; option, these are the steps&#58;</div>
<div>
<ol>
    <li>Copy the TFS2008 backups to TFS2010 server (e.g. C&#58;\TfsBackups) </li>
    <li>Restore all the databases to TFS2010’s instance of SQL 2008 </li>
    <li>Install Team Foundation Server 2010 </li>
    <li>After the install has completed the Team Foundation Server Configuration Wizard will open </li>
    <li>Select Upgrade | Start Wizard<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Config - Upgrade" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/01-TFS%20Config%20-%20Upgrade.png" /></span> </li>
    <li><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/02-TFS%20Upgrade%20Wizard%20-%20Upgrade.png" /></span></span> </li>
    <li><span><span>Click &quot;List Available Databases&quot;</span></span> </li>
    <li><span><span>Select the TfsIntegration database</span></span> </li>
    <li><span><span>Check &quot;By checking this box, I confirm that I have a current backup&quot;</span></span> </li>
    <li><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/03-TFS%20Upgrade%20Wizard%20-%20Databases.png" /></span></span></span> </li>
    <li><span><span><span>Select &quot;NT AUTHORITY\NETWORK SERVICE&quot; for the System account</span></span></span> </li>
    <li><span><span><span>Click &quot;Next&quot;&#160;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Account" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/04-TFS%20Upgrade%20Wizard%20-%20Account.png" /></span></span></span></span> </li>
    <li><span><a shape="rect" name="StartMigration"></a>Click &quot;Next&quot;<br>
    <img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Application Tier" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/05-TFS%20Upgrade%20Wizard%20-%20Application%20Tier.png" /></span> </li>
    <li><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Reporting" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/06-TFS%20Upgrade%20Wizard%20-%20Reporting.png" /></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Reporting - Reporting Services" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/07-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Reporting%20Services.png" /></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Reporting - Analysis Services" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/08-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Analysis%20Services.png" /></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span>Specify the TFSService account</span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Reporting - Report Reader Account" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/09-TFS%20Upgrade%20Wizard%20-%20Reporting%20-%20Report%20Reader%20Account.png" /></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Sharepoint" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/10-TFS%20Upgrade%20Wizard%20-%20Sharepoint.png" /></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Sharepoint - Settings" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/11-TFS%20Upgrade%20Wizard%20-%20Sharepoint%20-%20Settings.png" /></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Project Collection" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/12-TFS%20Upgrade%20Wizard%20-%20Project%20Collection.png" /></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Review" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/13-TFS%20Upgrade%20Wizard%20-%20Review.png" /></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Configure&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Readiness Checks" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/14-TFS%20Upgrade%20Wizard%20-%20Readiness%20Checks.png" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Have coffee (2 hours)<br>
    <span><img style="width&#58;200px;height&#58;170px;" alt="Coffee" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/coffee-cup.jpg" /></span><br>
    BTW&#58; A good user interface should have a coffee image <br>
    [TODO&#58; Martin to create new rule in &quot;Rules to better UI&quot;]<br>
    [TODO&#58; Martin to add sugestion to TFS]<br>
    <img style="width&#58;500px;height&#58;376px;" alt="TFS Upgrade Wizard - Configure - Upgrade Process" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/15-TFS%20Upgrade%20Wizard%20-%20Configure%20-%20Upgrade%20Process.png" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Next&quot;<br>
    <span><img style="width&#58;500px;height&#58;374px;" alt="TFS Upgrade Wizard - Configure - Upgrade Process Success" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/16-TFS%20Upgrade%20Wizard%20-%20Configure%20-%20Upgrade%20Process%20Success.png" /></span><br>
    </span></span></span></span></span></span></span></span></span></span></span></span></span></span></li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Close&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Upgrade Wizard - Complete" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/17-TFS%20Upgrade%20Wizard%20-%20Complete.png" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Click &quot;Close&quot;<br>
    <span><img style="width&#58;500px;height&#58;375px;" alt="TFS Config - Application Server Complete" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/18-TFS%20Config%20-%20Application%20Server%20Complete.png" /></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Change the DNS entry for tfs.northwind.com to point to TFS2010 on</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
    <ol>
        <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Internal DNS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
        <li><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>External DNS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li>
    </ol>
    <div>
    <table>
        <tbody>
            <tr>
                <td style="width&#58;32px;height&#58;32px;"><img style="width&#58;32px;height&#58;32px;" alt="Red Bull Can" src="/TFS/RulesToBetterTFS2010Migration/PublishingImages/redbull.jpg" /></td>
                <td>Since you have to deal with your system admins, this job will take the longest. Speed it up by buying a Red Bull for your system admin</td>
            </tr>
        </tbody>
    </table>
    </div>
    </li>
</ol>
</div>

<br><excerpt class='endintro'></excerpt><br>



