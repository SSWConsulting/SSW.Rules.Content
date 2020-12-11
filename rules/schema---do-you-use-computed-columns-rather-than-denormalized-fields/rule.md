---
type: rule
archivedreason: 
title: Schema - Do you use computed columns rather than denormalized fields?
guid: 6a71c411-854a-4425-a4e8-392e717bedec
uri: schema---do-you-use-computed-columns-rather-than-denormalized-fields
created: 2019-11-07T20:29:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>When you have a denormalized field, use a computed column.  In SQL Server ​they can be persisted.<br></p><p>Use the suffix "Computed" to clearly distinguish that this field is a computed field.<br><br><img src="NormalizedFields_Bad.jpg" alt="NormalizedFields_Bad.jpg style=" style="width:750px;" /><br></p><dl class="badImage"><dd>Figure: Bad Example - This field was manually​ updated from code in the middle tier.<br></dd></dl><dl class="goodImage"><dt>
      <img src="NormalizedFields_Good.jpg" alt="NormalizedFields_Good.jpg" style="width:750px;" />
   </dt><dd>Figure: Good Example​ - There was no code in the middle tier to calculate this (and it has the correct name)<br><br></dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<p>Computed columns have some limitations - they cannot access fields in other tables, or other computed fields in the current table.<br></p><p>You can use user-defined functions (UDF) from code in a reusable function, this allows one computed column to use a function to call another function.  Here is an example:​<br></p><p>ALTER FUNCTION [dbo].[udfEmpTime_TimeTotalComputed]<br></p><p class="ssw15-rteElement-CodeArea"> (<br>@TimeStart as DateTime,<br>@TimeEnd as DateTime 
   <br>)<br>RETURNS DECIMAL(8,6)<br>AS<br>BEGIN<br>-- This function returns the time difference in hours - decimal(8,6)<br>​RETURN (round(isnull(CONVERT([decimal](8,6),@TimeEnd - @TimeStart,(0))*(24),(0)),(2)))<br><br> END​<br></p><dd class="ssw15-rteElement-FigureNormal">Figure: This is the user defined function<br></dd>
<dl class="image"><dt><img src="NormalizedFieldsDefine.jpg" alt="NormalizedFieldsDefine.jpg" /></dt><dd>Figure: Sett​ing up a computed column in the table designer​<br><br><br></dd></dl>


