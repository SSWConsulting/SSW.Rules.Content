---
type: rule
title: Office365 - Do you avoid using 'Share' functionality with tasks/questions?
uri: avoid-using-share-functionality
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2023-12-01T15:34:47.574Z
guid: 02a35dc4-5c79-47b9-a561-8f4d2fe81363
---
Sharing a file is easy when looking at a file. However the email people get from it will have a notification-looking, which may result in it being overlooked/ignored.

Because of that, you should avoid using that funcionality if you want people to notice and read your email. A normal email with the link and instructions should be sent instead.

<!--endintro-->

::: bad
![Figure: Bad example - Sending an email with a file using the 'Share' funcionality](share-screenshot.jpg "Figure: Sending an email with a file using the Office365 'Share' funcionality")
:::

::: bad
![Figure: Bad example - The email sent has a notification-look meaning it may be ignored](share-email-screenshot.png "Figure: The email sent has a notification-look meaning it may be ignored")
:::

::: email-template  
|          |     |
| -------- | --- |
| From:      | Adam |
| To:      | Gordon |
| Subject: | "Invoices in June&July 2019" - Do we need this?  |  
::: email-content  

### Hi Gordon  

See this file: {{ URL }}

1. Do you need this anymore?
2. If not zz it

-a

:::  
:::  
::: good  
Figure: Good example - Link and tasks sent in a regular email  
:::

::: info
**Note:** It is a good idea to review SharePoint and Teams stats and tell users **not** to use this funcionality by pointing them to this rule.
:::
