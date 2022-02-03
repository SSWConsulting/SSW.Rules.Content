---
type: rule
title: Do you only explicitly include relationships you need?
uri: only-explicitly-include-relationships-you-need
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:12:38.187Z
guid: eaa1b402-b6a0-40d4-9f1b-38befe73b8eb
---
Often developers will include all the related entities in a query to help with debugging. Always remember to take these out. They cause excessive database load.

<!--endintro-->

If you need the related entities, then that is what Include is for.

```
var query = _dbContext
        .Sales
        .Include(x => x.SalesPerson);
```

::: bad
Figure: Bad example - Retrieved the sales records and the salesperson, even though we don't intend to use the salesperson record.
:::

```
var query = _dbContext
        .Sales;
```

::: good
Figure: Good example - Retrieved only the sales records themselves
:::