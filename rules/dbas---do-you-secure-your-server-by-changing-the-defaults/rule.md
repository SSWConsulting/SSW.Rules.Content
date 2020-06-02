

---
uri: dbas---do-you-secure-your-server-by-changing-the-defaults
title: DBAs - Do you secure your server by changing the 'defaults'?
created: YYYY-11-DD 17:49:51
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <ol><li>​Disable defaults<br></li><ul><li>Disable Administrator and Rename it, then create a new &quot;honeypot&quot; Administrator account with no permissions.</li><li>Disable Guest on the SQL</li><li>Change Port 1433</li><li>Delete the sample databases - (AdventureWorks, Northwind and Pubs). These have a Public Role which is a security risk and allow Massive SQL Statements</li></ul><li>Other security issues</li><ul><li>Use a service account with a strong password</li><li>Do&#160;not run SQL Server service as an administrator</li><li>Run in integrated security mode<br></li><li>Run on NTFS file system - Encrypt the data files​<br></li></ul></ol><br> </span>




