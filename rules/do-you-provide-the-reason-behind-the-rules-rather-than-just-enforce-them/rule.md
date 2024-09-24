---
type: rule
title: General - Standards Watchdog - Do you provide the reason behind the rules
  rather than just enforce them?
uri: do-you-provide-the-reason-behind-the-rules-rather-than-just-enforce-them
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
related: []
redirects:
  - general-standards-watchdog-do-you-provide-the-reason-behind-the-rules-rather-than-just-enforce-them
created: 2012-09-25T17:54:42.000Z
archivedreason: null
guid: b9a01f68-abe6-45aa-b1cd-aa4a68b02186
---

Learning lessons the hard way is a fact of life, but one of the great things about teamwork is that you can help others avoid making the same mistakes over and over again. This is the foundation of great standards! But what happens when a new (or old) team member misses a standard?

<!--endintro-->

> *"The floggings will continue until morale improves"*
> 
> \- A bad manager

Everyone makes mistakes. If you run around wielding your authority as a cudgel, telling them they'd better comply *or else*, two things will happen:

1. They will resent you
2. They will only bother following standards when you're around

For example: if one of your standards is for developers to send "test please" emails, there's a hard-learned lesson behind that standard (or else it wouldn't exist!). You can beat your developers over the head with the rule, or you can take 5 minutes to explain the reasons why it exists and why it's important.

::: email-template
|          |     |
| -------- | --- |
| From:    | Boss |
| To:      | Mark |
| Subject: | No test please email |
::: email-content  

### Hi Mark,

You didn't send a "test please" email. Please do that next time.

Boss

:::
:::
::: bad
Figure: Bad example - This email doesn't tell Mark why this is so important. 
:::


::: email-template
|          |     |
| -------- | --- |
| From:    | Boss |
| To:      | Mark |
| Subject: | Test Please emails standard |
::: email-content  

### Hi Mark,

Regarding that PBI you worked on yesterday.

We have a standard about sending Test Please emails to the client (check out [this rule](/request-a-test-please/)).

This saves time by getting early feedback, allowing bugs to be fixed while it's still fresh in the developer's mind.

The longer the feedback loop takes, the more expensive a PBI becomes to the client :(

:::
:::
::: good
Figure: Good example - provide a link to your standard and the main reason(s) why this standard is important
:::