---
type: rule
archivedreason: 
title: General - Do you know every object name should be owned by dbo?
guid: 5b2a72df-2ed7-42d4-95be-eb996e12d845
uri: every-object-name-should-be-owned-by-dbo
created: 2019-11-14T21:51:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- sql-stored-procedure-names-should-be-prefixed-with-the-owner
redirects:
- general-do-you-know-every-object-name-should-be-owned-by-dbo

---


<p class="ssw15-rteElement-P">​​The reason is that you avoid ownership chain problems. Where Mary owns an object, Fred can read the object and then he creates a proc and he gives permission to Tom to execute. But Tom cannot because there is a product chain of ownership.​​​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">CREATE PROCEDURE [Adam Cogan].[Sales by Year]<br><br>@Beginning_Date DateTime,<br><br>@Ending_Date DateTime AS<br><br>SELECT Orders.ShippedDate<br><br>,Orders.OrderID<br><br>,&quot;vwOrderSubTotals&quot;.Subtotal<br><br>,DATENAME(yy,ShippedDate) AS Year<br><br>FROM Orders<br><br>INNER JOIN &quot;vwOrderSubTotals&quot;<br><br>ON Orders.OrderID = &quot;vwOrderSubTotals&quot;.OrderID<br><br>WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example​<br></dd><p class="ssw15-rteElement-CodeArea">CREATE PROCEDURE [dbo].[Sales by Year]<br><br> @Beginning_Date DateTime,<br><br> @Ending_Date DateTime AS<br><br> SELECT Orders.ShippedDate<br><br> ,Orders.OrderID<br><br> ,&quot;vwOrderSubTotals&quot;.Subtotal<br><br> ,DATENAME(yy,ShippedDate) AS Year<br><br> FROM Orders<br><br> INNER JOIN &quot;vwOrderSubTotals&quot;<br><br> ON Orders.OrderID = &quot;vwOrderSubTotals&quot;.OrderID<br><br> WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good E​​​xample​​​<br></dd><p><br></p>


