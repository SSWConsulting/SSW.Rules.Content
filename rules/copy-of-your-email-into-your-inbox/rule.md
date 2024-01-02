---
type: rule
title: Microsoft 365 groups – Do you receive a copy of your own email into your inbox?
uri: do-you-receive-copy-of-your-email-into-your-inbox
authors:
  - title: Ash Anil
    url: https://www.ssw.com.au/people/ash
  - title: Kaique Biancatti
    url: https://www.ssw.com.au/people/kiki
created: 2023-04-12T06:50:43.070Z
guid: 28c7cfda-f78b-45fe-a60f-bd0e523e89bd
---
Microsoft 365 groups - When anyone sends an email to a Microsoft 365 group (Office365 groups) e.g: SysAdmins@Northwind.com they don’t receive a copy of their own email, which is different from normal distribution groups.

<https://support.microsoft.com/en-us/office/learn-about-microsoft-365-groups-b565caa1-5c40-40ef-9915-60fdb2d97fa2>

<!--endintro-->

To change the behavior the user can use the checkbox Outlook | Settings | Additional Settings | Groups | ‘Send me a copy of the email I send to a group’. 

<https://support.microsoft.com/en-us/office/i-m-not-receiving-a-copy-of-messages-i-send-to-a-group-in-my-inbox-07567cda-f5ce-4e52-b278-4c63dfdd6617>

![Figure: Outlook web – Enable group settings ](outlook-web-enable-group-settings.jpg)

Note: This can be enabled on the server side by doing a PowerShell script. This feature is turned on by default. Users can turn it off manually using the above steps to not receive a copy of a email sent to a Microsoft 365 group.

```powershell
# Connect to Exchange Online
Connect-ExchangeOnline -UserPrincipalName user@northwind.com

# Get the mailbox message configuration for a specific mailbox
Get-Mailbox user@northwind.com | Get-MailboxMessageConfiguration | Select EchoGroupMessageBackToSubscribedSender

# Enable the option to send a copy of the sent message to the sender's mailbox
$mailbox = Get-Mailbox -Identity "user@northwind.com" | Set-MailboxMessageConfiguration -EchoGroupMessageBackToSubscribedSender $true
```
