---
type: rule
title: Do you expose events as events?
uri: do-you-expose-events-as-events
created: 2018-04-30T19:30:42.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> You should&#160;expose events as events.​<br> </span>

<p class="ssw15-rteElement-CodeArea">​ public Action<br>&lt; connectioninformation &gt; ConnectionProblem;</p><dd class="ssw15-rteElement-FigureBad">Bad code​<br></dd><p class="ssw15-rteElement-CodeArea"> public event Action<br>&lt; connectioninformation &gt; ConnectionProblem;</p><dd class="ssw15-rteElement-FigureGood">​​​Good code​​<br></dd>


