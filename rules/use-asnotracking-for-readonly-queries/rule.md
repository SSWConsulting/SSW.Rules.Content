---
type: rule
title: Do you use AsNoTracking for readonly queries?
uri: use-asnotracking-for-readonly-queries
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:05:36.001Z
guid: 664e47fa-8634-429a-8c54-a7be1d97b6b2
---
One of EF Core's best features is the fact it tracks any changes you make to entity after you retrieve it. However this comes with a cost, if the data is only being read and the returned entities will never be modified then you can use the AsNoTracking method to inform EF Core not to bother tracking changes. 

This results in fairly significant memory and CPU improvements on the client side.

<!--endintro-->

```
return context.Sales.AsNoTracking().Where(x => x.Id == 5).ToList();
```
            


