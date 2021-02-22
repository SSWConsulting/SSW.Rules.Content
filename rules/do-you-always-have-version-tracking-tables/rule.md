---
type: rule
archivedreason: 
title: Schema - Do you always have version tracking tables?
guid: 5935acb7-2e10-49dc-ade6-38aba061a165
uri: do-you-always-have-version-tracking-tables
created: 2010-07-23T02:52:32.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-use-prefix-sys-in-table-name-best-practice
redirects:
- schema-do-you-always-have-version-tracking-tables

---

We always use two tables for tracking versioning information:

* \_zsDataVersion tracks the schema changes, and which update script we are up to. This helps tremendously in determining which version of the scripts are still required between development, test, and production databases.
* \_zsVersionLatest tracks which version the front-end client should be. This allows us to give a warning to (or even deny) users who are connecting to the database while not using the right version of the front-end client.


<!--endintro-->

Please see "[Is a Back-end structural change going to be a hassle?](/do-you-stop-dealing-with-data-and-schema)" on our Rules to Successful Projects.
