---
uri: schema---do-you-avoid-using-user-schema-separation
title: Schema - Do you avoid using user-schema separation?
created: 2019-11-06 17:57:17
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>​​User-schema separation allows more flexibility​ by adding another level of naming and shifting ownership of database objects to the schema, not the user. So, is it worth doing? Unless you are working with a very large database (100+ tables), the answer is &quot;no&quot;. Most smaller databases have all objects with owner &quot;dbo&quot;, which is fine in most cases.​<br></p> </span>

<dl class="badImage"><dt>
      <img src="/PublishingImages/SQLDatabases_UserSchema_Bad.jpg" alt="SQLDatabases_UserSchema_Bad.jpg" />
   </dt><dd>​Figure&#58; Bad Example - AdventureWorks using user schema - instead, keep it simple and avoid using user schema unnecessarily</dd></dl><dl class="goodImage"><dt>
         <img src="/PublishingImages/SQLDatabases_UserSchema_Good.jpg" alt="SQLDatabases_UserSchema_Good.jpg" />​<br></dt><dd>Figure&#58; Good Example -​ Adventure works with user schema cleaned out. Much simpler and more readable​​<br></dd></dl>


