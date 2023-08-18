---
type: rule
title: Do you assign tasks to individuals?
uri: send-email-tasks-to-individuals
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2022-03-15T18:31:01.031Z
guid: 4b0321a9-a4fe-4f60-a9e2-dd0b764cd1bc
related:
  - include-names-as-headings

---

Sending email tasks to a whole team or multiple team members is not a good idea because it can lead to confusion and lack of accountability. When everyone is responsible for a task, it can be easy for each person to assume that someone else will take care of it, leading to the task being ignored or forgotten.

Instead, it is recommended to assign tasks to specific individuals and make sure that each person knows what they are responsible for. This can help ensure that tasks are completed on time and that everyone is held accountable for their work.
 
As the old quote goes: _“If everyone is in charge of something, no one is!”_
            
<!--endintro-->

::: email-template
|          |     |
| -------- | --- |
| To:      | @TheDesigners |
| Subject: | Video thumbnail |  
::: email-content  

### Hi Designers,

1. Please create a video thumbnail for this week's Tech News video

:::
:::
::: bad  
Figure: Bad example - Designers don't know which of them should action the task
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Danny |
| Cc:      | @TheDesigners |
| Subject: | Video thumbnail |  
::: email-content  

### Hi Danny,

1. Please create a video thumbnail for this week's Tech News video

:::
:::
::: good  
Figure: Good example - It is clear who should do the task
:::

The exceptions are:
- If you have a ticketing system, like Zendesk, that automatically adds emails to a backlog, and you have a generic task that could be completed by anyone in the team
- If you are sending a ['test please'](/request-a-test-please) that could have a response from more than 1 person (e.g. When any of 3 designers could approve or give feedback on an artwork)
