---
type: rule
title: Security - Do you use service accounts?
uri: do-you-use-service-accounts
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects: []
created: 2018-08-22T05:08:37.000Z
archivedreason: This rule is now outdated, service accounts are useful but gMSAs
  and other kinds of secure identities should be used instead - replaced by
  [https://www.ssw.com.au/rules/group-managed-service-account-gmsa](/rules/group-managed-service-account-gmsa)
guid: 3a663158-60ca-4b55-b9cc-eec5774b3346
---

Do you use service accounts for recurring tasks and systems, or do you use user and personal accounts?

<!--endintro-->

As a rule, you should never use a user account for accessing systems, reports, tasks and other long-running applications that do not need human or user interaction to run.

Service accounts provide a security context where the applications run, without the need to worry about their passwords or privileges. If a user changes their password, you will not break anything, because service account password normally does not expire and changing them is never needed.

Also, if the security of a user account is breached, you do not have to worry about any other systems being compromised - that account was not being used to run any applications. Always keep your service accounts passwords safe and complex, and you will never need to worry about it.
