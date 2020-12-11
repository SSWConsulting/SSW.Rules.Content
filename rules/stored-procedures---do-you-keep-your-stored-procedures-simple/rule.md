---
type: rule
archivedreason: 
title: Stored Procedures - Do you keep your Stored Procedures simple?
guid: 89c2edec-cd84-4ac4-babd-f501fc54ce40
uri: stored-procedures---do-you-keep-your-stored-procedures-simple
created: 2019-11-12T22:31:13.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

If you are using the .NET Framework, put validation and defaults in the middle tier. The backend should have the required fields (Allow Nulls = False), but no complicated constraints. The following are examples that work with the Products table (with an added timestamp field called Concurrency) from Northwind.

<!--endintro-->

### 1. Code: Select Procedure


ALTER PROCEDURE dbo.ProductSelect
@ProductID int
AS
SELECT ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,
UnitsOnOrder, ReorderLevel, Discontinued, Concurrency
FROM Products
WHERE (ProductID= @ProductID)

### 2. Code: Insert Procedure

ALTER PROCEDURE dbo.ProductInsert
@ProductName nvarchar(40),
@SupplierID int,
@CategoryID int,
@QuantityPerUnit nvarchar(20),
@UnitPrice money,
@UnitsInStock smallint,
@UnitsOnOrder smallint,
@ReorderLevel smallint,
@Discontinued bit
AS
INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice,
UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES (@ProductName, @SupplierID, @CategoryID, @QuantityPerUnit, @UnitPrice, @UnitsInStock,
@UnitsOnOrder, @ReorderLevel, @Discontinued, 1)
SELECT Scope\_Identity() AS [SCOPE\_IDENTITY] --If table has identity column
--SELECT @@ROWCOUNT --If table doesn't have identity column
-- Note: The middle tier must check the ROWCOUNT = 1

### 3.Code: Update Procedure


ALTER PROCEDURE dbo.ProductUpdate 
@ProductID int, 
@ProductName nvarchar(40), 
@SupplierID int, 
@CategoryID int, 
@QuantityPerUnit nvarchar(20), 
@UnitPrice money, 
@UnitsInStock smallint, 
@UnitsOnOrder smallint, 
@ReorderLevel smallint, 
@Discontinued bit, 
@Concurrency timestamp 
UPDATE Products 
SET ProductName = @ProductName,
SupplierID = @SupplierID,
CategoryID = @CategoryID,
QuantityPerUnit = @QuantityPerUnit,
UnitPrice = @UnitPrice,
UnitsInStock = @UnitsInStock,
UnitsOnOrder = @UnitsOnOrder,
ReorderLevel = @ReorderLevel,
Discontinued = @Discontinued
WHERE (Concurrency = @Concurrency) AND (ProductID= @ProductID) --Note the double criteria to ensure concurrency 
SELECT @@ROWCOUNT 
-- Note: The middle tier must check the ROWCOUNT = 1

### 4.Code: Delete Procedure


ALTER PROCEDURE dbo.ProductDelete 
@ProductID int, 
@Concurrency timestamp 
AS 
DELETE FROM Products 
WHERE (ProductID= @ProductID) AND (Concurrency = @Concurrency)
--Note the double criteria to ensure concurrency 
SELECT @@ROWCOUNT 
--Note: The middle tier must check the ROWCOUNT = 1
