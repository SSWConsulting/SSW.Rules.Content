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


<p class="ssw15-rteElement-P">​​​In many cases, there are le​gal requirements to audit all updates to financial records. In other cases, you will want to be able to track and undo deletes to your database. With the use of Temporal tables, this becomes much easier to manage.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<div><font color="#333333"><a href="https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver15">​Temporal tables​</a> were introduced in SQL Server 2016 and enhanced with increased features in SQL Server 2017.<br>They offer the ability to record all the entity changes to a history table allowing the querying of the entity at a point in time.​<br></font></div><p class="ssw15-rteElement-P">​</p><dd class="ssw15-rteElement-FigureGood">​​Pros:<br></dd><p class="ssw15-rteElement-P"></p><ul><li>You can query values of a specific entity at a particular point in time or time range over its lifetime.</li><li>Restore accidentally deleted records by retrieving them from the history table.</li><li>Retention period can be set on the history table, this can be set as frequent as 1 day.</li></ul> <br><p></p><dd class="ssw15-rteElement-FigureBad">Co​​ns:<br></dd><p class="ssw15-rteElement-P"></p><ul><li>History tables can grow very quickly in size.​<br></li><li>Storing blob datatypes (nvarchar(max), varbinary(max), ntext and image) can increase storage costs and decrease performance.</li><li>You cannot truncate the table.</li><li>Temporal and history table cannot be FILETABLE.</li><li>Direct modification of the data in the history is not permitted.</li></ul> <h3 class="ssw15-rteElement-H3">How do I create a Temporal table?</h3> It’s actually quite simple, here is a code snippet converting a table from the Northwind schema into a temporal table.<br><p></p><p class="ssw15-rteElement-CodeArea">​​CREATE TABLE dbo.Shippers<br>(<br>               [ShipperID] int IDENTITY(1, 1) NOT NULL,<br>               [CompanyName] nvarchar(40) NOT NULL,<br>               [Phone] nvarchar(24) NULL,<br>             <strong>  [SysStartTime] datetime2 GENERATED ALWAYS AS ROW START,</strong><br><strong>               [SysEndTime]  datetime2 GENERATED ALWAYS AS ROW END,</strong><br><strong>               PERIOD FOR SYSTEM_TIME (SysStartTime, SysEndTime),</strong><br>               CONSTRAINT PK_Shippers PRIMARY KEY CLUSTERED<br>               (             <br>                              [ShipperID]<br>               )<br>)<br><strong>WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.ShippersHistory));</strong><br></p><dd class="ssw15-rteElement-FigureNormal">Figure: Shippers table from the Northwind schema converted to a temporal table.​<br></dd><dl class="ssw15-rteElement-ImageArea"><br><img src="Shippers_TemporalTable.PNG" alt="" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: New temporal table shown in SQL Management Studio.<br></dd><div><font color="#333333"><br></font></div><p class="ssw15-rteElement-CodeArea">-- Update the tables history data retention<br>ALTER TABLE dbo.Shippers<br>SET (SYSTEM_VERSIONING = ON (HISTORY_RETENTION_PERIOD = 7 YEARS));​<br></p><dd class="ssw15-rteElement-FigureNormal">Figure: Code snippet for updating data retention.<br></dd><div><font color="#333333">​</font></div><div><font color="#333333">Some alternative solutions are:<br></font></div><ol><li>Manually adding triggers on all database tables to log every table</li><li>The business objects or stored procedures all write to 2 tables the main table such as Customer and CustomerAudit</li><li>Using a logging utility to audit database changes<br></li></ol><div><font color="#333333"><br></font></div><p>This means that you can devote your development time to areas other than auditing. Also, unlike other utilities which use triggers (such as <a href="https://www.ssw.com.au/ssw/Redirect/ApexSQL.htm">ApexSQL Audit</a>), there is no performance overhead because it relies upon log files already created by SQL Server. If required, you can export the log information to SQL Server, so you can perform advanced queries on it. It even allows you to recover previously deleted tables.​<br></p>


