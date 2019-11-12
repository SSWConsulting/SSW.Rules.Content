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


<p class="ssw15-rteElement-P">​A transaction means an atomic operation, it assures that all operations within the transaction are successful, if not, the transaction will cancel all operations and roll back to the original state of the database, that means no dirty data and mess exists in the database, so if a stored procedure has many steps, and each step has relation with other steps, it is strongly recommended that you encapsulate the procedure in a transaction.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE [dbo].[procInit]<br>AS<br> DELETE ParaLeft<br> DELETE ParaRight<br> INSERT INTO ParaLeft (ParaID)<br> SELECT ParaID FROM Para</p><dd class="ssw15-rteElement-FigureBad">Bad example&#58;&#160;No tran​saction here, if any of operations fail, the database will only partially update, resulting in an unwanted result<br></dd><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE [dbo].[procInit]<br>AS<br> BEGIN TRANSACTION<br> DELETE ParaLeft<br> DELETE ParaRight<br> INSERT INTO ParaLeft (ParaID)<br> SELECT ParaID FROM Para<br> COMMIT</p><dd class="ssw15-rteElement-FigureGood">Good example&#58;&#160;Using a transaction to assure that all operations within the transaction will be successful, otherwise, the database will roll back to original state​<br></dd>


