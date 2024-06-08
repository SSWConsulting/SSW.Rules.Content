---
type: rule
title: Do you avoid materializing an IEnumerable?
uri: avoid-materializing-an-ienumerable
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-22T05:11:19.642Z
guid: 58a95e21-8c5e-4be6-b4e8-1f3689c7045b
---
This is the golden rule of LINQ. You generally have no idea how big the IEnumerable might be, so where possible just iterate through, don't force it into an array or list before doing that.
<!--endintro-->
 The primary reason for this is that your input stream might not fit into RAM, and you will cause unnecessary object creation and garbage collection which will also consume a lot of CPU on top of eating memory for breakfast.

```cs
foreach(var product in products.ToList())
{
	// Do something
} 
```
::: bad
Figure: Bad example - This creates a list with all of the products in RAM before iterating over them. This can very easily cause an OutOfMemoryException.
:::

```cs
foreach(var product in products)
{
    	// Do something
}
```
::: good
Figure: Good example - Doesn't force the data to be read into memory before iterating. This will behave nicely even for an infinite enumerator.
:::

Don't materialize an IEnumerable, just iterate it. ie don't ToList or ToArray it until it's been filtered. Do not assume that the input stream fits in RAM. 