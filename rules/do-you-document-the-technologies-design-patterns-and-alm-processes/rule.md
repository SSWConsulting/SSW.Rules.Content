---
type: rule
archivedreason: 
title: Do you document the technologies, design patterns and ALM processes?
guid: d9aaae27-b77a-4263-b5a8-4b8aeff51c81
uri: do-you-document-the-technologies-design-patterns-and-alm-processes
created: 2013-07-15T21:25:49.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The technologies and design patterns form the architecture that is usually the stuff that is hard to change.

A pattern allows using a few words to a dev and he knows exactly what coding pattern you mean.

ALM is about refining the work processes.

<!--endintro-->
<dl class="bad">&lt;dt&gt;We are doing this project using C#&lt;/dt&gt;<dd>Bad example - you know nothing about how the project will be done<br><br></dd></dl><dl class="good">&lt;dt&gt;
       <strong>Technologies&#58;</strong> WebAPI. The DI container is Structure Map. Entity Framework. Typescript. Angular.<br> <strong>Patterns&#58;</strong> Repository and Unit of Work (tied to Entity Framework to remove additional abstraction), IOC<br> <strong>ALM&#58;</strong> Scrum with 2-week sprints and a Definition of Done including StyleCop to green<br> <strong>ALM&#58;</strong> Continuous deployment to staging&lt;/dt&gt;<dd>Good example - this tells you a lot about the architecture and processes in a few words<br><br></dd></dl>
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


The decisions the team makes regarding these 3 areas, should be documented in \_Technologies.docx as per [https://rules.ssw.com.au/do-you-review-the-documentation](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=951ffbf9-4066-42f3-a9b7-e0d8603e728b).
