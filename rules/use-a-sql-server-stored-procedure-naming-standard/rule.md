---
type: rule
archivedreason: 
title: General - Do you use a SQL Server Stored Procedure Naming Standard?
guid: f158faaf-d3ac-4323-bde3-1a8d37b7fffb
uri: use-a-sql-server-stored-procedure-naming-standard
created: 2019-12-31T04:37:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- general-do-you-use-a-sql-server-stored-procedure-naming-standard

---

This standard outlines the standard on naming Stored Procedures within SQL Server. Use these standards when creating new Stored Procedures or if you find an older Stored Procedure that doesn't follow these standards within SSW.

<!--endintro-->

**Note:** Stored Procedures will run fractionally slower if they start with a prefix of sp\_   This is because SQL Server will look for a system stored proc first. Therefore we never recommend starting stored procs with a prefix of sp\_
Do you agree with them all? Are we missing some? Let us know what you think.

### Syntax

Stored Procedure names are to have this syntax:
[proc] [MainTableName] By [FieldName(optional)] [Action]
[  1  ] [         2          ]     [       3                  ] [   4    ]
[1] All stored procedures must have the prefix of 'proc'. All internal SQL Server stored procedures are prefixed with "sp\_", and it is recommended not to prefix stored procedures with this as it is a little slower.
[2] The name of the table that the Stored Procedure accesses.
[3] (optional) The name of the field that are in the WHERE clause. ie. procClientByCoNameSelect, procClientByClientIDSelect
[4] Lastly the action which this Stored Procedure performs.

If Stored Procedure returns a recordset then suffix is 'Select'.
If Stored Procedure inserts data then suffix is 'Insert'.
If Stored Procedure updates data then suffix is 'Update'.
If Stored Procedure Inserts and updates then suffix is 'Save'.
If Stored Procedure deletes data then suffix is 'Delete'.
If Stored Procedure refreshes data (ie. drop and create) a table then suffix is 'Create'.
If Stored Procedure returns an output parameter and nothing else then make the suffix is 'Output'.

```sql
ALTER PROCEDURE procClientRateOutput

         @pstrClientID VARCHAR(6) = 'CABLE',
         @pstrCategoryID VARCHAR(6) = '<All>',
         @pstrEmpID VARCHAR(6)='AC',
         @pdteDate datetime = '1996/1/1',
         @curRate MONEY OUTPUT

AS

-- Description: Get the $Rate for this client and this employee
--         and this category from Table ClientRate

SET @curRate = (
                SELECT TOP 1 Rate
                FROM ClientRate
                WHERE ClientID=@pstrClientID
                AND EmpID=@pstrEmpID
                AND CategoryID=@pstrCategoryID
                AND DateEnd > @pdteDate
                ORDER BY DateEnd
               )

IF @curRate IS NULL

         SET @curRate =
(
                SELECT TOP 1 Rate
                FROM ClientRate
                WHERE ClientID=@pstrClientID
                AND EmpID=@pstrEmpID
                AND CategoryID='<ALL>'
                AND DateEnd > @pdteDate
                ORDER BY DateEnd
               )

RETURN
```

::: good
Figure: Good Example - stored proc that returns only an output parameter

:::

::: greybox
Select 'procGetRate' or 'sp\_GetRate'
Insert 'procEmailMergeAdd'  
:::

::: bad
Figure: Bad Example

:::

::: greybox
'procClientRateSelect'
'procEmailMergeInsert'

:::

::: good
Figure: Good Example

:::
