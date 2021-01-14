---
type: rule
archivedreason: 
title: Do You Know Which Packages To Add To Your New MVC Project?
guid: ff1fcbc9-abe1-44f8-bfda-1d8720cb3799
uri: do-you-know-which-packages-to-add-to-your-new-mvc-project
created: 2014-12-30T00:24:02.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

When you create a new MVC project in Visual Studio it is important to include the right packages from the start. This makes the project more manageable and you become more efficient in producing your final result.

<!--endintro-->

If you add old, obsolete or incorrect NuGet packages, the project will suffer and you might have decreased performance or scope creep as new requirements are discovered.

Avoid old technologies such as:

* MVC Web Forms
* KnockoutJS

When you create a project you should be adding the following NuGet Packages:

* SSW.DataOnion
* SSW.HealthCheck
* AutoFac
* Serilog


You should also add the following NPM  packages:

* Angular JS
* Bootstrap
* Gulp


**Note** : Prior to 2016, SSW recommend developers choose bower over NPM as their front end package manager. That recomendation has changed due to the industry trend away from bower.

![](Bower_v_NPM.png)

::: good
Figure: NPM Popularity has been increasing

:::

Part of     [SugarLearning Developer Induction](https://sugarlearning.com/companies/SSW/modules/5099/induction-day-3-developer-induction).
