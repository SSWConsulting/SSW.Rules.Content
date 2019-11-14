

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">The reason is that you avoid ownership chain problems. Where Mary owns an object, Fred can read the object and then he creates a proc and he gives permission to Tom to execute. But Tom cant because there is a product chain of ownership.​​​​<br></p> </span>

<p class="ssw15-rteElement-CodeArea">CREATE PROCEDURE [Adam Cogan].[Sales by Year]<br><br>@Beginning_Date DateTime,<br><br>@Ending_Date DateTime AS<br><br>SELECT Orders.ShippedDate<br><br>,Orders.OrderID<br><br>,&quot;vwOrderSubTotals&quot;.Subtotal<br><br>,DATENAME(yy,ShippedDate) AS Year<br><br>FROM Orders<br><br>INNER JOIN &quot;vwOrderSubTotals&quot;<br><br>ON Orders.OrderID = &quot;vwOrderSubTotals&quot;.OrderID<br><br>WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example​<br></dd><p class="ssw15-rteElement-CodeArea">CREATE PROCEDURE [dbo].[Sales by Year]<br><br> @Beginning_Date DateTime,<br><br> @Ending_Date DateTime AS<br><br> SELECT Orders.ShippedDate<br><br> ,Orders.OrderID<br><br> ,&quot;vwOrderSubTotals&quot;.Subtotal<br><br> ,DATENAME(yy,ShippedDate) AS Year<br><br> FROM Orders<br><br> INNER JOIN &quot;vwOrderSubTotals&quot;<br><br> ON Orders.OrderID = &quot;vwOrderSubTotals&quot;.OrderID<br><br> WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example​​​<br></dd><p><br></p>


