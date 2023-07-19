---
type: rule
title: Do you build criteria by using a where clause?
uri: build-criteria-by-using-a-where-clause
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-build-criteria-by-using-a-where-clause
created: 2016-11-16T17:07:12.000Z
archivedreason: null
guid: 5fecc770-d99e-4fb3-9b96-f1d4e6613e22
---

It is very common to come up with ways to filter data. 

As an example, you could do it like this:

```sql
ClientSearch.aspx?Client.ClientID='ssw'&Client.CoName='S'
```
**Figure: Filtering Data**

This allows you to easily extract fields and values, but it only works for the fields you hard code. You could get around it by writing complex code to build a SQL query or ignore the ones that don't match.

<!--endintro-->

But this gives exact matches. E.g.:

```sql
ClientID=ssw
```

What if you want to give the ability to allow the user to be able to use a like. E.g.:

```sql
ClientID like '%ssw%'
```

Well then I could add something like:

```sql
ClientSearch.aspx?Client.ClientID=ssw&Client.ClientID.SearchMode=OR
```

But why do this when a WHERE clause in SQL can do all this. E.g.:

```sql
ClientSearch.aspx?Where=Client.ClientID%20like%20'%ssw%'
```
**Figure: Similar matches**

The PROS for do this are:

* Quicker development time.
* SQL is very powerful - say I want to JOIN another table in the WHERE, I could use an IN statement and do a sub query - no extra code by the developer.
* Matches HTML syntax (named value pair) and as a developer you can get it easy. E.g.:

```cs
Request.QueryString("Where")
```

The Cons:

* It shows the database schema to the users - users maybe should not see the structure of the database.
* Security - the where clause could show data we don't want users to see.
* Got to add a little extra code to avoid [SQL injection](https://www.w3schools.com/sql/sql_injection.asp).
