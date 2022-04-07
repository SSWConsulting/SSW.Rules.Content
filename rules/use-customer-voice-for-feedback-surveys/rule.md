---
type: rule
title: Do you use Customer Voice for feedback surveys?
uri: use-customer-voice-for-feedback-surveys
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2022-04-04T21:31:22.712Z
guid: b52ce649-7dd7-4fab-93d1-650e22bde0a6
---
You're doing some great work for your client... or you think you are, but how do you know for sure how happy they are?

Customer feedback is something that most companies do not harness, and is key data that you should be looking at. It is as important as your profit and loss.

A focus on customer feedback will give your customers’ experience more of a weighting in your decision making.

Main options available for this are:

* MailChimp
* Salesforce Surveys and Feedback Management
* Dynamics Customer Voice **(recommended if you're already using Dynamics)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/sbMReFrVYbs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!--endintro-->

Dynamics 365 has Customer Voice Surveys to harness this, and it is included with many D365 products (e.g. Sales module). 

It can also be added as a standalone product if you don’t already have it.

::: bad
![Figure: Bad Example - Email a client could receive](survey-email.png)
:::

::: good
![Figure: Good Example - Email a client could receive](good-survey-email.png)
:::

![Figure: Example survey if they click through](survey.png)

### Creating the Survey

It’s built on the Microsoft Forms engine, so creating feedback surveys is very simple and intuitive.

![Figure: Survey Creation](survey-edit-form.png "Figure: Survey Creation")

If you are running Scrum projects, and your clients are used to doing Sprint Retrospectives, it makes sense to frame the questions in the same way (what went well, what didn’t, and what should we change?).

### Sending the Survey

Surveys can be sent manually, but for consistent value, you should have automated triggers in place. This could be after any significant milestone, and it’s best if it’s something easily automated: e.g.

* After a Spec Review (i.e. when you mark an Opportunity as won or lost)
* At billing milestones (e.g. $50k if your usual project sizes are > $100k... i.e. after 2 Sprints)
* At project completion (manually triggered from Dynamics | Account | Project page in the ribbon)

Note: Avoid sending these at high pressure points, when you're already asking them for a decision, e.g. too early in the sales process. 

![Figure: Set up triggers to send out the surveys](workflow.png)

### Receiving Responses

The survey responses are viewable in the Dynamics | Survey Responses section, and stats like customer satisfaction  (CSAT) metrics are here. 

Or you can see individual responses from their respective Account’s page.

![Figure: Customer Voice Survey section of Dynamics showing Survey Responses all together](customer-voice-responses-together.png)

If you’re a company that cares more about qualitative information than quantitative (e.g. you run few large projects rather than many small ones), then it’s a good idea to also make sure you set up email notifications when responses come in so that you don’t miss them, and you can analyze each one individually.

![Figure: Email notification](customer-voice-email-notification.png)
