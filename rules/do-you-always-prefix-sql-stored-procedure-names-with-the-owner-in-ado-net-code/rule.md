---
type: rule
archivedreason: 
title: Do you always prefix SQL stored procedure names with the owner in ADO.NET code?
guid: 059f81e9-77a4-4eb2-8bd0-52fc3e3be0a6
uri: do-you-always-prefix-sql-stored-procedure-names-with-the-owner-in-ado-net-code
created: 2009-05-13T06:49:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

Stored procedure names in code should always be prefixed with the owner (usually dbo). This is because if the owner is not specified, SQL Server will look for a procedure with that name for the currently logged on user first, creating a performance hit.   

<!--endintro-->

``` dotnet
SqlCommand sqlcmd = new SqlCommand(); sqlcmd.CommandText = "
                    proc_InsertCustomer" sqlcmd.CommandType
                    = CommandType.StoredProcedure; sqlcmd.Connection = sqlcon;
```
::: bad
Bad example             
:::

``` dotnet
SqlCommand sqlcmd = new SqlCommand(); sqlcmd.CommandText = "
                     dbo.proc_InsertCustomer"; sqlcmd.CommandType
                     = CommandType.StoredProcedure; sqlcmd.Connection = sqlcon;
```
::: good
Good example   
:::

We have a program called [SSW Code Auditor](https://codeauditor.com/) to check for this rule.
