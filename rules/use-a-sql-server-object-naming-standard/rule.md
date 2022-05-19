---
type: rule
title: Do you use a SQL Server Object Naming Standard?
uri: use-a-sql-server-object-naming-standard
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - general-do-you-use-a-sql-server-object-naming-standard
created: 2019-12-31T04:20:06.000Z
archivedreason: null
guid: 68322e79-6a1a-4506-b4fa-422198f2c599
---

This standard outlines the standard on naming objects within SQL Server. Use these standards when naming any object or if you find an older object that doesn't follow these standards within SSW.

<!--endintro-->

All feedback is welcome. Thanks to all who gave feedback. A special thanks to Andy Baron.


| Object                 |   Prefix   |                       Example                        |
| ---------------------- | :--------: | :--------------------------------------------------: |
| Table                  |            |                      Clients                         |
| Column (PK)            |            |                        Id                            |
| Column (FK)            |            |                      ClientId                        |
| Temporary Table        |    \_zt    |                    \_ztClients                       |
| System Table           |    \_zs    |         \_zsDataVersion, \_zsVersionLatest           |
| View                   |  vw, gy\_  |   vwClientsWithNoPhoneW, gy\_ClientsWithNoPhoneW     |
| Stored Procedure       | proc, gp\_ | procSelectClientsClientID, gp\_SelectClientsClientID |
| Trigger                |    trg     |                     trgOrderIU                       |
| Default\*              |    dft \*  |                     dftToday \*                      |
| Rule                   |    rul     |                     rulCheckZIP                      |
| User-Defined Datatype  |    udt     |                      udtPhone                        |
| User-Defined Functions |    udf     |                     udfDueDates                      |


\* We never use defaults as objects, this is really an old thing that is just there for backwards compatibility. Much better to use a default constraint.

### Other Links

[SQL Server Coding Standards - Part 1](https&#58;//www.ssw.com.au/ssw/Redirect/SQLServer/SQLServerCentralcodingstandardspart1.htm)
By Steve Jones on SQL Server Central
