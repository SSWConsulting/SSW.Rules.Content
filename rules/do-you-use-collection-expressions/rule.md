---
type: rule
archivedreason: 
title: C# Code - Do you use collection expressions to keep your code clean?
guid: 012FDB70-5108-413D-BDCA-27DC24A9722C
uri: do-you-use-collection-expressions
created: 2023-12-06T00:00:00.0000000Z
authors:
- title: Daniel Mackay
  url: https://ssw.com.au/people/daniel-mackay
related: []
redirects: 
---

Do you know collection expressions can make your code cleaner?  They can be used to create arrays, lists, and other collections in a single line of code.

<!--endintro-->

``` cs
var numbers1 = new List<int> {1, 2, 3, 4, 5};
```
::: bad
Figure: Bad example - Verbose way of constructing a list 
:::

``` cs
var numbers2 = new[] { 1, 2, 3, 4, 5 };
```
::: ok
Figure: OK example - using implicit arrays
:::

``` cs
List<int> numbers3 = [1, 2, 3, 4, 5];
```
::: good
Figure: Good example - using collection expressions
:::

Another advantage of collection expressions is that they can be passed into methods accepting different types of list collections.  The compiler is smart enough to determine the correct underlying type.

```cs
Foo([1,2,3]);
Foo2([1,2,3]);
Foo3([1,2,3]);

void Foo(IEnumerable<int> numbers)
{
    // Do work
}

void Foo2(List<int> numbers)
{
    // Do work
}

void Foo3(int[] numbers)
{
    // Do work
}
```
**Figure: Versatile use of collection expressions in methods with varying collection types**

For more information on collection expressions see here: [learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/collection-expressions)
