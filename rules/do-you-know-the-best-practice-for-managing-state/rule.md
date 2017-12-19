---
type: rule
title: Do you know the best practice for managing state?
uri: do-you-know-the-best-practice-for-managing-state
created: 2017-08-15T23:35:06.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​State management is complex and time-consuming.​​​<br><br></p> </span>

<p>The redux pattern helps resolve this issue.<br></p><dl class="badImage"><dt><img src="/PublishingImages/maintaining-state.png" alt="maintaining-state.png" /><br></dt><dd>Bad example&#58; maintaining state on individual components</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/redux-logo.png" alt="redux-logo.png" /> <br></dt><dd> Good example&#58; use the redux pattern</dd></dl><p>The 3 principles of the redux pattern&#58;</p><ol><li>The entire state of the application is represented in a single JavaScript object called a store</li><li>The store is acted upon using special functions called reducers<br></li><li>State is immutable and reducers are the only part of the application that can change state<br></li></ol><div><font color="#333333">redux-saga&#160;is a library that aims to make redux application side effects.<br></font></div><div><font color="#333333">The&#160;advantage of using redux-saga&#58;</font></div><div><ol><li>Collects all asynchronous&#160;in one place, make code clear.<br></li><li>Use&#160;ES6 feature called Generators to make those asynchronous flows easy to read, write and test.</li><li>Generator also let&#160;these asynchronous flows look like your standard synchronous(kind of like&#160;async/await at .net) which&#160;Solve the callback hell.<br></li></ol></div>


