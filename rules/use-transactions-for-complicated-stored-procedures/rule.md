---
type: rule
archivedreason: 
title: Stored Procedures - Do you use transactions for complicated stored procedures?
guid: 5d8fa649-2fb5-4345-b244-bc7572ec2766
uri: use-transactions-for-complicated-stored-procedures
created: 2019-11-12T23:23:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- stored-procedures-do-you-use-transactions-for-complicated-stored-procedures

---

A transaction means an atomic operation, it assures that all operations within the transaction are successful, if not, the transaction will cancel all operations and roll back to the original state of the database, that means no dirty data and mess exists in the database, so if a stored procedure has many steps, and each step has relation with other steps, it is strongly recommended that you encapsulate the procedure in a transaction.

<!--endintro-->

```sql
ALTER PROCEDURE [dbo].[procInit]
AS
 DELETE ParaLeft
 DELETE ParaRight
 INSERT INTO ParaLeft (ParaID)
 SELECT ParaID FROM Para
```

::: bad
Figure: Bad Example - No transaction here, if any of operations fail, the database will only partially update, resulting in an unwanted result.

:::

```sql
ALTER PROCEDURE [dbo].[procInit]
AS
 BEGIN TRANSACTION
 DELETE ParaLeft
 DELETE ParaRight
 INSERT INTO ParaLeft (ParaID)
 SELECT ParaID FROM Para
 COMMIT
```

::: good
Figure: Good Example - Using a transaction to assure that all operations within the transaction will be successful, otherwise, the database will roll back to the original state.

:::
