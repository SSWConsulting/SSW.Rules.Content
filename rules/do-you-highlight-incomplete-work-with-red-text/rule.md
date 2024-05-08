---
type: rule
archivedreason: Covered by [https://www.ssw.com.au/rules/todo-tasks](/rules/todo-tasks)
title: Do you highlight incomplete work with red text?
guid: a45d8542-685d-4774-9f28-da9a5022c75f
uri: do-you-highlight-incomplete-work-with-red-text
created: 2014-06-11T05:40:53.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

It is important that users of your application who provide feedback have very clear indications of work that is not yet complete, to avoid feedback on sections of your application that are still under development.

<!--endintro-->

Also, see our [rule on colour usage in Windows Forms](https://www.ssw.com.au/ssw/Standards/rules/rulestobetterwindowsforms.aspx#RedYellowDesigner).

::: bad  
![Figure: Bad example - A tester or a Product Owner who comes to this page may believe that it is broken, or that the developers have 'missed' it. Always be clear about what parts of your application are not yet ready for feedback](4e246f\_bad-incomplete-work.jpg)  
:::

::: good  
![Figure: Good example - It is clear to testers and to the Product Owner that this page is incomplete, but they can get more details from the Product Backlog](400e3f\_good-incomplete-work.jpg)  
:::

::: good  
![Figure: Best example - Use feature toggles to not show incomplete elements to testers or Product Owners](5b99bb\_best-incomplete-work.jpg)
:::

[See FeatureToggle by Martin Fowler](https://martinfowler.com/articles/feature-toggles.html). Feature Toggling can require a large amount of extra work and so is often only implemented by teams with a need to ship features while others are still in development
