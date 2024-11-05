---
seoDescription: We often use ours or our company name to denote a custom version of something. Unless you're publishing a library, this is never a good idea.
type: rule
archivedreason:
title: Do you use ubiquitous language?
uri: ubiquitous-language
created: 2024-11-05T00:00:00.0000000Z
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related:
  - encapsulate-domain-models
  - use-specification-pattern
  - anemic-vs-rich-domain-models
  - consistent-words-for-concepts
  - avoid-micro-jargon
  - when-to-use-technical-names
guid: f8555180-50c2-423e-84e2-d73a9018222f
---

Ubiquitous language is a core principle in domain-driven design (DDD) that encourages developers and stakeholders to use the same vocabulary when discussing business logic and domain concepts. By using a shared, domain-specific language across code, documentation, and conversations, you ensure that everyone has a common understanding of core concepts. This approach reduces misunderstandings and makes the codebase more accessible to those familiar with the business domain.

<!--endintro-->

## Why Ubiquitous Language Matters
Ubiquitous language helps bridge the gap between technical and non-technical stakeholders, creating a consistent and clear understanding of the domain. When everyone uses the same terms — whether in code, documentation, or discussions — it’s easier to align on requirements, troubleshoot issues, and onboard new team members. Without it, terms can become muddled, causing confusion and misinterpretation.

:::greybox
Let’s say you’re working on an insurance system, and the domain term “policyholder” is used consistently among stakeholders. However, in the codebase, you see different terms used interchangeably: `AccountOwner`, `Customer`, and `InsuredParty`. Each of these terms could technically represent the policyholder, but the inconsistency can lead to confusion and misunderstandings about the exact role of each entity.
:::
:::bad
Terms in the code do not reflect domain language used by stakeholders
:::

:::greybox
To follow ubiquitous language, you would use `PolicyHolder` consistently across the codebase, aligning the code’s vocabulary with the language used by domain experts. This approach eliminates ambiguity, making it clear that `PolicyHolder` refers to the specific entity recognized by all stakeholders.
:::
:::good
Ubiquitous language is used, and developers and stakeholders are on the same page
:::

### Benefits
* **Improved Communication:** By using the same terms as domain experts, developers and stakeholders communicate more effectively, reducing the risk of misinterpretation.
* **Increased Readability:** Consistent terminology makes it easier for anyone familiar with the domain to understand the codebase.
* **Enhanced Maintenance:** When domain terms are used uniformly, developers spend less time deciphering concepts and more time building functionality.

:::greybox
💡 **Tip:** You can use the [Contextive](https://github.com/dev-cycles/contextive) extension for IntelliJ and VS Code (other IDEs coming soon) to assist with this. The linked repo also has a discussion between Chris Simon (the author) and [SSW's Gert Marx](https://www.ssw.com.au/people/gert-marx/) about both the extension and ubiquitous language in general
:::
