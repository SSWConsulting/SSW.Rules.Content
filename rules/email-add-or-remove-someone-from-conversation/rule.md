---
type: rule
archivedreason: 
title: Do you know how to add or remove someone from the conversation?
guid: 3c8003d8-0779-4ec2-977c-4d114dfb5bad
uri: email-add-or-remove-someone-from-conversation
created: 2009-03-30T02:33:59.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
related: 
- email-send-a-v2
redirects: 
- do-you-know-how-to-add-or-remove-someone-from-the-conversation

---

### Adding someone to the conversation

If you think someone should be involved in a conversation but they're not on the recipient list, all you need to do is "Reply All", put the new recipient in the 'Cc' field and include *(adding xxx to the loop)* at the top of the email. to inform people for clarity. 

<!--endintro-->

::: info
Be aware it is common to "over Cc" people. Every person added to a thread has a cost, so try to not copy people without a reason. When adding someone, it is a good idea to state the reason why they are being added, so it justifies the cost of their time. E.g.: *(Adding Dave to the loop - during the Daily Scrum today it was mentioned he has worked on similar issues and might have some input)*
:::

::: email-template  
|          |     |
| -------- | --- |
| To:      | Scott |
| Cc:      | Gary; Dave; Sophie |
| Bcc:     | |
| Subject: | This is the subject |  
::: email-content  

(looping in Gary, Dave, and Sophie in case they have any insight on the GitHub action)

### Hi Scott,  
\[Email content\]    

:::  
:::  
::: good  
Figure: Good Example - Adding people to an email thread 
:::

### Removing someone from the conversation

If you need to remove someone from the loop (e.g. To have an internal conversation about an email to a client), include *(removing xxx from the loop)* at the top of the email.

::: email-template  
|          |     |
| -------- | --- |
| To:      | Scott |
| Cc:      | Gary; Dave; Sophie |
| Bcc:     | |
| Subject: | This is the subject |  
::: email-content  

(removing Bob from the loop)

### Hi Scott,  
\[Email content\]    

:::  
:::  
::: good  
Figure: Good Example - Removing someone from an email thread
:::

### Moving someone to Bcc

Some issues might happen when deleting people from an email thread:

* The people being dropped won’t know and won’t be able to say *"I don't want to be dropped from this thread"*
* The people who added them in the 1st place don't know that they included unnecessary people
* The others on the thread might not notice the change in email addresses

To avoid these issues, instead of deleting people from the email, you can move them to the Bcc, including *(moving xxx to Bcc)* at the top of the email:

::: email-template  
|          |     |
| -------- | --- |
| To:      | Scott |
| Cc:      | Gary |
| Bcc:     | Dave; Sophie|
| Subject: | This is the subject |  
::: email-content  

(moving non-technical to Bcc)

### Hi Scott,    
\[Email content\]    

:::  
:::  
::: good  
Figure: Good Example - Moving someone to Bcc
:::

**Video:** [Top 10+ Rules to Better Email Communication with Ulysses Maclaren](https://www.youtube.com/watch?v=LAqRokqq4jI)
