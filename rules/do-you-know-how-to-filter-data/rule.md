---
type: rule
archivedreason: 
title: Do you know how to filter data?
guid: d5927c8a-0dd8-4698-b68d-5680a046fe6f
uri: do-you-know-how-to-filter-data
created: 2009-08-24T04:04:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

It is difficult for users to find their required records in a huge amount of data, so adding the filter data functionalities is very useful.    
<!--endintro-->

The standard DataGrid of ASP.NET doesn't include this functionality, developers need to implement it by themselves.
<dl class="badImage">    &lt;dt&gt;<img alt="Bad Example - implement data filter manually" src="FilterDataInDataGrid.jpg"> &lt;/dt&gt;
    <dd>Figure: Bad Example - implement data filter manually</dd></dl>
Fortunately, RadGrid supplies this perfect feature.
<dl class="goodImage">    &lt;dt&gt;<img alt="Good Example - add an attribute to filter data" src="FilterDataInRadGrid.jpg"> &lt;/dt&gt;
    <dd>Figure: Good Example - add an attribute to filter data</dd></dl>
Developer can turn this feature on by setting the AllowFilteringByColumn="True".
