---
type: rule
title: Do you know how to setup your Outlook to send but not receive?
uri: do-you-know-how-to-setup-your-outlook-to-send-but-not-receive
created: 2011-04-13T06:18:47.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins
- id: 1
  title: Adam Cogan

---



<span class='intro'> When using your presentation computer you may want to still be able to send emails but not want to download your entire Exchange mailbox to your Boot2VHD image. This is&#160;especially relevant for people with large mailboxes. 
 </span>

<p>Here is how you do it&#58;</p><ol><li>Open Outlook and create a new Exchange account&#58; 
      <br> 
      <dl class="image"><dt> 
            <img src="mail1.png" alt="Create New Account" style="width&#58;400px;height&#58;449px;" /> 
         </dt><dd>Figure - Tick manually configure server settings</dd></dl></li><li>​Enter your server name and user name, but un-tick 
      <strong>Use Cached Exchange Mode</strong>&#58; ​ 
      <dl class="image"><dt> 
            <img src="Mail3.png" alt="Un-tick Use Cached Exchange Mode" style="width&#58;400px;height&#58;449px;" /> 
         </dt><dd>Figure - Un-tick Use Cached Exchange Mode</dd></dl></li><li>Finish the setup and then open Outlook </li><li>Configure your Send / Receive Groups&#58; 
      <dl class="image"><dt> 
            <img src="Email2.png" alt="Click Send / Receive | Click Send / Receive Groups | Click Define Send / Receive Groups" style="width&#58;400px;height&#58;398px;" /> 
         </dt><dd>Figure - Click Send /&#160;Receive | Click Send /&#160;Receive Groups | Click Define Send /&#160;Receive Groups</dd></dl></li><li>Now we can choose the parts of our mailbox we want to synced to our PC. The following options are recommended&#58; 
      <ul><li>Untick 
            <strong>Receive Mail Items</strong></li><li>Tick 
            <strong>Download offline address book</strong></li><li>Tick the 
            <strong>Outbox</strong> folder</li><li>Tick the 
            <strong>Contacts</strong> folder</li><li>Tick the 
            <strong>Sent Items </strong>folder,</li><li>and select 
            <strong>Download headers only</strong></li></ul><dl class="image"><dt>
            <img src="Email.png" alt="" style="width&#58;600px;height&#58;635px;" />
         </dt><dd>Figure - Untick &quot;Receive mail items&quot; | Tick &quot;Sent Items&quot;, &quot;Contacts&quot; and &quot;Outbox&quot; | Download only headers for &quot;Sent Items&quot;</dd></dl></li><li>When back in the main Outlook window click 
      <strong>Send / Receive </strong><strong>All</strong><strong>Folders </strong>and this will sync your sent items and contacts which will now be available offline </li></ol><p>
   <strong>Suggestion to the Microsoft Outlook Team&#58;</strong></p><ul><li>​Give us a &quot;Sync last x weeks&quot; for each folder</li><li>Give us a &quot;Work in Minimal Mode&quot;​ that does the above</li></ul>


