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



<span class='intro'> <img class="ms-rteCustom-ImageArea" alt="inject" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/dependency-injection-bad.jpg" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example – N-Tiered architectures do not inherently support dependency injection</span> <img class="ms-rteCustom-ImageArea" alt="inject" src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/dependency-injection-good.jpg" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good Example – The Onion Architecture promotes layers built on interfaces, and then injecting dependencies into those layers. This keeps coupling low, and therefore maintainability high</span>  </span>

<p>The classes in each layer can depend on layers toward the centre.</p>
<p>It emphasizes the use of interfaces for the business logic and repository layers. The repository layer corresponds to the Data Access layer in an n-Tier architecture.</p>
<p>An n-Tier architecture has at its base the database.<br>The core of the onion architecture is the Domain Model, and all dependencies are injected. This leads to more maintainable applications since it emphasizes separation of concerns.</p>


