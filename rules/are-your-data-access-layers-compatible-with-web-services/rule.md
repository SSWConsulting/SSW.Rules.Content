---
seoDescription: Ensure seamless data access layers that seamlessly integrate with web services, facilitating cloud-based database connectivity for a future-proof application architecture.
type: rule
title: Are your Data Access Layers compatible with Web Services?
uri: are-your-data-access-layers-compatible-with-web-services
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T05:37:00.000Z
guid: 6de2de45-9c13-4890-a6c2-3efafaf0ab26
---

Data Access Layers should support not only direct connections to SQL Server but also connections through web services.

Many applications are designed for use with a database connection only. As users decide to take the application some where else away from the database, the need for web services arises.

<!--endintro-->

::: good
![Figure: Good example - Options form showing choice of connection](timepronetoptionsconnection_1711074081216.jpg)
:::

There are 3 ways to implement this:

1. Lots of if statements (really messy - most people try this first)
2. Interfaces (implements statement in VB)
3. Factory pattern (✅ best - most flexible and extensible approach)

All database applications should be web services ready as the future direction is to use web services only, because even locally a web service connection is not much slower than direct connection. The performance difference shouldn't be substantial enough to require a double code base.
