---
type: rule
title: 'MEF: Do you know not to go overboard with dynamic dependencies?'
uri: mef-do-you-know-not-to-go-overboard-with-dynamic-dependencies
created: 2012-03-21T09:45:50.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​Using Managed Extensibility Framework to load&#160;dynamic dependencies at runtime can be useful, but it's not always required and does have some disadvantages. You shouldn't always look to MEF to implement a dynamic strategy.</p> </span>

<p>​If a reference doesn't need to be dynamically loaded at runtime, it's perfectly fine to have a default constructor that has a hardcoded instantiation of a dependency. If it was never a requirement to make that thing configurable or dynamic, don't invent business requirements just because using an IoC container is &quot;fancier&quot;.</p>
<p>There are disadvantages to using dynamic loading of references&#58;</p>
<ol>
<li>You lose your Code Analysis. Only static references can be analysed by code analysis tools.</li>
<li>You lose your traceability. Visual Studio can no longer show you what concrete method is being called at design time.</li>
</ol>
More details on MEF can be foud here&#58;&#160;<a href="http&#58;//msdn.microsoft.com/en-us/library/dd460648%28v=vs.110%29.aspx" target="_blank">http&#58;//msdn.microsoft.com/en-us/library/dd460648(v=vs.110).aspx</a>​


