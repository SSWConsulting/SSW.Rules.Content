---
type: rule
archivedreason: 
title: General - Do you know object name should not be a reserved word?
guid: e500aff1-de87-4cac-88b1-d86c943920eb
uri: general-do-you-know-object-name-should-not-be-a-reserved-word
created: 2019-11-14T21:07:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- object-name-should-not-be-a-reserved-word

---

SQL Server reserves certain keywords for its exclusive use. It is not legal to include the reserved keywords in a Transact-SQL statement in any location except that defined by SQL Server. No objects in the database should be given a name that matches a reserved keyword. If such a name exists, the object must always be referred to using delimited identifiers. Although this method does allow for objects whose names are reserved words, it is recommended that you do not name any database objects with a name that is the same as a reserved word. In addition, the SQL-92 standard implemented by Microsoft SQL Server defines a list of reserved keywords.

<!--endintro-->

Avoid using SQL-92 reserved keywords for object names and identifiers, ie. User, Count, Group, etc. They can be used if joined with other words.
[What are reserved words for SQL Server 2000?](https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q931371)
[Why avoid reserved words and spaces in object names?](https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q1620415)
