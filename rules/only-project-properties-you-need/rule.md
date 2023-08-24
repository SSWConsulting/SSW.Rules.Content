---
type: rule
title: Do you only project properties you need?
uri: only-project-properties-you-need
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:06:46.280Z
guid: 18e53b62-b8c0-4cbf-bd85-447c10950f70
---
When retrieving data it's much more efficient to only collect the data you need. It saves computation and IO on the database and also saves memory and CPU on the calling side.

<!--endintro-->

::: bad
```cs
IEnumerable<string> GetProductGuids(string category)
{
    IEnumerable<Product> products = context.Products
        .Where(x => x.Category == category)
        .ToList();
  
    return products.Select(x => x.ProductGuid);
}
```

Figure: Bad example - Retrieved the whole product record when we only needed 1 property
:::

::: good
```cs
IEnumerable<string> GetProductGuids(string category)
{
    IEnumerable<string> productGuids = context.Products
        .Where(x => x.Category == category)
        .Select(x => x.ProductGuid)
        .ToList();
      
    return productGuids;
}
```

Figure: Good example - Retrieved only the required property.
:::