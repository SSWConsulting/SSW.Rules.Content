---
type: rule
title: Do you know when to use Entity Framework?
uri: when-to-use-entity-framework
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T16:53:12.200Z
guid: 834a4950-e20a-49ee-8c9d-8e7bbdcc84ba
---
::: todo
TODO: Byrden - Do you know why you are using linq (Complete rewrite)   
Old content from Better LINQ on .ASPX pasted below
:::

<!--endintro-->

```cs
using (SqlConnection conn = new SqlConnection())
      {
      conn.ConnectionString = "Data Source=(local);Initial Catalog=Northwind;Integrated Security=True";
      conn.Open();
  
      SqlCommand cmd = conn.CreateCommand();
      cmd.CommandText = "SELECT * FROM Customers WHERE CompanyName LIKE '" + companyNameTextbox.Text + "%'";
  
      bindingSource1.DataSource = cmd.ExecuteReader();\
  }
```
::: bad
Figure: Bad example - using ADO.NET and not strongly typed
:::

```cs
* var results =
      from c in dbContext.Customers
      where c.CompanyName.StartsWith(companyNameTextbox.Text)
      select c;
  customersBindingSource.DataSource = results;
  
  // or even
  
  var results =
      from c in dbContext.Customers
      where c.CompanyName.StartsWith(companyNameTextbox.Text)
      select new {c.CompanyName, c.Phone};
  customersBindingSource.DataSource = results;
```
::: good
Figure: Good example - at least 4 good reasons below
:::

1. More readable and less code
2. Less performance issues - Most serious .NET performance issues were because of unclosed connections. LINQ means no connection code needed to be done.
   LINQ is another layer and really is overhead.
3. Strongly typed fields - SQL tables/entities has intellisense
4. Strongly typed SQL - SQL (Familiar SQL like syntax aka LINQ) has intellisense
