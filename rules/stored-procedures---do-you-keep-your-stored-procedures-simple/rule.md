

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> If you are using the .NET Framework, put validation and defaults in the middle tier. The backend should have the required fields (Allow Nulls = False), but no complicated constraints. The following are examples that work with the Products table (with an added timestamp field called Concurrency) from Northwind.<br> </span>

<h3 class="ssw15-rteElement-H3">​1.&#160;Code&#58; Select Procedure​​​<br></h3><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE dbo.ProductSelect<br>@ProductID int<br>AS<br>SELECT ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,<br>UnitsOnOrder, ReorderLevel, Discontinued, Concurrency<br>FROM Products<br>WHERE (ProductID= @ProductID)</p><h3 class="ssw15-rteElement-H3">2. ​​Code&#58; Insert Procedure​</h3><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE dbo.ProductInsert<br>@ProductName nvarchar(40),<br>@SupplierID int,<br>@CategoryID int,<br>@QuantityPerUnit nvarchar(20),<br>@UnitPrice money,<br>@UnitsInStock smallint,<br>@UnitsOnOrder smallint,<br>@ReorderLevel smallint,<br>@Discontinued bit<br>AS<br>INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice,<br>UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)<br>VALUES (@ProductName, @SupplierID, @CategoryID, @QuantityPerUnit, @UnitPrice, @UnitsInStock,<br>@UnitsOnOrder, @ReorderLevel, @Discontinued, 1)<br>SELECT Scope_Identity() AS [SCOPE_IDENTITY] --If table has identity column<br>--SELECT @@ROWCOUNT --If table doesn't have identity column<br>-- Note&#58; The middle tier must check the ROWCOUNT = 1</p><h3 class="ssw15-rteElement-H3">3.Code&#58; Update Procedure​​<br></h3><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE dbo.ProductUpdate <br>@ProductID int, <br>@ProductName nvarchar(40), <br>@SupplierID int, <br>@CategoryID int, <br>@QuantityPerUnit nvarchar(20), <br>@UnitPrice money, <br>@UnitsInStock smallint, <br>@UnitsOnOrder smallint, <br>@ReorderLevel smallint, <br>@Discontinued bit, <br>@Concurrency timestamp <br>UPDATE Products <br>SET ProductName = @ProductName,<br>SupplierID = @SupplierID,<br>CategoryID = @CategoryID,<br>QuantityPerUnit = @QuantityPerUnit,<br>UnitPrice = @UnitPrice,<br>UnitsInStock = @UnitsInStock,<br>UnitsOnOrder = @UnitsOnOrder,<br>ReorderLevel = @ReorderLevel,<br>Discontinued = @Discontinued<br>WHERE (Concurrency = @Concurrency) AND (ProductID= @ProductID) --Note the double criteria to ensure concurrency <br>SELECT @@ROWCOUNT <br>-- Note&#58; The middle tier must check the ROWCOUNT = 1</p><h3 class="ssw15-rteElement-H3">4.Code&#58; Delete Procedure​<br></h3><p class="ssw15-rteElement-CodeArea">ALTER PROCEDURE dbo.ProductDelete <br>@ProductID int, <br>@Concurrency timestamp <br>AS <br>DELETE FROM Products <br>WHERE (ProductID= @ProductID) AND (Concurrency = @Concurrency)<br>--Note the double criteria to ensure concurrency <br>SELECT @@ROWCOUNT <br>--Note&#58; The middle tier must check the ROWCOUNT = 1​​<br></p>


