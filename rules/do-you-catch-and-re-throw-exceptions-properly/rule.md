---
type: rule
title: Do you catch and re-throw exceptions properly?
uri: do-you-catch-and-re-throw-exceptions-properly
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related: []
redirects: []
created: 2013-09-11T21:16:44.000Z
archivedreason: null
guid: d8992617-dcae-4dca-b775-9e417507d1b5
---

A good catch and re-throw will make life easier while debugging, a bad catch and re-throw will ruin the exception's stack trace and make debugging difficult.

Catch and rethrow where you can usefully add more information that would save a developer having to work through all the layers to understand the problem.

<!--endintro-->

```cs
catch {} 

catch (SomeException) {} 

catch { throw; } 

catch (SomeException) { throw; } 
```
::: bad
Bad Example - Never use an empty catch block. Do something in the block or remove it.
:::

```cs
catch (SomeException ex) { throw ex; } 

catch (SomeException ex) { someMethod(); throw ex; } 
```
::: bad
Bad Example - Never re-throw exceptions by passing the original exception object. Wrap the exception or use throw.
:::

Using `throw ex` resets the stack trace, obscuring the original the error and may hide highly valuable information to debug this exception.


```cs
catch (SomeException) 
{ 
     someMethod(); 
     throw; 
}
```

::: good
Good Example - Calling throw  
:::

If you are following the [Clean Architecture](https://github.com/jasontaylordev/CleanArchitecture) pattern - catching and rethrowing is useful for preventing your Infrastructure details from leaking into your Application e.g. we use a SQL server

```cs
catch (SqlException ex) when (ex.Number == 2601)
{
     throw new IdAlreadyTakenException(ex);
}
```
::: good
Good Example - By rethrowing a specific exception, my application code now doesn't need to know that there is a SQL database or the magic numbers that SQL exceptions use
:::
