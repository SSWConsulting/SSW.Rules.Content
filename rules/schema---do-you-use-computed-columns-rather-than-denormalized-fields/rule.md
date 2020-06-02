---
uri: schema---do-you-use-computed-columns-rather-than-denormalized-fields
title: Schema - Do you use computed columns rather than denormalized fields?
created: 2019-11-07 20:29:18
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>When you have a denormalized field, use a computed column.&#160; In&#160;SQL Server&#160;​they can be persisted.<br></p><p>Use the suffix &quot;Computed&quot; to clearly distinguish that this field is a computed field.<br><br><img src="/PublishingImages/NormalizedFields_Bad.jpg" alt="NormalizedFields_Bad.jpg style=" style="width&#58;750px;" /><br></p><dl class="badImage"><dd>Figure&#58; Bad Example - This field was manually​ updated from code in the middle tier.<br></dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/NormalizedFields_Good.jpg" alt="NormalizedFields_Good.jpg" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Good Example​ - There was no code in the middle tier to calculate this (and it has the correct&#160;name)<br><br></dd></dl> </span>

<p>Computed columns have&#160;some limitations - they cannot access fields in other tables, or other computed fields in the current table.<br></p><p>You can use&#160;user-defined functions (UDF) from code in a reusable function, this allows one computed column to use a function to call another function.&#160; Here is an example&#58;​<br></p><p>ALTER FUNCTION [dbo].[udfEmpTime_TimeTotalComputed]<br></p><p class="ssw15-rteElement-CodeArea"> (<br>@TimeStart as DateTime,<br>@TimeEnd as DateTime 
   <br>)<br>RETURNS DECIMAL(8,6)<br>AS<br>BEGIN<br>-- This function returns the time difference in hours - decimal(8,6)<br>​RETURN (round(isnull(CONVERT([decimal](8,6),@TimeEnd - @TimeStart,(0))*(24),(0)),(2)))<br><br> END​<br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; This is the user defined function<br></dd>
<dl class="image"><dt><img src="/PublishingImages/NormalizedFieldsDefine.jpg" alt="NormalizedFieldsDefine.jpg" /></dt><dd>Figure&#58; Sett​ing up a&#160;computed column in the table designer​<br><br><br></dd></dl>


