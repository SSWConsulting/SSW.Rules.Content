/*
   Thursday, 8 October 20098:09:41 PM
   User: 
   Server: .
   Database: Northwind
   Application: 
*/

/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/

/***********/
/*ATTENTION*/
/*Need to input data - char(2) into Gender field*/
/***********/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.Tmp_Employees
	(
	EmployeeID int NOT NULL IDENTITY (1, 1),
	LastName nvarchar(20) NOT NULL,
	FirstName nvarchar(10) NOT NULL,
	Title nvarchar(30) NULL,
	BirthDate datetime NULL,
	StartDate datetime NULL,
	Address nvarchar(60) NULL,
	City nvarchar(15) NULL,
	Region nvarchar(15) NULL,
	PostalCode nvarchar(10) NULL,
	Country nvarchar(15) NULL,
	HomePhone nvarchar(24) NULL,
	Extension nvarchar(4) NULL,
	Photo image NULL,
	Notes ntext NULL,
	ReportsTo int NULL,
	PhotoPath nvarchar(255) NULL,
	Gender int NULL
	)  ON [PRIMARY]
	 TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE dbo.Tmp_Employees SET (LOCK_ESCALATION = TABLE)
GO
SET IDENTITY_INSERT dbo.Tmp_Employees ON
GO
IF EXISTS(SELECT * FROM dbo.Employees)
	 EXEC('INSERT INTO dbo.Tmp_Employees (EmployeeID, LastName, FirstName, Title, BirthDate, StartDate, Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, ReportsTo, PhotoPath, Gender)
		SELECT EmployeeID, LastName, FirstName, Title, BirthDate, StartDate, Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes, ReportsTo, PhotoPath, 
		CASE Gender WHEN ''F'' THEN ''0'' 
					WHEN ''M'' THEN ''1''
					WHEN ''NA'' THEN ''2''
					WHEN ''U'' THEN ''3''
					ELSE ''-1''
		END AS Gender FROM dbo.Employees WITH (HOLDLOCK TABLOCKX)')
GO
SET IDENTITY_INSERT dbo.Tmp_Employees OFF
GO
ALTER TABLE dbo.Employees
	DROP CONSTRAINT FK_Employees_Employees
GO
ALTER TABLE dbo.EmployeeTerritories
	DROP CONSTRAINT FK_EmployeeTerritories_Employees
GO
ALTER TABLE dbo.Orders
	DROP CONSTRAINT FK_Orders_Employees
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', N'Employees', 'OBJECT' 
GO
ALTER TABLE dbo.Employees ADD CONSTRAINT
	PK_Employees PRIMARY KEY CLUSTERED 
	(
	EmployeeID
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
CREATE NONCLUSTERED INDEX LastName ON dbo.Employees
	(
	LastName
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX PostalCode ON dbo.Employees
	(
	PostalCode
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE dbo.Employees WITH NOCHECK ADD CONSTRAINT
	CK_Birthdate CHECK (([BirthDate]<getdate()))
GO
ALTER TABLE dbo.Employees WITH NOCHECK ADD CONSTRAINT
	FK_Employees_Employees FOREIGN KEY
	(
	ReportsTo
	) REFERENCES dbo.Employees
	(
	EmployeeID
	) ON UPDATE  NO ACTION 
	 ON DELETE  NO ACTION 
	
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Employees', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Employees', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Employees', 'Object', 'CONTROL') as Contr_Per BEGIN TRANSACTION
GO
ALTER TABLE dbo.Orders WITH NOCHECK ADD CONSTRAINT
	FK_Orders_Employees FOREIGN KEY
	(
	EmployeeID
	) REFERENCES dbo.Employees
	(
	EmployeeID
	) ON UPDATE  NO ACTION 
	 ON DELETE  NO ACTION 
	
GO
ALTER TABLE dbo.Orders SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Orders', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Orders', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Orders', 'Object', 'CONTROL') as Contr_Per BEGIN TRANSACTION
GO
ALTER TABLE dbo.EmployeeTerritories ADD CONSTRAINT
	FK_EmployeeTerritories_Employees FOREIGN KEY
	(
	EmployeeID
	) REFERENCES dbo.Employees
	(
	EmployeeID
	) ON UPDATE  NO ACTION 
	 ON DELETE  NO ACTION 
	
GO
ALTER TABLE dbo.EmployeeTerritories SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.EmployeeTerritories', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.EmployeeTerritories', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.EmployeeTerritories', 'Object', 'CONTROL') as Contr_Per 