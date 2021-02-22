---
type: rule
archivedreason: 
title: Views - Do you avoid having views as redundant objects?
guid: 4e697e4e-d33a-46ea-8d22-3e90642ba6ee
uri: do-not-have-views-as-redundant-objects
created: 2019-11-07T20:59:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- views-do-you-avoid-having-views-as-redundant-objects

---

Don't have views as redundant objects. e.g. vwCustomers as SELECT \* FROM Customers. This is unnecessary. Instead, Views should be generally used for security.

<!--endintro-->
