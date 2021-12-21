---
type: rule
title: Do you ensure your Test environment is representative of Production?
uri: ensure-testenvironment-is-representative-of-production
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:23:22.156Z
guid: 013bf720-9980-4ebb-b449-a27b4d7683a8
---
To avoid embarrassing failures in Production, it is important to ensure that your development systems are as similar as possible to what's expected in Production.

<!--endintro-->

Modifying and querying database tables is very dependent on the amount of data in the table. Often developers will run their code in a database without sufficient data in the tables and therefore the queries are nice and fast. The problem is when there's millions of transactions already in the database, all the queries turn out to be far too slow.

So it is an important part of the development process to seed your development databases with a reasonable amount of representative data.