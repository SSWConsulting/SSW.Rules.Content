---
type: rule
archivedreason: 
title: Do you catch and re-throw exceptions properly?
guid: d8992617-dcae-4dca-b775-9e417507d1b5
uri: do-you-catch-and-re-throw-exceptions-properly
created: 2013-09-11T21:16:44.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

A good catch and re-throw will make life easier while debugging, a bad catch and re-throw will ruin the exception's stack trace and make debugging difficult.

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
Bad Example - Never re-throw exceptions by passing the original exception object. Wrap the exception or use throw; instead.
:::

```cs
catch (SomeException ex) 
{ 
     someMethod(); 
     throw; 
}

catch (SomeException ex) 
{ 
     someMethod(); 
     SomeOtherException wrapperEx = new SomeOtherException("This is a wrapper exception", ex);
     throw wrapperEx; 
}
```
::: good
Good Example - Good code
:::
