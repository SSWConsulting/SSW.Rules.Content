---
type: rule
archivedreason: 
title: Do you name your events properly?
guid: 41af34f0-03c8-41f2-a85d-370420630d2a
uri: do-you-name-your-events-properly
created: 2018-04-30T22:51:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- name-your-events-properly

---

Events should end in "ing" or "ed".


<!--endintro-->



```
public event Action
< connectioninformation > ConnectionProblem;
```



::: bad
Bad code

:::



```
public event Action
< connectioninformation > ConnectionProblemDetected;
```



::: good
Good code  
:::
