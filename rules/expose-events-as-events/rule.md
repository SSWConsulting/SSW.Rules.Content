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


You should&#160;expose events as events.​<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​ public Action<br>&lt; connectioninformation &gt; ConnectionProblem;</p><dd class="ssw15-rteElement-FigureBad">Bad code​<br></dd><p class="ssw15-rteElement-CodeArea"> public event Action<br>&lt; connectioninformation &gt; ConnectionProblem;</p><dd class="ssw15-rteElement-FigureGood">​​​Good code​​<br></dd>


