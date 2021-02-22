---
type: rule
archivedreason: 
title: Do you have an understanding of 'schema changes' and their increasing complexity?
guid: 634434fa-12e0-4eed-9514-eaf4fb2fcc01
uri: do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity
created: 2009-10-06T23:32:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Do you dream to be a 'Schema Master' one day? If so you need to know what changes are low impact and what needs to be done with care. Take care when it involves existing data. Do you know what the hard ones are? 

 Let's look at examples of this increasing complexity (using [The Mr Northwinds database](http&#58;//www.microsoft.com/Downloads/details.aspx?FamilyID=06616212-0356-46a0-8da2-eebc53a68034&amp;displaylang=en)) :   
<!--endintro-->



```
ALTER TABLE dbo.Employees
    ADD Gender bit NOT NULL
GO
```


     Figure: Add a column (Easy)        


```
ALTER TABLE dbo.Employees
    DROP COLUMN TitleOfCourtesy
GO
```


     Figure: Delete a column (Easy)        


```
EXECUTE sp_rename N'dbo.Employees.HireDate', 
                  N'Tmp_StartDate_1', 'COLUMN'
GO
EXECUTE sp_rename N'dbo.Employees.Tmp_StartDate_1', 
                  N'StartDate', 'COLUMN'
GO
```


     Figure: Rename a column (Medium)        


```
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


     Figure: Change data type (Hard) e.g. Bit to Integer. The above is abbreviated, see [the full .SQL file](/Documents/EmployeesBitToInt.sql)


```
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


     Figure: Change data type (Very Hard) e.g. Text to Integer. Text to Integer and data conversion requires ["Data Motion Scripts"](/Pages/DoYouUnderstandADataTypeChangeDataMotionScripts.aspx). The above is abbreviated, see [the full .SQL file](/Documents/EmployeesCharToInt.sql)     
 And the point of know this. Well no tool out there, not Redgate's SQL Compare, not Microsoft's Data Dude, nor SSW's SQL Deploy will do this automagically for you. So you better understand that this stuff is delicate.
