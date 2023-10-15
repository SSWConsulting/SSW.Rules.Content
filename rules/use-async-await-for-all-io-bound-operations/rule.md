---
type: rule
title: Do you use async/await for all IO-bound operations?
uri: use-async-await-for-all-io-bound-operations
authors:
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
  - do-you-use-async-await-for-all-io-bound-operations
created: 2019-08-30T17:27:54.000Z
archivedreason: null
guid: eccb6764-2f5f-48b2-9e65-728f583f325d
---
IO-Bound operations are operations where the execution time is not determined by CPU speed but by the time taken for an input/output operation to complete.

Examples include:
* Reading from a hard disk
* Working with a database
* Sending an email
* HTTP REST API calls

It's important to note that all these IO operations are usually several orders of magnitude slower than performing operations against data in RAM.

Modern .NET applications provide a thread pool for handling many operations in parallel. Threads are pooled to mitigate the expense of thread creation and destruction.

If an individual thread is waiting for IO to complete, it is IO blocked and cannot be used to handle any more work until that IO operation is finished.

<!--endintro-->

When using async, the thread is released back to the thread pool while waiting for IO, while the await keyword registers a callback that will be executed after IO completion.

The async/await pattern is most effective when applied “all the way down”. For ASP.NET web applications this means that the Controller Action – which is usually the entry point for a request into your application – should be async.

```cs
public ActionResult Gizmos()
{
    var gizmoService = new GizmoService();
    return View("Gizmos", gizmoService.GetGizmos());
}
```
::: bad
Figure: Bad example – This MVC Controller Action endpoint is not async so the thread assigned to process it will be blocked for the whole lifetime of the request
:::

```cs
public async Task<ActionResult> GizmosAsync()
{
    var gizmoService = new GizmoService();
    return View("Gizmos", await gizmoService.GetGizmosAsync());
}
```
::: good
Figure: Good example - This MVC Controller Action is async. The thread will be released back to the threadpool while waiting for any IO operations under the “gizmoService” to complete 
:::

Above code examples are based on: [Using Asynchronous Methods in ASP.NET MVC 4](https://learn.microsoft.com/en-us/aspnet/mvc/overview/performance/using-asynchronous-methods-in-aspnet-mvc-4)

With these async/await patterns on .NET Core, our applications can handle very high levels of throughput.

Once an async/await based app is under heavy load, the next risk is from thread-pool starvation. Any blocking operations anywhere in the app can tie up threadpool threads – leaving fewer threads in the pool to handle the ongoing throughput. For this reason, the best practice is to ensure that all IO-bound operations are async and to avoid any other causes of blocking.

For more information on understanding and diagnosing thread pool starvation, read: [Diagnosing .NET Core ThreadPool Starvation with PerfView (Why my service is not saturating all cores or seems to stall)](https://learn.microsoft.com/en-us/archive/blogs/vancem/diagnosing-net-core-threadpool-starvation-with-perfview-why-my-service-is-not-saturating-all-cores-or-seems-to-stall).

### Further Information

* [Why would one use Task&lt;T&gt; over ValueTask&lt;T&gt; in C#?](https://stackoverflow.com/questions/43000520/why-would-one-use-taskt-over-valuetaskt-in-c)
* [Diagnosing issues in ASP.NET Core Applications - David Fowler & Damian Edwards](https://www.youtube.com/watch?v=RYI0DHoIVaA)
* [Why your ASP.NET Core application won't scale - Damian Edwards, David Fowler](https://www.youtube.com/watch?v=J-xqz_ZM9Wg)
