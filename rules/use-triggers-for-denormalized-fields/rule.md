---
type: rule
archivedreason: 
title: Schema - Do you use triggers for denormalized fields?
guid: 4385ff40-f78d-4d6d-8328-604927b807a8
uri: use-triggers-for-denormalized-fields
created: 2019-11-06T18:13:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-triggers-for-denormalized-fields

---


<p>Ideally you should be using computed columns as per&#160;<a>https&#58;//rules.ssw.com.au/use-computed-columns-rather-than-denormalized-fields​</a><br></p><p>​​You can also have a denormalized field that is manually updated.&#160; This should be the exception and not the rule.&#160;&#160;When used properly and sparingly, they can actually improve your application's performance. As an example&#58;<br></p><ul><li>You have an Orders table containing one record per order</li><li>You also have an OrderItems table which contains line items linked to the main OrderID, as well as subtotals for each line item</li><li>In your&#160;front end,​ you&#160;have a report showing the total for each order​<br></li></ul>
<br><excerpt class='endintro'></excerpt><br>
<p>To generate this report, you&#160;can either&#58;</p><ol><li>Calculate the Order total by summing up every single line item for the selected Order every time the report is loaded, or</li><li>Store the Order subtotal as a de-normalised field in the Orders table which gets updated using trigger.</li></ol><p>The second option will save me an expensive JOIN query each time because you​&#160;can just tack the denormalised field onto the end of my SELECT query.<br></p><p>​1.&#160;Code&#58; Alter Orders table​<br></p><p class="ssw15-rteElement-CodeArea">ALTER TABLE Orders<br>ADD SumOfOrderItems money NULL<br></p><p></p>				<br>2. Code&#58; Insert trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger tri_SumOfOrderItems<br>On dbo.OrderItems<br>For Insert<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID from inserted<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems + <br>(SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)<br>WHERE Orders.OrderID = @OrderID</p>				<br>3. Code&#58; Update trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger tru_SumOfOrderItems<br>On dbo.OrderItems<br>For Update<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID from deleted<br>--Could have used inserted table<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems<br>+ (SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)<br>- (SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID) <br>WHERE Orders.OrderID = @OrderID</p>4. Code&#58; Delete trigger<p class="ssw15-rteElement-CodeArea">Alter Trigger trd_SumOfOrderItems<br>On dbo.OrderItems<br>For Delete<br>AS<br>DECLARE @OrderID varchar (5)<br>SELECT @OrderID = OrderID FROM deleted<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Orders.SumOfOrderItems - <br>	(SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID)<br>WHERE Orders.OrderID = @OrderID</p>5. Code&#58; Maintenance stored procedure<p class="ssw15-rteElement-CodeArea">--Stored Procedure for Maintenance<br>Alter Procedure dt_Maintenance_SumOfItemValue<br>As<br>UPDATE Orders<br>SET Orders.SumOfOrderItems = Isnull((SELECT SUM (ItemValue) FROM OrderItems WHERE OrderItems.OrderID = Orders.OrderID),0)<br></p><p></p>


