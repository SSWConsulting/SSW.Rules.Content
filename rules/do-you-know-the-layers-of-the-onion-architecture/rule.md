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
<dt>​<a target="_blank" href="/Documents/Onion-Architecture.pdf" style="border&#58;medium none;"><img class="ms-rteCustom-ImageArea" alt="Onion Architecture" src="/PublishingImages/Onion-Architecture.jpg" /></a></dt>
<dd>Figure&#58; The layers of the onion architecture</dd></dl>
 </span>

<h3>Application Core (the grey stuff)</h3><p>This should be the big meaty part of the application where the domain logic resides. </p><h3>Domain Model</h3><p>In the very centre we see the Domain Model, which represents the state and behaviour combination that models truth for the organization and is only coupled to itself.</p><h3>Repository Interfaces</h3><p>The first layer around the Domain Model is typically where we find interfaces that provide object saving and retrieving behaviour.&#160;<br>The object saving behaviour is not in the application core, however, because it typically involves a database.&#160; Only the interface is&#160;in the application core.&#160; The actual implementation is a dependency which is injected. </p><h3>Business Logic Interfaces</h3><p>Business logic is also exposed via interfaces to provide decoupling of business logic. 
   <br>Examples of where this is useful include substituting a FacebookNotificationService for an EmailNotificationService or a FedExShippingCalculator for a DHLShippingCalculator</p><h3>Clients (the red stuff)</h3><p>The outer layer is reserved for things that change often.&#160; E.g. UI and the other applications that consume the Application Core.&#160;<br>This includes the MVC project.<br>Any interface dependencies in factories, services, repositories, etc, are injected into the domain by the controller.<br>This means any constructor-injected interfaces in domain classes are resolved automatically by the IoC container.</p><h3>Dependencies</h3><p>Dependencies are implementations of interfaces defined in&#160;Repository and Business Logic Interfaces&#160;and&#160;Domain.<br>These classes are specific implementations and can be coupled to a particular method of data access, or specific service technology.<br>e.g. this is where the EF DbContext is implemented, as well as things like logging, email sending, etc.<br>These dependencies are injected into the application core. 
   <br>Because the Application core only relies on abstractions of the dependencies, it is easy to update them.<br>The Onion Architecture relies heavily on the&#160;<a href="http&#58;//en.wikipedia.org/wiki/Dependency_inversion_principle">Dependency Inversion </a> 
   <span></span><span></span><span>principle</span>and other 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=21a9d999-80cd-4e39-a5f5-c511522ffcb2">SOLID principles</a>.</p><h4>References&#58;</h4><ul><li>
      <a href="http&#58;//blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/">http&#58;//blog.tonysneed.com/2011/10/08/peeling-back-the-onion-architecture/</a></li><li>
      <a href="http&#58;//stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371">http&#58;//stackoverflow.com/questions/9732747/what-type-of-architecture-is-this-called/9933371#9933371</a></li></ul><h3 class="ssw15-rteElement-H3"> 
   ​Use SSW Data Onion to Generate your Code<br></h3><p>To help make this process pain free, we've developed the <a href="http&#58;//www.sswdataonion.com/">SSW Data Onion​</a>&#160;to get you going and take away the boilerplate code you would normally need to write. Check out this cool video to see how it works&#58;<br></p><p>​</p><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"><iframe width="853" height="480" src="https&#58;//www.youtube.com/embed/FcuFya8vud8?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0"></iframe>&#160;</div><p><br></p><div> 
   <span style="line-height&#58;21px;">
      <br></span></div><p> 
   <strong>Further Reading&#58;</strong><a href="/Pages/Use-a-Dependency-Injection-Centric-Architecture.aspx">Do You Use a Dependency Injection Centric Architecture?</a> </p><p> 
​</p>


