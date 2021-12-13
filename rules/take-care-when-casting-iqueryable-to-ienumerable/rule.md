---
type: rule
title: Do you take care when casting IQueryable to IEnumerable?
uri: take-care-when-casting-iqueryable-to-ienumerable
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:00:03.219Z
guid: ee5bfbb5-7743-462b-bc8a-f32b3fb015b0
---
When you cast IQueryable to IEnumerable and then query the data from there, Entity Framework must collect the data at the point you do the cast.
            
<!--endintro-->

### Counting
```
context.Sales.ToList().Count The ToList generates a list of all records client side and then counts them
IEnumerable<Sale> sales = context.Sales; This implicitly treats the sales as an enumerable and enumerates all the items to count them
return sales.Count;	
```
::: bad
Bad example
:::

```
context.Sales.Count
```
::: good
Good example
:::

### Where
```
private IEnumerable<Sale> Sales {get {return context.Sales;}}
return Sales.Where(x => x.Id == 5).ToList();
```
::: bad
Bad example
:::

```
private IQueryable<Sale> Sales {get {return context.Sales;}}
return Sales.Where(x => x.Id == 5).ToList();
```
::: good
Good example
:::