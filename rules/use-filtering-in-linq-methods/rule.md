---
type: rule
title: Do you use the filtering parameter in LINQ methods?
uri: use-filtering-in-linq-methods
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-23T23:54:03.477Z
guid: 214d106b-0c61-472f-bcfe-05f3860c24f3
---
Many LINQ methods like Count, First and so on include an optional filter parameter. It's normally much more readable to use this than add an extra call to Where
            
<!--endintro-->
```cs
.Where(x => x < 5).Count()
.Where(x => x < 5).FirstOrDefault()

```
::: bad
Figure: Bad example - More code that requires extra thought to understand.
:::

```cs
.Count(x => x < 5)

.FirstOrDefault(x => x < 5)
```
::: good
Figure: Good example - Shorter and easier to read.
:::