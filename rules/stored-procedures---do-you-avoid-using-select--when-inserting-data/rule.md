---
type: rule
title: Stored Procedures - Do you avoid using SELECT * when inserting data?
uri: stored-procedures---do-you-avoid-using-select--when-inserting-data
created: 2019-11-12T23:04:20.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​Using a statement like &quot;INSERT tableName SELECT * FROM otherTable&quot;, makes your stored procedures vulnerable to failure. Once either of the two tables changs, your stored procedure won't work. Not only that, when the inserting table has an identity column, such a statement will cause an error - &quot;An explicit value for the identity column in table ParaRight can only be specified when a column list is used and IDENTITY_INSERT is ON.&quot;<br><br> </span>

<p class="ssw15-rteElement-CodeArea">​USE [ParaGreg]<br>GO<br>/****** Object&#58; StoredProcedure [dbo].[procMove] Script Date&#58; 08/08/2008 12&#58;18&#58;33 ******/<br>SET ANSI_NULLS ON<br>GO<br>SET QUOTED_IDENTIFIER ON<br>GO<br>ALTER PROCEDURE [dbo].[procMove]<br>@id AS Char,<br>@direction AS INT<br>AS<br>IF @direction = 0<br>BEGIN<br> INSERT INTO ParaRight<br> SELECT * FROM ParaLeft<br> WHERE ParaID = @id<br> DELETE FROM ParaLeft<br> WHERE ParaID = @id<br>END<br>ELSE IF @direction = 1<br>BEGIN<br> INSERT INTO ParaLeft<br> SELECT * FROM ParaRight<br> WHERE ParaID = @id<br> DELETE FROM ParaRight<br> WHERE ParaID = @id<br>END</p><dd class="ssw15-rteElement-FigureBad">​Bad example&#58;&#160;Using SELECT * when inserting data. Besides, this stored procedure should have an Else section to raise error when no condition is satisfied<br></dd><p class="ssw15-rteElement-CodeArea"><br>USE [ParaGreg]<br>GO<br>/****** Object&#58; StoredProcedure [dbo].[procMove] Script Date&#58; 08/08/2008 12&#58;18&#58;33 ******/<br>SET ANSI_NULLS ON<br>GO<br>SET QUOTED_IDENTIFIER ON<br>GO<br>ALTER PROCEDURE [dbo].[procMove]<br>@id AS Char,<br>@direction AS INT<br>AS<br>IF @direction = 0<br>BEGIN<br> INSERT INTO ParaRight<br> SELECT Col1,Col2 FROM ParaLeft<br> WHERE ParaID = @id<br> DELETE FROM ParaLeft<br> WHERE ParaID = @id<br>END<br>ELSE IF @direction = 1<br>BEGIN<br> INSERT INTO ParaLeft<br> SELECT * FROM ParaRight<br> WHERE ParaID = @id<br> DELETE FROM ParaRight<br> WHERE ParaID = @id<br>END<br>ELSE BEGIN PRINT &quot;Please use a correct direction&quot;<br> END</p><dd class="ssw15-rteElement-FigureGood">Good example&#58;&#160;Using concrete columns instead of * and provide an Else section to raise errors​​<br></dd>


