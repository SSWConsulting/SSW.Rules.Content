---
type: rule
archivedreason: 
title: Do you enable SQL (Read-Only) connect to the Common Data Service?
guid: 597a7415-6f5a-42e8-babd-75024df484ce
uri: do-you-enable-sql-read-only-connect-to-the-common-data-service
created: 2020-06-25T22:04:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir
related: []

---


Currently in preview (as at May 2020) Common Data Service supports direct SQL Access to Dynamics entities. This is huge for many Dynamics scenarios, in particular using it for direct query Power BI reports.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​As this feature is in preview (as at May 2020) you'll need to enable it, and it's not recommended for production environments. With that out of the way follow the steps at the Microsoft Docs page&#58;&#160;<a href="https&#58;//docs.microsoft.com/en-us/powerapps/developer/common-data-service/cds-sql-query">Use SQL to query data (Preview)</a></p><h3 class="ssw15-rteElement-H3">Supported operations and data types​​<br></h3><p>The list of supported SQL operations includes&#58;</p><p>Batch operations</p><ul><li>SELECT</li><li>Aggregation functions (i.e., Count() and Max() functions)</li><li>UNIONs and JOINs</li><li>Filtering</li></ul><p>Any operation that attempts to modify data (i.e., INSERT, UPDATE) will not work as this is a read-only SQL data connection. Common Data Service option sets are represented as &lt;OptionSet&gt;Name and &lt;OptionSet&gt;Label in a result set.</p><p>The following Common Data Service datatypes are not supported with the SQL connection&#58;<br></p><p class="ssw15-rteElement-CodeArea">binary,&#160;image,&#160;ntext,&#160;sql_variant,&#160;varbinary,&#160;virtual,&#160;HierarchyId,&#160;managedproperty,&#160;file,&#160;xml,&#160;partylist,&#160;timestamp.</p><p>​​<br></p>


