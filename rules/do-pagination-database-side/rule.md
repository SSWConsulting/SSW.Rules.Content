---
type: rule
title: Do you do pagination database side?
uri: do-pagination-database-side
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:19:34.260Z
guid: ef94f559-ea04-4c00-8b27-f8f7b80f07f4
redirects:
- do-pagination-server-side

---

Pagination can be expensive if all the pages are retrieved from the database before grabbing the relevant page. It's much more efficient to get only the page number requested back from the database.

<!--endintro-->

```
var query = context
    .Sales
    .AsNotTracking()
    .Where(x => x.SalesPersonId == salesPersonId);
var result = await query.ToListAsync(ct);
int count = result.Count;

result = result
    .Skip(page * pageSize)
    .Take(pageSize);
return (count, result);
```

::: bad
Figure: Bad example - Reads all the data from the database, counts the records and filters down to the page
:::

```
var query = context
    .Sales
    .AsNotTracking()
    .Where(x => x.SalesPersonId == salesPersonId);

int count = await query.CountAsync(ct);

query = query
    .Skip(page * pageSize)
    .Take(pageSize);
var result = await query.ToListAsync(ct);    
return (count, result);
```

::: good
Figure: Good example - Reads only the count and 1 page of data from the database
:::
