---
type: rule
title: Do you use the repository pattern for data access?
uri: do-you-use-the-repository-pattern-for-data-access
created: 2012-03-30T05:16:01.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>The repository pattern is a great way to handle your data access layer and should be used wherever you have a need to retrieve data and turn it into domain objects.</p> </span>

<p>The advantages of using a repository pattern are&#58;</p>
<ul><li>Abstraction away from the detail of how objects are retrieved and saved</li>
<li>Domain objects are ignorant of persistence - persistence is handled completely by the repository</li>
<li>Testability of your code without having to hit the database (you can just mock the repository)</li>
<li>Reusability of data access code without having to worry about consistency</li></ul>
<p>Even better, by providing a consistent repository base class, you can get all your CRUD operations while avoiding any plumbing code.</p>
<p>See&#160;the <a href="http&#58;//blog.damianbrady.com.au/2012/03/07/a-generic-crud-repository-for-entity-framework/">&quot;A Generic CRUD Repository for Entity Framework&quot;</a>&#160;blog post by Damian Brady for an example of how to implement a repository pattern.</p>


