---
type: rule
title: Do you use LINQ as a query language?
uri: use-linq-as-a-query-language
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-22T05:14:09.892Z
guid: e05038c8-e0d5-478f-8bc1-91336b535d2a
---


LINQ won't execute any of the subcalls until it needs too. It simply builds an expression tree. This can result in the side effects described below if you break the 'don't modify anything' rule.

<!--endintro-->

One of the core tenets of LINQ is that it is a query language designed for retrieving data, not updating it. 

There are a few rules around what not to do:
- Project data in a Select, don't modify it
- ForEach is not a LINQ method (do not use it in a LINQ query)
- Remember LINQ lazy executes, so if you don't force the evaluation, it won't happen.

So in the example below we have a list of products. I want to increase StockOnHand of product by 5 (if it's oversold this may still be less than 0)
```cs
List<Product> products = ...
var outOfStock = products
	.Select(x => {x.StockOnHand += 5; return x;})
    .Where(x => x.StockOnHand <= 0);

var inStockCount = products.Count(x => x.StockOnHand > 0);
var outOfStockCount = outOfStock.Count();

```
::: bad
Bad example : StockOnHand does not get updated before the foreach, it only gets evaluated when the enumerator for outOfStock is enumerated. This is unexpected from a quick glance at the code.
:::

The above example modified data in a select meaning subsequent calls didn't behave as expected.

```cs
List<Product> products = ...
foreach(var product in products)
{
    product.StockOnHand += 5;
}

inStockCount = products.Count(x => x.StockOnHand > 0);
outOfStockCount = products.Count(x => x.StockOnHand <= 0);
```
::: good
Good Example : StockOnHand is updated for each item in products before being used in any LINQ queries.
:::

It's important to be aware of this to avoid unexpected side effects like this.