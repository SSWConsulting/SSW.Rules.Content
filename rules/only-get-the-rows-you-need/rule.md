---
seoDescription: Only retrieve database rows that match your criteria to save time and resources.
type: rule
title: Do you only get the rows you need?
uri: only-get-the-rows-you-need
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T16:59:04.256Z
guid: 654730c9-8678-4295-9168-e67049c96041
---

It's expensive retrieving data from a database, as such it's important to only ask for the rows you require when getting data.

<!--endintro-->

Entity Framework nicely translates the various filters like the Where method into SQL WHERE clauses. This makes it really easy to write nice readable code that is also very efficient.

```csharp
List<Sale> sales = context.Sales.ToList();
foreach (var sale in sales)
{
    if (sale.ProductId == request.ProductId)
    {
        // Do stuff
    }
}
```

::: bad
Bad example - Retrieved all the data instead of items that matched the product id.
:::

```csharp
List<Sale> sales = context.Sales
      .Where(sale => sale.ProductId == Request.ProductId)
      .ToList();

foreach (var sale in sales)
{
    // Do stuff
}
```

::: good
Good example - Only the data required was retrieved from the database
:::
