---
type: rule
archivedreason: 
title: Do you use async/await for all IO-bound operations?
guid: eccb6764-2f5f-48b2-9e65-728f583f325d
uri: use-async-await-for-all-io-bound-operations
created: 2019-08-30T17:27:54.0000000Z
authors:
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-use-async-await-for-all-io-bound-operations

---


<p>IO-Bound operations are operations where the execution time is not determined by CPU speed but by the time taken for an input/output operation to complete.​</p><p>​​​​Examples include&#58;</p><div><div><ul><li>Reading from a hard disk</li><li>Woking with a database</li><li>Sending an email<br></li><li>HTTP REST API&#160;calls<br></li></ul><p>It's important to note that all these IO operations are usually several orders of magnitude slower than performing operations against data in RAM.</p><p>Modern .NET applications provide a thread pool for handling many operations in parallel. Threads are pooled to mitigate the expense of thread creation and destruction.</p><p>If an individual thread is waiting for IO to complete, it is IO blocked and cannot be used to handle any more work until that IO operation is finished.<br></p></div></div>
<br><excerpt class='endintro'></excerpt><br>
<p>​When using async, the thread is released back to the thread pool while waiting for IO, while the await keyword registers a callback that will be executed after IO completion.</p><p>The async/await pattern is most effective when applied “all the way down”. For ASP.NET web applications this means that the Controller Action – which is usually the entry point for a request into your application – should be async.<br></p><p class="ssw15-rteElement-CodeArea">public ActionResult Gizmos()<br>&#123;<br>&#160;&#160;&#160; var gizmoService = new GizmoService();<br>&#160;&#160;&#160; return View(&quot;Gizmos&quot;, gizmoService.GetGizmos());<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example – this MVC Controller Action endpoint is not async so the thread assigned to process it will be blocked for the whole lifetime of the request​<br></dd><p class="ssw15-rteElement-CodeArea"> 
   <br>public async Task{ltHTMLChar}ActionResult{gtHTMLChar} GizmosAsync()<br>&#123;<br>&#160;&#160;&#160; var gizmoService = new GizmoService();<br>&#160;&#160;&#160; return View(&quot;Gizmos&quot;, await gizmoService.GetGizmosAsync());<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example this MCV Controller Action is async. The thread will be released back to the threadpool while waiting for any IO operations under the “gizmoService” to complete&#160;<br></dd><p> 
   <br>Above code examples are based on&#58; 
   <a href="https&#58;//docs.microsoft.com/en-us/aspnet/mvc/overview/performance/using-asynchronous-methods-in-aspnet-mvc-4">https&#58;//docs.microsoft.com/en-us/aspnet/mvc/overview/performance/using-asynchronous-methods-in-aspnet-mvc-4</a></p><p>With these async/await patterns on .NET​ Core, our applications can handle very high levels of throughput.</p><p>Once an async/await based app is under heavy load, the next risk is from thread-pool starvation. Any blocking operations anywhere in the app can tie up threadpool threads – leaving fewer threads in the pool to handle the ongoing throughput. For this reason, the best practice is to ensure that all IO-bound operations are async and to avoid any other causes of blocking.</p><p>​For more information on understanding and diagnosing thread pool starvation, read&#58;&#160;<a href="https&#58;//blogs.msdn.microsoft.com/vancem/2018/10/16/diagnosing-net-core-threadpool-starvation-with-perfview-why-my-service-is-not-saturating-all-cores-or-seems-to-stall/">https&#58;//blogs.msdn.microsoft.com/vancem/2018/10/16/diagnosing-net-core-threadpool-starvation-with-perfview-why-my-service-is-not-saturating-all-cores-or-seems-to-stall/</a><br></p><h3 class="ssw15-rteElement-H3">Further Information&#58;​<br></h3><ul><li>
      <a href="https&#58;//stackoverflow.com/questions/43000520/why-would-one-use-taskt-over-valuetaskt-in-c">https&#58;//stackoverflow.com/questions/43000520/why-would-one-use-taskt-over-valuetaskt-in-c</a></li><li>
      <a href="https&#58;//www.youtube.com/watch?v=RYI0DHoIVaA">https&#58;//www.youtube.com/watch?v=RYI0DHoIVaA</a></li><li>
      <a href="https&#58;//www.youtube.com/watch?v=J-xqz_ZM9Wg">https&#58;//www.youtube.com/watch?v=J-xqz_ZM9Wg</a><br></li></ul>


