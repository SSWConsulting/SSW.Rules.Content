

---
uri: schema---do-you-avoid-using-indexes-on-rowguid-column
title: Schema - Do you avoid using indexes on RowGuid column?
created: YYYY-11-DD 01:32:42
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​​​RowGuids (uniqueidentifier) are large fields (16 bytes) and are basically going to ALWAYS​ be unique.​<br></p><div><p class="ssw15-rteElement-P">SQL Server adds a RowGUID column to all tables if you are using Merge Replication (but doesn't add an index).​​<br></p><p class="ssw15-rteElement-P">RowGuids in general slow things down. Some people may consider using a RowGuid as their primary key. This is a bad idea because the index is going to be quite slow.... you are searching a large field. It goes without saying, NEVER have clustered index on a RowGuid column.​​<br></p></div> </span>

<p class="ssw15-rteElement-P">​Another little annoyance with RowGuids is when you are searching for one. You can't use &gt; or &lt; on a RowGuid column.</p><p class="ssw15-rteElement-P"><b>​Note&#58;&#160;</b>There are not many cases where a RowGuid should have an index on it.&#160;<br></p><p>Be aware that SQL server adds this column when you perform merge replication. There are not many cases where this should have an index on it.<br></p>


