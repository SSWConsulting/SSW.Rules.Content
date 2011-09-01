---
type: rule
title: Schema - Do you always have version tracking tables?
uri: schema---do-you-always-have-version-tracking-tables
created: 2010-07-23T02:52:32.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>We always use two tables for tracking versioning information&#58;</p>
<ul>
    <li>_zsDataVersion tracks the schema changes, and which update script we are up to. This helps tremendously in determining which version of the scripts are still required between development, test, and production databases. </li>
    <li>_zsVersionLatest tracks which version the front-end client should be. This allows us to give a warning to (or even deny) users who are connecting to the database while not using the right version of the front-end client. </li>
</ul>
<p>Please see &quot;<a href="/do-you-stop-dealing-with-data-and-schema">Is a Back-end structural change going to be a hassle?</a>&quot; on our Rules to Successful Projects.</p>
 </span>




