---
type: rule
title: Do you assign tasks to individuals?
uri: send-email-tasks-to-individuals
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2022-03-15T18:31:01.031Z
guid: 4b0321a9-a4fe-4f60-a9e2-dd0b764cd1bc

---

It’s common to send email tasks to a whole team or multiple team members, but that is not a good idea. They may all assume that someone else will do the task, and ignore it. 
 
As the old quote goes: _“If everyone is in charge of something, no one is!”_
            
<!--endintro-->

It’s generally a better idea to direct each email/task to 1 person.

::: email-template
|          |     |
| -------- | --- |
| To:      | @SSWDesigners |
| Subject: | Video thumbnail |  
::: email-content  

### Hi Designers,

1. Please create a video thumbnail for XXX  

:::
:::
::: bad  
Figure: Bad example - Designers don't know which of them should action the task
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Danny |
| Cc:      | @SSWDesigners |
| Subject: | New logo |  
::: email-content  

### Hi Danny,

1. Please create a video thumbnail for XXX  

:::
:::
::: good  
Figure: Good example - It is clear who should do the task
:::

The exceptions are:
- If you have a ticketing system, like Zendesk, that automatically adds emails to a backlog, and you have a generic task that could be completed by anyone in the team
- If you are sending a ['test please'](/request-a-test-please) that could have a response from more than 1 person (e.g. When any of 3 designers could approve or give feedback on an artwork)
