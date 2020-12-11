---
type: rule
archivedreason: 
title: Stored Procedures - Do you use SCOPE_IDENTITY() to get the most recent row identity?
guid: ca492bae-b564-4446-9095-5bae88eecf66
uri: stored-procedures---do-you-use-scope_identity-to-get-the-most-recent-row-identity
created: 2019-11-12T22:20:30.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

When inserting a row in a stored procedure, always use SCOPE\_IDENTITY() if you want to get the ID of the row that was just inserted. A common error is to use @@IDENTITY, which returns the most recently created identity for your current connection, not necessarily the identity for the recently added row in a table. You could have a situation where there is a trigger that inserts a new record in a Logs Table, for example, when your Stored Procedure or INSERT SQL Statement inserts a record in the Orders Table. If you use @@IDENTITY to retrieve the identity of the new order, you will actually get the identity of the record added into the Log Table and not the Orders Table, which will create a nasty bug in your data access layer. To avoid the potential problems associated with someone adding a trigger later on, always use SCOPE\_IDENTITY() to return the identity of the recently added row in your INSERT SQL Statement or Stored Procedure.

<!--endintro-->

Behold this example from SQL Server Books online.

USE tempdb
GO
CREATE TABLE TZ (
 Z\_id int IDENTITY(1,1)PRIMARY KEY,
 Z\_name varchar(20) NOT NULL)
INSERT TZ
 VALUES ('Lisa')
INSERT TZ
 VALUES ('Mike')
INSERT TZ
 VALUES ('Carla')
SELECT \* FROM TZ
--Result set: This is how table TZ looks.
Z\_id Z\_name
-------------
1 Lisa
2 Mike
3 Carla
CREATE TABLE TY (
 Y\_id int IDENTITY(100,5)PRIMARY KEY,
 Y\_name varchar(20) NULL)
INSERT TY (Y\_name)
 VALUES ('boathouse')
INSERT TY (Y\_name)
 VALUES ('rocks')
INSERT TY (Y\_name)
 VALUES ('elevator')
SELECT \* FROM TY
--Result set: This is how TY looks:
Y\_id Y\_name
---------------
100 boathouse
105 rocks
110 elevator
/\*Create the trigger that inserts a row in table TY 
when a row is inserted in table TZ\*/
CREATE TRIGGER Ztrig
ON TZ
FOR INSERT AS 
 BEGIN
 INSERT TY VALUES ('')
 END
/\*FIRE the trigger and determine what identity values you obtain 
with the @@IDENTITY and SCOPE\_IDENTITY functions.\*/
INSERT TZ VALUES ('Rosalie')
SELECT SCOPE\_IDENTITY() AS [SCOPE\_IDENTITY]
GO
SELECT @@IDENTITY AS [@@IDENTITY]
GO

Notice the difference in the result sets. As you can see, it's crucial that you understand the difference between the 2 commands in order to get the correct ID of the row you just inserted.

SCOPE\_IDENTITY
4
/\*SCOPE\_IDENTITY returned the last identity value in the same scope. This was the insert on table TZ.\*/
@@IDENTITY
115
/\*@@IDENTITY returned the last identity value inserted to TY by the trigger. This fired because of an earlier insert on TZ.\*/
