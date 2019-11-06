---
type: rule
title: Schema - Do you use triggers for denormalized fields?
uri: schema---do-you-use-triggers-for-denormalized-fields
created: 2019-11-06T18:13:04.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>I believe that de-normalised fields are not a bad thing. When used properly and sparingly, they can actually improve your application's performance. As an example&#58;</p><ul><li>I have an Orders table containing one record per order</li><li>I also have an OrderItems table which contains line items linked to the main OrderID, as well as subtotals for each line item</li><li>In my front end I have a report showing the total for each order​<br></li></ul> </span>

<p>To generate this report, I can either&#58;</p><ol><li>Calculate the Order total by summing up every single line item for the selected Order every time the report is loaded, or</li><li>Store the Order subtotal as a de-normalised field in the Orders table which gets updated using trigger.</li></ol><p>The second option will save me an expensive JOIN query each time because I can just tack the denormalised field onto the end of my SELECT query.<br></p><p>​1.&#160;Code&#58; Alter Orders table​<br></p><p class="ssw15-rteElement-CodeArea">ALTER TABLE Orders<br>ADD SumOfOrderItems money NULL<br></p><p></p>    <br>2. Code&#58; Insert trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger tri_SumOfOrderItems<br>On dbo.OrderItems<br>For Insert<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID from inserted<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems + <br>(SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)<br>WHERE Orders.OrderID = @OrderID</p>    <br>3. Code&#58; Update trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger tru_SumOfOrderItems<br>On dbo.OrderItems<br>For Update<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID from deleted<br>--Could have used inserted table<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems<br>+ (SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)<br>- (SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID) <br>WHERE Orders.OrderID = @OrderID</p>4. Code&#58; Delete trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger trd_SumOfOrderItems<br>On dbo.OrderItems<br>For Delete<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID FROM deleted<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems - <br> (SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID)<br>WHERE Orders.OrderID = @OrderID</p>5. Code&#58; Maintenance stored procedure<p class="ssw15-rteElement-CodeArea">--Stored Procedure for Maintenance<br>Alter Procedure dt_Maintenance_SumOfItemValue<br>As<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Isnull((SELECT SUM (ItemValue) FROM OrderItems WHERE OrderItems.OrderID = Orders.OrderID),0)<br></p><p></p>


