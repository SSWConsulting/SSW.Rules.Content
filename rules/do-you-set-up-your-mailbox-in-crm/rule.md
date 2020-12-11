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

If you want to track appointments and emails in Microsoft Dynamics 365 (CRM), you first need to set up your mailbox in the system.

Do the following:

<!--endintro-->

1. Browse to your Dynamics 365 Online URL | Advanced Settings | Settings | Email Configuration | Mailboxes | Browse for your mailbox:<br>   <dl class="image">&lt;dt&gt;<img src="crm-open-meilbox-settings.png" alt="crm-open-meilbox-settings.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: You should see your mailbox. Click the link on Name and it will open up your mailbox settings<br></dd></dl>
2. Make sure the following options are set (they might differ a bit depending on your CRM configuration):
    * **Allow to Use Credentials for Email Processing:** checked
    * **User Name:**
    * **Password:**
    * **cServer Profile:** Exchange Online Hybrid
    * **Incoming Mail:** Server-Side Synchronization or Email Router
    * **Outgoing Mail:** Server-Side Synchronization or Email Router
    * **Appointments, Contacts, and Tasks:** Server-Side Synchronization
3. Click  **Test & Enable Mailbox** 
If successful, you will receive an email, if not, contact your nearest SysAdmin
4. Click Save & Close!

<dl class="image">&lt;dt&gt;
      <img src="setup-mailbox-crm.png" alt="setup-mailbox-crm.png" style="width:750px;">
   &lt;/dt&gt;<dd>Figure: Setting up your mailbox in CRM<br></dd></dl>
If you need more guidance on setting it up, you can find more on Microsoft documentation: [Set incoming and outgoing email synchronization](https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/admin/set-incoming-outgoing-email-synchronization).

After this is done, you should install the Dynamics 365 App for Outlook: [https://rules.ssw.com.au/dynamics-crm-install-the-dynamics-365-app-for-outlook](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=31d6b133-8ed2-4ef4-b0b8-33bfebd85d10)
