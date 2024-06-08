---
type: rule
archivedreason: 
title: Do you use the repository pattern for data access?
guid: 78d59d90-65f0-4cde-b2a9-858cc1cebe95
uri: do-you-use-the-repository-pattern-for-data-access
created: 2012-03-30T05:16:01.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

The repository pattern is a great way to handle your data access layer and should be used wherever you have a need to retrieve data and turn it into domain objects.

<!--endintro-->

The advantages of using a repository pattern are:

* Abstraction away from the detail of how objects are retrieved and saved
* Domain objects are ignorant of persistence - persistence is handled completely by the repository
* Testability of your code without having to hit the database (you can just mock the repository)
* Reusability of data access code without having to worry about consistency


Even better, by providing a consistent repository base class, you can get all your CRUD operations while avoiding any plumbing code.

Tip: Entity Framework provides a great abstraction for data access out of the box. See [Jason’s Clean Architecture with ASP.NET Core talk](https&#58;//tv.ssw.com/clean-architecture-with-asp-net-core-2-1-jason-taylor-ddd-sydney-2018/) for more information
