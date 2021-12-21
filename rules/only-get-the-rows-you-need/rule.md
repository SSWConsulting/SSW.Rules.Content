---
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



```
List<Sale> sales1 = context.Sales.ToList();
foreach(var sale in sales1)
{
    if(sale.ProductId == request.ProductId)
    {
        // Do stuff
    }
}
```

::: bad
Bad example - Retrieved all the data instead of items that matched the product id.
:::

```
List<Sale> sales1 = context
      .Sales
      .Where(sale => sale.ProductId == Request.ProductId)
      .ToList();
      
foreach(var sale in sales1)
{
    // Do stuff
}
```

::: good
Good example - Only the data required was retrieved from the database
:::