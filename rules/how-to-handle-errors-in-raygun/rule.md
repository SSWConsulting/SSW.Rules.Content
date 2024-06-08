---
type: rule
archivedreason: 
title: Do you know how to handle errors in Raygun?
guid: ffd7161f-7cac-435d-ae26-8ec42651b59b
uri: how-to-handle-errors-in-raygun
created: 2016-12-30T03:34:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-how-to-handle-errors-in-raygun

---

Your team should always be ensuring that the health of the application is continually improving.

The best way to do that is to check the exceptions that are being logged in the production application. Every morning, fix the most serious bug logged over the last week. After it is fixed then email yesterday's application health to the Product Owner.

<!--endintro-->

There's traditional error logging software like Log4Net or Elmah, but they just give you a wall of errors that are duplicated and don't give you the ability to mark anything as complete. You'll need to manually clear out the errors and move them into your task tracking system (Azure DevOps/VisualStudio.com).

This is where RayGun or Application Insights comes into the picture. RayGun gives you the following features:

* Grouping exceptions
* Ignoring/filtering exceptions
* Triaging exceptions (mark them as resolved)
* Integrations to TFS/VisualStudio.com to create a Bug, Slack
* Tracking the exceptions to a deployment
* See which errors are occurring the most often

::: bad  
![Figure: Bad example - Elmah gives you a wall of exceptions and no way to flag exceptions as completed](elmah.gif)  
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | Adam |
| Subject: | Raygun Health Check for TimePro |  
::: email-content  

### Hi Adam  

Please find below the Raygun Health Check for TimePro:

![Figure: Raygun health check for TimePro in the past 7 days  ](Raygun-health-check-for-TimePro-in-the-past-7-days.jpg)

![Figure: Resolved issues in the past 7 days](2.png)

![Figure: The next issue to be worked on](3.jpg)

&lt; This email is as per [https://ssw.com.au/rules/how-to-handle-errors-in-raygun](/how-to-handle-errors-in-raygun) &gt;

:::  
:::  
::: good
Figure: Good example - Email with Raygun application health report
:::
