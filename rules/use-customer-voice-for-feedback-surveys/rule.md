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
Customer feedback is something that most companies do not harness the full value of, and is a key way to give your customers’ experience more of a weighting in your decision making.

<!--endintro-->

Dynamics 365 has Customer Voice Surveys to harness this, and it is included with many D365 products. It can also be added as a standalone product if you don’t already have it.

### Creating the Survey

It’s built on the Microsoft Forms engine, so creating feedback surveys is very simple and intuitive.

![Figure: Survey creation](rules-picture.png)

Since we’re running Scrum projects, and our clients are used to doing Sprint Retrospectives, we frame the questions in the same way (what went well, what didn’t, and what should we change?).

### Sending the Survey

Surveys can be sent manually, but for consistent value, you should have automated triggers in place. This could be after any significant milestone (like after a Spec Review, or at project completion), but it’s best if it’s something easily automated, such as once you’ve billed them a certain amount (e.g. $50k if your usual project sizes are $100k-200k).

\[TODO: Mehmet - Image of trigger workflow]\
**Figure: Set up triggers to send out the surveys** 

### Receiving Responses

Responses to surveys will come into your Dynamics and can be viewed in the Survey Responses section, and aggregate information such as customer satisfaction metrics can be calculated from here. You can also see individual responses form their respective Account’s page.

![Figure: Customer Voice Survey section of Dynamics showing Survey Responses all together](customer-voice-responses-together.png)

If you’re a company that cares more about qualitative information than quantitative (e.g. you run few large projects rather than many small ones), then it’s a good idea to also make sure you set up email notifications when responses come in so that you don’t miss them, and you can analyze each one individually.

![Figure: Email notification](customer-voice-email-notification.png)