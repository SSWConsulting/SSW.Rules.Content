---
type: rule
archivedreason: Rule no longer required - Same information can be found at https://rules.ssw.com.au/only-use-unicode-datatypes-in-special-circumstances
title: Schema - Do you know the maximum row size for a table?
guid: 80b9232f-ae71-436d-bd11-91b6d9530f67
uri: maximum-row-size-for-a-table
created: 2019-11-05T23:20:11.0000000Z
authors:
- title: Adam Cogan
  url: /people/adam-cogan
related: []
redirects:
- schema-do-you-know-the-maximum-row-size-for-a-table

---

A tables' maximum row size should be less than the size of a single SQL Server data page (8060 bytes). Otherwise, data entry forms can give errors is not validated correctly.

<!--endintro-->
