---
type: rule
archivedreason: 
title: Do you know how to setup your Outlook to send but not receive?
guid: ddd15c6d-c09f-4acb-94c1-2496508f0af3
uri: do-you-know-how-to-setup-your-outlook-to-send-but-not-receive
created: 2011-04-13T06:18:47.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
- id: 1
  title: Adam Cogan
related: []

---


When using your presentation computer you may want to still be able to send emails but not want to download your entire Exchange mailbox to your Boot2VHD image. This is&#160;especially relevant for people with large mailboxes. 

<br><excerpt class='endintro'></excerpt><br>

  <ol>
    <li>Open Outlook 2010&#160;and create a new Exchange account <br>
<img src="/ITAndNetworking/RulesToBetterPresentationPCs/PublishingImages/new-account.jpg" alt="Create New Account" /><br></li>
    <font size="-0" class="ms-rteCustom-FigureNormal">Figure - Tick manually configure server settings</font>
    <li>Enter your server name and user name, but un-tick <strong>Use Cached Exchange Mode<br>
    <img width="595" height="413" src="/ITAndNetworking/RulesToBetterPresentationPCs/PublishingImages/fig3-untickcached.png" alt="Un-tick Use Cached Exchange Mode" /><br>
    </strong><font size="-0" class="ms-rteCustom-FigureNormal">Figure - Un-tick Use Cached Exchange Mode</font> </li>
    <li>Finish the setup and then open Outlook </li>
    <li>Configure your Send / Receive Groups&#58;<br>
    <img src="/ITAndNetworking/RulesToBetterPresentationPCs/PublishingImages/fig4-editaccounts.png" alt="Click Send / Receive | Click Send / Receive Groups | Click Define Send / Receive Groups" /> <font size="-0" class="ms-rteCustom-FigureNormal">Figure - Click Send /&#160;Receive | Click Send /&#160;Receive Groups | Click Define Send /&#160;Receive Groups</font> </li>
    <li>Now we can choose the parts of our mailbox we want to synced to our PC. The following options are recommened&#58;<br>
    <br>
    Untick <strong>Receive Mail Items<br>
    </strong>Tick <strong>Download offline address book<br>
    </strong>Tick the <strong>Outbox</strong> folder<br>
    Tick the <strong>Contacts</strong> folder<br>
    Tick the <strong>Sent Items </strong>folder, and select <strong>Download headers only</strong><br>
    <br>
    <img src="/ITAndNetworking/RulesToBetterPresentationPCs/PublishingImages/fig5-sendreciveall.png" alt="" /><br>
    <font size="-0" class="ms-rteCustom-FigureNormal">Figure - Untick &quot;Receive mail items&quot; | Tick &quot;Sent Items&quot;, &quot;Contacts&quot; and &quot;Outbox&quot; | Download only headers for &quot;Sent Items&quot;</font>&#160; </li>
    <li>When back in the main Outlook window click <strong>Send / Receive All</strong> <strong>Folders </strong>and this will sync your sent items and contacts which will now be available offline </li>
</ol>
<p><strong>Suggestion to the Microsoft Outlook Team&#58;</strong></p>
<ul>
    <li>Give us a “Sync last x weeks” for each folder</li>
    <li>Give us a ‘Work in Minimal Mode’ – that does the above</li>
</ul>



