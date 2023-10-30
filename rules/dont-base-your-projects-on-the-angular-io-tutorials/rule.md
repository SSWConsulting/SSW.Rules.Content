---
type: rule
archivedreason: 
title: Do you know the right way to create your Angular project?
guid: bc2dd342-6109-461f-8e9b-cd6b3e5aaa4e
uri: dont-base-your-projects-on-the-angular-io-tutorials
created: 2016-10-27T21:33:46.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-know-the-right-way-to-create-your-angular-project

---

[Angular.io](http://angular.io/) is a great place to get started learning Angular, and since the Angular CLI is now an official Angular project, these docs now include using the CLI from the beginning.

<!--endintro-->

The [Quick Start](https://angular.io/docs/ts/latest/quickstart.html) and [Tour of Heros Tutorial](https://angular.io/docs/ts/latest/tutorial/) will teach you lots about Angular.

For an enterprise real-world project you should also consider:

1. **Whether your application will require the redux pattern**  
See [Do you know to use ngrx on complex applications?](/use-ngrx-on-complex-applications)

2. **Do you need a UI framework?**  
See [Do you know the best UI framework for Angular?](/the-best-ui-framework-for-angular-2)

There are also several well-used templates that incorporate Angular and server-side tooling.

While these starters often include advanced functionality, we prefer to implement pure Angular CLI projects where possible because Angular updates frequently.. and when you are using someone else's template that incorporates Angular you are left with the options of waiting for them to update their template to the latest version of Angular, or working out how to do it yourself. This can often leave you with large amounts of work or be being several months behind the latest versions.

To learn how to build  **enterprise Angular applications** check out [Angular Dev Superpowers Tour](https://www.ssw.com.au/events/angular-superpowers-tour).

::: good  
![Figure: Good Example - The Angular CLI will create you a new Angular project with a single command, and that project will be set up with production build, unit testing, and end-to-end testing all configured. If you have very specific build requirements, the CLI also supports custom web pack builds](create-angular-good.png)  
:::
