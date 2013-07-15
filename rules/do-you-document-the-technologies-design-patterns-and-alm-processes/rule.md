---
type: rule
title: Do you document the technologies, design patterns and ALM processes?
uri: do-you-document-the-technologies-design-patterns-and-alm-processes
created: 2013-07-15T21:25:49.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>The technologies and design patterns form the architecture that is usually the stuff that is hard to change.</p><p>A pattern allows using a few words to a dev and he knows exactly what coding pattern you mean.</p><p>ALM is about refining the work processes.​</p> </span>

<dl class="bad"><dt>We are doing this project using C#​</dt><dd>Bad example - you know nothing about how the project will be done</dd></dl><dl class="good"><dt>
      <strong>Technologies&#58;</strong> MVC4. The DI container is Structure Map. Entity Framework. Typescript. Knockout.<br><strong>Patterns&#58;</strong> Repository and Unit of Work (tied to Entity Framework to remove additional abstraction), IOC<br><strong>ALM&#58;</strong> Scrum with 2 week sprints and a Definition of Done including StyleCop to green<br><strong>ALM&#58;</strong> Continuous deployment to staging</dt><dd>Good example - this tells you a lot about the architecture and processes in a few words</dd></dl><p>The important ones for most web projects&#58;</p><ol><li>Technologies&#58; MVC</li><li>Patterns&#58; Single responsibly - if it does more than one thing, then split it.<br> Eg. If it checks the weather and gets data out of the database, then split it&#160;</li><li>Patterns&#58; Inversion of control / dependency injection<br> Eg. If your controller needs to get data, then you inject the component that gets the data</li><li>Patterns&#58; Repository/Unit of Work - repository has standard methods for getting and saving data.&#160;The code calling the repository should not know where the data lives<br> Eg. A User Repository could be saving to Active Directory or CRM and it should not affect any other code<br> You may or may not choose to have an additional abstraction away from entity framework.</li><li>ALM&#58; Scrum - kind of a pattern for your process<br> A eg. Sprint Review every 2 weeks<br> Mostly a senior architect should be added for that 1 day each 2 weeks</li></ol><p>The decisions the team makes regarding these 3 areas, should be documented in _Technologies.docx as per&#160;<a href="/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouReviewTheDocumentation.aspx">http&#58;//rules.ssw.com.au/SoftwareDevelopment/RulestobetterArchitectureandCodeReview/Pages/DoYouReviewTheDocumentation.aspx</a>​.​</p> ​


