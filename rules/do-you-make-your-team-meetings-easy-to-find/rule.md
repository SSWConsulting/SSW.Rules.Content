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
When joining a new team, it's easy to be lost and not know when the important meetings are (like the Daily Scrum, or the next Sprint Review). Broadly, use Teams as the appointment source (rather than Outlook) then the benefit is that you can have a tab where you see it in the context of the team. Then, when a new member joins a Team they do not have to go looking for the appointment, and can easily join the call.

<!--endintro-->

`youtube: MYIjVqD8AUo`
**Video: An awesome introduction to Channel Calendars in Teams**

In the past, the best way to do this was to create a SharePoint page with a Group Calendar web part, then add this as a tab in Teams. Microsoft have since released Channel calendars, which are better because they are built into Microsoft Teams.

**Note:** There is another problem where only the original creator of an appointment can edit it.

::: bad
![Figure: Bad example - When looking at my calendar, don't know when the meetings are](team-meetings-bad-example.jpg)
:::

::: ok
![Figure: OK example - A SharePoint page was the best way to achieve this in the past](team-meetings-ok-example.jpg)
:::

::: good
![Figure: Good example - A channel calendar allows me to see my Team's meetings before been invited (and invite myself if required)](teams-calendar-good.png)
:::

### To add a channel calendar

1. Go to the **Team | General channel** (or another channel, if you prefer)
2. Click the + at the top to add a tab
3. Search for "Channel calendar" and click on it
4. Give the tab a name (e.g. SysAdmins Calendar)
5. Click "Add"
6. All done, now all you need to do is setup some meetings for the channel (if you haven't already) - see rule on [how to create recurring teams meetings for a channel](/create-recurring-teams-meetings-for-a-channel)

![Figure: Adding a Channel calendar](adding-channel-calendar.png)

::: greybox
**Suggestion to Microsoft:** This is an unnecessary extra hoop to jump through. If you create an appointment from a Team, then this tab should be automatically created.
:::

### Joining and leaving a Team calendar

When you join a Team, find and add yourself to Team calendar appointments (don’t ask the owner) - 
e.g. Daily Scrums and Sprint Reviews

![Figure: Add the event to "My calendar" from within Teams](teams-add-to-calendar.png)

If you need to leave the meeting, you can change your response and decline the appointment from Teams or Outlook - however, this will keep you as an **Optional** attendee, and you will still receive updates to the appointment. To completely remove yourself, you need to:

1. Go to **Outlook | Calendars | All Group Calendars**
2. Open the relevant calendar
3. Open the appointment and select **The entire series**
4. Remove yourself from the **Optional** field and click **Send Update**

![Figure: Removing yourself from the appointment](edit-appointment.png)

:::info

If you can't see the group calendar in Outlook, you (or your SysAdmins) will need to run this PowerShell command:

```
Set-UnifiedGroup -identity {{ group name }} -HiddenFromExchangeClientsEnabled:$False
```

More info here: https://techcommunity.microsoft.com/t5/microsoft-teams/removing-a-meeting-in-a-teams-channel-when-the-organizer-is-gone/m-p/2106354

:::