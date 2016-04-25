---
type: rule
title: Practices - Do you write small components?
uri: practices---do-you-write-small-components
created: 2016-04-22T22:43:46.0000000Z
authors:
- id: 55
  title: Steve Leigh

---



<span class='intro'> <p class="p1">The <a href="https&#58;//en.wikipedia.org/wiki/Single_responsibility_principle">Single Responsibility Principle </a>&#160;is a well understood, and&#160;well-accepted&#160;tenant of good code design.&#160; It states that a class should do one thing, and do it well – and an Angular2 component is no exception.</p><p class="p1">When designing components, keep them small, modular and reusable. For example, if you have a menu, put it into a menu component, don’t put it in your app component.</p> </span>

<dl class="badImage"><dt><img src="/PublishingImages/comp-1.png" alt="comp-1.png" style="width&#58;800px;" /></dt><dd>Figure&#58; Bad example - Having just 3 components for the page makes it difficult to reuse, maintain and test.</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/comp-2.png" alt="comp-2.png" style="width&#58;800px;" /></dt><dd>Figure&#58; Good example - Splitting up the page into 11 components means they are small and targeted - and thus easy to maintain and test. Components can be reused on other pages</dd></dl>​


