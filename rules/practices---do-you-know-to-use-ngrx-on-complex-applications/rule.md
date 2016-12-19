---
type: rule
title: Practices - Do you know to use NgRx on complex applications?
uri: practices---do-you-know-to-use-ngrx-on-complex-applications
created: 2016-08-02T14:25:26.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> State management is complex and time-consuming.<br>On large applications it becomes very difficult to maintain state. The redux pattern helps resolve this issue.<br>​​<br>
<p>ngrx is the redux pattern implemented for Angular 2. <a href="https&#58;//github.com/ngrx" target="_blank">View on GitHub</a>. <br></p> </span>

<dl class="image"><dt> <img src="/PublishingImages/ngrx.png" alt="ngrx.png" data-pin-nopin="true" /> </dt><dd>Figure&#58; ngrx supercharges the redux pattern with RxJS <br></dd><dd></dd></dl><p>Benefits&#58;</p><ul><li>Easy state management</li><li>Better tooling and debugging</li><li>Simpler applications to build</li><li>Increased performance<br></li><li>Code that is easy to test<br></li></ul><dl class="image"><dt> <img src="/PublishingImages/img1.png" alt="img1.png" /> </dt><dd>Figure&#58; ngrx supercharges the redux pattern with RxJS <br></dd></dl><dl class="image"><dt><img src="/PublishingImages/img2.png" alt="img2.png" /></dt><dd>Figure&#58; The redux pattern is a way to implement a predictable state container</dd></dl><p>The three principles of the redux pattern&#58;</p><ol><li>The entire state of the application is represented in a single JavaScript object called a store.</li><li>The store is acted upon using special functions called reducers.&#160;</li><li>State is immutable and reducers are the only part of the application that can change state.</li></ol>
​<br>


