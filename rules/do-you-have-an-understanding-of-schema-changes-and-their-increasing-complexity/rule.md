---
type: rule
title: Do you have an understanding of 'schema changes' and their increasing
  complexity?
uri: do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2009-10-06T23:32:50.000Z
archivedreason: null
guid: 634434fa-12e0-4eed-9514-eaf4fb2fcc01
---

Do you dream to be a 'Schema Master' one day? If so you need to know what changes are low impact and what needs to be done with care. Take care when it involves existing data. Do you know what the hard ones are?

 Let's look at examples of this increasing complexity (As per the Northwind sample database: [Do you know the best sample applications?](/the-best-sample-applications)):
<!--endintro-->

```sql
ALTER TABLE dbo.Employees
    ADD Gender bit NOT NULL
GO
```

**Figure: Add a column (Easy)**

```sql
ALTER TABLE dbo.Employees
    DROP COLUMN TitleOfCourtesy
GO
```

**Figure: Delete a column (Easy)**

```sql
EXECUTE sp_rename N'dbo.Employees.HireDate', 
                  N'Tmp_StartDate_1', 'COLUMN'
GO
EXECUTE sp_rename N'dbo.Employees.Tmp_StartDate_1', 
                  N'StartDate', 'COLUMN'
GO
```

**Figure: Rename a column (Medium)**

```sql
CREATE TABLE dbo.Tmp_Employees
(
    ...
    Gender char(2) NULL,
    ...
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
...
IF EXISTS(SELECT * FROM dbo.Employees)
    EXEC('INSERT INTO dbo.Tmp_Employees (..., Gender,...)
              SELECT ...,Gender ,... 
              FROM dbo.Employees WITH (HOLDLOCK TABLOCKX)
              ') 
...
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', 
                  N'Employees', 'OBJECT'
GO
```

**Figure: Change data type (Hard) e.g. Bit to Integer. The above is abbreviated, see [the full .SQL file](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity/EmployeesBitToInt.sql)**

```sql
CREATE TABLE dbo.Tmp_Employees
(
    ...
    Gender int NULL,
    ...
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
...
IF EXISTS(SELECT * FROM dbo.Employees)
    EXEC('INSERT INTO dbo.Tmp_Employees (..., Gender,...)
          SELECT ...,CASE Gender WHEN ''F'' THEN ''0'' 
                                 WHEN ''M'' THEN ''1''
                                 WHEN ''NA'' THEN ''2''
                                 WHEN ''U'' THEN ''3''
                                 ELSE ''-1''
                     END AS Gender ,... 
          FROM dbo.Employees WITH 
          (HOLDLOCK TABLOCKX)
          ')
...
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', 
                  N'Employees', 'OBJECT'
GO
```

**Figure: Change data type (Very Hard) e.g. Text to Integer. Text to Integer and data conversion requires ["Data Motion Scripts"](/do-you-understand-a-data-type-change-data-motion-scripts). The above is abbreviated, see [the full .SQL file](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity/EmployeesCharToInt.sql)**

The point of this is to know that no tool out there, not Redgate's SQL Compare, not Visual Studio SQL Schema Compare (aka Data Dude), nor SSW's SQL Deploy will do this automagically for you. So you better understand that this stuff is delicate.
