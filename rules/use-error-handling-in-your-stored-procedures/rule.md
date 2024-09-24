---
type: rule
archivedreason: 
title: Stored Procedures - Do you use error handling in your Stored Procedures?
guid: fe0b081d-019e-4810-beca-1d8b71957403
uri: use-error-handling-in-your-stored-procedures
created: 2020-03-17T03:41:49.0000000Z
authors:
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- stored-procedures-do-you-use-error-handling-in-your-stored-procedures

---

You should always include error handling in your stored procedures, it allows you to catch errors and either log them or attempt to correct them.
[THROW (Transact-SQL)](https&#58;//docs.microsoft.com/en-us/sql/t-sql/language-elements/throw-transact-sql?view=sql-server-ver15) lets you generate your own custom error messages, which can be more detailed in describing the problem and assist in debugging.

<!--endintro-->

Here’s an example of the syntax used when implementing THROW.

```sql
-- Syntax
THROW error_number, message, state;
```
**Figure: Example of the THROW syntax** 

There are 3 main arguments:
* **error\_number (int)** - Must be greater than or equal to 50000 and less than or equal to 2147483647.
* **message (nvarchar)** - Maximum of 2048 characters.
* **state (tinyint)** - Must be between 0 and 255

The  **state** argument can be used to help pinpoint where the error occurred by using a different value without changing the  **error\_number** or  **message** . This is useful if you have multiple steps in a process that may throw identical error descriptions.

```sql
-- Example
THROW 51000, 'The record does not exist.', 1;
```

**Figure: Example of using THROW** 

### Implementing Error Handling using THROW
Here we are generating a divide-by-zero error to easily raise a SQL exception and is used as a place holder for logic that we would have in our stored procedure.

```sql
DECLARE @inputNumber AS INT = 0;
 
-- Generate a divide-by-zero error
SELECT 1 / @inputNumber AS Error;
```

::: bad
Figure: Bad Example - No error handling.

:::

Below we have wrapped our stored procedure logic in a TRY block and added a CATCH block to handle the error. More information can be found here [TRY...CATCH (Transact-SQL)](https&#58;//docs.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver15).

We know this divide-by-zero is going to cause an exception and the error number for this specific SQL exception is 8134. See [(MSSQL Errors)](https&#58;//docs.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-events-and-errors?view=sql-server-ver15) for more error numbers.

In our CATCH block, we check the error to ensure it’s the one that we want to handle otherwise, we re-throw the original exception.
Finally, when we catch the error we are looking for we can log some information about it and attempt to run our stored procedure logic again with different parameters.

```sql
DECLARE @errorCode AS INT;
DECLARE @inputNumber AS INT;
 
BEGIN TRY
       -- Generate a divide-by-zero error
       SET @inputNumber = 0;
       SELECT 1 / @inputNumber AS Error;
END TRY
BEGIN CATCH
       SET @errorCode = (SELECT ERROR_NUMBER());
       IF @errorCode = 8134 -- Divide by zero error encountered.
              BEGIN
                    PRINT 'Divide by zero error encountered. Attempting to correct'
                     SET @inputNumber = 1;
                    SELECT 1 / @inputNumber AS Error;
             END
       ELSE
              THROW;
END CATCH;
```

::: good
Figure: Good Example - Using error handling to catch an error and attempt to resolve it.

:::

The example below shows how you can catch an error and retrieve all the details about it.
This is very useful if you want to save these errors to another table or trigger a stored procedure.

```sql
BEGIN TRY
       -- Generate a divide-by-zero error. 
       SELECT 1 / 0 AS Error;
END TRY
BEGIN CATCH
       SELECT
             ERROR_NUMBER() AS ErrorNumber,
             ERROR_STATE() AS ErrorState,
             ERROR_SEVERITY() AS ErrorSeverity,
             ERROR_PROCEDURE() AS ErrorProcedure,
             ERROR_LINE() AS ErrorLine,
             ERROR_MESSAGE() AS ErrorMessage;		 		             -- Insert logic for persisting log information (Log to table or log to file)
 
             THROW;
END CATCH;
```

::: good
Figure: Good Example - Using error handling to catch an error and retrieving its details, allowing it to be logged.

:::
