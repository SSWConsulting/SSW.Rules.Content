---
type: rule
title: Do you choose which Microsoft 365 groups you follow?
uri: following-microsoft-365-groups
authors:
  - title: Chris Schultz
    url: https://www.ssw.com.au/people/chris-schultz
created: 2023-06-18T23:52:23.432Z
guid: 60be42f8-bece-450e-89a2-14114b8e0cb1
---

Microsoft 365 groups add a lot of extra functionality to groups. The main things are a calendar and a Team for conversations and file storage (optional) - but they also have additional settings.

Email can be noisy - we all want to reduce the number of emails we receive. One really useful setting in Microsoft 365 groups is the option to unfollow groups. Here are some use cases:

<!--endintro-->

1. You have a group that receives a lot of emails that do not need to be actioned, but may need to be found at a later date. You can happily unfollow this group, remove the noise from your inbox, and check the group folder later if needed.

2. You have a team where one person is the main point of contact - but others need to help out occasionally. For example, if you own a lot of domains, you will receive many emails about their renewals. It is good practice to have one person managing this - but it is also good practice to have the emails going to a group (not just an individual). Other members of the team can unfollow the group, and only check the folder if the responsible person is unavailable.

## Follow/unfollow settings

### As a user:

To follow or unfollow a group in Outlook:

1. Go to the group in the navigation pane
2. Go to **Group Settings** in the ribbon
3. Choose which items you would like to receive in your inbox

![Figure: Outlook | Group Settings | Follow in Inbox](group-follow.png)

:::info
Note: This functionality is not available on Outlook for Mac. If you want to change these settings, use the [OWA](https://outlook.office.com/mail)
:::

### As an administrator (Microsoft 365 admin center)

When you set up a new Microsoft 365 group, you can choose the default behaviour for members of the group.

1. Go to **Microsoft 365 admin center | Teams & groups | Active teams & groups** and click on the group
2. Go to **Settings**
3. Check or uncheck **Send copies of team emails and events to the team members' inboxes**

![Figure: Microsoft 365 admin center | Teams & groups | Settings](group-admin.png)

:::info
Note: this will not change the behaviour for existing members - for this, you will need to use PowerShell.
:::

### As an administrator (PowerShell)

For more granular options, you can use PowerShell - you can view and edit settings for individual members of the group.

```powershell
# Connect to Exchange Online
Connect-ExchangeOnline

# View the group follow settings
Get-UnifiedGroup -Identity {{ group }} | fl Identity, DisplayName, AutoSubscribeNewMembers

# Enable or disable the above
Set-UnifiedGroup -Identity {{ group }} -AutoSubscribeNewMembers
Set-UnifiedGroup -Identity {{ group }} -AutoSubscribeNewMembers:$false

# Get a list or group members
Get-UnifiedGroupLinks -Identity {{ group }} -LinkType Members

# Check who is following the group
Get-UnifiedGroupLinks -Identity {{ group }} -LinkType Subscribers

# Add or remove people from following the group
Add-UnifiedGroupLinks -Identity {{ group }} -LinkType Subscribers -Links {{ User }}
Remove-UnifiedGroupLinks -Identity {{ group }} -LinkType Subscribers -Links {{ User }}
```
