---
type: rule
archivedreason: 
title: Do you know how to upgrade your TFS2013 Update 4 system? (the big one)
guid: 90fbc9d1-95de-4882-8f39-b56a2119dad0
uri: do-you-know-how-to-upgrade-your-tfs2013-update-4-system-the-big-one
created: 2015-08-13T12:32:42.0000000Z
authors: []
related: []
redirects:
- do-you-know-how-to-upgrade-your-tfs2013-update-4-system-(the-big-one)

---


<p>Once you have prepared your environment by creating backups, testing your rollback plan, and set your Project Collections to be offline, you're ready to run the setup process that will perform the upgrade.</p><div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>Here we assume that you are performing an in-place upgrade. Below are the high level steps that you should follow:</p><p>a.               <a href="http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart">Send an email</a> to let everyone know the TFS server will be offline.</p><p>b.              Ensure that your Project Collections are offline.</p><p>c.               Run the setup tool from the TFS 2015 media (or ISO).</p><p> .                Run through the wizard. It should remember most of your existing settings, so not much configuration is required.</p><p>d.              Make sure you have access to coffee while it's upgrading your Project Collections- it could take a while!<br> </p><p><br></p><p><img src="depending size.png" alt="depending size.png" style="margin:5px;width:650px;" /><br></p><p><strong>Figure: Depending on the size of your collections, the Project Collection upgrade process takes the longest out of all steps</strong></p><p> </p><p><img src="coffee2.png" alt="coffee.png" style="margin:5px;" /><br></p><p><strong>Figure: Wait for the Project Collection upgrade to complete</strong></p><p><strong> </strong></p><p><strong><img src="success.png" alt="success.png" style="margin:5px;width:650px;" /><br></strong></p><p><strong>Figure: TFS Upgrade wizard success!</strong></p><p><strong> </strong></p><p>Now you're almost done! That covers the core upgrade of your TFS server, your TFS configuration database, and Project Collections.</p><p> </p><p>Next, you'll need to make sure that additional services like XAML Build Configuration and SharePoint integration are configured before testing.</p>


