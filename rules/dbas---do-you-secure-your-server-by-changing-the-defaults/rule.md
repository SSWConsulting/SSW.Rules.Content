---
type: rule
archivedreason: 
title: DBAs - Do you secure your server by changing the 'defaults'?
guid: df5f2ab5-bad1-4bb4-a753-7eb8dc53b089
uri: dbas---do-you-secure-your-server-by-changing-the-defaults
created: 2019-11-21T17:49:51.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<ol><li>​Disable defaults<br></li><ul><li>Disable Administrator and Rename it, then create a new &quot;honeypot&quot; Administrator account with no permissions.</li><li>Disable Guest on the SQL</li><li>Change Port 1433</li><li>Delete the sample databases - (AdventureWorks, Northwind and Pubs). These have a Public Role which is a security risk and allow Massive SQL Statements</li></ul><li>Other security issues</li><ul><li>Use a service account with a strong password</li><li>Do&#160;not run SQL Server service as an administrator</li><li>Run in integrated security mode<br></li><li>Run on NTFS file system - Encrypt the data files​<br></li></ul></ol><br>
<br><excerpt class='endintro'></excerpt><br>



