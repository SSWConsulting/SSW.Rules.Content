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

When you have a denormalized field, use a computed column.  In SQL Server they can be persisted.

Use the suffix "Computed" to clearly distinguish that this field is a computed field.

![NormalizedFields_Bad.jpg style=](NormalizedFields_Bad.jpg)
Figure: Bad Example - This field was manually updated from code in the middle tier.


::: good  
![Figure: Good Example - There was no code in the middle tier to calculate this (and it has the correct name)](NormalizedFields\_Good.jpg)  
:::

<!--endintro-->

Computed columns have some limitations - they cannot access fields in other tables, or other computed fields in the current table.

You can use user-defined functions (UDF) from code in a reusable function, this allows one computed column to use a function to call another function.  Here is an example:

ALTER FUNCTION [dbo].[udfEmpTime\_TimeTotalComputed]



```
(
@TimeStart as DateTime,
@TimeEnd as DateTime 
   
)
RETURNS DECIMAL(8,6)
AS
BEGIN
-- This function returns the time difference in hours - decimal(8,6)
RETURN (round(isnull(CONVERT([decimal](8,6),@TimeEnd - @TimeStart,(0))*(24),(0)),(2)))

 END
```


 **Figure: This is the user defined function
** 
![Figure: Setting up a computed column in the table designer](NormalizedFieldsDefine.jpg)
