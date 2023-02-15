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
related: []
redirects:
  - appointments-do-you-make-your-team-meetings-easy-to-find
created: 2020-04-02T06:07:17.000Z
archivedreason: null
guid: b4c925ae-3d9b-48fd-868c-11ca49155a50
---
When joining a new team, it's easy to be lost and not know when the important meetings are (like the Daily Scrum, or the next Sprint Review). Broadly, use Teams as the appointment source (rather than Outlook) then the benefit is that you can have a tab where you see it in the context of the team. Then, when a new member joins a Team they do not have to go looking for the appointment, and can easily join the call.

<!--endintro-->

In the past, the best way to do this was to create a SharePoint page with a Group Calendar web part, then add this as a tab in Teams. Microsoft have since released Channel calendars, which are easier to add and nicer to use.

:::bad

![Figure: Bad Example - When I look at my calendar, I don't know when the meetings are](team-meetings-bad-example.jpg)

:::

:::ok

![Figure: OK example - A SharePoint page was the best way to achieve this in the past](team-meetings-ok-example.jpg)

:::

:::good

![Figure: Good Example - A channel calendar allows me to see my Team's meetings before I have been invited (and invite myself if required)](teams-calendar-good.png)

:::

### To add a channel calendar

1. Go to the **Team | General channel** (or another channel, if you prefer)
2. Click the + at the top to add a tab
3. Search for "Channel calendar" and click on it
4. Give the tab a name, e.g. SysAdmins Calendar
5. Click Add
6. All done, now all you need to do is setup some meetings for the channel (if you haven't already) - see rule: **[Do you know how to create recurring teams meetings for a channel?](https://www.ssw.com.au/rules/create-recurring-teams-meetings-for-a-channel)**

![Figure: Adding a Channel calendar](adding-channel-calendar.png)

**Suggestion to Microsoft:** This is an unnecessary extra hoop to jump through. If you create an appointment from a Team, then this tab should be automatically created.

![Figure: As a bonus, I can add the event to my calendar from within Teams](teams-add-to-calendar.png)