---
type: rule
title: Do you know when to use StringBuilder?
uri: when-to-use-stringbuilder
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-when-to-use-stringbuilder
created: 2019-01-12T01:08:17.000Z
archivedreason: null
guid: 9f1e383d-3369-47fb-8e04-42db96f18432
---

A String object is immutable - this means if you append two Strings together, the result is an entirely new String, rather than the original String being modified in place. This is inefficient because creating new objects is slower than altering existing objects.

Using StringBuilder to append Strings modifies the underlying Char array rather than creating a new String. Therefore, whenever you are performing multiple String appends or similar functions, you should always use a StringBuilder to improve performance.

<!--endintro-->

```cs
String s = "";

for (int i = 0; i < 1000; i ++) {
  s += i;
}
```
::: bad
Figure: Bad example - This inefficient code results in 1000 new String objects being created unnecessarily
:::

```cs
StringBuilder sb = new StringBuilder();

for (int i = 0; i < 1000; i ++) {
  sb.append(i);
}
```
::: good
Figure: Good example - This efficient code only uses one StringBuilder object
:::

See [StringBuilder Class](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-7.0) for more details.
