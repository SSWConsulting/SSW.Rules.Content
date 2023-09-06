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

The reason is that you avoid ownership chain problems. Where Mary owns an object, Fred can read the object and then he creates a proc and he gives permission to Tom to execute. But Tom cannot because there is a product chain of ownership.

<!--endintro-->

```sql
CREATE PROCEDURE [Adam Cogan].[Sales by Year]

@Beginning_Date DateTime,

@Ending_Date DateTime AS

SELECT Orders.ShippedDate

,Orders.OrderID

,"vwOrderSubTotals".Subtotal

,DATENAME(yy,ShippedDate) AS Year

FROM Orders

INNER JOIN "vwOrderSubTotals"

ON Orders.OrderID = "vwOrderSubTotals".OrderID

WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date
```

::: bad
Figure: Bad Example

:::

```sql
CREATE PROCEDURE [dbo].[Sales by Year]

 @Beginning_Date DateTime,

 @Ending_Date DateTime AS

 SELECT Orders.ShippedDate

 ,Orders.OrderID

 ,"vwOrderSubTotals".Subtotal

 ,DATENAME(yy,ShippedDate) AS Year

 FROM Orders

 INNER JOIN "vwOrderSubTotals"

 ON Orders.OrderID = "vwOrderSubTotals".OrderID

 WHERE Orders.ShippedDate Between @Beginning_Date And @Ending_Date
```

::: good
Figure: Good Example

:::
