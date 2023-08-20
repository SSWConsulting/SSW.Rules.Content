---
type: rule
archivedreason: 
title: Do you remove VBA function names in queries before upsizing queries (Upsizing problem)?
guid: b3b5fa0d-ec69-4767-988b-f1001a42479d
uri: do-you-remove-vba-function-names-in-queries-before-upsizing-queries-upsizing-problem
created: 2010-07-23T03:36:59.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators-or-upsizing-problem
- do-you-have-complex-queries-upsizing-problem
redirects:
- do-you-remove-vba-function-names-in-queries-before-upsizing-queries-(upsizing-problem)

---

The Upsizing Tools do not try to upsize Microsoft Access query that includes VBA function names that don't have their equivalent Transact-SQL functions. The upsizing result will depend on Microsoft Access version (2000/2002/2003) and SQL Server Version (2000/2005). The following varieties of queries will not upsize:   
<!--endintro-->

* Queries referencing value in control, for example Forms![FormName]![ControlName] (Access 2000)
* Select queries that take parameters (Access 2000)
* Select queries where parameter used more than once (All versions of Access)
* Select queries referencing Format function (All versions of Access)


You have to manually edit SQL definition in Microsoft Access (remove or replace keyword) and modify view/stored procedure/function T-SQL in SQL Server after upsizing.


```sql
SELECT Orders.OrderID,
    "Order Subtotals".Subtotal, 
     FORMAT (ShippedDate,'yyyy') AS Year 
FROM Orders 
INNER JOIN "Order Subtotals" 
    ON (Orders.OrderID="Order Subtotals".OrderID);
```



::: bad
Figure: Bad example of Access query with FORMAT keyword  
:::


```sql
SELECT Orders.OrderID,
    "Order Subtotals".Subtotal, 
     YEAR (ShippedDate) AS [Year] 
FROM Orders 
INNER JOIN "Order Subtotals" 
    ON (Orders.OrderID="Order Subtotals".OrderID)
```



::: good
Figure: Good example of SQL Server view with YEAR keyword 

:::


::: yellowBox
[Upsizing PRO](http&#58;//www.ssw.com.au/ssw/UpsizingPRO) will check this rule

:::
