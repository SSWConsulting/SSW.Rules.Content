---
type: rule
archivedreason: 
title: Data - Do you use Identities in SQL Server?
guid: fdf8110f-4d46-4459-b97c-a825bab3efed
uri: use-identities-in-sql-server
created: 2019-11-25T19:08:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- data-do-you-use-identities-in-sql-server

---

This one is going to be a controversial one. But the bottom line is every now and then you want to do something and then you curse and wish your database didn't have identities. So why use them? Let's look at the problems first:

<!--endintro-->


::: bad
Cons:  
:::

* You can't manually change a Primary Key and let the Cascade Update do its work, eg. an InvoiceID
* Hassles when importing data into related tables where you want to control the Primary Key eg. Order and Order Details
* Replication you will get conflicts


In Microsoft Access you have autonumbers and there is no way around them so never use them.
But in SQL Server you have identities and we have these procs:

* DBCC CHECKIDENT - Checks the current identity value for the specified table and, if needed, corrects the identity value
* SET IDENTITY\_INSERT { table } { ON | OFF } - Allows explicit values to be inserted into the identity column of a table



::: good
Pros:

:::

* Less programming - letting the database take care of it
* Replication (identities are supported by SQL Server with ranges so when you want replication, no coding)
* Avoiding concurrency errors on high INSERT systems so no coding


So the only Con left is the importing of data but we can use one of the above procs to get around it. See grey box.

### The best way to import data into SQL Server (with Identities)

Using SQL Management Studio

1. Right-Click your database to open the menu
2. Navigate to  **Tasks | Import Data…** to open the wizard
3. When selecting Source Tables and Views click on  **Edit Mappings…**



![](IdentityImportEditMappings.png) **Figure: SQL Import Wizard - Edit Mappings
** **
** 
4. Ensure the Enable identity insert is checked
![](EnableIdentityInsert.png) **Figure: SQL Import Wizard – Ensure Enable identity insert is checked.
** 

Alternatively, you can also enable and disable the identity insert through SQL with the following commands



```
SET IDENTITY_INSERT Shippers ON --this will allow manual identity INSERTS on the requested table
 
-- Modify the table here
 
SET IDENTITY_INSERT Shippers OFF --as it can only be on for one table at a time
```



More information on [IDENTITY\_INSERT](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-identity-insert-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15)

### Automatic Identity Range Handling


The simplest way of handling identity ranges across replicas is to allow SQL Server to manage identity range handling for you. To use automatic identity range handling, you must first enable the feature at the time the publication is created, assign a set of initial Publisher and Subscriber identity range values, and then assign a threshold value that determines when a new identity range is created.
For example, assigning an identity range from 1000 through 2000 to a Publisher, and a range from 2001 through 3000 to an initial Subscriber a range from 3001 to 4000 to the next publisher etc.
