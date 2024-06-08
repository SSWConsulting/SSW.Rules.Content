---
type: rule
archivedreason: 
title: Do you document the technologies, design patterns and ALM processes?
guid: d9aaae27-b77a-4263-b5a8-4b8aeff51c81
uri: do-you-document-the-technologies-design-patterns-and-alm-processes
created: 2013-07-15T21:25:49.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

The technologies and design patterns form the architecture that is usually the stuff that is hard to change.

A pattern allows using a few words to a dev and he knows exactly what coding pattern you mean.

ALM is about refining the work processes.

<!--endintro-->

::: greybox
We are doing this project using C#
:::
::: bad
Bad example - you know nothing about how the project will be done
:::

::: greybox
* **Technologies:** WebAPI. The DI container is Structure Map. Entity Framework. Typescript. Angular
* **Patterns:** Repository and Unit of Work (tied to Entity Framework to remove additional abstraction), IOC
* **ALM:** Scrum with 2-week Sprints and a Definition of Done including StyleCop to green
* **ALM:** Continuous deployment to staging
:::
::: good
Good example - this tells you a lot about the architecture and processes in a few words
:::

The important ones for most web projects:

1. **Technologies: WebAPI**
2. **Patterns: Single responsibly** - if it does more than one thing, then split it.
 Eg. If it checks the weather and gets data out of the database, then split it.
3. **Patterns: Inversion of control / dependency injection** 
 Eg. If your controller needs to get data, then you inject the component that gets the data.
4. **Patterns: Repository/Unit of Work** - repository has standard methods for getting and saving data. The code calling the repository should not know where the data lives.
 Eg. A User Repository could be saving to Active Directory or CRM and it should not affect any other code
 You may or may not choose to have an additional abstraction away from entity framework.
5. **ALM: Scrum** - kind of a pattern for your process.
Eg. Sprint Review every 2 weeks.
 Mostly a senior architect should be added for that 1 day each 2 weeks.

The decisions the team makes regarding these 3 areas, should be documented as per [Do you make awesome documentation?](/do-you-review-the-documentation)
