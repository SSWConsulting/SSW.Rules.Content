---
type: rule
archivedreason: 
title: Do you know the best practice for managing state?
guid: ca46ad62-e44e-4266-a68b-e8d1b04e3b08
uri: do-you-know-the-best-practice-for-managing-state
created: 2017-08-15T23:35:06.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
related: []

---


<p>State management is complex and time-consuming.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​​The redux pattern helps resolve this issue.<br></p><dl class="badImage"><dt><img src="/PublishingImages/maintaining-state.png" alt="maintaining-state.png" /></dt><dd>Bad example&#58; maintaining state on individual components</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/redux-logo.png" alt="redux-logo.png" />​​​</dt><dd> Good example&#58; use the redux pattern</dd></dl><p>The 3 principles of the redux pattern&#58;</p><ol><li>The entire state of the application is represented in a single JavaScript object called a store</li><li>The store is acted upon using special functions called reducers</li><li>State is immutable and reducers are the only part of the application that can change state</li></ol>
​<br>


