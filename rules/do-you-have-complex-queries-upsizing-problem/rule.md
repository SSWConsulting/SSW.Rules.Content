---
seoDescription: Microsoft Access query migration can be challenging, especially when dealing with complex queries that don't upsize properly using the Upsizing Tools.
type: rule
archivedreason:
title: Do you have complex queries (Upsizing Problem)?
guid: c77783a8-9a7d-403d-8c4c-01c49ebb078b
uri: do-you-have-complex-queries-upsizing-problem
created: 2010-07-23T03:23:22.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators-or-upsizing-problem
  - do-you-remove-vba-function-names-in-queries-before-upsizing-queries-upsizing-problem
redirects:
  - do-you-have-complex-queries-(upsizing-problem)
---

The Upsizing Tools do not try to upsize every type of Microsoft Access query that you may have in your Access (Jet) database. The following varieties of queries will not upsize:

<!--endintro-->

- Crosstab queries
- Action queries (append, delete, make-table, update) that take parameters
- Action queries that contain nested queries
- SQL pass-through queries
- SQL Data Definition Language (DDL) queries
- Union queries
- Queries that reference values on a form

You must manually re-create queries that the Upsizing Tools do not migrate.
