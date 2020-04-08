---
type: rule
title: Do You Use a Dependency Injection Centric Architecture ?
uri: do-you-use-a-dependency-injection-centric-architecture-
created: 2012-10-19T19:11:41.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 40
  title: Igor Goldobin

---



<span class='intro'> <img class="ms-rteCustom-ImageArea" alt="inject" src="/PublishingImages/dependency-injection-bad.jpg" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example – N-Tiered architectures do not inherently support dependency injection</span> <img class="ms-rteCustom-ImageArea" alt="inject" src="/PublishingImages/dependency-injection-good.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good Example – The Onion Architecture promotes layers built on interfaces, and then injecting dependencies into those layers. This keeps coupling low, and therefore maintainability high</span>  </span>

<p>The classes in each layer can depend on layers toward the centre.</p><p>It emphasizes the use of interfaces for the business logic and repository layers. The repository layer corresponds to the Data Access layer in an n-Tier architecture.</p><p>An n-Tier architecture has at its base the database.<br>The core of the onion architecture is the Domain Model, and all dependencies are injected. This leads to more ​maintainable applications since it emphasizes separation of concerns.</p>
<h4> Further Reading&#58; </h4><ul><li>
      <a href="/Pages/The-layers-of-the-onion-architecture.aspx">Do you know the layers of the onion architecture?</a></li><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=0aa194e1-2de9-4ed1-b430-444109d65a50">Do you know the best dependency injection container​?​</a></li></ul>


