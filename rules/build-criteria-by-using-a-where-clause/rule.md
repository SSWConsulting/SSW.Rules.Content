---
type: rule
archivedreason: 
title: Do you build criteria by using a where clause?
guid: 5fecc770-d99e-4fb3-9b96-f1d4e6613e22
uri: build-criteria-by-using-a-where-clause
created: 2016-11-16T17:07:12.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-build-criteria-by-using-a-where-clause

---

It is very common to come up with ways to filter data. 
As an example, you could do it like this.



```
ClientSearch.aspx?Client.ClientID='ssw'&Client.CoName='S'
```



**Figure: Filtering Data**

This allows you to easily extract fields and values, but it only works for the fields you hard code. You could get around it by writing complex code to build a SQL query or ignore the ones that don't match.

But this gives exact matches. E.g.:

<!--endintro-->



```
ClientID=ssw
```



What if you want to give the ability to allow the user to be able to use a like e.g.



```
ClientID like '%ssw%'
```



Well then I could add something like



```
ClientSearch.aspx?Client.ClientID=ssw&Client.ClientID.SearchMode=OR
```



But why do this when a WHERE clause in SQL can do all this 
e.g.



```
ClientSearch.aspx?Where=Client.ClientID%20like%20'%ssw%'
```



**Figure: Similar matches**

Try this - [ClientSearch.aspx?Where=Client.ClientID%20like%20'%ssw%'](https&#58;//www.ssw.com.au/timeproonline/ClientSearch.aspx?Where=Client.ClientID%20like%20%27%ssw%%27)

The Pros for do this are:

* Quicker development time.
* SQL is very powerful - say I want to JOIN another table in the WHERE, I could use an IN statement and do a sub query - no extra code by the developer.
* Matches HTML syntax (named value pair) and as a developer you can get it easy. e.g.



```
Request.QueryString("Where")
```




The CONS:

* It shows the database schema to the users - users maybe should not see the structure of the database.
* Security - the where clause could show data we don't want users to see.
* Got to add a little extra code to avoid [SQL injection](https&#58;//www.ssw.com.au/ssw/KB/KB.asp?KBID=Q995992).
