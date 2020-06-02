

---
uri: general---do-you-know-object-name-should-not-be-a-reserved-word
title: General - Do you know object name should not be a reserved word?
created: YYYY-11-DD 21:07:23
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">SQL Server reserves certain keywords for its exclusive use. It is not legal to include the reserved keywords in a Transact-SQL statement in any location except that defined by SQL Server. No objects in the database should be given a name that matches a reserved keyword. If such a name exists, the object must always be referred to using delimited identifiers. Although this method does allow for objects whose names are reserved words, it is recommended that you do not name any database objects with a name that is the same as a reserved word. In addition, the SQL-92 standard implemented by Microsoft SQL Server defines a list of reserved keywords.​​​<br></p> </span>

<p>​Avoid using SQL-92 reserved keywords for object names and identifiers, ie. User, Count, Group, etc. They can be used if joined with other words.<br><a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q931371">What are reserved words for SQL Server 2000?</a><br><a href="https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q1620415">Why avoid reserved words and spaces in object names?</a><br></p>


