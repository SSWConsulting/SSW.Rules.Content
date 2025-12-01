---
seoDescription: Avoid common issues with if-statements by using curly brackets to group multiple statements and prevent errors when adding more code later.
type: rule
archivedreason:
title: Do you know how to avoid problems in if-statements?
guid: 92b0df3a-dece-492f-b2f8-256890d8d03a
uri: how-to-avoid-problems-in-if-statements
created: 2018-04-24T22:00:00.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-how-to-avoid-problems-in-if-statements
---

Try to avoid problems in if-statements without curly brackets and just one statement which is written one line below the if-statement. Use just one line for such if-statements. If you want to add more statements later on and you could forget to add the curly brackets which may cause problems later on.

<!--endintro-->

```cs
if (ProductName == null) ProductName = string.Empty; if (ProductVersion == null)
 ProductVersion = string.Empty; if (StackTrace == null) StackTrace = string.Empty;
```

::: bad
Figure: Bad Example
:::

```cs
if (ProductName == null)
{
 ProductName = string.Empty;
}
if (ProductVersion == null)
{
 ProductVersion = string.Empty;
}
if (StackTrace == null)
{
 StackTrace = string.Empty;
}
```

::: good
Figure: Good Example  
:::
