

---
uri: middle-tier---do-you-implement-business-logic-in-middle-tier
title: Middle Tier - Do you implement business logic in middle tier?
created: YYYY-11-DD 22:30:36
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>​Business logic/rules should be implemented in an object oriented language such as VB.NET and C#.&#160; This dramatically increases the adaptability, extensibility and maintainability of the application.<br></p><p>Implementing business logic in stored procedures have the disadvantage of being hard to test, debug and evolve, therefore, they should only implement basic data access logic.</p><p>With the exception of some very heavy data oriented operations, it is excusable to use stored procedures to carry out some logic for performance reasons.</p><p>Triggers are even more difficult as their behaviour is event based. &#160;It is okay to use triggers for non-functional/infrastructural features such as logging changes&#160;or maintain more complex relational integrity which cannot be enforced by a simple relationship.​​<br></p> </span>




