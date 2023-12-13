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

Ideally you should be using computed columns as per [Do you use computed columns rather than denormalized fields?](/use-computed-columns-rather-than-denormalized-fields)

You can also have a denormalized field that is manually updated. This should be the exception and not the rule.  When used properly and sparingly, they can actually improve your application's performance.

<!--endintro-->

As an example:

* You have an Orders table containing one record per order
* You also have an OrderItems table which contains line items linked to the main OrderID, as well as subtotals for each line item
* In your front end, you have a report showing the total for each order

To generate this report, you can either:

1. Calculate the Order total by summing up every single line item for the selected Order every time the report is loaded, or
2. Store the Order subtotal as a de-normalised field in the Orders table which gets updated using trigger.

The second option will save me an expensive JOIN query each time because you can just tack the denormalised field onto the end of my SELECT query.

1. Code: Alter Orders table

```sql
ALTER TABLE Orders
ADD SumOfOrderItems money NULL
```

2. Code: Insert trigger

```sql
Alter Trigger tri_SumOfOrderItems
On dbo.OrderItems
For Insert
AS
DECLARE @OrderID varchar (5)
SELECT @OrderID = OrderID from inserted
UPDATE Orders
SET Orders.SumOfOrderItems = Orders.SumOfOrderItems + 
(SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)
WHERE Orders.OrderID = @OrderID
```

3. Code: Update trigger

```sql
Alter Trigger tru_SumOfOrderItems
On dbo.OrderItems
For Update
AS
DECLARE @OrderID varchar (5)
SELECT @OrderID = OrderID from deleted
--Could have used inserted table
UPDATE Orders
SET Orders.SumOfOrderItems = Orders.SumOfOrderItems
+ (SELECT isnull(SUM(ItemValue),0) FROM inserted WHERE inserted.OrderID = Orders.OrderID)
- (SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID) 
WHERE Orders.OrderID = @OrderID
```

4. Code: Delete trigger

```sql
Alter Trigger trd_SumOfOrderItems
On dbo.OrderItems
For Delete
AS
DECLARE @OrderID varchar (5)
SELECT @OrderID = OrderID FROM deleted
UPDATE Orders
SET Orders.SumOfOrderItems = Orders.SumOfOrderItems - 
(SELECT isnull(SUM(ItemValue),0) FROM deleted WHERE deleted.OrderID = Orders.OrderID)
WHERE Orders.OrderID = @OrderID
```

5. Code: Maintenance stored procedure

```sql
--Stored Procedure for Maintenance
Alter Procedure dt_Maintenance_SumOfItemValue
As
UPDATE Orders
SET Orders.SumOfOrderItems = Isnull((SELECT SUM (ItemValue) FROM OrderItems WHERE OrderItems.OrderID = Orders.OrderID),0)
```
