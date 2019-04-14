---
type: rule
title: Do you know the main principles of Clean Architecture?
uri: do-you-know-the-main-principles-of-clean-architecture
created: 2019-04-14T21:34:38.0000000Z
authors:
- id: 81
  title: Jason Taylor

---



<span class='intro'> <p>With Clean Architecture the Domain and the Application layers are at the centre of the design. This is known as the Core of the application. The Domain layer contains the enterprise logic and types and the Application layer contains the business logic and types. The difference being that enterprise logic could be shared with other systems whereas business logic would typically be specific to this system.<br></p><dl class="image"><dt><img src="/PublishingImages/onion-view-clean-architecture.png" alt="onion-view-clean-architecture.png" style="width&#58;600px;height&#58;600px;" /></dt><dd>Figure&#58; Onion View of Clean Architecture​<br></dd></dl> </span>

<p>Instead of having Core depend on data access and other infrastructure concerns we invert these dependencies, therefore Infrastructure, Persistence, and Presentation all depend on Core. This is achieved by adding abstractions, such as interfaces or abstract base classes, to the Application layer. Layers outside of Core, such as Infrastructure and Persistence, then implement these abstractions.</p><p>A good example is an implementation of the Repository pattern. Within this design, we would first add an IRepository interface to the Application layer. Next, we would implement this interface within Persistence by creating a Repository class using our preferred data access technology. Finally, within Core the logic we write will only use the IRepository interface, so Core will remain independent of data access concerns.</p><p>With this design, all dependencies must flow inwards. Core has no dependencies on any outside layers. Infrastructure, Persistence, and Presentation depend on Core, but not on one another.<br></p><p>This results in an architecture and design that is&#58;<br></p><ul><li><strong>Independent of Frameworks</strong>&#160;-&#160;<em>Core should not be dependent on external frameworks such as Entity Framework</em></li><li><b>Testable </b>-<b></b><em>The logic within Core can tested independently of anything external, such as UI, databases, servers. Without external dependencies the tests are very simple to write.</em></li><li><strong>Independent of UI</strong>&#160;-&#160;<em>It is easy to swap out the Web UI for a Console UI, or Angular for Vue. Logic is contained within Core, so changing the UI will not impact logic.</em></li><li><b>Independent of Database&#160;</b>-<b>&#160;</b><em>Initially you might choose SQL Server or Oracle, but soon we will all be switching to Cosmos DB</em></li><li><b>Independent of anything agency </b>-<b>&#160;</b><em>Core simply doesn't know anything about the outside world</em></li></ul><p></p><p>While the design in the below figure only includes three circles, you may need more - just think of this as a starting point.<br></p><h3 class="ssw15-rteElement-H3">​References</h3><ul><li><a href="http&#58;//blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html">The Clean Architecture</a></li><li><a href="https&#58;//docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/common-web-application-architectures#clean-architecture">Clean architecture</a><br></li></ul>


