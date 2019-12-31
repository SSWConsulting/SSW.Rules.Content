---
type: rule
archivedreason: 
title: Schema - Do you use computed columns rather than denormalized fields?
guid: 6a71c411-854a-4425-a4e8-392e717bedec
uri: use-computed-columns-rather-than-denormalized-fields
created: 2019-11-07T20:29:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-computed-columns-rather-than-denormalized-fields

---


<p>​We should always use computed columns (in SQL Server 2005 and later they can be persisted) to avoid these types of denormalized columns.​<br></p><dl class="badImage"><dt>
      <img src="/PublishingImages/NormalizedFields_Bad.jpg" alt="NormalizedFields_Bad.jpg style=" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Bad Example<br></dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/NormalizedFields_Good.jpg" alt="NormalizedFields_Good.jpg" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Good Example​<br><br></dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<p>Computed columns has some limitations - they cannot access fields in other tables, or other computed fields in the current table.<br></p><p>We use user defined functions (UDF) to encapsulate our logic in reusable functions, this allows one computed column to use a function to call another function.</p><p>Use the suffix Computed to clearly distinguish that this field is a computed field.<br><br></p><p> ALTER FUNCTION [dbo].[udfEmpTime_TimeTotalComputed]<br></p><p class="ssw15-rteElement-CodeArea"> (<br><br> @TimeStart as DateTime,<br><br> @TimeEnd as DateTime 
   <br>
   <br> )<br><br> RETURNS DECIMAL(8,6)<br><br> AS<br><br> BEGIN<br><br> -- This function returns the time difference in hours - decimal(8,6)<br><br> RETURN (round(isnull(CONVERT([decimal](8,6),@TimeEnd - @TimeStart,(0))*(24),(0)),(2)))<br><br> END​<br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; This is the user defined function<br></dd>
<dl class="image"><dt><img src="/PublishingImages/NormalizedFieldsDefine.jpg" alt="NormalizedFieldsDefine.jpg" /></dt><dd>Figure&#58; Sett​ing up a&#160;computed column in the table designer</dd></dl>


