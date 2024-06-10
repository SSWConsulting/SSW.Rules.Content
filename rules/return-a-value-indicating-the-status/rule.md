---
seoDescription: Stored procedures should always return a value indicating the status, with 0 signifying success and error numbers denoting errors.
type: rule
archivedreason:
title: Stored Procedures - Do you return a value indicating the status?
guid: d66669fc-55a7-47db-bb52-ef4496191c71
uri: return-a-value-indicating-the-status
created: 2019-11-08T17:28:06.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - stored-procedures-do-you-return-a-value-indicating-the-status
---

Make sure your stored procedures always return a value indicating the status. All stored procedures should return the error number (if an error) or a 0 to indicate no errors (ie success).

<!--endintro-->
