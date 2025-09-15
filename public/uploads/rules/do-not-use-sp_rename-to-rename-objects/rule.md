---
type: rule
archivedreason: 
title: General - Do you know to not use "sp_rename" to rename objects?
guid: 1aab9df8-5908-4540-8172-8a5bcf761ec4
uri: do-not-use-sp_rename-to-rename-objects
created: 2019-11-14T21:42:49.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- general-do-you-know-to-not-use-sp_rename-to-rename-objects

---

Do not use "sp\_rename" to rename objects like stored procedures, views and triggers.
 Object name should be the same as the name used in the object's script (e.g. CREATE script for stored procedures, views and triggers). Inconsistency can happen when object is renamed with sp\_rename, but its script is not updated.

<!--endintro-->
