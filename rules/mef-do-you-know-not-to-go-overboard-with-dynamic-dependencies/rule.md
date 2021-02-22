---
type: rule
archivedreason: >-
  Is anyone using MEF on their projects?


  Matt Wicks


  [RE: [SSW] Rules to Better Architecture and Code Review]
title: 'MEF: Do you know not to go overboard with dynamic dependencies?'
guid: 0e823f82-0fd5-43e4-8645-95a2da3b8449
uri: mef-do-you-know-not-to-go-overboard-with-dynamic-dependencies
created: 2012-03-21T09:45:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Using Managed Extensibility Framework to load dynamic dependencies at runtime can be useful, but it's not always required and does have some disadvantages. You shouldn't always look to MEF to implement a dynamic strategy.

<!--endintro-->

If a reference doesn't need to be dynamically loaded at runtime, it's perfectly fine to have a default constructor that has a hardcoded instantiation of a dependency. If it was never a requirement to make that thing configurable or dynamic, don't invent business requirements just because using an IoC container is "fancier".

There are disadvantages to using dynamic loading of references:

1. You lose your Code Analysis. Only static references can be analysed by code analysis tools.
2. You lose your traceability. Visual Studio can no longer show you what concrete method is being called at design time.

 More details on MEF can be foud here: [http://msdn.microsoft.com/en-us/library/dd460648(v=vs.110).aspx](http&#58;//msdn.microsoft.com/en-us/library/dd460648%28v=vs.110%29.aspx)
