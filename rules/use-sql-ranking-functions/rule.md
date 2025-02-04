---
seoDescription: Discover how to effectively rank your data with SQL ranking functions since SQL 2005.
type: rule
archivedreason:
title: Data Logic - Do you use SQL Ranking functions to rank your data?
guid: 9c85523b-824d-46cf-8398-5c1bdaae2a32
uri: use-sql-ranking-functions
created: 2024-08-02T14:59:33.0000000Z
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
