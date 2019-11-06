---
type: rule
archivedreason: 
title: Schema - Do you avoid using indexes on RowGuid column?
guid: 49e77277-e4f8-44a0-bc2c-3d7d487714a0
uri: avoid-using-indexes-on-rowguid-column
created: 2019-11-06T01:32:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-avoid-using-indexes-on-rowguid-column

---


<p class="ssw15-rteElement-P">​RowGuids (uniqueidentifier) are large fields (16 bytes) and are basically going to ALWAYS​ be unique.​<br></p><div><p class="ssw15-rteElement-P">SQL Server adds a RowGUID column to all tables if you are using Merge Replication (but doesn't add an index).​​<br></p><p class="ssw15-rteElement-P">RowGuids in general slow things down. Some people may consider using a RowGuid as their primary key. This is a bad idea because the index is going to be quite slow.... you are searching a large field. It goes without saying, NEVER have clustered index on a RowGuid column.​​<br></p></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​Another little annoyance with RowGuids is whe​​n you are searching for one. You can't use {gtHTMLChar} or {ltHTMLChar} on a RowGuid column.</p><p class="ssw15-rteElement-P"><b>​Note&#58;&#160;</b>There are not many cases where a RowGuid should have an index on it. (Exception SSW SQL Total Compare which is a tool that compares data is in sync via rowguids and this makes it lots faster).</p><p>Be aware that SQL server adds this column when you perform merge replication. There are not many cases where this should have an index on it. An exception is if you are using our utility&#160;<a href="https&#58;//www.ssw.com.au/ssw/SQLTotalCompare/">SQL Total Compare</a>.​<br></p>


