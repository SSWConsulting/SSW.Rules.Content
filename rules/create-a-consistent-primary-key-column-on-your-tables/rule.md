---
type: rule
archivedreason: 
title: Schema - Do you create a consistent primary key column on your tables?
guid: 9dc11961-9ede-4e90-8c37-44b9a5ba9bbc
uri: create-a-consistent-primary-key-column-on-your-tables
created: 2019-11-06T18:21:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-create-a-consistent-primary-key-column-on-your-tables

---

Make sure you created a consistent primary key column named  **Id** on your tables.

<!--endintro-->

```sql
Employee.ID, Employee.EmployeeId, Employee.EmployeeID, Employee.Employee_Code, Employee.Employee
```

::: bad
Figure: Bad example

:::

```sql
Employee.Id
```

::: good
Figure: Good example
:::

### Why?
* We shouldn’t capitalise ID (identifier) as it is an abbreviation not an acronym.
* Using the approach \[TableName\]Id, e.g. EmployeeId, is redundant as we already know the context of the Id.
