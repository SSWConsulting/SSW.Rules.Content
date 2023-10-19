---
type: rule
archivedreason: 
title: GitHub Issues - Do you turn emails into Issues before starting work?
guid: f866b251-c988-4e30-acc4-f6bac793c1d7
uri: turn-emails-into-a-github-issue
created: 2020-10-27T03:57:22.0000000Z
authors:
- title: Prem Radhakrishnan
  url: https://ssw.com.au/people/prem-radhakrishnan
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related:
- do-you-know-the-3-steps-to-a-pbi
- when-you-use-mentions-in-a-pbi
- turn-emails-into-pbis
redirects:
- do-you-turn-an-email-into-a-github-issue-before-starting-work

---

If a Product Owner sends an email to the development team with a request, that [email should be turned into a Github Issue](/turn-emails-into-pbis) before any work is started or the work is prioritized on the backlog. 

Power Automate has a connector to do this automatically when an email arrives in Outlook. It can create a new Github Issue by parsing the From, To, Subject and body of the email. 

However, at the moment there is a limitation that it doesn't read inline attachments in emails and therefore you have to create your issues manually in Github.

<!--endintro-->

![Figure: Power Automate | Connectors | Github](email-to-github-issue2.png)  

![Figure: Configure Flow connectors to create a new Github Issue from Outlook](email-to-github-issue1.png)  

🔥 Warning: This Flow connector does not suport inline images.

::: good  
![Figure: Good Example - Github issue created from Outlook using Flow connectors](email-to-github-issue3.png)  
:::

::: bad  
![Figure: Bad Example - Github issue created using Flow - inline attachment shows up as junk characters](email-to-github-issue.png)  
:::
