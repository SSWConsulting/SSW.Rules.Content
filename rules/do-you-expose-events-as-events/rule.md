---
type: rule
archivedreason: 
title: Do you expose events as events?
guid: a322a946-b020-4f03-b20e-afd5ec089323
uri: do-you-expose-events-as-events
created: 2018-04-30T19:30:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

You should expose events as events.

<!--endintro-->

public Action
&lt; connectioninformation &gt; ConnectionProblem;


::: bad
Bad code

:::


public event Action
&lt; connectioninformation &gt; ConnectionProblem;


::: good
Good code

:::
