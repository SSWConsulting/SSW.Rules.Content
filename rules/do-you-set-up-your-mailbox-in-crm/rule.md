---
type: rule
archivedreason: 
title: Do you set up your mailbox in CRM?
guid: 7ff2d0a5-bdd4-4874-9c85-98d3f8b4cd68
uri: do-you-set-up-your-mailbox-in-crm
created: 2020-09-17T21:24:52.0000000Z
authors:
- id: 73
  title: Kaique Biancatti
related: []

---


<p class="ssw15-rteElement-P">If you want to track appointments and emails in Microsoft Dynamics 365 (CRM), you first need to set up your mailbox in the system.<br></p><p class="ssw15-rteElement-P">​Do the following&#58;​​​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>Browse to&#160;your Dynamics 365 Online URL | Advanced Settings | Settings | Email Configuration | Mailboxes | Browse for your mailbox&#58;
   <dl class="image"><dt><img src="/PublishingImages/crm-open-meilbox-settings.png" alt="crm-open-meilbox-settings.png" style="width&#58;750px;" /></dt><dd>Figure&#58; You should see your mailbox. Click the link on Name and it will open up your mailbox settings<br></dd></dl></li><li>Make sure the following options are set (they might differ a bit depending on your CRM configuration)&#58; 
      <ul><li><b>Allow to Use Credentials for Email Processing&#58;</b> checked</li><li><b>User Name&#58;</b> &lt;YourUserName@yourcompany.com&gt;</li><li><b>Password&#58;</b> &lt;YourPassword&gt;</li><li><b>cServer Profile&#58;</b> Exchange Online Hybrid</li><li><b>Incoming Mail&#58;</b> Server-Side Synchronization or Email Router</li><li><b>Outgoing Mail&#58;</b> Server-Side Synchronization or Email Router</li><li><b>Appointments, Contacts, and Tasks&#58;</b> Server-Side Synchronization</li></ul></li><li>Click <b>Test &amp; Enable Mailbox</b><br>If successful, you will receive an email, if not, contact your nearest SysAdmin<br><br></li><li>Click Save &amp; Close!</li></ol><dl class="image"><dt>
      <img src="/PublishingImages/setup-mailbox-crm.png" alt="setup-mailbox-crm.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Setting up your mailbox in CRM<br></dd></dl><p>If you need more guidance on setting it up, you can find more on Microsoft documentantion&#58;&#160;<a href="https&#58;//docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/admin/set-incoming-outgoing-email-synchronization">Set incoming and outgoing email synchronization</a>.</p>


