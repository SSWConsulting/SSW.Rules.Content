---
type: rule
title: How to publish a report based on a list?
uri: how-to-publish-a-report-based-on-a-list
created: 2009-09-22T08:18:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>There are 6 options&#58;</p>
<ul>
    <li>Option 1 - use data view web part + AJAX (on test server, then export web part, and import to production) </li>
    <li>Option 2 - use content query web part (but no paging, no grouping, no totals) </li>
    <li>Option 3 - install Telerik grid and do aspx page
    <ul>
        <li>using this FILTERING&#160; <a href="http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx">http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx</a> </li>
    </ul>
    </li>
    <li>Option 4 - using RS + iFrame </li>
    <li>Option 5 - use a smart web part with Telerik
    <ul>
        <li>A grid control like &#58; <a href="http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/hierarchy/nestedviewtemplate/defaultcs.aspx">http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/hierarchy/nestedviewtemplate/defaultcs.aspx</a> </li>
        <li>A filter like&#58; <a href="http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/programming/filtertemplate/defaultcs.aspx">http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/programming/filtertemplate/defaultcs.aspx</a> </li>
        <li>Or a perfect filter like&#58; <a href="http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx">http&#58;//demos.telerik.com/aspnet-ajax/grid/examples/generalfeatures/filtering/defaultcs.aspx</a> </li>
    </ul>
    </li>
    <li>Option 6 - look for ready to go web part from Infragistics or Telerik that use their grid </li>
</ul>
<p>if you need to use the object model (like PublishedBy.aspx) to interate through records - use Option 1,3,5 , and we prefer option 5.</p>
<p>if you need to bind a simple list&#160; - use Option 4 (best designer, scheduling included, parameters are easy... we know that iFrame is not great).</p>
<p>&#160;</p>
<p>&#160;</p>



