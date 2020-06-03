---
type: rule
title: Do you know you can't think of data the same way?
uri: do-you-know-you-cant-think-of-data-the-same-way
created: 2009-05-21T23:35:36.0000000Z
authors:
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <p class="MsoNormal">
    <span lang="EN-AU">In SQL Server you have tables to store data.&#160; Then you have Views, Relations and Stored Procedures.</span> </p>
<p class="MsoNormal"><span lang="EN-AU">SharePoint gives us Lists where we can store rows and columns of data, but it is not the same as a full database.</span></p>
&#160;
<ul>
    <li>There are no joints out of SharePoint – you can do limited operations with lookup fields but they are not the same as joints in SQL Server </li>
    <li>Views in SharePoint are filters, grouping and sort on a single list only. </li>
    <li>Formula fields in SharePoint are only updated when the row is changed.&#160; If you change the lookup value in the lookup list, it will not change any of the items using formula fields that are currently referencing that lookup. </li>
    <li>No stored procedures in SharePoint </li>
</ul>
<p><span lang="EN-AU">Database remains the best at doing database work.&#160; SharePoint is OK at creating quick lists and working with simple lists, but it is not a database server.</span></p>
 </span>




