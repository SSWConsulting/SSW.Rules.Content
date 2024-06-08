---
type: rule
title: Do you use local copies to resolve race condition?
uri: local-copies-to-resolve-race-condition
authors:
  - title: Sylvia Huang
    url: https://ssw.com.au/people/sylvia-huang
created: 2023-07-31T01:19:28.222Z
guid: f49d4f99-522e-433c-a7ab-0e59d78f03df
redirects: 
 - local-copies-to-avoid-race-condition
---
Code that looks perfectly fine in a single-threaded scenario could be vulnerable to race condition when some value is shared among multiple threads.

<!--endintro-->

Examine the following if-statement:

```csharp
if (A is null || (A.PropertyA == SOME_CONSTANT && B))
{
   // some logic
}
```
::: bad
Figure: Bad example - Vulnerable to race condition
:::

When the above code is run single-threaded, the second part of the if-condition would never be reached when A is null. However, if A is shared among multiple threads, the value of A could change from not null to null after passing the first check of if-condition, resulting in a [NRE](https://learn.microsoft.com/en-us/dotnet/api/system.nullreferenceexception?view=net-7.0) in the second check of if-condition.

In order to make the code thread-safe, you should make a local copy of the shared value so that value change caused by another thread would no longer lead to crash.


```csharp
var copyA = A?.PropertyA;

if (A is null || (copyA == SOME_CONSTANT && B))
{
   // some logic
}
```
::: good
Figure: Good example - Local copy to resolve race condition
:::
