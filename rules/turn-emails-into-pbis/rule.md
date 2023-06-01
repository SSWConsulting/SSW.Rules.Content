---
type: rule
archivedreason: 
title: Do you turn an email into a PBI before starting work?
guid: 98d88bcd-85a4-4b7a-8612-2affd49021d5
uri: turn-emails-into-pbis
created: 2013-06-27T18:28:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Piers Sinclair
  url: https://ssw.com.au/people/piers-sinclair
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: 
- do-you-know-the-3-steps-to-a-pbi
- when-you-use-mentions-in-a-pbi
redirects:
- do-you-turn-an-email-into-a-tfs-work-item-before-starting-work
- do-you-turn-an-email-into-an-azure-devops-work-item-before-starting-work
- turn-emails-into-work-items

---

Emails are a natural way for people to give feedback about a product. Unfortunately, they also serve as a poor mechanism for performing work. As work is done, the thread can become untennable by splitting off into multiple different threads and becoming buried amoung other emails.

That's why when a feedback email is received, it is important to turn it into a Product Backlog Item (PBI) and communicate that back to the sender.

If someone often sends email tasks rather than creating PBIs, kindly suggest they create PBIs directly to save time and keep workflows organized.

<!--endintro-->

### Benefits of turning emails into PBIs
There are several benefits of turning an email into a PBI including:

::: good
Providing one source of truth
:::

::: good
Better Prioritization
:::

::: good
Easily accessible by anyone in the team
:::

### Steps to turn an email into a PBI
It's important that you follow the right steps so that the PBI contains all the information someone would need to find the original email thread, and also so that the original sender knows where the PBI is, and whether it has completed.

1. Create a PBI in the backlog and give it a name
2. Copy the **email header** into the top of the PBI, indent it and add the words "Based on email chain:" so that the email can be found later e.g.

    ::: greybox
    Based on email chain:
      **From:** Bob Northwind [SSW] BobNorthwind@ssw.com.au 

      **Sent:** Thursday, 24 November 2022 2:52 PM

      **To:** Jane Doe [SSW] JaneDoe@ssw.com.au

      **Cc:** John Doe [SSW] JohnDoe@ssw.com.au; Eliza Northwind [SSW] ElizaNorthwind@ssw.com.au

      **Subject:** TimePro PBI 50209: ☠️ Displaying past employees
    :::

4. Fill out the description and Acceptance Criteria.
5. In the Acceptance Criteria, add "Reply 'Done' to the email and also @mention them in the PBI with 'Done'"
6. Reply back to the original email saying "That's awesome feedback, I've moved it to a PBI: {{ url }}
For future ones, if you have access, please add your comments there 🙂"

**Tip:** If the request from the client is too large for one PBI, then it will need to be turned into multiple PBIs as per the rule  [Do you keep your PBIs smaller than 2 days' effort?](/spec-do-you-create-tasks-under-4-hours) In this case, you will need to let the client know this and include URLs to each PBI.

### Keeping it up-to-date
If there is more communication in emails at a later date, it's important to make sure the PBI stays in sync with the emails. Otherwise, the source of truth will become confusing since there will be differing information in 2 places.

When there is a new update in emails do the following asap:

1. Update the PBI with any relevant information
2. Mention that it was updated as per the email thread in the discussion


::: bad
![Figure: Bad Example - Don't work from your email inbox!](EmailExample.png)
:::

::: good
![Figure: Good Example - Put it in a PBI!](PbiExample.png)
:::
