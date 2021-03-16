---
type: rule
archivedreason: 
title: Do you catch exceptions precisely?
guid: 1072907b-d837-45e1-9db5-2a9236bf362f
uri: do-you-catch-exceptions-precisely
created: 2013-09-11T19:22:41.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

In the try and catch block, if you always catch for normal [Exception](https://docs.microsoft.com/en-us/dotnet/api/system.exception?redirectedfrom=MSDN&view=net-5.0) you will never know where the true problem is. When using try you should always expect some exception may happen, so in our code we always catch the specific exceptions.

<!--endintro-->

```cpp
try 
{ 
     connection.Open();
}
catch (Exception ex) 
{ 
     return ex.ToString ();
}
```
::: bad
Bad code – Catching the general Exception
:::

```cpp
try 
{ 
     connection.Open(); 
}
catch (InvalidOperationException ex) 
{ 
     return ex.ToString(); 
}
catch (SqlException ex) 
{ 
     return ex.ToString(); 
}
```
::: good
Good code - Catch with specific Exception
:::

