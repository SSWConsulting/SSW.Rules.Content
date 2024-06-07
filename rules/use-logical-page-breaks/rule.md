---
type: rule
archivedreason:
title: Data Layout - Do you know how to use logical page breaks?
guid: 2cdd195b-477e-4a8d-934d-b7605ce5dcd3
uri: use-logical-page-breaks
created: 2024-06-05T11:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Sometime you want your report to break at somewhere to separate different part of content into individual pages. A logical page break is what you need.
<!--endintro-->

Logical page breaks are defined in the report definition by using the PageBreakAtStart and PageBreakAtEnd properties in various report elements, including group, rectangle, list, table, matrix, and chart.

Here is an example of how we add logical page breaks in a report to make each subreport start showing at right beginning in a new page.

![Figure: Insert a logical page break before a rectangle containing a subreport](RSLogicalPageBreak.jpg)

![Figure: The subreport started in a new page](RSLogicalPageBreak_Preview.jpg)
