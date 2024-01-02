---
type: rule
archivedreason: 
title: Do you avoid parameter queries with EXISTS keyword and comparison operators (<> or =)(Upsizing Problem)?
guid: 1d25cc5a-91af-45c8-9b97-5ac6055364d1
uri: do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators-or-upsizing-problem
created: 2010-07-23T03:28:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-have-complex-queries-upsizing-problem
- do-you-remove-vba-function-names-in-queries-before-upsizing-queries-upsizing-problem
redirects:
- do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators-(-or-)(upsizing-problem)

---

The MS Upsizing Wizard cannot upsize Microsoft Access queries containing:

* EXISTS &lt;&gt; FALSE/TRUE or
* EXISTS = FALSE/TRUE


For example, the following query will not be upsized:

<!--endintro-->

```sql
PARAMETERS [@Employee Last Name] Text ( 20 );    
SELECT Orders.OrderID
, Orders.CustomerID
, Orders.EmployeeID
FROM Orders
WHERE EXISTS (SELECT EmployeeID
 FROM Employees 
 WHERE LastName= [@Employee Last Name] 
 AND Employees.EmployeeID=Orders.EmployeeID) <> FALSE
```

::: bad
Figure: Bad example - Access query with EXISTS keyword and comparison operator  
:::

```sql
PARAMETERS [@Employee Last Name] Text ( 20 ); 
SELECT Orders.OrderID
, Orders.CustomerID
, Orders.EmployeeID

FROM Orders

WHERE EXISTS (SELECT EmployeeID 
 FROM Employees

 WHERE LastName= [@Employee Last Name] 
 AND Employees.EmployeeID=Orders.EmployeeID)
```

::: good
Figure: Good example - Access query with EXISTS keyword and without comparison operator  
:::

In order to get the good example syntax you must switch from Design View window to SQL View in query designer window and save query definition.
