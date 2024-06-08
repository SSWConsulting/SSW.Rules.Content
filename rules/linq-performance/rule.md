---
type: rule
archivedreason:
title: Do you know how to get the best performance out of LINQ?
guid: 7c56242c-4ecc-45e1-a689-97ddea0a26a6
uri: linq-performance
created: 2023-09-18T11:18:00.000Z
authors:
  - title: Alex Rothwell
    url: https://www.ssw.com.au/people/alex-rothwell
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
related: []
---

LINQ is a super powerful toolkit, letting you get your business logic implemented in .NET using a standard set of operations.
While it may be tempting to use it in every scenario, it's important to remember to profile and benchmark any code that is time sensitive for your application.
            
<!--endintro-->

## Getting started with profiling
Once you've identified that you've got a performance issue in your application, rather than assuming what the problem is, it's time to profile.
[Profiling your application](/do-you-profile-your-code-when-optimising-performance) will allow for method level insights into what's being called, how often, and how long each call takes.

Armed with your profiling results, you can now identify any hot spots in the application.
Effectively eliminating these is made far easier by benchmarking alternatives for fixing efficiency issues.

## Benchmarking your options
Once the cause of the slowness has been identified, it should be isolated so that multiple fixes can be tried and compared through benchmarking.
Much like profiling helps identify the exact cause of the slowness, rather than relying on intuition; benchmarking helps identify which fix is actually going to help the most.

While you can set up your benchmarking manually, it's much easier when using a library like [BenchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet).

The entire benchmarking process is showcased well by Nick Chapsas:

`youtube: https://www.youtube.com/watch?v=K1Ye_QEpAq8`
**Video: Stop using LINQ to order your primitive collections in C# - [Nick Chapsas](https://www.youtube.com/@nickchapsas) (14 min)**

The above video very clearly shows one of the cases where LINQ may not be the optimal solution.
Here, LINQ provides very easy-to-use Order and OrderBy methods but there may be better implementations available, depending on the collection that needs sorting.

LINQ may often be the easy solution to implement, but if you find the application needing better performance, you may need to inspect your LINQ usage and investigate if there's better and more appropriate alternatives available.

