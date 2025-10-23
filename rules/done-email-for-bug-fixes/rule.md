---
seoDescription: Perfectly fix bugs by including current status, investigation, and solution in your email replies, ensuring efficient communication with clients.
type: rule
archivedreason:
title: Do you know how to reply 'Done' after fixing a bug?
guid: b1304beb-f898-4ae3-a18f-a8bfbb1b7a45
uri: done-email-for-bug-fixes
created: 2009-04-08T09:05:06.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - reply-done
  - close-pbis-with-context
  - include-useful-details-in-emails
redirects:
  - dones-do-you-know-how-to-do-a-perfect-done-replying-to-a-bug
  - dones-do-you-know-how-to-do-a-perfect-done-(replying-to-a-bug)
  - how-to-do-a-perfect-done

---


When replying to a bug in an email, make sure your response helps everyone understand the current state, what you found, and how it was resolved.

<!--endintro-->

## 1. Investigation details

Share what you discovered about the issue.  

* If you already know the cause, describe it clearly
* If you are still investigating, explain what you have checked and what possible causes you ruled out

## 2. Solution

Describe how you fixed the problem.  

Include a short code snippet or example if it helps others understand the change.

## 3. Current ctatus

Explain the most up-to-date situation for the bug.  

* If the bug is **fixed**, [include a screenshot](/include-useful-details-in-emails) showing the working result
* If it’s **not yet fixed**, ask the reporter for more details so you can continue investigating

::: info
**Note:** For clarity, "Done" (or "Not done" / "Already done" / "Partially done") should be [the first word(s) of the email](/reply-done/#tip-1-say-done-first).
:::

---

::: email-template  

| | |
| -------- | --- |
| To: | John |
| Subject: | RE: 🐛 SSW.Website - Can't access website |  
::: email-content

### Hi John

✅ Done - Bug has been fixed

**Investigation:**\
As per the error message you provided below, it’s a timeout issue.

**Solution:**\
I have increased the timeout threshold in the connection string.

**Current Status:**\
The site is working now.

![Figure: Website is up and running](bug-reply-screenshot.png)  

:::  
:::  
::: good  
Figure: Good example - Replying to a bug with the details  
:::
