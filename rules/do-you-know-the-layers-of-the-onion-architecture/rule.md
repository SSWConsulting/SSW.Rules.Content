---
type: rule
title: Do you know the layers of the onion architecture?
uri: do-you-know-the-layers-of-the-onion-architecture
created: 2012-10-19T19:23:27.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
- id: 37
  title: Ben Cull

---



<span class='intro'> <dl class="image">
<dt><a target="_blank" href="/SoftwareDevelopment/RulesToBetterMVC/Documents/Onion-Architecture.pdf" style="border&#58;medium none;"><img class="ms-rteCustom-ImageArea" alt="Onion Architecture" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/Onion-Architecture.jpg" /></a></dt>
<dd>Figure&#58; The layers of the onion architecture</dd></dl>
 </span>

<h3>Application Core (the grey stuff)</h3><p>This should be the big meaty part of the application where the domain logic resides. </p><h3>Domain Model</h3><p>In the very centre we see the Domain Model, which represents the state and behaviour combination that models truth for the organization and is only coupled to itself.</p><h3>Repository Interfaces</h3><p>The first layer around the Domain Model is typically where we find interfaces that provide object saving and retrieving behaviour.&#160;<br>The object saving behaviour is not in the application core, however, because it typically involves a database.&#160; Only the interface is&#160;in the application core.&#160; The actual implementation is a dependency which is injected. </p><h3>Business Logic Interfaces</h3><p>Business logic is also exposed via interfaces to provide decoupling of business logic. 
   <br>Examples of where this is useful include substituting a FacebookNotificationService for an EmailNotificationService or a FedExShippingCalculator for a DHLShippingCalculator</p><h3>Clients (the red stuff)</h3><p>The outer layer is reserved for things that change often.&#160; E.g. UI and the other applications that consume the Application Core.&#160;<br>This includes the MVC project.<br>Any interface dependencies in factories, services, repositories, etc, are injected into the domain by the controller.<br>This means any constructor-injected interfaces in domain classes are resolved automatically by the IoC container.</p><h3>Dependencies</h3><p>Dependencies are implementations of interfaces defined in&#160;Repository and Business Logic Interfaces&#160;and&#160;Domain.<br>These classes are specific implementations and can be coupled to a particular method of data access, or specific service technology.<br>e.g. this is where the EF DbContext is implemented, as well as things like logging, email sending, etc.<br>These dependencies are injected into the application core. 
   <br>Because the Application core only relies on abstractions of the dependencies, it is easy to update them.<br>The Onion Architecture relies heavily on the&#160;<a href="http&#58;//en.wikipedia.org/wiki/Dependency_inversion_principle">Dependency Inversion </a><span></span><span></span><span>principle</span>and other 
   <a href="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouKnowCommonDesignPrinciples.aspx">SOLID principles</a>.</p><h4>References&#58;</h4><ul><li>
      <a href="http&#58;//blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/">http&#58;//blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/</a></li><li>
      <a href="http&#58;//stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371">http&#58;//stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371#9933371</a></li></ul><p><strong>Further Reading&#58;</strong> <a href="/SoftwareDevelopment/RulesToBetterMVC/Pages/Use-a-Dependency-Injection-Centric-Architecture.aspx">Do You Use a Dependency Injection Centric Architecture?</a></p>


