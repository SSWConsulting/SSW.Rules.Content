---
type: rule
title: Do you name your events properly?
uri: name-your-events-properly
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-name-your-events-properly
created: 2018-04-30T22:51:18.000Z
archivedreason: null
guid: 41af34f0-03c8-41f2-a85d-370420630d2a
---
Events should end in "ing" or "ed".

<!--endintro-->

```csharp
public event Action
< connectioninformation > ConnectionProblem;
```

::: bad
Bad example
:::

```csharp
public event Action
< connectioninformation > ConnectionProblemDetected;
```

::: good
Good example
:::
