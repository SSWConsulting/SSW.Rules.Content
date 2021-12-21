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

```
IEnumerable<string> GetProductGuids(string category)
{
  return context.Products
      .Where(x => x.Category == category)
      .ToList()
      .Select(x => x.ProductGuid);
}
```

::: bad
Figure: Bad example - Retrieved the whole product record when we only needed 1 property
:::

```
IEnumerable<string> GetProductGuids(string category)
{
  return context.Products
      .Where(x => x.Category == category)
      .Select(x => x.ProductGuid)
      .ToList();
}
```

::: good
Figure: Good example - Retrieved only the required property.
:::