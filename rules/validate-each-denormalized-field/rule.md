---
type: rule
title: Do you validate each "Denormalized Field"?
uri: validate-each-denormalized-field
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-validate-each-denormalized-field-with-procvalidate
  - schema-do-you-validate-each-denormalized-field-with-procvalidate
  - validate-each-denormalized-field-with-procvalidate
created: 2009-10-06T01:11:30.000Z
archivedreason: null
guid: f9056515-7c6c-4886-babd-a2af281c3a74
---

Ideally you should be using computed columns as per [Schema - Do you use computed columns rather than denormalized fields?](/use-computed-columns-rather-than-denormalized-fields)

Many of the databases that SSW works with make use of denormalized fields. We believe this is with good reason. However, several precautions should be taken to ensure that the data held within these fields is reliable. This is particularly the case several applications are updating your denormalized data. To illustrate, let's say that we want to show all Customers with a calculated field totalling their order amount (ie Customer.OrderTotal).

With this example in mind, the main reasons we use denormalized fields are:

<!--endintro-->

::: good
Reducing development complexity
:::

A denormalized field can mean that all SELECT queries in the database are simpler. Power users find it easier to use for reporting purposes - without the need for a cube. In our example, we would not need a large view to retrieve the data (as below).

```
SELECT 
    Customer.CustomerID, 
    SUM (SalesOrderDetail.OrderQty * 
             (SalesOrderDetail.UnitPrice - 
              SalesOrderDetail.UnitPriceDiscount)
    ) AS DetailTotal, 
    Customer.SalesPersonID, Customer.TerritoryID,
    Customer.AccountNumber, 
    Customer.CustomerType, 
    Customer.ModifiedDate, Customer.rowguid
FROM Customer 
INNER JOIN SalesOrderHeader 
    ON Customer.CustomerID = SalesOrderHeader.CustomerID
INNER JOIN SalesOrderDetail 
    ON SalesOrderHeader.SalesOrderID = 
       SalesOrderDetail.SalesOrderID
GROUP BY Customer.CustomerID, Customer.SalesPersonID, 
    Customer.TerritoryID, Customer.AccountNumber,
    Customer.CustomerType, 
    Customer.ModifiedDate,Customer.rowguid 
ORDER BY Customer.CustomerID
```
**Figure: A view to get customer totals when no denormalized fields are used**

If we had a denormalized field, the user or developer would simply have run the following query: 

```
SELECT 
    Customer.CustomerID, 
    Customer.OrderTotal AS DetailTotal 
FROM Customer 
ORDER BY Customer.CustomerID
```
**Figure: Queries are much simpler with denormalized fields**

::: greybox
**Note:** that this is not a particularly complicated example. However, you can see why it can simplify development greatly when working with a large number of tables.
:::

::: good
Performance is better for read-intensive reports
:::

Particularly when reporting on data with a cube.

::: good
When there a multiple tables in a SQL Server view
:::

They cannot be updated in one hit - they must be updated one table at a time.

::: good
It is a built-in validation device
:::

For example, if records are accidentally deleted directly in the database, there is still a validation check for the correct totals. The value of this is mitigated when there is a full audit log on the database

However, there are reasons against using denormalized fields:

::: bad
They have to be maintained and can potentially get out of synch
:::
 
This can make them unreliable - particularly if several applications are incorrectly updating the denormalized fields. UPDATE, INSERT, DELETEs are more complicated as they have to update the denormalized fields

::: bad
They can be seen as an unnecessary waste of space
:::

All in all, we choose to still use denormalized fields because they can save development time. We do this with some provisos. In particular, they must be validated correctly to ensure the integrity of the data.

Here is how we ensure that this data is validated:

1. Change the description on any denormalized fields to include "Denormalized" in the description - "Denormalized: Sum(OrderTotal) FROM Orders" in description in SQL Server Management Studio.
2. Create a view that lists all the denormalized fields in the database - based on the description field. 

  ```
  CREATE VIEW dbo.vwValidateDenormalizedFields
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
  ```
  **Figure: Standard view for validation of a denormalized field**

3. Create a stored procedure (based on the above view) that validates whether all denormalized fields have a stored procedure that validates the data within them 

  ```
  CREATE PROCEDURE procValidateDenormalizedFieldValidators
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
  ```
  **Figure: Standard stored procedure for validation of a denormalized field**

If you want to know how to implement denormalized fields, see our rule [Do you use triggers for denormalized fields?](/use-triggers-for-denormalized-fields)
