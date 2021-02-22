---
type: rule
archivedreason: 
title: Do you know the layers of the onion architecture?
guid: aa31cbec-f7bf-463c-ab4f-02c346fdc14b
uri: do-you-know-the-layers-of-the-onion-architecture
created: 2012-10-19T19:23:27.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
related: []
redirects: []

---


<dl class="image"><dt>​​​<a target="_blank" href="/Documents/Onion-Architecture.pdf"><img alt="Onion Architecture" src="Onion-Architecture.jpg" /></a></dt><dd>Figure: The layers of the onion architecture</dd></dl>
<br><excerpt class='endintro'></excerpt><br>
<h3>Application Core (the grey stuff)</h3><p>This should be the big meaty part of the application where the domain logic resides.</p><h3>Domain Model</h3><p>In the very centre, we see the Domain Model, which represents the state and behaviour combination that models truth for the organization and is only coupled to itself.</p><h3>Repository Interfaces</h3><p>The first layer around the Domain Model is typically where we find interfaces that provide object saving and retrieving behaviour. <br>The object saving behaviour is not in the application core, however, because it typically involves a database.  Only the interface is in the application core.  The actual implementation is a dependency which is injected.</p><h3>Business Logic Interfaces</h3><p>Business logic is also exposed via interfaces to provide decoupling of business logic. <br>Examples of where this is useful include substituting a FacebookNotificationService for an EmailNotificationService or a FedExShippingCalculator for a DHLShippingCalculator</p><h3>Clients (the red stuff)</h3><p>The outer layer is reserved for things that change often.  E.g. UI and the other applications that consume the Application Core. <br>This includes the MVC project.<br>Any interface dependencies in factories, services, repositories, etc, are injected into the domain by the controller.<br>This means any constructor-injected interfaces in domain classes are resolved automatically by the IoC container.</p><h3>Dependencies</h3><p>Dependencies are implementations of interfaces defined in Repository and Business Logic Interfaces and Domain.<br>These classes are specific implementations and can be coupled to a particular method of data access, or specific service technology.<br>e.g. this is where the EF DbContext is implemented, as well as things like logging, email sending, etc.</p><p>These dependencies are injected into the application core.</p><p>Because the Application core only relies on abstractions of the dependencies, it is easy to update them.</p><p>​The Onion Architecture relies heavily on the <a href="http://en.wikipedia.org/wiki/Dependency_inversion_principle">Dependency Inversion</a> principle and other <a href=/do-you-know-the-common-design-principles-part-1>SOLID principles</a>.<br>(Note: Onion Architecture has been replaced by <a href=/rules-to-better-clean-architecture>Clean Architecture</a>)<br><br></p><h4>References:</h4><ul><li>
      <a href="http://blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/">http://blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/</a></li><li>
      <a href="http://stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371">http://stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371#9933371</a></li></ul><h3 class="ssw15-rteElement-H3">Use SSW Data Onion to Generate your Code<br></h3><p>To help make this process pain free, we've developed the <a href="http://www.sswdataonion.com/">SSW Data Onion</a> to get you going and take away the boilerplate code you would normally need to write. Check out this cool video to see how it works:<br></p><p>​</p><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"><iframe width="853" height="480" src="https://www.youtube.com/embed/FcuFya8vud8?rel=0&controls=0&showinfo=0" frameborder="0"></iframe> </div><p>​<br></p><p> 
   <strong>Further Reading: </strong><a href="/Pages/Use-a-Dependency-Injection-Centric-Architecture.aspx">Do You Use a Dependency Injection Centric Architecture?</a> </p><p> 
​</p>


