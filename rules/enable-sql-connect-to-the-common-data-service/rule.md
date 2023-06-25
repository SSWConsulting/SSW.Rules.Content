---
type: rule
title: Do you enable SQL (Read-Only) connect to the Common Data Service?
uri: enable-sql-connect-to-the-common-data-service
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-enable-sql-read-only-connect-to-the-common-data-service
  - do-you-enable-sql-(read-only)-connect-to-the-common-data-service
created: 2020-06-25T22:04:54.000Z
archivedreason: null
guid: 597a7415-6f5a-42e8-babd-75024df484ce
---
Currently in preview (as at May 2020) Common Data Service supports direct SQL Access to Dynamics entities. This is huge for many Dynamics scenarios, in particular using it for direct query Power BI reports.

<!--endintro-->

As this feature is in preview (as at May 2020) you'll need to enable it, and it's not recommended for production environments. With that out of the way follow the steps at the Microsoft Docs page: [Use SQL to query data (Preview)](https&#58;//docs.microsoft.com/en-us/powerapps/developer/common-data-service/cds-sql-query)

### Supported operations and data types
The list of supported SQL operations includes:

Batch operations

* SELECT
* Aggregation functions (i.e., Count() and Max() functions)
* UNIONs and JOINs
* Filtering

Any operation that attempts to modify data (i.e., INSERT, UPDATE) will not work as this is a read-only SQL data connection. Common Data Service option sets are represented as &lt;OptionSet&gt;Name and &lt;OptionSet&gt;Label in a result set.

The following Common Data Service datatypes are not supported with the SQL connection:
- binary
- image
- ntext
- sql_variant
- varbinary
- virtual
- HierarchyId
- managedproperty
- file
- xml
- partylist
- timestamp