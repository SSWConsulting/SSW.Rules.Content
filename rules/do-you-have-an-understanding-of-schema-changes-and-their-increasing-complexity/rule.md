---
type: rule
title: Do you have an understanding of 'schema changes' and their increasing complexity?
uri: do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity
created: 2009-10-06T23:32:50.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Do you dream to be a 'Schema Master' one day? If so you need to know what changes are low impact and what needs to be done with care. Take care when it involves existing data. Do you know what the hard ones are? <br>
<br>
Let's look at examples of this increasing complexity (using <a shape="rect" href="http&#58;//www.microsoft.com/Downloads/details.aspx?FamilyID=06616212-0356-46a0-8da2-eebc53a68034&amp;displaylang=en">The Mr Northwinds database</a>) &#58; 
 </span>


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
    <pre>EXECUTE sp_rename N'dbo.Employees.HireDate', 
                  N'Tmp_StartDate_1', 'COLUMN'
GO
EXECUTE sp_rename N'dbo.Employees.Tmp_StartDate_1', 
                  N'StartDate', 'COLUMN'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58; Rename a column (Medium) </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>CREATE TABLE dbo.Tmp_Employees
(
    ...
    Gender char(2) NULL,
    ...
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
...
IF EXISTS(SELECT * FROM dbo.Employees)
&#160;&#160;&#160; EXEC('INSERT INTO dbo.Tmp_Employees (..., Gender,...)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;SELECT ...,Gender&#160;,... 
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;FROM dbo.Employees WITH (HOLDLOCK TABLOCKX)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;') 
...
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', <br>                  N'Employees', 'OBJECT'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58; Change data type (Hard) e.g.&#160;Bit to&#160;Integer. The above is abbreviated, see <a shape="rect" href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Documents/EmployeesBitToInt.sql">the full .SQL file</a> </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>CREATE TABLE dbo.Tmp_Employees
(
    ...
    Gender&#160;int NULL,
    ...
) ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
...
IF EXISTS(SELECT * FROM dbo.Employees)
&#160;&#160;&#160; EXEC('INSERT INTO dbo.Tmp_Employees (..., Gender,...)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;SELECT ...,<font style="background-color&#58;#ffff00;">CASE Gender&#160;WHEN ''F'' THEN ''0''&#160;
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''M'' THEN ''1''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''NA'' THEN ''2''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;WHEN ''U'' THEN ''3''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ELSE ''-1''
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;END AS Gender</font>&#160;,... 
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;FROM dbo.Employees WITH <br>          (HOLDLOCK TABLOCKX)
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;')
...
GO
DROP TABLE dbo.Employees
GO
EXECUTE sp_rename N'dbo.Tmp_Employees', <br>                  N'Employees', 'OBJECT'
GO 
</pre>
    </font></dt>
    <dd>Figure&#58;&#160;Change data type (Very Hard) e.g. Text to Integer. Text to Integer and data conversion requires <a shape="rect" href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouUnderstandADataTypeChangeDataMotionScripts.aspx">&quot;Data Motion Scripts&quot;</a>. The above is abbreviated, see <a shape="rect" href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Documents/EmployeesCharToInt.sql">the full .SQL file</a> </dd>
</dl>
&#160; <br>
And the point of know this. Well no tool out there, not Redgate's SQL Compare, not Microsoft's Data Dude, nor SSW's SQL Deploy will do this automagically for you. So you better understand that this stuff is delicate. 



