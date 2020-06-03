---
type: rule
title: Stored Procedures - Do you use transactions for complicated stored procedures?
uri: stored-procedures---do-you-use-transactions-for-complicated-stored-procedures
created: 2019-11-12T23:23:19.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​A transaction means an atomic operation, it assures that all operations within the transaction are successful, if not, the transaction will cancel all operations and roll back to the original state of the database, that means no dirty data and mess exists in the database, so if a stored procedure has many steps, and each step has relation with other steps, it is strongly recommended that you encapsulate the procedure in a transaction.​<br></p> </span>

<p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE [dbo].[procInit]<br>AS<br> DELETE ParaLeft<br> DELETE ParaRight<br> INSERT INTO ParaLeft (ParaID)<br> SELECT ParaID FROM Para</p><dd class="ssw15-rteElement-FigureBad">Figure&#58;&#160;Bad Example -&#160;No tran​saction here, if any of operations fail, the database will only partially update, resulting in an unwanted result.<br></dd><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE [dbo].[procInit]<br>AS<br> BEGIN TRANSACTION<br> DELETE ParaLeft<br> DELETE ParaRight<br> INSERT INTO ParaLeft (ParaID)<br> SELECT ParaID FROM Para<br> COMMIT</p><dd class="ssw15-rteElement-FigureGood">Figure&#58;&#160;Good Example -&#160;Using a transaction to assure that all operations within the transaction will be successful, otherwise, the database will roll back to the original state​.<br></dd>


