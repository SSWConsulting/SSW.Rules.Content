---
type: rule
title: Do you know how to upgrade your TFS2013 Update 4 system? (the big one)
uri: do-you-know-how-to-upgrade-your-tfs2013-update-4-system-the-big-one
created: 2015-08-13T12:32:42.0000000Z
authors: []

---



<span class='intro'> <p>Once you have prepared your environment by creating backups, testing your rollback plan, and set your Project Collections to be offline, you're ready to run the setup process that will perform the upgrade.</p><div><br></div> </span>

<p>Here we assume that you are performing an in-place upgrade. Below are the high level steps that you should follow&#58;</p><p>a.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <a href="http&#58;//www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart">Send an email</a>&#160;to let everyone know the TFS server will be offline.</p><p>b.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Ensure that your Project Collections are offline.</p><p>c.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Run the setup tool from the TFS 2015 media (or ISO).</p><p>&#160;.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Run through the wizard. It should remember most of your existing settings, so not much configuration is required.</p><p>d.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Make sure you have access to coffee while it's upgrading your Project Collections- it could take a while!<br> </p><p><br></p><p><img src="/PublishingImages/depending%20size.png" alt="depending size.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p><strong>Figure&#58; Depending on the size of your collections, the Project Collection upgrade process takes the longest out of all steps</strong></p><p>&#160;</p><p><img src="/PublishingImages/coffee2.png" alt="coffee.png" style="margin&#58;5px;" /><br></p><p><strong>Figure&#58; Wait for the Project Collection upgrade to complete</strong></p><p><strong>&#160;</strong></p><p><strong><img src="/PublishingImages/success.png" alt="success.png" style="margin&#58;5px;width&#58;650px;" /><br></strong></p><p><strong>Figure&#58; TFS Upgrade wizard success!</strong></p><p><strong>&#160;</strong></p><p>Now you're almost done! That covers the core upgrade of your TFS server, your TFS configuration database, and Project Collections.</p><p>&#160;</p><p>Next, you'll need to make sure that additional services like XAML Build Configuration and SharePoint integration are configured before testing.</p>


