---
type: rule
title: General - Do you know to not use "sp_rename" to rename objects?
uri: general---do-you-know-to-not-use-sp_rename-to-rename-objects
created: 2019-11-14T21:42:49.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​Do not use &quot;sp_rename&quot; to rename objects like stored procedures, views and triggers.​<br></p>
​​​Object name should be the same as the name used in the object's script (e.g. CREATE script for stored procedures, views and triggers). Inconsistency can happen when object is renamed with sp_rename, but its script is not updated.<br> </span>




