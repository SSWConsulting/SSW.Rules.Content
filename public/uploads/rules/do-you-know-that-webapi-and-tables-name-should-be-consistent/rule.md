---
seoDescription: WebAPIs and table names should be consistent to simplify development and maintenance of your API layer.
type: rule
archivedreason:
title: Do you know that WebAPI and table names should be consistent?
guid: d7511f71-d615-4f30-ab45-4f0b77ddb0b2
uri: do-you-know-that-webapi-and-tables-name-should-be-consistent
created: 2015-04-28T13:30:47.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-that-webapi-and-table-names-should-be-consistent
---

When creating WebAPIs for your applications, it is useful to keep the naming consistent all the way from the back-end to the front-end.

<!--endintro-->

::: greybox
**Table name:** Employees
**Endpoint:** /api/Users

:::

::: bad
Bad Example: The endpoint is different to the table name

:::

::: greybox
**Table name:** Employees
**Endpoint:** /api/Employees

:::

::: good
Good Example: Table name is the same as the WebAPI endpoint  
:::

By making the endpoint name the same as the table name, you can simplify development and maintenance of the WebAPI layer.

In some circumstances you may not have direct control over the database, and sometimes you may be exposing a resource that doesn't have a meaningful analogue in the database. In these situations, it may make sense to have different endpoint names - if doing so will simplify development for consumers of your WebAPI endpoints.
