---
type: rule
title: Do You Know Which Packages To Add To Your New MVC Project?
uri: do-you-know-which-packages-to-add-to-your-new-mvc-project
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
  - clean-architecture-the-best-way-to-get-started
redirects: []
created: 2014-12-30T00:24:02.000Z
archivedreason: null
guid: ff1fcbc9-abe1-44f8-bfda-1d8720cb3799
---
When you create a new MVC project in Visual Studio it is important to include the right packages from the start. This will make a solution more manageable and developers will be more efficient.

<!--endintro-->

Adding old, obsolete or incorrect packages can lead to decreased performance, scope creep as new requirements are discovered and generally lead to projects suffering.

Some technologies to avoid are :

* MVC Web Forms
* KnockoutJS
* AngularJS
* Gulp

When creating a new MVC project we recommend you use the [Clean Architecture Template](/clean-architecture-the-best-way-to-get-started). This template not only gives you a great structure, but it also includes all the required packages.

The following are some of the NuGet packages included:

* EntityFramework
* FluentValidation
* NSwag
* AutoMapper
* MediatR

The following are some of the NPM packages included:

* Angular
* FontAwesome
* RxJs
* Bootstrap
* TypeScript

Part of     [SugarLearning Developer Induction](https://sugarlearning.com/companies/SSW/modules/5099/induction-day-3-developer-induction).
