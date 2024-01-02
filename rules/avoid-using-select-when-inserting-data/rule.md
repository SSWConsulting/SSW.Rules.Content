---
type: rule
archivedreason: 
title: Stored Procedures - Do you avoid using SELECT * when inserting data?
guid: f4a72ca6-08bd-41a0-8138-83ab0adab728
uri: avoid-using-select-when-inserting-data
created: 2019-11-12T23:04:20.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- stored-procedures-do-you-avoid-using-select-when-inserting-data

---

Using a statement like "INSERT tableName SELECT \* FROM otherTable", makes your stored procedures vulnerable to failure. Once either of the two tables change, your stored procedure won't work. Not only that, when the inserting table has an identity column, such a statement will cause an error - "An explicit value for the identity column in table ParaRight can only be specified when a column list is used and IDENTITY\_INSERT is ON."


<!--endintro-->

```sql
USE [ParaGreg]
GO
/****** Object: StoredProcedure [dbo].[procMove] Script Date: 08/08/2008 12:18:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[procMove]
@id AS Char,
@direction AS INT
AS
IF @direction = 0
BEGIN
 INSERT INTO ParaRight
 SELECT * FROM ParaLeft
 WHERE ParaID = @id
 DELETE FROM ParaLeft
 WHERE ParaID = @id
END
ELSE IF @direction = 1
BEGIN
 INSERT INTO ParaLeft
 SELECT * FROM ParaRight
 WHERE ParaID = @id
 DELETE FROM ParaRight
 WHERE ParaID = @id
END
```

::: bad
Figure: Bad Example - Using SELECT \* when inserting data. Besides, this stored procedure should have an Else section to raise error when no condition is satisfied

:::

```sql
USE [ParaGreg]
GO
/****** Object: StoredProcedure [dbo].[procMove] Script Date: 08/08/2008 12:18:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[procMove]
@id AS Char,
@direction AS INT
AS
IF @direction = 0
BEGIN
 INSERT INTO ParaRight
 SELECT Col1,Col2 FROM ParaLeft
 WHERE ParaID = @id
 DELETE FROM ParaLeft
 WHERE ParaID = @id
END
ELSE IF @direction = 1
BEGIN
 INSERT INTO ParaLeft
 SELECT * FROM ParaRight
 WHERE ParaID = @id
 DELETE FROM ParaRight
 WHERE ParaID = @id
END
ELSE BEGIN PRINT "Please use a correct direction"
 END
```

::: good
Figure: Good Example - Using concrete columns instead of \* and provide an Else section to raise errors

:::
