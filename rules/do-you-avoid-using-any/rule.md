---
type: rule
title: Do you avoid using “any”?
uri: do-you-avoid-using-any
created: 2016-04-28T19:32:36.0000000Z
authors:
- id: 55
  title: Steve Leigh

---



<span class='intro'> <p class="p1">TypeScript’s any keyword is a blessing and a curse.&#160; It is a type that can be anything, where every possible property and method exists and also returns any. It can be casted to and from anything and is how you tell the compiler to get out of your way. </p><p class="p1">However, it’s easy to use it as a crutch, and as a result, miss out on handy intellisense, refactoring support and compile-time safety – the main benefits of TypeScript!</p> </span>

<p>Aim to use any in the same way that you use the dynamic keyword in C# - that is, sparingly, and with careful consideration.</p><dl class="badImage"><dt><img src="/PublishingImages/any-bad.png" alt="any-bad.png" data-pin-nopin="true" /></dt><dd>Figure&#58; Bad example&#160;– I can pass anything into this method, so I get bad output at run time (“undefined undefined”)</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/any-good.png" alt="any-good.png" /></dt><dd>Figure&#58; Good example&#160;– using types means I get errors and intellisense support </dd></dl> ​


