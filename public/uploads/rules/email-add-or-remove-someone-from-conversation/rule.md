---
seoDescription: Learn how to add or remove someone from an email conversation, including tips on when and how to do it effectively.
type: rule
archivedreason:
title: Do you know how to add or remove someone from the conversation?
guid: 3c8003d8-0779-4ec2-977c-4d114dfb5bad
uri: email-add-or-remove-someone-from-conversation
created: 2009-03-30T02:33:59.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
related:
  - cc-and-reply-to-all
  - avoid-replying-to-all-when-bcced
  - email-send-a-v2
redirects:
  - do-you-know-how-to-add-or-remove-someone-from-the-conversation
---

It's crucial to have the right people in email threads to maintain clear communication by ensuring key stakeholders are informed, unnecessary participants are removed, and sensitive information is handled with discretion through BCC.

<!--endintro-->

## Adding someone to the conversation

If you think someone should be involved in a conversation but they're not on the recipient list, all you need to do is ["Reply All", put the new recipient in the 'Cc' field](/cc-and-reply-to-all) and include _(adding xxx to the loop)_ at the top of the email. to inform people for clarity.

::: info
Be aware it is common to "over Cc" people. Every person added to a thread has a cost, so try to not copy people without a reason. When adding someone, it is a good idea to state the reason why they are being added, so it justifies the cost of their time. E.g.: _(Adding Dave to the loop - during the Daily Scrum today it was mentioned he has worked on similar issues and might have some input)_
:::

::: email-template  

| | |
| -------- | --- |
| To: | Scott |
| Cc: | Gary; Dave; Sophie |
| Bcc: | |
| Subject: | {{ SUBJECT }} |  
::: email-content

(looping in Gary, Dave, and Sophie in case they have any insight on the GitHub action)

### Hi Scott

{{ EMAIL CONTENT }}

:::  
:::  
::: good  
Figure: Good example - Adding people to an email thread
:::

## Removing someone from the conversation

If you need to remove someone from the loop (e.g. To have an internal conversation about an email to a client), include _(removing Bob from the loop)_ at the top of the email.

::: email-template  

| | |
| -------- | --- |
| To: | Scott |
| Cc: | Gary; Dave; Sophie |
| Bcc: | |
| Subject: | {{ SUBJECT }} |  
::: email-content

(removing Bob from the loop)

### Hi Scott

{{ EMAIL CONTENT }}

:::  
:::  
::: good  
Figure: Good example - Removing someone from an email thread
:::

## Moving someone to Bcc

Some issues might happen when deleting people from an email thread:

* The people being dropped won’t know and won’t be able to say _"I don't want to be dropped from this thread"_
* The people who added them in the 1st place don't know that they included unnecessary people
* The others on the thread might not notice the change in email addresses

To avoid these issues, instead of deleting people from the email, you can move them to the Bcc, including _(moving Bob to Bcc)_ at the top of the email:

::: email-template  

| | |
| -------- | --- |
| To: | Scott |
| Cc: | Gary |
| Bcc: | Dave; Sophie|
| Subject: | {{ SUBJECT }} |  
::: email-content

(moving non-technical to Bcc)

### Hi Scott

{{ EMAIL CONTENT }}

:::  
:::  
::: good  
Figure: Good example - Moving someone to Bcc
:::

**Video:** [Top 10+ Rules to Better Email Communication with Ulysses Maclaren](https://www.youtube.com/watch?v=LAqRokqq4jI)
