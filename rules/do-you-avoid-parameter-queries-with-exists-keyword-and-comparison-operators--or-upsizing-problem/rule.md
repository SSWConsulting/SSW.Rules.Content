---
type: rule
title: Do you avoid parameter queries with EXISTS keyword and comparison operators (<> or =)(Upsizing Problem)?
uri: do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators--or-upsizing-problem
created: 2010-07-23T03:28:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <pre class="ms-rteCustom-CodeArea">PARAMETERS [@Employee Last Name] Text ( 20 );    
SELECT Orders.OrderID
, Orders.CustomerID
, Orders.EmployeeID
FROM Orders
WHERE EXISTS (SELECT EmployeeID
 FROM Employees 
 WHERE LastName= [@Employee Last Name] 
 AND Employees.EmployeeID=Orders.EmployeeID) &lt;&gt; FALSE</pre>
<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad example of Access query with EXISTS keyword and comparison operator </font>
<pre class="ms-rteCustom-CodeArea">PARAMETERS [@Employee Last Name] Text ( 20 ); 
SELECT Orders.OrderID
, Orders.CustomerID
, Orders.EmployeeID
<br>FROM Orders
<br>WHERE EXISTS (SELECT EmployeeID 
 FROM Employees
<br> WHERE LastName= [@Employee Last Name] 
 AND Employees.EmployeeID=Orders.EmployeeID)</pre>
<font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good example of Access query with EXISTS keyword and without comparison operator</font>In order to get the good example syntax you must switch from Design View window to SQL View in query designer window and save query definition.



