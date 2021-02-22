---
type: rule
archivedreason: 
title: Stored Procedures - Do you avoid starting user stored procedures with system prefix "sp_" or "dt_"?
guid: 1512205e-fbd3-417e-b11c-3c07aca34ec6
uri: avoid-starting-user-stored-procedures-with-system-prefix-sp_-or-dt_
created: 2019-11-12T22:38:15.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- stored-procedures-do-you-avoid-starting-user-stored-procedures-with-system-prefix-sp_-or-dt_

---

System stored procedures are created and stored in the master database and have the sp\_ prefix. System stored procedures can be executed from any database without having to qualify the stored procedure name fully using the database name master. It is strongly recommended that you do not create any stored procedures using sp\_ as a prefix. SQL Server always looks for a stored procedure beginning with sp\_ in this order:

1. The stored procedure in the master database.
2. The stored procedure based on any qualifiers provided (database name or owner).
3. The stored procedure using dbo as the owner, if one is not specified.


<!--endintro-->

Therefore, although the user-created stored procedure prefixed with sp\_ may exist in the current database, the master database is always checked first, even if the stored procedure is qualified with the database name.

**Important:**  If any user-created stored procedure has the same name as a system stored procedure, the user-created stored procedure will never be executed.
