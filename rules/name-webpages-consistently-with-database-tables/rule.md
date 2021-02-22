---
type: rule
archivedreason: 
title: Do you name web pages to be consistent with database tables?
guid: 0c0d45e1-e1b4-4cde-922d-bfe4e3b28271
uri: name-webpages-consistently-with-database-tables
created: 2016-08-26T17:47:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-name-web-pages-to-be-consistent-with-database-tables

---

In a database-driven page, it is important that the name of the page is based on the data that the page contains. For example, if a page shows client details and is based on the Client table, then the page should be called Client.aspx.
Other examples are: 


<!--endintro-->

* a search page. This page [ssw/Kb/KBSearch.asp](https&#58;//www.ssw.com.au/ssw/KB/KBSearch.aspx) is for searching a table obviously called KB
* a search results page. This page [ssw/KB/KBResult.aspx?searchOn=Words&searchFor=problem](https&#58;//www.ssw.com.au/ssw/KB/KBResult.aspx?searchOn=Words&amp;searchFor=problem) is returning the records for a table called KB
* a detail page. This page is showing the detail record for a record in the table 'KB'
