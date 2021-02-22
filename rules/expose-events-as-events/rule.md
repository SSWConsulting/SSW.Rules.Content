---
type: rule
archivedreason: 
title: Do you expose events as events?
guid: a322a946-b020-4f03-b20e-afd5ec089323
uri: expose-events-as-events
created: 2018-04-30T19:30:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-expose-events-as-events

---

You should expose events as events.

<!--endintro-->



```
public Action
< connectioninformation > ConnectionProblem;
```




::: bad
Bad code

:::



```
public event Action
< connectioninformation > ConnectionProblem;
```




::: good
Good code

:::
