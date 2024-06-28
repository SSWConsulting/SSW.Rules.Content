---
seoDescription: New MVC projects require specific packages to ensure efficiency and scalability.
type: rule
title: Do you know which packages to add to new MVC projects?
uri: packages-to-add-to-your-mvc-project
authors:
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Andrew Harris
    url: https://ssw.com.au/people/andrew-harris
related:
  - clean-architecture-get-started
redirects:
  - do-you-know-which-packages-to-add-to-your-new-mvc-project
created: 2014-12-30T00:24:02.000Z
archivedreason: null
guid: ff1fcbc9-abe1-44f8-bfda-1d8720cb3799
---

When you create a new MVC project in Visual Studio it is important to include the right packages from the start. This will make a solution more manageable and developers will be more efficient.

<!--endintro-->

Adding old, obsolete or incorrect packages can lead to decreased performance, scope creep as new requirements are discovered and generally lead to projects suffering.

❌ Some technologies to **avoid** are:

* MVC Web Forms
* KnockoutJS
* AngularJS
* Gulp

When creating a new MVC project, we recommend you use the [Clean Architecture Template](/clean-architecture-get-started). This template not only gives you a great structure, but it also includes all the required packages.

✅ Some of the NuGet packages included:

* EntityFramework
* FluentValidation
* NSwag
* AutoMapper
* MediatR

✅ Some of the NPM packages included:

* Angular
* FontAwesome
* RxJs
* NgRx
* Bootstrap
* TypeScript

::: info
**Note:** This is part of [SugarLearning Developer Induction](https://sugarlearning.com/companies/SSW/modules/5099/induction-day-3-developer-induction).
:::
