---
type: rule
archivedreason: 
title: Practices - Do you know to use NgRx on complex applications?
guid: 4dfae201-17ca-4d5e-90de-90dd492c3e1b
uri: use-ngrx-on-complex-applications
created: 2016-08-02T14:25:26.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- practices-do-you-know-to-use-ngrx-on-complex-applications

---


<div><p class="ssw15-rteElement-InfoBox">
      <b>​Heads Up​&#58;</b> For new teams creating their first SPA using Angular, it is recommend to limit the initial focus to learning Angular, TypeScript, and RxJs. Avoid including advanced state management patterns such as NgRx, unless someone on the team has prior experience. Start with a simple approach to state management and evolve your design once the team has mastered the basics. When your team is ready, be sure to investigate the multitude of patterns, supporting libraries, and best practices available for advanced state management. If you are developing an application that absolutely requires advanced state management then be sure to invest in some training and / or enlist the help of another developer with the right skillset.</p>
   <br>​​State management is complex and time-consuming.</div><div>On large applications, it becomes very difficult to maintain state. The redux pattern helps resolve this issue.<br>​​<br> 
   <p>NgRx&#160;is the redux pattern implemented for Angular. 
      <a href="https&#58;//github.com/ngrx" target="_blank">View on GitHub</a>. 
      <br></p></div>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> <img src="/PublishingImages/ngrx.png" alt="ngrx.png" data-pin-nopin="true" /> </dt><dd>Figure&#58; NgRx supercharges the redux pattern with RxJS <br></dd><dd></dd></dl><p>Benefits&#58;</p><ul><li>Easy state management</li><li>Better tooling and debugging</li><li>Simpler applications to build</li><li>Increased performance<br></li><li>Code that is easy to test<br></li></ul><dl class="image"><dt> <img src="/PublishingImages/img1.png" alt="img1.png" /> </dt><dd>Figure&#58; NgR​x supercharges the redux pattern with RxJS <br></dd></dl><dl class="image"><dt><img src="/PublishingImages/img2.png" alt="img2.png" /></dt><dd>Figure&#58; The redux pattern is a way to implement a predictable state container</dd></dl><p>The three principles of the redux pattern&#58;</p><ol><li>The entire state of the application is represented in a single JavaScript object called a store.</li><li>The store is acted upon using special functions called reducers.&#160;</li><li>State is immutable and reducers are the only part of the application that can change state.<br></li></ol><h3 class="ssw15-rteElement-H3">What do we mean by complex?<br></h3><p>State management such as ngrx is most useful when applied to shared data&#160; - that can be changed or &quot;mutated&quot; in multiple ways. When applied to data that is not shared there is a risk&#160;of adding much more effort with little value<br></p><p class="ssw15-rteElement-P"><strong>Simple Example</strong><br></p><p class="ssw15-rteElement-P">&quot;Add a company edit form to capture a company's&#160;address and contact details, when the user clicks 'save', we send a HTTP POST to an API&quot;.&#160;<br><br>In this type of scenario, the company details you are editing are not&#160;shared with&#160;any other&#160;component so you get little benefit from using state management.<br></p><p class="ssw15-rteElement-P"><strong>Complex example</strong><br></p><p class="ssw15-rteElement-P">&quot;Add&#160;a checkout screen where users can change&#160;order&#160;quantities and see the totals immedately update. Also there is a widget in the toolbar that shows number of items and cart total at all times&quot;<br></p><p class="ssw15-rteElement-P">This type of complexity is perfect for ngrx! The state of your shopping cart can be in kept&#160;the Store an both the main Checkout Component and the&#160;Cart widget can be kept in sync by selecting this state from the store and raising actions to mutate that state in controlled and predictable ways.<br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><br><br></p><p class="ssw15-rteElement-P">&#160;<br></p><p><br></p><p><br></p><p><br></p><p><br></p>
​<br>


