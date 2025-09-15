---
seoDescription: Why use Entity Framework? Simplify database interactions and query complexity with a strongly typed object framework.
type: rule
title: Do you know why to use Entity Framework?
uri: why-to-use-entity-framework
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T16:53:12.200Z
guid: 834a4950-e20a-49ee-8c9d-8e7bbdcc84ba
redirects:
  - when-to-use-entity-framework
---

Entity Framework allows you to provide a strongly typed object framework (ORM) over your database. This helps abstract the database away allowing it to be replaced with other technologies as needed.

<!--endintro-->

```cs
using (SqlConnection conn = new SqlConnection())
{
    conn.ConnectionString = "Data Source=(local);Initial Catalog=Northwind;Integrated Security=True";
    conn.Open();

    SqlCommand cmd = conn.CreateCommand();
    cmd.CommandText = "SELECT * FROM Customers WHERE CompanyName LIKE '" + companyNameTextbox.Text + "%'";

    bindingSource1.DataSource = cmd.ExecuteReader();
}
```

::: bad
Figure: Bad example - using ADO.NET and not strongly typed
:::

```cs
var results = dbContext.Customers
    .Where(c => c.CompanyName.StartsWith(companyNameTextbox.Text));
customersBindingSource.DataSource = results;

// Or even
var results = dbContext.Customers
    .Where(c => c.CompanyName.StartsWith(companyNameTextbox.Text))
    .Select(c => new
    {
        c.CompanyName,
        c.Phone
    });
customersBindingSource.DataSource = results;
```

::: good
Figure: Good example - at least 4 good reasons below
:::

1. Making queries that are independent from specific Database engine
2. Strongly typed fields - SQL tables/entities have intellisense
3. More readable and less code
4. It's easy to chain more operation like `OrderBy`, `GroupBy`, `FirstOrDefault`, `Count`, `Any` and many more
5. Developers are generally poor at writing SQL, so using code constructs makes writing queries much easier
