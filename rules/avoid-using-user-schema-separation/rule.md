---
seoDescription: Schema simplification boosts readability and maintainability, making it unnecessary to use user-schema separation unless dealing with very large databases.
type: rule
archivedreason:
title: Schema - Do you avoid using user-schema separation?
guid: bcc574f7-3dd5-45e1-8ec6-e37c434f5243
uri: avoid-using-user-schema-separation
created: 2019-11-06T17:57:17.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - schema-do-you-avoid-using-user-schema-separation
---

User-schema separation allows more flexibility by adding another level of naming and shifting ownership of database objects to the schema, not the user. So, is it worth doing? Unless you are working with a very large database (100+ tables), the answer is "no". Most smaller databases have all objects with owner "dbo", which is fine in most cases.

<!--endintro-->

::: bad  
![Figure: Bad Example - AdventureWorks using user schema - instead, keep it simple and avoid using user schema unnecessarily](SQLDatabases_UserSchema_Bad.jpg)  
:::

::: good  
![Figure: Good Example - Adventure works with user schema cleaned out. Much simpler and more readable](SQLDatabases_UserSchema_Good.jpg)  
:::
