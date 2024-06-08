---
type: rule
archivedreason: 
title: Do you stop dealing with Data and Schema?
guid: d8a098fd-b81e-4f70-92ae-c03af30915f5
uri: do-you-stop-dealing-with-data-and-schema
created: 2009-03-10T06:36:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Why don't most developers plan ahead? Take an average Desktop application that you sell to a few customers. When the customer wants a new version, there is no problem giving the customer the new exe. But what if you made a back-end structural [changes to your database](https://www.ssw.com.au/ssw/Standards/Rules/DataSchemaStandard.aspx)? Big hassle! You need to compare the database to remind you what was changed. Sure there are utilities for this - for Access back ends you can use [SSW Data Renovator](https://www.ssw.com.au/ssw/Standards/DeveloperAccess/WhyDataRenovator.aspx) or for SQL Server back ends there is [Red-gate SQL Compare](https://www.red-gate.com/products/#1)  - but why go to this trouble?

<!--endintro-->

Version control for your Schema and where required your Data should be an important part of planning your projects.

For more information read [Rules to Better SQL Server Schema Deployment](/rules-to-better-sql-server-schema-deployment).
