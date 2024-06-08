---
type: rule
title: Do you expose events as events?
uri: expose-events-as-events
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-expose-events-as-events
created: 2018-04-30T19:30:42.000Z
archivedreason: null
guid: a322a946-b020-4f03-b20e-afd5ec089323
---
You should expose events as events.

<!--endintro-->

```csharp
public Action
< connectioninformation > ConnectionProblem;
```

::: bad
Bad code

:::

```csharp
public event Action
< connectioninformation > ConnectionProblem;
```

::: good
Good code

:::