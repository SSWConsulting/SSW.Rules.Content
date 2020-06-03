---
type: rule
title: Do you remove VBA function names in queries before upsizing queries (Upsizing problem)?
uri: do-you-remove-vba-function-names-in-queries-before-upsizing-queries-upsizing-problem
created: 2010-07-23T03:36:59.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> The Upsizing Tools do not try to upsize Microsoft Access query that includes VBA function names that don't have their equivalent Transact-SQL functions. The upsizing result will depend on Microsoft Access version (2000/2002/2003) and SQL Server Version (2000/2005). The following varieties of queries will not upsize&#58; 
 </span>


  <ul>
    <li>Queries referencing value in control, for example Forms![FormName]![ControlName] (Access 2000) </li>
    <li>Select queries that take parameters (Access 2000) </li>
    <li>Select queries where parameter used more than once (All versions of Access) </li>
    <li>Select queries referencing Format function (All versions of Access) </li>
</ul>
<p>You have to manually edit SQL definition in Microsoft Access (remove or replace keyword) and modify view/stored procedure/function T-SQL in SQL Server after upsizing.</p>
<pre class="ms-rteCustom-CodeArea">SELECT Orders.OrderID,
    &quot;Order Subtotals&quot;.Subtotal, 
    <b>FORMAT</b>(ShippedDate,'yyyy') AS Year 
FROM Orders 
INNER JOIN &quot;Order Subtotals&quot; 
    ON (Orders.OrderID=&quot;Order Subtotals&quot;.OrderID);</pre>
<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad example of Access query with FORMAT keyword</font>
<pre class="ms-rteCustom-CodeArea">SELECT Orders.OrderID,
    &quot;Order Subtotals&quot;.Subtotal, 
    <b>YEAR</b>(ShippedDate) AS [Year] 
FROM Orders 
INNER JOIN &quot;Order Subtotals&quot; 
    ON (Orders.OrderID=&quot;Order Subtotals&quot;.OrderID)</pre>
<font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good example of SQL Server view with YEAR keyword <br>
</font><font class="ms-rteCustom-YellowBorderBox" size="+0"><a href="http&#58;//www.ssw.com.au/ssw/UpsizingPRO">Upsizing PRO</a> will check this rule<br>
</font>



