---
type: rule
archivedreason: 
title: Appointments - Do you make your team meetings easy to find?
guid: b4c925ae-3d9b-48fd-868c-11ca49155a50
uri: do-you-make-your-team-meetings-easy-to-find
created: 2020-04-02T06:07:17.0000000Z
authors:
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- appointments-do-you-make-your-team-meetings-easy-to-find

---

When joining a new team, it's easy to be lost and not know when the important meetings are (like the Daily Scrum, or the next Sprint Review). Broadly we use Teams as the appointment source (rather than Outlook) but you see it in both. This is because when a new member joins a Team e.g. Piers, he should not have to go looking for the appointment, so he can easily join the call.

<!--endintro-->


::: bad  
![Figure: Bad Example - When I look at my calendar, I don't know when the meetings are](team meetings - bad example.jpg)  
:::


::: good  
![Figure: Good Example - A SharePoint page allows me to see my Team's meetings before I have been invited (and invite myself if required)](team meetings - good example.jpg)  
:::

1. Open up the Team's SharePoint site (you can find this easily by going to the 
      *Files* tab and clicking 
      *Open in SharePoint*)
2. Go to the SharePoint site's Home page (from the menu on the left)
3. Add a new page
4. Add a Group Calendar web part to the page
5. Publish the page

![Figure: Some easy to follow steps to create the SharePoint page](team meeting - create calendar page.gif)  

6. In Teams, click add a new SharePoint tab to the Team
7. Select the newly published SharePoint page
8. Click Save

![Figure: Adding a tab to a Team is an indispensable skill](team meeting - add sharepoint tab.gif)  

9. All done, now all you need to do is setup some meetings for the channel (see rule: [Do you know how to create recurring teams meetings for a channel?](https://www.ssw.com.au/rules/create-recurring-teams-meetings-for-a-channel))! 😀

**Suggestion to Microsoft:** [This is an unnecessary extra hoop to jump through. If you create an appointment from a Team then this tab should be automatically created.](https://microsoftteams.uservoice.com/forums/555103-public/suggestions/36007027-add-a-team-calendar-to-teams-or-allow-a-project-te)

![Figure: As a bonus, I can the event to my calendar](team meetings - add yourself.jpg)  


**Warning:** Only the organizer of a meeting can make changes to it and Teams offers no ability to transfer ownership of that meeting.
To be fair you also can’t change meeting owners in Exchange.

Vote for this UserVoice item (that describes that the Teams team is working on delegation for Teams meetings but no ETA).
https://microsoftteams.uservoice.com/forums/555103-public/suggestions/34050022-ms-teams-meeting-delegation
