---
type: rule
archivedreason: 
title: Practices - Do you write small components?
guid: 1c5fbef9-bfa1-4986-bc81-a1028bebfec3
uri: practices---do-you-write-small-components
created: 2016-04-22T22:43:46.0000000Z
authors:
- id: 55
  title: Steve Leigh
related: []

---


<p class="p1">The Single Responsibility Principle is a well understood, and well-accepted tenant of good code design.  It states that a class should do one thing, and do it well – and an Angular component is no exception.</p><p class="p1">When designing components, keep them small, modular and reusable. For example, if you have a menu, put it into a menu component, don’t put it in your app component.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><img src="comp-1.png" alt="comp-1.png" style="width:800px;" /></dt><dd>Figure: Bad example - Having just 3 components for the page makes it difficult to reuse, maintain and test​<br></dd></dl><dl class="goodImage"><dt><img src="comp-2.png" alt="comp-2.png" style="width:800px;" /></dt><dd>Figure: Good example - Splitting up the page into 11 components means they are small and targeted - and thus easy to maintain and test. Components can be reused on other pages</dd></dl>​


