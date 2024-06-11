---
seoDescription: C# developers can simplify variable declarations by using the "var" keyword to infer the type from the initial assignment.
type: rule
title: Do you use "var"?
uri: use-var
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
created: 2021-12-13T17:44:06.489Z
related:
  - consistent-code-style
guid: edd8d397-3651-47c0-8737-fa38152558d1
---

In C# the "var" keyword can be used instead of providing an explicit type when declaring a variable. The type is then inferred from the initial assignment of the variable.

<!--endintro-->

It is just a short hand to save developers from typing out the type of a variable.

```
List<string> items = new List<string>();
```

::: bad
Figure: Bad example - You should just use "var" instead of "List<string>"
:::

```
var item = new List<string>();
```

::: good
Figure: Good example - Using "var" to save a few keystrokes and reduce repetition
:::

This can be kept consistent by creating an [editorconfig file](/consistent-code-style) which can then generate compile time warnings.

An [example editor config](https://github.com/SSWConsulting/SSW.CleanArchitecture/blob/main/.editorconfig), look for the **var preferences**.
