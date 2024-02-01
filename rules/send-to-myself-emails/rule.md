---
type: rule
title: Dones - Do you send yourself emails?
uri: send-to-myself-emails
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - do-you-send-as-per-our-conversation-emails
  - do-you-include-the-name-of-the-person-you-address-on-the-first-line
redirects:
  - dones-do-you-send-yourself-emails
created: 2009-03-26T02:29:14.000Z
archivedreason: null
guid: 603ce646-dca9-443f-91a4-ba09d3cbec3b
---

When a client or coworker **verbally** asks you to do a task... How to make sure you will remember it?

<!--endintro-->

The best solution is to **send yourself an email**, Cc'ing the person who asked you, and including "[As per our conversation](/do-you-send-as-per-our-conversation-emails)..." This way both of you know that the job needs to be done. This is really important especially when you are working for clients so there is a documented record of the requests for work.

Another scenario is when you found something you should work on, but don't have time to do it immediately... you should also send a "To myself" email, Cc'ing someone who is also interested in that task (e.g. The Product Owner).

::: info
**Note:** If the request is relevant to client work or an existing Product Backlog then it would be better to create or update a PBI and @mention the Product Owner and relevant people as per [using @ mentions in PBI](/when-you-use-mentions-in-a-pbi).
:::

::: bad
![Figure: Bad example - Writing yourself a "Post-It Note" is not the best method](postit-screen.jpg)
:::

::: greybox
**Tips:**

* Make it clearer to everyone else [by making "To myself" a heading or bold](/include-names-as-headings)  
  Always add "To myself" in the email body - not on the subject - so that other people Cc'd know what is going on
* When replying "Done", address it to the Product Owner (or another person), not to yourself... Only crazy people talk to themselves :-)
* Include an estimate and priority too...so the expectations are set better. With this estimate, the Product Owner can stop you if they think the amount of time doesn't provide good ROI
* If there are other people addressed in the email, put the "To myself" at the top so the tasks aren't buried at the bottom of the email.
  
:::

::: email-template
|          |     |
| -------- | --- |
| From:    | John |
| To:      | John |
| Cc:      | Adam, Uly, Dave |
| Subject: | Add a bad example to Rules to Better UI - Progress bar |
::: email-content  

### To myself,

As per my conversation with Lei, the rule on progress bars {{link}} is missing a bad example

1. Include a bad example to Rules to Better UI - progress bar  

It's estimated to take **2 hours** and I'll make it my #1 priority on the next Sprint, starting tomorrow

:::
:::
::: good
Figure: Good example - Send yourself an email with estimate and prioritization
:::

::: email-template
|          |     |
| -------- | --- |
| From:    | John |
| To:      | Dave |
| Cc:      | Adam, Uly |
| Subject: | RE: Add a bad example to Rules to Better UI - Progress bar |
::: email-content  

### Hi Lei,

\> 1. Include a bad example to Rules to Better UI - progress bar

Done - This change has been made and can be found at {{ URL }}

:::
:::
::: good
Figure: Good example - Replying to a 'To myself' email showing done evidence and correctly replying to the person who requested the task
:::
