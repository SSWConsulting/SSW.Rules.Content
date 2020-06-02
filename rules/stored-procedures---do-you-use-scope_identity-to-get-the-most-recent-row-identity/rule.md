

---
uri: stored-procedures---do-you-use-scope_identity-to-get-the-most-recent-row-identity
title: Stored Procedures - Do you use SCOPE_IDENTITY() to get the most recent row identity?
created: YYYY-11-DD 22:20:30
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> When inserting a row in a stored procedure, always use SCOPE_IDENTITY() if you want to get the ID of the row that was just inserted. A common error is to use @@IDENTITY, which returns the most recently created identity for your current connection, not necessarily the identity for the recently added row in a table. You could have a situation where there is a trigger that inserts a new record in a Logs Table, for example, when your Stored Procedure or INSERT SQL Statement inserts a record in the Orders Table. If you use @@IDENTITY to retrieve the identity of the new order, you will actually get the identity of the record added into the Log Table and not the Orders Table, which will create a nasty bug in your data access layer. To avoid the potential problems associated with someone adding a trigger later on, always use SCOPE_IDENTITY() to return the identity of the recently added row in your INSERT SQL Statement or Stored Procedure.<br> </span>

<p>​Behold this example from SQL Server Books online.</p><p class="ssw15-rteElement-CodeArea">USE tempdb<br>GO<br>CREATE TABLE TZ (<br> Z_id int IDENTITY(1,1)PRIMARY KEY,<br> Z_name varchar(20) NOT NULL)<br>INSERT TZ<br> VALUES ('Lisa')<br>INSERT TZ<br> VALUES ('Mike')<br>INSERT TZ<br> VALUES ('Carla')<br>SELECT * FROM TZ<br>--Result set&#58; This is how table TZ looks.<br>Z_id Z_name<br>-------------<br>1 Lisa<br>2 Mike<br>3 Carla<br>CREATE TABLE TY (<br> Y_id int IDENTITY(100,5)PRIMARY KEY,<br> Y_name varchar(20) NULL)<br>INSERT TY (Y_name)<br> VALUES ('boathouse')<br>INSERT TY (Y_name)<br> VALUES ('rocks')<br>INSERT TY (Y_name)<br> VALUES ('elevator')<br>SELECT * FROM TY<br>--Result set&#58; This is how TY looks&#58;<br>Y_id Y_name<br>---------------<br>100 boathouse<br>105 rocks<br>110 elevator<br>/*Create the trigger that inserts a row in table TY <br>when a row is inserted in table TZ*/<br>CREATE TRIGGER Ztrig<br>ON TZ<br>FOR INSERT AS <br> BEGIN<br> INSERT TY VALUES ('')<br> END<br>/*FIRE the trigger and determine what identity values you obtain <br>with the @@IDENTITY and SCOPE_IDENTITY functions.*/<br>INSERT TZ VALUES ('Rosalie')<br>SELECT SCOPE_IDENTITY() AS [SCOPE_IDENTITY]<br>GO<br>SELECT @@IDENTITY AS [@@IDENTITY]<br>GO</p><p><br>Notice the difference in the result sets. As you can see, it's crucial that you understand the difference between the 2 commands in order to get the correct ID of the row you just inserted.</p><p class="ssw15-rteElement-CodeArea">SCOPE_IDENTITY<br>4<br>/*SCOPE_IDENTITY returned the last identity value in the same scope. This was the insert on table TZ.*/<br>@@IDENTITY<br>115<br>/*@@IDENTITY returned the last identity value inserted to TY by the trigger. This fired because of an earlier insert on TZ.*/​<br></p>


