---
type: rule
archivedreason: 
title: Schema - Do you use FillFactor of 90% for indexes and constraints?
guid: 7508330e-019a-463e-817f-38a91bcfafb6
uri: use-fillfactor-of-90-percent-for-indexes-and-constraints
created: 2019-11-06T17:32:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-fillfactor-of-90-for-indexes-and-constraints

---

Indexes should generally have a fillfactor of 90%. If the amount of data stored in the database does not prohibit rebuilding indexes, a fillfactor of 90% should be maintained to increase the performance of inserts.

<!--endintro-->

A table that expects a lot of insert operations could use a lower fillfactor.
