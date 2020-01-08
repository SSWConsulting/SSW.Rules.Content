---
type: rule
title: Schema - Do you validate each "Denormalized Field" with procValidate?
uri: schema---do-you-validate-each-denormalized-field-with-procvalidate
created: 2009-10-06T01:11:30.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​​​90% of the databases that SSW works with make use of denormalized fields. We believe this is with good reason. However, several precautions should be taken to ensure that the data held within these fields is reliable. This is particularly the case several applications are updating your denormalized data. To illustrate, let's say that we want to show all Customers with a calculated field totalling their order amount (ie Customer.OrderTotal). <br></p>
<p>With this example in mind, the main reasons we use denormalized fields are&#58; </p> </span>

<blockquote dir="ltr" style="margin-right&#58;0px;"><blockquote dir="ltr" style="margin-right&#58;0px;"><p>&#160;</p></blockquote></blockquote>
<font class="ms-rteCustom-FigureGood" size="2"><font size="2">Reducing development complexity</font> </font><p>A denormalized field can mean that all SELECT queries in the database are simpler. Power users find it easier to use for reporting purposes - without the need for a cube. In our example, we would not need a large view to retrieve the data (as below). </p>
<dl class="image"><dt><font class="ms-rteCustom-CodeArea" size="+0"><pre>SELECT <br>    Customer.CustomerID, 
    SUM (SalesOrderDetail.OrderQty * 
             (SalesOrderDetail.UnitPrice - 
              SalesOrderDetail.UnitPriceDiscount)
    ) AS DetailTotal, 
    Customer.SalesPersonID, Customer.TerritoryID,
    Customer.AccountNumber, 
    Customer.CustomerType, 
    Customer.ModifiedDate, Customer.rowguid
FROM Customer <br>INNER JOIN SalesOrderHeader 
    ON Customer.CustomerID = SalesOrderHeader.CustomerID
INNER JOIN SalesOrderDetail 
    ON SalesOrderHeader.SalesOrderID = 
       SalesOrderDetail.SalesOrderID
GROUP BY Customer.CustomerID, Customer.SalesPersonID, 
    Customer.TerritoryID, Customer.AccountNumber,
    Customer.CustomerType, 
    Customer.ModifiedDate,Customer.rowguid 
ORDER BY Customer.CustomerID</pre></font></dt>
<dd>Figure&#58; A view to get customer totals when no denormalized fields are used </dd></dl>
If we had a denormalized field, the user or developer would simply have run the following query&#58; <dl class="image"><dt><font class="ms-rteCustom-CodeArea" size="+0"><pre>SELECT <br>    Customer.CustomerID, <br>    Customer.OrderTotal AS DetailTotal 
FROM Customer 
ORDER BY Customer.CustomerID</pre></font></dt>
<dd>Figure&#58; Queries are much simpler with denormalized fields </dd></dl>
<p>Note that this is not a particularly complicated example. However, you can see why it can simplify development greatly when working with a large number of tables</p>
<p><font class="ms-rteCustom-FigureGood" size="2"><font size="2">Performance is better for read-intensive reports</font><br></font>Particularly when reporting on data with a cube. </p>
<p><font class="ms-rteCustom-FigureGood" size="2"><font size="2">When there a multiple tables in a SQL Server view</font> </font>They cannot be updated in one hit - they must be updated one table at a time.&#160;&#160;</p>
<p><font class="ms-rteCustom-FigureGood" size="2"><font size="2">It is a built-in validation device</font></font> For example, if records are accidentally deleted directly in the database, there is still a validation check for the correct totals. The value of this is mitigated when there is a full audit log on the database </p>
<p>However, there are reasons against using denormalized fields </p>
<font class="ms-rteCustom-FigureBad" size="2"><font size="2">They have to be maintained and can potentially get out of synch</font></font> <p>This can make&#160;them unreliable - particularly if several applications are incorrectly updating the denormalized fields. UPDATE, INSERT, DELETEs are more complicated as they have to update the denormalized fields </p>
<font class="ms-rteCustom-FigureBad" size="2"><font size="2">They can be seen as an unnecessary waste of space</font></font> <p>All in all, we choose to still use denormalized fields because they can save development time. We do this with some provisos. In particular, they must be validated correctly to ensure the integrity of the data. </p>
<p>Here is how we ensure that this data is validated&#58; </p>
<ol><li>Change the description on any denormalized fields to include &quot;Denormalized&quot; in the description - &quot;Denormalized&#58; Sum(OrderTotal) FROM Orders&quot; in description in SQL Server Management Studio.<br></li>
<li>Create a view that lists all the denormalized fields in the database - based on the description field. <dl class="image"><dt><font class="ms-rteCustom-CodeArea" size="+0"><pre>CREATE VIEW dbo.vwValidateDenormalizedFields
AS
    SELECT OBJECT_NAME(id) AS TableName, 
        COL_NAME(id, smallid) AS ColumnName,
        CAST([value] AS VARCHAR(8000)) AS Description,
        'procValidate_' + OBJECT_NAME(id) + 
        '_' + COL_NAME(id, smallid) as
        ValidationProcedureName
    FROM dbo.sysproperties
    WHERE (name = 'MS_Description') AND 
                 (CAST([value] AS VARCHAR(8000))
                  LIKE '%Denormalized&#58;%')
</pre></font></dt>
<dd>Figure&#58; Standard view for validation of a denormalized field </dd></dl></li>
<li>Create a stored procedure (based on the above view) that validates whether all denormalized fields have a stored procedure that validates the data within them <dl class="image"><dt><font class="ms-rteCustom-CodeArea" size="+0"><pre>CREATE PROCEDURE procValidateDenormalizedFieldValidators
AS
    SELECT 
        ValidationProcedureName AS
        MissingValidationProcedureName 
    FROM vwValidateDenormalizedFields
    WHERE ValidationProcedureName NOT IN
    (
        SELECT ValidationProcedureName
        FROM vwValidateDenormalizedFields AS vw
        LEFT JOIN sysobjects 
        ON 
            vw.ValidationProcedureName = 
            OBJECT_NAME(sysobjects.id)
        WHERE id IS NOT NULL
    )
</pre></font></dt>
<dd>Figure&#58; Standard stored procedure for validation of a&#160;denormalized field </dd></dl></li></ol>
If you want to know how to implement denormalized fields, see our rules <a href="http&#58;//www.ssw.com.au/ssw/standards/rules/rulestobettersqlserverdatabases.aspx#triggersdenormalized">Do you use triggers for denormalized fields?</a> 


