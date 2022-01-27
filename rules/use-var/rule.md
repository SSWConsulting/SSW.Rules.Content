---
type: rule
title: Do you use "var"?
uri: use-var
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:44:06.489Z
guid: edd8d397-3651-47c0-8737-fa38152558d1
---
::: todo
TODO: Byrden - needs a new home (category) and a complete rewrite  
Old content from Better LINQ on .ASPX pasted below
:::
            
<!--endintro-->

Despite what it looks like, the var keyword is not a throwback to the dark ages where we did not have strongly typed variables. It is just a short hand to save developers from typing out the type of a variable.

```
IQueryable<Customers> results =
    from c in dbContext.Customers
    where c.CompanyName.StartsWith(companyNameTextbox.Text)
    select c;
customersBindingSource.DataSource = results;
```
::: bad
Figure: Bad - you should just use "var" instead of "IQueryable"
:::

```
var results =
    from c in dbContext.Customers
    where c.CompanyName.StartsWith(companyNameTextbox.Text)
    select c;
customersBindingSource.DataSource = results;
```
::: good
Figure: Good - using "var" to save few keystrokes
:::