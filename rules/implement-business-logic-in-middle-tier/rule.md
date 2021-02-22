---
type: rule
archivedreason: 
title: Middle Tier - Do you implement business logic in middle tier?
guid: 66e5d862-74c1-440d-89df-3c27ab1d0485
uri: implement-business-logic-in-middle-tier
created: 2019-11-14T22:30:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- middle-tier-do-you-implement-business-logic-in-middle-tier

---

Business logic/rules should be implemented in an object oriented language such as VB.NET and C#.  This dramatically increases the adaptability, extensibility and maintainability of the application.

Implementing business logic in stored procedures have the disadvantage of being hard to test, debug and evolve, therefore, they should only implement basic data access logic.

With the exception of some very heavy data oriented operations, it is excusable to use stored procedures to carry out some logic for performance reasons.

Triggers are even more difficult as their behaviour is event based.  It is okay to use triggers for non-functional/infrastructural features such as logging changes or maintain more complex relational integrity which cannot be enforced by a simple relationship.

<!--endintro-->
