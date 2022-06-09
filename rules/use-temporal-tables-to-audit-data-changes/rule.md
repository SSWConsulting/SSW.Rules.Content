---
type: rule
archivedreason: 
title: Data - Do you use temporal tables to audit data changes?
guid: 94b69b2e-cb6e-482a-bc6a-f710a7079fec
uri: use-temporal-tables-to-audit-data-changes
created: 2019-11-25T22:35:48.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects:
- data-do-you-use-temporal-tables-to-audit-data-changes

---

In many cases, there are legal requirements to audit all updates to financial records. In other cases, you will want to be able to track and undo deletes to your database. With the use of Temporal tables, this becomes much easier to manage.

<!--endintro-->

[Temporal tables](https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables) were introduced in SQL Server 2016 and enhanced with increased features in SQL Server 2017.
They offer the ability to record all the entity changes to a history table allowing the querying of the entity at a point in time.

::: good
Pros:

:::

* You can query values of a specific entity at a particular point in time or time range over its lifetime.
* Restore accidentally deleted records by retrieving them from the history table.
* Retention period can be set on the history table, this can be set as frequent as 1 day.

::: bad
Cons:

:::


* History tables can grow very quickly in size.
* Storing blob datatypes (nvarchar(max), varbinary(max), ntext and image) can increase storage costs and decrease performance.
* You cannot truncate the table.
* Temporal and history table cannot be FILETABLE.
* Direct modification of the data in the history is not permitted.

 
### How do I create a Temporal table?
It’s actually quite simple, here is a code snippet converting a table from the Northwind schema into a temporal table.

```sql
CREATE TABLE dbo.Shippers
(
               [ShipperID] int IDENTITY(1, 1) NOT NULL,
               [CompanyName] nvarchar(40) NOT NULL,
               [Phone] nvarchar(24) NULL,
              [SysStartTime] datetime2 GENERATED ALWAYS AS ROW START, [SysEndTime]  datetime2 GENERATED ALWAYS AS ROW END, PERIOD FOR SYSTEM_TIME (SysStartTime, SysEndTime), CONSTRAINT PK_Shippers PRIMARY KEY CLUSTERED
               (             
                              [ShipperID]
               )
)
 WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.ShippersHistory));
```
 **Figure: Shippers table from the Northwind schema converted to a temporal table.** 
 
 
![Figure: New temporal table shown in SQL Management Studio.](Shippers_TemporalTable.PNG)


```sql
-- Update the tables history data retention
ALTER TABLE dbo.Shippers
SET (SYSTEM_VERSIONING = ON (HISTORY_RETENTION_PERIOD = 7 YEARS));
```
 **Figure: Code snippet for updating data retention.
** 


Some alternative solutions are:

1. Manually adding triggers on all database tables to log every table
2. The business objects or stored procedures all write to 2 tables the main table such as Customer and CustomerAudit
3. Using a logging utility to audit database changes

This means that you can devote your development time to areas other than auditing. Also, unlike other utilities which use triggers (such as [ApexSQL Audit](https://www.ssw.com.au/ssw/Redirect/ApexSQL.htm)), there is no performance overhead because it relies upon log files already created by SQL Server. If required, you can export the log information to SQL Server, so you can perform advanced queries on it. It even allows you to recover previously deleted tables.
