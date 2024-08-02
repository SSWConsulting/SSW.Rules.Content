---
type: rule
archivedreason:
title: Data Logic - Do you use SQL Ranking functions to rank your data?
guid: 6e392875-0d7f-4737-82a3-5e3b640c2e08
uri: use-sql-ranking-functions
created: 2023-12-13T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

SQL Ranking functions are introduced since SQL 2005. With these handy functions, you can easily rank your data.

<!--endintro-->

```sql
	SQL Snippet
	SELECT Rank() Over(Order A.BillableTimeTotal Desc) As Rank
```

::: good  
![Figure: Good example - Rank by SQL Ranking functions](RS_SQLRank.gif) 
:::
