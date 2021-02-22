---
type: rule
archivedreason: 
title: How to publish a report based on a list?
guid: 06f92453-fdd3-4a3f-8770-bf79d6c35944
uri: how-to-publish-a-report-based-on-a-list
created: 2009-09-22T08:18:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When you want a Grid with filters, group by, totals and sorting, how do you do this (if all the data is in a list) ?   
<!--endintro-->

There are 6 options:

* Option 1 - use data view web part + AJAX (on test server, then export web part, and import to production)
* Option 2 - use content query web part (but no paging, no grouping, no totals)
* Option 3 - install Telerik grid and do aspx page
    * using this FILTERING  [http://demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx](http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx)
* Option 4 - using RS + iFrame
* Option 5 - use a smart web part with Telerik
    * A grid control like : [http://demos.telerik.com/aspnet-ajax/grid/examples/hierarchy/nestedviewtemplate/defaultcs.aspx](http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/hierarchy/nestedviewtemplate/defaultcs.aspx)
    * A filter like: [http://demos.telerik.com/aspnet-ajax/grid/examples/programming/filtertemplate/defaultcs.aspx](http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/programming/filtertemplate/defaultcs.aspx)
    * Or a perfect filter like: [http://demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx](http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx)
* Option 6 - look for ready to go web part from Infragistics or Telerik that use their grid


if you need to use the object model (like PublishedBy.aspx) to interate through records - use Option 1,3,5 , and we prefer option 5.

if you need to bind a simple list  - use Option 4 (best designer, scheduling included, parameters are easy... we know that iFrame is not great).
