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


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>ALTER TABLE dbo.Employees
    ADD Gender bit NOT NULL
GO
</pre>
    </font></dt>
    <dd>Figure&#58; Add a column (Easy) </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>ALTER TABLE dbo.Employees
    DROP COLUMN TitleOfCourtesy
GO 
</pre>
    </font></dt>
    <dd>Figure&#58; Delete a column (Easy) </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>EXECUTE sp_rename N'dbo.Employees.HireDate', N'Tmp_StartDate_1', 'COLUMN'
GO
EXECUTE sp_rename N'dbo.Employees.Tmp_StartDate_1', N'StartDate', 'COLUMN'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58; Rename a column (Medium) </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>CREATE TABLE dbo.Tmp_Employees
(
......
Gender char(2) NULL,
......
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
......
IF EXISTS(SELECT * FROM dbo.Employees)
&#160;&#160;&#160; EXEC('INSERT INTO dbo.Tmp_Employees (......, Gender,......)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; SELECT ......,Gender&#160;,...... 
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; FROM dbo.Employees WITH (HOLDLOCK TABLOCKX)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;') 
......
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', N'Employees', 'OBJECT'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58; Change data type (Hard) e.g.&#160;Bit to&#160;Integer. The above is abbreviated, see <a shape="rect" href="/Standards/CodeAndApplicationDesign/RulesToBetterSQLServerSchemaDeployment/Documents/EmployeesBitToInt.sql">the full .SQL file</a> </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>CREATE TABLE dbo.Tmp_Employees
(
......
Gender&#160;int NULL,
......
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
......
IF EXISTS(SELECT * FROM dbo.Employees)
&#160;&#160;&#160; EXEC('INSERT INTO dbo.Tmp_Employees (......, Gender,......)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; SELECT ......,<font style="background-color&#58;#ffff00;">CASE Gender&#160;WHEN ''F'' THEN ''0''&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''M'' THEN ''1''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''NA'' THEN ''2''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''U'' THEN ''3''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ELSE ''-1''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;END AS Gender</font>&#160;,...... 
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; FROM dbo.Employees WITH (HOLDLOCK TABLOCKX)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;')
......
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', N'Employees', 'OBJECT'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58;&#160;Change data type (Very Hard) e.g. Text to Integer. Text to Integer and data conversion requires <a shape="rect" href="/Standards/CodeAndApplicationDesign/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouUnderstandADataTypeChangeDataMotionScripts.aspx">&quot;Data Motion Scripts&quot;</a>. The above is abbreviated, see <a shape="rect" href="/Standards/CodeAndApplicationDesign/RulesToBetterSQLServerSchemaDeployment/Documents/EmployeesCharToInt.sql">the full .SQL file</a> </dd>
</dl>
&#160; <br>
And the point of know this. Well no tool out there, not Redgate's SQL Compare, not Microsoft's Data Dude, nor SSW's SQL Deploy will do this automagically for you. So you better understand that this stuff is delicate.



