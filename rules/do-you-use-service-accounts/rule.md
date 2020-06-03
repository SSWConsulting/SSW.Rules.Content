---
type: rule
title: Do you use service accounts?
uri: do-you-use-service-accounts
created: 2018-08-22T05:08:37.0000000Z
authors:
- id: 73
  title: Kaique Biancatti

---



<span class='intro'> Do you use service accounts for recurring tasks and systems, or do you use user and personal accounts?<br> </span>

<p><br></p><p>​As a rule, you should never use a user account for accessing systems, reports, tasks and other long-running&#160;applications that do not need human or user interaction to run.</p><p>Service accounts provide a security context where the applications run, without the need to worry about their passwords or privileges. If a user changes their password, you will not break anything, because service account password normally does not expire and changing them is never needed. <br></p><p>Also, if the security of a user account is breached, you do not have to worry about any other systems being compromised - that account was not being used to run any applications. Always keep your service accounts passwords safe and complex, and you will never need to worry about it.​</p>


