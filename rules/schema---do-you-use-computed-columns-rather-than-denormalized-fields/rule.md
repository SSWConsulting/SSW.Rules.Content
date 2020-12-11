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

When you have a denormalized field, use a computed column.  In SQL Server they can be persisted.

Use the suffix "Computed" to clearly distinguish that this field is a computed field.


![](NormalizedFields_Bad.jpg)
<dl class="badImage"><dd>Figure: Bad Example - This field was manually updated from code in the middle tier.<br></dd></dl><dl class="goodImage">&lt;dt&gt;
      <img src="NormalizedFields_Good.jpg" alt="NormalizedFields_Good.jpg" style="width:750px;">
   &lt;/dt&gt;<dd>Figure: Good Example - There was no code in the middle tier to calculate this (and it has the correct name)<br><br></dd></dl>
<!--endintro-->

Computed columns have some limitations - they cannot access fields in other tables, or other computed fields in the current table.

You can use user-defined functions (UDF) from code in a reusable function, this allows one computed column to use a function to call another function.  Here is an example:

ALTER FUNCTION [dbo].[udfEmpTime\_TimeTotalComputed]

(
@TimeStart as DateTime,
@TimeEnd as DateTime     
)
RETURNS DECIMAL(8,6)
AS
BEGIN
-- This function returns the time difference in hours - decimal(8,6)
RETURN (round(isnull(CONVERT([decimal](8,6),@TimeEnd - @TimeStart,(0))\*(24),(0)),(2)))

 END
 **Figure: This is the user defined function
** <dl class="image">&lt;dt&gt;<img src="NormalizedFieldsDefine.jpg" alt="NormalizedFieldsDefine.jpg">&lt;/dt&gt;<dd>Figure: Setting up a computed column in the table designer<br><br><br></dd></dl>
