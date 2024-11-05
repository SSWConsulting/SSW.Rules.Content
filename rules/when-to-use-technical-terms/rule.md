---
seoDescription: It's tempting as developers to use technical terms as they accurately represent a complex concept. We're often told to avoid this and use domain-specific terms instead, but know when to use each is just as important.
type: rule
archivedreason:
title: Do you know when to use technical terms versus domain terms?
uri: when-to-use-technical-names
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - clear-meaningful-names
  - verbs-for-method-names
  - nouns-for-class-names
  - avoid-generic-names
  - avoid-micro-jargon
  - consistent-words-for-concepts
  - avoid-using-your-name-in-client-code
  - use-meaningful-modifiers
  - follow-naming-conventions-for-tests-and-test-projects
guid: 881ea4a4-f8a4-4e2e-a298-1cd020ffd7d5
---

Naming is most effective when it aligns with the audience’s understanding. In code, this often means distinguishing between when to use technical terms, which are clear to developers, and when to use domain-specific terms, which align more closely with business requirements and are familiar to stakeholders. Using technical terms in the wrong context can make code feel disconnected from the business, while overusing domain terms for technical concepts can create confusion.

<!--endintro-->

## Choosing the Right Term
### Use Domain Terms for Business Logic
When naming classes, methods, or variables that represent core business concepts, use terms that reflect the language of the domain. This approach, often called *ubiquitous language* (see our rule [Do you use ubiquitous language?](/ubiquitous-language)), helps ensure that the code is understandable to developers and domain experts alike, reducing the risk of misinterpretation. For example, in a retail application, classes like `Order`, `ProductCatalog`, and `CustomerAccount` use domain terms that match stakeholders' understanding.

### Use Technical Terms for Implementation Details
Conversely, use technical terms for internal or lower-level code that doesn't directly involve business logic. These terms should clearly describe the technical functionality, helping developers quickly understand the purpose without needing domain context. For instance, classes or methods named `CacheInterceptor`, `AnalyticsLogger`, or `CustomerRepository` make sense to developers without domain knowledge, focusing instead on their technical purpose.

:::greybox
Let’s say you’re building an online banking system and need a class to manage the process of logging customer transactions. You name the class `TransactionProcessor`. This name is technically accurate, but it doesn't align well with banking terminology. “Processor” is too generic for the banking context and may not resonate with stakeholders, potentially leading to misunderstandings.
:::
:::bad
Using a technical term that has a potential meaning in the domain context is bound to cause confusion
:::

:::greybox
A better name might be `TransactionLedger` or `TransactionLog`, aligning the term with common banking concepts. This shift helps communicate to both developers and business stakeholders that this component handles logging and auditing of transactions, not merely processing.
:::
:::good
Using domain language helps reflect the business value of the code, and helps all stakeholders (technical and non-technical) work together with a shared understanding
:::

:::greybox
In a retail application, you create a class called `CatalogFetcher` to retrieve the list of products. The name describes its technical function, but it doesn’t align with domain language. “CatalogFetcher” sounds more like an internal utility than a core business concept.
:::
:::bad
Names that describe what something does at a technical level are only valuable for low-level functionality
:::

:::greybox
A clearer, domain-aligned name would be `ProductCatalog`. This name reflects the business term and would be immediately recognizable to anyone familiar with the retail context.
:::
:::good
Code that provides business value is expressed in business terms
:::
