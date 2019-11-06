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
  <p>​We always use two tables for tracking versioning information&#58;<br></p>
<ul>
    <li>_zsDataVersion tracks the schema changes, and which update script we are up to. This helps tremendously in determining which version of the scripts are still required between development, test, and production databases. </li>
    <li>_zsVersionLatest tracks which version the front-end client should be. This allows us to give a warning to (or even deny) users who are connecting to the database while not using the right version of the front-end client.<br></li>
</ul>

 </span>

<p>Please see &quot;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=8c1a4352-348d-48d7-931a-9e6da2b8f8b2">Is a Back-end structural change going to be a hassle?</a>&quot; on our Rules to Successful Projects.​<br></p>


