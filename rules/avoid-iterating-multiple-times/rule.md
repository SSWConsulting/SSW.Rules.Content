---
type: rule
title: Do you avoid iterating multiple times?
uri: avoid-iterating-multiple-times
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-22T05:14:11.473Z
guid: 977d44f6-fc2a-4ead-ab01-910cbbfdefef
---


Due to LINQ expressions being lazy executed, it is a important to avoid re-evaluating the expression. For LINQ extension methods, this is critically important.
<!--endintro-->

There are 2 problems with multiple evaluations:
- It is needlessly expensive
- It may not be possible

Some IEnumerables may be tied to something like a Stream that doesn't support seeking. In this case, the enumeration can only occur once. This is true of the web request Content stream. That would mean that you simply can't enumerate it again as to start the enumeration again would require seeking back to the start.

```cs
public IEnumerable<Product> UpdateStockLevels(IEnumerable<Product> products)
{
    if (products.Any())
    {
        ... IfAnyItemsExist()
    }

    foreach (var product in products)
    {
        ... OnEachItem()
    }
}
```
::: bad
Figure: Bad example - Calls any which enumerates the first item and then foreach which forces a second evaluation
:::

```cs
public IEnumerable<Product> UpdateStockLevels(IEnumerable<Product> products)
{
    var first = true;    
    foreach (var product in products)
    {
        if (first)
        {
            ... IfAnyItemsExist()
        }
        ... OnEachItem()
        first = false;
    }
}
```
::: good
Figure: Good example - Only enumerates once
:::

The worst part about this is that you may test it against an array, or some other input and it may seem fine. This is especially true with unit testing, as typically an incoming stream of objects is simulated by just providing a fixed array or list, but these will support re enumeration where the real input in your application may not.