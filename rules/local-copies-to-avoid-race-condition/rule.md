---
type: rule
title: Do you use local copies to avoid race condition?
uri: local-copies-to-avoid-race-condition
authors:
  - title: Sylvia Huang
    url: https://ssw.com.au/people/sylvia-huang/
created: 2023-07-31T01:19:28.222Z
guid: f49d4f99-522e-433c-a7ab-0e59d78f03df
---
Code looks perfectly fine in a single-threaded scenario could be vulnerable to race condition when some value is shared among multiple threads.

Examine the following if-statement:

::: bad

```csharp
if (A is null || (A.PropertyA == SOME_CONSTANT && B))
{
   // some logic
}
```
Figure: Bad example - vulnerable to race condition
:::

When the above code is run single-threaded, the second part of the if-condition would never be reached when A is null. However, if A is shared among multiple threads, the value of A could change from not null to null after passing the first check of if-condition, resulting in a [NRE](https://learn.microsoft.com/en-us/dotnet/api/system.nullreferenceexception?view=net-7.0) in the second check of if-condition.

In order to make the code thread-safe, you should make a local copy of the shared object so that value change caused by another thread would no longer lead to crash.

::: good

```csharp
var copyA = A?.PropertyA;

if (A is null || (copyA == SOME_CONSTANT && B))
{
   // some logic
}
```
Figure: Good example - local copy to avoid race condition
:::