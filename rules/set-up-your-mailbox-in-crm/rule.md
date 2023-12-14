---
type: rule
title: Do you set up your mailbox in CRM?
uri: set-up-your-mailbox-in-crm
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-set-up-your-mailbox-in-crm
created: 2020-09-17T21:24:52.000Z
archivedreason: null
guid: 7ff2d0a5-bdd4-4874-9c85-98d3f8b4cd68
---
If you want to track appointments and emails in Microsoft Dynamics 365 (CRM), you first need to set up your mailbox in the system.

Do the following:

<!--endintro-->

1. Browse to your Dynamics 365 Online URL | Advanced Settings | Settings | Email Configuration | Mailboxes | Browse for your mailbox:

![Figure: You should see your mailbox. Click the link on Name and it will open up your mailbox settings](crm-open-meilbox-settings.png)

2. Make sure the following options are set (they might differ a bit depending on your CRM configuration):

   * **Allow to Use Credentials for Email Processing:** Yes
   * **User Name:** &lt;<YourUserName@yourcompany.com>&gt;
   * **Password:** &lt;YourPassword&gt;
   * **Server Profile:** Microsoft Exchange Online
   * **Incoming Mail:** Server-Side Synchronization or Email Router
   * **Outgoing Mail:** Server-Side Synchronization or Email Router
   * **Appointments, Contacts, and Tasks:** Server-Side Synchronization
3. Click  **Test & Enable Mailbox**
   If successful, you will receive an email, if not, contact your nearest SysAdmin
4. Click Save & Close!

![Figure: Setting up your mailbox in CRM](setup-mailbox-crm.png)

If you need more guidance on setting it up, you can find more on Microsoft documentation: [Set incoming and outgoing email synchronization](https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/admin/set-incoming-outgoing-email-synchronization).

After this is done, you should [install the Dynamics 365 App for Outlook](/dynamics-crm-install-the-dynamics-365-app-for-outlook)
