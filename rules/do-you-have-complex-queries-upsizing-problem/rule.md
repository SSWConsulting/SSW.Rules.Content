---
type: rule
title: Do you have complex queries (Upsizing Problem)?
uri: do-you-have-complex-queries-upsizing-problem
created: 2010-07-23T03:23:22.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> The Upsizing Tools do not try to upsize every type of Microsoft Access query that you may have in your Access (Jet) database. The following varieties of queries will not upsize&#58; 
 </span>


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



