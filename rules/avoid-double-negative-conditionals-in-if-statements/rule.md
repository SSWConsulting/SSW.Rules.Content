---
type: rule
archivedreason: 
title: Do you avoid Double-Negative Conditionals in if-statements?
guid: 994524f4-cb01-4dbb-b2fa-0fea1642839f
uri: avoid-double-negative-conditionals-in-if-statements
created: 2018-04-24T22:03:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-double-negative-conditionals-in-if-statements

---

Try to avoid Double-Negative Conditionals in if-statements. Double negative conditionals are difficult to read because developers have to evaluate which is the positive state of two negatives. So always try to make a single positive when you write if-statement.

<!--endintro-->



```cs
if (!IsValid)
{
        // handle error
}
else
{
       // handle success
}
```






::: bad
Figure: Bad example

:::



```cs
if (IsValid)
{
       // handle success
}
else
{
       // handle error
}
```






::: good
Figure: Good example

:::



```cs
if (!IsValid)
{
       // handle error
}
```




::: good
Figure: Another good example
:::


Use pattern matching for boolean evaluations to make your code even more readable!
```cs
if (IsValid is false)
{
       // handle error
}
```




::: good
Figure: Even better
:::
