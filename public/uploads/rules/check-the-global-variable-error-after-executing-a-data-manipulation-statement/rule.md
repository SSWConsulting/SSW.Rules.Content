---
seoDescription: Check the global variable @@ERROR after executing a data manipulation statement to ensure transactional integrity and rollback potential errors.
type: rule
archivedreason:
title: Stored Procedures - Do you check the global variable @@ERROR after executing a data manipulation statement?
guid: a5e09c0c-cb3b-4d36-a400-51d42fb5a94e
uri: check-the-global-variable-error-after-executing-a-data-manipulation-statement
created: 2019-11-08T20:36:14.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - stored-procedures-do-you-check-the-global-variable-error-after-executing-a-data-manipulation-statement
  - stored-procedures-do-you-check-the-global-variable-@@error-after-executing-a-data-manipulation-statement
---

Always check the global variable @@ERROR immediately after executing a data manipulation statement (like INSERT/UPDATE/DELETE), so that you can rollback the transaction in case of an error (@@ERROR will be greater than 0 in case of an error). This is important, because, by default, SQL Server will not rollback all the previous changes within a transaction if a particular statement fails. This behaviour can be changed by executing SET XACT_ABORT ON. The @@ROWCOUNT variable also plays an important role in determining how many rows were affected by a previous data manipulation (also, retrieval) statement, and based on that you could choose to commit or rollback a particular transaction.

<!--endintro-->
