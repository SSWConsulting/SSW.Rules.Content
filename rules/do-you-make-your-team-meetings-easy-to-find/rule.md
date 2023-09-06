---
type: rule
title: Appointments - Do you make your Teams meetings easy to find?
uri: do-you-make-your-team-meetings-easy-to-find
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair/
  - url: https://www.ssw.com.au/people/warwick-leahy/
    title: Warwick Leahy
related:
  - methodology-daily-scrums
  - do-you-know-what-happens-at-a-sprint-review-meeting
redirects:
  - appointments-do-you-make-your-team-meetings-easy-to-find
created: 2020-04-02T06:07:17.000Z
archivedreason: null
guid: b4c925ae-3d9b-48fd-868c-11ca49155a50
---

When a developer joins a team, they need to find the important meetings like the Daily Scrum and the Sprint Review. Unfortunately, these meetings are often organized by a team member and there is no way to find them.

Ideally, a new team member would jump into Microsoft Teams and find the team they are joining. Then they would see all the important meetings from within the team and join them as needed.

From then on, they would be able to see those appointments in Microsoft Outlook and edit them as needed.

In the past, the best way to do this was to create a SharePoint page with a Group Calendar web part, then add this as a tab in Teams. 

Microsoft have since released Channel Calendars, which are better because they are built into Microsoft Teams.

<!--endintro-->

::: bad
![Figure: Bad Example - A team member searching for the Daily Scrum cannot find it if it is scheduled like a normal meeting](teams-meetings-bad-example.png)
:::

::: ok
![Figure: OK Example - In the past, a SharePoint page was the best way to make meetings visible to the team](team-meetings-ok-example.jpg)
:::

::: good
![Figure: Good Example - A Channel Calendar allows team members to see the Team's meetings before being invited](teams-calendar-good.png)
:::

`youtube: MYIjVqD8AUo`
**Video: An awesome introduction to Channel Calendars in Teams**

## Setup - Make the calendar visible to the team
Before anyone can view and edit the appointment, it needs to be setup correctly to allow editing.

There are 2 steps:
1. Add a Channel Calendar
2. Make the Channel Calendar visible in Microsoft Outlook

### Add a Channel Calendar

1. Go to the **Team | General channel** (or another channel, if you prefer)
2. Click the + at the top to add a tab
3. Search for "Channel Calendar" and click on it
4. Give the tab a name (e.g. SysAdmins Calendar)
5. Click "Add"
6. All done, now the team can see all meetings relating to the team

![Figure: Adding a Channel Calendar](adding-channel-calendar.png)

::: greybox
**Suggestion to Microsoft:** This is an unnecessary extra hoop to jump through. If you create an appointment from a Team, then this tab should be automatically created.
:::

### Make the Channel Calendar visible in Microsoft Outlook

Channel Calendar meetings need to be editable by anyone in the Team and the only way to enable that is via a group calendar in Microsoft Outlook.

By default, group calendars do not show up in Microsoft Outlook, so they need to be made visible to the team with a PowerShell command:

::: greybox

```
Set-UnifiedGroup -identity {{ group name }} -HiddenFromExchangeClientsEnabled:$False
```

More info here: https://techcommunity.microsoft.com/t5/microsoft-teams/removing-a-meeting-in-a-teams-channel-when-the-organizer-is-gone/m-p/2106354

:::

![Figure: Group calendars allow meetings to be edited](team-calendar.png)

## Management - Team members create, join, edit and leave meetings themselves

Now that the team calendars are properly configured, it is easy to create, join, edit or leave a meeting 

### Creating a meeting

Creating a meeting should always be done from Microsoft Teams because Microsoft Outlook doesn't support setting the channel.

To create a meeting:

1. Follow the rule on [how to create recurring teams meetings for a channel](/create-recurring-teams-meetings-for-a-channel)

### Joining a meeting

To join a meeting do the following:

1. Navigate to **Microsoft Teams | Team | Channel Calendar**
2. Click on the meeting you want to join and expand it
3. Select "Add to calendar" 
4. Done! You are now one of the meeting attendees.

![Figure: Add the event to "My calendar" from within Teams](teams-add-to-calendar.png)

### Editing a meeting

To update a meeting, you can change the details in Microsoft Outlook:

1. Go to **Microsoft Outlook | Calendars | All Group Calendars**
2. Open the relevant calendar (same as team name)
3. Open the appointment and select **The entire series**
4. Make changes as needed

![Figure: It's easy to edit the SugarLearning Daily Scrum using the Microsoft Outlook group calendar](EditSugarLearningDailyScrum.png)

### Leaving a meeting

Many people decline a meeting when they no longer want to attend. However, this method is problematic because you will still be an **Optional** attendee, and receive updates to the appointment.

To leave a meeting properly:

1. Edit the meeting and remove yourself as a participant
2. Double check that no other mailboxes have been added which include you e.g. the Team mailbox

::: bad
![Figure: Bad Example - Hitting decline only removes you from the meeting temporarily](declining-appointment.png)
::: 

::: good
![Figure: Good Example - Removing yourself from the meeting via an update](edit-appointment.png)
:::
