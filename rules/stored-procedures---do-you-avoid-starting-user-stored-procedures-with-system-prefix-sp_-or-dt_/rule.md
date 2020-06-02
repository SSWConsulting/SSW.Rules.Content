

---
uri: stored-procedures---do-you-avoid-starting-user-stored-procedures-with-system-prefix-sp_-or-dt_
title: Stored Procedures - Do you avoid starting user stored procedures with system prefix "sp_" or "dt_"?
created: YYYY-11-DD 22:38:15
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>System stored procedures are created and stored in the master database and have the sp_ prefix. System stored procedures can be executed from any database without having to qualify the stored procedure name fully using the database name master. It is strongly recommended that you do not create any stored procedures using sp_ as a prefix. SQL Server always looks for a stored procedure beginning with sp_ in this order&#58;</p><ol><li>The stored procedure in the master database.</li><li>The stored procedure based on any qualifiers provided (database name or owner).</li><li>The stored procedure using dbo as the owner, if one is not specified.<br></li></ol> </span>

<p>Therefore, although the user-created stored procedure prefixed with sp_ may exist in the current database, the master database is always checked first, even if the stored procedure is qualified with the database name.<br></p><p><strong>Important&#58;</strong>&#160;If any user-created stored procedure has the same name as a system stored procedure, the user-created stored procedure will never be executed.<br></p>


