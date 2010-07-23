---
type: rule
archivedreason: 
title: Do you have complex queries (Upsizing Problem)?
guid: c77783a8-9a7d-403d-8c4c-01c49ebb078b
uri: do-you-have-complex-queries-upsizing-problem
created: 2010-07-23T03:23:22.0000000Z
authors:
- id: 1
  title: Adam Cogan
related:
- do-you-avoid-parameter-queries-with-exists-keyword-and-comparison-operators-<>-or-=upsizing-problem
- do-you-remove-vba-function-names-in-queries-before-upsizing-queries-upsizing-problem

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <ul>
    <li>Crosstab queries </li>
    <li>Action queries (append, delete, make-table, update) that take parameters </li>
    <li>Action queries that contain nested queries </li>
    <li>SQL pass-through queries </li>
    <li>SQL Data Definition Language (DDL) queries </li>
    <li>Union queries </li>
    <li>Queries that reference values on a form</li>
</ul>
<p>&#160;</p>
<p>You must manually re-create queries that the Upsizing Tools do not migrate.</p>



